---
slug: "elda-ai"
url: "https://devpost.com/software/elda-ai"
title: "Elda AI"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 434
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/clinician"
  - "user/patient_family"
---

# Elda AI

> EldaAI listens, learns, and detects, transforming eldercare with AI that monitors behavior, prevents medication mistakes, and empowers caregivers through real-time insights.

[Devpost](https://devpost.com/software/elda-ai) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[elder_child_care]] [[health_clinical]] [[transportation]]
**user** [[clinician]] [[patient_family]]

**stack** html5, java, javascript, python, shell, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what’s next for eldaai

## Body

Inspiration When my grandmother was diagnosed with dementia, we watched her memory fade and her independence slowly disappear. Simple routines like taking medicine or remembering meals became daily struggles. That experience made us realize how deeply technology fails the people who need it most. EldaAI was born from the desire to build an AI that could understand, care, and detect before things get worse. What it does EldaAI is an AI-powered eldercare platform that transforms caregiving from reminders to real-time intelligence. It listens, learns, and detects using Claude to understand speech and emotion, Letta to learn daily behavior patterns, and Chroma to detect changes over time. EldaAI automatically generates daily and monthly health summaries for doctors and caregivers, highlighting medication compliance, mood shifts, and potential cognitive decline. How we built it Backend: FastAPI with PostgreSQL, JWT authentication, and APScheduler for smart reminders. AI Layer: Claude for intent and sentiment analysis, Letta for behavioral memory, Chroma for semantic pattern detection. Mobile App: Built with React Native + Expo for voice-first interaction. Caregiver Dashboard: Built with Next.js + Tailwind for real-time monitoring, insights, and alerts. Communication: Twilio for voice calls, Firebase for push notifications. Deployment: Railway (backend), Vercel (dashboard). Challenges we ran into Making voice-based AI interactions natural for elderly users with limited tech familiarity. Training Claude to detect subtle emotional cues and health-related intent. Integrating multiple AI services (Claude, Letta, Chroma) seamlessly while staying within API limits. Designing a UI that feels simple enough for 80-year-olds but powerful enough for doctors. Accomplishments that we're proud of Built a fully functional prototype Mobile App for Elder People and Care Giver web app in 2 days that integrates Claude, Letta, and Chroma. Successfully generated real-time AI health summaries from daily conversations. Designed a caregiver dashboard that visualizes daily mood and medication adherence. Created a system that bridges empathy, AI, and healthcare — something our team truly believes in. What we learned Building human-centric AI means designing for emotion, not just accuracy. Simplicity in UX is more powerful than complexity in features — especially for elders. Prompt engineering and data context are key to getting reliable results from LLMs like Claude. Collaboration across AI, design, and healthcare perspectives can create deeply impactful solutions. What’s next for EldaAI Integrate with wearable health data (heart rate, sleep, activity) for early disease detection. Enable multi-language and cultural personalization for global accessibility. Expand caregiver tools to include doctor collaboration and long-term pattern analytics. Long-term vision: Let people “train” their AI throughout their lives so when they age, their AI already knows them deeply, acting as a personal caregiver and memory companion. <div