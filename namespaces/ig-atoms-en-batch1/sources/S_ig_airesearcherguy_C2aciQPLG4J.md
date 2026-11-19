---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C2aciQPLG4J.txt"
words: 346
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C2aciQPLG4J

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C2aciQPLG4J.txt` — حساب: airesearcherguy — إنستجرام — فيديو C2aciQPLG4J

---

So a lot of good automations rely on being able to scrape a web page and take that information and give it to AI. The problem is, is if you just use like a scraping tool, like one I've used many times in the past, Scraping Ninja, it takes way too much metadata, way too much like code, and if you give all of that to GPT, you're gonna pay a ton in tokens. I found a better solution, a couple of different ways to do it, all in no code using free APIs. Let me show you. So first we have this service called AppyHub. Com. Sign up for a free account. The starter plan gets a whole bunch of free uses every month. And then you just go in the search bar and look for extract text from web page, and you'll get the documentation to make that API call. And then in a simple HTTP request in Make. Com, you can make a quick GET request and extract the text from any web page. So I extracted the text from an Unbounce landing page, and here is all of the text. None of the metadata, no code, just all of the actual text on the page. Another way to do it is with this service called API Flash, which has a screenshot API. It allows you 100 free screenshots per month. You can actually just go right here into the query builder once you create your free account, and tell it the page and the output that you want, and it will tell you exactly what to put in the HTTP request. And this is another really easy HTTP GET request. Just put in your API key and then this full page parameter, and then you connect that to a Google Cloud Vision OCR, map over the data, and here we have all of the text on that Unbounce page. And that's how you get all the text without all of that messy metadata from a page scrape. Hope that was helpful. Cheers.