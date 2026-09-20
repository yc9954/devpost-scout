---
slug: "the-grand-caste-nova-event"
url: "https://devpost.com/software/the-grand-caste-nova-event"
title: "The Grand Castle - Nova orchestration"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 1116
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "domain/supply_logistics"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# The Grand Castle - Nova orchestration

> The Grand Castle is a sophisticated multi-agentic AI system that uses Amazon Bedrock's Nova models to focus on operation and visual storytelling.

[Devpost](https://devpost.com/software/the-grand-caste-nova-event) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[media_journalism]] [[supply_logistics]]
**substrate** [[financial_record]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** asyncpg, boto3, docker, duckduckgo-search, fastapi, langchain, langchain-aws, langgraph, pydantic, python-multipart, redis, sqlmodel, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for the grand caste - nova orchestration

## Body

System Arcitecture Inspiration I do admire Art (most of the time i don't understand it), (un)fortunately i am not good at it. When multimedia LLMs arrived, I spent hours generating images and videos, but I often felt a disconnect—I couldn't quite capture the emotion I was looking for, and even when the results were beautiful, it felt like the AI deserved more credit than the prompt. So here i am with the Nova Orchestra were Nova gets all the credit. The Castle part is born of Creative thinking(Definitely not hallucination!!!) What it does The Grand Castle is a sophisticated architectural implementation designed to transcend the limitations of traditional linear chat applications. By treating user commands as "Imperial Decrees," the system utilizes a non-blocking, dual-tier architecture that allows for continuous, asynchronous interaction without forcing the user to wait for individual query completions. At its core is a persistent Royal Archive(PostgreSQL database) that maintains a real-time session history and evolving summary, enabling the AI to intelligently synthesize multiple rapid-fire requests—such as combining the first two answers of a five-query sequence while simultaneously updating the context for the remaining tasks. It is essentially a castle where the Nova Orchestra performs its Grand Art. The Grand Castle is a sophisticated multi-agentic AI system that treats the user as an Emperor whose command is absolute. Specialized Guards (LLMs) accept user commands asynchronously, conducting investigations using available tools like DuckDuckGo web search. They then archive these findings in Redis, making them available for the Scholar (LLM) to organize and present back to the Emperor. Upon the Emperor's command to begin a Grand Event, a second multi-agentic system, the Nova Orchestra, performs its Grand Art based on real-world events. This performance is presented to the Emperor, and the Scholar remains available to provide specific details on the event should the Emperor inquire. How I built it The system is constructed using a robust, dual-tier architecture designed for both speed and creative depth: The Royal Brain (Backend): Built with FastAPI and LangGraph, it serves as the orchestration layer. I implemented a Supervisor-Worker pattern where specialized "Guards"(Nova Pro) use Langchain to handle intent analysis and real-time web searching via DuckDuckGo. The Royal Interface (Frontend): Developed with React and Vite, featuring a WebSocket integration for real-time, bidirectional communication between the Emperor and the Castle. I used Framer Motion to ensure the "Imperial" UI felt fluid and responsive. The Nova Orchestra (AI/ML): Powered by Amazon Bedrock, I leveraged Nova Pro for complex reasoning and transcription, while Nova Canvas and Nova Reel act as our "Grand Artists" to generate thematic images and videos. Imperial Logistics: Redis serves a dual purpose—handling the asynchronous task queue for the "Heavy Tier" processing and managing the Pub/Sub broadcasts that push updates to the UI. Infrastructure: The entire realm is containerized using Docker and Docker Compose, with a custom PowerShell manifest to automate the build and deployment process. Challenges I ran into Building a realm as complex as The Grand Castle came with its own set of "imperial" hurdles: Asynchronous Orchestration: Managing the transition between the Fast Tier (immediate feedback) and the Heavy Tier (media generation) was a significant challenge. I had to implement a robust Redis-based queue to ensure the UI remained responsive while the Nova Orchestra performed its complex tasks. Parallel Processing: Coordinating three concurrent LLM workers using asyncio.gather required precise state management. Ensuring that each worker stayed aligned with the Director’s execution blueprint without conflicting was a major technical puzzle. Real-time Synchronization: Keeping the React frontend in perfect sync with the Background Worker across distributed services required fine-tuning our WebSocket and Redis Pub/Sub logic to prevent "laggy" royal decrees. This challenge directly led to the creation of the Technical Ledger (Signal Dashboard) and Notice Board. These components were initially developed as debugging tools to track synchronization in real-time, but they proved so effective for monitoring the system's "pulse" that they became core features of the imperial interface. Prompt Engineering for Art: Directing Amazon Nova Canvas and Reel to produce consistent thematic styles—like the "Live Sketch" on parchment—required extensive iteration to ensure the visual output felt like a cohesive "Grand Art" performance rather than random generations. Accomplishments that I am proud of High-Efficiency Dual-Tier Architecture: Successfully implemented a non-blocking command flow that separates immediate "Fast Tier" intent analysis from "Heavy Tier" media generation, ensuring the user never has to wait for a query to complete. Seamless Voice-to-Visual Pipeline: Developed a fluid system where spoken "Imperial Decrees" are transcribed by Amazon Nova Pro and transformed into dynamic, themed visualizations via Nova Canvas and Reel. The Royal Archive Integration: Built a sophisticated session management system using Redis and PostgreSQL that allows the AI to synthesize multiple rapid-fire requests while maintaining full contextual awareness. Real-time Synchronization: Achieved sub-second updates between the Background Worker and React frontend using a robust WebSocket and Redis Pub/Sub implementation. Automated Imperial Deployment: Engineered a comprehensive PowerShell manifest that automates the entire multi-service build, containerization, and environment setup, making the complex architecture "one-click" deployable. What I learned Asynchronous Event Processing: Gained deep experience in managing distributed AI tasks using aioredis and Python's asyncio to prevent system blocking. Prompt Engineering for Media: Discovered how to consistently direct Amazon Nova Canvas to produce specific aesthetic styles. Precision Guardrails: Learned to navigate the 1024-character prompt limit for Nova Canvas, requiring the implementation of specific guardrails and concise prompting strategies to successfully invoke the model within its constraints. State Management in Multi-Agent Systems: Learned to coordinate multiple concurrent LLM workers by strictly adhering to a shared Director’s execution blueprint while leveraging LangGraph and Langchain for complex orchestration. Real-time Infrastructure: Learned the use of WebSockets and Redis Pub/Sub to bridge the gap between heavy background processing and a responsive React frontend. What's next for The Grand Caste - Nova orchestration Advanced Audio Cues: Implementing natively generated audio feedback to complement the visual storytelling. Enhanced Multi-Modal Interaction: Refining the Grand Canvas to allow for interactive editing of generated art through follow-up voice commands and the generation of Nova Reels. The Ultimate Goal — The AI Director: Evolving the system into an autonomous AI Director capable of not just executing commands, but implementing complex scripts born from its own synthesized "thoughts" and reasoning. Reducing Hallucination through Orchestration - I discovered that The Grand Castle’s architecture serves as a natural deterrent to AI hallucination. By forcing the system to listen, investigate, and organize findings within the Royal Archive before producing a final response, we can reduce the model's reliance on "predicting" the next word in a vacuum. Instead, the AI summarizes a verified body of results in a neat, structured way, ensuring that the output is grounded in the current topic's actual data rather than creative speculation. <div