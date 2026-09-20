---
slug: "liquilex"
url: "https://devpost.com/software/liquilex"
title: "LiquiLex"
hackathon: "The AI Champion Ship "
organization: "LiquidMetalAI"
winner: true
words: 800
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/developer"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# LiquiLex

> LiquiLex is an advanced AI-powered platform designed to help businesses and developers navigate complex zoning regulations, building codes, and permit fees in Austin, Texas.

[Devpost](https://devpost.com/software/liquilex) · hackathon [[The AI Champion Ship]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[civic_government]] [[developer_tools]] [[legal_justice]]
**user** [[developer]] [[small_business]]
**substrate** [[document_pdf]] [[geospatial]] [[regulation_legal_text]] [[structured_db]]

**stack** antigravity, cerebras, elevenlabs, framer, gemini3pro, leaflet.js, liquidmetal, next.js, node.js, postgis, postgresql, raindrop, tailwind, valkey

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for liquilex

## Body

Landing Page Login Page User Dashboard Lex Agent Chat Screen Zoning Check Screen Calculate Permit Fees Screen Raindrop Services being used Vultr Databases I'm using Cerebras Service I'm using Inspiration The inspiration for LiquiLex came from witnessing the crushing weight of regulatory complexity on small business ambition. I observed that opening a simple business, like a food truck, requires navigating three disconnected and hostile silos: Unstructured Law: Ordinances hidden in hundreds of pages of dense PDFs. Geospatial Restrictions: Zoning maps that are unintelligible without GIS expertise. Structured Math: Fee schedules buried in obscure tables. I realized that current AI "chatbots" weren't enough. A food truck owner doesn't need a summary of the law; they need a "Civic Operating System" that acts. I built LiquiLex to decouple this complexity from entrepreneurship, creating an agent that doesn't just chat, but checks zoning, calculates fees with 100% accuracy, and speaks naturally to users in the field. What it does LiquiLex is an agentic interface that unifies the regulatory journey. It acts as a "Civic Navigator" that: Acts, Don't Just Chat: It creates tasks ( manageTasks ) and monitors regulatory changes specific to the user's business type (e.g., Food Truck vs. Bar) using a "Regulatory Watchdog". Verifies "Spatial Truth": It performs real-time point-in-polygon checks using Vultr PostGIS to tell a user exactly where they can operate. Calculates Fees Deterministically: It translates natural language ("Fee for a 2,500 sq ft patio?") into precise SQL queries to guarantee accurate pricing, avoiding LLM math errors. Speaks Naturally: It features a voice-native interface where users can talk to Lex in the field, with responses synthesized instantly via ElevenLabs. How I built it I utilized a novel "Two-Plane" Architecture to maximize efficiency and speed: 1. The Build Plane (Zero-Cost Agentic) I used Antigravity powered by Gemini 3 Pro as our "AI Architect." Instead of manually writing boilerplate, I used a "One-Shot" prompt to generate our entire Infrastructure-as-Code (IaC) via the Raindrop CLI. 2. The Runtime Plane (The "Golden Triangle") To achieve a "magic" feeling, I combined three powerful technologies: Intelligence (Cerebras): I leveraged Llama 3.3 70B on Cerebras to achieve ~2,000 tokens/sec inference, crucial for our low-latency voice interaction. Cognition (LiquidMetal Raindrop): I deployed specialized services— SmartBuckets for PDF RAG, SmartSQL for math logic, and SmartMemory for user context. Infrastructure (Vultr): I used Vultr Managed PostgreSQL (with PostGIS) for geospatial queries and Vultr Valkey for high-speed session caching. Voice (ElevenLabs): I integrated ElevenLabs via a WebSocket proxy to create a seamless "Brain-to-Voice" loop. Challenges I ran into The "Math Hallucination" Problem: LLMs are notoriously bad at math. I couldn't risk an agent guessing a permit fee. I solved this by forcing the agent to use SmartSQL , translating natural language into SQL queries (e.g., SELECT fee FROM fees WHERE... ) to ensure 100% deterministic accuracy. The Latency Barrier: Making a voice agent feel "human" requires near-instant responses. I had to optimize the journey from Audio -> Text -> Cerebras Inference -> Tool Use -> TTS to remain under ~1.2 seconds. This required tight orchestration between Vultr's compute and Cerebras's inference speed. Data Ingestion: Parsing complex "Zoning Permitted Use Matrices" from PDFs was difficult. I used AI Decomposition within Raindrop SmartBuckets to extract table rows (e.g., "Cocktail Lounge: Conditional in CS-1") into structured queryable data. Accomplishments that I'm proud of Solopreneur Feeling: Ideated, developed and deployed the entire app alone in around 10 days. Hyper-Speed Runtime: Achieving a total voice latency of ~1.2 seconds, creating a truly "magical" user experience. The "Thinking Chain" Visualizer: I built a UI that shows the user exactly how the agent is thinking—displaying "Reading PDF...", "Querying Spatial DB...", or "Calculating Fee..." in real-time to build trust. Zero-Cost Build: I successfully provisioned the entire backend using free tools and the "Antigravity" architect pattern, proving that complex software can be built by solopreneurs without massive budgets. What I learned Latency is the UI: In voice interfaces, speed is more important than perfect grammar. The Cerebras integration was not just a performance upgrade; it was a UX necessity. Agents Need "Hands": A chatbot that can only talk is a toy. Giving Lex the ability to write to databases ( SmartMemory ), query maps ( PostGIS ), calculate permit fees and create tasks transformed it into an expert agent. Context is King: By persisting the "Business Profile" in SmartMemory , the agent became proactive rather than reactive, remembering the user's specific journey across sessions. What's next for LiquiLex Expansion to New Cities: The "SmartBucket" architecture allows us to ingest ordinances from other municipalities simply by uploading new regulations. Full Legal Integration: Moving beyond information to execution—automatically filling out and filing PDF permit applications on behalf of the user. Mobile App Launch: Taking the "Voice Proxy" logic and wrapping it into a native mobile experience for true "on-site" usability. <div