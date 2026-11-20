---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_0.txt"
words: 676
sha1: 9fac1b6ef3564afd8efbbecb57b120b84402d9da
lang: en
account: aiagently
quality: ocr+carousel-10
---

# S_igocr_aiagently_DZ4zia8iO-U

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_0.txt`
> الأجزاء: 10 — `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DZ4zia8iO-U_9.txt`

<!-- image 0 -->
Fire Power
How to get
unlimited leads
with Claude
<!-- image 1 -->
What this claude system does:

• Finds leads on Linkedin
• Sends connection requests & InMails
• Classifies cold email replies
• Runs autonomously
<!-- image 2 -->
What You Need
• Claude Code
• Google Sheets (free)
• Slack (free)
• Modal (free)
• n8n (free)
• Instantly or Smartlead (if running cold email)
• You own the system outright. Nothing recurring

Automation Stack
Google Sheets
(Free)
✓ Lead lists
✓ Campaign tracking
✓ Data storage
Memory

Instantly/Smartlead
(For cold email)
✓ Sending infra
✓ Sequences
✓ Deliverability
Voice

Slack (Free)
(Free)
✓ Alerts
✓ Logs
✓ Team updates
Feedback Loop

Claude Code
AI code for automations
✓ Prompting
✓ Code generation
✓ Workflow decisions
Claude Code

n8n (Free)
(Free)
✓ Connect APIs
✓ Automate flows
Nervous System

Modal (Free)
(Free)
✓ Run scripts
✓ Process heavy tasks
✓ Handle async jobs
Muscles
<!-- image 3 -->
The Problem
Tools charge $80–$500/month
You still configure it yourself.
One mistake = account suspended or banned.
This system has zero flags for LinkedIn to detect.
LinkedIn
Access to your account has been restricted
Access to your account has been restricted because we detected fraudulent activity associated with your account. To learn more about account restrictions, visit our Help Center.
If you are in the European Union, additional information on about your potential redress rights can be found here.
<!-- image 4 -->
Step 1:
Google credentials → Google Cloud Console →
create new project

→ Library → enable Google Sheets
+ Drive API

Credentials → OAuth Client ID → Desktop App

Download JSON rename to credentials.json

Drop into your project folder

Do this before anything else.

Google Cloud Platform
New Project
You have 11 projects remaining in your quota. Request an increase or
delete projects. Learn more
MANAGE QUOTAS
Project name *
My Project
Project ID: imbould-dalla-346418. It cannot be changed later. EDIT
Location *
No organization
Parent organization or folder
BROWSE
CREATE CANCEL
<!-- image 5 -->
Step 2:
Build the spreadsheet
Open Claude Code → paste the spreadsheet prompt
Claude builds 4 tabs:
• Sample Leads
• Blacklist
• InMail Queue
• Connection Queue
• Replace sample leads with your real list.
CLAUDE
CODE
> Unlimited Leads with Claude
<!-- image 6 -->
Step 3:
Add message templates

Claude writes 3 connection messages:
• Warm lead: who replied to your cold email (pulls email context from the row)
• Generic: "Noticed your company in the space, would love to connect"
• Fallback: "Connecting with industry professionals to share insights"

Tweak to match your offer before running..

3. Fallback (95 chars):
Hi Seth, connecting with [industry] professionals to share insights. Would be great to connect.

INMAIL MESSAGES

1. Warm Level (50):
Subject: Quick question about [VaynerMedia]
Hi [Name],
I work with companies like [VaynerMedia] in the [industry] space to help them [key value prop - e.g., close more deals, reduce overhead, increase ROI].
Most [Job Title] I talk to are focused on [efficiency and growth - curious if that's on your radar too.
Would a 15-minute call this week make sense? Happy to share what's working for similar companies.
Best,
[Your Name]

2. GM/Director level (VP Marketing):
<!-- image 7 -->
Step 4:
Install the browser agent

Run in terminal:

npm install @vercel/agent-browser

Reads pages using accessibility tree not CSS selectors.

Less tokens. Less bugs. More stable than Playwright.

Then Claude builds all browser actions on top of it.

npm-test npm install sass
added 16 packages, and audited 17 packages in 1s
1 package is looking for funding
  run `npm fund` for details
found 0 vulnerabilities
npm-test
<!-- image 8 -->
Step 5:
Build the n8n workflow

Warm or hot reply comes in:

• Find lead in Sample Leads sheet by em
• Do they have a Linkedin URL? Validate i contains /in/
• Already in Connection Queue? → updad priority to 1
• Not in queue? → use LinkUp to find Link append as Priority 1
• Already sent? → ignore
Next time script runs they go first.

n8n AUTOMATION
AI Agent
Tools Agent
<!-- image 9 -->
If you want this
System for your
Business
n8n AUTOMATION
AI Agent
Tools Agent
Gmail Trigger
Gmail Trigger
Comment "Apply"