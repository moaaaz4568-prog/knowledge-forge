---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_0.txt"
words: 1562
sha1: 6d766699295436dea4cf7816bf11f094bfcc17c6
lang: en
account: leadgenman
quality: ocr+carousel-16
---

# S_igocr_leadgenman_DbaV_gtEXuj

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_0.txt`
> الأجزاء: 16 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_11.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_13.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_14.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_15.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DbaV_gtEXuj_16.txt`

<!-- image 0 -->
CLAUDE CODE
15 Vibe Coding
Prompts
the exact prompt for every stage of the build
01
Write a Full PRD
02
Create Your CLAUDE.md
03
Ultra Plan Mode
04
Spec-Driven Development
05
Full UI & UX Design Brief
06
Implementation Plan
07
Wire Up an MCP Server
08
Connect Your Database
09
Find Security Gaps
10
Debug an Error Fast
11
E2E Test Your Application
12
Clean Up Dead Code
13
Write Clean Git Commits
14
Hooks as Guardrails
15
Turn a Task Into a Skill
<!-- image 1 -->
01
Write a Full PRD

PRD for the feature below.

Write a complete PRD for the feature below.

Feature: [DESCRIBE FEATURE]
Users: [WHO USES IT]
Stack: [YOUR STACK]

Include:

* Problem statement + success metrics
* User stories w/ acceptance criteria
* Scope: what ships in v1, what does not
* Data model changes
* Edge cases + failure states
* Open questions for me to answer

Keep it under 2 pages. Be specific, no filler.
Save it as docs/prd-[feature].md so every later prompt can reference it.
<!-- image 2 -->
02
Create Your CLAUDE.md

Scan this entire codebase, then generate a CLAUDE.md.

Include:

* What this project is, in 2 lines
* Tech stack + the versions that matter
* Commands: [DEV / BUILD / TEST / LINT] what to
do
* Architecture: where things live and week 1
* Code conventions you actually detect in the code
* Hard rules: [YOUR NON-NEGOTIABLES] -- without asking
never touch
* Gotchas a new engineer would hit in week 1

Write rules as short imperatives. Nothing generic --
only what is true for THIS repo. If you are unsure
about a rule, ask me instead of inventing it.
<!-- image 3 -->
03
Ultra Plan Mode
Enter plan mode. DO NOT write any code yet.
Task: [PASTE TASK] Constraints: [DEADLINE / STACK / NO-GO ZONES]
1. Read every file this task touches, list them with one line on what each does today
2. Map current behavior vs target behavior
3. Propose 2-3 approaches with real tradeoffs: complexity, risk, blast radius
4. Pick one and justify it in 3 lines
5. Break it into steps small enough to verify one at a time, each with its own check
6. List risks + the exact rollback for each
7. Flag anything touching [AUTH / PAYMENTS / PROD DATA] for my explicit sign-off
Then stop. Show me the plan and wait for my approval before touching a single file.
<!-- image 4 -->
04
Spec-Driven Development

We build specs first. Write a spec for: [FEATURE]
Context: [WHO USES IT + WHY NOW]

Spec format:

* Behavior: given / when / then, every case -- happy path, edge cases, failure states
* API contract: inputs, outputs, error shapes, status codes
* Data: schema changes + migrations needed
* UI states: loading, empty, error, success
* Non-goals: what this spec deliberately skips
* Acceptance checklist I can verify line by line

After I approve the spec, implement EXACTLY the spec. If reality forces a deviation, stop, update the spec, get my ok, then continue. The spec is the source of truth, not the code.
<!-- image 5 -->
05
Full UI & UX Design Brief

Create a full UI/UX design brief for: [SCREEN OR FLOW]

Audience: [USERS]
Brand: [COLORS / FONTS / VIBE]

Deliver:

* User journey through the flow, step by step
* Layout per screen: hierarchy, spacing, breakpoints
* Component inventory with every state – hover, empty, error, loading
* Typography + color tokens
* Motion: what animates, duration, easing
* Accessibility notes

Study patterns from [2-3 PRODUCTS YOU ADMIRE]
for direction. Never copy them.
<!-- image 6 -->
06
Implementation Plan

Create an implementation plan for: [APPROVED
SPEC / PRD]

Rules:

* Sequence steps so the app compiles and runs
after EVERY single step
* Each step: files touched, what changes,
how I verify it works
* Flag steps needing a migration or new dependency
* Put the riskiest/unknowns first
* Size each step: [S / M / L]

Output a numbered build sequence I can run one
step at a time. Wait for my "go" between steps.
<!-- image 7 -->
07
Wire Up an MCP Server

Wire up an MCP server for: [SERVICE / API]

What I need it to do: [JOBS TO BE DONE]

