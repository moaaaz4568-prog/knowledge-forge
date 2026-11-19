---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CsY7BG3IA4q.txt"
words: 390
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CsY7BG3IA4q

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CsY7BG3IA4q.txt` — حساب: airesearcherguy — إنستجرام — فيديو CsY7BG3IA4q

---

Oh, y'all thought I was done? So remember that epic Amazon review analyzer that I built using Anthropic's Claude AI? Well, I just built an epic listing analyzer. Check it out. It's got essentially the same setup. We're still using a JotForm that takes a keyword. We're still making an API call to grab products. Now, the original vision was to do this for 25 listings, but unfortunately I am running into my monthly API call cap, so I had to stop at 17. But hopefully you'll get the point. All of these are API calls for individual ASINs, but instead of reviews, this time it grabs the listing information. Here I have it grabbing the title, bullets, description, price, and review rating. And then that's all aggregated into a JSON. Check out this prompt. Here's a set of Amazon product listings, top ranked for the keyword, and then the keyword, each including a title, product features, description, price, and average review rating. Here's the Amazon listings. And then please analyze the listings and provide the following information. What are the most commonly used keywords and key phrases across the listings? What are the most persuasive copy elements? What specific conversion elements exist in the listings that may attribute to their success? What consumer psychology elements are at play? And then what improvements are suggested? And this is what we came up with. So the keyword I chose was slim leather wallet for men, and here's what Claude had to say. First, a list of the most common keywords and key phrases, then a list of the most persuasive copy elements. So here it says highlighting the slim, minimal, and lightweight design, which appeals to those looking for a compact wallet. Here this last one, offering an unconditional money back guarantee to reduce perceived risk and instill confidence. Specific conversion elements, a rating of four stars and above, professional product photos. Here are the consumer psychology elements, desire for a stylish and lightweight wallet that doesn't bulge in the pockets, interest in durable and high quality product given the premium price points, and then the recommendations for improvements, focus on an ultra slim and minimalist design with premium luxury materials, provide specific statistics and test results on the effectiveness of the RFID blocking. All right, I think that's pretty helpful.