---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CrN-VGNoKjS.txt"
words: 296
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CrN-VGNoKjS

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CrN-VGNoKjS.txt` — حساب: airesearcherguy — إنستجرام — فيديو CrN-VGNoKjS

---

I made an AI-powered web page creator. Check it, let's go. So for the input, I created a JotForm with two simple questions: focus keyword and page topic or purpose. And then in Make.com, that form is the trigger. Really, this scenario is just a modification of my SEO keyword seed blog writer. But the seed keyword input is fed into the search keywords Google API, and then it's filtered by volume, and then the resulting keywords are aggregated. And then we have OpenAI, first the page title. All right, the system prompt here is you are an SEO-focused website creator that creates high-converting web pages. And then the first user prompt is talking about how they need to create a title based on the keyword list and the page purpose. And then the next prompt has GPT create an intro, basically explaining what that page is gonna be all about. And then the prompt after that tells GPT to create the actual body of the page. Then we have GPT format that in HTML. Then we have GPT use the title to create a slug. And then these all transform the GPT answers into JSON because that's the way the WordPress API takes the info. And then in here, we're calling the pages API endpoint and then feeding it the JSON with title, content, and slug. Status is publish, meaning it publishes immediately. And here's what we came up with. This is my WordPress page, Unstoppable Instagram Growth: Dominate Your Niche with Our Proven Techniques. And this was promoting an Instagram growth service. This is the intro, and then here's the body talking about the service. So yeah, let me know if something like this is useful and I'll add it to the bot bundles.