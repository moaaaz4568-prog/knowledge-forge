---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/DRubBBtjNw4.txt"
words: 551
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_DRubBBtjNw4

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/DRubBBtjNw4.txt` — حساب: airesearcherguy — إنستجرام — فيديو DRubBBtjNw4

---

Basically, I took the entire dictionary of Excel functions. I vectorized it, I indexed the full text, and then I put the content, the vectors, and the indexed text in a spreadsheet and converted that to a JSON and used that as the single source of truth and then worked with AI to build an Excel add-in around that. And this is what we created. Let's check it out. All right, so I have some dummy data here inside of an Excel workbook. I'm gonna go ahead and open Formula AI. All right, I have some test queries to give it. So let's go down the list. Give me a formula that calculates total net sales for Facebook ad orders in March 2025 using the orders table. This formula sums the net sales column for orders where the channel column is Facebook ads and the order date falls within March 2025 between Excel date values 45710 and 45740. All right, this says place this wherever you need the result. So I'll put it here under the L, insert into selected cell, and the total net sales for Facebook ads ordered in March 2025 is 218. All right, let's do the next one. Write an Excel formula that calculates total profit, net sales minus COGS from the order table, but include any orders where refunded equals yes. Let's do this. This formula calculates the total profit by subtracting the sum of COGS from the sum of net sales, but only includes orders where refunded is no. All right, so we'll do this right here. 280. 2. Beautiful. I have an orders table with net sales and order ID. Create a formula to calculate average order value for each channel, for example for Facebook ads only. All right, let's do it. All right, so this is gonna give me Facebook ads only because that's what my request was. Average order value of 72 for Facebook ads and we can do that for all of them. Give me a formula that calculates ROAS for Facebook ads on the 2nd of March from the marketing spend table. Right now we're working in the marketing spend table. Let's insert this formula to calculate ROAS and here we go, 5. 6, perfect. Okay. I want a formula in the inventory table that calculates days of stock remaining for each SKU based on on hand divided by daily sales. If daily sales is zero, avoid errors. All right, there we go. We have our calculations. All right, so there you go. It's as simple as that. You tell the AI what you want and it'll tell you where to put it. I've actually tested this before. It does also create formulas that can pull data from separate tables. You just have to be explicit about where you want to put the formula so it knows to include the variables needed for pulling from a different table or from a different sheet. But yeah, I mean all the functions are loaded in it and it's smart enough to know how to guide you through creating the most efficient formulas to get your data. So hope this helps. Check out aiplusautomation. Com for this Excel add-in. There's one for Google Sheets as well. Peace, be well and do good things.