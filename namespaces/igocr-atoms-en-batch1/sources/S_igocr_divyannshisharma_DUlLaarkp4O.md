---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_0.txt"
words: 930
sha1: 2c76daff0209d35329a948a2e94c2b56f49c74a0
lang: en
account: divyannshisharma
quality: ocr+carousel-19
---

# S_igocr_divyannshisharma_DUlLaarkp4O

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_0.txt`
> الأجزاء: 19 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_11.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_12.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_13.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_14.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_15.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_16.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_17.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DUlLaarkp4O_18.txt`

<!-- image 0 -->
antfarm dashboard
feature-dev
@divyanshsharma
HOW TO SETUP A TEAM OF
AGENTS IN OPENCLAW:
IN JUST 1 COMMAND
SWIPE FOR MORE
<!-- image 1 -->
Divyanshi | Agentic AI Expert
@divyanshisharma

Your lobster will then be able to manage an agent team and have
them execute repeatable, deterministic workflows built right on top of @openclaw
Say hello to Antfarm -
1. It's free and open source
2. You get a dashboard to visualize what's happening ...

antfarm dashboard
<!-- image 2 -->
Divyanshi | Agentic AI Expert
@divyanshisharma

And you can click into a task to see all the details, including the user stories (with acceptance criteria) that your agent team is cranking through ...

antfarm dashboard
feature-dev
Add user authentication with OAuth.
AI Assist
Created: Tue 8:53AM Updated: Wed 8:41 AM
setup
implementation
verify
test
dr
review
Stories
6 / 13 Done
5-1 Create OAuth provider configuration module
5-2 Implement Google OAuth callback handler
5-3 Implement GitHub OAuth callback handler

PRE
Add CSV export for billing ...
Add audit logging for admin ...
Implement SSO with SAML ...
Add dark mode support ...

REVIEW
Add RBAC with role-based ...
Implement SSO with SAML ...
Add dark mode support ...
<!-- image 3 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
TL;DR:
One command installs a full agent team
Deterministic workflows: same steps & order
Agents verify each other's work
Each agent gets fresh context
YAML: defined, u can build your own workflows
Zero infrastructure: no Docker, no Redis
<!-- image 4 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
Install:
Tell your OpenClaw agent ...
bash
install github.com/snarktank/antfarm
One command provisions everything: Agent
workspaces, cron polling, subagent permissions.
→
<!-- image 5 -->
Divyanshi | Agentic AI Expert
@divyanshisharma

Agent team workflows included:

1. feature-dev (7 agents)
plaintext
plan → setup → implement → verify → test → PR → review

Drop a feature request. Get a fully tested PR – planned, built, verified, and auto-retried.

2. security-audit (7 agents)
plaintext
scan → prioritize → setup → fix → verify → test → PR

Point it at a repo. Get a security-fix PR – vulnerabilities ranked, patched and re-audited.
<!-- image 6 -->
Divyanshi | Agentic AI Expert
@divyanshisharma

3. bug-fix (6 agents)

plaintext
setup → fix → verify → PR
triage → investigate → setup → fix → verify → PR

Paste a bug. Get a fix with a regression test – reproduced, patched, and verified.

4. Quick example:

bash
$ antfarm workflow install feature-dev
✓ Installed workflow: feature-dev

$ antfarm workflow run feature-dev "Add user authentication with OAuth"
Run: a1fd5f3
Workflow: feature-dev
Status: running

$ antfarm workflow status "OAuth"
Run: a1fd5f3
Workflow: feature-dev
Steps:
  [done]  plan (planner)
  [done]  setup (setup)
  [running] implement (developer)  Stories: 3/7 done
  [pending] verify (verifier)
  [pending] test (tester)
  [pending] pr (developer)
  [pending] review (reviewer)
<!-- image 7 -->
Divyanshi | Agentic AI Expert
@divyanshisharma

Why it works:

Deterministic workflows:
Same workflow, same steps, same order. Not "hopefully the agent remembers to test."

Agents verify each other:
The developer doesn't mark their own homework. A separate state verifier checks every story.

Fresh context, every step:
Each agent gets a clean session using Ralph loops. No context window bloat. No hallucinated state.

Auto Retry and escalate:
Failed steps retry automatically. If retries exhaust, it escalates to you. Nothing fails silently.
<!-- image 8 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
How it works:
Define:
Agents as a role, workspace and steps in YAML. Each agent has a role, workspace, and strict acceptance criteria.
Install:
One command provisions everything: no Docker, queues, or external services.
Run It:
Agents work independently: claim tasks, pass context, SQLite tracks state, cron runs.
<!-- image 9 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
Minimal by design:
No Redis, no Kafka,
no orchestrator.
YAML + SQLite +
cron. That's it.
Antfarm is a zero-dependency TypeScript
CLI that runs anywhere OpenClaw does.
<!-- image 10 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
Built on the Ralph loop:
Each agent runs fresh, with memory persisted via git and progress files: Ralph's loop, scaled to multi-agent workflows.
<!-- image 11 -->
Divyanshi | Agentic AI Expert
@divyanshisharma

Add your own workflows:

• Bundled workflows are starters: define agents, steps, retries, and checks in YAML and Markdown.
• Full guide: docs/creating-workflows.md

yaml
id: my-workflow
name: My Custom Workflow
agents:
  - id: researcher
    name: Researcher
    workspace:
      files:
        AGENTS.md: agents/researcher/AGENTS.md
  - id: research
    agent: researcher
    input: |
      Research {{task}} and report findings.
      Reply with STATUS: done and FINDINGS: ...
    expects: "STATUS: done"
<!-- image 12 -->
Divyanshi | Agentic AI Expert
@divyanshisharma

Security:

Curated repo only:
Antfarm installs workflows only from the official repository. No arbitrary remote sources.

Reviewed for prompt:
Every Antfarm workflow is reviewed for prompt injection and malicious agents.

Community-driven:
Submit a PR to add a workflow: all contributions undergo security review.

Transparent by default:
All workflows are plain YAML and Markdown: fully readable before install.
<!-- image 13 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
Dashboard:
Monitor runs, track step progress, and view agent output in real
time with:
bash
antfarm dashboard
<!-- image 14 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
Commands:
1. Lifecycle
bash
antfarm install
Install all bundled workflows
bash
antfarm uninstall
Full teardown (agents, crons, DB)
<!-- image 15 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
2. Workflow:
bash
antfarm workflow run <id> <task>
Start a run
bash
antfarm workflow status <query>
Check run status
bash
antfarm workflow runs
List all runs
bash
antfarm workflow resume <run-id>
Resume a failed run
<!-- image 16 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
3. Management:
bash
antfarm workflow list
List available workflows
bash
antfarm workflow install <id>
Install a single workflow
bash
antfarm workflow uninstall <id>
Remove a single workflow
<!-- image 17 -->
Divyanshi | Agentic AI Expert
@divyanshisharma
bash
antfarm dashboard
Start the web dashboard
bash
antfarm logs
View recent log entries
bash
install github.com/snarktank/antfarm
Tell your OpenClaw agent
<!-- image 18 -->
clawdbot
239 Branches
main
ngutma
DON'T GET LEFT BEHIND
FOLLOW @DIVYANSHISHARMA