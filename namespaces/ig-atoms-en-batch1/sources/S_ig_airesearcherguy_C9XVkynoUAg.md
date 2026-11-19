---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/airesearcherguy/C9XVkynoUAg.txt"
words: 608
account: airesearcherguy
lang: en
quality: transcript
---

# S_ig_airesearcherguy_C9XVkynoUAg

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/airesearcherguy/C9XVkynoUAg.txt` — حساب: airesearcherguy — إنستجرام — فيديو C9XVkynoUAg

---

This is how you supercharge your RAG databases. I built next-level data prep flows for upserting documents into a RAG database. These things are awesome. Let me show you what they can do. All right, so right off the bat, you want to go into your Google Drive and you want to create a folder. It will be empty except for a single sheet that you will create. I'll show you that in a second, but first create a folder in your Google Drive for the purpose of what we're about to do. Then inside of that folder, create a sheet and the only headings that you need in that sheet are the file ID column and upserted. That's it. And that'll all make sense in a moment. But first, don't be intimidated by all the rows. I'm still building this out, but this is so I can have multiple inputs because I want to be able to take a form and then in any form that I want to, be it a URL, maybe a file upload, a YouTube video, or even maybe a voice note, anything that I want to do that I would like to store in my RAG database, I'll be able to use this form and put whatever media I want into it, and then it'll turn it into what I need it to. But for now, I only have the one for URL on and working. So first things first, I have a form that triggers when I press submit, and one of the fields for it is a URL. So it takes a URL. This is a simple HTTP get request, and all it does is it takes the URL because what it's going to do is it's going to basically scrape that whole page. Like that's what it does. When you get request that web page, it'll take all the HTML from that page. Next we have an HTML to text text parser that take the data from that HTTP call and it'll take all of those tags, all that meta information out. Then I have a text parser replace module. This is to get rid of all of the URLs because every image will have a URL, every button will have a URL. I want that all out too. So this is the pattern that I'm matching. And then I replace it with an empty string. And there you go. And then what happens is I have all the words from a web page. So then I have to set some variables. This is for chunking because I want to chunk the data. It needs to be chunked when it gets upserted into a RAG database anyway, so this is how I do it. So the first variable is the actual text string, and then the next variable is chunk size, and that I set to 4, 000. That's how many characters I want the chunk to be. Right, so I set those, then I have the repeater. It runs however many times it needs to be run for it to split it up in 4, 000 or less character chunks. So this simple formula does that length. So it counts the number of characters in the text string and then divides that by the chunk size, and that's how many times this is going to repeat. And then I have the set variable, and what this does cuts the text string at 4, 000 characters, right? So this tells it how many times it needs to do that, and then this actually does the cut. This chops it.