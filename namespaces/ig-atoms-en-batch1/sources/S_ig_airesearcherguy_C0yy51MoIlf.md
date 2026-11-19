---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C0yy51MoIlf.txt"
words: 533
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C0yy51MoIlf

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C0yy51MoIlf.txt` — حساب: airesearcherguy — إنستجرام — فيديو C0yy51MoIlf

---

Let's talk about knowledge base bots. I've had a couple people ask me about this and I have talked about them in the past, but today I want to show you how to implement one. But first let's talk about what they are. A knowledge base bot is an AI chatbot that's connected to a database of knowledge. Now why would you use one? Well, large language models are really smart and they have a ton of information, but for the most part it's all generic. It's not niche specific to your situation or your business. And this is why a lot of people are so hesitant to allow AI to create content for them. They complain that it's just too generic sounding. And while prompting can help with a lot of that, you can get even farther by connecting it to a knowledge base. So I'm actually gonna show you how to build one and then I'm gonna show you how to implement it in a make. Com automation flow and the service that'll help you make it all happen in no code. Check it out. So real quick, you can do all this with Dante AI and I know I've talked about them before, but back then they were prohibitively expensive. You could only get access to the API with a $90 a month plan, but they've changed that. Now they have new entry plans for $10 a month and API access. So with that, let's get into it. First, Dante makes creating a knowledge base bot the simplest thing ever. You just click to create a new knowledge base and then you give it links or PDFs or txts or whatever format you have the information. So here's an example of one of our knowledge bases. It has PDFs, it has a bunch of URLs and it has a bunch of YouTube videos. Now in make. Com, accessing the knowledge base is through API, so it takes three HTTP modules. Obviously the rest of your flow will be before and after. This is just the part that accesses the Dante knowledge base that you built. The API endpoint is conversations, so this first HTTP call just creates the conversation in the knowledge base. The next one is query stream. This one's where you actually ask it the question and then start collecting the answer. So you have two parameters, the conversation ID, which is created in the previous module, and then the question. And then you ask it whatever question. It doesn't actually have to be a question. It could just be a search term. I mean, it works a lot like Google. You just put whatever in there and it's gonna use that to search the database before answering. And then this last API call calls messages. As you can see, this is a get request and all this does is it grabs that last message that was created in the previous module. And there you go. And if you insert that into a flow that creates content, then you will have much better context that is much more suitable for your business. Anyway, I hope that helps. Cheers.