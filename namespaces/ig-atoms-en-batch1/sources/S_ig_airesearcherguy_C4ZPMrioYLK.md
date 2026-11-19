---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C4ZPMrioYLK.txt"
words: 522
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C4ZPMrioYLK

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C4ZPMrioYLK.txt` — حساب: airesearcherguy — إنستجرام — فيديو C4ZPMrioYLK

---

I cloned myself again. This time I created something I call a personality vector, but I wanted to use Claude instead of GPT-4. I really like the way Claude 3 Opus works, so I built a system around that, effectively cloning my writing style, tone, and personality for posting specifically on LinkedIn. Let me show you. The trigger is a form. I only have two questions on it, the topic and the context. The first input into Claude Opus is examples of my most recent LinkedIn posts, and all I tell it to do is read and assess the posts to understand the desired structure for a LinkedIn post. Here is the Claude API call. The system prompt tells it that it is a LinkedIn poster and its goal is to mimic me, and then it gives it those examples again for the purpose of outlining the structure of the posts. Then this is an API call to Voiceflow, and all I'm doing here is grabbing the vector database chunks. Then I'm giving those chunks to Claude Opus, telling it that these are vector store chunks of data representing a whole body of work of Anthony's social posts, telling Claude to read them, assess them, and use them as an outline for the desired personality, tone, and writing style. Then I call Perplexity AI, telling it that it's an internet searcher and that it just needs to gather the most recent data on a topic, and then I give it the topic from my form. Then I tell Claude, this is outside context from the internet on a topic. Please read this because it'll be used as context for your LinkedIn post. Then finally, Claude Opus is instructed to please write the LinkedIn post on this topic, and it's given the additional context from me myself. So when I ran it, I ran it about business automation, and the vector database search brought up a lot of awesome posts from me talking about business automation. And then the Perplexity API call brought back a bunch of really great information about business process automation and robotic process automation. So this was really good recent context. And then the LinkedIn post, I'm happy with it. Supercharge your business automations with AI. It addresses automation enthusiasts. This is something that I have definitely done in the past. Think about it, that's something I say a lot. Picture this, that's something I say a lot. Overall, I think it's a good post. And what can I do with that? Well, I could post it directly to LinkedIn if I want to, or I could put it in a Google sheet so that I can have some human oversight before posting it. But either way, I cloned myself for the purpose of LinkedIn posts, and I could do the same thing with every platform, and that would be how I would effectively automate my social media, and it'll sound human. Hope that helps. Anyway, this flow will be one of the flows available to Bot of the Month Club subscribers. Hopefully we'll see you in there. Cheers.