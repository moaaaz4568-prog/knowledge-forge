---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DFYcxt8R7cJ.txt"
words: 295
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DFYcxt8R7cJ

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DFYcxt8R7cJ.txt` — حساب: chase.h.ai — إنستجرام — فيديو DFYcxt8R7cJ

---

It's impossible. Tony Stark was able to build this in a cave with a bunch of scraps. So DeepSeek had a little more than a box of scraps when they created their new R1 model. But how did they actually train it? Well, let's take a look and break it down step by step. So here's how they went from DeepSeek V3 to DeepSeek R1, and I got most of this information from the papers they released. So step one was fine tuning. So they took the V3 model and they fed it thousands and thousands of chain of thought problems. Now, chain of thought is any sort of problem you give to an LLM that requires multiple steps to reach your desired output. So that allows the model to flex its reasoning muscles. Now the second phase was reinforcement learning, and this was the big thing that came out of the DeepSeek papers. DeepSeek referred to it as GRPO, and essentially it's a rules-based system that rewards good reasoning. So the way this actually worked is they fed their model 144, 000 different math and coding problems. Now for each of those 144, 000 problems, they gave their model 64 attempts to solve it. Every single attempt was graded based on how correct it was. And then they took every single individual score and they compared it to the mean of scores, the average score for that particular problem. And if that score, when compared to the mean, was better than the mean, then they increased the probability of the model using that line of reasoning to achieve that output. And the opposite was true. If it did worse than the mean, then they reduced the probability that the model would give you that.
