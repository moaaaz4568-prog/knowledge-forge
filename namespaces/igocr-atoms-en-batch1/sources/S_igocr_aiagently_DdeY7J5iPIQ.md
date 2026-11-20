---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_0.txt"
words: 818
sha1: 04b94bd6e9ed84cd96d9983f068a359103e35a3a
lang: en
account: aiagently
quality: ocr+carousel-8
---

# S_igocr_aiagently_DdeY7J5iPIQ

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_0.txt`
> الأجزاء: 8 — `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/aiagently/DdeY7J5iPIQ_7.txt`

<!-- image 0 -->
Turn Any YouTube Video Into a AI Agent
<!-- image 1 -->
STEP 01
Download this YouTube Skill
https://github.com/bradautomates/claude-video
GitHub
bradautomates/claude-video
Give Claude the ability to watch videos from YouTube and other platforms.
2.8k stars
400+ forks
Public
watch.skill
1 Download
watch.skill from GitHub.
2 Go to Settings
Capabilities → Skills
3 Enable
Code execution & file creation.
4 Done
You're ready to use /watch
<!-- image 2 -->
STEP 02
GET YOUR FREE
GEMINI KEY
1 Go to Google AI Studio.
Open your browser and visit
https://aistudio.google.com
2 Create a free Gemini API key.
Sign in with your Google account
and create a new AI API key.
3 Copy the key.
Once it's created, copy the API key
from the dashboard.
4 That's it.
You'll use this key to let Gemini help
Claude understand the actual
YouTube video.
Google
and visit
Home
API keys
Models
Library
More
Gemini
Build with Gemini
Create API key
API key
AIZaSyB8fXk1...7gHk
Key created successfully
Gemini
(understands
YouTube video)
Claude
(Claude
does the work)
<!-- image 3 -->
STEP 03
ADD YOUTUBE ANALYSIS MCP

1 Add YT Analysis MCP to Claude Code.
Open your Claude Code config and add the YT Analysis MCP server.

2 Paste your Gemini API key when the setup asks for it.
This connects Gemini to Claude through the MCP server.

3 Now Gemini can analyze the actual video:

Claude Code
Added
mcpServers: {
  "yt-analysis": {
    "command": "npx",
    "args": ["-y", "analysis-mcp"],
    "env": {
      "GEMINI_API_KEY": "AIzaSyB8fX1...7gHk"
    }
  }
}
GEMINI_API_KEY

Claude Code
(gets full context)
AIzaSyB8fX1...7gHk

Gemini
(analyzes video)
Gemini API Key

YouTube Analysis MCP
Video Analysis
The video contains:
Audio
(what's said)
Visuals
(what's shown)

Claude now gets much more than just text.
It understands the real video — not just the transcript.

What happens on screen
(context & actions)
<!-- image 4 -->
STEP 04
WORDS +
VISUALS
Now your setup can understand two sides
of the video:
YouTube Skill
Captures the words
transcript.
Transcript
"The best way to grow is
with consistent action..."
+
Gemini
Understands the video
and visuals.
Visuals
Scenes
Context
+
Together:
WORDS + VISUALS =
MORE COMPLETE
KNOWLEDGE
<!-- image 5 -->
STEP 05
BUILD YOUR
EXPERT AGENT
Now choose what you want your agent
to learn.
1 Choose your goal
Example:
Want an AI Video Editor?
Your Agent
AI Video Editor
2 Find the best resources
Find the 10 best editing tutorials
on YouTube.
YouTube Tutorials
Video Editing Tutorials (Beginner to Pro)
YouTube • 12:36
Cinematic Editing Techniques
YouTube • 18:42
Advanced Editing in Premiere Pro
YouTube • 22:17
Top 10
10 YouTube videos
3 Give them to Claude
Tell Claude to study those videos.
Claude
Study these tutorials and turn
the best techniques into an
editing skill.
4 Your expert agent is ready
Now you have an AI editing agent
trained around those techniques.
AI Video Editor Agent
Trained
Learnt from:
10 YouTube editing tutorials
Best editing techniques
Pro workflows & shortcuts
Now you have
a personal AI
video editing
expert.
<!-- image 6 -->
AND YOU CAN DO THIS FOR ANY SKILL
Grab 10 YouTube videos. Train your agent.
It's that simple.

01 Sales
Learn proven sales techniques from YouTube.

10 sales videos
Sales Agent
Finds leads. Writes scripts. Helps you close.

02 Copywriting
Learn high converting copywriting strategies.

10 copywriting videos
Copywriting Agent
Writes hooks. Creates copy. Boosts your conversions.

03 Marketing
Learn modern marketing strategies and growth tactics.

10 marketing videos
Marketing Agent
Plans campaigns. Finds content. Grows your brand.

04 Editing
Learn video editing techniques and workflows.

10 editing videos
Editing Agent
Creates edits. Uses best techniques. Saves time.

05 Research
Learn how to find, analyze and organize information.

10 research videos
Research Agent
Finds data. Summarizes info. Gives you the insights.
<!-- image 7 -->
THE WHOLE SYSTEM
THE COMPLETE
YOUTUBE → EXPERT AGENT
Here's the complete system — step by step.

01 The Gap
By default, Claude Code cannot watch
anything. Paste a YouTube link and it has no
way to see or hear the video.
YouTube video
Claude Code

02 YouTube Skill
Install the YouTube skill from GitHub. It pulls
transcripts, analyzes the content, and
extracts the knowledge from any video.
GitHub
YouTube skill
Transcript

03 Get a Free Gemini API Key
Create a free API key in Gemini at Google AI Studio.
Gemini already understands YouTube links
natively, because Google owns both.
Google AI Studio
Free API key
Gemini

04 Add YT Analysis MCP
Plug Gemini into Claude Code with the
YT Analysis MCP server. Gemini analyzes
the real video frames and audio.
Gemini
YT Analysis MCP
Claude Code

05 Words + Visuals
The raw transcript captures every word said.
Gemini adds its native understanding of the
visuals.
Transcript
(words + context)
Visuals + audio
(frames + sound)
More complete
knowledge
10 best tutorials

06 Build Expert Agents
Use a multi-skill framework. Feed it the 10
best editing tutorials and you get an editor
agent that uses their techniques.
Editor agent
Outreach
Marketing
Content

Want all the resources?
COMMENT "YT AGENT"
and I'll send you the complete guide + resources.