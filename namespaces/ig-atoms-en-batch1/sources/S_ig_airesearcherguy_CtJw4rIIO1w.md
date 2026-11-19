---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CtJw4rIIO1w.txt"
words: 473
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CtJw4rIIO1w

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CtJw4rIIO1w.txt` — حساب: airesearcherguy — إنستجرام — فيديو CtJw4rIIO1w

---

I just created an AI-powered social media assistant. So I know I've created a few different bots that basically automate social media posting. A lot of them work off of rotating through predefined topics, but what about more recent information? How do you make posts on the fly about trending or breaking news? Let me show you. All right, here in make. Com, the first module is a webhook, just because I wanted to use a form that I built, but that could be any form. That could be a Typeform, a Jotform, a chatbot. You just gotta have these two inputs, a topic and instruction. That's it. This is the Google Custom Search Engine, and it searches for the topic. Now, while you can set that to search the entire web, you can also set it to only search certain pages, and this one I have searching news. Google. Com. Alternatively, you could use an RSS feed, but I feel like news. Google has a broader spectrum. And then this uses Scrape Ninja to take all the information off of the news webpage. These modules just format the text, take a bunch of characters out of it, so it's easier for OpenAI to read. Then we have the first OpenAI module, and this just has GPT-4 summarize the information. Then we have a router, and the router filters the direction based on the instruction. So this one checks the instruction to see if it has the word thread in it. If it does, it writes a Twitter thread. If it has the word tweet in it, it writes a tweet. If it has the word LinkedIn in it, it posts to LinkedIn. If it has the word Facebook in it, it posts to your Facebook page. And you could put an image module in there and post to Instagram. You could post to Reddit, your website, a number of different places. And all of these are basically the same. It just tells GPT, hey, you're a platform writer. Here's a bunch of examples, and the more examples you can give it of your own posting, the more it will mimic your style. But it says here below are a list of example posts. Use the tone and personality of the examples to craft a new post on the topic and news summary provided, but add a compelling hook. And then this grabs the image from the news article and then posts to Facebook. Let's see it in action. All right, here I'm using my form. The topic's gonna be ChatGPT, and then we're gonna write a LinkedIn post. Press submit. Data was sent to Make. The run was a success. We see here it did post to LinkedIn, the proper channel, and here's the post. And that's your AI-powered social media assistant.