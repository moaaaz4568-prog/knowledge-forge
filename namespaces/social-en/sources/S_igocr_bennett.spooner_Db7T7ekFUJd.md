---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_0.txt"
words: 701
sha1: 9aecc9c6e90273dcca6144519c56bd689c144aab
lang: en
account: bennett.spooner
quality: ocr+carousel-9
---

# S_igocr_bennett.spooner_Db7T7ekFUJd

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_0.txt`
> الأجزاء: 9 — `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/Db7T7ekFUJd_8.txt`

<!-- image 0 -->
// BENNETTOS
01 / 09
// BUILD LOG - MULTI-AGENT
ONE PERSON.
A COMPANY
OF AGENTS.
The full stack for running a multi-agent
company locally – orchestrator, models,
gateway, and the metal it runs on.
@bennettos
SWIPE →
<!-- image 1 -->
// BENNETTOS
02 / 09
// THE MAP
SIX LAYERS.
ZERO EMPLOYEES.
- CLAUDE CODE HEADLESS
  01 - CONDUCTOR + DEPT
     HEADS (No API Cost)
- GLM-5.2 + CODEX
- MCP SERVERS
  05 - THE HANDS
- PAPERCLIP
  02 - THE BACK OFFICE
- HERMES
  04 - THE WORKER POOL
- MINI + TAILSCALE
  06 - THE METAL
03 - HERMES MODEL LANES
// LIVE ORG - CONDUCTOR + SIX X CREWS
@bennettos
SWIPE ->
<!-- image 2 -->
BENNETTOS
03 / 09
// 01 • CONDUCTOR + DEPT HEADS
CLAUDE CODE,
HEADLESS.
The Conductor and every department head are Claude
Code running headless – spanwed by Paperclip,
working in tmux, committing like a senior engineer.
It signs in with OAuth on the Max plan: no API key,
no per-token meter. The subscription is the payroll.
$ Claude -p # headLess : OAuth, not the API
@bennettos
SWIPE →
@bennettos
SWIPE →
<!-- image 3 -->
// BENNETTOS
04 / 09
// 02 • THE BACK OFFICE
PAPERCLIP
You never look at this dashboard. Paperclip runs behind the scenes – org hierarchy, tickets, heartbeats, budgets – while agents wake, pull work, and report back. The cockpit you actually watch just reads its board over the API.
$ npx paperclipai onboard
@bennettos
SWIPE →
@bennettos
SWIPE →
<!-- image 4 -->
// BENNETTOS
05 / 09
// 03 . THE MODEL LANES
GLM-5.2 +
These lanes belong to Hermes, not Claude. Workers run GLM-5.2 on Ollama Cloud – glm-5.1 for code, 4.7-flash for light work – with Codex on the ChatGPT plan as the second lane. Subscriptions and one flat key. Still no API meter.
CODEX.
$ export OLLAMA_API_KEY=*** # lane 1 - glm-5.2
$ hermes auth # lane 2 - codex, ChatGPT OAuth
SEATS
10
0
3
RUNNING NOW
OPENED
TASKS
RUNS - 24h
HEARTBEATS - 24h
17
4
- Sales
- Sumanizer
- Communicatio...
- Reflection C...
- Forge
- Hermes Work...
- Marketing/Dr...
- Conductor
- Finances
- TECH
TASK LANES
IN PROGRESS - 1
BLOCKED - 1
Bennett OS Cockpit
Paul FounderOS Cohort 1
@bennettos
SWIPE →
@bennettos
<!-- image 5 -->
06 / 09
// BENNETTOS
// 04 • THE WORKER POOL
HERMES
Nous Research's agent engine, Live on the board as a
hermes_gateway employee - 9 tools, 70 skills, its
own chat, cron, and MCP. The gateway binds loopback
on the mini behind Tailscale, so the whole worker
pool runs its own model lanes without a port open to
the world.
$ hermes gateway # 127.0.0.1:8642 · tailscale serve
@bennetos
SWIPE →
$ hermes gateway # 127.0.0.1:8642 · tailscale serve
REAL AGENTS
@bennetos
SWIPE →
<!-- image 6 -->
BENNETTOS
07 / 09
// 05 • THE HANDS
MCP SERVERS
Agents are only as useful as what they can touch.
MCP plugs real software into every layer of
the stack:
TRAKYO
ORGANIC CONTENT
ATTIO
CRM & PIPELINE
CANVA
CAROUSELS & CREATIVE
COMPUTER USE
BROWSER & DESKTOP
// AGENT TOOLS
attio canva trakyo stripe notion manychat fathom
tmux ollama
One config file. Every agent in the org inherits
the tools.
@bennettos
SWIPE →
<!-- image 7 -->
08 / 09
@BENNETTOS
// 06 • THE METAL
RAILWAY, OR
A MAC MINI.
A Mac mini in the room if you want sovereignty – Docker sandboxes every worker, and the OS answers only on your tailnet. Railway, if you want zero ops: two services, a volume, auto-deploy on push. Either way, Tailscale is the only front door.
$ docker compose up -d # worker sandboxes
$ tailscale up # the only front door
// OPTION A
MAC MINI M4
TAILNET-ONLY • NO OPEN PORTS • YOURS
// OPTION B – ZERO OPS
@bennettos
PRO • 24GB
OPEN PORTS • YOURS
RAILWAY ~$15/MO
SWIPE →
MAC MINI M4 PRO • 24GB
TAILNET-ONLY • NO OPEN PORTS • YOURS
// OPTION A
// OPTION B – ZERO OPS
@bennettos
RAILWAY
SWIPE –
<!-- image 8 -->
// BENNETTOS
09 / 09
// THE ENTIRE STACK - CONFIGS - ADAPTERS -
PROMPTS
COMMENT
"AGENT"
and I'll send you the entire stack - every
config included.
agent
SEND
@bennettos
// THE AGENT STACK