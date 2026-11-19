---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DK2gakcx-pg.txt"
words: 385
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DK2gakcx-pg

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DK2gakcx-pg.txt` — حساب: chase.h.ai — إنستجرام — فيديو DK2gakcx-pg

---

Let me show you how simple it is to get Google's V03 video generation model, you know, the crazy one with the audio that costs you $250 a month on the ultra plan, inside of N8N without paying for that wild package. Now, how do we do this? Are we doing this through Google? No, we're using a third-party tool called Fal. AI, which you can see here. It's essentially a marketplace for all sorts of third-party APIs, including Google's V03. You're simply gonna go to that website, register and create an API key and add some funds to your account because while this is cheaper than $250 a month, it still has a steep price of $6 for an eight-second video, which while wild is pretty much par for the course when it comes to top-tier video quality. Now let's take a look at the HTTP request because it's gonna be the same for pretty much everybody. You're simply gonna have a URL that calls to Fal. AI. You're gonna have authorization for the headers. You're gonna have key, and then this is where you're gonna put your API key, space API key. And then at the bottom, you're just gonna do JSON prompts, and then this is where you put your prompt for the video. Next, you just need to wait. This is 10 minutes long, but it usually takes somewhere between three and five minutes to get the video. And then lastly, you just have a GET HTTP request. And in this case, this is what it's gonna look like. It's gonna be q. Fal. Run, and then you have the request, and then you have the request ID. This request ID will be generated from that first module. And then again, all you need to put there is the API key. And voila, you now have the ability to put Google V03 video generation inside of your N8N workflows. And so if you're looking for a deeper dive of how to actually use this inside of an automation and how to actually do all the nitty-gritty of it, or you just want the template, go ahead and check out the community in my profile. I got guides for all that, and it assumes you're non-technical, so it's pretty easy to follow.
