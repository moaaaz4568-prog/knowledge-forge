---
type: atom
topic: instagram-transcripts
source: sources/S_ig_chase.h.ai_DIH1FmARVnJ.md
location: instagram/chase.h.ai
---

# T_DIH1FmARVnJ_01

"So the other day I showed this custom AI newsletter creator that I made for a client, and had a bunch of you ask me, how did I make it? So in this video, I'm gonna show you a quick guide of how to create a simplified version of that AI custom newsletter creator for ourselves." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md

# T_DIH1FmARVnJ_02

"Now once we're inside n8n, the first thing you're gonna do is create a schedule trigger so it runs every single morning. Next, you're gonna need to do a code module, and I know code can be very frightening, but you just want it to look like this, right? We're just setting a couple JSON lines that then say feed, and then it has the URL in there." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md

# T_DIH1FmARVnJ_03

"And if you're not seeing this, that means you just need to have it run workflow. So if you right click right here and hit test workflow, you'll see some data. Now the next thing we're gonna do is we're gonna do an aggregate module, and you're just gonna set it to all item data into a single list." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md

# T_DIH1FmARVnJ_04

"Again, if you're not seeing this data, just go to test workflow. And then you need to set a system prompt. Now what's a system prompt? Well, a system prompt is just that like custom set of instructions for our AI. In this case, you just need to spell out that, hey, I'm about to give you a ton of articles on this subject, and this is how I want you to pick them out." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md

# T_DIH1FmARVnJ_05

"Like I want the five most relevant, the 10 most relevant, and I want you to grade relevance based on, you know, whatever criteria and include the headline, right, the source, etc. You decide all this, but this is where you put it. Now next, all we do is we just send that off into Gmail. Now I have another code block in here which I named pretty HTML." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md

# T_DIH1FmARVnJ_06

"Lastly, you're just gonna have a Gmail block and you're gonna take that output either from the HTML block or the large language model, and you're just gonna drag it here into the message. And you can name it whatever you want. You can send it to whoever you want. For email type, if you didn't do that code block, just set it to text. Otherwise, you can do HTML." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md

# T_DIH1FmARVnJ_07

"So if you're interested in learning more about like AI automations and AI agents, I would suggest checking out the community my profile. And it's all about, you know, creating guides for non-technical users. So if that's something you're interested, I hope to see you there and let me know what you think of this video." — sources/S_ig_chase.h.ai_DIH1FmARVnJ.md
