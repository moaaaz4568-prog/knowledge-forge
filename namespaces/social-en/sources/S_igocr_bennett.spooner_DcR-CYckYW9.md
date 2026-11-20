---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_0.txt"
words: 1123
sha1: e40c76255442e5ae479a2312669d93d51f57cd06
lang: en
account: bennett.spooner
quality: ocr+carousel-11
---

# S_igocr_bennett.spooner_DcR-CYckYW9

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_0.txt`
> الأجزاء: 11 — `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/bennett.spooner/DcR-CYckYW9_10.txt`

<!-- image 0 -->
// BENNETTOS
01 / 11
// BUILD LOG · MULTI-AGENT
A MULTI-AGENT
ARMY ON
ZERO API KEYS.
Three subscriptions. $240 a month. Flat. No
meter, no per-token bill, and enough capacity
to run a company of agents unless you're
running a large business.
@bennettos
SWIPE →
<!-- image 1 -->
BENNETTOS
02 / 11
// THE WHOLE BILL
$240 FLAT.
NOTHING METERED.

CLAUDE MAX / HEADLESS
CONDUCTOR + DEPT HEADS - AUTH, NOT API
$200

OLLAMA CLOUD / GLM-5.2
HERMES WORKER LANE - ONE FLAT KEY
$20

CODEX / CHATGPT PLAN
SECOND WORKER LANE - CODE EXECUTION
$20

TOTAL / MONTH
$240

// THE SAME WORK, ON THE METER
$15,000
VS
~$800

ONE heavy operator. ~93% of the bill disappears the moment you stop paying per token.
// SOURCE: REPORTED CLAUDE CODE MAX USAGE, 2026

API RATES - 10B TOKENS
SUBSCRIPTION - SAME 8 MONTHS

@bennettos
SWIPE →
SWIPE →
<!-- image 2 -->
BENNETTOS
03 / 11
// THE CHAIN OF COMMAND
CLAUDE DELEGATES.
IT DOESN'T TYPE.

■ CONDUCTOR / FABLE 5 OR OPUS 5
Reads the goal. Writes the plan.
OPUS 5
EXPENSIVE
Never reads raw output.

SPEC WRITERS
Brief a cheap model can't misread.

■ HERMES / GLM + CODEX
Do the work, spawn their own sub-agents, return a 1-page result.
THE HANDS

■ DEPT HEADS / CLAUDE x6
Turn one line of intent into a broker model can't misread.

// LIVE ORG // CONDUCTOR + SIX CREWS

@bennettos
SWIPE →

@bennettos
SWIPE →
<!-- image 3 -->
// BENNETTOS
04 / 11
// THE RESEARCH
ORCHESTRATION IS
THE TOKEN BILL.
Anthropic measured their own multi-agent system. The
numbers are why the delegation layer is the only place
worth optimizing.
15x
tokens of a plain chat for the
same task, once you go multi-
agent. A single agent already
runs ~4x.
// WHERE THE MULTIPLIER COMES FROM
Retries dragging
Orchestrator + verification
The actual work
Cost compounds at every handoff
a pricing problem.
80%
of performance variance on
their browsing eval is
explained by token usage
alone.
Context copied agent →
agent
Orchestrator + verification
dragging dependents
An architecture problem, not
SWIPE →
// SOURCES: ANTHROPIC ENGINEERING
BROWSECOMP ANALYSIS
@bennettos
SWIPE →
@bennettos
SWIPE →
<!-- image 4 -->
BENNETTOS
05 / 11
// THE ONE RULE
EXPENSIVE TOKENS
PLAN. CHEAP
TOKENS TYPE.

// CLAUDE · THINKING
DECOMPOSE.
SPEC. JUDGE.
Break the goal into
independent lanes
Write the acceptance criteria
up front
Read summaries, never
transcripts
Decide, then hand off and
forget
~5% OF THE TOKENS
~90% OF THE OUTCOME

// GLM + CODEX · TYPING
READ. WRITE.
REPEAT. REPORT.
Crawl the repo, the logs, the
Draft, refactor, classify,
transcribe
Spawn sub-agents for wide
sweeps
Return one page, not one
thread
~95% OF THE TOKENS
OFF THE CLAUDE METER

Every token Claude spends reading raw tool output is a token
spent twice: once to fetch it, once to carry it for the rest
of the session.

@bennettos

SWIPE →

لا يوجد نص
<!-- image 5 -->
06 / 11

// BENNETTOS

// THE WORKER POOL

THE
HERMES DOES THE
DIRTY WORK.

Hermes sits on the board as its own employee with its own
lanes: GLM-5.2 on Ollama Cloud, Codex on the ChatGPT
plan. A worker doesn't just answer a brief: it fans out
into sub-agents on someone else's plan, then hands back a
distilled page.

token brief from a
deep hand

INSIDE
~600

40K+

OUT
1-2K

$ hermes gateway # loopback + tailscale
$ hermes run --lane glm --summarize 1500 # cap

REAL AGENTS

@bennettos

SWIPE →

REAL AGENTS

@bennettos

SWIPE →
<!-- image 6 -->
07 / 11 01 CONTEXT
// BENNETTOS
// TOKEN OPTIMIZATION • 01 CONTEXT
STARVE THE CONTEXT WINDOW.

01 ISOLATE, DON'T ACCUMULATE
Stateless sub-agents measured 9K tokens where an accumulating pattern burned 15K. Same answer, 40% less.

02 CAP THE RETURN, NOT THE WORK
Explore for 50k tokens; report in 1,500. The exploration is disposable. The summary is what you carry.

03 OFFLOAD TO DISK
Plans, findings and tool dumps go to files; the window holds pointers. The plan survives a truncation.

04 COMPACT EARLY, ON PURPOSE
Auto-compaction fires near 85%. Recall is already degraded. Compact at task boundaries, from ~50%.

05 MAP FIRST, READ NARROWLY
A repo map to orient; full source only for files being edited. Grep is a worker's job, not the conductor's.

@bennettos
SWIPE →
SWIPE →
@bennettos
SHIPE –
<!-- image 7 -->
08 / 11
BENNETTOS
02 THE PREFIX
// TOKEN OPTIMIZATION •
PROTECT THE
CACHE PREFIX.
A cache read costs a tenth of a fresh read. On a long agent session that's the difference between a plan that lasts a week and one that dies Tuesday.

~90%
healthy cache hit rate on a stable prefix

10%
of base input price for a cached token

// WHAT BREAKS IT MID-SESSION
* Adding or removing an MCP server mid-session
* Switching models halfway through a run
* Timestamps or run ids in the system prompt

// THE HABIT
One stable system block per agent. Tools loaded per phase. Nothing rotating above the first user turn.
* ALERT AT ZERO HIT RATE, NOT AT MONTH END

@bennettos
SWIPE →
<!-- image 8 -->
09 / 11
03 ROUTING
// BENNETTOS
// TOKEN OPTIMIZATION • 03 ROUTING
A MODEL PER SEAT.

WORK
Decomposition, architecture, judgement
Briefs, review, merge decisions
Codogen, tests, execution loops
Bulk refactors, crawls, long reads
Watchers, cron, classification, triage

LANE
gement
■ FABLE 5 / OPUS 5
■ CLAUDE · SONNET
■ CODEX
■ GLM-5.2
■ GLM · FLASH

Routing is the cheapest optimization you have: nothing about the task changes, only which meter it lands on. Escalation is one-way: a worker can ask for a decision, never take one.

@bennettos

SWIPE →

// LIVE ROSTER • MODEL PINNED PER SEAT

Stats
Forms, Reruns,
Communications,
Connector
Fances
TIC

// LIVE ROSTER • MODEL PINNED PER SEAT
@bennettos
SWIPE →
<!-- image 9 -->
10 / 11 EST LIMIT
// BENNETTOS
// GUARDRAILS + THE HONEST LIMIT
WHAT STOPS IT
RUNNING AWAY.
A sub-agent that recursively spawns sub-agents, or a tool
returning a 200K-token dump, multiplies a run by 10x on its own.
The published research architecture ships no circuit breakers.
Yours has to.
DEPTH CAP
Two levels of spawn. A worker's
sub-agent cannot recruit.
PER-RUN BUDGET
Every ticket carries a token
ceiling. Overrun stops and asks.
OUTPUT TRUNCATION
Nothing over ~2K tokens enters a
window unsummarized.
WINDOW AWARENESS
Heavy Claude runs staggered across
the 5-hour window.
// WHERE THIS STOPS EARNING IS KEEP
Work that splits into independent lanes pays for delegation. Work
where every step depends on the last pays the multiplier without
earning it. Keep that on one thread.
@bennettos
SWIPE →
لا يوجد نص
<!-- image 10 -->
BENNETTOS
11 / 11
// ROUTING TABLE • BUDGET CAPS • WORKER
PROMPTS
COMMENT
"ARMY"
and I'll send the whole $240 stack: the
delegation prompts, the token caps, the
lane config.
army
SEND
@bennettos
// ZERO API KEYS