---
slug: "prepx-y4kfst"
url: "https://devpost.com/software/prepx-y4kfst"
title: "PrepX"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 857
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PrepX

> PrepX - The Smartest Way to Land Dream Job

[Devpost](https://devpost.com/software/prepx-y4kfst) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** express.js, fastapi, gcp, gemini, groq, hocuspocus, langchain, langgraph, python, react, typescript, yjs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for prepx

## Body

Inspiration NOTE :- https://prezi.com/view/8Bu63E9F3r1ORuqk1BR3/?referral_token=QjXOnUlnB3FN This is a presentation for this project. Please read this more info The Challenge Faced by Tech Job Seekers While preparing for technical careers, we observed that students and developers often struggle not because of lack of talent, but because career preparation tools are fragmented and inefficient. Candidates typically rely on multiple disconnected platforms for: learning new skills practicing coding problems preparing for interviews discovering job opportunities This scattered approach makes career preparation confusing, time-consuming, and inefficient. With the rapid advancement of Large Language Models, real-time AI agents, and intelligent automation, we saw an opportunity to build a system that could act as a personal AI career co-pilot. We were inspired to create PrepX, a platform that integrates learning, interview preparation, career guidance, and job discovery into a single intelligent ecosystem powered by AI. What it does AI-Powered Interview Practice PrepX allows users to simulate real-time technical and behavioral interviews with an AI interviewer. Users receive performance analytics, skill assessments, and feedback to improve their interview readiness. Real-Time AI Learning Assistant The platform provides an interactive AI tutor with voice and video capabilities, helping users understand concepts, review code, and learn through real-time guidance. Intelligent Job Discovery PrepX analyzes a user’s resume and automatically matches them with relevant job opportunities, highlighting skill gaps and providing insights into market demand. Personalized AI Course Generation Users can generate custom learning courses tailored to their goals, including articles, flashcards, quizzes, and visual mind maps for structured learning. Career Path Simulation PrepX uses multi-agent AI workflows to simulate potential career paths, providing users with skill roadmaps, timeline projections, and salary insights. How we built it Architecture Overview We built PrepX as a three-tier microservices architecture: Frontend: React + TypeScript + Vite with Lexical editor Collaboration Server: Express.js + Hocuspocus + Yjs + MongoDB + Redis AI Engine: FastAPI + LangGraph + LangChain + ChromaDB AI Orchestration We used LangGraph to coordinate multiple AI agents (Planner, Explainer, Tester) that work together to generate complete courses. The Planner creates the knowledge graph structure, the Explainer generates content for each node, and the Tester creates assessments - all orchestrated in a stateful workflow. Real-Time Collaboration We implemented Yjs CRDT technology through Hocuspocus to enable real-time document editing. MongoDB serves as the persistence layer while Redis handles real-time synchronization between clients, ensuring conflict-free collaborative editing. Content Generation Pipeline Our system processes user input through multiple stages: topic analysis → knowledge graph creation → content generation → multimedia integration → assessment creation. Each stage feeds into the next, creating a cohesive learning experience. Progressive Loading To handle long AI processing times, we implemented a progressive loading system that saves generated chapters to MongoDB as they're completed, allowing users to start learning before the full course is ready. Challenges we ran into Building live AI interactions for interviews and tutoring required very low latency. Managing real-time audio/video streaming alongside LLM inference was challenging and required optimizing model calls and using fast inference providers. Ensuring accurate responses from LLMs was difficult, especially in document Q&A and career advice. We addressed this by implementing Retrieval-Augmented Generation (RAG) and structured prompts to ground responses in verified context. Designing LangGraph-based multi-agent pipelines for career simulation and job discovery required careful orchestration of agent roles, data flow, and validation between stages. Job listings came from different APIs and ATS platforms with inconsistent formats. We built a normalization and scoring pipeline to clean, deduplicate, and match jobs with user profiles. Integrating React, Node.js, FastAPI, vector databases, and real-time AI agents required careful system design to ensure scalability, maintainability, and smooth communication between services. Accomplishments that we're proud of Built a low-latency real-time AI interaction system using LiveKit WebRTC that enables users to practice interviews and learn with a voice-enabled AI tutor and 3D avatar — a technically challenging integration of streaming, AI inference, and user interaction. -Designed complex multi-agent workflows using LangGraph to simulate career paths, analyze skill gaps, and generate market insights, enabling AI to perform structured reasoning instead of simple text generation. Developed an 8-agent job discovery system that aggregates listings from multiple ATS platforms, normalizes data, and scores opportunities against a user's resume — turning scattered job data into personalized career insights. Implemented dynamic course generation using LLMs, producing structured learning content including articles, flashcards, quizzes, and mind maps tailored to the user's learning goals. Built Retrieval-Augmented Generation pipelines with ChromaDB, allowing users to interact with PDFs and documents while ensuring responses are grounded in retrieved context to reduce hallucinations. What we learned Through building PrepX, we gained expertise in: Real-time AI systems using LiveKit WebRTC for low-latency voice and video AI interactions Advanced AI orchestration using LangGraph and multi-agent systems Microservices architecture with proper inter-service communication Retrieval-Augmented Generation (RAG) pipelines using ChromaDB and Gemini embeddings for grounded document-based AI responses Performance optimization for AI-heavy workloads Modern React development with complex state management What's next for PrepX We plan to enhance AI personalization through advanced learning analytics and expand our multilingual support to reach underserved communities globally. Additionally, we're developing mobile applications and AR/VR integration to create immersive learning experiences that transcend traditional educational boundaries. <div