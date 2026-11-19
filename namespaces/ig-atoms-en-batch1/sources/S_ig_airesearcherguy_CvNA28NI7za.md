---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CvNA28NI7za.txt"
words: 215
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CvNA28NI7za

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CvNA28NI7za.txt` — حساب: airesearcherguy — إنستجرام — فيديو CvNA28NI7za

---

Hey, you remember that AI-powered Instagram Reels generator that I created? Well, I just figured out how to do it on Pinterest. Let me show ya. So this is almost exactly like the Instagram Reels generator. You have your topic randomizer, then you have the OpenAI module that writes the script. This is the API call to D-ID to have the AI video generated, and then this is the API call that retrieves the video. However, this is where it starts being different from the Instagram Reels flow. Instead of using Cloud Convert, this module uploads the video to Make. Then you have to make a Pinterest API call, basically just telling Pinterest, hey, I'm gonna upload a video. Then you have to take the URL that it gives you and also let it fill out all of this multi-form data and then actually upload that video to the URL. You gotta give it a little while to process, and then you can create a Pinterest pin with the source type video ID. You also have to make sure that you have a cover image, so I'm gonna build a cover image generator into this soon, but that media ID will actually work once there's a video uploaded to it basically. Anyway, hope that helps.