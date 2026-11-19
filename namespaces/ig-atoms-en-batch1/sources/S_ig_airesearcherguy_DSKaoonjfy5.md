---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/DSKaoonjfy5.txt"
words: 564
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_DSKaoonjfy5

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/DSKaoonjfy5.txt` — حساب: airesearcherguy — إنستجرام — فيديو DSKaoonjfy5

---

So I decided I wanted to test some assumptions and use AI to help me build the tooling. The assumption I wanted to test was, do AI jobs pay higher? So looking on Upwork, I decided to look on Upwork. If you search for AI agent, it basically brings up a bunch of, you know, AI agent engineer type jobs. And I wanted to compare the going rate for those jobs against a traditional marketing job like copywriting. So that's what I did. Anyway, let's see how I built the tool that gave us these numbers. So I went to Upwork, searched, and then once I got to the search page, I right-clicked on this portion and then inspect. And basically what I was looking to do was copy the whole element, right? So right here, this article, I right-clicked again and then copy element. And so what that did was it gave the AI, or would give the AI, the information it needed to build out a scraper for me. Anyway, so once I got that information, I started in Google AI Studio to do this work with Gemini 3. I gave it a screenshot and said, I want to build a Python script to analyze the pricing difference between two job markets on Upwork. I want to compare the job offer prices for AI agent related jobs and copywriting jobs. I was thinking perhaps we would use Playwright to scrape. Here are the details, keyword AI agent, URL, and then I gave it the URL to the search page and then that element that I copied. Then it said, copy this and paste it in a file that you save as main. Py, which is a Python script. And then I ran it and then it worked. And I got a bunch of numbers. All the numbers were saved, all the raw data was saved inside of a file that I could open. Now here's the thing. It gave me the raw data because I have already created with the help of AI an add-in for Excel that specifically does this. Its job is to help with Excel formulas. I just went to it and said, hey, I would like a median and mean score for type hourly and type fixed for each keyword. And then it gave me the formulas. Anyway, so now let's look at the numbers. So for AI agent, the hourly median is 18. So this is the middle price of the price range. And then the hourly mean, which is the average, is 21. So about $21 an hour. The fixed median, so the median for the total budget, the fixed pricing is 300, and the fixed mean, the average is $922. For copywriter, the median is 19, and then the hourly average is 20. 86. So $20 and 86 cents. The fixed median is 150, and then the fixed mean, the fixed average is 582. 89. All right, so what does this tell us? Well, the assumption was that AI jobs probably pay more. That assumption is not entirely correct, right? Literally, you can make $21 an hour as an AI agent engineer on Upwork or $20 and 86 cents an hour as a copywriter. That was fun. It only took, I don't know, 10 minutes to build this. Be well and do good things. Cheers.