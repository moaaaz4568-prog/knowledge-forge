---
type: source
topic: instagram-ocr
origin: "/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_0.txt"
words: 1227
sha1: 5971cc612f898abf6bbeb1bf05e20cbbc459cf82
lang: en
account: divyannshisharma
quality: ocr+carousel-12
---

# S_igocr_divyannshisharma_DXrkddHjIG8

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_0.txt`
> الأجزاء: 12 — `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_0.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_1.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_2.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_3.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_4.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_5.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_6.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_7.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_8.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_9.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_10.txt`؛ `/home/hatch/workspace/instagram-reels-texts/ocr/divyannshisharma/DXrkddHjIG8_11.txt`

<!-- image 0 -->
Divyanshi
@divyanshi sharma
10 AI skills
to learn in 2026
(Complete guide with
FREE resources)
Swipe →
Layers
Nodes
Layers
def learn_model(data):
    commands
    key_commands=[data]
    cey = learn_model(cey)
    # learn command
    data = prospect(data)
    # Data: results data
    return model(data)
Data Collection
Preprocessing
Feature
Engineering
Model Training
AI
<!-- image 1 -->
1. LLM Fundamentals
LLM Fundamentals
• How LLMs work (at a high level) • What they’re good at vs where they fail • Working with APIs like OpenAI and Anthropic • Structured outputs (JSON, schemas, tool responses) • Prompt engineering across different tasks
X □ -
1. Input
2. Tokenization
3. Transformer (Neural Network)
Multiple Layers
Inside the Transformer Block
Add & Norm
Feed Forward Network
Add & Norm
4. Decoding
5. Output
From input to intelligent output
Multi-Head Self-Attention
The model looks at all words in the input to understand their relationships.
Focuses on relevant parts of the input
Learns from billions of examples.
Adds the original input back in (residual connection) and normalizes.
Stabilizes training and improves performance
Applies transformations to extract higher-level features.
Learns complex patterns in the data
Ensures stable gradients and better learning
Foundation for many AI applications
Billions of parameters (trained weights)
Emergent capabilities through scale
Swipe →
<!-- image 2 -->
2. Retrieval Augmented Generation

• Injecting custom data into LLMs • Vector search + semantic retrieval • Tools like Elasticsearch, Qdrant • Chunking strategies (this matters more than people think) • Handling real world data: PDFs, web pages, transcripts
Practice projects: FAQ assistant Document, Q&A system, Internal knowledge search

Ground LLMs on your data for accurate, up-to-date responses

Data Sources
Documents
Web Pages
PDFs
Databases
APIs

Ingestion & Chunking
Split documents into manageable chunks

Chunking
[0.21, 0.21, ...]
[0.11, 0.52, ...]
[0.73, 0.31, ...]

Embedding
Convert chunks into embedding vectors

Vector Database
Store and index vectors for fast similarity search

Retrieve & Generate
User Query
"What is quantum computing?"
Retrieves top K most relevant chunks
LLM uses context + retrieved chunks
Generated Response

How Retrieval-Augmented Generation Works
User asks a question
System converts query to embedding
Searches vector DB for relevant chunks
Retrieves top K most relevant chunks
LLM uses context + retrieved chunks
Generates accurate, context-aware response

More Accurate
Uses your data as source of truth
Up-to-Date
Reflects latest information in your data
Reduced Hallucinations
Grounded with retrieved evidence
Scalable
Works with data of any size
Secure & Private
Your data stays in your infrastructure

Swipe →
<!-- image 3 -->
3. AI Agents

• Tool calling (LLMs that can act, not just respond) • Agent loop: think → act → observe → repeat • Frameworks: LangChain, PydanticAI, OpenAI Agents SDK, Google ADK • MCP
• Multi-agent systems (routing, coordination, pipelines)
• Projects: Web research agent, Data extraction pipeline, Multi-agent workflow

Practice projects: Web research agent, Data extraction pipeline, Multi-agent workflow

X □ —
AI agents perceive, reason, act, and learn in a continuous loop to achieve goals.

1. Think (Reason)
Understand the goal, analyze context, and decide what to do next.

2. Act (Tool Use)
Use tools, APIs, or plugins to take action in the environment.

3. Observe (Results)
Observe the results, evaluate outcomes, and update the agent’s understanding.

4. Reflect (Learn)
Evaluate outcome, learn from feedback, and refine strategy.

Memory
Stores context, history, and knowledge for better decisions.

Search
Web / Docs Search

Database
Query Databases

API
Call External APIs

Code Executor
Run Code / Scripts

File System
Read / Write Files

Email / Slack
Send Messages

Analytics
Generate Reports & Insights

More
Custom Tools & Integrations

Autonomous
Works independently towards goals

Efficient
Completes complex tasks faster

Adaptive
Learns and improves over time

Reliable
Uses memory and feedback to reduce errors

Extensible
Connects with any tool, API, or data source

Swipe →
<!-- image 4 -->
4. Testing AI System

• Testing tool usage and outputs • Evaluating consistency
• Using LLMs as judges (yes, meta—but useful)

Goal: Make AI systems reliable, not just impressive

Swipe →
<!-- image 5 -->
5. Monitoring and Observability

• Tracing agent workflows • Logging interactions • Cost tracking • Feedback loops • Dashboards (Grafana, OpenTelemetry)

👉 Real-world impact: This is what separates demos from production systems

Track, analyze, and understand your AI systems in real time

Observability Dashboard

What to Monitor
Latency
Error Rate
Throughput
Token Usage
Cost
Model Quality
Traces
Logs
Alerts

See Everything
Full visibility across your AI stack

Detect Issues Early
Identify problems before users do

Optimize Performance
Improve latency, throughput, and reliability

Reduce Costs
Monitor usage and optimize spend

Build with Confidence
Validate system performance and reliability

Swipe →
<!-- image 6 -->
6. Evaluation

• Offline eval datasets • Measuring retrieval quality
• Synthetic data gen • Prompt optimization based on results

Goal: Move from "It feels good" → it's measurable

Swipe →
<!-- image 7 -->
7. Production System
• Turning notebooks into real services
• Deployment
(Streamlit for quick prototypes) • Cloud platforms: AWS / GCP / Azure • Guardrails & safety layers • Parallel processing
Production & Deployment
Build, deploy, and operate reliable AI systems at scale
Swipe →
<!-- image 8 -->
8. Supporting Skills

• Python & Engineering Basics • Web Development (For Real Products) • Cloud & Infrastructure • Databases • ML Fundamentals (Just Enough) • Data Engineering • Languages Beyond Python

Critical Skill Areas (Click to explore)
1. Python & Engineering Basics
2. Web Development (For Real Products)
3. Cloud & Infrastructure
4. Databases
5. ML Fundamentals (Just Enough)
6. Data Engineering
7. Key Languages

Core Skill Breakdown (Details)
Python: 80%+ rtes, data, backends
Testing: Code quality, automations
FastAPI: Backend standard for AI
React UI: Frontend UI
Cloud Choice: (AWS, GCP, Azure)
Docker: Containerization
PostgreSQL: (Default choice for SQL)
Vector DBs: (Pinecone, Weaviate)
Next.js: (Frontend framework)
APIs: (REST, GraphQL)
Kubernetes: (Orchestration)
DBs: (TypeScript, SQL)

Skills (Metrics)
Git Workflows: (Code versioning, collaboration) 82%
CI/CD: (Automated testing, deployment)
Cloud Platform Usage: (AWS, GCP, Azure)
Vector DB Importance: 75%
SQL Mastery Demand: 90%

Applying the Skills
Data Tools: (Pandas, NumPy, Spark)
ML Essentials: (Scikit-learn, TensorFlow)
Languages: (Python, SQL, TypeScript)

Swipe →
Swipe →
<!-- image 9 -->
9. Typical AI Engineering Stack

• Frontend: React / Next.js • Backend: FastAPI • AI orchestration: LangChain, LangGraph, PydanticAI • LLMs: OpenAI, Anthropic, Groq • Vector DB: Pinecone / Weaviate / Qdrant • Infra: Docker + Kubernetes + Cloud • Monitoring: OpenTelemetry, Grafana • Evaluation: LLM judges, Evidently

Continuous Architecture Diagram

1
User Interface (Frontend)
Frontend Frameworks:
React, Next.js

2
API Layer (Backend)
Backend Services:
FastAPI
PydanticAI

3
AI Application Logic (Orchestration)
Orchestration & Agents:
LangChain
LangGraph

4
Core Models (LLMs)
Large Language Models (LLMs):
OpenAI, Anthropic, Pinecone, Groq, local models

5
Vector Databases
Vector Databases:
Pinecone, Weaviate, Qdrant

6
Data Store (Memory)
Data Stores:
Pinecone, Weaviate, Qdrant

Infrastructure (Platform)
Orchestration & Cloud:
Docker, Kubernetes, Cloud

AI Components Breakdown

Rule-based
Safety Checks
Human Eval
Collaboration
LLM Judges
Evidently
Evaluations
LLM judged
tools like
Aider, Cline
Evaluation Tools

Operational Pillars

Frontend
Collect frontend
data to monitor:
React, Next.js

Backend
Choose a framework
to implement:
FastAPI

LLMs
Is it useful
models and
specific needs.

Orchestration
Useful to
agents and
orchestration.

Continuous Stack Health (Monitoring & Ops)

System Latency (P99)
API Request Volume

Model Response Accuracy (Eval)
Vector DB Recall

Deploy Flow
Collect Data
Preprocess
Index
Judge
Deploy

Monitoring: OpenTelemetry, Grafana

Swipe →
<!-- image 10 -->
10. Skill Priority

* Must-Have: Python, Prompt engineering, RAG systems, One cloud platform, Docker • High-Value: LangChain or PydanticAI, FastAPI, TypeScript, CI/CD, Kubernetes, PyTorch basics • Differentiators: Agent frameworks (LangGraph, CrewAI), Fine-tuning models, Evaluation systems, Vector databases

Swipe →
<!-- image 11 -->
COMMENT "AI GUIDE"
DON'T GET LEFT BEHIND!
FOLLOW @DIVYANSHISHARMA