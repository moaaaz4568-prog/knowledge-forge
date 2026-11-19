---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Con7tJ7uZoW.txt"
words: 487
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Con7tJ7uZoW

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Con7tJ7uZoW.txt` — حساب: airesearcherguy — إنستجرام — فيديو Con7tJ7uZoW

---

So I created an AI persona that writes blogs and social media content automatically. It even has a newsletter. Let me show you. First, let's look at what this thing cranks out. So there is the AI marketing bot on Medium, and we have the blog article. That is an AI-generated image. Nice, robust article there. We got the Twitter. There's the image and a tweet about the blog article topic. There's the AI marketing bot on LinkedIn, a much longer summary of the topic and the image again. There's the image on Instagram with the title of the blog and then check it out on the Medium. And my personal favorite, there is the newsletter with the title of the blog in the subject and then a newsletter-worthy summary of the topic. Now let me show you what I did. I just call this scenario ultimate in make. Com. I'm gonna go through this pretty quickly though, 'cause there's a lot here. First we have the topic randomizer, seven different topics that it will land on a different one every time. The blog title creator by OpenAI, the image prompt creator, the converting the image prompt into a string that doesn't have quotation marks. Markdown to HTML takes that and turns it into HTML. HTML to text and the text parser turns it back into text. And the reason is because this has extra spaces and that gets rid of the spaces. This is the HTTP make a request where I get the Stable Diffusion API to create an image. OpenAI creates a blog intro paragraph here. Then it creates the body of the blog. Then I have a router here because sometimes that image will come back as done and sometimes it'll come back as processing. So you have to have two different tracks based on whether or not it's done or processing. This formatter is what turns the image as well as the intro paragraph and the article body into HTML to post to Medium. Here we post it to Medium. This OpenAI module summarizes everything for a LinkedIn post. This module grabs the hero image that was created by the Stable Diffusion API to put into the LinkedIn post. And then of course text to HTML and HTML to text to get rid of all of the extra space. Then this posts to the AI marketing bot's LinkedIn, that image as well as the summary. This creates a summary for the newsletter. Here's the get response module that then sends out that newsletter. This OpenAI module creates a summary for Twitter. Text to HTML, HTML to text gets rid of the extra space. Here's where it posts it to Twitter, and then finally the image to Instagram. And that is the ultimate automatic content generation scenario that is currently fueling an AI avatar with totally artificial intelligence generated content. Hope you like it.