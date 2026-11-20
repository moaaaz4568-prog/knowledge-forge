---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_0.txt"
words: 1166
sha1: 255051990efa432905e1891d5de53a56cb87b4cc
lang: en
account: divyannshisharma
quality: ocr+carousel-11
---

# S_igocr_divyannshisharma_DaqH6G0kn5P

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_0.txt`
> الأجزاء: 11 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DaqH6G0kn5P_10.txt`

<!-- image 0 -->
Designing loops
with
Claude
Fable 5
build self-improving
systems that run on repeat
<!-- image 1 -->
Slide 2
Most people
use AI wrong.

They prompt it once.
They ask a question.

They get an answer.
The model responds.

They accept
whatever comes out.
No follow-up. No iteration.
Just move on.

good
enough.

That works fine for simple tasks.

80%

But for hard tasks —
the ones that actually matter —
that approach leaves 80% of the
model’s capability on the table.

Fable 5 is designed to work in loops,
not single shots.
Here’s what that
why it changes
everything.

unused
potential
<!-- image 2 -->
Slide 3
Technique 1
The self-correction loop

we don't do one and done here.

NORMAL APPROACH
you ask → model answers → done.

LOOP APPROACH
model runs a task → something grades the output against a rubric → model sees the feedback → model corrects itself → repeats until it gets it right

Think of it like a student taking a practice test, seeing the wrong answers marked, fixing them, and taking it again — except this happens automatically, in minutes.

Fable 5 is genuinely good at this. Earlier models were not.

Goal-driven loops: two implementations

| | Claude Code / goal | Claude Managed Agent Outcomes |
|---|---|---|
| Goal | Measurable end state | Rubric with gradable criteria |
| The judge | Independent grader model (Haiku) | Independent grader sub-agent |
| The loop | Not-met grade → revise | Iterate → clause in the condition |
| Bound | Turn / time iterations | max_iterations |
| Feedback | Grader model feedback | Grader sub-agent feedback |
| Exit | Auto-cesses / interrupt | Rubric pass on met or /goal clear |
<!-- image 3 -->
Slide 4
A real test:
the Parameter Golf challenge

Parameter Golf is a public ML challenge:
Train the best AI model you can in under 10 minutes,
using a file size smaller than 16MB.

let's run this
8 hours and
see what wins.

The agent has to:
Write training code → Launch it → Read
the results → Decide what to try next →
Repeat for up to 8 hours

Fable 5 was tested against an
earlier model (Opus 4.7) on this
exact challenge.

Parameter golf — Fable 5 vs Claude Opus 4.7
20 experiments - val_bpb, lower is better
● kept ○ discarded × crashed

Fable 5 (best 1.1604)
Claude Opus 4.7 (best 1.2178)

val_bpb (lower is better)
1.24
1.22
1.20
1.18
1.16
0.0 2.5 5.0 7.5 10.0 12.5 15.0 17.5 20.0
experiment # (0 = baseline)

QK_GAIN_INIT=5.0 (-0.0016)
0.048 train.eval (-0.0179)
TRAIN_SEQ_LEN=2
overlapped sliding-window eval (-0.0207)
Int64 QAT + Int64 expo (-0.0163)
fp16 pass-through tied embedding (-0.0063)
<!-- image 4 -->
Slide 5
What happened
Fable 5 improved the training pipeline roughly 6x more than Opus 4.7.
not here to play safe. we're here to win.
Here's why that gap happened:
Opus 4.7 found one small win early on — and then just kept tweaking small numbers around that same idea for the rest of the 8 hours.
Fable 5 took bigger bets. Changed the whole structure when it needed. Hit a setback (a regression), pushed through it anyway, and came out ahead.
One is playing it safe.
One is actually thinking.
<!-- image 5 -->
* One important detail:
who does the grading matters

► You might think: just let the model grade its own work.
This doesn’t work well. Models are bad at criticizing themselves — they tend to approve their own outputs even when they’re wrong.

★ The fix: use a separate grader.
A second model, running in a completely fresh context, grades the output independently.
This is called a verifier sub-agent and it consistently outperforms self-critique. Fable 5’s tooling handles this automatically.

MAIN AGENT:
DOES THE WORK

WORK
Completes the task and produces output.

OUTPUT
The result of the work.

① OUTPUT
Main agent sends output to grader.

GRADER AGENT:
CHECKS THE WORK INDEPENDENTLY

EVALUATE
Independently reviews the output against the standard.

GRADE & FEEDBACK
Provides a score and clear feedback.

② FEEDBACK
Grader sends feedback back to main agent.

IMPROVE & REPEAT
Main agent uses feedback to improve and try again.
<!-- image 6 -->
Technique 2:
memory
across
sessions

✦ The loop above
works within
one session.

❋ Memory lets the loop
work across many sessions
days, weeks, however long
the task runs.

✦ The idea:

1 Agent works
on a task
Attempts the task
and produces
an answer.

2 Gets something
wrong
Realizes the task
isn't correct.

3 Investigates
why it went wrong
Finds the root cause
of the mistake.

4 Verifies the
correct answer
Confirms the
correct answer.

5 Turns that into
a general rule
Forms the right
solution.
Writes a rule
that prevents the
same mistake.

6 Writes it to memory
Stores the rule for
future sessions.

7 Next session:
reads the rule
Uses the rule instead of
making the same
mistake again.

❋ It's like a junior analyst
and reads them before the
who actually keeps notes
the next meeting.

NOTES
MEMORY
RULE
<!-- image 7 -->
* How different models handled memory
A benchmark tested agents on sequential questions using a SQL database session. Each question was a separate session. Memory was available.
→ Sonnet 4.6:
Stored a list of guesses and failures.
Rarely looked at them again.
Basically didn't use memory at all.
→ Opus 4.7:
Built a better reference —
but only verified about 17% of what it stored.
Lots of uncertainty left in the notes.
→ Fable 5:
Verified up to 73% of what it stored.
Turned specific findings into general rules.
Actually consulted those rules in future sessions.
* Same tool. Completely different behavior.
<!-- image 8 -->
Slide 9 —
The shift
in mindset

Most people try to control
AI by writing better prompts.

That works up to a point.

But with Fable 5, the bigger
lever is designing the
environment the model
runs in:

Give it a rubric
to grade against

Let a separate
grader do the
checking

Give it memory that
persists across
sessions

Let it self-correct until
the rubric is satisfied

Stop steering. Start designing
the loop. The model does the rest.
<!-- image 9 -->
Slide 10 —
Where to start
If you want to try this yourself:
→ /goal in Claude Code —
lets you set an end condition
Claude works toward
→ Outcomes in Claude Managed Agents —
spawns a grader automatically for you
→ Memory in CMA —
gives your agent a shared
filesystem across
sessions
You don't need to understand the
technical details to use any of these.
Start with one task. Set a rubric.
Watch what happens.
<!-- image 10 -->
Slide 11 —
The model is only as good as the loop you put it in

Fable 5 is powerful in a way earlier models weren't.

But raw power with no structure gives you fast mediocrity.

A well-designed loop — with grading, feedback, and memory — gives you something that actually compounds over time.

Design the loop.
Let the model climb.

Save this if you work with AI agents 🚀
Follow for more on building real AI systems

grade
***
memory
feedback