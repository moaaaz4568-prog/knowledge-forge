---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/algorithmswithpeter/DPY4r6yDcuC.txt"
words: 399
account: algorithmswithpeter
lang: en
quality: transcript
---

# S_ig_algorithmswithpeter_DPY4r6yDcuC

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/algorithmswithpeter/DPY4r6yDcuC.txt` — حساب: algorithmswithpeter — إنستجرام — فيديو DPY4r6yDcuC

---

Do you know how React JS was invented? So back in the early two thousands when Facebook started, it was just a simple PHP website where every time you clicked something, the entire page had to reload from the server, which was really slow and annoying. Wait, what exactly is a server doing in this scenario, and why was reloading the entire page such a problem? Well, imagine every time you wanted to see a new post, the website had to ask Facebook's computer for a completely new version of the whole page, send it across the internet, and your browser had to redraw everything from scratch, even the stuff that didn't change. That sounds inefficient. So what changed? How did they solve this? As Facebook grew bigger with news feed and ads, their code became a nightmare to maintain. That's when this engineer Jordan Walke around two thousand and eleven had an idea while working on the ads platform. But before we get to his solution, what exactly is the DOM? I hear it every time in web development. The DOM or Document Object Model is like a family tree for your web page. The browser takes your HTML and creates this tree structure where every button, paragraph, and image is a node with parent child relationships. So when developers wanted to update something on the page, what did they have to do with this DOM? They had to manually write code to find specific nodes in the tree and change them directly, which was tedious and slow because DOM operations are computationally expensive. That sounds like a lot of work. So what was Jordan Walke's solution? He created React with something called the virtual DOM. Instead of developers tracking every change, they just describe what the UI should look like and React figures out what needs updating. How does this virtual DOM actually work? React keeps a lightweight copy of the DOM in memory. When something changes, it creates a new virtual version, compares it with the old one using a diffing algorithm, and only updates the specific parts of the real DOM that actually changed. That's brilliant. So instead of recreating the entire DOM, you just update the one thing that changed. Exactly. This made Facebook way faster because even though React conceptually re renders everything, it only touches the minimal DOM elements that need changing.