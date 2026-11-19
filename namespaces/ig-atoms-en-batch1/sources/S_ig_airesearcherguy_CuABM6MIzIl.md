---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CuABM6MIzIl.txt"
words: 347
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CuABM6MIzIl

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CuABM6MIzIl.txt` — حساب: airesearcherguy — إنستجرام — فيديو CuABM6MIzIl

---

I created an AI email assistant that listens for emails from specific addresses, sends you a voice alert with a summary of the email when it comes in, asks you if you want to respond, and if you say yes, it will craft an email and automatically send it on your behalf. Let me show you how I did it. So first, in make. Com, I created a mail hook, and then in my Gmail settings, I set up a filter. Any emails that come from that specific address will get forwarded to the mail hook, and that will trigger the scenario. When the scenario is triggered, GPT creates an alert, tells me where the email is coming from and summarizes what the email is about. That alert is then turned into a voice with Google Cloud text to speech and then sent to a Telegram channel as a voice message. And then information is stored in this data store. At the end of the message, it asks me whether or not I want to respond or not. If I say yes, it takes the information from that data store in a brand new scenario, hands it off to GPT and asks for a response. Then the response is turned into a JSON, given to Gmass and automatically sent out. Let's see it in action. Alright, so here is an email I'm gonna send regarding the keyword reports. Looks great, but I have a question. Is SEO really necessary for our blog? Let's send it. And here's our voice alert. Alert, an email was received from Antonio regarding the keyword reports. Antonio is questioning the necessity of SEO for the blog. Summary, Antonio has complimented the work on the keyword performance reports, but is now questioning whether SEO is necessary for the blog. Would you like to respond to Antonio's email? And then we reply yes, and we get an email in response. Hey Antonio, thank you for the compliment on the keyword performance reports. In regards to your inquiry, we highly recommend SEO. Boom, automated responses.