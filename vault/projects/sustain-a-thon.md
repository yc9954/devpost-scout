---
slug: "sustain-a-thon"
url: "https://devpost.com/software/sustain-a-thon"
title: "Sustain-a-thon"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1132
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/immigration_refugee"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Sustain-a-thon

> Sustain-a-thon gamifies saving the planet. Track real-time impact, earn XP & badges, and get AI coaching. It’s a movement to prove fixing the future is fun, social, and addictive.

[Devpost](https://devpost.com/software/sustain-a-thon) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
  <sub>weak: cross_origin_web</sub>
**domain** [[climate_energy]] [[developer_tools]] [[education]] [[immigration_refugee]] [[mental_health]] [[security_privacy]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[web_dom]]

**stack** autoprefixer, browser-apis, client-side, css3-variables, custom-react-context, dom-api, esbuild, git, github, google-gemini-api, gpu-acceleration, html5, json, localstorage-api

## How they structured the write-up

- inspiration
- 🚀 what sustain-a-thon does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sustain-a-thon

## Body

Inspiration In a world grappling with the "climate crisis," a parallel epidemic has emerged: Eco-Anxiety . Millions of people feel paralyzed by the sheer magnitude of the problem, leading to inaction and despair. We realized that the traditional narrative—fear, guilt, and austerity—was failing to motivate the digital generation. We asked ourselves: What if saving the planet felt less like a chore and more like a massive multiplayer online game (MMO)? 🚀 What Sustain-a-thon Does Sustain-a-thon is not just a sustainability tracker—it is a behavioral transformation engine designed to rewire how individuals interact with climate action through gamification, AI, and real-time feedback systems. At its core, Sustain-a-thon converts abstract, overwhelming environmental problems into structured, actionable, and rewarding micro-interactions , enabling users to seamlessly integrate sustainability into their daily lives without cognitive overload. 🧠 1. AI-Powered Behavioral Coaching Engine (EcoBot) Sustain-a-thon deploys EcoBot , a context-aware AI system powered by advanced LLM architecture (Gemini/OpenRouter), functioning as a real-time behavioral coach rather than a passive chatbot. Dynamically ingests user-specific telemetry : XP progression curves Habit streaks Action frequency & consistency Badge unlock history Applies adaptive prompt injection pipelines to generate: Personalized nudges based on behavioral psychology Positive reinforcement loops to combat eco-anxiety Contextual goal-setting aligned with user capability 👉 The system effectively acts as a closed feedback loop , continuously optimizing user motivation and engagement through reinforcement learning-inspired interaction patterns. 📊 2. Real-Time Impact Quantification & Visualization Layer Sustain-a-thon bridges the gap between invisible environmental impact and user perception by transforming raw sustainability metrics into intuitive, visual, and emotionally engaging insights . Converts abstract data (CO₂ savings, water conservation, energy reduction) into: Interactive SVG-based visual dashboards Comparative analogies (e.g., “You saved energy equal to powering X homes”) Progressive impact milestones Implements reactive data-binding pipelines : Updates visualizations instantly upon user actions Maintains temporal tracking (daily, weekly, lifetime impact) 👉 This creates a tangible sense of contribution , eliminating the psychological disconnect that often leads to inaction. 🎮 3. Advanced Gamification & Progression System Sustain-a-thon incorporates a multi-layered gamification engine inspired by MMORPG progression systems to drive long-term engagement and habit formation. Core Mechanics: XP accumulation tied to real-world sustainable actions Non-linear leveling curves to maintain challenge-reward balance Tiered badge systems (e.g., milestone-based, consistency-based, impact-based) Behavioral Design: Dopamine-trigger loops via instant feedback (animations, rewards) Streak reinforcement mechanics to build habit persistence Unlockable achievements that act as status symbols within the ecosystem 👉 The platform transforms sustainability from a moral obligation into a competitive and rewarding experience loop . 📚 4. Adaptive Micro-Learning System To address the knowledge gap in climate literacy, Sustain-a-thon integrates a context-aware micro-learning engine . Breaks down complex domains such as: Climate systems (Greenhouse Effect, Ocean Acidification) Renewable infrastructure (Grid Storage, Carbon Capture) Uses: Bite-sized interactive modules Scenario-based learning flows AI-assisted simplification without loss of scientific accuracy Dynamically adapts content based on: User knowledge level Engagement patterns Learning progress 👉 This ensures users are not just acting sustainably—but understanding why their actions matter , increasing long-term retention. 🔁 5. Habit Formation & Behavioral Feedback Loop Sustain-a-thon is engineered around habit loop theory (cue → action → reward) : Cue: AI-driven reminders and contextual prompts Action: Logging sustainable activities (manual or automated in future) Reward: XP, badges, visual impact feedback This loop is reinforced through: Real-time UI feedback (<16ms interactions) Streak tracking and loss aversion mechanics Progressive goal systems 👉 The result is a self-sustaining behavioral system that gradually shifts users from awareness → action → identity. 🌐 6. Scalable Ecosystem Vision (Beyond MVP) The platform is designed as a foundation for a global sustainability network , with extensibility toward: Social leaderboards and cooperative challenges Community-driven impact missions Smart device & IoT integrations for passive tracking API integrations with carbon tracking and energy platforms 👉 Sustain-a-thon evolves from a personal tool into a collective climate action infrastructure . How we built it We architected Sustain-a-thon as a high-performance Single Page Application (SPA), leveraging the bleeding edge of the modern web ecosystem: Core Architecture: Built on React 19 and Vite , utilizing a modular component-based architecture. We employed TypeScript for strict type safety across our data models ( UserStats , ActionLogs ), ensuring a robust and maintainable codebase. Generative AI Integration: We engineered a seamless integration with Open Router open source mmodel . By implementing dynamic prompt injection , we feed real-time application state—user level, recent activities, and unlocked achievements—into the system context. This allows the LLM to generate responses that are not just accurate, but contextually aware and emotionally resonant. Data Visualization: We integrated Recharts to render responsive, SVG-based data visualizations. The charts are data-bound to our state management system, updating reactively as users log new actions. Persistence Layer: To ensure a frictionless user experience (UX) without the latency of server-side roundtrips for the MVP, we implemented an optimized localStorage persistence layer . This uses custom hooks to synchronize state changes instantly, providing offline-first capabilities. Design System: We bypassed generic UI libraries to build a custom Neo-Brutalist design system using Tailwind CSS . This involves high-contrast borders, hard-edged shadows ( box-shadow ), and tailored CSS transitions ( transform-gpu ) to ensure 60fps animations even on lower-end devices. Challenges we ran into Prompt Engineering vs. Hallucination: Balancing the AI's "youthful, optimistic" persona while ensuring scientific accuracy was difficult. We iterated through multiple system instruction sets to strictly bound the AI's creativity within the realm of factual climate science. State Synchronization: Managing the complex state dependencies between the gamification engine (XP calculations, Badge unlocking logic) and the persistence layer required careful handling of React's useEffect dependency arrays to avoid infinite render loops. Visual Consistency: Implementing the Neo-Brutalist aesthetic required precise control over CSS borders and layout shifts, challenging standard responsive design patterns. Accomplishments that we're proud of The "EcoBot" Personality: We successfully tuned the LLM to avoid "cringe" slang while remaining genuinely engaging and supportive. Zero-Latency Interactions: The app feels instantaneous. Action logging, level-ups, and page transitions happen in <16ms thanks to our aggressive client-side optimizations. Educational Depth: We didn't just make a tracker; we built an educational tool that simplifies complex topics like "The Greenhouse Effect" without dumbing them down. What we learned The Power of Context: Large Language Models (LLMs) become exponentially more useful when grounded in structured application data. Gamification Psychology: Small UI feedbacks—like a progress bar filling up or a badge unlocking—have a disproportionate impact on user motivation. Sustainable Web Design: Just as we track carbon, we optimized our asset delivery and code splitting to ensure the website itself has a low digital carbon footprint. What's next for Sustain-a-thon Backend Migration: Migrating our persistence layer to Supabase (PostgreSQL) to enable social features and real-time multiplayer leaderboards. Mobile Native: Porting the React code to React Native (Expo) for iOS/Android deployment. IoT Integration: Connecting to smart home APIs to automatically log energy savings. <div