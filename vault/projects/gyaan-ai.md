---
slug: "gyaan-ai"
url: "https://devpost.com/software/gyaan-ai"
title: "Gyaan AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 665
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/developer"
  - "user/educator_student"
  - "user/government_staff"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Gyaan AI

> Revolutionizing STEM learning via Gyaan AI—an AI tutor delivering root mastery through a 9-step method, interactive PhET simulations, immersive quizzes, and 20+ languages.

[Devpost](https://devpost.com/software/gyaan-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
  <sub>weak: realtime_stream</sub>
**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[developer]] [[educator_student]] [[government_staff]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** clerk, deepseek, deno, gemma, markdown, openrouter, phet, postgresql, react-18, supabase, tailwind-css, typescript, vercel, vite

## How they structured the write-up

- 🌟 inspiration
- 🚀 what it does
- 🧠 core innovation: the 9-step teaching method
- 🛠️ how i built it
- ⚡ challenges i faced
- 📈 what's next for gyaan ai

## Body

Gyaan AI Landing Page: A fully functional, production-ready AI STEM tutor tailored for global students on any mobile browser. Gyaan AI Settings: Instant language selection for a tailored UI, showcasing comprehensive support for over 25+ global languages. Gyaan AI Core Features: Highlighting the proprietary 9-step learning method, interactive quizzes, and multi-language support. Gyaan AI Dashboard: Tracking learning stats, active streaks, and saving bilingual chat history for a customized student experience. Gyaan AI Chat: Delivering structured STEM lessons natively via the 9-step method, starting from core root concepts instead of definitions. Gyaan AI Simulation: Interactive PhET labs embedded inline with AI quizzes to visualize STEM concepts without any external redirects. Gyaan AI Quiz: AI-generated interactive MCQs customized per lesson for real-time concept testing and immediate score review. Gyaan AI Analysis: Step 9 delivers targeted result analysis, instantly breaking down wrong quiz answers to fix core student misconceptions. 🌟 Inspiration Millions of students across developing nations in rural India, Africa, and Southeast Asia lack access to quality STEM education. Private tutors are often unaffordable, and traditional textbooks are frequently printed in foreign languages, creating a massive barrier to learning. I wanted to build a solution that is patient, structured, and completely free—leading to the creation of Gyaan AI , an AI-powered tutor that bridges this knowledge gap by speaking the student's local language natively. 🚀 What it does Gyaan AI is a fully deployed, production-ready web application acting as a personal AI tutor for Physics, Chemistry, Mathematics, and Biology. Students can interact via typing, voice input (STT), or by photographing textbook questions. The platform automatically detects the user's browser language and delivers a comprehensive, curriculum-aligned lesson instantly. It is optimized for mobile browsers, ensuring students can learn anywhere without requiring any software installation. 🧠 Core Innovation: The 9-Step Teaching Method Every topic is broken down into a structured, root-level learning workflow designed to build deep conceptual mastery rather than rote memorization: Foundation: Building the root concept from scratch. Why This?: Explaining the underlying logic and necessity of the concept. Deep Dive: Comprehensive explanation with all necessary formulas. Summary: A bullet-point recap for quick revision. Memory Trick: Lifetime shortcuts and mnemonics to ensure recall. Real Life: Connecting abstract concepts to daily observable phenomena. Simulation: Interactive PhET labs embedded directly for visualization. Quiz: 3 AI-generated MCQs to test understanding with instant feedback. Re-Teach: Automatic re-explanation if the student struggles, ensuring no concept is left unclear. 🛠️ How I built it The application is crafted with a highly scalable, modern, and cost-effective tech stack: Frontend: React 18 & Vite for a lightning-fast, responsive UI. Authentication: Clerk (JWT + OAuth) for secure, seamless user management. Database: Supabase (PostgreSQL) for handling student profiles, streak tracking, and chat histories. AI Engine: OpenRouter (free-tier) powering advanced models like Gemma 2 & DeepSeek R1. Backend: Edge Functions on Deno/TypeScript deployed globally via Vercel for low-latency performance. ⚡ Challenges I faced Building Gyaan AI as a solo developer came with significant hurdles: Mobile-Only Development: Building a full-stack, production-ready application entirely on a mobile phone was a massive hurdle. Managing local servers and debugging frontend layouts without desktop dev-tools pushed me to develop highly creative and efficient workflows. Markdown Rendering: Handling raw AI responses in React was complex. Converting markdown structures back to UI components required intensive debugging to fix rendering bugs and layout inconsistencies. Connectivity & Bandwidth: Serving underserved regions meant optimizing for unstable network conditions, which led me to implement efficient edge-caching and lightweight UI components. Zero-Cost Architecture: Achieving production-scale capability while stitching together completely free-tier resources (Vercel, Clerk, Supabase, OpenRouter) was a rewarding challenge in systems integration. 📈 What's next for Gyaan AI Phase 2 (Ads Revenue): Implementing non-intrusive, student-safe contextual ads to fund higher database and API limits. Phase 3 (Premium Tier): Introducing ad-free premium accounts with access to advanced AI models (GPT-4o/Claude) and bulk licensing for schools and NGOs. Phase 4 (Partnerships): Collaborating with state education boards, launching a WhatsApp/Telegram bot, and building an offline-first PWA for regions with zero-internet access. <div