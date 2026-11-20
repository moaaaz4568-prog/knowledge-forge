---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_0.txt"
words: 1451
sha1: de793ab38f747266aa230e00a9852c920c89fa70
lang: en
account: divyannshisharma
quality: ocr+carousel-19
---

# S_igocr_divyannshisharma_DDHP65IzbKb

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_0.txt`
> الأجزاء: 19 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_11.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_12.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_13.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_14.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_15.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_16.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_17.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DDHP65IzbKb_18.txt`

<!-- image 0 -->
15
AI prompts for
automating your
lead gen funnel
<!-- image 1 -->
Here's a playbook full of AI prompts to help you do these lead gen tasks for free, without spending $$$ on tools.
Automate leads enrichment
Personalise at scale
Find target audience
Find client's lookalikes
<!-- image 2 -->
prompt 1 →
Create Google Sheets formula
Prompt:
Create a Google Sheets formula to help me achieve the following:
[instructions]
Expected format:[format] ###
Only return the google sheet formula. No explanations
###
Create a Google Sheets formula to help me achieve the following:
Extract names from a long text.
Name_1, Name_2
Expected format:
### Only return the google sheet formula. No explanations ###
Output:
=JOIN(",", FILTER(A1, REGEXMATCH(A1, "[A-Z][a-z]+ [A-Z][a-z]+")))
<!-- image 3 -->
prompt 2 →
Summarize a Sales Call
Prompt:
This is a transcript from my last call: "[CALL_TRANSCRIPT]"
From the transcript, return a BANT analysis of the call in
this format:
- Quick background of client: client_background
- Client's budget discussion: client_budget
- Decision-makers identification: decisionmakers
- Detailed client need: client_need
- Addressing barriers and concerns: barriers_and_concerns
- Timeline expectations: timeline_expectations
- Next steps and follow-up actions: next_steps_and_actions
<!-- image 4 -->
prompt 3 →
Classify Emails

Prompt:
The following is an email and a list of the categories it can fall into:
Categories=["interested", "Out of office", "unsubscribe", "other"]

Interested is when the reply is positive.
Email content:"{{email_content}}"
Category:

The following is an email and a list of the categories it can fall into:
Categories=["interested", "Out of office", "unsubscribe", "other"]

Interested is when the reply is positive.
Email content:"Hello Lucas, I want to know more about Terminus!"
Category:

Given the email content, the category for the email is:
Category: "Interested"
<!-- image 5 -->
prompt 4 →
Classify job title by function
Prompt:
You can only reply by ONE of this value from this array:
["Sales","Founder","Growth/Marketing/Ops","Recruiter","Other"]
Never reply with several. Only ONE.
Usually, job titles containing either "business", "sales", "sdr", "bdr", "account executive", "commercial" will be classified to "Sales"
Examples:
Input:Sales Operations Manager
Output:Operations
Input:Sales Development Representative
Output:Sales
Input:{job_title}
Output:
<!-- image 6 -->
prompt 5 →
Company Enrichment - Master prompt

Prompt:
This is the content of the company website: ["website_content"]

