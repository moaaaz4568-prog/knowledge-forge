---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_0.txt"
words: 1581
sha1: a9700a0afa100bda5a9753a08c61261445629dd0
lang: en
account: divyannshisharma
quality: ocr+carousel-11
---

# S_igocr_divyannshisharma_DZc2MSYEvk0

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_0.txt`
> الأجزاء: 11 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DZc2MSYEvk0_10.txt`

<!-- image 0 -->
How to build a
Claude
4-agent team,
that ships
(Exact Setup Inside)
SWIPE TO LEARN >
<!-- image 1 -->
here's how
most people
use
AI to
code:
plan
write
code
test
another
thing...
FIRE
FIRE
FIRE
FIRE
FIRE
You're still doing
all the connecting
manually.
You're still the
bottleneck.
</>
<!-- image 2 -->
SLIDE 3
The fix is
a pipeline.
4 specialist agents that hand off
to each other automatically.
One command kicks the whole thing off.
You wake up to a finished, reviewed,
tested feature.
No babysitting. No copy-pasting
between agents. No manual
work.
/ship-feature
1. PLAN
Understands the
request and
creates a plan.
2. CODE
Writes clean,
working code.
3. TEST
Tests everything
thoroughly.
4. REVIEW
Reviews, polishes,
and approves.
Feature
delivered
No
babysitting.
No copy-pasting
between agents.
No
manual work.
<!-- image 3 -->
SLIDE 4
How the
handoff
works.
Each agent writes its output to a
shared folder. The next agent reads
that file and picks up
exactly where
the last one stopped.
Planner writes →
.pipeline/spec.md
Coder reads spec, writes →
.pipeline/changes.md
Tester reads changes, writes →
.pipeline/test-results.md
Reviewer reads everything, writes →
.pipeline/review.md
One folder. Four files. Zero
confusion.
.pipeline/
spec.md
changes.md
test-results.md
review.md
<!-- image 4 -->
SLIDE 5
AGENT 1:
THE PLANNER

Job: turn a vague idea into a clear plan

It never writes code. It reads your codebase to understand how things are built. Then writes a detailed spec:

Exactly which files to change →
What functions are needed →
Edge cases to handle →
Questions if anything is unclear →

Think of it as the architect who draws the blueprint before anyone picks up a hammer.

EXPLORER
PROJECT
pipeline
planner.md
code.md
test.md
review.md
src
tests
README.md
package.json

# Planner Agent Configuration
version: 1.0
agent: planner-agent
id: planner-agent-001
created_at: 2025-05-20T08:30:00Z

## Role
Implement a user authentication endpoint with login functionality.

### Constraints
- Node.js with Express
- 3000 line tokens (30%)
- Use existing code style and patterns
- Follow security best practices and input sanitization.

### Acceptance Criteria
- Login succeeds with valid credentials
- Login fails with invalid credentials
- Returns HTTP 200 on success
- Returns HTTP 401 on failed attempts
- Unit tests written for auth logic

### Implementation Plan
1. Design request/response schema
2. Implement validation middleware
3. Add authentication logic
4. Write unit tests
5. Update API documentation

Note: Do not write any code yet.
<!-- image 5 -->
SLIDE 6
AGENT 2:
THE CODER
Job: build exactly what the
spec says.
Nothing more.
It reads the Planner's spec
Writes the actual code. Follows the patterns
already in your codebase Then writes a short
summary of what
it changed and why
It doesn't plan. It
doesn't review its own work.
It just builds.
</>
<!-- image 6 -->
SLIDE 7
AGENT 3:
THE TESTER

Job: prove that the code actually works

It reads what the Code Writer built
Writes tests covering:
→ The normal use cases
→ The edge cases
→ At least one failure case

Then it RUNS the tests
If anything fails → It stops and reports.
It does NOT try to fix the code itself.

One job. One output.
Find problems. Report them. Move on.

EXPLORER
PROJECT
.pipeline
planner.md
code.md
tester.md
review.md
src
tests
README.md
package.json

pipeline.md (implementation and context)
Tests (requirements and acceptance criteria)
Project dependencies and configuration
Responsibilities
Design and implement comprehensive tests
Execute tests and report results
Validate against acceptance criteria
Identify bugs, edge cases, and risks
Ensure code quality and reliability
Constraints
Do not modify source code
Tests must be deterministic and repeatable
Cover happy path, edge cases, and error scenarios
Follow existing test framework and conventions
Definition of Done
All tests pass
Coverage meets project standards (if applicable)
Acceptance criteria from plan.md are validated
Bugs and issues documented
Test results and summary included
Output
Test files with test cases, results, and findings
Reporting test files (e.g., *.test.js)
Any issues found if list is empty
Notes on quality, reliability, and preventing regressions.

