---
type: atom
topic: instagram-transcripts
source: sources/S_ig_chase.h.ai_DJUK3vzxR_r.md
location: instagram/chase.h.ai
---

# T_DJUK3vzxR_r_01

"All right, welcome to part three of my step-by-step guide of how to create an AI agent that allows you to do public sentiment analysis and technical analysis on any stock you want without using any code. Make sure to check out my previous videos on this topic to get caught up and follow this page to see the rest of the guide. So here we are in part three." — sources/S_ig_chase.h.ai_DJUK3vzxR_r.md

# T_DJUK3vzxR_r_02

"So we're actually gonna download the chart of that stock we got in part two. We're gonna analyze it and then we're gonna hook it up to our greater AI agent. So to do that, hit the plus button here. You're gonna search for HTTP request and all we're gonna do is we're gonna drag in this URL over here and that's gonna allow to go to that URL and download the image, right? So test the step." — sources/S_ig_chase.h.ai_DJUK3vzxR_r.md

# T_DJUK3vzxR_r_03

"For the input type, you're gonna do binary file. You're gonna set that to data. And then inside this text input, this is where you're gonna put the system prompt for how you want the image to actually be analyzed. So I have a whole prompt here that I got from ChatGPT. You can get something similar." — sources/S_ig_chase.h.ai_DJUK3vzxR_r.md

# T_DJUK3vzxR_r_04

"Just go to ChatGPT and say, hey, I'm looking for a system prompt for an AI agent that analyzes, you know, charts for technical analysis, right? And then it'll spit something out for you. And this is where you put it. And so once you do that, just do test step. And then here you'll see all the information it gave us regarding the stock, all the analysis it did." — sources/S_ig_chase.h.ai_DJUK3vzxR_r.md

# T_DJUK3vzxR_r_05

"And so now we need a way to feed that back to the main AI agent we created in part one. So we're gonna go to plus, we're gonna go to edit fields, and we're gonna call this response. We want to send back this content, right? So map that in. That was all the analysis. And then we also want to send back the actual image." — sources/S_ig_chase.h.ai_DJUK3vzxR_r.md

# T_DJUK3vzxR_r_06

"We'll say call this tool when you want to do technical analysis on a stock. And then from workflow, you're gonna do by ID. So for the ID, if you come up here to the URL, in your browser you'll see this stuff like n8n. Cloud/workflow/ and then after the workflow/ is a whole string. That's the workflow ID. You're gonna copy that, you're gonna paste that in the workflow, and then you go back." — sources/S_ig_chase.h.ai_DJUK3vzxR_r.md

# T_DJUK3vzxR_r_07

"And so now you can actually call on that tool to do the analysis and have it come back to an agent that you can actually chat. So that's it for phase three of building this agent. In phase four, we're actually gonna go in and do the sentiment analysis by scraping the web." — sources/S_ig_chase.h.ai_DJUK3vzxR_r.md
