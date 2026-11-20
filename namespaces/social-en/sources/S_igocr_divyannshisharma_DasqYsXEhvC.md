---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_0.txt"
words: 1154
sha1: d3239e5b587ecd3c908c153b6e2a02dae4184b63
lang: en
account: divyannshisharma
quality: ocr+carousel-12
---

# S_igocr_divyannshisharma_DasqYsXEhvC

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_0.txt`
> الأجزاء: 12 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DasqYsXEhvC_11.txt`

<!-- image 0 -->
I built the AI
Customer Map
on Cursor
“Here’s how it works”
CUSTOMER
<!-- image 1 -->
Why I built
• Your next power users are hanging out in niche communities right now, asking for tool recommendations, sharing pain points, and looking for alternatives.
• Tracking these conversations manually across hundreds of independent servers is impossible.
REGION / CITY
e.g. North America, I
MIN INTENT
Any
MAX INTENT
Any
48 leads match
Export CSV
Enrich All
PIN = COMMUNITY WITH BUYING INTENT
Click on a pin to view. Enrich all with Apollo. Export for outreach.
INDIA
MALI
Timbuktu
DJENNE
BURKINA FASO
IVORY COAST
GHANA
TOGO
NIGERIA
BENIN
NIGER
CHAD
ABEOKUTA
CAMEROON
CENTRAL AFRICAN REPUBLIC
LAGOS
ENUGU
KANO
ZINDER
MADAGASCAR
+
-
<!-- image 2 -->
How it works

• The Aggregator: Direct scrapes from Slofile + API-driven discovery on Disboard.
• The Processor: Text is parsed, categorized, and fed into an Intent Analyzer.
• The Output: Clean data points synced directly to a centralized SQLite database and visualized on your dashboard.

Cursor Agent
Slofile
Disboard
Apify API
Apollo API
<!-- image 3 -->
The Intent Scoring Framework
• Every community gets a hard value score from 0 to 100 based on linguistic signals.
• Active Triggers: Higher weight assigned to phrases like "looking for a tool," "recommend an alternative," or "budget".
• Audience Context: Baseline signals boosted by commercial keywords like SaaS, founder, marketing, and SEO

Discord High Intent
SaaS Founders Hub
OVERVIEW MEMBERS
12,400 members # Business
A community for SaaS founders sharing growth tactics, pricing strategies, tool recommendations, and customer acquisition. Weekly AMAs with founders looking for...
INTENT SIGNALS
looking for +12 recommend +10 recommendation +10
pricing +9 saas +9 founder +9
INTENT SCORE
100
<!-- image 4 -->
The Problem: Gated Directories
• You can’t scrape private, closed directories easily without getting blocked.
• The Solution: Focus heavily on indexable, public highly active public communities.
• We built direct pipelines into the major public indexes for Slack and Discord.
Find Public Slack groups to join
Slofile lists public Slack groups. Discover Slack communities and channels to join. List your Slack workspace.
Find Slack by keyword
<!-- image 5 -->
How I built it

Step 1: Prompting the Discovery Map
• Go to your cursor agent workspace, initialize your criteria, and run the discovery sequence:
• "Build an AI platform that turns public Discord and Slack online communities into a live map of customer buying intent..."

AI intent mapping platform 📋 purpledizzy67/AI-Customer-Map
build an AI platform that turn public discord, slack online communities into a live map of customer buying intent, helping me discover and reach potential customers faster. You can find public discord groups from https://disboard.org/ and public slack group from https://slofile.com/ plus i also have apify api key let me know if you want that
Environment ready
Worked for 10m 57s
IntentMap is built and ready — a platform that maps public Discord and Slack communities by customer buying intent
PR: https://github.com/purpledizzy67/AI-Customer-Map/pull/1

What you get
Feature | Details
Slack discovery | Live scrapers, intent signals, filters by platform/tier
Discord discovery | Apify integration for Disboard (Cloudflare-protected)
Intent scoring | Keyword signals + optional OpenAI hybrid analysis (0–100, Hot/Warm/Cool/Cold)
Live intent map | D3 scatter plot — intent score x community reach
Outreach panel | Join links, intent signals, filters by platform/tier
<!-- image 6 -->
Bypassing the
Cloudflare Wall

Step 2: Connect Apify

