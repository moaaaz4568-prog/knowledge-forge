---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DV14jB5Rplh.txt"
words: 295
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DV14jB5Rplh

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DV14jB5Rplh.txt` — حساب: chase.h.ai — إنستجرام — فيديو DV14jB5Rplh

---

We now have a one million token context window inside of Claude Opus 4. 6 and Sonnet 4. 6 for everybody. This is no longer hidden behind the API. But does this mean that it just got five times better, or are we dealing with context rot and this is kind of fake news? Well, to help us answer that question, Anthropic provided us with the long context retrieval benchmark. Essentially, they're asking Claude code to find specific things in a bunch of documents after they fill up the context window more and more and more and more. So over here you see it at 256k tokens, and on the right you see it at 1 million. Now first of all, Opus 4. 6 is better than everybody else, but when we're looking at it from a full context window point of view, we're still hitting 78. 3 with Opus 4. 6 compared to say Gemini 3. 1, which is at a 25. 9. However, with that being said, we are still going down into the right, so context rot still is something we want to worry about, but we're not seeing that sharp drop that we've seen in previous tests, especially the ones from like the Chroma study last summer. Now I wish we got some data from Anthropic looking at this from 128k token point of view, because for all we know this is at 99 and we already start to see a drop off. But from this graph it seems pretty linear, and I think the idea is, hey, we don't want to push it to 1 million context if we don't have to. But again, no huge drop off is a big deal, and this makes it a pretty solid update.
