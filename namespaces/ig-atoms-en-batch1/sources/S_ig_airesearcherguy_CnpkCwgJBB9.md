---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CnpkCwgJBB9.txt"
words: 366
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CnpkCwgJBB9

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CnpkCwgJBB9.txt` — حساب: airesearcherguy — إنستجرام — فيديو CnpkCwgJBB9

---

I just connected ChatGPT to the internet. Let me show you how. All right, one of the biggest limitations of GPT-3 is that it doesn't have access to the internet. There is a Chrome extension called WebChatGPT, and it adds search results to the query that you put into ChatGPT-3, which is cool, but you can't automate that. But I figured out how to automate it. So first, this requires a free ParseHub account. Download the software, create a project. This project is going to go to the webpage techexplorer. Com/machine-learning-ai-news. And then once it gets there, it's gonna click on the first result, and then it's gonna scrape the text from that result. So this is a AI news website, and this just extracts the text from the latest news. It updates every day. And then in make. Com, you just create a webhook which watches for runs. So every time you run the scrape, this will trigger. You need a sleep module for at least 60 seconds because it takes a little bit of time to scrape, but you don't want the whole thing running before it's had a chance to finish. Then you gotta make an API call. And then of course the next module is OpenAI GPT-3. So here we have it set to DaVinci 003. The prompt is provide a summary of and add commentary to the following news update, and then put the data that was scraped from the previous module in here. Use a casual tone and then constraints don't include anything other than the summary and commentary and make the response at least 500 words in length. Now let's see what that gets us. And here we can see GPT-3 has provided us with four paragraphs of summary and commentary on the news article from that AI news website. And then the very last module will be whatever output you want to connect that to. You can make that commentary go to Twitter or LinkedIn or wherever you want to post it. And that's how you create a bot that scrapes the internet, gives that scraped information to OpenAI, and then lets it process it however you want.