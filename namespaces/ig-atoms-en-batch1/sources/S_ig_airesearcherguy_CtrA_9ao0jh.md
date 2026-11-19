---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CtrA_9ao0jh.txt"
words: 270
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CtrA_9ao0jh

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CtrA_9ao0jh.txt` — حساب: airesearcherguy — إنستجرام — فيديو CtrA_9ao0jh

---

So the truth is, I haven't been building any new bots the last couple of weeks because I've been refining a couple to use for my day job. One in particular I'm pretty proud of, the review analysis bot. Now I have a version of this in my bot bundle that does this with Google Maps business reviews, but the one I built for Signalitics uses Amazon reviews and it's pretty well refined. We're about to release the alpha test tool. Let's check it out. This thing's pretty epic. We have a form input that asks the user if they want to do it by ASIN or by keyword. If they do it by ASIN, then the bot only reads the reviews from that product. If they do it by keyword, then the bot does it from their top 10 competitors. We use an API call to grab the reviews. All of these aggregates those reviews into a block of text, turns it into a JSON, and then several API calls for different functions to our Anthropic Claude API turn that all into HTML and then make a PDF out of it and email it. Here's what that looks like, your AI review analysis with the I chose keyword. Then here's our branded PDF download. It includes sentiment analysis, most positive and negative trait, repeated keywords, repeated phrases, repeated themes, goals and values of the reviewers, demographic, if there is any demographic information to be gleaned from the reviews, challenges and pain points, product improvements. So this includes the purchase motivation and then suggestions for improvement. Pretty dope, I think.