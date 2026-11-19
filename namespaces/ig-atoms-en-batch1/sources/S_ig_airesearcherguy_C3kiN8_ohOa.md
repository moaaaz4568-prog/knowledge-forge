---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C3kiN8_ohOa.txt"
words: 395
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C3kiN8_ohOa

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C3kiN8_ohOa.txt` — حساب: airesearcherguy — إنستجرام — فيديو C3kiN8_ohOa

---

LinkedIn prospecting. I built the bots and they're dope. Let's go. So it turns out there are a ton of tools out there that let you LinkedIn search. The problem is they use your LinkedIn profile and all that search activity definitely raises some red flags. So I don't like to use those. Instead, here I have a variable value, which you could put whatever, co-founder, CEO, digital marketing, whatever it is that you're looking for, whatever your niche is. Then right here, these are all Google Custom Search Engine API calls, calling Google Custom Search. And this is the query, site linkedin. Com/in/ and then in title, it has your search query. So then it'll only pull up all of the URLs that have been crawled by Google that include the keyword that you entered in the variable. Each search yields 10 results, so this repeater repeats 10 times, and then all 10 leads get recorded in a Google sheet. And there's 100 leads with people on LinkedIn who have co-founder in their title. Next we have the LinkedIn influencer scraper. And this scenario uses the Rapid API LinkedIn data scraper API. And here it scrapes the LinkedIn URLs of whatever influencers you put in there, and then it takes their last 10 posts and pulls the last 10 comments on those posts. And then it records all of those commenters' profile information. And that's how you collect leads from people who engage with your competitors. Then I have this handy flow, the LinkedIn deduper. And basically all this does is it goes into those Google sheets and it removes duplicates from the rows because you're probably gonna have a lot of overlap and you don't wanna send connection requests to the same person multiple times. And last we have the automated connection requester. So you feed it from your Google sheets with the first two scenarios that populate a Google sheet with leads. Then you use that LinkedIn scraper API and you grab the last three posts that the person posted on LinkedIn. Then you have GPT write a connection request custom message. Then you call this awesome API from Unipile, which automates the sending of connection requests. Then you update your sheet to reflect that you've already sent a connection request to that lead. And there you go. Hope that helps. Cheers.