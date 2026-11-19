---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CzbdgZQI8tw.txt"
words: 354
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CzbdgZQI8tw

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CzbdgZQI8tw.txt` — حساب: airesearcherguy — إنستجرام — فيديو CzbdgZQI8tw

---

How to make GPTs using the API. Had a few people ask me about this. No worries, I got you. I know it seems really complicated through the API documentation, but it's not. This is the path of least resistance. Let me show you. First things first, you have to create an assistant and then attach files to it. And you can do all that with the API, but it's not necessary. They're all separate API endpoints and it's needlessly complex. Instead, just come to the playground here in platform.openai.com/playground and then create an assistant. Name it, give it its system prompt, and then upload all the files that you want it to be able to access. Done and done. Now in make.com, choose the make an API call GPT module, and then in the URL, put the threads/runs endpoint. You will need content type and OpenAI beta, and then it's really simple. In the JSON, you just reference the assistant ID, which will be right underneath the new assistant you just created in the playground. And then under messages, the role is always user right now, and then the content is your question. In this, I asked it a question specifically about the files that I had attached to it. And then you run the threads/thread ID/messages call, and here it'll list all the messages in that thread. It's listed in reverse chronological order, so the first message is the most relevant. And there you go. You can also use code interpreter via API like this. You just have to add the file IDs for any files that you want it to look at. So you have to upload the file to Make first, and then you have to make a regular HTTP request. And then here you just upload the file from the Make upload, and you'll get a file ID, and then you just reference the file ID in your prompt, and there you go. You'll have a GPT that can use code interpreter and access files that you upload to its database, all with no code. Hope that helps. Cheers.