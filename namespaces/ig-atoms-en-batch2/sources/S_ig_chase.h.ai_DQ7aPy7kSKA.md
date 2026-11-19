---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DQ7aPy7kSKA.txt"
words: 567
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DQ7aPy7kSKA

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DQ7aPy7kSKA.txt` — حساب: chase.h.ai — إنستجرام — فيديو DQ7aPy7kSKA

---

Did we overhype MCP? Because just this last week, Anthropic released this article called Code Execution with MCP, and the first half of this article is all about the real world problems people are having with their agentic systems when trying to use MCP servers. So the primary problem with these MCP servers is token bloat, and you can see it in action right here. I'm inside of Claude Code. I have not done anything. I haven't even talked to it. And we are already two thirds of our way through our 200, 000 token context window. And of that, a third of that window, 66, 000 tokens are already being eaten up by these MCP servers. And I only have three attached right now. We have the N8N MCP server, Playwright, and GitHub. So before we've done a single task, we are already two thirds of the way through our window. Now you're probably saying that's not a big deal. I still have 70, 000 tokens to go. But the problem is we start running into context rot situations very quickly in this scenario. Now what's context rot? That means as we start dealing with our later tokens, right? We are at token 132, 000 already. That last 50, 000 tokens is not the same as the first 50, 000 tokens. Those later tokens, as we eat up the context window, are worse. Now the exact token number when we begin to fall off in terms of performance isn't exact and it depends both upon the model and the tasks we're giving it. But when we think about it, we realize we are right away behind the eight ball if we are trying to create agentic solutions with a large amount of MCP servers, right? This isn't where you want to begin. So what exactly is the solution to this? Well, Anthropic talks about code execution and it says to present MCP servers as code APIs rather than direct tool calls. So instead of having a scenario like you see here where every single MCP server and all of its associated tokens is loaded on the front end, we instead take that away and we just put it inside of our file system. One approach from Anthropic is to generate a file tree structure which shows all the available tools from connected MCP servers like you see here. The long story short is basically this reduces the amount of tokens used by up to 99% because we aren't loading all these tools on the front end like you saw before. And the reason this works so much better too is because this allows the AI to essentially write code on the fly to execute these tools, which these AI systems are really, really good at. However, Anthropic does talk about the fact that this is a trade off, right? This does add a bit of complexity because you're having the AI system go to another file, search for the exact tool, and then spin up some code or scripts for it, versus just having it all ready to go, which means, you know, whether you want to use this new approach that Anthropic talks about or the old school quote unquote approach or just loading everything up traditionally kind of just depends on the complexity of your system and how many MCP servers you really need.
