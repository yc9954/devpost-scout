---
slug: "tutorgetter-ai"
url: "https://devpost.com/software/tutorgetter-ai"
title: "TutorGetter AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 387
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# TutorGetter AI

> High-integrity hiring at scale. TutorGetter AI uses video-proctored assessments to rank candidates on technical depth and communication skills through real-time AI analysis.

[Devpost](https://devpost.com/software/tutorgetter-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]]
**domain** [[labor_employment]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: sensor_telemetry</sub>

**stack** ai-template-engine, bcryptjs, mediastream-api, next.js-15, prisma, sqlite, tailwind-css-v4, typescript

## How they structured the write-up

- 💡 inspiration
- 🚀 what it does
- 🛠️ how we built it
- 🧠 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📖 what we learned
- 🔮 what's next for tutorgetter ai

## Body

Unified Admin Dashboard featuring a real-time candidate leaderboard, hiring pipeline tracking, and key technical performance metrics. A proctored, distraction-free environment for candidates with dynamic technical challenges and integrated video monitoring. Deep AI analysis reports breaking down candidate skills into Logic, Communication, Speed, and Code Quality for better hiring. 💡 Inspiration The remote hiring landscape is broken. Between "ghost" candidates and the rising ease of cheating in technical assessments, companies are struggling to verify true talent. We built TutorGetter AI to restore integrity to recruitment by combining the power of AI with immutable proctoring data. 🚀 What it does TutorGetter AI is a dual-portal recruitment engine: For Candidates : A high-stakes, video-proctored assessment environment that dynamically generates technical questions tailored to specific roles (Python, React, JS, etc.). For Admins : A comprehensive dashboard that provides an AI-driven behavioral analysis of every candidate, grading them on technical depth, communication, and teaching ability. 🛠️ How we built it We leveraged Next.js 15 (Turbopack) for a lightning-fast experience across two integrated portals. We used Prisma with a shared SQLite database to maintain real-time state. The core innovation is our Dynamic Template Engine , which ensures no two assessments are the same, preventing "leaked" questions. 🧠 Challenges we ran into One of the biggest hurdles was managing high-quality video proctoring streams and ensuring they were securely saved before submission. We refactored our submission logic to be fully asynchronous, guaranteeing that proctoring data is preserved even on slower networks. Additionally, migrating to Tailwind CSS v4 required a deep dive into the new build engine to maintain our premium "Glassmorphism" aesthetic. 🏆 Accomplishments that we're proud of End-to-End Integrity : A fully functional video recording and playback system for recruiters. Premium UX : A "Cosmic" dark-mode interface that feels like a top-tier SaaS product. AI Ranking : A real-time leaderboard that actually helps recruiters make decisions based on multi-dimensional data, not just a single score. 📖 What we learned Building this taught us the power of Next.js Route Handlers for simplifying complex backends. We also deepened our expertise in technical behavioral analysis—learning how to translate code quality and communication into actionable hiring data. 🔮 What's next for TutorGetter AI We plan to integrate real-time AI monitoring during assessments to flag suspicious behavior instantly and add collaborative live coding for the final interview phase. <div