Ln 1, Col 1 Spaces: 2 UTF-8 LF Markdown
<!-- image 7 -->
SLIDE 8
AGENT 4:
THE REVIEWER
Job: the final gate before anything reaches your codebase
It reads the spec, the changes, and the test results
Runs a git diff to see exactly what changed
Then gives one of three verdicts:
SHIP
— it's ready
NEEDS WORK
— here's exactly what to fix
BLOCK
— do not merge this
Important: the Reviewer can only read.
It cannot edit code. If it sees a problem, it flags it. That's your job to fix.
EXPLORER
PROJECT
.pipeline
planner.md
code.md
test.md
reviewer.md
src
reviewer.md
README.md
package.json
main
0
0
0
.pipeline
Agent Configuration
version: 1.0
owner: reviewer-agent
Prev: test.md
Next: planner.md
Status: completed
created: 2025-05-26T18:45:08Z
Goal
Perform a final review of the implementation and tests to ensure quality and readiness.
Instructions
Review (test results and findings)
- Code (augmentation)
- Tests (requirements and acceptance criteria)
Responsibilities
- Conduct a thorough code and test review
- Verify all requirements and acceptance criteria are met
- Check for code quality, security, and best practices
- Ensure tests adequately cover functionality and edge cases
- Provide clear summary and final recommendation
Constraints
- Do not modify source code or tests
- Remain objective, decisive, thorough, and constructive
- Flag all risks, issues, and concerns
- Follow project guidelines and standards
Definition of Done
- All acceptance criteria are met
- Code quality and standards are met
- Test coverage is adequate
- No outstanding issues or risks
- Final recommendation provided (approve / changes needed)
Output
- Review with review summary and recommendation
- List of issues or improvements (if any)
- The final step in the pipeline. Provide a clear go/no-go decision.
Ln 1, Col 1 Spaces: 2 UTF-8 LF Markdown
<!-- image 8 -->
SLIDE 9
THE ONE COMMAND
THAT RUNS ALL 4

You create one slash command
called /ship

Type: /ship add rate limiting to the login endpoint

That's it. The orchestrator: → Sends it to the Planner →
Waits for the spec → Sends spec to the Coder →
Waits for the code → Sends changes to the Tester →
Waits for test results → Sends everything to the Reviewer →
Shows you the final verdict

One line. Four agents. Full feature.

THE ORCHESTRATOR:

PLANNER
Sends it to the Planner
Waits for the spec

CODER
Sends spec to the Coder
Waits for the code

TESTER
Sends changes to the Tester
Waits for test results

REVIEWER
Sends everything
to the Reviewer
Shows you the
final verdict

>_/ship |

EXPLORER
PROJECT
.pipeline
H ship.md
tests
> ship.md
src
CODE.md
tester.md
reviewer.md
README.md
package.json

main √ ⚠ 0

.pipeline > H ship.md
# Ship.md
# Multi-Agent Software Delivery Pipeline
version: 1.0.0
description: Ship.md
created: 2025-05-26T18:45:00Z

# Orchestration Instructions
Execute the full 4-agent pipeline in sequence. Each agent runs only if the previous step completed successfully.

Pipeline Flow → Planner → Coder → Tester → Reviewer

# 1. Planner Step
- Read existing files: .pipeline/plan.md
- Update .pipeline/plan.md with detailed implementation plan
- Agent: Planner
- Output: Updated .pipeline/plan.md
- Stop pipeline on failure and report error

# 2. Coder Step
- Read .pipeline/plan.md
- Implement code changes based on the plan
- Create/modify code files in src/
- Agent: Coder
- Output: Updated code files
- Stop pipeline on failure and report error

# 3. Tester Step
- Read implemented code files
- Write comprehensive tests in tests/
- Run tests and ensure all pass
- Agent: Tester
- Output: Test files and test results
- Stop pipeline on failure and report error

# 4. Reviewer Step
- Read all artifacts: plan, code, tests
- Perform final review and create .pipeline/review.md
- Agent: Reviewer
- Output: .pipeline/review.md with verdict
- Stop pipeline on failure and report error

# Success Criteria
- All steps completed successfully
- .pipeline/plan.md exists
- Code files created/updated
- Test files created and passing
- .pipeline/review.md exists with "approved" verdict

# Error Handling
- Stop pipeline on any failure and why
- Do not proceed to subsequent steps

Ln 1, Col 1 Spaces: 2 UTF-8 LF Markdown
<!-- image 9 -->
SLIDE 10
WHAT YOU
WAKE UP TO

You typed one command before bed.

By morning you have:

A written spec of what was planned
The actual code written
Tests written and run
A SHIP / NEEDS WORK / BLOCK verdict waiting for you

You just do the final review and merge.
The pipeline did everything else.

z z
>_ /ship

SPEC
What was planned

CODE
What was written for you

TESTS
Written and run

SHIP
NEEDS WORK
BLOCK

Favorites
AirDrop
Recents
Applications
Desktop
Documents
Downloads
iCloud
iCloud Drive
Shared
Locations
MacBook Pro
Tags
Work
Projects
Personal
Ideas
Archive
All Tags...

.pipeline
Name
plan.md
code.md
test.md
review.md

Date Modified
Today at 6:12 AM
Today at 6:42 AM
Today at 7:18 AM
Today at 7:55 AM

Size
14 KB
89 KB
52 KB
31 KB

Kind
Markdown
Markdown
Markdown
Markdown

4 items, 183.23 GB available
<!-- image 10 -->
SLIDE 11
HOW TO
BUILD THIS
Start simple. Don’t wire all 4 at once.
Week 1 → Build Planner + Coder only. Run as a 2-agent chain.
Week 2 → Add the Tester once the first two feel solid.
Week 3 → Add the Reviewer as the final gate.
By week 3 you have the full pipeline running.
Each stage builds on the last.
WEEK
1
Build Planner
+ Coder only.
Run as a 2-agent chain.
PLANNER
CODER
WEEK
2
Add the Tester
once the first
two feel solid.
PLANNER
CODER
TESTER
REVIEWER
WEEK
3
Add the Reviewer
as the final gate.
PLANNER
CODER
TESTER
REVIEWER
Ship small. Iterate fast. Let the pipeline scale with you.