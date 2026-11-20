---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_0.txt"
words: 1090
sha1: 56dfd943ebeee47caa52b08a96a7f280b0e64db6
lang: en
account: divyannshisharma
quality: ocr+carousel-10
---

# S_igocr_divyannshisharma_DbgKdJQkpbA

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_0.txt`
> الأجزاء: 10 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DbgKdJQkpbA_9.txt`

<!-- image 0 -->
Claude Code + Playwright
Automates Literally Anything
<!-- image 1 -->
Why Playwright,
Not MCP

MCP servers burn tokens because
every tool loads its own
description.
Playwright CLI does the same job
for way less. That's the whole
unlock here.
<!-- image 2 -->
Setup is
a non-event.

File Edit Selection ...
playwright-homepage.png - Browser Automation Demo - Visual Studio Code
playwright-homepage.png
screenshots
playwright-homepage.png
package-lock.json
package.json

hey Claude Code! I want to use Playwright...
> cd C:/Users/matej/OneDrive/Desktop/Bro
> npx playwright@latest install
Out: Title page: Fast and reliable end-to-end
Screenshots saved to: C:\Users\matej\One

Everything is working. Here's what was set up:
* Playwright installed with Chromium,
Firefox, and WebKit browsers.
* Demo script at demo.js — launches
Chromium, visits playwright.dev, prints
the page title, and saves a full-page screenshot
* Screenshot saved to
screenshots/playwright-homepage.png
You're all set to start automating. You can modify
demo.js or create new scripts — just
ctrl + esc to focus or unfocus Claude
> Bypass permiss... settings/local...

Told it to figure out install + build a plan. It installed Playwright,
opened a real browser, hit a live site, saved a screenshot.
First try, no errors.
<!-- image 3 -->
Use Case 1:
build it AND
test it

File Edit Selection ...
EXPLORER
BROWSER AUTOMATION DEMO
> .claude
> node_modules
> screenshots
> playwright-homepage.png
CLAUDE.md
js demo.js
package-lock.json
package.json

need you to build me a ... Browser Automation Demo - Visual Studio Code
08:00:00

I need you to build me a form submission ...
I want you to build me a form submission website now. I want this to basically be one page per question. As soon as I open up the page, it should ask me for my first name, and then there should be a button that prompts me to next page, and then I have my last name, my phone number, my business, and maybe, let's say eight questions about me, kind of getting me onboarded into this what of you're able to build me here. I just want to do this to see and test the functionality of what you're able to build me here. I still want it to look nice, so use the frontend design skill, but help me build out this plan so that you know exactly how you can actually execute on this.

Baking...

queue another message...

Plan mode settings.local.json

Screen Reader Optimized 278.8KB

Asked for a 12-question onboarding form, one question per page.
Caveat: Claude doesn't get to just build it — it has to test what it built too.
<!-- image 4 -->
It catches
its own bugs.

File Edit Selection ...
I need you to build me a ... Browser Automation Demo - Visual Studio Code
I need you to build me a form submission ...

EXPLORER
BROWSER AUTOMATION DEMO
.claude
node_modules
onboarding
screenshots
CLAUDE.md
demo.js
package-lock.json
package.json
qa-test.js
serve.js
test-onboarding.js

Read: C:\Users\hatef\OneDrive\Desktop\Browser Automation Demo\screenshots\qa-02-validation-error.png
Read: C:\Users\hatef\OneDrive\Desktop\Browser Automation Demo\screenshots\qa-10-comment-size-page.png
Good — the UI looks polished. I can see two bugs from the test:
Bug 1: Enter on keyboard didn't advance to review — it stayed on the notes page (step indicator opacity was still
Bug 2: The enter keydown handler has a logic issue for textarea.
Bug 1: The review page never loaded — the test found 0 review items and the edit button was interrupted by a
stage page overlay. This is because the textarea page's Enter didn't advance, so clicking Continue also didn't
properly transition to review (the old page's active class wasn't being properly removed, causing z-index
overlap).
Read the relevant JS code and fix both issues.
Read: C:\Users\hatef\OneDrive\Desktop\Browser Automation Demo\onboarding\index.html (lines 351-430)
Read: C:\Users\hatef\OneDrive\Desktop\Browser Automation Demo\onboarding\index.html (lines 576-675)
Queue another message...
Bypass permissions settings.local.json
Screen Reader Optimized 278.82KB

