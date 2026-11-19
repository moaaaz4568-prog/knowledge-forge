---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/chase.h.ai/DNRLYRWxIv5.txt"
words: 587
account: chase.h.ai
lang: en
quality: transcript
---

# S_chase.h.ai_DNRLYRWxIv5

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/chase.h.ai/DNRLYRWxIv5.txt` — حساب: chase.h.ai — إنستجرام — فيديو DNRLYRWxIv5

---

It's never been easier to create multi-agent setups without knowing any code than it is today. And let me prove it to you by creating a multi-agent setup just like this in 60 seconds. Okay, so here I am inside of N8N, and we're gonna create our AI agent infrastructure to start. So this first guy, this is our orchestrator agent. This is what we are going to talk with, and this is what's gonna control all the sub-agents. Now to create those sub-agents, I just go to tools and I search for AI agent tool. Now once I'm inside here, I'm gonna click this button. That's gonna let essentially the top orchestrator agent control this sub-agent's prompt. And then I'm gonna rename it to research. Then I'm gonna copy it, just Control C, Control V, connect this guy, but this guy we're gonna call email. Right, so now I have this orchestrator agent and his two sub-agents all ready to go. Now we just need to add a chat model and then the actual tools. Now for the chat model, I just click this. I scroll down to OpenAI. We're gonna use 4. 1 mini, that's totally fine. And we need to connect that to all the agents. So just drag and dropping, we now have three agents connected to this singular model. Now time for the tools. So for the research tool, we're gonna use Tableau. So I'm just gonna put in Tableau. You could do Perplexity, you could do Google SERP, whatever. But for the query, we're gonna have the AI decide. So this means the search will be based on what the AI thinks we want. So based on the chat message up here, it's gonna go all the way down to the research agent, which uses that tool. For the email tool, we're just gonna search for Gmail and same kind of deal, right? I'm gonna have AI figure out who the two is, what the subject is, and what the message is. Now it doesn't just make it up randomly. It uses its brain based on the conversation we have with it to make those decisions. Lastly, I'm gonna add some memory and simple memory will work fine. And just like that, you now have a multi-agent setup with our main orchestrator agent and then two sub-agents, the research agent and the email agent. And obviously they're simplistic with only one tool, but we could add more and more and more tools. But that's how easy it is to put it together with no code. And now let's test it. So I told our agent do some research about GPT-5 and then send an email to Chase talking about that research. All right, it said it did it, so let's check out the email. All right, so here's the email it sent us with all the research about GPT-5, and we could go inside the system prompt and actually make the sound way better if we wanted to. This was just a demo to actually see if it would do what we told it. So there you have it. That's how easy it is to make a multi-agent setup without any code. And again, very simplistic, but it was just a demo and you can make it more and more sophisticated as you add more and more tools. Now if you wanna dive deeper into this stuff, get guides and templates, just comment agent below and I'll send them to you.
