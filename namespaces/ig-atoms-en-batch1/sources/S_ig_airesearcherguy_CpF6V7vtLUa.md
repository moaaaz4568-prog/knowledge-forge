---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CpF6V7vtLUa.txt"
words: 509
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CpF6V7vtLUa

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CpF6V7vtLUa.txt` — حساب: airesearcherguy — إنستجرام — فيديو CpF6V7vtLUa

---

A lot of people have been asking, "Hey, can your blog bots do SEO?" So I decided to build an AI-powered SEO blog bot. Check it out. So over here in make dot com, we are utilizing the Google Ads campaign management API. So this is the URL. Your customer ID goes there. Do not include the dashes. It took me way too long to figure that one out. This is a post. There's actually a couple different ways you can do this. Keyword seed, there's also site seed, and then there's a combination of the two. I'll show you examples of both, but this is keyword seed, and it's got three seed keywords. The very next thing is very important. This is the filter, and this filters the keywords because you're gonna get a ton. So here I have it where the average monthly searches are above 10,000. So anything that's not above 10,000 won't make it through that filter. This rotates through them so that it can be aggregated, and this gives you a list of keywords. Then we have the first prompt. Using the SEO keyword list provided, create a blog article headline. And then of course, the remove quotation marks prompt. Then we have create an intro using that same list and the new title created. We have OpenAI generate an intro paragraph. Then we have the article body using the intro and the title. Important constraint here is to not repeat the points made in the intro paragraph. And then we have this module which formats the entire article into HTML. We have this create an excerpt which is gonna act as the meta description, and then this one creates a slug for the URL. And then we use the Yoast SEO plugin to publish to WordPress. Now let me show you what all that looks like. So here is the article that we ended up with using the keyword list. And what's cool is that it absolutely hit those keywords. It also formatted everything really well with subheads. And again, all the target keywords I think have been hit. There's still some work to be done. Unfortunately, for some reason, the Yoast plugin is not putting the excerpt in the meta description, so you'll have to do that manually. And I can't figure out how to get OpenAI to format tags properly so that the plugin will take it, so you need to add your tags manually as well. But the bulk of the work has been done. As I mentioned, you can also use a seed site, so I took a quote unquote competitor website and targeted social media management. And again, the article absolutely hits all of the list of keywords that it was given. This was before I added the remove quotes module, but this is based on a website instead of keywords, and it ended up being a bit longer probably because there was more data to pull from. And that's how you leverage AI to create SEO content.