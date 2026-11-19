---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CwnTSKcIdtk.txt"
words: 346
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CwnTSKcIdtk

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CwnTSKcIdtk.txt` — حساب: airesearcherguy — إنستجرام — فيديو CwnTSKcIdtk

---

All right, so not so long ago, I made a bot that automatically generates an AI avatar video, which is basically a talking image video. And while a lot of people loved it, some people were like, ah, you know, the AI avatars look kind of creepy. Okay, all good to each their own. Guess what? I just created a bot, although I'm still in the process of perfecting it, that creates faceless slideshow videos with an audio track. Let's take a look. So I created a couple different versions of this one. This one uses my usual topic rotator. See, there are all my topics, and then has GPT write a script. The script is given to Eleven Labs to create an audio file, and then GPT writes a prompt based on the script for Midjourney, and then that's the slash imagine Midjourney API request. And here's where it gets interesting. The last API call is to a service called Transloadit, which basically stitches together all of the images that Midjourney creates. In that flow, it's all from one prompt. It just upscales all four of the images and then merges it with the audio file from Eleven Labs to create a slideshow video. And let me tell you, getting all this code and everything to work, it took me conferring with Code Interpreter and GPT and Transloadit's customer support several times, but I finally got it and it works. It creates a slideshow video with a voiceover, which you can't hear right now because I don't have a speaker, but you'll hear it in the next one. But yeah, I was really happy with how it worked out. So then I made a more epic one, but this one illustrates that you can change the inputs, right? So this is a Google Sheet that has a Robert Frost poem in it. That poem is then fed to GPT, who is told to create 10 image generation prompts and output them in a table. Then all 10 of those prompts are given to StableDiffusionAPI. Com.