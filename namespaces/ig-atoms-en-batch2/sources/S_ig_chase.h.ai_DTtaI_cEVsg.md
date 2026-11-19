---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DTtaI_cEVsg.txt"
words: 491
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DTtaI_cEVsg

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DTtaI_cEVsg.txt` — حساب: chase.h.ai — إنستجرام — فيديو DTtaI_cEVsg

---

So this technical paper just came out a couple weeks ago from MIT, and they're claiming that they've essentially solved the context window issue with their new recursive language model system. So for normal AI systems, you're limited by the context window, and in this study they used GPT-5, which has a context window of 262, 000 tokens. Now, as you know, the closer you bump up against that context window, the worse their performance gets. You can see that in this graph right here. They gave it a couple tests. The more input it gets, the worse it does, right? That's why you see everything sloping down into the right. Now, the big thing with this study is they brought in the RLM, the recursive language model framework. Now if we zoom in here, we can see those two same tests depicted here. Now two things to note. One, notice it goes past the context window of 272, and it goes all the way to a million. And the effectiveness is way higher. If we look at it here on the olong pairs, it scored about a 50. Over here with the base model, what did we get? It's at almost zero. Now here's some more tests to look at. So we have GPT-5, you have the base model right here, and then we have RLM. And you can see they used a test called browse comp, which uses 11 million tokens, right? They're essentially throwing 100 documents at it and asking for questions about the documents. The base model can't even handle it, right? Too much context. Well, the RLM scores a 91. Wild stuff. How is it actually doing this? The answer is with recursive language models, which is what you see right here. Now on my YouTube, I do a full deep dive and break this down piece by piece so you can really understand it. So check that out. But to quickly summarize it, instead of taking a giant million token document and shoving it into ChatGPT because you can't do that because of the context window, instead they have it inside of a Python environment and they never feed that document to ChatGPT exactly. Instead, what they essentially do is they chop up that document into chunks and it figures out how to chop it up using code, and then it sends those chunks to recursive large language models that the main GPT agent has spawned, right? So think of little mini ChatGPTs. In this case, they use GPT-5 mini. It then processes those chunks and sends the answer to the primary LLM. That's how they do it. So like I said, really interesting stuff. If you want to know more about this paper, just search up recursive language models and it'll be the technical paper that pops up. And again, I did a deep dive on my YouTube as well, so check that out.
