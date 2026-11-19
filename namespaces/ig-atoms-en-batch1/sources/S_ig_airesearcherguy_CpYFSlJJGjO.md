---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CpYFSlJJGjO.txt"
words: 208
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CpYFSlJJGjO

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CpYFSlJJGjO.txt` — حساب: airesearcherguy — إنستجرام — فيديو CpYFSlJJGjO

---

All right, I know everybody's really excited about using the new ChatGPT API, specifically for its conversational chat capabilities. The problem is that's really hard to do in no code. Here are the challenges that I've discovered when using a platform like Make. First, you have to send the data back to the API, but then the question becomes, well, how do you trigger it again? In Make, you would have to create a series of triggers, but technically every trigger would start a whole new conversation. So then you'd have to figure out how to pass the data from one scenario to another. But then the question becomes, well, how do you know how long to do that for until you start a new conversation? So here is the solution that I'm working towards in my head. Create a chat fuel chat flow and then have it do question answer trigger, question answer trigger. Obviously, once the conversation's over, it won't trip the next trigger. And then the responses can be saved in a data store so that every new trigger, which is technically a new make. Com flow, can reference the previous conversation. So far, those are the only solutions that I've come up with. Cheers.