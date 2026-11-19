---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C38OWR_LkiY.txt"
words: 549
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C38OWR_LkiY

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C38OWR_LkiY.txt` — حساب: airesearcherguy — إنستجرام — فيديو C38OWR_LkiY

---

I finally built a TikTok bot. This thing's pretty awesome. Check it out. This flow will find a viral video from either your favorite creator or through a keyword search, will transcribe that video, rewrite the script, and then produce a video with an AI avatar reading the new script. And it's fueled by this API I found on RapidAPI called the TikTok Scraper. Here's how it works. First, we call the TikTok Scraper and grab the videos. Each API call can grab up to 30 videos, so I have this repeat 30 times and it filters by the number of likes, but you can filter by the number of shares, the number of comments, whatever is an indicator of virality to you. It'll find the first video that meets that criteria. Cloud Convert here will then compress it because the video is usually too big. Then the cover GIF, which usually has some writing on it and some information about what the video is about, that's given to API Flash to grab a screenshot and that screenshot is given to GPT-4 Vision to be analyzed. Then all of that information is given to GPT-4. So GPT-4 is prompted to be a teleprompter scriptwriter. It's given the TikTok description, it's given the description of the cover, and it's given the video transcript. It's asked to rewrite the script. We tell GPT that this is a viral video, here's all the context, rewrite the script so that we can make our own version. Then we call D-ID to make an avatar video. After some time, the video is fetched, it's compressed again, then we upload it to Cloudinary. I'll explain why in a minute. Next, we have GPT write a new TikTok description. This is called a TikTok title. Then we ask GPT to create a short caption. And the reason is because I have an image that is just a little text box and I overlay that on the video. What this does is it takes the caption from GPT and overlays it on that text box on the video for the first five seconds. Then the video is generated, uploaded to Make, and then downloaded to Google Drive. Unfortunately, you can't hear it because a microphone is plugged into my phone, but this is the video. It's a D-ID Studio Avatar. You have to have a premium account to use them. It also doesn't have the subtitles because you have to have a paid account for that, but this is what you can do with D-ID now. The technology has actually gotten a lot better. This is about a minute-long video and it's basically a recreation of a viral video that we found on TikTok. That automation is one of the perks that you get when you join the Bot of the Month Club. This is our new premium Discord server. Costs 20 euros a month. You get access to the server, to all the knowledge that will be put in there. I'm dedicated to sharing new videos and stuff every week. And as a bonus, every month you'll get a new automation template. The new LinkedIn templates will be a part of that and then so will the TikTok. Hope to see you in the club. Cheers.