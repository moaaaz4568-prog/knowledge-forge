---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_0.txt"
words: 546
sha1: 097644612602277b9d07e29b7a1d67d72220d669
lang: en
account: leadgenman
quality: ocr+carousel-9
---

# S_igocr_leadgenman_DZW4Q3bDaBo

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_0.txt`
> الأجزاء: 9 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZW4Q3bDaBo_9.txt`

<!-- image 0 -->
claude_setup.workspace
leadgenman 2026
set up claude code
in one hour
six blocks. ten minutes each. a real coding agent in your
terminal by the end.
first task
install
1
2
Launch
3
auth
CLAUDE.md
4
5
claude/
6
<!-- image 1 -->
before-you-start.md
00
before the clock starts
three things you need open, or block one stalls.
node 18 or newer
node --version should print v18+
a terminal you like
iTerm, Warp, or the built-in. Claude lives here, not a browser.
a claude account
pro, max, or an anthropic api key. you authorize once.
check -- zsh
$ node --version
v20.11.0
you are good to go
no signup walls inside the terminal. you log in from it.
<!-- image 3 -->
login.sh
02
0:10 -> 0:20
block two -- launch and log in
type one word, then authorize in the browser.
code-setup -- Manthan Patel
~/penanywhere > claude
Welcome to Claude Code
opening browser to authenticate...
logged in as manthan@leadgenman.com
run claude
browser opens
paste back - done
api key instead? export ANTHROPIC_API_KEY and skip the browser.
<!-- image 4 -->
CLAUDE.md
03
0:20 -> 0:30
block three -- give it a brain
one command writes the file that makes it stop guessing.
code-setup -- Manthan Patel -- zsh
~/penanywhere > /init
generated CLAUDE.md from your repo
CLAUDE.md
# Project: PenAnywhere
Stack: Next.js 15, Supabase, Stripe, Canvas 2D, Zustand
Rules:
- be direct, push back on bad ideas
- never touch /lib/engine without asking
- production-ready, no placeholders
/init scans your code. then you edit. this file is read every session.
<!-- image 5 -->
.claude/
04
0:30 -> 0:40
block four -- hire the team
four folders turn one assistant into a crew that knows your rules.
agents/
the specialists.
named experts you summon.
commands/
the shortcuts.
/deploy, /review, your repeatable moves.
hooks/
the safety rails.
scripts that fire before and after edits.
skills/
the playbooks.
reusable how-tos it loads on demand.
.claude/
mkdir -p .claude/{agents,commands,hooks,skills} -- one line scaffolds all four.
<!-- image 6 -->
settings.json
05
block five -- set the guardrails
decide what it can do without asking, once.
.claude/settings.json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Read", "Edit",
      "Bash(git status)"
    ],
    "ask": ["Bash(git push:*)"],
    "deny": ["Read(.env*)"]
  }
}
allow
runs silently
ask
stops to confirm
deny
never, full stop
secrets stay locked. deny your .env so it can never read your keys.
<!-- image 7 -->
first-task.sh
06
0:50 -> 1:00
block six -- give it real work
the setup is done. now make it earn its keep.
code-setup -- Manthan Patel
claude -- zsh
~/penanywhere > claude
> add a /pricing route with three tiers
and a Stripe checkout button
reading CLAUDE.md + settings.json
editing app/pricing/page.tsx
running npm run build
done · 1 route, 2 files, build passing
you described it. it read your rules, wrote the code, and
verified itself.
<!-- image 8 -->
recap -- the full hour
sixty minutes, start to shipping
here is the whole hour on one face.
first task
install
launch
.claude/
CLAUDE .md
auth
1
2
3
4
5
6
0:00 install
0:10 launch + auth
0:20 CLAUDE.md
0:30 .claude/
0:40 settings.json
0:50 first task
I you did not learn a tool. you built a coworker. you built a coworker.
<!-- image 9 -->
get-the-files.md
want the files I actually use?
my real CLAUDE.md, settings.json, and four starter folders,
ready to drop in.
Comment
"CODE"
I'll send the starter pack to your DMs.
@leadgenman