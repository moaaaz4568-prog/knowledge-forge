---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CoKkPjyOglp.txt"
words: 498
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CoKkPjyOglp

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CoKkPjyOglp.txt` — حساب: airesearcherguy — إنستجرام — فيديو CoKkPjyOglp

---

Stable Diffusion text-to-image AI is pretty amazing. It's one of the most advanced ones out there, but can you automate usage of it? Yeah, let me show you. All right, before I get into what I found with regard to Stable Diffusion, let's look at what your automation options are in Make. Com. You can actually use a module already created by OpenAI. This utilizes DALL-E 2. We're gonna test it real quick. So here I have the prompt, beautiful girl with cybernetic arm, cyberpunk style, hyperrealistic, 8K, Unreal Engine. And what it gave me for that prompt is okay, but this isn't something that I would want to use. You can also use an API with Make. Com. Another one I found was DeepAI. It's like five bucks for 100 generations, and one of the engines they have is a surreal portrait generator. Let's test that out to see the output real quick. Using the exact same prompt, this is what I got from DeepAI. As you can see, the quality is very similar to DALL-E 2. Not something I'd like to use. As a basis for comparison, we're gonna use Midjourney, which is arguably the best in this particular field. Unfortunately, you can't automate Midjourney because they don't have an API yet. This is Midjourney's output. That's a very, very market difference in quality. So I found this website called StableDiffusionAPI. Com. It offers API access to Stable Diffusion and Dreambooth. So here's an interesting thing. The reason why those other services don't have such great output is because they haven't been trained. You have to actually train the model that you're using. Now here on Stable Diffusion API, you can see there's a whole bunch of pre-trained public models. And that's cool because you get access to that with this API. So here's how you do it. You find a public model you like, and then you go to view code, and this right here is all the information you need, except for your API key, which you will input into Make. Com. So I copied the JSON from that public model, and then I replaced the prompt. I left their negative prompt though, because it's a really good negative prompt, and we're gonna run this and see what it comes up with. All right, this one requires an extra step where I had to actually send another API request to grab the output, but this was the output. Not quite where Midjourney is, but that's pretty good. And that was from the model that I chose. But as you can see here, there are a bunch of models to choose from, and then you can automate it in Make. Com. Now once it's automated, what can you do with it? Well, you can post it on your Instagram, you can insert it automatically into a blog post on your WordPress. The sky's the limit, really. You can do whatever you want with that image.