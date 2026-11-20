---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_0.txt"
words: 1372
sha1: 613697bec781e70228892c55f3ac47339cdec502
lang: en
account: divyannshisharma
quality: ocr+carousel-9
---

# S_igocr_divyannshisharma_DavP09SEuon

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_0.txt`
> الأجزاء: 9 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DavP09SEuon_8.txt`

<!-- image 0 -->
How to run
Claude code
in autopilot
<!-- image 1 -->
2
THE PROBLEM + THE 3 TIERS
There’s a full automation stack
But most people never use it.
THE AUTOMATION STACK
LOOP
TIER 1 · THE MANUAL
/loop · CronCreate · CronList · CronDelete
Session-scoped. Up to 50 tasks. Auto-expires after 7 days.
Dies when you close the terminal.
PERSISTENT LAYER
TIER 2 · THE PERSISTENT LAYER
Desktop scheduled tasks · Auto Mode · Permissions
Survives restarts. Runs while the machine is awake.
macOS and Windows only. Linux uses /loop or system cron.
CLOUD LAYER
TIER 3 · THE CLOUD LAYER
Routines · schedule · API trigger · GitHub event
Anthropic-hosted. Laptop can be off. Released April 14, 2026.
All paid plans in research preview.
Most people use Claude like this:
open it, type a prompt, read the answer, close the tab,
come back tomorrow and repeat.
That’s supposed to work FOR you
is still waiting on YOU to show up.
<!-- image 2 -->
3
TIER 1: /loop
The fastest way to
schedule anything
in Claude Code.
Your prompt
Gather context
Take action
Verify results
Done
agentic loop
You: interrupt, steer,
or add context
⚡ Type inside any session:
/loop 10m check the deployment status
🕒 That's it. Claude checks it every 10 min,
no setup.
💬 Works in plain English too:
→ every weeknain English too:
→ every weekday at 7am, summarize overnight commits
→ every hour, check for new support tickets
→ at 6:30pm today, post a status update to Slack
<!-- image 3 -->
4 TIER 1: /loop WITH /goal
Loops alone
aren’t enough.
Pair /loop with /goal.

Loops alone have a problem:
Claude does 30 of 50 tasks, calls the rest "handled," and bails.

Fix it:
/loop 5m process the rest "handled."
don’t stop until the queue is empty

Now Claude keeps going until it’s actually done.
Not "good enough." Done.

Use it for:
→ fixing flaky tests until zero fail
→ processing a queue until it’s clear
→ investigating a bug until one theory holds

* Without /goal — You Are the Loop
You prompt → Claude works → Claude stops → You review
You review again ← Claude stops ← Claude works ← You prompt again
You are the bottleneck. Every turn requires your input to continue.

* With /goal — Claude Closes the Loop
You set the goal → Claude works → Evaluator checks → Not done → Claude starts next turn
Done ✓ → Goal cleared
You are removed from the loop. Claude works until the condition is met.
<!-- image 4 -->
5 Tier 2: Desktop scheduled tasks
Runs later. Survives restarts.

Claude
Schedule
Automate tasks that run later
New task
Create a one-time or recurring task
New task
Create a brief
Task name
Daily research
Instructions
Search the web for top AI news and research from the past 24 hours. Summarize the 5 most important items with sources and key takeaways.
Schedule
Every day
Every day at 8:30 AM
Time zone
(UTC-7) Pacific Time (US & Canada)
Claude will use
Default (Claude 3.7 Sonnet)
Notifications
Default (Claude)
Notify me when this task runs
Cancel
Create task

All scheduled tasks run in the cloud. Learn more

New scheduled task
Task name
Daily research
Instructions
Search the web for top AI news and research from the past 24 hours. Summarize the 5 most important items with sources and key takeaways.
Schedule
Every day
Every day at 8:30 AM
Time zone
(UTC-7) Pacific Time (US & Canada)
Claude will use
Default (Claude 3.7 Sonnet)
Notifications
Default (Claude)
Notify me when this task runs
Cancel
Create task

