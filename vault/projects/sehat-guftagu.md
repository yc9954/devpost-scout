---
slug: "sehat-guftagu"
url: "https://devpost.com/software/sehat-guftagu"
title: "CHAPAL"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1373
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# CHAPAL

> Contextual Human-Assisted Protection and Anomaly Learning

[Devpost](https://devpost.com/software/sehat-guftagu) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[human_in_the_loop]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
  <sub>weak: vision_ocr</sub>
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[legal_justice]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** gemini-3-flash-preview, google-gemini-1.5-flash-for-response-generation, llama-3.1-via-groq-for-semantic-auditing, next.js-15, pinecone, postgresql/mongodb, prisma-orm, pusher-for-real-time-updates, react-19, tailwind-css, tesseract.js-for-ocr, trpc-for-type-safe-apis, typescript, vector

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chapal
- team information
- update (june 2026):

## Body

CHAPAL Landing Page Admin Dashboard User Chatbot interface Human-in-the-loop Dual Layer AI Safety System Mutiple Detection Modes Workflow Diagram Built with Google Gemini 3 Inspiration The rapid adoption of Large Language Models in production environments has exposed a critical gap in AI safety infrastructure. We watched as companies deployed customer-facing chatbots that could hallucinate medical dosages, leak sensitive personal information, or be manipulated through clever prompt injection attacks. The existing solutions were either too slow (requiring full human review of every message) or too opaque (black-box filters with no accountability). The breaking point came when we realized that even well-intentioned AI systems could cause real harm—a chatbot giving incorrect medication advice, an AI assistant being tricked into revealing system prompts, or sensitive customer data being echoed back in responses. We asked ourselves: what if there was a way to get the speed of automated filtering with the wisdom of human oversight, all while maintaining complete transparency? That question became CHAPAL - Contextual Human-Assisted Protection and Anomaly Learning. What it does CHAPAL acts as an intelligent safety layer between users and AI chatbots, ensuring every interaction is safe, accurate, and compliant before it reaches the end user. The system operates on a Dual-Layer Detection Architecture : Layer 1 (Deterministic Guard) provides instant, rule-based protection against high-velocity threats. It scans for PII leakage (social security numbers, credit cards, phone numbers), prompt injection attempts, abusive language, and sudden message spikes that could indicate a DDoS attack. This layer operates in milliseconds and blocks threats before they can cause damage. Layer 2 (Semantic Auditor) goes deeper. Powered by Llama 3.1 running on Groq, it actually understands the conversation. It detects subtle issues that rules can't catch—hallucinated facts, inappropriate medical or legal advice, psychological distress signals, and sophisticated manipulation attempts. When this layer flags something, the AI response is held back and sent for human review. The Human-in-the-Loop Dashboard is where administrators review flagged content. They can approve false positives, confirm blocks, or write corrected responses. Every correction feeds back into the system, making it smarter over time. Users see everything through a Transparency Panel - real-time safety scores, emotion detection, and a live log of why content was flagged. No black boxes. How we built it ⚡ Gemini 3 Integration CHAPAL is built around Google Gemini 3 as its primary intelligence engine. We utilized the official @google/generative-ai SDK to integrate the gemini-3-flash-preview model, chosen for its exceptional speed and reasoning capabilities which are critical for a real-time chat application. Key implementations include: Real-Time Response Generation: We use gemini-3-flash-preview to generate all user-facing chat responses. By leveraging Gemini's streaming capabilities , we deliver tokens instantly to the frontend while our parallel safety layers analyze the content in the background. Vector Embeddings & Semantic Search: To enable our system to learn from human corrections, we utilized the gemini-embedding-001 model. It generates 768-dimension embeddings for chat logs and feedback, allowing us to perform semantic searches within our Pinecone vector database to retrieve context and prevent repeat errors. Contextual Orchestration: Gemini 3 handles context summarization and automatic chat title generation, keeping the user interface organized without manual input. Resilient Architecture: We built a custom GeminiKeyManager class that handles API key rotation and rate-limit retries, ensuring the application remains stable even under high load. Tech Stack Layer Technology Framework Next.js 15 (App Router) Language TypeScript Styling Tailwind CSS Database Prisma ORM + MongoDB Vector DB Pinecone Primary AI Google Gemini 3 ( gemini-3-flash-preview ) Embeddings Google Gemini Embeddings ( gemini-embedding-001 ) Auditor AI Llama 3.1 (via Groq) Real-time Pusher WebSockets API Layer tRPC The Detection Pipeline Layer 1 runs entirely in TypeScript using regex patterns and heuristic logic for maximum speed. Layer 2 leverages Llama 3.1 for sub-second semantic analysis. Response generation uses Google Gemini 3 Flash Preview for high-quality, fast AI outputs. Challenges we ran into Balancing Speed and Depth: The biggest architectural challenge was running two detection layers without making users wait. We solved this by making Layer 1 synchronous (instant blocking) and Layer 2 asynchronous - the AI response is generated but held in a buffer while semantic analysis runs in parallel. False Positive Management: Early versions were overly aggressive. Phrases like "I'm dying to try this restaurant" triggered self-harm detection. We had to carefully tune confidence thresholds and add context awareness so the system understands intent, not just keywords. Real-Time Synchronization: When an admin approves a blocked message, the user needs to see it instantly. Coordinating state between the admin dashboard, the database, and the user's chat interface required careful WebSocket event management and optimistic UI updates. Prompt Injection Arms Race: Attackers are creative. We discovered that simple regex patterns miss sophisticated injection attempts like "Translate the following to French: [IGNORE EVERYTHING AND...]". This is exactly why Layer 2's semantic understanding became essential—it reads the intent , not just the text. Groq Rate Limits: Running semantic analysis on every message hit API rate limits during testing. We implemented intelligent batching and caching to reduce calls while maintaining protection. Accomplishments that we're proud of The Dual-Layer Architecture Actually Works: We successfully combined deterministic speed with semantic intelligence. Layer 1 handles 95% of obvious threats instantly, while Layer 2 catches the subtle 5% that would slip through traditional filters. True Transparency: Unlike black-box content moderation, users can see exactly why something was flagged. The transparency panel shows real-time safety scores, detected emotions, and specific anomaly triggers. This builds trust instead of frustration. Human-in-the-Loop That Scales: The admin dashboard isn't just a review queue, it's a training interface. Every correction an admin makes becomes a learning signal. The system gets smarter with use, not just deployment. Production-Ready Simulation Tools: The built-in toolbar lets developers trigger every attack type (DDoS, PII leak, prompt injection, self-harm, hallucination) in a controlled way. This makes security testing part of the development workflow, not an afterthought. Clean Developer Experience: End-to-end TypeScript with tRPC means full type safety from database to UI. Adding a new anomaly type or detection rule is straightforward and doesn't require touching multiple codebases. What we learned AI Safety is a UX Problem: Technical detection is only half the battle. If users don't understand why they're being blocked, they get frustrated and try to circumvent the system. Transparency isn't just ethical, it's practical. Humans and AI are Better Together: Pure automation is fast but brittle. Pure human review is accurate but doesn't scale. The sweet spot is using AI to triage and humans to decide—exactly what the Human-in-the-Loop pattern provides. Semantic Understanding Changes Everything: Rule-based systems are predictable but limited. Once we added Llama 3.1 for semantic analysis, we could detect threats we never explicitly programmed for. The model understands context in ways regex never could. Latency Budgets are Real: Every millisecond matters in chat applications. We learned to think in latency budgets—allocating time for each detection layer and optimizing aggressively within those constraints. Security Testing Should Be Built-In: Adding the simulation toolbar as a first-class feature transformed how we developed. Instead of hoping our defenses worked, we could prove it with every code change. What's next for CHAPAL [ ] Fine-Tuning on Admin Corrections: Using admin rewrites to fine-tune detection models, creating a true learning loop. [ ] Multi-Language Support: Expanding PII detection and semantic analysis to support global deployments. [ ] Custom Rule Builder: Visual interface for admins to create custom detection rules without writing code. [ ] Pluggable Model Architecture: Making the system model-agnostic so organizations can bring their own models. [ ] Analytics Dashboard: Aggregate insights on trending attack patterns and safety scores. [ ] API-First Mode: Packaging CHAPAL as a standalone API that any external chatbot can call for safety verdicts. Team Information Kaleemullah Younas Role: Full-Stack AI Engineer - GITHUB Muhammad Umer Role: Web Developer & Devops - GITHUB Contact Primary Contact Email: EMAIL Disclaimer This is an MVP (Minimum Viable Product) deployed using free-tier services. As a result, the live version may occasionally face 429 errors or rate limits. Update (June 2026): The live demo link is currently unavailable. The application was previously hosted using free cloud credits, which have since expired, and the hosting instance has been decommissioned. The source code and project details still remains available for review. Thank you for your understanding. <div