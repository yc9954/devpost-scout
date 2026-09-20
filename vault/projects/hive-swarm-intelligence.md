---
slug: "hive-swarm-intelligence"
url: "https://devpost.com/software/hive-swarm-intelligence"
title: "HIVE: Swarm Intelligence."
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 881
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# HIVE: Swarm Intelligence.

> HIVE is your personal workforce that makes digital busywork obsolete. Launch a swarm of parallel, background computer use agents to solve any computer use task — specialized agents for GSuite and more

[Devpost](https://devpost.com/software/hive-swarm-intelligence) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[labor_employment]]
**substrate** [[structured_db]] [[web_dom]]

**stack** browserbase, claude, fetch.ai, modal

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

home many computer use agents in action simultaneously for a task independent browser w/ computer use agent per task modal deployment of gpt-oss-120b on a B200 instance Inspiration We spend hours every day on repetitive digital tasks — replying to emails, filling out forms, creating slide decks, scheduling meetings. What if you could deploy a swarm of computer use agents to handle all of them at once, all in parallel and asynchronously? We were inspired by the parallel efficiency of a beehive: every worker bee knows its job, and together they accomplish far more than any single bee could alone. We built Hive to bring that same model to personal productivity. Digital busywork is now obsolete. What it does Hive is a multi-agent AI platform with a “queen bee” orchestrator that deploys parallel "worker bees" to handle your digital busywork across Gmail, Google Docs, Sheets, Slides, Forms, Calendar, Drive, and any website — all at the same time. Type in your tasks (one per line), hit deploy, and watch your swarm come alive: "Reply to my unread emails". Hive reads each thread, classifies intent, generates a draft in your personal writing style, and opens it in real Gmail for your approval. "Create a pitch deck about our Q4 results". A browser agent autonomously builds a Google Slides presentation. "Fill out this survey: forms.google.com/...". An agent navigates to the form and fills it out based on your context. "Research competitor pricing and summarize". A web research agent searches, synthesizes, and delivers a report. “Create a spreadsheet of …”. An Excel agent creates a spreadsheet of information. Features Orchestrate dozens of computer use agents, specialized for numerous tasks (research, docs, slides, web navigation) for multi-agent, multi-turn agentic AI systems. Stagehand computer use harness with Claude Opus for efficient and accurate computer navigation Asynchronous agents operating in parallel, working on dozens of personal tasks at once through Browserbase windows. Computer use agents are currently less adopted because they are slow and synchronous; what if they could operate asynchronously in the background, working on many tasks all in parallel? Just like how Claude Code and Devin are background agents, Hive is a background computer-use agent. Extremely fast and efficient: highly optimized deployment of GPT OSS 120B in MXFP4 on B200 with speculative decoding, continuous batching, and custom FusedMoE kernel via Modal deployment as a “flash” option. 24x higher throughput than native Huggingface Inference. We serve browser use models on Modal via high-throughput memory-efficient vLLM library on a B200 GPU deployment. Continual learning and personalization: agent continuously learns from recorded examples of users navigating common webpages. “Order me the usual on Doordash” → agent learns what “the usual” is from a user-recorded example with the restaurant and order on Doordash. “Search up the syllabus for 6.1060.” Agent learns that the user attends MIT and the place to look for syllabi is an educational platform called Canvas, with user login info. AI Safety and human-in-the-loop: for tasks requiring approval (e.g. purchases, mass emails), the agent will always ask for human feedback. Sandboxed execution in a VM with constant resource and behavior monitoring to prevent rogue agentic behavior. Draft the whole email, but have a quick human review before sending. Go through with the order, but have the human approve the purchase page before buying. Custom, highly optimized tool calls for fast access to GSuite Applications Docs, Gmail, Slides, Forms, Excel are supported We develop a custom toolkit consisting of commonly used GSuite tool calls, APIs, etc. to make specific tasks extremely fast. A general agent will use a VLM and parse the DOM which is much slower. Context and session management while using a sandboxed VM (Browserbase): cookies and login info are saved so the agent knows what to do in the future. How we built it Browser Management and Agent Harness We use BrowserBase + StageHand as our baseline agent harness and how the agent interacts with the VM. We created custom toolkits for specific applications that build on top of the harness. Claude Agent SDK as the model Computer Use Agent: Vision Language Model + HTML DOM Processing Extremely high throughput and memory efficiency We deployed GPT-OSS-120B on a Modal B200 with an OpenAI API compatible endpoint with highly optimized inference implementation consisting of speculative decoding and fusedMoE Triton kernels. This serves as a “flash” option for users which is faster than Opus — key if users care about speed. Agentic AI orchestration + workers Claude Agent SDK, langchain, fetch.ai. Custom tool calls for different GSuite applications Parallelization and Asynchronous Operations Virtual Machines for each browser On-demand inference via Modal deployment Front-end + UI Vercel + Next.js Real-time websocket streaming between VM and user view. Challenges we ran into Computer use agents are slow and inefficient on common tasks (Docs, Slides, Gmail). We created an optimized set of tool calls for the agents: specific APIs and functionalities that are hyper-optimized for GSuite. We built an orchestration framework with parallel agents operating asynchronously to complete tasks extremely quickly. We built an open source deployment of GPT-OSS 120B with low latency inference on Modal with vLLM. Computer use agents didn’t know how to complete tasks I personally cared about (e.g. “find the syllabus for x class on Canvas”). Solution: real-time human feedback + training the agent. <div