---
slug: "neuroflow-ai-m4h6pi"
url: "https://devpost.com/software/neuroflow-ai-m4h6pi"
title: "NeuroFlow AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 886
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# NeuroFlow AI

> NeuroFlow AI: A unified, AI-powered study space. Adapts to your learning with spaced repetition flashcards, custom quizzes, note analysis, and physics-based knowledge graphs.

[Devpost](https://devpost.com/software/neuroflow-ai-m4h6pi) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[labor_employment]] [[mental_health]]
**user** [[educator_student]] [[general_public]] [[legal_professional]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** css3, git, google-fonts, html5, javascript, localstorage, lucide-react, react, react-router, recharts, vite

## How they structured the write-up

- 💡 inspiration
- ⚡ what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 💡 what we learned
- 🚀 what's next for neuroflow ai

## Body

🧠 NeuroFlow AI — Your Adaptive Cognitive Study Sanctuary ⚡ 💡 Inspiration 🤯 The Problem: Modern students are suffering from cognitive overload and digital burnout. They are forced to juggle 5+ fragmented apps daily—using Notion for notes, Anki for flashcards, Forest for timers, Discord for study groups, and ChatGPT for explanations. This constant context-switching destroys focus, halts deep work, and decimates memory retention. 🎯 The Spark: We wanted to build a single, deeply integrated, and visually stunning digital sanctuary. By combining the mathematics of cognitive science ( SuperMemo SM-2 Spaced Repetition ) with advanced interactive AI helpers and premium gaming mechanics, we engineered NeuroFlow AI —a unified, gorgeous learning workspace that adapts to your brain in real-time. ⚡ What It Does NeuroFlow AI is a unified, gamified, and AI-powered study universe that helps students study smarter, not harder . It integrates 35+ high-fidelity features into one breathtaking platform: 🤖 AI Study Blueprint Generator: Instantly curates hyper-customized, day-by-day learning roadmaps based on your upcoming exams, subjects, and study goals. 🧠 SM-2 Spaced Repetition Engine: A native implementation of the gold-standard memory algorithm that schedules flashcards precisely at the point of forgetting. Includes an AI Flashcard Generator to turn notes into study decks in 1 click! 📝 Cognitive Note-Taking: Color-coded rich notes with instant AI summarization, nested tag filters, quick search, and pinning mechanics. 📐 AI Quiz Engine: Generates target-specific assessments on the fly with comprehensive, readable explanations for every single option, plotting your progress on dynamic radar graphs. 🕸️ Physics-Powered Knowledge Graph: An interactive, canvas-driven 2D force-directed physics simulation that automatically maps out visual webs of concepts and memory nodes. 📊 Ultimate Analytics Suite: Track your progress with 8 rich data visualizations, including GitHub-style 12-week study heatmaps, subject distribution charts, Recharts progress trends, and a custom AI Exam Readiness Score . 🎮 High-Engagement Gamification: Earn XP for every action, level up, maintain study streaks with gorgeous flame animations, complete daily challenges, and unlock 20 custom achievement badges! ⏱️ Smart Pomodoro Suite: An animated SVG focus ring timer with study, short break, and long break modes linked to your custom subject catalog. 🛠️ How We Built It We custom-engineered NeuroFlow AI from scratch to deliver a seamless, high-performance web experience: 🚀 Core Tech Stack: Architected as a super-fast SPA utilizing Vite 5 and React 18 for lightning-fast compilation and load times. ⚡ Global State: Powered by a centralized React Context + useReducer action architecture, seamlessly syncing XP, streaks, levels, and study metrics across 11 fully functional views. 🎨 Premium Design System: Styled completely with Vanilla CSS featuring a futuristic, glassmorphic dark theme ( #0a0a1a ), glowing neon gradients (electric purple, cyan, emerald), Space Grotesk/Inter typography, and 15+ custom-crafted CSS keyframe animations. 💻 Physics Engine: Coded a custom force-directed physics solver directly onto HTML5 Canvas to handle high-frequency particle attraction, repulsion, friction, and node-dragging. 🧬 Native Math: Avoided heavy external dependencies by writing a pure JavaScript implementation of the SM-2 Spaced Repetition algorithm. 💾 Persistent Data Layer: Abstracted a complete localStorage system with automated state hydration and data export support. 🚧 Challenges We Ran Into 🔄 Bridging React State & Physics Canvas: High-frequency rendering loops (for the Knowledge Graph physics) easily stutter under standard React render lifecycles. We bypassed this by utilizing useRef hooks and a native requestAnimationFrame canvas rendering loop to keep animations silky smooth. 📦 Strict Build Optimization: We ran into early package compilation warnings. We carefully audited our dependencies, pinning Vite 5 , React Router v6 , and Recharts 2 to guarantee a perfect production build with zero warnings or errors. 🧠 Robust AI Demoware Logic: For a stunning, zero-setup judge experience, we avoided expensive API rate-limits and credential setups. We created structured heuristic pattern matchers and templates that simulate highly interactive, context-aware AI outputs (chatbot, summaries, planners) right in the client! 🏆 Accomplishments That We're Proud Of 💎 Breathtaking UI/UX Design: The aesthetic represents a premium, consumer-ready application. The glassmorphic cards, dynamic neon accents, floating glow states, and micro-interactions create an immediate "Wow" factor. 📈 Stunning Visual Density: Packaging 8 separate data visualizations (including a beautiful study heatmap and radar graphs) into a readable, high-impact layout. 🚀 Optimized Performance: The entire app compiles in just 3.69 seconds with a bundle weight optimized for instantaneous load times. 🧩 Zero-Dependency Implementations: Proud of coding our own custom 2D canvas physics simulation and SM-2 spaced repetition logic from first principles. 💡 What We Learned 🧠 The Mathematics of Memory: Dive deep into cognitive psychology, understanding how the Easiness Factor ($E$-Factor) and interval intervals affect long-term retention. ⚙️ High-Performance Canvas Rendering: Learned how to cleanly couple React’s declarative component UI with raw, high-performance imperative Canvas drawing logic. 🏗️ State Scaling: Best practices for structuring scalable frontend architectures with unified context layers. 🚀 What's Next for NeuroFlow AI 🌐 Live LLM Integration: Connect the heuristic AI module to active OpenAI/Gemini APIs for fully dynamic, real-time context-aware tutor responses. ☁️ Cloud Sync & Supabase Backend: Introduce a Postgres database for real-time multiplayer study lobbies, shared study decks, and global class leaderboards. 📲 Progressive Web App (PWA) & Mobile: Package NeuroFlow AI with service workers for full offline accessibility, paving the way for a React Native mobile application. 🎓 LMS Integrations: Integrate with tools like Canvas or Google Classroom so students can pull their university course syllabi directly into NeuroFlow AI. <div