---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/algorithmswithpeter/DLElIgnSzCY.txt"
words: 203
account: algorithmswithpeter
lang: en
quality: transcript
---

# S_ig_algorithmswithpeter_DLElIgnSzCY

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/algorithmswithpeter/DLElIgnSzCY.txt` — حساب: algorithmswithpeter — إنستجرام — فيديو DLElIgnSzCY

---

Hey Peter, how do those A I tools magically erase stuff from photos? Like I saw a guy disappear from a beach pic. What sorcery is that? Oh Stewie, that's not magic, that's machine learning flexin'. First, the A I uses a process called semantic segmentation. Basically, it scans the image with a neural network, usually a U Net, and labels every pixel. It figures out, hey, that's a person, let's mark 'em. So it's identifying what not to keep. Exactly. Once it has the object mask, we toss it into a generative inpainting model. Lately, everyone's using Stable Diffusion variants. It fills in the masked area by generating new pixels based on the surroundings, using a process called reverse denoising diffusion. Reverse what? Basically, it starts with static noise where the object was and slowly refines it step by step using patterns from nearby areas. It learns from tons of training images, so it knows how sand, sky, or sleeves are supposed to look. And it blends perfectly. Yep, it adds Poisson blending at the end to smooth the seams. Throw in color matching and boom, object gone. No trace, like Lois hiding my browser history. That's oddly specific. So's the algorithm.