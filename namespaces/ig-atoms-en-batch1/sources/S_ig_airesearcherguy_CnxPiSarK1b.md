---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CnxPiSarK1b.txt"
words: 377
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CnxPiSarK1b

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CnxPiSarK1b.txt` — حساب: airesearcherguy — إنستجرام — فيديو CnxPiSarK1b

---

How do you get your AI generated content to pass AI checkers? Let me show you. Now a lot of people are saying to use Quillbot, but Quillbot doesn't have an API, which means this cannot be automated. You have to do it manually. Well, I've found a solution. This service, Rephrase. Info, offers an API. Now it is $10 a month, but if you plan on autoblogging, you definitely want to use a service like this. So I connected the Rephrase API to my autoblogger. So here's the topic picker again, and then the first OpenAI prompt is to create a title. The second prompt was to create an introductory paragraph, and that's the first thing I'm going to rephrase. Do this with an HTTP module. You got to put your Rephrase. Info API key in there, and then in the body, it's a multipart form data. Set the language. The actual data that you want rephrased is going to come from the previous OpenAI module. They have four modes. Zero is just picking different words. One is standard. Two is advanced. That's what I choose usually, but they do have a third, which is for creative mode. And then style is zero because you don't need it formatted. Parse response yes. The output is going to be in JSON, so you just use a parse JSON module, and then that'll make that readable. The next OpenAI module was for the article body, and then you set up the Rephrase API and JSON again. And then the final OpenAI module is to take the introductory paragraph and the article and turn it into HTML so you can send it to medium. Com. And that's it. Once I run this, it's going to take AI generated content, rephrase it so that it looks 100% human, and post it to Medium. Let's try it. And the article it posted was "Unlock Your Power to Persuade: Proven Strategies to Increase Your Influence. " This looks like a decent article, but let's really put it to the test and run it through an AI checker. Alright, contentatscale. Ai is probably the most accurate AI checker I have found so far. Let's check our article. Look at that, 100% real. Fantastic.