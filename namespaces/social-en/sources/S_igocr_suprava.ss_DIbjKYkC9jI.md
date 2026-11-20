---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_0.txt"
words: 760
sha1: 5bea356c763531788ad05557ab32d95cb23a98fd
lang: en
account: suprava.ss
quality: ocr+carousel-13
---

# S_igocr_suprava.ss_DIbjKYkC9jI

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_0.txt`
> الأجزاء: 13 — `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_11.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/suprava.ss/DIbjKYkC9jI_12.txt`

<!-- image 0 -->
Build the ultimate
Lead-Gen AI Agent
that books sales calls!
Lead
search
Enriched
info
Qualify
leads
Ice
breakers
Auto Add
campaign
SWIPE
WAH TEA
WAH TEA
WAH TEA
WAH TEA
<!-- image 1 -->
Still manually finding leads and writing cold emails?

You are falling behind!

slow & not consistent
Manual Finding
doesn't scale

What if you could build a system that fixes this for you!

Finds & Enriches ideal leads

Writes personalized ice breakers

Auto adds to campaigns
<!-- image 2 -->
The Complete Tool Stack
Google
for prospect
discovery
Proxycurl
for company
info via URL
Dropcontact
for company
info via URL
OpenAI
for lead scoring &
ice breakers
G Sheet
to store &
organize leads
Smartlead
for email
campaigns
HeyReach
for linkedin
campaigns
n8n
for
automation
Let’s break it down module
by module, to understand
better.
<!-- image 3 -->
Search Leads with
Custom Google Search

Tell the system who you're
targeting—niche + geo and
automate scraping search results.

A. Paginate the entire google search

Add Page
module

Set to
"Run once for
all item"

Auto
search all
URLs

Auto
search all
URLs
<!-- image 4 -->
B. Add API & set parameters
Go to Custom google search engine
Paste API key
Set all search parameters
C. Loop & wait function
LOOP ---> Repeat the search (for all pages)
WAIT ---> To avoid API limit issues
(1 sec delay)
D. Filter results
Use FILTER function
To sort and organize data into columns
<!-- image 5 -->
Enrich With Info + Title
+ Location + URL

Enrich and get more details about
each lead. Turn raw domains into
usable contact info.

A. Proxycurl credentials

Create an API
Key from
Proxycurl

Set credential
in N8N: Header
Auth

*Add IF condition to
continue if data found

Name: Authorization

Value: Bearer
YOURAPLKEY
<!-- image 6 -->
B. Plug Dropcontact into workflow
Log into Dropcontact acc. & copy API contact
Paste in the Dropcontact node in workflow
Set "Enrich" operation & add parameters

C. Find out company details
Use Proxycurt to search
Search for Company URL instead
Get all data - company size, type, location
Add IF condition if not found to search from URL by itself!
<!-- image 7 -->
Qualify Leads Using
RAG Qualifier (& GPT 4)

Let AI decide which leads are
actually worth your time and
score it accordingly!

A. Add instruction to RAG Agent

Instruction

Query the vector database for ICP data (ask:
"What is my ideal target ICP? Please
summarize to compare with my prospect.")

Compare this prospect to the ICP (size,
industry, pain points, etc.).
Return a single JSON with:
{ "lead_potential": "High" | "Medium" | "Low",
"lead_grade": <decimal> } No extra keys,
text, or wrapping.
<!-- image 8 -->
B. Customize system message
according to needs to qualify data

Use system
message to tell
the AI exactly
what you want.

Expression
Anything inside {{ }} is JavaScript. Learn more

4 items
You are an AI Lead Qualification Agent for cold
outreach.
Your goal: Identify potential leads, not eliminate
them based on rigid ICP matching. The ICP is a
reference, not a strict rublekat.
Process
Your Company Information: pitching cold outreach skool
community which teaches client acquisition,
copywriting frameworks, modern multi-channel outreach,
cold email mastery, linkedin playbook, B2B guide,
reddit funnel, etc to GM and SMB BDR and sales

C. Add Open AI (GPT 4) model

OpenAI ---->

To qualify leads
according to the
instructions

the score data

*Add CODE module to format
<!-- image 9 -->
Generate Ice Breakers
with GPT -4

Get replies by making every email
feel human. Prompt GPT to
analyze data and create intros!

A. Add prompt to generate icebreakers

Add your
business USP
& prompt

Create an icebreaker starting with "I know you
are tired of automated emails... so to prove you
this email is not, I can tell you that I love ... (find
something very specific about the web design
of the website. Be the more specific you can
be it needs to be like a detail you found inside
the landing page that stand out from other
websites.) One sentence only as it's going to
be used as an icebreaker in the start of a cold
email. Delete all superfluous information.
Return as a single line.
<!-- image 10 -->
Auto-Add to Smartlead
or LinkedIn Campaigns

Skip manual work—push
leads straight into outreach.

1. HTTP call to auto add

Add campaign
ID & API key.
Set input
fields

If added, Set
Gsheet Input
as "YES"

And it's done! 🎉
<!-- image 11 -->
Here’s what we’ve automated—start to finish:
Entire Lead Gen Engine
Build the lead list
Qualify based on your ICP
Enrich each prospect
Add into campaign
you can focus on closing, not chasing!
<!-- image 12 -->
I post daily content on
lead generation
and how to get clients
follow for more :)