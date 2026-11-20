---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_0.txt"
words: 365
sha1: c95c2f2caf88e8ee6139db33273f0b6e28286762
lang: en
account: divyannshisharma
quality: ocr+carousel-8
---

# S_igocr_divyannshisharma_DKjsmN4zQdE

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_0.txt`
> الأجزاء: 8 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DKjsmN4zQdE_7.txt`

<!-- image 0 -->
find your
client lookalikes
for free
Google
Sheets
companyname domainname traffic
Lay lay.com =gettraffic(B2)
Barry barry.co
Notion notion.com
<!-- image 1 -->
Save hours by automating traffic look-ups in Google Sheets!

Qualify leads with traffic data

Research competitor websites

Estimate potential opportunities
<!-- image 2 -->
Step 1 →
Open Google Apps
Script
Google
Sheets
Extensions
Apps Script
Name -> Domain (Clearbit API)
File Edit View Insert Format Data Tools Extensions Help
100%
A B
companyName domainName
lemlist lemlist.com
Alan alan.com
Praiz praiz.io
Lavender lavender.ai
datagamma datagamma.com
n8n n8n.io
Nolen nolen.so
AppSheet
Add-ons
Macros
Apps Script
Apps Script
SerpApi - Search Engine Results and Ranks
<!-- image 3 -->
Step 2 →
Copy & Paste the Code
Paste the following Apps Script code
(summarized version)
const similarWeb_api_key = "YOUR_API_KEY";

function getTraffic(domain) {
  var url = "https://api.similarweb.com/v1/similar-rank/" + domain + "/rank?api_key=" + similarWeb_api_key;
  var response = UrlFetchApp.fetch(url, {"muteHttpExceptions": true});
  var rank = JSON.parse(response.getContentText()).similar_rank.rank;
  return calculateTraffic(rank);
}

function calculateTraffic(rank) {
  if (rank > 3079440) return "Not Enough Traffic";
  const data = [[0, 86400000000], [20, 14000000000], [118, 200000000], ...];
  let lowerBound, upperBound, lowerTraffic, upperTraffic;
  for (let i = 0; i < data.length; i++) {
    let c = data[i][1];
    if (data[i][0] >= rank) {
      upperBound = data[i][0]; upperTraffic = data[i][1];
      lowerBound = data[i-1][0]; lowerTraffic = data[i-1][1];
      break;
    }
  }
  return lowerTraffic + (rank - lowerBound) * (upperTraffic - lowerTraffic) / (upperBound - lowerBound);
}
<!-- image 4 -->
Step 3 →
Go to SimilarWeb
Sign in/Sign up to SimilarWeb and then find your
API key
SimilarWeb
Sign in/
Sign up
similarweb
Effortlessly Analyze Your Competitive Landscape
Search for any website or app
Want to do a deeper analysis?
Start your free trial
yahoo.com
<!-- image 5 -->
Step 4 →
Get Your SimilarWeb
API Key
Find your API key & replace in the script with your
API key.
SimilarWeb
Generate
your API key
Add your API
API key
key in the
script
Generated Keys
Generate a New API Key
<!-- image 6 -->
Set up once, and let 🙂
Google Sheets handle the rest.
Comment
Share your research startegies
in comments below!!!
<!-- image 7 -->
follow! for more content
on Lead generation &
getting clients!

divyanshisharma
59 posts
36.1K followers
35 following

Divyanshi Sharma
I help you to
✨ Lead Gen
✨ SaaS Marketing
✨ Client Acquisition
SaaS Marketing | Client Acquisition
www.skool.com/the-client-magnet-6963/about

Follow
Message
...