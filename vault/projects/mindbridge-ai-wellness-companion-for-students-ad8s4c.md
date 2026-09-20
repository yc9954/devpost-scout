---
slug: "mindbridge-ai-wellness-companion-for-students-ad8s4c"
url: "https://devpost.com/software/mindbridge-ai-wellness-companion-for-students-ad8s4c"
title: "MindBridge — AI Wellness Companion for Students"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 694
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# MindBridge — AI Wellness Companion for Students

> AI that detects student burnout 14 days before it peaks.

[Devpost](https://devpost.com/software/mindbridge-ai-wellness-companion-for-students-ad8s4c) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[health_clinical]] [[mental_health]] [[supply_logistics]]
**user** [[clinician]] [[developer]] [[educator_student]] [[researcher]] [[social_worker]]
**substrate** [[genomic_bio]] [[geospatial]] [[structured_db]]

**stack** css3, react, supabase, typescript

## How they structured the write-up

- 🧠 inspiration
- 💡 what it does
- 🛠️ how i built it
- 🔬 the burnout dna algorithm
- ⚔️ challenges i faced
- 📚 what i learned
- 🎯 what's next

## Body

🧠 Inspiration I watched my friends fall apart during exam season. Not dramatically — quietly. Skipping meals. Stopping replies. Saying "I'm fine" when they clearly weren't. The scariest part? Nobody saw it coming. Not their friends. Not their professors. Not even themselves. I kept thinking — we have fitness trackers for our bodies. Weather forecasts for tomorrow. Why does nobody build an early warning system for the mind? That question became MindBridge. 💡 What It Does MindBridge is an AI-powered student wellness companion that detects burnout 14 days before it peaks — and gives students the tools to recover before it breaks them. Students complete a 60-second daily check-in tracking mood, energy, sleep, and stress. Gemini AI analyzes 14+ days of behavioral patterns to generate a personalized Burnout DNA Score across 5 dimensions. Three things no other wellness app does: 🗺️ Crisis Pulse Campus Map — world's first real-time anonymous campus wellness heatmap 📅 Academic Stress Forecast — predicts burnout risk weeks before exam season hits 🎤 Voice Emotion Check-in — speak 30 seconds, AI detects your emotional tone and auto-fills your entire check-in 🛠️ How I Built It I built MindBridge as a solo developer using Lovable.dev for rapid full-stack development, combining React, TypeScript, Tailwind CSS, and Supabase in a single cohesive platform. The AI layer runs entirely on Google Gemini Flash — handling burnout pattern analysis, coping strategy generation, wellness coaching, voice emotion detection, peer matching, and academic stress forecasting. The data layer uses Supabase with Row Level Security enforced at the database level — ensuring student privacy is a technical guarantee, not just a policy promise. The Crisis Pulse Campus Map was the hardest feature to architect. It needed to show real wellness trends without ever exposing individual student data. The solution: a minimum threshold algorithm that only activates a campus zone when at least 10 students have checked in — making reverse-engineering individual data mathematically impossible. Architecture: Student Check-in (60 sec) ↓ Gemini AI Pattern Analysis ↓ Burnout DNA Score (0–100) ↓ Personalized Coping Strategies ↓ Crisis Pulse Map (Institution View) 🔬 The Burnout DNA Algorithm MindBridge uses a weighted multi-dimensional scoring model inspired by the Maslach Burnout Inventory: $$\text{Burnout Score} = \sum_{i=1}^{5} w_i \cdot d_i$$ Where: \( d_i \) = dimension score (Emotional, Physical, Academic, Social, Motivational) \( w_i \) = clinical weight per dimension Result normalized to \( [0, 100] \) Risk zones: 0–30 ✅ Thriving 31–55 🟡 Moderate 56–75 🟠 At Risk 76–100 🔴 Crisis ⚔️ Challenges I Faced 1. Making AI responses feel human, not clinical Early Gemini responses sounded like a medical textbook. Students in testing said it felt "robotic and scary." I rewrote the entire system prompt with strict tone constraints — validate before advising, lead with empathy, max 3 sentences, end with one small action step. Result: students described it as "like a friend who actually gets it." 2. Anonymous campus heatmap without data leaks The Crisis Pulse Map needed real wellness data without ever exposing individuals. Early builds leaked zone data with fewer than 3 students. Fixed with a 10-student minimum threshold + Supabase RLS policies that only expose aggregated counts — never raw rows. 3. Voice check-in latency First build had 6–8 second lag between speech and results. Fixed by streaming interim results from Web Speech API and firing the Gemini call after 15+ words captured — reducing perceived latency from 8 seconds to under 2 seconds. 4. Burnout score accuracy Early versions gave identical scores to completely different student situations. Redesigned with weighted multi-dimensional scoring inspired by the Maslach Burnout Inventory clinical framework. 📚 What I Learned Privacy is not a feature — it's an architecture AI tone matters as much as AI accuracy The best wellness tools feel like a friend, not a doctor Solo building forces clarity — every feature must justify its existence Student mental health is a systemic problem that needs systemic data to solve 🎯 What's Next Native mobile app (React Native) WhatsApp daily check-in bot University ERP integration Multi-language support (Hindi, Tamil, Telugu) Research partnership with psychology departments Corporate employee wellness expansion MindBridge doesn't replace counselors. It makes sure students actually reach them. <div