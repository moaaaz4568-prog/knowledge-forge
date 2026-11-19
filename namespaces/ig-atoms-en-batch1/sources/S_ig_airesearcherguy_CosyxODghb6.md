---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CosyxODghb6.txt"
words: 483
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CosyxODghb6

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CosyxODghb6.txt` — حساب: airesearcherguy — إنستجرام — فيديو CosyxODghb6

---

I just created an AI-powered e-commerce bot. Dropshippers and e-commerce sellers, check it out. All right, first we head over to browse.ai, which is an AI web scraper. And here I created what I call a dropship robot. Basically, I took a category page out of AliExpress, and I have it scraping the page for product titles, prices, and imagery. And when I run that scraper, it extracts the data onto this Google sheet. Then in make.com, the trigger is to watch rows in Google Sheets. You can't feed OpenAI multiple bundles, so you gotta limit it to one and just have it run like every minute or two. The first OpenAI module is to rewrite the title, so rewrite the following product title, and then it takes the product title from the sheet that was scraped. The next OpenAI module creates a product description. Now we don't have a product description because this is a simple scraping bot that can't click into each product, so we're gonna have artificial intelligence create a product description based on the title. That's an increment function. I'll show you what that does in a minute. Then we have this OpenAI module. Basically, this just extracts the number from the price because the price always includes like a currency symbol or US in front of it. So this just makes sure that all we get is a number. And the reason is because in Squarespace, in the price section, you can only put a number, otherwise it'll fail. Now, you can do this with any website that has an integration with Make, Squarespace, Wix, Shopify. I'm just using Squarespace because it's free. But here, that was the increment function. This is so every product has a new SKU number. And then this parse number makes sure that this price is only a number. And then the name and the description are the product title and description created earlier in the scenario by OpenAI. And this right here gets the product image from the sheet, and then this uploads the product image. Let's see what we get. And here it is automatically uploaded the product to my Squarespace e-commerce site. Here's the title rewritten. 7A Super Speed Huawei P40, P30, Mate 40 USB-C Charging Cable. That'll probably make a lot more sense if it wasn't cell phone accessories. The description's actually pretty good because it looks like OpenAI understood what this product does. There's the image. It could use work, but I think that's because AliExpress has really poor quality images on it. So if you use another site, that might work better. But overall, this is cool. And what happens now? Anytime I run the Browse AI scraper, as long as this scenario is on, it's gonna just keep uploading products automatically to my e-commerce site. And that is how you automate e-commerce and dropshipping using AI.