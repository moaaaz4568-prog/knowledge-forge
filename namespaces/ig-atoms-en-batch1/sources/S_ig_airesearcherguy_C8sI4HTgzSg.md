---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C8sI4HTgzSg.txt"
words: 454
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C8sI4HTgzSg

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C8sI4HTgzSg.txt` — حساب: airesearcherguy — إنستجرام — فيديو C8sI4HTgzSg

---

I cloned myself again. Seriously, what is my obsession with cloning myself? If you've followed me for a little while, you may know that I've been working really hard on essentially creating an AI agent that can output content that sounds just like me. In essence, I'm trying to clone myself. I've done this in a couple of different ways. One way that was pretty effective was using data chunks pulled from Voiceflow, but I really didn't like the idea of using an off-the-shelf RAG database because I couldn't control the chunk size and just things of that nature. So I wanted to be able to create my own. Then I tried to do this in Relevance AI, and while Relevance is a really powerful tool, I wasn't happy with the output. It kept coming back sounding robotic. It sounded like ChatGPT wrote everything. So I found a solution. I first created my own vector database using Qdrant and Natan, or Natan, however you say it. And then I created my own agent, and this time leaned on Sonnet 3. 5 as the language model for the output, and it does a phenomenal job at really replicating my voice, my tone, based on examples from other social media posts. So let's get into how I did that. So upserting documents into my own vector store was actually pretty easy with Natan. So I just uploaded all of the documents that I wanted inside of my Google Drive, connected that to Natan, and then connected a Qdrant vector store account, which is free. I created a cluster, and that's where all of this stuff will be stored, using the new text-3 small model for embeddings through OpenAI, and then the default data loader and recursive text. Actually, I can show you these. 4, 000 chunk size, a pretty big chunk size with 400 overlap. And then that's just the default data loader where I used. . . Yeah, this is where you tell it what kind of data it's taking in. So take that and put it from JSON to binary, and then either PDF or TXT or CSV. I had a bunch of different ones. Every time I ran it, I would have to change that depending on the file type. But yeah, and then just test workflow after each document, test workflow, test workflow. And here I have saved 74 megabytes of my 4 gigabytes of free storage in this cluster, and I have them separated by collections, which each represent the type of data that's in there. So yeah, Natan made it pretty simple. All right, and now using that Qdrant vector database, I have set up this cool little flow here.