---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_0.txt"
words: 904
sha1: 2685516d2d792a9843fdcefde6d4e23688e50873
lang: en
account: aiagently
quality: ocr+carousel-10
---

# S_igocr_aiagently_DblXlD1iPnS

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_0.txt`
> الأجزاء: 10 — `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DblXlD1iPnS_9.txt`

<!-- image 0 -->
How to Build
WHATSAPP
AI AGENT (FREE)
WhatsApp Trigger
Agent
Send message
Simple Memory
OpenAI Chat Model
<!-- image 1 -->
AI AGENTLY
Step 1: Create Your
Meta Business Account
Go to Meta
Business Suite /
Business Manager.
Create your
business portfolio.
Add:
→ Business name
→ Business email
→ Website
→ Business information
Don’t create random
API accounts from
third-party websites.
Start with Meta.
You need this
because your WhatsApp
Business Platform
assets are managed
through Meta.
All in one
with Partner
<!-- image 2 -->
AI AGENTLY
Step 2: Create a
Meta Developer App
Go to Meta for
Developers.
Create a
new app.
Then add:
WhatsApp
as a product.
This is where your
WhatsApp API
connection
starts.
Your setup will look like:
Business Portfolio
Meta App
Developer App
WhatsApp Product
WhatsApp Business Account
Phone Number
All in one
With Partner
Your
Growth
<!-- image 3 -->
AI AGENTLY
Step 3: Connect Your WhatsApp Number
Inside your Meta app:
Open the WhatsApp configuration.
Connect your: WhatsApp Business Account.
Then add the phone number you want your automation to use.
Depending on the setup you're using, Meta may require verification and other eligibility checks.
Once connected, you'll have the information required to communicate with WhatsApp through the API.
Your ally in one Partner
Growth
<!-- image 4 -->
AI AGENTLY
Step 4: Get Your API Credentials

Key
You will typically work with credentials and IDs such as:

Access Token
Your permission to make API requests.

Phone Number ID
Identifies the WhatsApp number you're sending messages from.

WhatsApp Business Account ID
Identifies the WhatsApp business account.

Webhook
The URL where Meta sends incoming events/messages.

Think about it like this:
Token = Permission
Phone Number ID = Your WhatsApp number
Business Account ID = Your business
Webhook = Where WhatsApp sends incoming messages

Keep all credentials private.

Your all in one
Growth Partner
<!-- image 5 -->
AI AGENTLY
Step 5: Connect
n8n MCP With Claude
Open Claude.
Connect your
MCP server
using the current MCP
connection method
supported by your
Claude environment
and n8n setup.
1
1st go to n8n
copy mcp
n8n MCP Server
MCP URL
https://your-n8n-domain.com/mcp
Connect
2
then add in
claude mcp tab
Claude Settings
General
MCP
Tools
Advanced
MCP Server URL
https://your-n8n-domain.com/mcp
Status: Connected
Once connected,
Claude can work with
your n8n automation
environment through MCP.
The idea is:
You tell Claude what you
want.
Claude can then work with
the available n8n tools
instead of you manually
creating every piece
from scratch.
Your all in one
Growth Partner
<!-- image 6 -->
AI AGENTLY
Step 6:
Build Whatsapp AI AGent

Give Claude This Prompt
Now paste this into Claude:

I want you to build a WhatsApp AI auto-reply workflow in my n8n environment.
GOAL:
When a customer sends a WhatsApp message, the workflow should:
1. Receive the incoming WhatsApp message.
2. Extract the customer's phone number.
3. Extract the customer's message.
4. Send the customer's message to Claude.
5. Give Claude my business information.
6. Generate a short, natural WhatsApp reply.
7. Send Claude's reply back to the same WhatsApp customer through the Meta WhatsApp Cloud API.

TECH STACK:
- n8n
- WhatsApp Business Platform / Meta Cloud API
- Claude
- n8n MCP

BUSINESS:
• Business name: [YOUR BUSINESS NAME]
• What we do: [DESCRIBE YOUR BUSINESS]
• Products/services: [ADD PRODUCTS OR SERVICES]
• Pricing: [ADD PRICING]
• Business hours: [ADD HOURS]
• Website: [ADD WEBSITE]
• Important policies: [ADD POLICIES]

CLAUDE RULES:
• Answer using only the business information provided.
• Never invent prices, products, policies, availability, or facts.
• Keep WhatsApp replies short and natural.
• Use simple American English.
• Don't sound robotic.
• Don't mention that you are an AI unless the customer asks.
• If the answer isn't available, say you don't know.
• Never claim an action happened unless the workflow actually completed it.
• If the customer asks for a human, tell them a team member can help.

IMPORTANT:
• Before making changes, inspect my available n8n tools and existing workflows.
• Build the workflow using the tools available through my n8n MCP connection.
• Use credentials securely.
• Do not expose API keys or access tokens in workflow text.

After building it, explain:
1. What you created.
2. Which credentials I need to paste my WhatsApp credentials.
3. Where I need to paste the workflow.
4. How I need to connect.
5. If I test the workflow, any missing configuration.
<!-- image 7 -->
AI AGENTLY
Step 7:
Add Your
WhatsApp Credentials
Claude still needs
the actual WhatsApp
API credentials.
In n8n, configure
them securely.
You may need:
WhatsApp Access Token
Phone Number ID
WhatsApp Business Account ID
Do NOT put these
inside your
Claude prompt.
Do NOT publish
them in your
codebase.
Do NOT paste them
into a public
GitHub repository.
Use n8n
credentials/environment
secrets where
appropriate.
<!-- image 8 -->
AI AGENTLY
Step 8:
Test the Workflow

For example:
Hey, what services do you offer?

WhatsApp
Your business number.

Meta
WhatsApp

The workflow should run:
WhatsApp → Meta → n8n → Claude → Reply → WhatsApp

Customer receives something like:
We help businesses automate repetitive tasks and lead generation. What would you like to automate?
10:30 AM ✓

That's your first working AI reply.

And your WhatsApp AI agent ready!

Your all in one
Growth Partner
<!-- image 9 -->
Book 1.1
Free Strategy Call
STOP GUESSING.
START GROWING.
YOU JUST GET RELAX
GROW YOUR BUSINESS
MORE LEADS
COMING DAILY
SAVE TIME
CUT COSTS
AI DOES
THE HEAVY LIFTING
MAX RESULTS
SCALE
WITHOUT LIMITS
Client
60:05
mute
keypad
audio
add call
FaceTime
contacts
Comment "1.1"