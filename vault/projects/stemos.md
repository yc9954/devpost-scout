---
slug: "stemos"
url: "https://devpost.com/software/stemos"
title: "STEMOS"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 647
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# STEMOS

> STEMOS is an autonomous AI STEM learning platform with adaptive tutoring, personalized learning paths, and interactive simulations that simplify complex concepts for students.

[Devpost](https://devpost.com/software/stemos) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** framer-motion, groq, html5, llama-3.1, lucide-icons, node.js, postgresql, react, supabase, tailwind-css, tanstack-router, tanstack-start, typescript, vercel-serverless

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stemos

## Body

just look of my project Inspiration STEM subjects (Science, Technology, Engineering, and Mathematics) represent the foundations of human innovation, yet the traditional way of learning them is often dry, static, and isolating. Textbooks fail to convey the dynamic beauty of chemical reactions, physics forces, or mathematical functions, while students are forced to study in silos. We built STEMOS to change this. We envisioned a visual, highly collaborative, and gamified learning ecosystem—a "STEM Odyssey"—where students learn visually through interactive simulators and study together in real-time, backed by cutting-edge generative AI. What it does STEMOS is a comprehensive, production-ready STEM learning platform featuring: AI STEM Tutor: A highly contextual, personalized academic guide that adapts to individual student learning curves. Interactive STEM Lab: Visual, interactive physics, math, and chemistry simulators that make abstract formulas tangible. Dynamic AI Paths: On-demand dynamic roadmap compilation generating customized career and skill paths for students. Live Arena: A real-time multiplayer study hub. It features a buddy request sidebar, direct private chats, active AI chat moderation, and a dynamic AI MCQ Rapid Fire game. Every 60 seconds, the AI generates a unique, high-difficulty General Knowledge/STEM MCQ and spawns the panel at a randomized screen coordinate identically across all connected clients' viewports for collaborative lobby solving. Gamified Progression & Shop: Integrated milestone tracking via a visual dashboard, focus streaks, and a study-credit shop for custom avatar items. How we built it We engineered a high-fidelity, full-stack TypeScript application: Meta-Framework & Routing: Structured with TanStack Start and TanStack Router to achieve perfect type safety across all frontend and API routes. Real-time Synced Database: Powered by Supabase (PostgreSQL) , managing secure Auth, profile data, study streaks, and multiplayer synchronization. Generative AI Orchestration: Integrated with the Groq API (Llama-3.1) to generate dynamic study paths, moderate live chat rooms, and generate unique MCQ questions on-the-fly. Advanced UI & Micro-Animations: Designed with Tailwind CSS and Framer Motion to deliver a premium, glassmorphism visual layout that is fully mobile-responsive (featuring mobile navigation tab bars, collapsible sidebars, and adaptive viewport modals). Vercel Serverless Bridge: Built a custom Node.js request bridge to translate standard Node server calls to Web-standard Request/Response formats, ensuring zero-latency SSR on Vercel. Challenges we ran into Multiplayer Real-time Coordinates Sync: Emitting dynamic random positions for the MCQ popup so that all online users see the exact same card in the exact same spot without causing React hydration mismatches on page load. We solved this by using client-side hydration hooks paired with stateful Supabase Presence and Broadcast channels. Serverless SSR Bridging on Vercel: Deploying TanStack Start within standard serverless environments rather than strict edge containers due to complex dependencies. We designed a custom Web-API request bridge to adapt the server bundle to standard nodejs runtime targets. Build-Time Secret Injection: Handling Vite's static word-level string replacements of client-side environment variables securely without exposing them in Git repositories. We automated a workflow using customized .env.production.local variables kept safely out of version tracking. Accomplishments that we're proud of Designing and implementing a fully-moderated, real-time multiplayer study arena with active buddy-list management in under a week. Creating a highly visual simulation Lab that translates complex abstract science into satisfying, interactive components. Achieving a highly optimized, responsive CSS architecture that feels like a native mobile app on iPhones/Androids and stands out on wide desktop monitors. What we learned Real-time multiplayer synchronization combined with client-side state prediction yields highly responsive, zero-latency user experiences. Integrating strict full-stack type safety with TanStack and TypeScript saves hours of production debugging and makes compiling highly reliable. What's next for STEMOS Collaborative Boss Raids: Multiplayer RPG-style bosses (e.g., a "Calculus Dragon" or "Entropy Monster") that the lobby must defeat collaboratively by solving advanced STEM challenges. Hands-free Voice Mode: Integration of real-time browser Speech-to-Text and Text-to-Speech APIs so students can speak to their AI Tutor naturally. Procedural focus gardens: Growing fractal-based geometric trees that grow branch-by-branch in real-time as focus study timers run. <div