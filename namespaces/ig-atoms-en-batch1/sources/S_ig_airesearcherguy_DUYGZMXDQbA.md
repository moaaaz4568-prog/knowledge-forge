---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/DUYGZMXDQbA.txt"
words: 464
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_DUYGZMXDQbA

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/DUYGZMXDQbA.txt` — حساب: airesearcherguy — إنستجرام — فيديو DUYGZMXDQbA

---

So currently my favorite MCP is one that I built, which makes me super proud. So true story, how it came about was I'm in a WhatsApp group that talks about AI, and there were a couple of people in there that were complaining about agent memory. A lot of enterprise solutions offer a free tier, but either they are very complicated to set up or they're really limited because obviously they want you to take advantage of their premium offerings. And then the free stuff, it seems like all it really does is it takes memories or sessions and then appends them to a super long list that ends up either taking up way too much context or way too much space on your computer. Well, I've actually been thinking about this for about a year and a half now, how to make AI agents forget in a helpful way. So I built Arunla. Now first, Arunla is totally local. Obviously the LLM that you're talking to, the agent, probably won't be, it's probably Claude Code or Cursor or whatever, but the memory and knowledge extraction, everything is local. So how Arunla works is you can input a document, but it's mainly built around chat snippets, and it'll take these memories and it uses a tiny language model, very, very small, that's only job is to extract entities, and it creates a small knowledge graph. So it creates these things called triples, which is person, place or thing, action, person, place or thing that the action impacts, and it saves that on your computer. Every memory has a score, and this score slowly goes down over time, and the only way to replenish that score is to recall the memory. This way, Arunla can sort useful memories and unuseful memories, and the most unuseful memories, the ones that never get recalled over a period of time, will self-prune. They'll delete themselves. That way, the file never gets too big. And the way memories are recalled is through a hybrid search, searches text and knowledge graph traversal. That way, the memories are relevant. So yeah, that's Arunla. You can use it in your CLI, you can use it by API. It does have a app interface, but that really is only for uploading a document or adding memories manually if you want to. But for the most part, the most useful way to use it is MCP. Right now it's free. There is a pro tier if you want cross-device sync. So if you like it a lot and you want to be able to use it in multiple instances, the pro tier lets you do that. Anyway, go to aiplusautomation. Com/arunla and download it for free. I hope you find it useful. Cheers.