---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CsWDklHIP6C.txt"
words: 359
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CsWDklHIP6C

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CsWDklHIP6C.txt` — حساب: airesearcherguy — إنستجرام — فيديو CsWDklHIP6C

---

I just built a next level competitor analysis tool using AI. Check it out. So I did this with Amazon reviews because the company I work for, we're developing AI tools for Amazon sellers. But this could just as easily be Google reviews, Shopify reviews, anywhere where you have a reliable source of data. How this works is I have the API call that grabs Amazon products, and then each of these is an API call that grabs the reviews for a product. I do this for 10 of them, and then each review API call grabs 10 reviews. All of those get saved as variables, formatted as a JSON, and then sent to Anthropic Claude because they now have a 100,000 token model, so it can easily take 100 reviews. All right, so let me break this down real quick for y'all. The trigger is a Jot form. It's real simple. It's not elegant at all. This is just where I put my Amazon keyword. This is the API call to grab Amazon products, and then all of these are API calls to grab individual Amazon product reviews. The repeater repeats 10 times so that it can grab all 10 of the reviews that are pulled for every product. And then on this last track, it aggregates all of it, formats it into a JSON, sends it to Anthropic Claude. You see the prompt right here. Here is a list of competitor reviews for the keyword. Please analyze the reviews and provide an analysis. And then I even have GPT in here, but all it's doing is formatting the response from Claude, and then it goes to a Google Doc. Now let's check it out and see what it did with 100 reviews. So the keyword that I used was cotton baby sling, and after 100 reviews from the top 10 competitors, Claude gave me the common themes, the repeated keywords, the general sentiment over all of the reviews, potential improvements that could be made, the most positive trait, the most negative trait, and then an overall analysis. So that is AI powered next level competitor analysis. Cheers.