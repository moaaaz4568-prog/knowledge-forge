---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CofW9qqtYBG.txt"
words: 536
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CofW9qqtYBG

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CofW9qqtYBG.txt` — حساب: airesearcherguy — إنستجرام — فيديو CofW9qqtYBG

---

I just figured out how to build an AI-powered engagement bot on Twitter. Let me show you. Okay, so we're here on make. Com. Now, engagement is so important on Twitter, and that's why this is a very powerful bot. So the first module gets a user, and when you use the get a user module, it actually pulls in the latest tweet from that user. So in this example, we'll use Gary V. Then we'll use OpenAI. Here's the prompt. You're a marketer active on Twitter. You see a tweet from one of your favorite marketers and wish to reply. Read the following tweet and reply in a conversational tone. Be sure to consider the implications of the tweet and add to the conversation in some profound way. Make the tweet reply robust yet concise. And then the text of their status, which is their latest tweet. And then the constraints are not to include context or pretext. Don't include the user's handle because that's already gonna be in the tweet, you'll see. And make sure it doesn't exceed 280 characters. And I'm attempting to get it to not include quotation marks because sometimes it does that for some reason. And then we have markdown to HTML. The reason is because there's gonna be extra spaces in that response we don't need. And then we have HTML to text, which is gonna take that space out. And then we have make an API call. It makes an API call to statuses update. However, in the query string, as long as you at the person and then put in the in reply to status ID with the tweet ID, it'll respond to that tweet. Now let's run it and see what happens. And look, Gary V's latest tweet as of this video is about VCON, to which my bot replied, I can't wait to see what you've got in store. Now here's a different approach. Here we search tweets, and then we can search by a phrase or a hashtag. I had to include a filter to make sure that it wasn't a retweet because for some reason the tweet replies function does not work on retweets. And then here is the OpenAI module. You're an active Twitter user. You see an interesting tweet you feel you can add to the conversation. Read the tweet, consider its implications, and reply in a conversational tone. Make your tweet reply add meaningfully to the conversation and make sure you follow the guidelines in the constraints. As usual, don't add context or pretext. Don't include the user's handle. Don't exceed 220 characters because this thing loves to go over the character count. It's ridiculous. And then don't return unnecessary punctuation. Here's that markdown and text parser again, and then we'll run it. And here's what we got. Virginia SBDC says our startup program, the Innovation Commercialization Assistance Program, is hiring a new program coordinator, to which my reply is, that's great news. Love to see ICAP Virginia continuing to help startups. What qualifications do applicants need? But yeah, that's how you use AI to create engagement automatically on Twitter. Also check out my free GPT guide. Link in bio.