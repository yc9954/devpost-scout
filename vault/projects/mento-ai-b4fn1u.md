---
slug: "mento-ai-b4fn1u"
url: "https://devpost.com/software/mento-ai-b4fn1u"
title: "mento.ai"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1144
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
---

# mento.ai

> mento.ai is an AI-powered 3D personal STEM tutor that teaches students through real-time, human-like voice conversations and emotionally adaptive learning — not just answers, but actual mentorship.

[Devpost](https://devpost.com/software/mento-ai-b4fn1u) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[health_clinical]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[genomic_bio]] [[geospatial]]
  <sub>weak: sensor_telemetry</sub>

**stack** deepgram, elevenlabs, express.js, framer, framer-motion, microsoft-azure-face-api, mongodb, motion, node.js, openai, postgresql, react, tailwindcss, tavus-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mento.ai

## Body

Landing Page System Architecture Market Growth Projections Performance Metrics Competitor Analysis Inspiration Every student knows the feeling: you're stuck on a chemistry problem at 11 PM, your notes don't help, YouTube has seventeen conflicting videos, and your teacher is unavailable. You turn to an AI chatbot, and it gives you an answer , not an explanation, not a walkthrough, just text on a screen. We felt this gap deeply. Students don't just need answers. They need patience, presence, and personalised guidance , the kind only a great tutor can provide. But great tutors are expensive, time-limited, and out of reach for millions of students globally. That's what inspired mento.ai : an AI-powered personal STEM tutor that doesn't just respond, it teaches . We wanted to build something that captures the warmth of a real mentor while being available 24/7 to anyone with an internet connection. What it does mento.ai is an AI-powered educational platform that delivers real-time, personalised STEM learning through a lifelike 3D AI tutor avatar, think Google Meet, but your meeting partner is your most patient, knowledgeable, and always-available teacher. Core experience: A student opens mento.ai and enters a Conversational Video Interface (CVI) , a Google Meet-style session where the AI avatar joins them face-to-face The student speaks naturally: "I'm great at physics but struggling with chemistry, where do I start?" The AI tutor responds with voice, facial expressions, and step-by-step explanations tailored to the student's level The session adapts in real-time based on the student's engagement, confusion, or confidence Key features: 🎥 Conversational Video Interface , A real-time AI tutor session with a lifelike avatar that lip-syncs, reacts, and teaches like a human 🧠 Adaptive Teaching , Explanations adjust in depth, speed, and style based on how the student is responding 🎙️ Voice-First Interaction , Students ask doubts naturally through speech; no typing required 📊 Learning Dashboard , Tracks progress, time spent per subject, session history, and learning insights 📚 Subject Library , Organised STEM content across Mathematics, Physics, Chemistry, and Computer Science ⚡ Instant Doubt Clarification , Step-by-step breakdowns of any concept, formula, or problem on demand 😊 Emotion Recognition (roadmap), Detects confusion, boredom, or excitement through facial and vocal cues to dynamically adjust the teaching approach How we built it We built mento.ai as a full-stack AI application with a layered architecture designed for real-time conversational learning. Frontend — Built with React 18 + TypeScript and styled using Tailwind CSS. Framer Motion powers the smooth animations across the landing page, CVI, and dashboard. Vite gives us a fast development and build experience. Backend — Node.js and Express.js serve the API layer, connecting the frontend to our AI services. The backend handles session management, avatar API calls, and routing for learning analytics. AI Avatar — We integrated the Tavus API to power the lifelike 3D tutor avatar. Tavus handles real-time video generation, lip-sync, and avatar responsiveness during live sessions. Voice Pipeline — Student speech is captured using the Web Speech API and processed into text. AI responses are converted back to natural voice using ElevenLabs TTS , creating a seamless voice conversation loop. Tutoring Intelligence — The educational AI backbone uses OpenAI GPT-4/Groq to generate personalised, pedagogically structured responses — not just answers, but step-by-step explanations crafted for the student's context. Challenges we ran into Building something that feels human, not robotic was our hardest challenge. It's easy to make an AI that answers — it's incredibly difficult to make one that teaches . Specific technical hurdles we faced: Avatar-response synchronisation — Keeping the 3D avatar's lip-sync, expressions, and voice output in sync with the AI response in real time required careful latency management between the Tavus API and our TTS pipeline Latency in the voice loop — Minimising the delay between a student speaking and the avatar responding was critical to maintaining a natural conversation flow Adaptive explanation logic — Designing prompts and context management so the LLM actually teaches step-by-step rather than just answering took significant iteration UX simplicity over technical complexity — We wanted a student to open the app and feel comfortable in seconds. Hiding the complexity of 4+ integrated AI services behind a clean, calming interface was a serious design challenge Multimodal state management — Coordinating voice input, video output, session state, and learning analytics across the frontend and backend simultaneously required careful architectural decisions Accomplishments that we're proud of 🎥 Built a fully functional Google Meet-style AI tutor session — a student can join, speak naturally, and receive real-time voice + avatar responses 🤖 Successfully integrated Tavus, ElevenLabs, Web Speech API, and GPT-4 into one seamless conversational flow 📊 Shipped a working learning dashboard that tracks subject progress, session time, and learning insights 🎨 Designed a polished, futuristic UI with glassmorphism aesthetics and smooth Framer Motion animations that make learning feel premium and engaging 💡 Proved that AI can go beyond being a chatbot — mento.ai is the first step toward AI that genuinely mentors Most importantly, we built something a student can actually sit down with and learn from. That was our north star, and we hit it. What we learned How to orchestrate multiple AI APIs into a single, coherent real-time product — Tavus, ElevenLabs, Web Speech API, and an LLM all working together is non-trivial Pedagogical design matters as much as technical design — prompting an LLM to teach is fundamentally different from prompting it to answer Latency is a UX problem, not just a performance problem — even 200ms of extra delay breaks the conversational illusion of a live tutor session Education technology is about empathy first, intelligence second — students learn better when the experience feels safe, supportive, and personal Scope discipline under time pressure — we learned to ship the core experience well rather than spreading across every planned feature What's next for mento.ai mento.ai is just getting started. Our roadmap targets expanding this prototype into a full AI-powered STEM learning ecosystem: 🌍 Multilingual support — tutoring in Hindi, Spanish, French, and more to reach underserved students globally 😊 Emotion & engagement recognition — integrating Microsoft Azure Face API to detect confusion, boredom, or excitement and dynamically adapt the teaching style mid-session 🧪 Interactive STEM simulations — visual, animated concept breakdowns for topics like chemical reactions, physics equations, and data structures 📝 AI-generated quizzes and assignments — personalised practice problems generated after each session based on weak areas 🥽 AR/VR classrooms — immersive environments where students can step inside a molecule or walk through a circuit 👨‍🏫 Classroom mode — enabling teachers to deploy mento.ai as a 24/7 support tool for their students 📱 Mobile app — bringing the full mento.ai experience to smartphones for accessibility anywhere Our long-term mission: make personalised, high-quality STEM education accessible to every student on Earth — regardless of background, geography, or income. mento.ai — where confusion becomes understanding, anytime and anywhere. <div