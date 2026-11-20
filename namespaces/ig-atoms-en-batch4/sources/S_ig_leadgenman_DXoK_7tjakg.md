---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/leadgenman/DXoK_7tjakg.txt"
words: 475
account: leadgenman
lang: en
quality: transcript
---

# S_ig_leadgenman_DXoK_7tjakg

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/leadgenman/DXoK_7tjakg.txt` — حساب: leadgenman — إنستجرام — فيديو DXoK_7tjakg

---

If you're using Claude Code and you don't know about these three things, then you're only using 10% of it. First is agent teams. Most people only know about sub agents, but Claude Code has something way more powerful called agent teams. Sub agents are just contractor you send for one specific job. But with agent teams, you are deploying full parallel agents that can actually talk with each other. So we have one orchestrator agent that holds the plan and agent spawns their own context window limit without going through your main session context window. So whenever you are saying, "Hey, build me an authentication page, " three agents will split it up. One will handle the setup, another one will handle the API, and last one will handle the testing. All of them are coordinating with themselves to complete the job. You can turn on this feature by using this one command, Claude Code experimental agent teams equals to one. Second is your Claude. Md file or context management. Most people repeat the same context to Claude Code every single new session. For example, your tech stack, file structure, coding style, your do's and don'ts. But if you just drop everything inside your Claude. Md file, which lives inside your root folder, Claude will automatically read every single time when you open a new session. I have mine loaded with my Supabase schema, my component rules, and never to-do list. So every new session start with the knowledge of my project, and I don't have to waste my five minutes feeding the context anymore. You can also create your own Claude. Md file just by typing slash init inside your project, and Claude Code will draft that file for you. And then you can obviously customize and make it yours. And third one is honestly my favorite one. You can combine slash commands and hooks to give Claude Code superpowers. Slash commands are basically set of instructions where you just feed your prompt to once, and then you need to call it again. You can do it by using the slash commands. And hooks are actually what prevents anything funny happening inside your codebase. A hook is basically shell command script that runs automatically at a specific moment. For instance, whenever a single line of code change is made by Claude, the auto commit hook will make sure that everything is getting committed and keep track of. I have hooks for auto review, test, linter, and here you don't have to manage anything. The system manages itself. So these three things together make my Claude Code session feels like 10x developer and not just another chatbot. So if you want the whole setup, just comment word setup and I will send you my DMS, templates, and agent team setup guide inside your DMS.