1. Check for an official or well-maintained existing server source -- name your src + the .mcp.json config, scoped to this project
2. If one exists: exact install command
3. If not: scaffold one with the MCP SDK -- tools, auth, responses error handling, typed re
4. Add ONLY the tools I will actually use: [LIST]
5. Wire secrets through [ENV VARS], never hardcode keys in the config file
6. Verify the connection and call one tool end to end, show me the output
7. Document each tool in 1 line so future sessions know when to reach for it
<!-- image 8 -->
08
Connect Your Database

Connect this app to [POSTGRES / SUPABASE / YOUR DB].

* Pick the client that fits this stack, justify it in 1 line
* Env vars: name them, add to .env.example, never commit real values
* Schema: tables for [ENTITIES] with types, relations, and indexes for [HOT QUERIES]
* Create + run the migrations, and show me the rollback for each one
* One typed query helper per table -- no raw SQL scattered through components
* Access rules / modeling if we are serverless, row-level security if this is [MULTI-TENANT]
* Connection pooling

Then prove it: seed one row, read it back, show me the output.
<!-- image 9 -->
09
Find Security Gaps
Audit this codebase for security gaps.
Attack it like you want in.
Focus areas: [AUTH / PAYMENTS / USER DATA]
[EXPENSIVE ENDPOINTS]
Check:
* Secrets in code, config, or git history
* Injection: SQL, XSS, command, path traversal
* Auth: routes missing checks, weak sessions,
broken redirects
* IDOR: can user A read user B's data?
* File uploads + input validation on every form
* Dependency CVEs -- run the audit, read it
* Rate limiting on high error messages and logs
* What leaks through logs
Rank findings by severity with exact file:line,
fix the critical ones now, and list the rest
as tickets with effort estimates.
<!-- image 10 -->
10
Debug an Error Fast

Debug this error. Do NOT guess.

Error: [PASTE FULL ERROR + STACK TRACE]
When it happens: [STEPS TO REPRODUCE]

1. Read the stack trace, open the exact files involved
2. State expected vs actual behavior in 1 line
3. List 3 hypotheses, ranked by likelihood
4. Prove or kill each one with logs or a tiny test -- evidence, not vibes
5. Fix the root cause, not the symptom
6. Search the repo for the same pattern -- if it can break here, it breaks elsewhere
7. Add a regression test that fails without the fix
8. Tell me in 2 lines why it broke and why it can never break this way again
<!-- image 11 -->
11
E2E Test Your Application

Write Playwright E2E tests for: [FLOW]
Stack: [YOUR STACK] CI: [GITHUB ACTIONS / OTHER]

* Money paths first: [SIGNUP / CHECKOUT / CORE ACTION]
* Test what the user sees, not implementation details
* Selectors: roles and labels, never brittle CSS chains
* One unhappy path per flow: bad input, network failure, expired session
* Tests stay independent -- any order, zero shared state, each seeds its own data
* Headless in CI, headed locally for debugging
* Screenshots + traces on failure only

Run the suite, show me the results, fix what fails, and tell me what the suite still does NOT cover.
<!-- image 13 -->
13
Write Clean Git Commits
Commit my staged changes properly.
Convention: [CONVENTIONAL COMMITS / YOUR FORMAT]
* Split unrelated changes into separate commits
* Format: type(scope): what changed and why
  feat / fix / refactor / chore / docs / test
* Subject under 50 chars, imperative mood
* Body explains the WHY, wrapped at 72
* Reference the ticket: [TICKET-ID]
* Never mix a refactor with a behavior change
  in one commit
* Never commit [SECRETS / .ENV / GENERATED
  FILES]
Show me the plan -- files per commit + messages --
before you commit anything. Then commit one at
a time so I can stop you between them.
<!-- image 14 -->
14
Hooks as Guardrails

Set up Claude Code hooks as guardrails here.

Stack: [YOUR STACK + PACKAGE MANAGER]

* PostToolUse: run [LINT + TYPECHECK] after every file edit, feed errors straight back
* PreToolUse: block edits to [PROTECTED PATHS: MIGRATIONS, .ENV, PROD CONFIG]
* Stop: run [TEST SUITE] before a session ends
* Notification: ping me with [SOUND / SLACK] when my input is needed

Write the hook scripts + the settings.json script under 20 lines and exit non-zero with a clear message so the agent knows exactly what to fix. Then trigger each hook on purpose and show me it firing.
<!-- image 15 -->
15
Turn a Task Into a Skill

Turn this repetitive task into a Claude Code skill.

The task I keep doing: [DESCRIBE TASK + STEPS]

* Create .claude/skills/[NAME]/SKILL.md
* Frontmatter: name + description with the exact trigger phrases I actually say
* Body: numbered workflow, my conventions, edge cases
* What it should ask me for vs infer on its own
* What "done" looks like

Then dry-run the skill on a real example and refine until the output matches how I do it by hand.
<!-- image 16 -->
Want all 15 prompts?
COMMENT
PROMPT
and I'll send the full pack
straight to your DMs