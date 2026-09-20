---
slug: "planix-ai-the-learning-operating-system-xgtd1f"
url: "https://devpost.com/software/planix-ai-the-learning-operating-system-xgtd1f"
title: "Planix AI — The Learning Operating System"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 628
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Planix AI — The Learning Operating System

> Planix AI turns learning goals into structured execution plans. Enter a skill and available time, and the AI generates a phase-based roadmap with milestones and progress tracking.

[Devpost](https://devpost.com/software/planix-ai-the-learning-operating-system-xgtd1f) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** framermotion, googlegeminiapi, next.js, postgresql, prisma, react, supabase, tailwindcss, typescript, vercel

## How they structured the write-up

- 💡 inspiration
- 🎯 what it does
- 🛠 how we built it
- 🏔 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for planix ai — the learning operating system

## Body

Planix AI — The Learning Operating System 💡 Inspiration We are not lacking information. We are drowning in it. Students save courses they never finish. Professionals bookmark tutorials they never execute. AI tools answer questions instantly — yet real growth remains inconsistent. The problem is not knowledge access. The problem is lack of structured execution . Most learning journeys fail because people don't know: where to start what to learn next how to structure progress how to stay consistent Modern AI tools respond to prompts, but they rarely design learning progression . Planix AI was built to change that. Instead of simply answering questions, it acts as an AI-powered learning architect , transforming goals into structured execution systems. Growth should be engineered — not improvised. 🎯 What it does Planix AI converts a learning goal into a structured roadmap. A user defines: what they want to learn how many days they want to study how many hours they can dedicate daily Planix AI then generates a phase-based learning architecture including: logically sequenced phases time-calibrated milestones structured competency progression estimated effort per task Once a roadmap is generated, users can: explore roadmap phases ask AI to explain concepts generate structured learning notes refine the roadmap dynamically Unlike traditional chat-based tools, Planix operates on roadmap context , not isolated prompts. It designs the path before answering. 🛠 How we built it Planix AI is built as a modern full-stack AI application. Frontend Next.js 15 TypeScript Tailwind CSS Framer Motion for UI transitions Backend Next.js API routes Prisma ORM PostgreSQL (Supabase) AI Layer Google Gemini API Structured prompt engineering Deterministic roadmap formatting The AI generates structured JSON outputs which are then rendered into roadmap components inside the UI. This architecture separates the system into: UI Layer AI Reasoning Layer Persistence Layer This modular structure makes the platform scalable and extensible. 🏔 Challenges we ran into Structured AI Output Large language models naturally produce long text responses. However, Planix requires structured roadmap architecture . We solved this using strict prompt constraints and normalization logic that forces the AI to generate consistent phase and milestone structures. Adaptive Time Calibration Learning goals vary widely in complexity. Balancing the user's available time with realistic roadmap planning required designing logic that dynamically adjusts milestone density. Context-Aware AI Interaction Standard chat systems operate on isolated prompts. Planix needed persistent roadmap context so users could refine and explore learning paths without losing structure. This required building roadmap-aware AI interaction layers. 🏆 Accomplishments that we're proud of We are proud that Planix AI moves beyond the traditional chatbot paradigm. Instead of simply generating answers, it generates structured systems for learning progression . Key accomplishments include: designing an AI-powered roadmap architecture system building a full-stack AI learning platform implementing structured AI outputs instead of free text responses creating a user interface that visualizes learning progression clearly Planix demonstrates how AI can move from information generation to system design . 📚 What we learned Building Planix AI taught us that the real power of AI is unlocked when it produces structured outputs instead of raw text . We learned how prompt engineering can transform a language model into a planning engine rather than a conversational assistant. We also gained experience designing AI systems where the model becomes a core architectural component rather than an optional feature. 🔮 What's next for Planix AI — The Learning Operating System Our long-term vision is to turn Planix into a complete growth infrastructure platform . Future directions include: AI-powered progress analytics adaptive roadmap recalibration based on learning speed community-shared learning architectures collaborative learning systems skill verification and feedback loops mobile platform support The goal is a world where no learner ever asks: “Where do I start?” Instead, AI responds: “Here is your structured system.” <div