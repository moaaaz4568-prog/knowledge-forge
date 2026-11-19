---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Cv4pEoDIYnB.txt"
words: 381
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Cv4pEoDIYnB

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Cv4pEoDIYnB.txt` — حساب: airesearcherguy — إنستجرام — فيديو Cv4pEoDIYnB

---

So if you're using the make. Com Twitter v5 module to post media tweets, that's a tweet with a video or an image, you'll notice that it doesn't work anymore. Like it doesn't work because Twitter is slowly trying to move everything over to the API v2, and part of that process is only posting media with a media ID. And the v1. 1 API endpoint doesn't use a media ID, it just publishes the image and the tweet. And I think they've discontinued that. So now what you have to do is create a connection for your Twitter app with both the v5 module, which is the legacy module, and the v6 module. And then you use the v5 upload media module to get a media ID, and then you can use the v6 create a tweet because you have the media ID, so it'll publish the media. Let me show you real quick. First, it's important to note that in your Twitter app in the Twitter developer portal, in order to create a connection with the v6 module in Make, this has to say Twitter 2. But in order to create a connection with the v5 legacy module, you have to take the 2 off. Just know that you have to come in here and change that. It's real simple. You just go to your app in the developer portal and then click edit down here in user authentication settings. Now you'll notice I keep referring to the Twitter modules as v5 and v6. The legacy is v5 and this is v6. In v5, you use your API key and your API secret, but in v6, use your client ID and your client secret. And how this will look in your scenario is that you'll have an HTTP get a file module that's going to upload your image to Make, then the v5 Twitter module upload a media, and here you just grab the file, and then you'll have the Twitter v6 module create a tweet, and then you just put the media ID from the previous v5 module in there, and it will post the image. Let me show you the work. There it is. This is the test. That's the image. And that's the workaround. Cheers, guys.