In a JSON format:
- Give me the value proposition of the company. In less than 25 words. In English. Casual Tone. Format is: "[Company Name] helps [target audience] [achieve desired outcome] with [additional benefit]"
- Give me the industry of the company. (Classify using this industry list: [Agriculture, Arts, Construction, Consumer Goods, Education, Entertainment, Finance, Other, Health Care, Legal, Manufacturing, Media & Communications, Public Administration, Advertisements, Real Estate, Recreation & Travel, Retail, Software, Transportation & Logistics, Wellness & Fitness] If it's ambiguous between Software and Consumer Goods, prefer Consumer Goods) - Guess the target audience of each company.(Classify and choose 1 from this list: [sales teams, marketing teams, HR teams, customer Service teams, consumers, finance teams, accounting teams, IT teams, developer teams...]) Write it in lowercase
- Tell me if they are B2B or B2C

Format should be: {"value_proposition": value_proposition, "industry": industry, "target_audience": target_audience, "market": market}

JSON:
<!-- image 7 -->
prompt 6 →
Find market of the
company (B2B / B2C)
Prompt:
Website content: "[website_content]"
Based on the website content provided, determine if the
company is primarily B2B or B2C.
A B2B company sells products or services to other
businesses, while a B2C company sells directly to individual
consumers.
The response should be either 'B2B' or 'B2C' without any
additional comment
Output:
<!-- image 8 -->
prompt 7 →
Write icebreaker from LinkedIn post

Prompt:
Use the input to complete my sentence in under 8 words.
Keep the output short and use specific keywords from the post.
These are social media posts by other people, and I would just like to know the main idea of each post.
The input is this: {{LinkedIn Post}}. Complete the output with my prefix.
This is my prefix: "I just wanted to reach out because I saw your post about"

What will be your score? Complete the output with my prefix.
This is my prefix: "I just wanted to reach out because I saw your post about"

I just wanted to reach out because I saw your post about avoiding the spam folder through deliverability audits.
<!-- image 9 -->
prompt 8 →
Check and fix your
grammar
Prompt:
Only fix grammar: "[email_content]"
Only fix grammar:
"Hey,
I'd like to show you a sales prospecting workflow that might
increase your outreach results by 20%.
Are you interested to know more about it?"
"Hey,
I'd like to show you a sales prospecting workflow that might increase your outreach results by 20%.
Are you interested in knowing more about it?"
"Hey,
Are you interested to know more about it?"
<!-- image 10 -->
prompt 9 →
Draft a Linkedin
Connection Request

Prompt:
You are an experienced career coach.
Based on the following linkedin profile, could you please
generate a summary of this person’s career
accomplishments, and highlight their top three achievements.
Please provide as much detail as possible, including relevant
skills, experiences, and positions held that showcase their
expertise in the field.
Here’s their profile

I’m seeking a job and would like to connect with this person over LinkedIn.
Based on their top three accomplishments, give me three actionable
ideas on how I can get them to accept a connection request from me.
Explain using detailed examples. Let’s think step-by-step.

Certainly! Connecting with influential professionals on LinkedIn requires a strategic approach. Here’s
a step-by-step guide based on Adam Broda’s top three accomplishments:
1. Engage with Broda Coaching Content:
<!-- image 11 -->
prompt 10 →
Clean company
name variables

Prompt:
I will provide a company name that requires editing.
Please simplify the name by removing any superfluous details to ensure it's clear, easy to read, and can be naturally used in written communication by a salesperson.

People often include:
- Extraneous information in the company name
- The company's legal entity designation
- The country of the company

For example, if the provided company name is:
"Name of the company | Agency web"
It should be edited to:
"Name of the company"

Your task is to retain only the essential company name.
Please clean the following company name:

Output:
<!-- image 12 -->
prompt 11 →
Extract Value Proposition
Prompt:
This is company website content: "[website_content]"
Give me the value proposition of the company. In less than 25 words. In English. Casual Tone.
Format is: "[Company Name] helps [target audience] [achieve desired outcome] and [additional benefit]"
Value Proposition:
This is company website content: *
Pricing
Contact Sales
Login
Try for free
AI-Powered by 437 Million Successful Email campaigns
Turn Strangers into Customers
Find buyers, engage across multiple channels and convert them into your next customers.
<!-- image 13 -->
prompt 12 →
Find Target Audience
Prompt:
This is the company website content([website_content])
Guess the target audience of the company.
Classify and choose 1 from this list:
[sales teams, marketing teams, HR teams, customer Service teams, consumers, finance teams, accounting teams, IT teams, developer teams...]
Guess the target audience of the company.
Classify and choose 1 from this list:
[sales teams, marketing teams, HR teams, customer Service teams, consumers, finance teams, accounting teams, IT teams, developer teams...]
Write it in lowercase.
Output:
sales teams
<!-- image 14 -->
prompt 13 →
Find Competitors
Prompt:
Visit [company name] website.
Understand its core activity.
Then use Google Search to find 10 companies doing the same activity.
Return the result in a table. Columns are:
- company name
- website URL
- Description
Do not comment. Only return the table.
<!-- image 15 -->
prompt 14 →
Research ICP
Prompt:
I'm prospecting a [ICP].

I'm looking to sell them a [tool/service] that:
- [value prop 1]
- [value prop 2]
- [value prop 3]
- [value prop 4]
- [value prop 5]

List their top 3 KPIs.

Give me the most likely top 3 problems they're facing in hitting these KPIs.

Also give me their top 3 most likely lagging, leading and leading indicators.

Give 3 suggestions of how my product can solve their top problem.
Keep it concise.
<!-- image 16 -->
prompt 15 →
Extract relevant lines
from job posting

Prompt:
Here is the content of a job offer:"[job_offer_content]"

Extract the most relevant sentence from the text that discusses
the company's prospecting challenges that my company can solve
with their [product/service].
My company information:
- Product:
- Value Prop 1:
- Value Prop 2:
- Value Prop 3:

Prioritize extracting a sentence from the bullet points in the
employee's job description.

Do not provide explanations.
Extract a sentence that is less than 300 words.
If you don't find any relevant sentence, return null.
Do not translate.
Sentence:
<!-- image 17 -->
Drop a comment below on
what hacks you use in your
marketing strategies!

What hacks do you use in
your marketing
strategies?

Add a comment below...
<!-- image 18 -->
follow!
for more content
on Lead generation &
getting clients!
divyanshisharma
Follow
Message
36.1K followers
35 following
59 posts
Divyanshi Sharma
Daily tips on
Lead Gen
✨ SaaS Marketing
✨ Client Acquisition
www.skool.com/the-client-magnet-6963/about