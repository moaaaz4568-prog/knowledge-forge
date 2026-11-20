---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/leadgenman/DWMPTvCDXcn.txt"
words: 436
account: leadgenman
lang: en
quality: transcript
---

# S_ig_leadgenman_DWMPTvCDXcn

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/leadgenman/DWMPTvCDXcn.txt` — حساب: leadgenman — إنستجرام — فيديو DWMPTvCDXcn

---

I have been using Claude Code for over a year now, and this is how I set up my Claude folder to get the best output. Let's start with agents. These are your AI teammates, each one trained on a specific job, and I have got six of them. For example, I have this code review agent that checks for bugs and security issues before anything gets merged. Then we have slash commands. These are your custom shortcuts where you just type your prompt once and you can rerun it anytime without retyping anything. I have this slash fix issue command where I just drop the GitHub issue number and Claude will automatically pull the issue and start fixing on it. Next, there are hooks. So these are rules that Claude always must follow. I have this pre-commit hook, so before Claude can commit any code, it runs all of these tests first, and if anything fails, the commit get blocks without any exception. Then there are rules. So instead of stuffing everything in one massive file, I break down into separate files. I have this frontend. Md for component patterns and styling, then database. Md for queries and migration, and Claude will only use the relevant ones to what it is actually working on. Then you also have skills. So these are instructions Claude follows when it recognizes a specific situation. For instance, I have this frontend design skill, and whenever I ask Claude to build a landing page or a website, it will follow this particular exact design standards, my color palette, my spacing, everything from that particular skill, and Claude will automatically choose when it needs to apply them. Now at the root, we have Claude. Md file. This is basically your brain of your project. It knows your tech stack, folder structure, build commands, test commands, and your entire coding convention all lives here. And Claude will automatically load this every single time when you start a new session. And lastly, settings. Json. This is your config file where you control which hooks are active, what Claude can run, and what is completely off the limits. And by the way, I run all of this inside VS Code with agent team mode, so that I can launch multiple agents in parallel, each with their own isolated environment, and all of them work together at the same time without overlapping or clashing anything. If you want me to send this complete guide on how to set up your Claude folder, just comment Claude, and I will send you straight away inside your DMs.