Ran a headed browser test on its own form. Found two real bugs on its own —
Enter key not advancing, review page stuck behind a stale overlay.
Read its own code, fixed both. No human touched it.
<!-- image 5 -->
Finished,
working,
tested.

File Edit Selection ...
EXPLORER
BROWSER AUTOMATION DEMO
.claude
.node_modules
.onboarding
.screenshots
CLAUDE.md
demo.js
package-lock.json
package.json
qs-test.js
serve.js
test-onboarding.js

Welcome — Get Started
localhost:3000

What's your first name?
Required - question 1 of 12
John

Continue

Reran the whole flow start to finish. Zero glitches. Built, broken, fixed, and shipped — same session.
<!-- image 6 -->
Use Case 2:
real lead gen.

File Edit Selection ...
Claude's Plan - Browser Automation Demo - Visual Studio Code
You need to help me bu...
Claude's Plan
X Code
08 19
Ready for review
Select text to add comments on the plan

EXPLORER
...
BROWSER AUTOMATION DEMO
> .claude
> node_modules
> onboarding
> screenshots
CLAUDE.md
demo.js
package-lock.json
package.json
qa-test.js
serve.js
test-onboarding.js

Plan: Dentist Contact Info Scraper

Context
A playwright script that automates Google Search to find dentist offices in California, visits 5 result websites, extracts contact information (names, phone numbers, emails), and reports a summary.

Implementation: find-dentists.js
A single new file following the existing project patterns (CommonJS, async IIFE, non-headless Chromium, screenshots).

Script Flow
Launch browser — non-headless with realistic user agent, slowMo: 200
California, visit 5 sites, pull names/numbers/emails.
bot-task — it switched to DuckDuckGo on its own and kept going.

New ask: find dentists in California, visit 5 sites, pull names/numbers/emails.
Google blocked the bot mid-task — it switched to DuckDuckGo on its own and kept going.
<!-- image 7 -->
Real contact,
pulled live.

Vision Dental

Contact Us Vision Dental

Have Questions? Contact Us:

Contact Us:

Phone:
(310) 470-6121

Address:
10700 Santa Monica Blvd
Suite 100
Los Angeles, CA 90025

Hours:
Monday 8:00AM - 5:00PM
Tuesday 8:00AM - 5:00PM
Wednesday 7:00AM - 4:00PM
Thursday 8:00AM - 5:00PM
Friday 8:00AM - 5:00PM
Saturday 8:00AM - 12:00PM
Sunday Closed

Comments:

Told it not to stop until it had 5 real numbers from 5 sites.
It landed on an actual dental practice site and pulled the
phone number and address straight off the contact page.
<!-- image 8 -->
Use Case 3:
your logged-in
accounts.

Chat
Cowork
Code
Generic coding session
Preview

New session
Search
Scheduled
Dispatch
Customize

All projects
Scheduled
Skool wins engagement Daily
AI news roundup Daily
Notification responses Custom
Youtube comment replies Daily

Today
Generic coding session
Yesterday
Update Skool wins response prompts

Nate
Max plan

Bash cd /Users/nateh/OneDrive/Desktop/Scheduled Automations/ && python scripts/post_comment.py --url "https://www.skool.com/ai-automation-society-123456/post/123456789" --comment "This is an automated comment from my Skool automation!" --api-key "sk-..."

4m 59s • 4.9k tokens

Can it run Skool while you're logged in? Yes — reuse your session or hand off after a manual login. First runs were messy (double-likes, a crash). After feedback with zero input, and once even dropped a birthday comment nobody asked for.

Reply...
Ask permissions

C:\Users\...\Desktop\Scheduled Automations
<!-- image 9 -->
Comment
skills
below,
and I will drop
the full setup.