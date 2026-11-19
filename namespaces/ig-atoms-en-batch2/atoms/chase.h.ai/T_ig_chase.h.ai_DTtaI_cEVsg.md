---
type: atom
topic: instagram-transcripts
source: sources/S_ig_chase.h.ai_DTtaI_cEVsg.md
location: instagram/chase.h.ai
---

# T_DTtaI_cEVsg_01

"So this technical paper just came out a couple weeks ago from MIT, and they're claiming that they've essentially solved the context window issue with their new recursive language model system. So for normal AI systems, you're limited by the context window, and in this study they used GPT-5, which has a context window of 262, 000 tokens." — sources/S_ig_chase.h.ai_DTtaI_cEVsg.md

# T_DTtaI_cEVsg_02

"Now, as you know, the closer you bump up against that context window, the worse their performance gets. You can see that in this graph right here. They gave it a couple tests. The more input it gets, the worse it does, right? That's why you see everything sloping down into the right. Now, the big thing with this study is they brought in the RLM, the recursive language model framework." — sources/S_ig_chase.h.ai_DTtaI_cEVsg.md

# T_DTtaI_cEVsg_03

"Now if we zoom in here, we can see those two same tests depicted here. Now two things to note. One, notice it goes past the context window of 272, and it goes all the way to a million. And the effectiveness is way higher. If we look at it here on the olong pairs, it scored about a 50. Over here with the base model, what did we get? It's at almost zero. Now here's some more tests to look at." — sources/S_ig_chase.h.ai_DTtaI_cEVsg.md

# T_DTtaI_cEVsg_04

"The answer is with recursive language models, which is what you see right here. Now on my YouTube, I do a full deep dive and break this down piece by piece so you can really understand it. So check that out." — sources/S_ig_chase.h.ai_DTtaI_cEVsg.md

# T_DTtaI_cEVsg_05

"But to quickly summarize it, instead of taking a giant million token document and shoving it into ChatGPT because you can't do that because of the context window, instead they have it inside of a Python environment and they never feed that document to ChatGPT exactly." — sources/S_ig_chase.h.ai_DTtaI_cEVsg.md

# T_DTtaI_cEVsg_06

"Instead, what they essentially do is they chop up that document into chunks and it figures out how to chop it up using code, and then it sends those chunks to recursive large language models that the main GPT agent has spawned, right? So think of little mini ChatGPTs. In this case, they use GPT-5 mini. It then processes those chunks and sends the answer to the primary LLM. That's how they do it." — sources/S_ig_chase.h.ai_DTtaI_cEVsg.md

# T_DTtaI_cEVsg_07

"So like I said, really interesting stuff. If you want to know more about this paper, just search up recursive language models and it'll be the technical paper that pops up. And again, I did a deep dive on my YouTube as well, so check that out." — sources/S_ig_chase.h.ai_DTtaI_cEVsg.md
