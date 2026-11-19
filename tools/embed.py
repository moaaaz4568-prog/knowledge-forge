#!/usr/bin/env python3
"""embed.py — dense embedding as an optional, degradable rung (v2 §4.2).

The core loop (gates + BM25 + eval) is stdlib-only. Dense retrieval is an
ADDITION: when onnxruntime / a downloaded model / sqlite-vec are missing,
everything here raises EmbeddingUnavailable and callers degrade to
keyword-only — and say so in the answer receipt (idea 14). Never silent.

Models are local ONNX int8 exports (no torch, no paid API):
    e5-small   Xenova/multilingual-e5-small   118 MB, 384-dim, 512 tokens
    e5-large   Xenova/multilingual-e5-large   562 MB, 1024-dim, 512 tokens
    bge-m3     Xenova/bge-m3                  570 MB, 1024-dim
    gte-reranker (cross-encoder)              341 MB
Model + dimension are PINNED per namespace in config.yml; mixing two dims
in one store corrupts it, so the store refuses (§4.2 hard rules).

Vectors live in <kb>/.kforge/vec.db (sqlite-vec), separate from the BM25
index.db so a pure-stdlib clone never touches a database it cannot open.

Usage:
    python tools/embed.py info
    python tools/embed.py download e5-small
    python tools/embed.py index --namespace <n>     # sync vec.db to index.db
    python tools/embed.py query "..." --namespace <n>  # dense search debug
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MODELS_ROOT = os.environ.get('KF_MODELS')  # or auto-detected below
DEFAULT_DIRS = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.models'),
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'work', 'models'),
]

# repo -> (files to fetch, dim, prefix pair, max_len)
MODELS = {
    'e5-small': dict(repo='Xenova/multilingual-e5-small', dim=384, max_len=512,
                     prefixes=('query: ', 'passage: ')),
    'e5-large': dict(repo='Xenova/multilingual-e5-large', dim=1024, max_len=512,
                     prefixes=('query: ', 'passage: ')),
    'bge-m3': dict(repo='Xenova/bge-m3', dim=1024, max_len=512,
                   prefixes=('', '')),
}
RERANKERS = {
    'gte-reranker': dict(repo='onnx-community/gte-multilingual-reranker-base'),
}


class EmbeddingUnavailable(Exception):
    """The dense rung is off — degrade to keyword (and say so)."""


def _models_root():
    if MODELS_ROOT and os.path.isdir(MODELS_ROOT):
        return MODELS_ROOT
    for d in DEFAULT_DIRS:
        if os.path.isdir(d):
            return d
    return DEFAULT_DIRS[0]


def model_dir(name):
    return os.path.join(_models_root(), name)


def model_path(name):
    d = model_dir(name)
    if not os.path.isfile(os.path.join(d, 'onnx', 'model_quantized.onnx')):
        return None
    if name not in MODELS and name not in RERANKERS:
        return None
    return d


def import_onnx():
    try:
        import numpy
        import onnxruntime
        from tokenizers import Tokenizer
        return numpy, onnxruntime, Tokenizer
    except ImportError as e:
        raise EmbeddingUnavailable('onnx stack not installed (%s)' % e)


def import_sqlite_vec():
    try:
        import sqlite_vec
        return sqlite_vec
    except ImportError as e:
        raise EmbeddingUnavailable('sqlite-vec not installed (%s)' % e)


def download(name, root=None):
    """Fetch a model from Hugging Face (curl, no deps). ~118–570 MB."""
    spec = MODELS.get(name) or RERANKERS.get(name)
    if not spec:
        raise SystemExit('unknown model: %s (have: %s)' %
                         (name, ', '.join(sorted(MODELS) + sorted(RERANKERS))))
    d = os.path.join(root, name) if root else model_dir(name)
    os.makedirs(os.path.join(d, 'onnx'), exist_ok=True)
    repo = spec['repo']
    files = ['tokenizer.json', 'config.json', 'onnx/model_quantized.onnx']
    for f in files:
        dst = os.path.join(d, f)
        if os.path.isfile(dst) and os.path.getsize(dst) > 0:
            print('have   %s' % dst)
            continue
        url = 'https://huggingface.co/%s/resolve/main/%s' % (repo, f)
        print('fetch  %s' % url)
        r = subprocess.run(['curl', '-sL', '--retry', '3', '-o', dst, url])
        if r.returncode != 0 or not os.path.isfile(dst) or \
                os.path.getsize(dst) < 1000:
            raise SystemExit('download failed: %s' % url)
    print('done   %s (%.0f MB)' % (d, sum(
        os.path.getsize(os.path.join(dp, fn))
        for dp, _dn, fns in os.walk(d) for fn in fns) / 1e6))


class Embedder:
    """One local ONNX embedding model, pinned name + dim."""

    def __init__(self, name):
        if name not in MODELS:
            raise EmbeddingUnavailable('unknown embedding model: %r' % name)
        self.name = name
        self.spec = MODELS[name]
        d = model_path(name)
        if not d:
            raise EmbeddingUnavailable(
                'model %r not downloaded — run: python tools/embed.py download %s'
                % (name, name))
        numpy, onnxruntime, Tokenizer = import_onnx()
        self.np = numpy
        self.tok = Tokenizer.from_file(os.path.join(d, 'tokenizer.json'))
        opts = onnxruntime.SessionOptions()
        opts.intra_op_num_threads = max(1, (os.cpu_count() or 2))
        opts.inter_op_num_threads = 1
        self.sess = onnxruntime.InferenceSession(
            os.path.join(d, 'onnx', 'model_quantized.onnx'),
            providers=['CPUExecutionProvider'], sess_options=opts)
        self.max_len = self.spec['max_len']
        self.dim = self.spec['dim']
        self.input_names = {i.name for i in self.sess.get_inputs()}

    def _encode(self, texts, kind):
        q_p, d_p = self.spec['prefixes']
        pre = q_p if kind == 'query' else d_p
        enc = self.tok.encode_batch([pre + t for t in texts])
        L = self.max_len
        ids = self.np.array(
            [e.ids[:L] + [0] * max(0, L - len(e.ids)) for e in enc],
            dtype=self.np.int64)
        mask = self.np.array(
            [[1] * min(len(e.ids), L) + [0] * max(0, L - len(e.ids)) for e in enc],
            dtype=self.np.int64)
        feed = {'input_ids': ids, 'attention_mask': mask}
        if 'token_type_ids' in self.input_names:
            feed['token_type_ids'] = self.np.zeros_like(ids)
        out = self.sess.run(None, feed)
        hidden = out[0]
        mask_f = mask[:, :, None].astype(self.np.float32)
        emb = (hidden * mask_f).sum(1) / self.np.clip(mask_f.sum(1), 1e-9, None)
        emb = emb / self.np.clip(
            self.np.linalg.norm(emb, axis=1, keepdims=True), 1e-9, None)
        return emb.astype(self.np.float32)

    def embed_passages(self, texts):
        return self._encode(texts, 'passage')

    def embed_query(self, text):
        return self._encode([text], 'query')[0]


class Reranker:
    """Cross-encoder reranker over (query, passage) pairs. Optional rung."""

    def __init__(self, name='gte-reranker'):
        if name not in RERANKERS:
            raise EmbeddingUnavailable('unknown reranker: %r' % name)
        d = model_path(name)
        if not d:
            raise EmbeddingUnavailable(
                'reranker %r not downloaded — run: python tools/embed.py download %s'
                % (name, name))
        numpy, onnxruntime, Tokenizer = import_onnx()
        self.np = numpy
        self.tok = Tokenizer.from_file(os.path.join(d, 'tokenizer.json'))
        opts = onnxruntime.SessionOptions()
        opts.intra_op_num_threads = max(1, (os.cpu_count() or 2))
        self.sess = onnxruntime.InferenceSession(
            os.path.join(d, 'onnx', 'model_quantized.onnx'),
            providers=['CPUExecutionProvider'], sess_options=opts)
        self.max_len = 512
        self.name = name
        # pair input: some rerankers take a single "text" pair tokenized with
        # special tokens, others take text_pair — detect from the graph.
        names = [i.name for i in self.sess.get_inputs()]
        self.pair_mode = 'text_pair' in names or 'token_type_ids' in names

    def score(self, query, passages):
        """Higher = more relevant. Returns float list, len == len(passages)."""
        np_ = self.np
        L = self.max_len
        q = self.tok.encode(query)
        scores = []
        # serial: reranking runs on <=30 candidates; serial keeps RAM flat
        for p in passages:
            pp = self.tok.encode(p)
            ids = q.ids[:L // 2] + pp.ids[:L // 2]
            ids = ids[:L] + [0] * max(0, L - len(ids))
            mask = [1] * min(len(q.ids) + len(pp.ids), L) + \
                   [0] * max(0, L - min(len(q.ids) + len(pp.ids), L))
            feed = {'input_ids': np_.array([ids], dtype=np_.int64),
                    'attention_mask': np_.array([mask], dtype=np_.int64)}
            if self.pair_mode:
                types = [0] * min(len(q.ids), L // 2) + \
                        [1] * min(len(pp.ids), L // 2)
                types = (types + [0] * L)[:L]
                feed['token_type_ids'] = np_.array([types], dtype=np_.int64)
            try:
                out = self.sess.run(None, feed)
                logits = out[0]
                # logits shape [1,1] (regression head) — take the scalar
                scores.append(float(logits.reshape(-1)[0]))
            except Exception as e:
                raise EmbeddingUnavailable('reranker failed: %s' % e)
        return scores


_EMBEDDER = None


def get_embedder(name):
    """Process-wide cache: one model, one load (RAM lives once)."""
    global _EMBEDDER
    if _EMBEDDER is None or _EMBEDDER.name != name:
        _EMBEDDER = Embedder(name)
    return _EMBEDDER


_RERANKER = None


def get_reranker():
    global _RERANKER
    if _RERANKER is None:
        _RERANKER = Reranker()
    return _RERANKER


# ---------- the dense store (vec.db, separate from index.db) ----------

def vec_db_path(kb):
    return os.path.join(kb, '.kforge', 'vec.db')


def open_vec_store(kb, create=False):
    """Open the vector store. Returns (conn, meta) or (None, reason)."""
    if not os.path.isfile(vec_db_path(kb)):
        if not create:
            return None, 'no vec.db (dense index not built for this namespace)'
    try:
        import sqlite3
        import struct
        sqlite_vec = import_sqlite_vec()
        conn = sqlite3.connect(vec_db_path(kb))
        conn.enable_load_extension(True)
        sqlite_vec.load(conn)
        conn.enable_load_extension(False)
        conn.execute('CREATE TABLE IF NOT EXISTS vmeta(key TEXT PRIMARY KEY, value TEXT)')
        meta = {k: v for k, v in conn.execute('SELECT key, value FROM vmeta')}
        return conn, meta
    except EmbeddingUnavailable as e:
        return None, str(e)
    except Exception as e:
        return None, 'vec.db unreadable: %s' % e


def sync_index(kb, model_name, batch=8, force=False):
    """Make vec.db match index.db. Incremental: only new/changed chunks embed.

    Chunk identity = (path, heading, sha1(text)) so a BM25 rebuild that
    renumbers chunk ids does not re-embed unchanged text.
    """
    import hashlib
    import sqlite3
    sqlite_vec = import_sqlite_vec()
    if model_name not in MODELS:
        raise EmbeddingUnavailable('unknown model %r' % model_name)
    dim = MODELS[model_name]['dim']
    emb = get_embedder(model_name)

    idx = sqlite3.connect(os.path.join(kb, '.kforge', 'index.db'))
    idx.row_factory = sqlite3.Row
    try:
        chunks = idx.execute(
            'SELECT id, path, heading, text FROM chunks ORDER BY id').fetchall()
    except sqlite3.Error:
        raise EmbeddingUnavailable('index.db missing — run retriever.py index first')

    os.makedirs(os.path.join(kb, '.kforge'), exist_ok=True)
    conn = sqlite3.connect(vec_db_path(kb))
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    conn.execute('CREATE TABLE IF NOT EXISTS vmeta(key TEXT PRIMARY KEY, value TEXT)')

    meta = {k: v for k, v in conn.execute('SELECT key, value FROM vmeta')}
    if force:
        conn.execute('DROP TABLE IF EXISTS vec_chunks')
        conn.execute('DROP TABLE IF EXISTS vec_map')
        meta = {}
    if meta.get('model') and (meta.get('model') != model_name or
                              meta.get('dim') != str(dim)):
        # §4.2: never mix dims — a model change requires a full rebuild
        conn.execute('DROP TABLE IF EXISTS vec_chunks')
        conn.execute('DROP TABLE IF EXISTS vec_map')
        meta = {}
    conn.execute('CREATE VIRTUAL TABLE IF NOT EXISTS vec_chunks USING vec0('
                 'embedding float[%d])' % dim)
    conn.execute('CREATE TABLE IF NOT EXISTS vec_map('
                 'key TEXT PRIMARY KEY, chunk_id INTEGER)')

    want = {}
    for c in chunks:
        key = '%s|%s|%s' % (c['path'], c['heading'],
                            hashlib.sha1(c['text'].encode()).hexdigest()[:12])
        want[key] = c['id']
    have = {k: cid for k, cid in conn.execute('SELECT key, chunk_id FROM vec_map')}

    t0 = time.time()
    by_id = {c['id']: c for c in chunks}
    n_new, n_moved = 0, 0
    # delete rows for chunks that vanished (deleted files / changed text)
    for key in set(have) - set(want):
        conn.execute('DELETE FROM vec_chunks WHERE rowid=?', (have[key],))
        conn.execute('DELETE FROM vec_map WHERE key=?', (key,))
    # re-point rows whose chunk id changed but text is identical
    for key, new_id in want.items():
        if key in have and have[key] != new_id:
            conn.execute('DELETE FROM vec_chunks WHERE rowid=?', (have[key],))
            conn.execute('UPDATE vec_map SET chunk_id=? WHERE key=?', (new_id, key))
            have[key] = new_id
            n_moved += 1
    # embed the genuinely new
    todo = [(key, cid) for key, cid in want.items() if key not in have]
    for i in range(0, len(todo), batch):
        part = todo[i:i + batch]
        texts = []
        for key, cid in part:
            c = by_id[cid]
            texts.append(c['text'])
        vecs = emb.embed_passages(texts)
        for (key, cid), v in zip(part, vecs):
            conn.execute('INSERT INTO vec_chunks(rowid, embedding) '
                         'VALUES (?, vec_f32(?))', (cid, v.tobytes()))
            conn.execute('INSERT OR REPLACE INTO vec_map VALUES (?, ?)', (key, cid))
        n_new += len(part)
        conn.commit()
        print('  embedded %d/%d' % (min(i + batch, len(todo)), len(todo)),
              flush=True)

    conn.execute('INSERT OR REPLACE INTO vmeta VALUES (?,?)', ('model', model_name))
    conn.execute('INSERT OR REPLACE INTO vmeta VALUES (?,?)', ('dim', str(dim)))
    conn.execute('INSERT OR REPLACE INTO vmeta VALUES (?,?)',
                 ('built_at', time.strftime('%Y-%m-%dT%H:%M:%S')))
    conn.commit()
    dt = time.time() - t0
    n_vec = conn.execute('SELECT COUNT(*) FROM vec_map').fetchone()[0]
    conn.close()
    idx.close()
    return {'model': model_name, 'dim': dim, 'chunks_in_index': len(chunks),
            'embedded_new': n_new, 'repointed': n_moved, 'vectors': n_vec,
            'seconds': round(dt, 1), 'ms_per_chunk': round(dt * 1000 / max(1, n_new), 0)}


def dense_search(kb, query, top_n=30):
    """Pure dense search against vec.db. Returns [(chunk_id, cosine)] or raises."""
    conn, meta = open_vec_store(kb)
    if conn is None:
        raise EmbeddingUnavailable(meta)
    try:
        model = meta.get('model')
        if not model:
            raise EmbeddingUnavailable('vec.db has no model recorded')
        emb = get_embedder(model)
        import sqlite3
        qv = emb.embed_query(query)
        rows = conn.execute(
            'SELECT rowid, distance FROM vec_chunks '
            'WHERE embedding MATCH vec_f32(?) AND k=?',
            (qv.tobytes(), top_n)).fetchall()
        # vec0 'distance' is L2 by default; for unit vectors L2^2 = 2-2cos,
        # monotone in cosine, so ranking is correct either way
        return [(r[0], r[1]) for r in rows], model
    finally:
        conn.close()


def main(argv=None):
    ap = argparse.ArgumentParser(description='dense embedding rung (optional)')
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('info', help='what is available on this machine')
    d = sub.add_parser('download', help='fetch a model from Hugging Face')
    d.add_argument('model', choices=sorted(MODELS) + sorted(RERANKERS))
    i = sub.add_parser('index', help='sync <kb>/.kforge/vec.db to index.db')
    i.add_argument('--namespace')
    i.add_argument('--model', default=None, help='default: config embedding.model')
    i.add_argument('--force', action='store_true', help='full rebuild')
    q = sub.add_parser('query', help='debug: dense search a namespace')
    q.add_argument('text')
    q.add_argument('--namespace')
    q.add_argument('-k', type=int, default=5)
    args = ap.parse_args(argv)

    if args.cmd == 'info':
        print('models root : %s' % _models_root())
        for name in sorted(MODELS) + sorted(RERANKERS):
            p = model_path(name)
            size = ''
            if p:
                size = ' (%.0f MB)' % (sum(
                    os.path.getsize(os.path.join(dp, fn))
                    for dp, _dn, fns in os.walk(p) for fn in fns) / 1e6)
            print('  %-14s %s%s' % (name, 'READY' if p else 'not downloaded', size))
        try:
            import_onnx()
            print('onnx stack  : installed')
        except EmbeddingUnavailable as e:
            print('onnx stack  : MISSING (%s)' % e)
        try:
            import_sqlite_vec()
            print('sqlite-vec  : installed')
        except EmbeddingUnavailable as e:
            print('sqlite-vec  : MISSING (%s)' % e)
        return 0

    if args.cmd == 'download':
        download(args.model)
        return 0

    from kforge import paths
    root = paths.repo_root()
    kb = paths.find_kb(root, args.namespace) if args.namespace else None
    if kb is None:
        # fall back: cwd is a KB?
        if os.path.isfile(os.path.join(os.getcwd(), 'config.yml')):
            kb = os.getcwd()
        else:
            print('namespace not found (have: %s)' %
                  ', '.join(os.path.basename(d) for d in paths.kb_dirs(root)),
                  file=sys.stderr)
            return 1

    if args.cmd == 'index':
        cfg = paths.load_cfg(kb)
        model = args.model or (cfg.get('embedding') or {}).get('model')
        if not model:
            print('no embedding.model in %s config.yml and no --model given' % kb,
                  file=sys.stderr)
            return 1
        r = sync_index(kb, model, force=args.force)
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0

    if args.cmd == 'query':
        try:
            hits, model = dense_search(kb, args.text, args.k)
        except EmbeddingUnavailable as e:
            print('dense unavailable: %s' % e, file=sys.stderr)
            return 1
        import sqlite3
        conn = sqlite3.connect(os.path.join(kb, '.kforge', 'index.db'))
        conn.row_factory = sqlite3.Row
        for cid, dist in hits:
            c = conn.execute('SELECT path, heading FROM chunks WHERE id=?',
                             (cid,)).fetchone()
            print('%.4f  %s  # %s' % (dist, c['path'], c['heading']))
        return 0


if __name__ == '__main__':
    sys.exit(main())
