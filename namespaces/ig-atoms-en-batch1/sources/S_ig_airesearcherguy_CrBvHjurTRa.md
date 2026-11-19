---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CrBvHjurTRa.txt"
words: 274
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CrBvHjurTRa

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CrBvHjurTRa.txt` — حساب: airesearcherguy — إنستجرام — فيديو CrBvHjurTRa

---

I made a new bot. It'll take your YouTube video transcripts and use AI to generate content for other channels. Check it out. All right, so first thing to note, I found this amazing API from RapidAPI that gives you access to the YouTube API data. And here in make. Com, the very first module is an HTTP API request that pulls channel data. So this just pulls the videos from your channel so that it can grab the latest one. Here's a sleep module because you can't make more than one API call per second on the free tier. And then this API call grabs the subtitles from that latest video. Then we make sure we separate all those subtitles out and then put them all together in one block of text. And then here's the GPT module. The system prompt is, you are a content aggregator and distributor who takes transcripts, subtitles extracted from videos and rewords, summarizes, or expands upon the topic discussed. And then the user prompt is telling GPT to use the same tone and personality as the text in the subtitles and then summarize the transcript for a LinkedIn post. And then it posts it to LinkedIn. And I made one for Facebook as well and then one that also writes a Twitter thread. But let me show it to you in action. And there it is. This is the post complete with emojis and all, and it links back to the YouTube video. Also, the Instagram video avatar bot as well as this YouTube transcript bot are both in the AI Plus Automation Store. Check it out.