---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C89f7pcI3Jw.txt"
words: 563
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C89f7pcI3Jw

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C89f7pcI3Jw.txt` — حساب: airesearcherguy — إنستجرام — فيديو C89f7pcI3Jw

---

Filming outside today because it's freaking beautiful out here. Anyway, see that? Oh my gosh, absolutely gorgeous. Anyway, I just built an amazing tool that I think will be really helpful to Amazon sellers. I did build it in N8N, N8N, however you want to say it, instead of Make. And the reason is because N8N has some really awesome AWS tool integrations that are native to the platform. Now why is that important? Well, if you've ever tried to deal with Amazon API calls, Amazon, a lot like Microsoft, makes it very difficult. There's like a signature you have to sign and then hash and do a bunch of really complex stuff that is kind of beyond my current skill set. But when the integration is native to the platform, all that stuff is handled automatically. So that's why I built it in N8N. And N8N has access native integration to two tools that are very useful to Amazon sellers. One is AWS Recognition, which is Amazon's AI label detection tool. And basically it takes images and tells you what's in them. And what this does is it tells you what Amazon sees when it looks at your listing images. And the other tool is AWS Comprehend. This is a text label detection service. So basically it tells you what Amazon sees your listing says, or what the words inside your listing mean to Amazon. So these are cool, very, very useful AI tools within AWS. And I built a tool that essentially takes that AI data and feeds it to another AI and gives you a report on what the data means. So let's take a look. All right, let's get into this bad boy. So first we have form trigger as usual. That's how I love to make these things. This is because it's just easier to grab the URL of the Amazon listing and put it in instead of like trying to find the ASIN. I just try to make it as easy as possible. So here we just take the URL. That's the only field that this takes. And then these two fields, they essentially find the ASIN within the URL and extract it. So that's what this is. It's a regex that takes the ASIN from the URL. Once we have the ASIN, we're able to do an HTTP request to Parazon. This is the Amazon API that I love to use. This gets the product details. So once the ASIN's in there, we put that in as a query and it grabs all of the details for the product. Then what these three do here is actually grab the first three images. All right, so this is just a simple request for to download the image because it needs to be, I guess, in N8N. So we download the image and then upload it to AWS S3. We have to upload it to an AWS bucket. And then AWS Recognition, right? So this is detect labels. This is Amazon's AI that essentially looks at an image and then figures out everything that's in that image. And then this code right here, which I did not write because I don't know how to write functions, Claude Sonnet 3. 5 wrote this. This code right here just grabs all of the details and puts it in one block.