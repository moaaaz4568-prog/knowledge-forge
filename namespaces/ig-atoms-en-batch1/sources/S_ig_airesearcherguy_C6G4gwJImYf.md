---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C6G4gwJImYf.txt"
words: 406
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C6G4gwJImYf

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C6G4gwJImYf.txt` — حساب: airesearcherguy — إنستجرام — فيديو C6G4gwJImYf

---

A day in the life of me trying to build an AI blog writer that produces quality content. There are quite a few tools out there that produce decent looking blog articles, but the content is so surface level. Whenever you try to give it more context so that it can write something deeper, it becomes repetitive and robotic. I've gone through so many iterations to try and get around that. The first content team bot that I built split off every section into its own. That saved on tokens. Unfortunately, it also caused a lot of repetition. In version two, I made it linear so that it was one single conversation. But this of course would require a language model with a large context window. Another element that I put in was in the system prompt, I defined the voice and the tone and personality by providing a bunch of pre-written examples. Unfortunately, those examples in the system prompt don't take as well as they do as an actual user prompt. So the next version would include the voice instructions or the personality examples in its own user prompt. The next version I would spend a lot of time building. I built two different tracks so that I could generate a blog based on either a keyword or idea I had or another article if I saw something that was interesting. Unfortunately, one of the downsides of giving it examples is that it would repeat the structure of attempting to sound human in the same places in every subsequent blog post. So then I had to build a mechanism that would not only eliminate repetition, but store previous writings and reference those and ask the AI to make sure that there wasn't any repetition within the post itself, nor would there be any repetition in the previously written post. The outputs are sounding pretty good now. Unfortunately, a single run costs about 150, 000 Claude Opus tokens. That can get pretty expensive. So now my next challenge is to build the entire thing again, but using Llama 3, which is a challenge because Llama 3 has a max token output of about 4, 000 tokens. But as I mentioned, the outputs look pretty good. Here's one, a pretty detailed article. It doesn't have repetition finally. It sounds human. It writes in my style. So all of that prompt engineering looks like it paid off. Cheers.