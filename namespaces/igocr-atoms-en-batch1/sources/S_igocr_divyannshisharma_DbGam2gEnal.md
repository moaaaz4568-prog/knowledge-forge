---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_0.txt"
words: 1568
sha1: fa716ce50d0df5a5ee398291df98fa6329882a50
lang: en
account: divyannshisharma
quality: ocr+carousel-11
---

# S_igocr_divyannshisharma_DbGam2gEnal

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_0.txt`
> الأجزاء: 11 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbGam2gEnal_10.txt`

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
No
copy-pasting
between agents.
No
manual work.
<!-- image 3 -->
SLIDE 4
How the handoff works.
Each agent writes its output to a shared folder. The next agent reads that file and picks up exactly where the last one stopped.
Planner writes → .pipeline/spec.md
Coder reads spec, writes → .pipeline/changes.md
Tester reads changes, writes → .pipeline/test-results.md
Reviewer reads everything, writes → .pipeline/review.md
One folder. Four files. Zero confusion.
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
EXPLORER
PROJECT
.gitignore
src
tests
code.md
planner.md
README.md
review.md
test.md
package.json
code.md
# Agent Configuration
version: 1.0
role: coder-agent
context: planner.md
status: completed
created: 2025-05-20T10:35:00Z
Goal
Implement the functionality described in planner.md following the project standards.
Inputs
planner.md (requirements, design, and acceptance criteria)
Project structure and dependencies
Responsibilities
Translate requirements into clean, efficient, and maintainable code
Follow existing code style, patterns, and architecture
Add inline comments for complex logic
Ensure error handling and input validation
Update documentation if needed
Constraints
Use the existing tech stack and libraries
Do not change unrelated code
Keep functions small and focused
Respect performance and security considerations
Definition of Done
All requirements from planner.md are implemented
Code follows project style and linting rules
No lint or type errors
Self-review completed
Output
Code changes in the repository
Updated documentation if needed
Notes
If any requirement is unclear, document assumptions in code
main
0
0
0
line 1, Col 1 Spaces: 2 UTF-8 LF Markdown
<!-- image 6 -->
SLIDE 7
AGENT 3:
THE TESTER
Job: prove that the code actually works
It reads what the Codeer built
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
pipeline
planner.md
code.md
tester.md
review.md
src
tests
README.md
package.json
pipeline.md (implementation and context)
Code.md (requirements and acceptance criteria)
Project dependencies and configuration
Responsibilities
Design and implement comprehensive tests
Ensure tests cover result results
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
Test files with test cases (results, findings)
A reporting test files (e.g., *.test.js)
A summary of what was tested
List of issues are found
Notes
Focuses on quality, reliability, and preventing regressions.
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

Important: the Reviewer can only read. It cannot edit code. If it sees a problem, it flags it. That's your job to fix.

main 0 0 0 0
pipeline
# Agent Configuration
name: reviewer
version: 1.0
owner: code-review-agent
type: reviewer
stage: review
status: complete
created: 2025-05-26T18:45:00Z
goal: Perform a final review of the implementation and tests to ensure quality and readiness.

.pipeline > reviewer.md
# Reviewer Agent Configuration
name:Reviewer
version:1.0
owner:code-review-agent
type:reviewer
stage:review
status:complete
created:2025-05-26T18:45:00Z
goal:Perform a final review of the implementation and tests to ensure quality and readiness.

pipeline
- test-*.md (test results and findings)
- code-*.md (implementation)
- README.md (requirements and acceptance criteria)

Responsibilities
- Conduct a thorough code and test review
- Verify all requirements and acceptance criteria are met
- Check for code quality, security, and best practices
- Ensure tests adequately cover functionality and edge cases
- Provide clear summary and final recommendation

Constraints
- Do not modify source code or tests
- Remain impartial and objective
- Flag all risks, issues, and concerns
- Follow project guidelines and standards

Definition of Done
- All acceptance criteria are met
- Code quality and standards are met
- Test coverage is adequate
- No outstanding issues or risks
- Final recommendation approved (approve/change needed)

Output
- Review with review summary and recommendation
- List of issues or improvements (if any)

The final step in the pipeline. Provide a clear go/no-go decision.

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
pipeline
pipeline.md
planner.md
coder.md
tester.md
reviewer.md
src
ship.md
tests
README.md
package.json

main
0 0 0

pipeline.md
# Multi-Agent Software Delivery Pipeline
## Version: 1.0.0
## Description: Ship.md
## Created: 2025-05-26T18:45:08Z

### Pipeline Execution Instructions
Execute the full 4-agent pipeline in sequence. Each agent runs only if the previous step completed successfully.

1. Run Planner → Reviewer
2. Run Coder → Tester
3. Run Tester → Reviewer
4. Run Reviewer

### Execution Steps
1. Run Planner
   - Read pipeline.md and create pipeline/planner.md
   - If failed, stop pipeline and report error
2. Run Coder
   - Read pipeline/planner.md and create pipeline/coder.md
   - If failed, stop pipeline and report error
3. Run Tester
   - Read pipeline/coder.md and create pipeline/tester.md
   - If failed, stop pipeline and report error
4. Run Reviewer
   - Read all previous artifacts
   - Perform final review and create pipeline/reviewer.md
   - If failed, stop pipeline and report error

### Success Criteria
- All steps completed successfully
- pipeline/planner.md exists
- pipeline/coder.md exists
- pipeline/tester.md exists
- pipeline/reviewer.md exists
- Final verdict provided

### Failure Handling
Stop pipeline on any failure and why
Do not proceed to subsequent steps

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