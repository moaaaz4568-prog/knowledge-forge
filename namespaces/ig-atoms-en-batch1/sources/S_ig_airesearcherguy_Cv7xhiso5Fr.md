---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Cv7xhiso5Fr.txt"
words: 463
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Cv7xhiso5Fr

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Cv7xhiso5Fr.txt` — حساب: airesearcherguy — إنستجرام — فيديو Cv7xhiso5Fr

---

So GPT-4's architecture has been leaked. Apparently the large language model's structure was behind a paywall and somebody decided to share it on Twitter. It has since been taken down from Twitter, but not before a bunch of publications picked it up. So let's go over what it revealed. First, we'll go ahead and gloss over the boring stuff, the stuff that we already expected, like how much it costs. We know it's gonna cost money. The fact that there are GPUs distributed around the world and the fact that training is done in batches. Now let's get on to the juicy stuff. First is the obvious one, parameters. GPT-4 has 1.7 trillion parameters. However, that's just for the text that it was trained on. Since it also leverages encoded data, meaning that it can take video and other media inputs, once you include the visual encoding, parameters actually jump to 2 trillion, which is currently the most for any large language model on the market at this point. Here's the thing though, hitting 2 trillion parameters for every generated token would be insane. It would cost too much, it would take too long. So that's why GPT leverages a strategy called mixture of experts. And this is essentially where it batches together information in particular subjects and only the relevant batch is accessed for any given query. That way it actually only utilizes a fraction of the available parameters at any given time. GPT has 16 MoEs, each utilizing 100 billion parameters. Now let's talk about the dataset that it was trained on. This is books, a lot of scientific papers, and then a bunch of stuff from GitHub. It was trained on about 13 trillion tokens, so that's a lot of information. Now for the most interesting part of this, it's the speculative decoding. So apparently GPT-4 utilizes a smaller, faster model that basically takes the information and summarizes and outlines it before passing it on to the larger oracle model. So this is like what a lot of us actually do when we use GPT-3. 5 16k to summarize something with a lot of text before we give it to GPT-4. And this is where most people think the decline in quality that GPT-4 recently saw is coming from. Because apparently the oracle was accepting a lower threshold. And what that means is it was being less strict about some of the outputs of the smaller, faster model. So the larger model's inputs were lower quality and therefore outputs were lower quality. Anyway, that's the stuff that I found interesting, but definitely look up the leaked information yourself if you're a nerd like me and you want to look at all the data. Hope learning about this was fun. Cheers.