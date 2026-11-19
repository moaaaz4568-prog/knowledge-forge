---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C3nMejPIkKN.txt"
words: 440
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C3nMejPIkKN

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C3nMejPIkKN.txt` — حساب: airesearcherguy — إنستجرام — فيديو C3nMejPIkKN

---

I built essentially an entire virtual blog writing team for my work. This thing is dope. Let me show you. All right, the first step is a jot form where we're able to either put in a URL or not. If we put in a URL, this is the URL to a article that's already been written and that gets scraped and then the information from that article is used as context. Or we just give it a query and then Perplexity AI searches the internet, answers the query and we use that as outside context. And that's context for our knowledge base bot, which is this API call. This calls Dante AI where we have our expert knowledge in tons of documents and we give the outside web context to it and we say, hey, give us some expert knowledge from the perspective of an expert on your knowledge base commenting on this outside context. The next step is we do Google keyword research on the focus keyword that's entered into the form. And then the last step is we make an API call to a series of writing agents. Basically one agent is the writer and it is prompted to come up with a title and then come up with an outline, come up with subheaders based on that outline, and then write each section based on the subheader using the keywords it's given and then using the expert knowledge and the web context as context. And then the second agent checks to make sure that the focus keyword is present, checks to make sure that it's readable and gives it a score. Each section is scored. If it scores too low, it has to be rewritten. If it scores high enough, then it passes and all that information is then sent to a webhook. Here we have the webhook that's triggered and then this is a series of DALL-E 3 calls that generate images for the blog that are then uploaded to WordPress until all the images are present. We also have GPT write an excerpt for Google and then all that information is put into WordPress and it is published as a draft article. Here's an example of what comes out. That's the main image and this is the written content that focuses in on a target keyword, that target keyword being content marketing for Amazon. Now I do have to come in here and do some edits like make these images smaller and bold highlight some subheaders, but overall this is well written and it has images and once I edit it, it will be.