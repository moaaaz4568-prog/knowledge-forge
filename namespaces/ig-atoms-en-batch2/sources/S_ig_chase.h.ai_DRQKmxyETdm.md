---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DRQKmxyETdm.txt"
words: 416
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DRQKmxyETdm

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DRQKmxyETdm.txt` — حساب: chase.h.ai — إنستجرام — فيديو DRQKmxyETdm

---

These AI influencers are lying to you about their voice agents. If you watch a video of someone's AI voice agent and they show you an end-to-end backend that looks like this, I can promise you the demo calls that you are watching are not real. Now the voices are real, the responses are real, but what isn't real is the latency. If you watch those videos, when they ask their AI agent to do something and when it responds to them, you will notice they cut the clip every single time. Why is that? Well, it's because they have a backend that looks like this, and this is not how you should set up your voice agent backends if you want low latency. Because what happens is the response or the call from the user goes to this webhook. That's me telling the voice agent, hey, I want you to do X, right? Your receptionist, I want you to check appointment availability. Well, that then is gonna go into this AI agent, which then takes all that information, thinks about it, goes down to the tool call, checks availability, it comes back up to the AI agent, it thinks about it again, it makes its response, which then goes back to the voice agent via this webhook. Notice all that back and forth. That adds a ton of latency. And these voice agent demos you're seeing that have a busted backend like this are in reality taking six, seven, eight, nine, ten seconds to actually respond. Now I say that as someone who has built real voice agents and done full videos with the actual latency. A setup like this with a very tight tool calling architecture, aka the webhook comes in, the response is made, the tool is called straight to the webhook, no intermediary AI agent in the mix, still takes one and a half to three seconds. There is still a delay right now when it comes to these voice agents. So understand when you're watching somebody's videos and they show you this and you notice they're cutting their clips, they're not showing you the real deal. So be careful. Now if you wanna learn how to make voice agents that are actually as low latency as you can get, make sure to check out mine. I have them on YouTube and in my community, I give away the templates for free. So check them out there, the links in my profile.
