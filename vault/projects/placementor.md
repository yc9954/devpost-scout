---
slug: "placementor"
url: "https://devpost.com/software/placementor"
title: "Placementor"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 910
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# Placementor

> AI-Powered Voice Interview Coach

[Devpost](https://devpost.com/software/placementor) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** agno, axios, flask, gemini, murfai, react

## How they structured the write-up

- deployed link: link
- 📚 table of contents
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for placementor
- about
- features
- tech stack
- agents
- usage
- developed by

## Body

🚀 Placementor — AI-Powered Voice Interview Coach Built Using Murf Falcon Deployed Link: link 📚 Table of Contents Inspiration What it does How we built it Challenges we ran into Accomplishments that we're proud of What we learned What's next for Placementor Features Tech Stack Agents Usage Developed By Inspiration Real interviews depend on communication skills — yet most prep platforms are entirely text-based. Millions of students and job-seekers struggle not because they lack knowledge, but because they lack a realistic space to practice speaking under pressure. We wanted to build a platform where you don't just read interview questions — you hear them, answer them out loud, and get instant feedback. That gap between text-based prep and real interview dynamics was our starting point for Placementor. What it does Placementor is a voice-first AI interview training platform that simulates a real interview experience end-to-end: 🎤 Hear questions narrated by Murf Falcon TTS in a natural interviewer voice 🗣️ Speak your answers captured live via Automatic Speech Recognition (ASR) 📊 Receive instant structured AI feedback on structure, clarity, relevance, and depth 📄 Upload your resume for personalized, role-specific question generation 🔁 Repeat or proceed based on AI recommendations for mastery learning It supports company-specific, role-specific, and round-specific interview simulations — making prep genuinely targeted and immersive. How we built it Placementor is built on a modular dual-agent architecture with a voice layer on top: Frontend: React.js + Tailwind CSS for a clean, responsive UI Backend: Python + Flask for fast real-time API handling Voice Layer: Murf Falcon TTS API for low-latency, natural question narration ASR for live speech-to-text answer capture AI Agents: Built using the Agno framework + Gemini , split into four dedicated agents: Resume Parser — extracts structured data from uploaded PDFs Interview Planner — generates progressively difficult, personalized question sets Question Fetcher — retrieves questions by serial number for smooth voice flow Feedback Agent — scores answers and provides detailed improvement guidance The seamless loop of listen → speak → analyze → respond was made possible by Murf Falcon's stable, low-latency API output integrating cleanly with our Flask backend. Challenges we ran into Synchronizing TTS narration with ASR capture without overlap or lag Ensuring low-latency voice output so the conversation felt natural, not robotic Designing structured AI scoring that was consistent and not arbitrary across sessions Parsing diverse resume formats reliably into clean, structured JSON Balancing question difficulty progression so interviews felt realistic rather than random Building a smooth repeat-or-proceed logic that didn't disrupt the interview flow Accomplishments that we're proud of ✅ Built a fully voice-first interview simulation — hear the question, speak the answer, get feedback ✅ Achieved seamless Murf Falcon + ASR integration with real-time response ✅ Designed a modular 4-agent architecture that is clean, maintainable, and extensible ✅ Delivered company and role-specific question generation from resume context ✅ Implemented structured AI feedback scoring (1–10) with ideal answer comparisons ✅ Deployed a fully functional live product at place-mentor-murf-ai.vercel.app What we learned Voice-first UX requires a fundamentally different design mindset than text-based apps — latency is everything Structured agent outputs (clean JSON) are far more reliable than freeform AI responses for downstream processing Murf Falcon's stable API made real-time TTS integration far more practical than expected Resume parsing needs robust fallback handling given the variety of real-world formats Modular agent separation makes the system significantly easier to debug, test, and extend What's next for Placementor [ ] Multiple voice personalities — choose HR, technical, or panel interviewer tones [ ] Mock HR stress testing — pressure-based question sequences [ ] Multilingual interview modes — practice in regional languages [ ] Company-specific interview packs — curated question banks per company [ ] Behavioral + Technical + System Design rounds — full interview cycle support [ ] Tone and pacing analytics — feedback on how you speak, not just what you say [ ] Progress tracking dashboard — visualize improvement over sessions About Placementor is a next-generation voice-first interview training platform designed to help users practice, improve, and perfect their interview performance. It integrates: ✅ Murf Falcon TTS for ultra-natural, real-time question narration ✅ Automatic Speech Recognition (ASR) for live conversational interaction ✅ AI Agents for adaptive question generation & feedback Features 🎤 Voice-first Interview Simulation using Murf Falcon TTS 🗣️ Real-time ASR-based Response Capture 📄 Resume Upload & Parsing 🧠 AI Interview Planner generates role/company-specific questions ❓ Dynamic Question Fetching 📊 AI Feedback Agent provides structure, clarity & relevance scores 🔁 Repeat Question Logic for mastery learning ⚡ Fast Flask Backend for Real-Time Conversations Tech Stack Frontend: React.js, Tailwind CSS Backend: Python, Flask Voice Tech: Murf Falcon TTS API ASR (Automatic Speech Recognition) AI Agents Framework: Agno + Gemini Others: Axios, JSON, Git Agents Resume Parser Extracts structured resume data: name, email, phone, skills, projects, education, experience. Uses Gemini via Agno Framework. Returns clean JSON with parsed content. Interview Planner Generates progressively difficult interview questions. Personalized based on company, role, resume, and round. Outputs a detailed JSON plan. Question Fetcher Retrieves specific questions by serial number. Ensures smooth integration with the voice agent step. Feedback Agent Evaluates user answers using AI scoring parameters: structure, clarity, relevance, depth. Provides: Score (1–10) Detailed feedback Corrected ideal answer Repeat-or-proceed recommendation Usage Upload Resume (PDF) Select Target Company + Role + Round Start Voice Interview Murf Falcon narrates questions ASR captures user answers Get Instant Feedback Repeat or Proceed Based on AI Recommendations Developed By Tejas Gadge Anisha Shankar <div