What /loop can’t survive a restart. This fixes that.
Schedule → New task → New local task
Set the prompt, the cadence, the folder.
What you get: survives reboots, every run starts fresh (no leftover context), permissions locked per task.
What it still needs: your laptop awake.
If it sleeps, the run gets skipped — turn on “Keep computer awake” in Desktop Settings.
<!-- image 5 -->
6
Permissions
that don't
babysit you
Less friction. More flow.
my-app — claude — 80x24
Claude
claude-code
~ /code/ sonnet-4-6
my-app
Claude Code v2.0.76
• Auto permissions mode enabled.
Claude will make changes without asking.
Review commits before pushing.
By default Claude asks before every action.
Fine when you're not watching. Useless when you're not.
Set rules instead:
Always allowed → reading files, running tests, checking git status
Never allowed → force pushing, deleting everything, editing .env
Or let Auto Mode decide. Anthropic found users approve 93% of prompts anyway —
Auto Mode handles that 93%, you only get pinged on the risky 7%.
Pick Permissive, Balanced, or Restrictive. Comes with
prompt-injection scanning + a full audit trail.
(Max/Team/Enterprise/API — not on Pro yet.)
Rule of thumb:
cheap to undo = auto-approve. Expensive to undo = never.
<!-- image 6 -->
7
Tier 3: Cloud routines
Your laptop off. Work still on.
Automate this →
Today
TO DO
Create docs for new features
Investigate alerts
Clean up flaky tests
Comb the backlog
attempt a fix, and open a draft PR.
claude.ai/code/routines/new
New routine
Name
Comb the backin
Select a trigger
Pull the top issue from Linear, a
Schedule
Weekly, Mon 9:00 AM
GitHub event
Runs when a GitHub webhook event fires
API
via the /fire endpoint
Trigger from your own code
The most powerful tier — your laptop can be completely off.
Set up at claude.ai/code/routines or type /schedule in Claude Code.
Each routine = a self-contained prompt (be specific, no follow-up questions)
+ repos + connectors (Slack, GitHub, Linear, Drive) + permissions + a trigger.
3 that pay for themselves:
☀️ Morning briefing — pulls overnight issues, classifies severity,
posts to Slack before you wake up
🔍 PR review pass — flags security/style issues before a human even opens the PR
📄 Doc drift detection — catches docs that didn’t get updated
with the code, opens a fix PR
By default routines can only push to branches starting with claude/ —
a bad routine can’t touch main.
<!-- image 7 -->
8 Trigger routines from anywhere
No schedule. Just events.
New routine
Name
pr-_triage-bot
Add trigger
Runs as jared@spacetowerdev.com
Filter (optional)
+ Add a filter condition
Without a filter, the routine fires on every matching event.
or choose event
Fires only on Pull request opened
Add trigger
Runs as jared@spacetowerdev.com
Filter (optional)
+ Add a filter condition
Trigger this routine from external systems by sending a POST request to the URL below with your token.
URL
https://hooks.routines.dev/pr-triage-b...
Token
rt_live_8f2CEPcHdFa
Regenerate
Delete
Example curl
> Triggering invalidates the previous token immediately.
> Delete the token to disable API triggering for this routine.
Done
Select a trigger
Schedule
Runs on a recurring cron schedule
GitHub event
Runs when a GitHub webhook event fires
API
Trigger from your own code via the /fire endpoint
Connectors
4
Connectors
All connected integrations are included.
Remove any you don't need for this routine.
Permissions
GitHub x Linear x
Routines don't need a schedule.
Any system can fire one.
API trigger — one HTTP call from anywhere:
→ CI fails → routine investigates, opens a fix PR
→ PagerDuty alert → routine triages, posts context to Slack
GitHub trigger — connects straight to GitHub events:
→ PR opened → first-pass review comment
→ issue created → labels + linked code
→ release published → routine writes the changelog
Set it once.
Every future event handles itself.
<!-- image 8 -->
9 The full stack + what wastes money
Build smart. Spend less.
claude
kicks off N tasks
N can be in the 100s
TASK 1
TASK 2
TASK N
implementer
verifiers
fixer
returns when done
AGENT TEAMS
DYNAMIC WORKFLOWS
When it's all connected: Skills = your recipes, Routines = what triggers it,
Auto Mode = handles permissions, Audit Logs = your morning review.
You don't need all of it day one. Week 1 → first loop. Week 2 → Desktop task.
Week 3 → Cloud Routine. Week 4 → Skills + Workflows once it gets complex.
Mistakes that cost you:
✗ never trying /loopo — it's free
✗ forgetting the 7-day expiry
✗ Opus for every automation — Sonnet's cheaper and does the job
✗ no goal — Claude stops at "good enough"
✗ blanket-approving everything
✗ vague routine prompts — ambiguous in, random out
✗ running heavy automation on Pro — rate limits will ruin your day