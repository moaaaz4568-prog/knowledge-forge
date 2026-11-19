---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/DY2EH2ANaJm.txt"
words: 520
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_DY2EH2ANaJm

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/DY2EH2ANaJm.txt` — حساب: airesearcherguy — إنستجرام — فيديو DY2EH2ANaJm

---

All right, I still have plenty of friends in the Amazon space, so I see their conversations on social media a lot. Many complaining about big services such as Helium 10 charging more and more and offering less and less, and then they talk about where they're gonna go. And recently I saw that conversation play out, and at the end, all of the suggestions to transition to, they said that those were not really good options for keyword discovery. So I thought I could build a keyword discovery tool. I could build a skill that's not a SaaS. So that's what I did. Let me show you what I built. I built an agent skill, and it utilizes to get the Amazon data a rapid API called Parazon. They have a very generous free tier. If you do need to use thousands of API calls a month, they have a plan for like 20 bucks a month. So it's really inexpensive. And then it also utilizes a very inexpensive language model through Open Router. So every run is like less than half a penny. Anyway, all that aside, let's just show you what it does. So here, we're gonna pretend this is the product that I wanna look up. Now, the skill's already uploaded. As I explained in the last video I made, with these skills, all you have to do is open Claude Code in the folder that the skill is in and say read agent. Md and help me install this skill. And then Claude Code does it. So that skill is already in. Now all you have to do is say run keyword discovery for ASIN. So ASIN discovery already knows that that's a skill that it has to utilize, and it is, and that's making sure that it is allowed to run the Python scripts that are inside of that skill, making sure that all of the API keys are in there. That's part of the setup. All right, so I had to change the ASIN because the ASIN that I picked wasn't indexed inside of Parazon. Whatever happens. Anyway, and what I got back was this report here. It's giving me snippets inside of the window, but I can ask the agent any questions I have about these keywords. So the first thing it presents is the most relevant keywords that it found, and then it ranks the rest. It even offers a PPC campaign blueprint, backend keywords, suggested negative match campaign keywords. And again, I can converse back and forth with the agent about this information, or I can just ask it to export the keyword data as a spreadsheet. And on the first pass, I ended up with 125 highly relevant keywords, and I can go deeper in each of these clusters and get even more, as many as a thousand plus. So yeah, if that looks like it could be helpful for you, check out the Scrappy Apps Gumroad, aiplus3. Gumroad. Com, Amazon keyword discovery. There's a couple other ones there too if you want to take a look. Anyway, cheers.