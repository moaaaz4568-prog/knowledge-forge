---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CpXnMspApJF.txt"
words: 219
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CpXnMspApJF

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CpXnMspApJF.txt` — حساب: airesearcherguy — إنستجرام — فيديو CpXnMspApJF

---

OpenAI just added GPT 3.5 Turbo to the API, otherwise known as ChatGPT. A lot of people have been asking, what is the difference? Let me show you. The first thing to note is GPT 3.5 Turbo's price is a tenth of that of DaVinci, and there's a reason for that. If you look at the code, you'll see it's essentially a conversation instead of a completion. You have user, assistant, user, and what that means is using this JSON, you can feed the output and the conversation results back to ChatGPT so that it remembers your conversation, which is not something that happened with text DaVinci 003. Here's what that looks like in make. Com. Use an HTTP module and you call chat/completions, and then you have your JSON, the messages here, the system message, and then the role user content, which is basically your prompt. Then you got to transform the answer into a JSON, and then you feed it right back through the API. And that way, ChatGPT has a memory of the conversation. You can keep this going over and over, and the reason why the cost is only a tenth is so that you can keep feeding it. So the prompt obviously gets longer and longer and longer, and this makes that cost effective.