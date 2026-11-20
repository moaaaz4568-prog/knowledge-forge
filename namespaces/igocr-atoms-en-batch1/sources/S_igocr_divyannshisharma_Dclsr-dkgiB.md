---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_0.txt"
words: 1382
sha1: e867aa5998401db2f6885aa352ae46c6003f001f
lang: en
account: divyannshisharma
quality: ocr+carousel-10
---

# S_igocr_divyannshisharma_Dclsr-dkgiB

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_0.txt`
> الأجزاء: 10 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/Dclsr-dkgiB_9.txt`

<!-- image 0 -->
Your Claude Code
Is Burning
2-3× More
Tokens
Than It Should
<!-- image 1 -->
CLAUDE READS
TOO MUCH CODE

1. Claude reads the whole codebase to find one file

You say: "Fix the auth bug."

Claude may scan modules, configs and adjacent files before finding the right one.

Fix: Give Claude structured context + semantic search.

Less searching → fewer tokens.

WITHOUT
STRUCTURED SEARCH

✗
Full codebase
Scans everything
↓
Adjacent files
Checks related files
↓
Config
Reads configs
↓
Right file
Finally finds & edits
~30K+ tokens

WITH
STRUCTURED SEARCH

✓
Search: auth flow
Semantic search finds relevant code
↓
Relevant file
Directly jumps to what matters
↓
Edit
Makes the change
~1-2K tokens

Bottom takeaway:
Same task. Fraction of the context.
<!-- image 2 -->
STOP USING
OPUS FOR
EVERYTHING

2. Don’t use Opus for every task
Simple work doesn’t need your
most powerful model.

Haiku → search, locate, simple review
Sonnet → everyday coding
Opus → architecture + complex refactors

HAIKU
Simple
Search, locate,
simple review

SONNET
Normal
Nx refactors
Search, locate,
everyday coding

OPUS
Complex
Architecture +
complex refactors

Simple ——————————————— Complex

$ Opus is powerful.
Use it wisely.

Add routing rules to your
project instructions:

routing.md

1 # 3-Tier Model Routing
2
3 Haiku → locate code, grep, diff review
4 Sonnet → iterative development
5 Opus → architecture decisions only
6
7 NEVER use Opus for:
8 - File lookup
9 - Simple function questions
10 - Basic diff review

* Use the right model for the right job.
Smarter routing = lower tokens + faster results.
<!-- image 3 -->
TERMINAL OUTPUT
IS EATING CONTEXT

with noise

3. CLI output floods Claude with context

A command like `npm install` can dump
thousands of lines into context.

Claude processes them even when
the useful result is just:

"Installed successfully."

Fix: Filter verbose output before Claude
sees it.

CODE / RULE

# Block verbose output before context
if echo "$command" | grep -qE '(pytest|EXPLAIN|ANALYZE)'; then
    echo "Use batched/filtered output instead."
    exit 2
fi

output before context

BEFORE Verbose CLI Output

$ npm install
npm WARN deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it.
npm WARN deprecated glob@7.2.3: Glob versions prior to v9 are no longer supported
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN notsup Unsupported engine for thingies@1.5.0: wanted: {"node":">=18"} (current: {"node":"14.21.3","npm":"6.14.18"})
npm WARN notsup Not compatible with your node version: node>=18, npm>=8

added 1234 packages, and audited 1235 packages in 45s

128 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities

Before: +18K tokens

FILTER

AFTER Useful Output Only

$ npm install
Installed successfully.

After: only useful output
~50 tokens

Bottom line:
Filter noise. Save tokens. Keep context clean.
<!-- image 4 -->
CLAUDE FORGETS
BETWEEN SESSIONS

*
starts from zero

4. Every new session starts from ZERO

New session = re-explaining:
→ What you built
→ What you tried
→ What failed
→ What’s next

Fix: Use persistent project memory
so relevant context carries forward

CODE / RULE
# Example: index previous project conversations
memory-tool index ~/claude/projects/
--mode conversations

PERSISTENT
MEMORY ON
Feeds useful previous
context into Claude.

YESTERDAY (HAS CONTEXT)
Project knowledge exists.
Claude remembers.
Knows:
✓ What you built
✓ What you tried
✓ What failed
✓ What’s next

NEW SESSION (EMPTY)
Without memory, Claude
starts from scratch.
Knows:
– Nothing
– Nothing
– Nothing
– Nothing

Context carried forward

QUICK COMMAND
memory-tool index ~/claude/projects/ --mode conversations

Bottom line:
Enable persistent memory. Stop re-explaining. Keep momentum.

Retention line:
Enable persistent memory. Stop re-explaining. Keep momentum.
<!-- image 5 -->
STOP FEEDING CLAUDE
ENTIRE WEBPAGES

HTML into context

5. One URL can dump raw HTML into context

You need one GitHub issue.
Claude may receive navigation, headers,
footer, HTML and banners too.

Fix: Extract + compress external

Feed Claude what matters —
not the whole page.

CODE / RULE
# External content first.
Public URLs → fetch + index, then search
Never dump the full webpage inline.
Docs → fetch once per session
Never re-fetch unchanged content

60KB WEBPAGE (RAW HTML)
× Navigation
× Headers
× Footer
× Banners
× HTML noise
× Everything you don’t need.
BAD: Bloates context. Wastes tokens.

COMPRESS
Extract + summarize
useful content only.
Title
Description
Code / Details
Comments
Key info
Remove everything
that doesn’t help.

