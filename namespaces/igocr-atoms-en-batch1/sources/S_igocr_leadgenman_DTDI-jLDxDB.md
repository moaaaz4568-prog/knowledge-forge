---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DTDI-jLDxDB_0.txt"
words: 347
sha1: 090e255424a5e53e61e59924898d5232d4ef2a38
lang: en
account: leadgenman
quality: ocr+carousel-3
---

# S_igocr_leadgenman_DTDI-jLDxDB

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DTDI-jLDxDB_0.txt`
> الأجزاء: 3 — `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DTDI-jLDxDB_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DTDI-jLDxDB_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/leadgenman/DTDI-jLDxDB_2.txt`

<!-- image 0 -->
Single System
Multi-Agent System
System System
Agentic Architectures

CodeAct Agent
The tool-use mechanism is built on the AI agent that can interact with its environment by writing and running code. This work proposes to use executable Python code to consolidate LLMs' actions into a unified action space (CodeAct)

ReAct Agent
Reasoning and acting (ReAct) framework to combine chain of thought (CoT) reasoning with external tool use ReAct prompts LLMs to generate verbal thought traces and actions for a task. ReAct overcomes issues of hallucination and error propagation prevalent in (CoT) reasoning using tools.

Agentic RAG
Agentic RAG means an AI agent-based implementation of RAG. Specifically, it adds AI agents into the RAG pipeline to orchestrate its components and generate additional actions beyond simple information retrieval and completion

User
Memory
AI Agent
Tools
Memory
AI Agent
Tools
Memory
AI Agent
Tools
Action
CodeAct
Result
Think
Agent
Environment
User
Query
Observation
Outcome
Reason
LLM 1
LLM 2
Query
Tools
Output
Query
Agent
Tools
Vector Search
Vector Db
Output
Generator
<!-- image 1 -->
6 Patterns
Examples

How
AI Agent
Works

Tool Use with MCP
The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context and tools to LLMs. MCP aims to simplify this by providing a common API and transforming this into an "M+N problem" instead of an M×N integration problem.

Self-Reflection
Allows autonomous agents to improve iteratively by refining past action decisions and correcting previous mistakes. The Reflection Pattern consists of three key steps: generation, self-reflection, and iterative refinement.

Multi-Agent System
In ADK, a multi-agent system is an application where different agents, often forming a hierarchy, collaborate or coordinate to achieve a larger goal. Used by Gemini Deep Research for complex research tasks.

Query
Agent
Output
MCP Server 1
MCP Server 2
User
Main LLM
Memory
Tools
Result
Generator
Critique
Yes
No
First draft
User
Query
Agent
Memory
Tools
Agent 1
Agent n
Output
Agent LLM
User
Query
Agent
Memory
Tools
Output
<!-- image 2 -->
Single-Agent System
User
AI Agent
Memory
Tools
Multi-Agent System
User
AI Agent
Memory
Tools
Tools
AI Agent
Memory
AI Agent
Tools
Memory
AI Agent
Memory