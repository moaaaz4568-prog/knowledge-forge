---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DK0btE6R1fd.txt"
words: 572
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DK0btE6R1fd

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DK0btE6R1fd.txt` — حساب: chase.h.ai — إنستجرام — فيديو DK0btE6R1fd

---

Have you seen that you can now use V03 inside of N8N? Yeah, I saw it. It's insane how easy it is to set up. So she's not lying. It's actually really easy to set up Google's V03, their new video model, inside of N8N. And let me show you how. Okay, so here we are inside of N8N, and this is a skeleton that I built so that you can automate video generation with Google's V03. Now, why do we care about this? Well, Google's V03 costs a ton of money. Right here you're looking at the Google AI Ultra plan, which while they discount you at $125 a month for the first three months, it then bumps up to $250 a month to get the max amount of credits available for V03. But what if you don't want to pay all that for V03? What if you just want to use it a little bit and you wanted to use it in some sort of automations, whether that's for small ads for you or some sort of marketing material? Well, this automation does that. So the way it works is simple. It starts with a form submission where you just describe what sort of video you're trying to make. What's the subject? What's the context? What do you want the style to be? From there, it then goes to an OpenAI basic LLM chain where it essentially optimizes your prompt to create the best text to video prompt it can. From there, we then make an HTTP request not to Google, but to fale AI. Now, what's fale AI? It's essentially a marketplace for API calls. So you're pretty much asking to borrow their Google account to make an API call on your behalf. So you can use V03 without paying the huge subscription upfront. And now what does that actual cost look like? Well, it's still steep. For an eight second video, you're still looking at $6, which is wild, but the video quality cannot be beat and it's still less than paying $250 a month for the whole AI package. From there, we then wait for the video to be generated. We grab the video. It actually gives you a URL and then we send it off to ourself via Gmail. Now, like I said before, this is a simple skeleton where we're just getting the video once off of submission and Gmailing it to ourself. But you could totally put this in to a bunch of different content creation automations. You could, for example, have a Google sheet that has, you know, say 30 different video ideas and this runs every 24 hours, creates V03 videos for you, and then on the back end you could have it post to a bunch of different socials. So there's a ton of ways you could improve upon and customize this automation. And if you're looking for this template as well as a guide of how to actually set this up step by step, go ahead and check out the community in my profile. I have this template and a video tutorial that goes in depth of how it all works, and it's built for non-technical users. So if this is your first time getting into the AI space, don't worry, it's explained very simply and assumes you haven't done anything like this before. So hope to see you there.
