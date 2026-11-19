---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DH9lMz6xgTE.txt"
words: 520
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DH9lMz6xgTE

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DH9lMz6xgTE.txt` — حساب: chase.h.ai — إنستجرام — فيديو DH9lMz6xgTE

---

Here's a 60 second guide on how to set up MCP for your N8N server so you can start using the latest tech for your AI agents. Okay, so step one, you need to be self hosting. I suggest either DigitalOcean or Render guides for that in my profile. Next, you're gonna go to N8N, you're gonna go to settings. So come to the bottom left, you're gonna go to community nodes, and you're gonna go to install, and you're gonna put in N8N nodes MCP and install it. So here's the one tricky part. I suggest going to the N8N MCP client GitHub for kind of more in depth directions, but basically you got to go into your environment variables. If that's something like DigitalOcean, that'll be inside your Docker file, and you need to set N8N community packages allow tool usage to true. If that's super confusing, you have no idea how to do that, just copy paste this page into ChatGPT and it'll give you step by step directions. Now once you do that, come back into N8N, hit the plus sign, and we're searching for MCP. Hit MCP client, and we'll do list available tools. And then for each tool, you're gonna have to connect it to an MCP server. So to do that, you need to go to this GitHub, it's model context protocol GitHub. And if you come down here, you're gonna see all the different servers you can connect to. Now let's do a quick test with Airbnb because it doesn't actually require us to have an API key. So just scroll down, click Airbnb. And once inside the Airbnb MCP server, you can scroll down and you should see something that looks like this. We're looking for something that says command and something that says args. So that's the command and the arguments. If you come back into here, you'll see the command. So we're gonna put npx, same thing from there. And the arguments, what we're gonna do is we're gonna take each of these arguments and copy paste them in one by one, put a space in between them. So dash wise base and then at openbnb, etc. And it should look like this, right? We don't need an environment variable because there's no API key associated with this. Hit save, and then we can hit test step. And here's the tools. As you can see, there's two Airbnb tools, Airbnb search and then listing details. So there you have it. That was a real down and dirty of how to connect MCP. You know, we could continue going more and more in depth, right? Like there's all sorts of things we can then start executing tools, listing prompts, etc, etc. If you're looking for in-depth guides of how to actually do that, I have a full tutorial coming out in my community tonight. There's a link to that in my profile. So hope to see you there. All the guides I do are built for like non-technical users so you can get the most out of things like this.
