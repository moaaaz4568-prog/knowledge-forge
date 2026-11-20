---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/leadgenman/DWvofo7DbVG.txt"
words: 398
account: leadgenman
lang: en
quality: transcript
---

# S_ig_leadgenman_DWvofo7DbVG

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/leadgenman/DWvofo7DbVG.txt` — حساب: leadgenman — إنستجرام — فيديو DWvofo7DbVG

---

I have spent over six months building my perfect Claude code setup, and this is what it looks like. Let me break it down. Starting from hooks, these are hard safety rails with zero exceptions. They will catch things before they actually run. Like if I accidentally try to delete my entire Supabase production or push my OpenAI API key to public repo, the hook will catch the command, block it from running, and throws me a warning signal in my terminal. It will actually stop me before doing any damage. Then comes rules. So instead of just dumping everything in one massive prompt, everything is much more modular here. For instance, if I'm working on Stripe payments, it will load my billing rules. If I'm working on Supabase queries, it will load my database rule. If I'm building my landing page, it will load my front-end and component rules. So the goal here is Claude will only load those files which are relevant and nothing else to be context friendly. Then comes agents. These are specialist reviewers that will catch things I will miss on my own. For instance, bug agent will catch race conditions, null crashes and edge cases before they hit production. Another is security agent that will scan exposed API keys, missing RLS policies or any open endpoint. Another is performance agent that flags N+1 problem or anything that will kill my load time. And the front-end design agent will reject all the UI bad decisions and generic AI purpose slop. Now here the most important part is skills. These are custom slash commands that run your entire workflow. For example, slash ship will take my code from my machine all the way to a deployable Vercel build. Slash video editor will get my raw camera file, use Remotion to edit the entire video, put caption on it and add sound effects at the end. Slash review all agents will give me a clear merge or reject decision before anything goes live. And at the root, we have Claude. Md file. This is basically your brain of your project. You have your architecture, decisions, texts, everything live inside this one file. And lastly, settings will wire all of this together so nothing breaks or leaks your entire project. This entire thing is open source. Just comment files and I will send it your way.