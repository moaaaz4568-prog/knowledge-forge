---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C2slL3VLmA2.txt"
words: 491
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C2slL3VLmA2

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C2slL3VLmA2.txt` — حساب: airesearcherguy — إنستجرام — فيديو C2slL3VLmA2

---

Check it out. So custom GPT actions would be so baller if they weren't so worthless. This is what I mean. Currently custom GPT actions only allow you to add one header and that's for your authentication. But most API calls require multiple headers. You got to specify the content type, you got to specify what it accepts, and you can't put all of that into a custom header in the GPT. Now you could system prompt it to add those headers if you only want to make one API call, but what if you want multiple actions? What if you want to call multiple APIs? Well, I found the solution. It's a cool tool called Retool where you can wrap your API and all those headers and everything are in there and then you just make a webhook call from your custom GPT. Let me show you. First you go to Retool. As you can see, they have a free tier, 500 runs per month. That's pretty awesome. Once you log into your free account, you create a web flow and then you make the start trigger a webhook and then inside the JSON you put an example JSON of the parameters that you need to pass through the webhook. Then you add a query, which is going to be a REST API call. In this particular instance, I'm using a rapid API call, which has two headers. So this is the API call. Here are the parameters, which I grabbed from the webhook module. Those are the two headers, the API key and the host. Then you just add a webhook return. And of course you can run it to test it, but that's all you need right there. Then you take the webhook, come here, copy as curl, then you paste that somewhere because you're going to need that in a second. Then you go into your GPT account and you create your GPT as normal. Then you come in here to create new action, go down to examples, weather JSON, you grab that weather JSON. Then you go to ChatGPT and you say, here's an example schema for a custom GPT action. Please follow the example and create a schema for the provided C-URL, which is what you copied from Retool. Give it the weather JSON schema that you copied, and then you give it the C-URL for the new schema, which is the information that you got from Retool. You copy the schema that GPT provides you, then you go over to your custom GPT and create a new action, paste that schema right there. When it's done, you can test it. You can see here it pushed a proper API call and it worked. So you just wrap all the APIs that you want to call in Retool and then make webhook calls to all of them in your custom GPT. Hope that helps. Cheers.