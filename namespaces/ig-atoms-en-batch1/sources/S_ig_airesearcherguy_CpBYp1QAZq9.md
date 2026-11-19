---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CpBYp1QAZq9.txt"
words: 446
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CpBYp1QAZq9

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CpBYp1QAZq9.txt` — حساب: airesearcherguy — إنستجرام — فيديو CpBYp1QAZq9

---

I just built a really cool AI-powered customer support bot. Let me show it to you. All right, the customer support window has opened and I am putting in my customer concern, saying that I want to cancel my account. That's pretty standard stuff. I had to put in some delays because it'll take a couple seconds for what we want to have happen to render. And here's our AI-generated text response and then a video. Thank you for your interest in Boring Company. We apologize for any inconvenience this may have caused. Your account has been canceled. Please let us know if there is anything else we can help you with. So we have to have two different make. Com scenarios here because we have to pass data in between two different webhooks. But the first one has a trigger that goes off and passes the customer information from Chatfuel to make. Com, and that's the complaint, the customer service concern, which then gets passed to OpenAI, where the prompt says you're a customer service representative for, and then I put Boring Company, but you'd put whatever your company is. Customers reached out with a common concern, and then put the data that they input. These two format that data so that there's not extra characters whenever you make an HTTP request. I use a service called D-ID, which has a talking portrait, which is what you saw. Just got to put your API key there, put in the JSON from their API documentation. Then you got to let it sleep so that it can process, and then this HTTP request just grabs the finished video and then saves it to a data store. And then there's another webhook so that the same flow can continue going. And then this data store gets the record that is saved in the data store from the previous scenario, and then it sends it back to Chatfuel. Now let me show you the Chatfuel flow. So for this example, I used a URL, but you would actually put a website widget here so that it could live on your website or on your customer support page. The question you saw, what can we do for you today, and then it collects the answer in this variable, which is what's passed over to make. Com. Make a JSON request, that's the first trigger. Typing animation to give it some time. Hold on a second while I find somebody to assist you. Delay so that it gives it more time. And then this is the second trigger, which then should trigger a response, which is the video that you saw.