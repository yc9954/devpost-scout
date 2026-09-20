---
slug: "intelliclass-your-end-to-end-smart-learning-platform"
url: "https://devpost.com/software/intelliclass-your-end-to-end-smart-learning-platform"
title: "IntelliClass : Your End-to-End Smart Learning Platform"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 230
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
---

# IntelliClass : Your End-to-End Smart Learning Platform

> IntelliClass converts any educational video into interactive quizzes, tracks performance, and ensures students truly understand content instead of passively watching making overall a fun experience.

[Devpost](https://devpost.com/software/intelliclass-your-end-to-end-smart-learning-platform) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[transcript_audio]]

**stack** api, deepgram, express.js, gemini, google, jitsi, meet, mern, mongodb, n8n, node.js, react, render, serpapi

## How they structured the write-up

- problems faced
- solution
- admin module
- teacher module
- student module
- core features
- tech stack
- how it works
- impact
- future scope

## Body

LANDING PAGE Why Choose us? Brochure of the Project ARCHITECTURE TECH STACK n8n Automation workflow PROBLEMS FACED Students passively watch videos without testing understanding Teachers spend excessive time creating quizzes manually No efficient tools to convert video content into assessments Lack of quick revision and retention-check systems No automated pipeline for video → quiz generation with timestamps SOLUTION IntelliClass provides a fully automated video-to-assessment pipeline. ADMIN MODULE User roles & permission management Curriculum & course structuring Analytics dashboards for performance insights Activity tracking & audit logs TEACHER MODULE Classroom management Live MCQ quiz builder with gamification Document digitization Real-time polls Video meetings with Jitsi STUDENT MODULE Personalized performance dashboard Leaderboards AI-powered study assistance Quiz generation from YouTube links Interactive transcripts Discussion forums CORE FEATURES Video → Quiz Automation Transcript-based question generation Timestamp-linked learning Real-time analytics & feedback Personalized learning insights Gamification TECH STACK Frontend & Backend: MERN Stack AI: Gemini API, NLP, Fuzzy Matching Speech-to-Text: Deepgram API Realtime: Socket.io Meetings: Jitsi Meet Deployment: Vercel & Render HOW IT WORKS User inputs a YouTube link Transcript is fetched/generated AI extracts key concepts Quiz is generated automatically Students attempt quizzes Insights & analytics are generated IMPACT Saves hours of manual quiz creation Improves engagement & retention Enables data-driven learning Bridges content consumption & understanding FUTURE SCOPE Adaptive learning paths Multi-language support LMS integrations Advanced analytics Offline learning & mobile app support <div