---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DLir1tnxLlG.txt"
words: 508
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DLir1tnxLlG

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DLir1tnxLlG.txt` — حساب: chase.h.ai — إنستجرام — فيديو DLir1tnxLlG

---

Let me teach you how to self-host your AI agents and your large language models for free on your computer using Docker and Ollama in the next two minutes. Step one, go to docker. Com, download Docker Desktop and install it. Step two, create a project folder on your computer's desktop, name it n8n-server. Once inside the folder, create a new text file. Open up the text file, put this text into it. This is going to be our Docker Compose file that creates the Docker container that has the local n8n image. If you don't know how to write this text, just go to ChatGPT, tell it to create a Docker Compose YAML file to run the latest n8n image. It's going to spit this out, copy and paste it into that file. Now make sure you name that text file docker-compose. Yml. Next, open up your terminal or your PowerShell if you're on Windows and type docker compose up -d. You now have n8n locally hosted for free on your computer and you can access it by going to localhost: 5678. Now let's locally host our large language model. Go to ollama. Com, download Ollama. Go to models, find a model you like. Let's look at DeepSeek. Let's use their 1. 5 billion parameter model, which is their smallest one. Next, go back to your terminal and you're going to type in ollama pull deepseek: 1. 5b or whichever model you chose. This is going to quickly download the large language model and congratulations, DeepSeek can now run on your computer for free. Now let's go inside our locally hosted n8n and let's connect our locally hosted AI. Search for AI agent, put that in there. Now go to add model and hit Ollama. Now let's create our credential. For the base URL, you're just going to do http: //host. Docker. Internal: 11434, save. Now you can test it out and talk to your large language model inside of n8n on your computer. And again, this is for free and your data stays here. It's not exposed to the internet at all. Now if you want to take this to the next level and actually make it production ready, you're going to have to hook up some sort of tunnel. And I do a deep dive on that on my latest YouTube video where I show you how to hook up Cloudflare to your locally hosted instance. This allows you to properly use webhooks and it allows you to do things like external triggers that you need if you're using these workflows for real. So go ahead and check it out. The guide is pretty easy to follow and assumes you're non-technical. And lastly, if you're looking for more AI guides like this, just check out my community. There's a link to it in my profile and it's all about getting you up to speed on all this different AI stuff if you're non-technical and you're not a coder. So I'd love to see you there.
