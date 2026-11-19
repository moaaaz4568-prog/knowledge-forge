---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DW7qXkVt04l.txt"
words: 243
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DW7qXkVt04l

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DW7qXkVt04l.txt` — حساب: chase.h.ai — إنستجرام — فيديو DW7qXkVt04l

---

Anthropic just released Advisor Mode, which gives us better performance with Sonnet and Haiku at a cheaper cost. So the way the advisor strategy works is we have an agent that is executing tasks. It's either going to be Sonnet or Haiku, and it has Opus, the more powerful model, as the advisor. Opus comes up with a plan. This is like having Opus plan moment and having Sonnet actually generate the code. The difference is this is a little more sophisticated than that, because if the agent, say Sonnet or Haiku, starts working on Opus's plan, but it runs into a problem, well, it's going to go back to Opus and say, hey, here's the issue. What should we do? Opus then gives it a new updated plan for it to execute on. Now Opus also has full context of what's happening, but Opus doesn't make any tool calls, which is why we're able to keep the cost low even when we bring it in to advise. And because that advice is so much better than what Sonnet or IQ normally generate, we're able to get better performance, like you see on this graph, at a cheaper cost. So here, Sonnet with Opus Advisor scored 74. 8 versus 72. 1, and it was at $0. 96 versus $1. 09. This held up across multiple benchmarks, and you can use it both as an API or using slash advisor inside of Cloud Code.
