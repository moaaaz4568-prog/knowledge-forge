---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_0.txt"
words: 342
sha1: 21d8fe4c67de4ed2282a0a1cf340b160d5d3f9a1
lang: en
account: leadgenman
quality: ocr+carousel-10
---

# S_igocr_leadgenman_DZo_htdje6F

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_0.txt`
> الأجزاء: 10 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DZo_htdje6F_9.txt`

<!-- image 0 -->
Claude
Maildoso
+
Inboxes that land
<!-- image 1 -->
Step 1
Set up your sending infrastructure
Maildoso spins up cold email domains + inboxes
Go to maildoso.ai and sign up
Mailboxes
built for outbound
Diversify your sending strategy with reputable mailboxes built specifically for cold outreach, starting at just $0.49. Automate your SPF, DKIM, and DMARC setup, connect to your favorite tools in one click, and achieve 95%+ email deliverability.
Watch the product video
10M+
emails sent per day
4.7
G2 rating with 197 reviews
Get Started
400k+
mailboxes managed
<!-- image 2 -->
Step 2
Get your API key
Go to settings
Copy your Maildoso API key
Settings
Global Custom Domain Tracking
API token
You'll need this later
<!-- image 3 -->
Step 3
Open Claude Desktop
Go to "Customize"
Click "Add"
Claude
Connectors
Web
Desktop
Not connected
Browse connectors
Add custom connector
Tool perm
Choose v
Read
Go
<!-- image 4 -->
Step 4
Connect Maildoso
to Claude

Find the Maildoso MCP
Paste your API key
Save

Settings > Developer > Local MCP servers > Edit config. That opens
claude_desktop_config.json. Add this inside "mcpServers":

{
  "maildoso-api": {
    "command": "npx",
    "args": [
      "-y",
      "mcp-remote",
      "https://mcp.maildoso.com/mcp",
      "--header",
      "Authorization: ${AUTH_HEADER}"
    ],
    "env": {
      "AUTH_HEADER": "Bearer YOUR_PAT_TOKEN"
    }
  }
}

Save, fully restart Claude Desktop.
<!-- image 5 -->
Step 5
Tell Claude to
build your infra
Afternoon, Manthan
Currently unavailable.
Learn more
Claude Code is currently unavailable.
Using the Maildoso MCP, register 5 domains, create 3 inboxes on each, set up a forwarding inbox for replies, and run a placement check so I only send from healthy mailboxes.
Opus 4.8, Extra
My email accounts (24)
Search accounts or domains
Claude handles the rest
<!-- image 6 -->
What's
happening
here
m
Maildoso spins up the inboxes
Claude runs the checks
You send
from inboxes
that land
<!-- image 7 -->
Why this works?
Skip the DNS setup
Stop babysitting mailboxes
Stop guessing on inbox health
<!-- image 8 -->
Sending ≠ landing

Do this next

☑️ Check inbox placement
☑️ See if you hit primary or promotions
☑️ Watch mailbox health
☑️ Catch a burned inbox before it kills a campaign
☑️ Audit before you scale, run it through maildoso.ai
<!-- image 9 -->
LEAD GEN MAN
www.leadgenman.com