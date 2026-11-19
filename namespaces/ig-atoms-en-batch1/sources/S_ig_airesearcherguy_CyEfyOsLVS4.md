---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/CyEfyOsLVS4.txt"
words: 362
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_CyEfyOsLVS4

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/CyEfyOsLVS4.txt` — حساب: airesearcherguy — إنستجرام — فيديو CyEfyOsLVS4

---

Heygen avatars are the most realistic on the market today, and I truly think that one of the best use cases for them is personalized emails. I can't imagine anything increasing conversion rates as much as that would. So let me show you what I've been building. So first I have this set up in HubSpot because that's our CRM. Obviously you would use whatever you use, but this is set on a trigger that goes off whenever somebody books a meeting with one of our sales reps. Then I describe to GPT that it's a representative for our company and tell it to create a script that says thank you with the meeting details. Here's the API call where we call Heygen to create the video with the script that GPT just wrote, and then details about the contact are saved in the data store. All right, normally that would be a webhook. The trigger is as soon as the video is done, but I'm still doing testing, so for now I just fetched the URL. But the next step is to resize the video for mobile view, and then that data store module grabs the contact information that we stored earlier, and then it sends the email. All right, here's the email we got saying thanks for scheduling and then to check out the attachment. This is Anthony Lee, CTO of Signly. I just want to take a moment to personally thank you for booking a meeting with our sales team. We're passionate about providing impactful PPC management and innovative software tools for Amazon sellers. We are very much looking forward to our conversation on Tuesday, October 10th, 2023 at 9: 30 a. M. US Eastern. We appreciate your time and are excited about the potential to help propel your Amazon business forward. Thank you again. See you soon. And that was the video. All the watermarks are because I'm still using the testing API. I'd imagine that is probably going to get people to keep their appointments. It could also be a great sales aid. I really think this is a powerful use case. Anyway, hope that helps. Cheers.