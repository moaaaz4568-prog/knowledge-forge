---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_0.txt"
words: 881
sha1: 694877bc28442058048b499ea8d3332fe5b4b432
lang: en
account: leadgenman
quality: ocr+carousel-18
---

# S_igocr_leadgenman_DbhvmUJDXrv

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_0.txt`
> الأجزاء: 18 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_11.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_12.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_13.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_15.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_16.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_17.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_18.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbhvmUJDXrv_19.txt`

<!-- image 0 -->
My Production App Tool Stack
GITHUB
• code and ci checks
NEXT.JS
• frontend and backend
VERCEL
• hosting and deploys
CLOUDFLARE
• dns and ddos
SUPABASE
• database and auth
CLAUDE CODE
• writes every feature
INTERCOM
• live chat support
POSTHOG
• product analytics
RESEND
• receipts and logins
STRIPE
• every payment
BEEHIV
• newsletter to 25k readers
SENTRY
• catches errors
CODEx
• second agent on the repo
AGER.DEV
• background jobs
TRIGGER.DEV
• background jobs
N8N & ZAPIER
• ai automation & workflows
BETTER STACK & UPSTASH
• uptime alerts & cache
<!-- image 1 -->
Quick Reference:
When
to Use

I NEED TO… USE THIS
write and ship the code Claude code + codex
build frontend and backend next.js + typescript
store code and run checks github + actions
host it and deploy vercel
database, auth and storage supabase
take payments stripe
block bad traffic cloudflare
catch errors in production sentry
know before users complain better stack
see where users drop off posthog
cache and rate limit upstash + redis
ai automation and workflows n8n
send emails resend + beehiiv
<!-- image 2 -->
Layer 1:
The Builder

Claude Code:
• The agent that writes and ships every feature.
• Runs from the terminal, no editor open.

Next.js:
• Frontend, backend routes and server logic in one stack.

GitHub:
• Stores every line of code I ship.
• Typecheck, lint, tests and security audit on every push.
<!-- image 3 -->
Layer 2:
The Spine

• Hosts the app
and deploys
globally in
under a minute.

• Every push goes
straight to
production.

Vercel:

• Managed Postgres
with auth built
in.

Supabase:

• Row-level
security and one
source of truth.

• Processes
every payment.

Stripe:

• Checkout,
webhooks, refunds
and disputes.
<!-- image 4 -->
Everything Hits
This First
Cloudflare
• CDN, DNS, bot & DDoS protection.
• Blocks bad traffic before it reaches the app.
<!-- image 5 -->
Layer 3:
Keeping It Alive

Sentry:
• Catches every error
in production.
• Full stack trace
pings my phone.

Better Stack:
• Pings the site
every single
minute.
• Alerts me before
users
notice.
• Funnels and session
replays.

PostHog:
• Shows where users
drop off.

Upstash Redis:
• Caching and rate
limiting.
• Sits on every
public API
endpoint.
<!-- image 7 -->
What Goes in
Your CLAUDE.md

What to put in it:

Your stack and versions, the
folder layout, the commands to run
before every commit, and what it
should never touch.

Keep it short:

Every line gets read on every
single turn. So a bloated file
quietly burns your tokens all day.
200 lines in it is a sweet spot.
<!-- image 8 -->
Claude Code Prompts to Copy

Ship a feature:
"Build [feature]. Read how the repo already does this, match that pattern, then run typecheck and tests before you tell me it's done."

Write the tests first:
"Write failing tests for [feature] first. Show me them. Then write the code until every one of them passes."
<!-- image 9 -->
Debug Prompts to Copy

Debug from Sentry:
"Here's the Sentry trace. Find the root cause, not the symptom. Tell me what broke before you change a single line."

Before I merge:
"Review this diff like you didn't write it. Flag anything that breaks in production, then tell me what you would delete."
<!-- image 10 -->
Two Flows That
Run Every Day

Prompt →
Shipped:

I prompt it
Claude Code
writes it
CI checks pass
Vercel preview
then live

New user →
Paying:

Signs up
Supabase auth
Stripe checkout
Resend sends
the receipt
Intercom if stuck
<!-- image 11 -->
Three Files in
Every Repo

1. CLAUDE.md:
→ Your stack, your folder layout, and what
it should never touch.

2. .claudeignore:
→ Keeps build folders, lock files and huge
assets out of the context window.

3. The CI workflow:
→ Typecheck, lint, tests and a security
audit on every single push.
<!-- image 12 -->
Start with
Layers 1 and 2.

→ write down every tool.
→ keep what you need today.
→ everything else can wait.

WHAT MAKES THE CUT:

need it now
costs nothing

pick the smallest thing that
can take money.
<!-- image 13 -->
What to Add First.

higher

NEED IT

lower

paid

COST

free

Claude Code

Vercel

Supabase

Code

Next.js

GitHub

Cloudflare

Stripe

Intertool

beehiv

Upstash

Trigger.dev

Resend

WordPress

PostHog

Better Stack

Sentry

Cloudflare

Stripe

Intertool

beehiv

Upstash

Trigger.dev

Resend

WordPress

PostHog

Better Stack

Sentry
<!-- image 15 -->
PHASE 2
(DAYS 31-60):
Know When
It Breaks.
How I Find Out:
error
alert
my phone
posthog
add sentry, better stack,
and upstash.
this whole layer costs nothing
until you get big.
<!-- image 16 -->
An Error at 2am.
2am → 8am
error fires
sentry catches it
full trace hits my phone
claude code fixes it
→ vercel redeployed it.
→ nobody woke me up.
<!-- image 17 -->
PHASE 3
(DAYS 61-90):
Let Users Talk.
Get Found.

1k.

and
add resend, beehiiv, intercom and
trigger.dev.

LAYER 5:
blog in
wordpress
→
next.js
→
indexnow
→
google
know
→
google
sees it
fast
over
graphql
→
beehiiv run
25,000 readers.
ns about $117 at
ders.
<!-- image 18 -->
The Audit That Matters:

Day 30:
↳ it's live and someone actually paid you

Day 60:
↳ you find out it broke before a user tells you

Day 90:
↳ users can reach you and google can find you

if you can't check these, you're still dabbling.
<!-- image 19 -->
Check out my YT
video where I break
down everything
[Link in bio]

Claude Code
FULL ROADMAP

Vibe App
5.0

LEAD GEN MAN