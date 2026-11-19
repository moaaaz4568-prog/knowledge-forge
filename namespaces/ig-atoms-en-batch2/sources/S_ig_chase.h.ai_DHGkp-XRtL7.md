---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DHGkp-XRtL7.txt"
words: 458
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DHGkp-XRtL7

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DHGkp-XRtL7.txt` — حساب: chase.h.ai — إنستجرام — فيديو DHGkp-XRtL7

---

Let me show you how I research content ideas with my AI agent so you can copy it and do it yourself. So here's my AI agent, Jarvis. He acts as my personal assistant and he has the ability to do a ton of different stuff for me. He sends my email, sets up my calendar, can search the internet, a whole bunch of stuff. But one of the things I use him most for is for content research, and he does this by calling on a specific content tool I created, and it's actually really, really simple. And let me show you it. So this is the content research tool in its entirety. Now, every single tool your AI agent uses doesn't have to be some crazy thing. All that's happening here is I'm talking to Jarvis and I say, hey, I want to get some content ideas that are based on the latest AI news. And so that command, hey, I want the latest AI news and content ideas on that, it gets sent to this sub workflow, and then this goes to this HTTP request. All this HTTP request is, is it's sending that information to Perplexity. So I've now turned that command to my agent into a Perplexity search. Now the next thing that happens is it then goes here to the OpenAI message a model. So I get all that data from Perplexity and then it shoves it into OpenAI's GPT 4o. So basically I'm taking it Perplexity, shoving it into ChatGPT, and I tell ChatGPT, hey, you're gonna get all this Perplexity information. I want you to break it down into five potential content ideas. I want a potential title, a hook, and a three bullet outline. And then it just creates a document and dumps that into Google Drive. And this is really a very simple three step process. Perplexity, OpenAI, Google Drive. Now you could get way more complicated with how you do your research, but for this it's very simple. I just kind of want some ideas to bounce off of, and so this is how I do it with my AI agent. So this is something you could totally copy inside of N8N. It's super easy to do. The HTTP request, all the information is on Perplexity how to do it, and the rest of these modules are already pre-built. So again, this is just one tool of many for Jarvis. I created this also without any code. So if you're interested in creating stuff like that, just make sure to check out the community in my profile where it's all about creating guides for AI agents for like the non-technical user. So hope to see you there.
