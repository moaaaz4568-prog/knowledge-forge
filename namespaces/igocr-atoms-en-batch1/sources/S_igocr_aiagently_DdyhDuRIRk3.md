---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdyhDuRIRk3_0.txt"
words: 450
sha1: c90116683f536217431a955a857913c97bd3b0b1
lang: en
account: aiagently
quality: ocr
---

# S_igocr_aiagently_DdyhDuRIRk3

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdyhDuRIRk3_0.txt`

<!-- image 0 -->
Build an AI Agent in 10 Minutes
No code. Every prompt to copy and paste.
Six steps.
context
1 Install Claude Code
The foundation everything else sits on. Pick whichever surface fits your workflow, set it up in under a minute, and everything below it compounds.
Terminal
npx -y @anthropic/claude-code
2 Build context
~/CLAUDE.md is the onboarding doc Claude reads before every chat.
Use Bori Cherny’s CLAUDE.md as a starting template. Ask me about your business, voice, banned words, output defaults, and how I want you to work. Save the final file to ~/CLAUDE.md
## Role
## Voice
## Brand guide
## Default
Claude reads
VSCode panel extension
CLAUDE.md
PASTE THIS
Help me build my CLAUDE.md from scratch.
Use Bori Cherny’s CLAUDE.md as a starting template. Ask me about my business, voice, banned words, output defaults, and how I want you to work. Save the final file to ~/CLAUDE.md
3 Build memory
Every correction becomes its own .md file. The same mistake never lands twice.
YOU
You correct
Claude saves
.md
PASTE THIS
From now on, whenever I correct you, save it as its own .md file at ~/claude/projects/[project]/memory/, prefixed free[project]_memory_, [reference]. Index every
MEMORY.md.
4 Build skills
One command fires a whole workflow across multiple tools, no retyping a 200-word prompt every time.
M
G
A
Output
PASTE THIS
Turn this workflow into a /{name:skill}
[describe trigger, inputs, outputs]. Create ~/claude/skills/{name}/SKILL.md, wire the MCP connectors I need (Notion, Gmail, Drive, etc.), and make it fire-able from any chat.
/your-skill
autopilot
One command fires a whole workflow across multiple tools, no retyping a 200-word prompt every time.
5 Build agents
Each agent gets one file and one job. Opus on the analyzing roles, Sonnet on the executing roles, with a 95/100 QA gate that fails any work below the bar.
STRATEGIST
Opus
BUILDER
Sonnet
QA GATE
95/100
PASTE THIS
Build me an agent team for [process]. Create one md file per specialist at ~/claude/agents/[name]/AGENT.md. Sonnet for executors. Ana-
lyzer/analysts, Sonnet for executors. Add a 95/100 QA gate that fails any work below the bar.
6 Run on autopilot
One job. Opus on the analyzing roles, Sonnet on the executing roles, with a 95/100 QA gate that fails any work below the bar.
Claude Routines turn your agent team into a cron job on Anthropic’s cloud, so you set it once and walk away.
UK → runs in cloud
Daily 8am → drops to Notion
Weekly Monday → drops to Notion
PASTE THIS
Create a Claude Routine that runs my [agent or skill]
every [schedule]. Run it on Anthropic’s cloud, not my Laptop. Drop the output into [folder, Notion page, or tool].
CLAUDE
AI Agent workflow
Follow Usama Akram for more