---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DMTFDYzx6g4.txt"
words: 566
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DMTFDYzx6g4

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DMTFDYzx6g4.txt` — حساب: chase.h.ai — إنستجرام — فيديو DMTFDYzx6g4

---

How much do my AI agents actually cost me? That's a question I get all the time. So I figured I would make a quick video breaking down the cost of the average AI agent that I use and sell. In this example, we're gonna be looking at this RAG AI agent that I recently sold a client for $5, 000, so you can get a good idea of what these things cost in the real world for people who are actually buying them. So first, let's talk about hosting costs. Where does this actually live? Well, in this case, we are using Hostinger as our third party self hosting platform, and month to month it's costing us $8. 50. Pretty cheap. Now, how much is the actual AI portion costing us, right? The OpenAI chat model that's running in the background. Well, in this case, we're using 4. 1 Mini, which again, very, very inexpensive. The input is $0. 40 per million tokens, and the output is $1. 60 per million tokens. Now, what's a token? Think of one word as one token. So every time I give this RAG agent a million words of input, right, a million word prompt, that's $0. 40. And for every million words it gives me as an answer, that's $1. 60. And obviously you're usually only doing prompts that are what, 50 to 100 words max, and maybe getting double the output. So very, very inexpensive. Now, I said this was a RAG agent, right? So we're actually taking a bunch of data and we're shoving it into a vector database inside of Supabase. How much does that cost to vectorize all the data and have all his documents sitting inside a third party database? Well, let's take a look. In this case, because we're using primarily just PDFs and Google Docs, even though there's hundreds of them, we are able to get away with the free tier on Supabase. So our entire vector database ecosystem is totally free at this point. And if we needed to upgrade, it would be $25 a month. So still not breaking the bank. Lastly, in our RAG system, we're using a re-ranker, which is Cohere, which means every single time a request is made to our database, we have a third party API jump in there, a third party program, and basically rank all the answers so we always get an accurate response. How much does that cost? Well, for Cohere, it's $2 per 1, 000 searches, which means for every single search it does, we're talking about one fifth of a penny. Very, very cheap. So let's take it all together. Cohere, less than a penny. Supabase, free for us right now. OpenAI, fractions of a penny. Hostinger, under 10 bucks a month. So you're looking at total cost to actually run this thing of what, easily under 20 bucks a month for a pretty robust RAG AI agent that this company is gonna be using. So as you can see, these AI solutions for small to medium sized businesses are actually relatively inexpensive, and so cost shouldn't be what stops you from using them. Now, if you're looking to get your hands on AI templates like this one, or just learn more about AI agents in general, just comment agent below, and I'll send them to you for free.