• Directly crawling public Discord indices like
Disboard triggers strict Cloudflare protection.

• The Workaround: Inject your Apify API Key
to unlock the magicfingers/discord-server-scrap
actor.

• Uses distributed residential proxies to safely pull
fresh server metadata, growth rates, and
active profiles.

Discord Server Scraper
Pay per usage
magicfingers/discord-server-scraper
Scrapes publicly accessible Discord server information from disc
icons, and more.
Input
Information
Runs 12
Builds 1
Inte
★ 0.0 (0) 🔗 0 👥 4
<!-- image 7 -->
Connect Apollo API
Step 3: Connect Apollo API
• Finding a chat community is only half the battle; you need to map it to real businesses.
• Automatic Extraction: The app parses community profiles and metadata to isolate target company domains.
• Data Payload: Pings Apollo to instantly append firmographic data: company size, revenue tiers, and direct corporate LinkedIn links.
Workflows
Templates
Search templates
All templates
AI Recommended
Generate pipeline
Data enrichment
Integrations
Website Visitor
Multi-branch
Templates Competition Winners
Learn more
+ Outbound Copilot
Create workflow
All templates are end-to-end campaigns for a more efficient, scaleable, and accelerated GTM motion.
Website Visitor
Auto-enrich and save new website visitors
By Apollo.io
Preview template
Data Enrichment
Auto-enrich form submissions
By Apollo.io
Preview template
Website Visitor
Website Visitor - Add to list
Automatically add companies who visit your website to a list
By Apollo.io
Preview template
Website Visitor
Contact-level Website Visitor - Add to list
Add any identified website visitor to a list
By Apollo.io
Preview template
AI Recommended
Convert ideal customers with AI sequences
Email Reply Template
Create follow-up sequences when contacts reply to your emails.
By Apollo.io
Preview template
AI Recommended
Engage companies hiring in the US via AI sequences
Add companies with US job openings to a list, then use AI-crafted sequences to reach out.
By Apollo.io
Preview template
Pipeline Tracker
Engage companies hiring in the US via AI sequences
Add companies with US job openings to a list, then use AI-crafted sequences to reach out.
By Apollo.io
Preview template
<!-- image 8 -->
Once ready, here’s
what it looks like and does

1. Find communities where your clients already gather

Search communities...
All platforms
All Intent

SaaS Founders Hub
Discord • 12,400 members • Business
100

Growth Marketers Collective
Discord • 8,900 members • Marketing
78

Sales & RevOps Network
Discord • 6,700 members • Business
78

Indie Hackers & Builders
Discord • 22,100 members • Startup
75

Product Hunt Launches
Slack • 0 members • Startup
73

Salesforce HQ 🚀
Discord • 1,966 members • Startup
64

Product Builders
Discord • 15,600 members • Technology
61

Rehma Studio
Discord • 0 members • Web-development
61

Nofinderz Community
Slack • 2,234 members • Marketing
60
<!-- image 9 -->
Intent scoring tells you where to focus
2. Intent scoring tells you where to focus
Each community gets an intent score (0–100) based on
signals like:
• “looking for a tool”
• “recommend an alternative”
• “switching from…”
• SaaS/startup/marketing language
Discord
High Intent
Sales & RevOps Network
MEMBERS
OVERVIEW
6,700 members
# Business
INTENT SCORE
78
B2B sales professionals and revenue operations leaders
comparing CRM solutions, outreach tools, and pipeline
automation vendors. Active hiring and budget channels.
INTENT SIGNALS
looking for a tool
recommend an alternative
switching from…
SaaS / startup / marketing language
<!-- image 10 -->
Company-level
lead enrichment
3. Company-level lead enrichment
For each community, you can enrich the organization behind it
Slack Warm Lead
Salesforge HQ
OVERVIEW
MEMBERS
INTENT SIGNALS
saas +9
startup +8
founder +9
founders +9
marketer +8
marketing +7
APOLLO LEAD
Enrich
salesforge.ai
Go
ENRICHMENT
Enrich
Salesforge.ai 🔥
salesforge.ai
Employees
130
Industry
Information Technology & Services
sales engagement
generative ai
machine learning
cold email
email deliverability
Revenue
—
<!-- image 11 -->
Comment
AI Customer Map
below and I'll send you
the link to the project.