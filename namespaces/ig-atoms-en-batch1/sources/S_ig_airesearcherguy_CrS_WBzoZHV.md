---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CrS_WBzoZHV.txt"
words: 483
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CrS_WBzoZHV

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CrS_WBzoZHV.txt` — حساب: airesearcherguy — إنستجرام — فيديو CrS_WBzoZHV

---

I have brought AI into the physical world. Now I know I've said this before, but this is probably the coolest bot I have built yet. But I created a bot that writes physical letters and sends them to people through snail mail. Check it out. So first, this bot relies on an API from a program called PostGrid, which allows you to send mail communications and then their company sends out physical mail. And this is what that looks like. This is an API request that sends the sender's information as a contact because everything has to exist in their system as a contact first. This is a Google Sheet full of contact information. So as you can see here, these are names and physical addresses of people. Here's another API call that adds the people from the sheet into PostGrid as a contact. And then we have the OpenAI module. The system prompt for GPT is, you are a physical mail outreach agent. You are promoting company XYZ's social media growth services via physical mail. Obviously, you would put your own business use case in there. And then the user prompt is, write a personalized letter to, and then you take the first name from the previous API call, about how XYZ can help them grow their Instagram account. Use direct response style language and try to evoke emotion while creating a real connection with this prospect. Break up the text so the paragraphs are no more than two to three sentences long and make it at least 200 words. Sign off the letter from, and then this is my contact info from the first API call. Constraints are as usual not to include context or pretext. And then this JSON transformer takes the response and turns it into JSON because that's what's needed for the API call. And then this final API call actually sends the letter. And you'll see here that I ran it successfully. Dear Banjo, I recently stumbled upon your Instagram account. Luckily for you, I work at XYZ. And that would be sent out live as a physical letter. And then if you come in here and you set the maximum number of return rows to however many rows you have, it'll cycle through each and every one of those. And then all you have to do is turn it on and then it'll send out all your physical mail. And then you might be thinking, where am I going to get physical addresses from? Well, you can buy leads lists as one method. Here, DirectMail. Com sells them, AccuZip sells them, and then LeadsPlease sells them. And this is by customer segment. You can send mail to specific demographics, to specific income or activities, investment types. So this is a great tool for any business that wants to differentiate themselves by sending out physical mail.