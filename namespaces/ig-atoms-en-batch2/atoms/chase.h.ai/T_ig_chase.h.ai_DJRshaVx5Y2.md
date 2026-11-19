---
type: atom
topic: instagram-transcripts
source: sources/S_ig_chase.h.ai_DJRshaVx5Y2.md
location: instagram/chase.h.ai
---

# T_DJRshaVx5Y2_01

"Welcome to part two of my guide that shows you how to build an AI agent that does public sentiment analysis and technical analysis on any stock you want, all without using any code. So make sure to check out my previous videos to catch up and follow this page to see the rest. All right, so here's where we were on the chart image website. You already signed up and you did the basic." — sources/S_ig_chase.h.ai_DJRshaVx5Y2.md

# T_DJRshaVx5Y2_02

"Now this is where you can see all the different charts you have available to you. And on the right, it will show the chart as well as the code that you need to put inside of n8n to actually grab that information. So for this example, we're gonna use this MACD chart and it shows it with Microsoft, but we're gonna change it so it's dynamic and it pulls whatever chart we want." — sources/S_ig_chase.h.ai_DJRshaVx5Y2.md

# T_DJRshaVx5Y2_03

"And so to do that, we need to copy this code down here where it says curl. You can just click on these two squares that are overlapping. Next, we're gonna go back into n8n. You're gonna go to this HTTP request module we made earlier. Go to import curl, paste that in there, delete this for window stuff, and then import it." — sources/S_ig_chase.h.ai_DJRshaVx5Y2.md

# T_DJRshaVx5Y2_04

"And so now we got a bunch of stuff filled out, but we need to change a few things. So go to URL, open it up, and you're gonna add slash the words to this. We're then gonna go to x API key and this is where you're gonna put in your API key. And then I want you to come down here where it says response format. We're gonna change that to JSON." — sources/S_ig_chase.h.ai_DJRshaVx5Y2.md

# T_DJRshaVx5Y2_05

"So delete all that stuff and you're gonna put in query and then whatever ticker you want. In this case, I'm just gonna use Tesla. Hit save, come to edit fields, and here what you're gonna wanna do is for name, you're just gonna do ticker in lowercase. And then you're gonna drag in this value from the left where it says query and put that in there." — sources/S_ig_chase.h.ai_DJRshaVx5Y2.md

# T_DJRshaVx5Y2_06

"So it should look like this if you pull it up where it shows symbol, NASDAQ, and then the ticker. And so if you've done that correctly, when you hit test step, you should get something like this where it shows the URL, the size, and all this stuff. And if we actually copy paste that URL, we can actually see the chart we got. So that's it for part two. We were able to actually grab the chart." — sources/S_ig_chase.h.ai_DJRshaVx5Y2.md

# T_DJRshaVx5Y2_07

"In part three, I'm gonna show you how to connect that to the AI agent so we can actually start doing some real analysis." — sources/S_ig_chase.h.ai_DJRshaVx5Y2.md
