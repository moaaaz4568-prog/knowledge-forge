---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_0.txt"
words: 470
sha1: 3fc5adf4d36038c66f451cab8371bdca4438bd49
lang: en
account: aiagently
quality: ocr+carousel-8
---

# S_igocr_aiagently_DbopjfSCGnm

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_0.txt`
> الأجزاء: 8 — `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DbopjfSCGnm_7.txt`

<!-- image 0 -->
How to Build
AI RECEPTIONIST
that book clients 24/7
GAME CHANGER
VOICE AI Agent
<!-- image 1 -->
STEP 1
Create Your
Retell AI Agent

Create a new
voice agent in Retell.

Give it:
Business information
Services
Prices
Opening hours
Location
Booking rules
Your receptionist prompt

“You are Sarah, the AI receptionist for AANUKO
Barbershop in Los Angeles.
Your job is to make every caller feel like they are
speaking with a real, experienced receptionist.
Speak naturally and conversationally.
Keep responses short, usually 3–12 words.
Never sound robotic or scripted. Use natural
phrases like “Sure,” “Absolutely,” “Got it,”
“One moment,” and occasional “yeah”
or “uh-huh” when they fit naturally.
Collect only what is necessary to book:
service, preferred barber, date/time,
customer name, and phone number.
Check the calendar before confirming
availability. Never claim a time is available
without checking.
Answer questions using only the provided
business information. Never invent details.
Use Los Angeles time for all appointments.
Your priority is simple: understand the customer,
help them quickly, and make booking effortless.

Website: aanuko.com/#main
Business: AANUKO Barbershop,
Los Angeles

Then connect your
phone number.
<!-- image 2 -->
STEP 2
Give Your
Agent a Tool
Connect with
Google Calendar
This is where it gets powerful.
Create a
Custom Function / Tool
in Retell:
</> check_availability
Your agent can now ask:
“Is Saturday at 2 available?”
Instead of guessing,
Retell sends the request
to your backend.
<!-- image 3 -->
If you want the
AI Receptionist
for Your Business like this
Fish Audio
Voice AI Agent
Shijia Liao
Co-Founder & Chief Scientist of Fish Audio
Credit: Fish Audio
Comment “build”
i will send you the link of 1.1 Call with me
<!-- image 4 -->
STEP 3
Connect
Retell → n8n
In n8n:
Webhook → POST
Copy the
webhook URL.
Then put that URL
inside your Retell
custom function.
Now the conversation becomes:
Caller
Retell AI
Custom
Function
n8n
Webhook
Your AI can now
trigger your automation.
<!-- image 5 -->
STEP 4
Send Booking Data
When someone says:
"I need a haircut Saturday around 2."
Retell sends n8n:
service: Haircut
date: Saturday
time: 2:00 PM
timezone: America/Los_Angeles
n8n now handles the actual booking logic.
Check Google Calendar
Connect Google Calendar to n8n.
Check:
Saturday → 2 PM
Then:
AVAILABLE?
YES → Continue
NO → Find another time
Never let the AI invent availability.
<!-- image 6 -->
STEP 5
Collect Customer Details
Once the slot is available:
“Great. What’s your name?”
Customer:
“Johnny.”
“Johnny?”
“J-H-O-N-N-Y.”
Save the exact spelling.
Then:
“And your email?”
“johnny@gmail.com.”
“That’s johnny@gmail.com, right?”
No guessing.
Save It To Google Sheets
After collecting the details, n8n adds a row:
Name	Email	Service	Date	Time
Johnny	johnny@gmail.com	Haircut	Saturday	2 PM
Now you have a simple customer database.
Every call → organized data.
<!-- image 7 -->
Here is the Full System
CUSTOMER
RETELL AI
CUSTOM FUNCTION
n8n WEBHOOK
CHECK GOOGLE CALENDAR
AVAILABLE?
YES
NO
BOOK
FIND SLOT
GOOGLE CALENDAR
GOOGLE SHEETS
RETURN RESULT
RETELL AI
CUSTOMER