---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/algorithmswithpeter/DWzMkIqiRFP.txt"
words: 293
account: algorithmswithpeter
lang: en
quality: transcript
---

# S_ig_algorithmswithpeter_DWzMkIqiRFP

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/algorithmswithpeter/DWzMkIqiRFP.txt` — حساب: algorithmswithpeter — إنستجرام — فيديو DWzMkIqiRFP

---

Peter, everyone keeps yelling "just dockerize it." What does that even mean? It means your app runs inside the same packaged environment everywhere, so developers can finally stop saying, "Bro, it works on my machine!" Okay, so how do I do it from zero? First, install Docker Desktop from docker.com. If you're on Windows, it may ask you to install WSL2 because apparently nothing can ever just install normally. Open Docker Desktop and make sure it says the engine is running. Congratulations, you've installed a giant shipping company for your code. Then what? Open your project in VS Code and create a file called Dockerfile. That file tells Docker what environment your app needs, what dependencies to install, what files to copy, what port to expose, and what command should start the app. In short, it's a recipe for trapping your app in a box and forcing it to behave. Okay, so after creating that, what do I do? Open terminal in your project folder and run docker build -t your app name. That creates a Docker image. What's an image? Think of image as the blueprint, container as the running app made from that blueprint. So how do I run it? Run command docker run -p 3000:3000 your app name. That maps your local port to the app inside the container. Then open localhost:3000 and your app should run. And if it doesn't, welcome to debugging where grown adults stare at logs like they're reading ancient prophecy. And what if my project has front end, back end, and database? Then use Docker Compose so multiple containers can run together without your laptop sounding like it's filing for divorce. Comment next topic below and we'll cover and explain them in our next video.