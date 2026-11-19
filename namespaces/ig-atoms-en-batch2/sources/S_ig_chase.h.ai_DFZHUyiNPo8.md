---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DFZHUyiNPo8.txt"
words: 305
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DFZHUyiNPo8

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DFZHUyiNPo8.txt` — حساب: chase.h.ai — إنستجرام — فيديو DFZHUyiNPo8

---

So tons of people have been asking questions about how DeepSeek was actually trained, and the answer that keeps coming back is reinforcement learning. But what is reinforcement learning, and how did DeepSeek employ that to get the R1 model? Well, let's take a look. So what they did is they gave their model 144, 000 different coding and math questions. They then graded their answers to these questions, and they gave the model 64 attempts for each question. For each answer the DeepSeek model gave to that question, they compared its specific answer to the average answer to that question. Now, if that specific answer that DeepSeek gave was better than average, they then bumped up the probability that in the future DeepSeek would use that same line of reasoning. Now, if the answer was worse than average, the opposite occurred. They reduced the probability that those specific tokens would be used. What this did in the aggregate is it reinforced specific reasoning patterns that gave better answers. So that's reinforcement learning in a nutshell. You give the model some questions, you rate its answers. If they're better than average, you then bump up the probability it uses that line of reasoning in the future. And DeepSeek did this multiple times as it created DeepSeek R1, and they refer to this as GRPO, and you can read a lot more about it in its papers that they published. And remember, this reinforcement learning was just one piece of the DeepSeek training puzzle, but it's super interesting to look at because we just don't have this sort of information for stuff like ChatGPT. We don't really know how it was trained. We have some ideas, but nothing as concrete as this. And so if you like videos like this, make sure to follow my page.