USEFUL CONTEXT ONLY
GOOD: Focused context.
Saves tokens.

BOTTOM LINE
Extract first. Compress hard. Feed
Claude only what matters.

QUICK COMMAND
memo-tool index ~/.claude/projects/
--mode conversations
<!-- image 6 -->
STOP RE-READING
THE SAME FILE

CONTENT
6. Claude can read the same file again…and again

File A → read
Later → read again
Another question → read again

Every read consumes context.
Fix: Reuse what’s already in the session.

* [Octopus icon]

/ RULE
CODE
# Anti-re-read rule
NEVER re-read a file already read during this session.
If you need it again, use what is already in context.

X BAD: WASTES CONTEXT
FILE A (same file) → Claude reads it → [READ AGAIN arrow back to file] → Claude reads it again
⚠️ Every read consumes context. Stop the loop.

✓ GOOD: REUSE IN CONTEXT
FILE A → [Document with lines] → Claude uses what’s already in context
✓ Already in context → REUSE ✓
Save these tokens. Saves money. Works faster.

* BOTTOM LINE
Don’t re-read. Reuse.
Break the loop. Save context.

>_ QUICK RULE
NEVER re-read a file already read during this session.
If you need it again, use what is already in context.
<!-- image 7 -->
MAKE CLAUDE
SAY LESS

CONTENT
7. Claude’s output costs tokens too

You often don’t need:
✗ Long preambles
✗ Huge comments
✗ Repeated summaries
✗ Full explanations after code

Fix: Default to short, direct output.

/> CODE / RULE
output mode
✅ Answer directly
✅ Avoid unnecessary preambles
✅ Don’t repeat the prompt
✅ Keep explanations minimal
✅ Expand only when requested

✅ CONCISE MODE
~1,000 TOKENS
</>
✅ Short. Direct. Saves tokens.

✗ DEFAULT VERBOSE
~3,000 TOKENS
</>
⚠️ Too long. Costs more. Harder to scan.

~65%
FEWER OUTPUT
TOKENS

💰 Fewer tokens
💲 Lower cost
⚡ Faster & easier to read

/> QUICK RULE (drop-in)
claude config set output_mode concise

* BOTTOM LINE
Default to short, direct answers. Expand only when you ask.
<!-- image 8 -->
THE FULL CLAUDE TOKEN STACK
FIX THESE 7 TOKEN LEAKS

THE PATTERN:
Better context
fewer wasted tokens.

CLAUBE CODE

HIGH TOKEN WASTE
SEARCH EVERYTHING
Unstructured search pulls too much.
WRONG MODEL
Big model for small tasks.
NO OUTPUT FILTER
Irrelevant, verbose output passes through.
NO MEMORY
Context is lost. Re-explaining every time.
RAW URL DUMP
Whole pages, headers, footers, junk.
RE-READ FILES
Same files read again and again.
VERBOSE OUTPUT
Long preambles, repeats, extra explanations.
RESULT: BLOATED CONTEXT. HIGH COST. SLOWER.

01 STRUCTURED CODE SEARCH
02 SMART MODEL ROUTING
03 CLI OUTPUT FILTERING
04 PERSISTENT MEMORY
05 URL COMPRESSION
06 REUSE FILE CONTEXT
07 CONCISE OUTPUT

LEAN CONTEXT
TARGETED SEARCH
Only relevant code. Less is more.
RIGHT MODEL
Small useful models for small tasks.
FILTER FIRST
Only useful output moves forward.
REMEMBER
No re-explaining. Context carries forward.
COMPRESS URLS
Extract what matters. Drop the rest.
REUSE CONTEXT
Don't re-read what's already here.
BE CONCISE
Short, direct answers. No fluff.
RESULT: LEAN CONTEXT. LOWER COST. FASTER.

7 LEAKS FIXED. 1 SYSTEM OPTIMIZED.
Code Search → Model Router → CLI Filter → Memory → File Reuse → Output Control
URL Compression
<!-- image 9 -->
FINAL TAKEAWAY

CONTENT
Claude Code doesn't need more context.
It needs better context.
Give it the right files.
Route work to the right model.
Filter noise.
Preserve memory.
Compress external content.
Reuse context.
Keep answers concise.

Better context.
Less noise.
Lower cost.
Same quality.

CONTEXT FILTER PIPELINE
(OPTIMIZED FLOW)

01 STRUCTURED CODE SEARCH
02 SMART MODEL ROUTING
03 CLI OUTPUT FILTERING
04 PERSISTENT MEMORY
05 URL COMPRESSION
06 REUSE FILE CONTEXT
07 CONCISE OUTPUT

MESSY INPUTS
(HIGH TOKEN WASTE)

CODE FILES
Unstructured,
duplicate,
irrelevant parts

LOGS
Verbose, repetitive,
low signal

HTML / WEB PAGES
Headers, footers,
nav, ads, junk

REPEATED FILES
Read again
and again

VERBOSE OUTPUT
Long preambles,
extra explanations

CLEAN CONTEXT
(LEAN & USEFUL)

RELEVANT CODE
Only what matters

RIGHT MODEL
Best fit for the task

NO NOISE
Only useful output

MEMORY PRESERVED
Context carries forward

COMPRESSED CONTENT
Small, focused
information

CONTEXT REUSED
No wasted reads

SHORT ANSWERS
Concise & direct

MORE CONTEXT ✕ → BETTER CONTEXT √

Better context.
Less noise.
Lower cost.
Same quality.