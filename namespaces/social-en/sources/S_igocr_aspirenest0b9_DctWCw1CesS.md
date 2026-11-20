---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_0.txt"
words: 890
sha1: 4c7566613261460b50d72fc61067522b98ed7e88
lang: en
account: aspirenest0b9
quality: ocr+carousel-11
---

# S_igocr_aspirenest0b9_DctWCw1CesS

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_0.txt`
> الأجزاء: 11 — `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aspirenest0b9/DctWCw1CesS_10.txt`

<!-- image 0 -->
Punit Kumar
Build a WhatsApp AI
Agent in 30 Minutes
Using Claude Code + Meta WhatsApp API
It can answer customers, understand their needs,
recommend services, collect details and even book
appointments.
SWIPE →
01 / 11
<!-- image 1 -->
STEP 1
Punit Kumar
01 / 09
Start with Claude Code
Open Claude Code inside VS Code and create a fresh project folder.
Then use Plan Mode before asking it to build.
Instead of explaining the code you want, describe the business outcome.
PROMPT (ALTERNATIVE)
Hi Claude, I'm building an intelligent WhatsApp assistant for my business, a pet grooming and spa service called Pet-sy. The assistant should act as the first point of contact for our customers.
Here's what I need:
1. Greet customers warmly and introduce Pet-sy.
2. Answer FAQs about our services, pricing, and location.
3. Help customers book appointments (collect name, pet type, service, date, and time preference).
4. Understand if they are new or existing customers and personalize the response.
5. Use emojis appropriately to make the conversation friendly and engaging.
6. If unsure about something, politely ask for more details or offer to connect with our team.
7. Keep the tone professional, caring, and pet-friendly.
The goal is to provide a smooth and delightful experience while helping Pet-sy save time and manage appointments efficiently.
Type /model to pick the right tool for the job.
Paste
Claude can then create the architecture and suggest the technology stack.
<!-- image 2 -->
STEP 2
Punit Kumar
02 / 09
Give Claude the right instructions
Your first prompt should explain:
• What your business does
• Who the customers are
• What the agent should handle
• How it should behave
• What actions it should take
• What information it should collect
FOR EXAMPLE
Answer
↓
Understand
↓
Recommend
↓
Book
Don’t overcomplicate the first prompt.
Start with the outcome and let Claude figure out the implementation.
<!-- image 3 -->
Punit Kumar
STEP 3
03 / 09
Connect WhatsApp
Now create a Meta Developer App and select WhatsApp.
You'll need:
Phone Number ID
App Secret
Access Token
Verify Token
Webhook Callback URL
These credentials allow your AI agent to receive incoming WhatsApp messages and send responses back.
During development, you can use a Meta test number before connecting your actual business number.
Meta
Docs
Tools
Support
Apps
Required actions
Apps
Filter by
All Apps (1)
Archived
Required actions
Business portfolio
Clear
No business portfolio selected
Search by App Name or App ID
Create App
Recently used
App Name
App ID
Mode: In Development
Type: Business
Administrator
<!-- image 4 -->
STEP 4
Punit Kumar
04 / 09
Connect the AI model
Your WhatsApp messages now need an AI model to generate responses.
In this setup, use OpenRouter as the AI gateway.
Add your:
OPENROUTER_API_KEY
Then choose the model you want your agent to use.
This also makes it easier to switch models later without rebuilding the entire WhatsApp integration.
Settings
Account
Credits
Preset
API Keys
Provisioning Keys
Integrations (BYOK)
Training, Logging, & Privacy
Organization Members
Observability
API Keys
Manage your API keys to access all models from OpenRouter
Key
Usage
Limit
Create API Key
k-or-...
$0.0000
unlimited
TOTAL
k-or-...
$5.2888
unlimited
TOTAL
<!-- image 5 -->
STEP 5
Punit Kumar
05 / 09
Give the agent memory
Without memory, every WhatsApp message can feel like a completely new conversation.
Add conversation history to your workflow.
FOR EXAMPLE
Custome message
Last 15 messages
AI model
Context-aware response
Now the agent can remember what the customer was discussing and personalize its responses.
<!-- image 6 -->
STEP 6
Punit Kumar
06 / 09
Add your business knowledge
Create a separate system prompt file inside your project.
Put everything the agent needs to know inside it:
Business details
Services
Pricing
Opening hours
Location
Policies
FAQs
Brand personality
Booking rules
The advantage?
You can update the agent's behavior without rebuilding the entire application.
<!-- image 7 -->
STEP 7
Punit Kumar
07 / 09
Connect your
booking system
Now make the agent capable of taking action.
In the example, connect Cal.com.
Add the required API credentials and event
configuration.
The agent can then:
Check availability
Show slots
Collect details
Book appointment
You can replace Cal.com with another booking
system or connect the agent to your CRM or internal
tools.
<!-- image 8 -->
STEP 8
Punit Kumar
08 / 09
Test the agent like a real customer
Don't assume the first version will be perfect.
Start a real WhatsApp conversation.
Test things like:
"What's the price?"
"I want to book."
"Is tomorrow available?"
"Restart"
Then give Claude feedback based on what happens.
For example:
"Reduce the back and forth. Ask only 2-3 questions before recommending a service."
Claude can update the system and you test again.
<!-- image 9 -->
STEP 9
Punit Kumar
09 / 09
Deploy it 24/7
Your laptop shouldn't be the server.
Deploy the agent to a VPS so it can keep running even when your computer is turned off.
Your production setup becomes:
WhatsApp → Meta API → AI Agent →
Business Tools → VPS running 24/7
LLM + Memory
Once deployed, replace your temporary webhook URL with your production callback URL.
<!-- image 10 -->
Punit Kumar
Want the full tutorial?
I can share the complete step-by-step guide for building
this WhatsApp AI Agent with Claude Code.
INCLUDING
✓ Claude Code prompts
✓ API configuration
✓ System prompt
✓ Testing
✓ Meta WhatsApp setup
✓ Memory
✓ Cal.com integration
✓ VPS deployment
Comment “WHATSAPP” below
and I’ll share the tutorial + full guide.