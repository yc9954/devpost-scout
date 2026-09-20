---
slug: "ta-da-intelligent-teaching-assistant"
url: "https://devpost.com/software/ta-da-intelligent-teaching-assistant"
title: "TA-DA: Intelligent Teaching Assistant"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1042
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# TA-DA: Intelligent Teaching Assistant

> Why are students Googling mid-lecture? TA-DA keeps them in the room: AI teaching assistant built into Zoom that detects confusion and generates concept cards instantly. No context loss. Just learning.

[Devpost](https://devpost.com/software/ta-da-intelligent-teaching-assistant) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** elasticsearch, fetch.ai, javascript, langchain, llms, python, rmts, zoom

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for ta-da

## Body

TA-DA: Smart Teaching Assistant Inspiration We've all been in that Zoom lecture where the instructor asks "Any questions?" and silence follows. Not because everyone understands—but because no one wants to interrupt. Students tab out to Google concepts mid-lecture, losing context. Instructors teach blind, with no feedback loop until the exam reveals the damage. The problem isn't recording or transcription. Tools like Otter.ai capture words. But they don't close the learning loop. TA-DA was born from a simple question: What if the classroom could sense confusion in real time and intervene—without breaking the flow? We wanted to build a teaching assistant that lives where learning happens: inside Zoom, always listening, always ready, never interrupting unless you need it. What it does TA-DA is an AI-powered teaching assistant built natively into Zoom using the Real-Time Meeting SDK (RTMS). It runs as an in-meeting side panel—no browser tabs, no context switching. Core Features: Auto-Generated Concept Cards : As the instructor teaches, TA-DA autonomously detects topic boundaries and generates concept cards with explanations and examples—appearing in real time on the Learning Timeline. Intelligent Q&A : Students ask questions directly in the side panel. TA-DA doesn't just answer—it retrieves relevant transcript context, explains the concept, and provides examples. Live Learning Analytics : Instructors see which concepts students marked as "Lost" or "Understood," enabling instant intervention. Catch-Up Summaries : Joined late? Ask TA-DA for a summary and get a structured recap of everything covered so far. No Tab Switching : Everything happens inside Zoom. No Googling mid-lecture. No context loss. Just seamless learning. How we built it We designed TA-DA as a real-time, multi-agent system with four key layers: 1️⃣ Zoom RTMS + SDK (Frontend) Built a native Zoom app using the Real-Time Meeting SDK for in-meeting side panels Integrated RTMS pipeline to stream live transcripts and meeting events Created a responsive UI with Learning Timeline, Q&A interface, and analytics dashboard Designed for Zoom Marketplace deployment—one-click install for educators 2️⃣ Node.js Backend (Orchestration) Express.js API to handle transcript ingestion, agent communication, and search queries WebSocket events for real-time updates between Zoom, Elastic, and Fetch.ai agents Proxy layer for concept card retrieval and agent conversation endpoints 3️⃣ Elasticsearch (Memory Layer) Two indices: ta-da-latest (transcript chunks) and ta-da-concept-cards (structured concepts) Semantic search with vector embeddings for intelligent retrieval Filters by meeting ID, timestamps, and concept tags The single source of truth for everything we know about the lecture 4️⃣ Fetch.ai Agents (Intelligence Layer) Concept Card Agent : Runs on Fetch.ai's Agentverse platform Monitors new transcript chunks via Redis state tracking Detects topic boundaries using LLM-powered segmentation Generates concept cards (title, short explanation, example) and indexes them to Elastic Autonomous 60-second intervals with pause/resume controls Agent Tools : query_elastic_chunks() – Retrieve transcript context create_concept_card() – Generate and store concept cards call_backend_agent_converse() – Provide summaries and answers LLM Integration : OpenAI GPT-4 for concept extraction, summarization, and Q&A 5️⃣ Tech Stack Frontend : Zoom RTMS SDK, JavaScript, CSS Backend : Node.js, Express.js, WebSockets Memory : Elasticsearch (with semantic search) Agents : Fetch.ai Agentverse, Python LLM : OpenAI GPT-4 / xAI State : Redis (incremental processing, pause/resume) Deployment : Docker, cloud-ready architecture Challenges we ran into 1. Real-Time Agent Coordination Running autonomous agents while avoiding duplicate processing was tricky. We solved it with Redis-based state tracking : each agent stores the last processed chunk index per meeting and only processes new chunks incrementally. 2. Zoom RTMS Learning Curve The Real-Time Meeting SDK documentation was sparse. We spent hours debugging WebSocket connections, transcript streaming delays, and side panel rendering. Eventually, we built a robust event-driven architecture that handles live data gracefully. 3. Live Avatar Instability We built a TA avatar assistant with lip-sync and custom-configured voice for a human-like learning experience. The feature works but isn't production-stable yet—lip-sync timing drifts, and rendering performance degrades in low-bandwidth scenarios. It's one of our most exciting features, but needs optimization. 4. Concept Boundary Detection Determining when one "concept" ends and another begins is subjective. We iterated on LLM prompts, testing different segmentation strategies (sliding windows, topic modeling, explicit markers) before landing on a hybrid approach: fixed chunk windows + LLM-based topic extraction. 5. Elastic Search Latency Initially, our searches were slow because we were doing full-text queries on large transcript indices. We optimized by: Adding semantic vector search with embeddings Filtering by meeting ID and timestamps Pre-indexing concept cards separately from raw transcripts 6. Fetch.ai Agent Debugging Debugging agents running on Agentverse was non-trivial—logs were async, and testing required deploying to the cloud. We added verbose logging, local Redis mocking, and a manual trigger endpoint to iterate faster. Accomplishments that we're proud of Built a fully functional AI teaching assistant in 36 hours —from idea to live demo Seamless Zoom integration with native side panel—no browser tabs required Autonomous agents that generate concept cards without human intervention Real-time learning analytics that give instructors actionable feedback Scalable architecture ready for thousands of concurrent classrooms Closed the learning loop : sense confusion → intervene → verify understanding We didn't just build a transcript tool. We built a learning intelligence system that actively improves education outcomes. What's next for TA-DA Short-term: Stabilize Live Avatar : Fix lip-sync timing, optimize rendering, and make the TA avatar production-ready for a truly immersive learning experience Voice-based Q&A : Students speak questions instead of typing Multi-language support : Real-time translation for global classrooms Instructor dashboards : Advanced analytics—confusion heatmaps, engagement scores, concept mastery Pre-class prep mode : Upload slides/notes before class; TA-DA cross-references during lecture Long-term: TA-DA as Substitute Teacher : Train TA-DA on a professor's teaching style, course materials, and past lectures—if the professor can't join, TA-DA delivers the lecture autonomously with the live avatar Adaptive learning paths : TA-DA generates personalized review sessions based on which concepts each student struggled with Cross-meeting memory : Agents remember past lectures, building a knowledge graph across an entire course Federated agents : Specialized agents for different subjects (Math Tutor, Code Debugger, Writing Coach) Zoom Marketplace launch : One-click install for universities, bootcamps, and corporate training The vision? Every classroom gets a teaching assistant that never sleeps, never judges, and scales infinitely. Education shouldn't be a guessing game. With TA-DA, it won't be. TA-DA: Teaching Assistant Done Autonomously The closed-loop learning system built for Zoom. <div