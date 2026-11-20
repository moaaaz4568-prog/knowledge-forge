---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_0.txt"
words: 585
sha1: 48a00f9a94c7746f5fa3ad21a01c170c5a5485ef
lang: en
account: divyannshisharma
quality: ocr+carousel-9
---

# S_igocr_divyannshisharma_DKbwDVqzH4X

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_0.txt`
> الأجزاء: 9 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKbwDVqzH4X_8.txt`

<!-- image 0 -->
find competitors
of any company
with
Google
Sheets
= findcompetitors(A2)
A	B	C
1	companyname	domainname	Competitors
2	Lav	lav.com	= findcompetitors(A2)
3	Barry	barry.co	barry.co
4	Notion	notion.so	notion.so
5	Datamail	datamail.com	datamail.com
for free
<!-- image 1 -->
Add competitors directly to G sheet, with this you can:
Add personalization
Research competitors easily
Automate tasks that save time
<!-- image 2 -->
1
Set Up
Google Sheets
Navigate to Extensions > Apps Script to
create a new script project
Google
Sheets
Extensions
Apps Script
Find competitors using Google Sheets
File Edit View Insert Format Data Tools Extensions Help
Add-ons
Apps Script
AppSheet
Cargo
GPT for Sheets™ and Docs™
SerperAI - Search Engine Results and Ranks
Notion
Airtable
Slack
HubSpot
Salesforce
COMPANY NAME
Competitors
ClickUp, Coda, Sli.do, Asana
Gladson, Mouseflow, Cont
ClickUp, Wrike, monday.com
Zendeek Support Suite, Fre
Salesforce Marketing Cloud
GLENCE, noblet, Coastal Gurus
4
5
6
7
Company Name
Competitors
<!-- image 3 -->
2
Copy & Paste the Code
Paste the following Apps Script code (summarized version)

/**
 * Get the top competitors for a specific company.
 * @param {string} companyName - Name of the company
 * @return {string} Result
 */
function findCompetitors(companyName) {
  if (companyName === "") {return "Error - Input is empty";}
  const API_KEY = "YOUR_API_KEY";
  const SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID";
  const searchQuery = "Top 10 + " + companyName + " Alternatives & Competitors site:gsa.com/products";
  const searchUrl = "https://www.googleapis.com/customsearch/v1?key=" + API_KEY + "&cx=" + SEARCH_ENGINE_ID + "&q=" + encodeURIComponent(searchQuery);
  const response = UrlFetchApp.fetch(searchUrl, { method: 'get' });
  const data = JSON.parse(response.getContentText());
  if (data?.items?.length > 0) {
    const competitorsList = data.items[0]?.link ? [data.items[0]] : [];
    const competitors = competitorsList.length > 0 ? competitorsList.map(item => item.title + ": " + item.link) : [];
    return competitors.length > 0 ? competitors.join(', ') : "Not found";
  } else {
    return "Not found";
  }
}
<!-- image 4 -->
3
Get Your API Key
Go to the Google Custom Search API and get the API key.
Search engine ID
Before using the Custom Search JSON API you will first need to create and configure your Programmable Search Engine. If you have already created a Programmable Search Engine, you can start by visiting the Programmable Search Engine control panel. Follow the tutorial to learn more about different configuration options.
After you have created a Programmable Search Engine, visit the help center to learn how to locate your Search Engine ID.
API key
Custom Search JSON API requires the use of an API key. Get a Key
Programmable
engine
Get a key
Copy the key
and paste it
into your
script
<!-- image 5 -->
4
Save and
Run the Script
Review and approve any permissions and
run.
Connect to an external service
Make sure you trust name to domain Apps Script
You may be sharing sensitive info with this site or app. You
can always see or remove access in your Google Account.
Learn how Google helps you share data safely.
See name to domain Apps Script's Privacy Policy and
Terms of Service.
Cancel
Allow
<!-- image 6 -->
5
Use the
Gsheet Formula
Use the function like any standard Google
Sheets formula:
=findCompetitors("Company Name")
C2
fx
=findcompetitors(A1)
A
B
C
D
1
companyname
domainname
Competitors
2
Lav
lav.com
=findcompetitors(A1)
3
Barry
barry.co
4
Notion
notion.com
5
Datamail
datam.com
<!-- image 7 -->
And you are all ready to
do your lead research
and analyze the market!
Your lead gen automation hacks!
Comment
Drop a comment sharing your
lead gen automation hacks!
<!-- image 8 -->
follow! for more content
on Lead generation &
getting clients!

divyanshisharma
59 posts
36.1K followers
35 following
Follow
Message

Divyanshi Sharma
Daily tips on
Lead Gen
SaaS Marketing
Client Acquistion
https://www.skool.com/the-client-magnet-6963/about

......