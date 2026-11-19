---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Cw3D3eyrf-t.txt"
words: 318
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Cw3D3eyrf-t

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Cw3D3eyrf-t.txt` — حساب: airesearcherguy — إنستجرام — فيديو Cw3D3eyrf-t

---

I finally did it. I created an AI generated image slideshow video with AI generated music soundtrack, all automated. So you know all those gurus that are always talking about faceless YouTube videos, where you like play stock footage and have meditative music in the background? Well, I figured out how to automate that. Now before I show you the output, I'm not happy with the size of the image, and that's because I still have to play with it. Problem is the bigger the image, the longer it takes to render, and a make. Com scenario can only run for 40 minutes before it automatically shuts down. Originally I tried to generate like 48 images all 1080 by 1080, and that definitely didn't work. So what I generated is bare bones. There's a few different ways I can play this. I could try to double scale the output. I could use webhooks and split it up across multiple scenarios. I'm not really sure what I'm gonna do yet, but I do wanna show you what this looks like. Now let me show you how I created it. First we have the topic rotator. Then we have GPT create 11 image prompts based on the theme from the topic rotator. This splits up the table into 11 prompts. All of these are stable diffusion api. Com API calls to the SDXL model, and they're all set to sample four. So it's 11 of them all outputting four images each. And then this calls a new API I just found called beatoven. Ai that generates music. So these create the audio track, and then transloadit stitches all the images and the audio track together into a video. There's a lot of instructions that go along with that, so it's gonna be a few days before I can add it to the bundles, but I'll have it available soon. Cheers.