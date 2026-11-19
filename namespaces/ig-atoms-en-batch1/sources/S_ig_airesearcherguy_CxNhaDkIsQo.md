---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CxNhaDkIsQo.txt"
words: 344
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CxNhaDkIsQo

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CxNhaDkIsQo.txt` — حساب: airesearcherguy — إنستجرام — فيديو CxNhaDkIsQo

---

So I just wanted to share really quickly an advanced make dot com strategy. So a lot of the scenarios that I create involve a lot of API calls, but because it's easier to just have one flow in a blueprint, usually I keep it all in a single scenario. And what that means is some of these API calls require a period of time to wait before the results are rendered. So I'll use sleep modules to wait a reasonable amount of time until you should be able to fetch the results. But actually a more efficient way to handle that would be to split up your scenario into multiple scenarios and employ webhooks. And I'm gonna show you how to do that real quick. So most APIs support using webhooks. Here's an example. This is the stable diffusion api dot com dreambooth API documentation. Here are all the parameters that you can put in the JSON and you'll see webhook is one of them. So it's just a simple parameter. You put the webhook parameter in there followed by the actual URL of the webhook and it'll work. Here's another example in trans loaded. It's actually called the notify URL, but it works the exact same way. You put it in the JSON and it'll work. And this is how that works. Here's an example of JSON. As you can see, this is a trans loaded API call and the notify URL parameter is in there. In make dot com, when you create a webhook, it gives you a URL. You put that URL in that parameter and then whenever the API is done making the call and the results are rendered, then it pushes that data back through that webhook. And here is the second scenario. The scenario has been split in half. As soon as that webhook is pinged, all the data gets pushed into here and that data is then used to continue its workflow, which in this case is publishing to social media platforms. Anyway, hope that helps.