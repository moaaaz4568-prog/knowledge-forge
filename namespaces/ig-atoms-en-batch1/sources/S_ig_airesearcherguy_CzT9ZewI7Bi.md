---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CzT9ZewI7Bi.txt"
words: 527
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CzT9ZewI7Bi

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CzT9ZewI7Bi.txt` — حساب: airesearcherguy — إنستجرام — فيديو CzT9ZewI7Bi

---

How about some automations with image recognition? See, we've all been enjoying GPT-4V because we can give it images and it tells us what's in them. And before that came out, we were doing that with Bing and Bard. It's a really useful capability. Problem is, is you have to use the chat interface and you can't automate that. A couple months ago, I wanted to solve that, so I went in search of an API that I could use for image recognition. I found Google Cloud Visions. It sucked. Every time I sent it a picture of an exercise ball, it insisted it was probably an orange. Then I went to RapidAPI and found a couple more. They also didn't really work. I kept giving them images of e-commerce products and they just couldn't get it right. They couldn't tell me what was in the image. So I figured we just weren't there yet. But then the other day I was scrolling through social media and I read an article about Cosmos 2. In that article, there was a link to a GitHub. As a no-coder, that's really cool, but it doesn't really do me a lot of good. But on a whim, I decided to run a Google search and found that somebody had uploaded it to Replicate, which means that I would be able to access it via Replicate's API. And you can too. It's really easy. I'll show you how, but let's take a look at what this thing can do. So first I show it this image, and this is the response I get. The room features a large tapestry hanging on the wall and a bed with a white comforter and pillows. It doesn't tell me the words on the pillow, and it said something about pillows on the floor. Obviously the floor isn't in this picture, so it's not perfect. But so far, this was one of the better descriptions of this image that I've gotten. Then I showed it this slightly more complex image, and this one, it described it pretty good. It talks about it being two young women dressed in Hogwarts robes, pointing wands at each other. It even talked about the decorations in the background, and it saw other people, which were reflections in the glass, but still, this is really good. But this was the real test. This is the real use case. This is an e-commerce main image. If I could get this image recognition program to describe this image in detail, then I could use it for something. And this is what I got out of it. It told me that the image was a close-up of three tacos. It told me that they were arranged in front of metal holders, and it even had an opinion on the quality of the image. And this is really easy to access. Just start a Replicate account, go to replicate. Com forward slash lucataco forward slash cosmos 2. When you go to the API tab, hit HTTP, and it'll give you the JSON that you need to run in make. Com. Hope this helps. Cheers.