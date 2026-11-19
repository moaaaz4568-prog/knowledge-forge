---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/Csqi_osoRhn.txt"
words: 524
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_Csqi_osoRhn

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/Csqi_osoRhn.txt` — حساب: airesearcherguy — إنستجرام — فيديو Csqi_osoRhn

---

So we're finally testing probably my favorite thing that I've built, which is the cold email bot. This thing's amazing. Let me show you how we're using it. All right, so here in make. Com, we actually don't scrape for our leads because we already have a huge list of cold emails. So those are in this Google sheet, and on a timed basis, it pulls in X amount of emails. In this particular scenario, we're not using ChatGPT. Now I want to point out GPT-4 is hands down the best sales writer. However, it's really slow. If you want to send 100 emails out, you just can't because it takes anywhere from two to three minutes for an email completion. And the way Make works is they have a cap. No scenario can take more than 40 minutes to run. After 40 minutes, it just shuts it off. So you can't send more than a few emails a day. I think the max we've been able to pull off with GPT-4 is like 480. So we're testing Claude and we're gonna test GPT-3. 5. Claude is almost as good a writer, but not quite. But we can send over 2, 000 emails a day. So how this works is we have it cycle through the emails here. Then we have the email subject line prompt turned into a JSON, and then we call the AI to create the email subject line, format the answer, turn the email prompt into a JSON, call the AI to create the email body, format the answer, and then send it through Gmass. And then this last one, we annotate on the sheet that an email's already been sent to that email address, so it doesn't get sent twice. And with this particular scenario, we're able to send over 2, 000 individually crafted emails per day. So now you're probably wondering, why write individual emails for cold leads? The answer to that question is personalization. If you have anything more than just a name and an email address, like for instance, if you have business information, you can personalize the emails, and that personalization will increase conversion rates. This has been scientifically proven. Personalization will increase conversion rates. So let's go ahead and use some imaginary numbers real quick. Across the board, average open rates for cold emails is about 43%. But let's say you're in a really tough industry and you're only getting 20% opens. Now let's say that you only get a 2% click-through rate. That means for every 1, 000 emails, 200 people open and only four click through to see your offer. All 200 of those people saw a copy-paste template that everybody else saw. Now if you personalize the email custom to every person, let's say that only increases your conversion rates by 10%. In this instance, conversion equals click-through. That additional 10% means that instead of only four people seeing your offer, 24 people do, because now you're getting 12% click-through rate. That would effectively 6x your cold email efforts. That's the reason why I think this bot is so amazing. Cheers.