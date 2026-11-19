---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CwQL1mgI1RC.txt"
words: 280
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CwQL1mgI1RC

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CwQL1mgI1RC.txt` — حساب: airesearcherguy — إنستجرام — فيديو CwQL1mgI1RC

---

All right, here's a quick GoHighLevel API automation hack. So one of the challenges of automating with GoHighLevel's version two of their API is that you have to use an authorization token in the API calls. The authorization token only lasts 24 hours. In order to initially generate it, however, you have to go to some confusing URL, that one right there, and that'll generate a code that you use in the token generation API call. But you have to click a button on the page before you can generate that code, and I don't know how to automate that in Make. However, I figured out that you can use the refresh token, which lasts up to a year, to refresh both the authorization token and the new refresh token. And you can automate that, so let me show you how I did it. It's actually pretty simple. I have this running every 23 hours and 59 minutes, and the first module gets a record from a data store. So I created a data store that stores both the authorization token and the refresh token. And then this HTTP request calls the token creation API endpoint, and it uses the refresh token, which is the reason why we had to get the record from the data store first. So it's going to grab the latest refresh token, and then using that refresh token, it generates a new refresh token and a new access token. So anytime I want to run any scenarios using GoHighLevel's API, the access token should always be valid because it's constantly refreshing once a day using the latest refresh token. All right, hope that helps. Cheers.