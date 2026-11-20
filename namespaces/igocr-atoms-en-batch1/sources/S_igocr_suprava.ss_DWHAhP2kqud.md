---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_0.txt"
words: 737
sha1: eed174c032f66342e8d12b2034af59160bed7c05
lang: en
account: suprava.ss
quality: ocr+carousel-11
---

# S_igocr_suprava.ss_DWHAhP2kqud

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_0.txt`
> الأجزاء: 11 — `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DWHAhP2kqud_11.txt`

<!-- image 0 -->
HOW TO GET
UNLIMITED LEADS
using LinkedIn + Claude Code
CLAUDE
CODE
<!-- image 1 -->
Suprava Sabat
What this clause system does:
• Finds leads on LinkedIn
• Sends connection requests & InMails
• Classifies cold email replies
• Runs autonomously
System Architecture
LinkedIn
PARALLEL FLOW: Email Replies
<!-- image 2 -->
Suprava Sabat
What You Need
• Claude Code
• Google Sheets (free)
• Slack (free)
• Modal (free)
• n8n (free)
• Instantly or Smartlead (if running cold email)
You own the system outright. Nothing recurring.
* Automation Stack
Google Sheets
(Free)
✓ Lead lists
✓ Data storage
✓ Campaign tracking
✓ Data storage
Memory
Instantly/Smartlead
(For cold email)
✓ Sending infra
✓ Sequences
✓ Deliverability
Voice
Slack (Free)
(Free)
✓ Alerts
✓ Logs
✓ Team updates
Feedback Loop
Claude Code
AI code for automations
✓ Prompting
✓ Code generation
✓ Workflow decisions
Claude Code
n8n (Free)
(Free)
✓ Connect APIs
✓ Automate flows
Nervous System
Modal (Free)
(Free)
✓ Run scripts
✓ Process heavy tasks
✓ Handle async jobs
Muscles
<!-- image 3 -->
Suprava Sabat

The Problem

Tools charge $80–$500/month

You still configure it yourself.

One mistake = account suspended or banned.

This system has zero flags for LinkedIn to detect.

LinkedIn

Access to your account has been restricted

Access to your account has been restricted because we detected fraudulent activity associated with your account. To learn more about account restrictions, visit our Help Center.

If you are in the European Union, additional information about your potential redress rights can be found here.
<!-- image 4 -->
Suprava Sabat
Step 1:
Google credentials → Google Cloud Console →
create new project
→ APIs & Services → Library → enable Google
Sheets + Drive API
→ Credentials → OAuth Client ID → Desktop App
→ Download JSON → rename to credentials.json
→ Drop into your project folder
Do this before anything else.
<!-- image 5 -->
Suprava Sabat
Step 2: Build the spreadsheet
Open Claude Code → paste the spreadsheet prompt
Claude builds 4 tabs:
• Sample Leads
• Blacklist
• InMail Queue
• Connection Queue
Replace sample leads with your real list.
<!-- image 7 -->
Suprava Sabat
Step 5: Install the browser agent
Run in terminal:
npm install @vercel/agent-browser
Reads pages using accessibility tree not CSS selectors.
Less tokens. Less bugs. More stable than Playwright.
Then Claude builds all browser actions on top of it.
Read 1 file (ctrl+o to expand)
Update (CLAUDE.md)
+ 2 lines, -2 lines, removed 2
- httpx, requests (HTTP clients)
- python-dotenv (env loading)
64 - python -m bun install per-video as needed:
65 + @anthropic-ai/agent-browser (browser automation)
66 + node -m bun install per-video as needed:
67 + agent-browser (browser automation)
68 # Google Sheets Integration
Updated CLAUDE.md - changed @anthropic-ai/agent-browser to agent-browser and run to npm.
[Pasted text #1 446 lines]
Opus 4.0
40%
780k/200k | main | youtube-demos
accept edits on (shift+tab to cycle)
<!-- image 8 -->
Suprava Sabat
What Slack looks like
Every reply notification shows:
• Lead classification (cold / warm / hot)
• Full thread summary
• Suggested reply ready to copy
• Direct link to Instantly inbox
Cold replies get a connection request sent immediately. Hot replies get nurtured.
<!-- image 9 -->
Suprava Sabat

Step 8: Build the n8n workflow

Warm or hot reply comes in: by email
• Find lead in Sample Leads sheet by email
• Do they have a LinkedIn URL? Validate it contains /in/
• Already in Connection Queue? → update priority to 1
• Not in queue? → use LinkUp to find LinkedIn → append as Priority 1
• Already sent? → ignore

Next time script runs they go first.
<!-- image 10 -->
Suprava Sabat
The live demo
It actually works.
Test leads: Gary Vee, Alex Hormozi, Leila Hormozi
• Agent visits profile
• Finds Connect button or clicks three dot menu
• Sends connection request
• All 3 went through live on camera
Add a note to your invitation?
Personalize your invitation to Alex Hormozi by adding a note.
LinkedIn members are more likely to accept invitations that include a
note.
Add a note
Send without a note
Alex Hormozi
Founder Acquired.com, Co-Founder Scalar
Scaling Startup
100K+ followers • 500+ connections
<!-- image 11 -->
Suprava Sabat
A quick summary:
• Claude Code builds it.
• Browser agent runs it.
• Slack tells you who replied.
• n8n handles the rest.
Save this. And comment “workflow” if you need a
detailed workflow on this.
Follow for more content on lead gen.
CLAUDE
CODE
Claude Code
builds it.
Browser agent
runs it.
Slack tells you who
replied.
n8n handles
the rest.