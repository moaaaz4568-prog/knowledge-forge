---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/algorithmswithpeter/DKBemUDS_RN.txt"
words: 171
account: algorithmswithpeter
lang: en
quality: transcript
---

# S_ig_algorithmswithpeter_DKBemUDS_RN

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/algorithmswithpeter/DKBemUDS_RN.txt` — حساب: algorithmswithpeter — إنستجرام — فيديو DKBemUDS_RN

---

Peter, how would you build a massive chat app like WhatsApp? I don't know where to start. Start with WebSockets. Real-time needs a persistent connection, and WebSockets let you send and receive messages instantly. Alright, what about backend? What's your stack? You could go with Go, Rust, or Java, but I will use Elixir with Phoenix framework. It runs on the Erlang VM, same thing WhatsApp uses. Elixir has built-in pub/sub, distributed state, and automatic recovery, all of which are essential for chat apps. And the database? Start with Postgres, it's fast and simple. Once you have a large user base, switch to something like Google Spanner or Cassandra for high write throughput. This all sounds very complex. What if I do not know anything about backend? Then use Firebase. It gives you WebSockets, auth, and a database all in one. Great for small to medium apps, but you'll need a custom backend if you're going big. Got it. WebSockets, Elixir for scale, Postgres to start, Spanner later. Clean and scalable.