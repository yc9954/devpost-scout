---
slug: "predvisit"
url: "https://devpost.com/software/predvisit"
title: "PredVisit"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 470
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# PredVisit

> The AI copilot for hospital staff — patient records, readmission risk scoring, and clinical guidance, all in one place.

[Devpost](https://devpost.com/software/predvisit) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[health_clinical]]
  <sub>weak: accessibility, supply_logistics</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]
  <sub>weak: document_pdf, video_visual, web_dom</sub>

**stack** api, css3, groq, html5, javascript, json, llama, sql, supabase, vercel

## Body

Screenshotes Patients list + analyze AI Chat Analyze with Database My sister is a nurse. My aunt has been in and out of hospitals for years. Watching them navigate the system — my sister buried in paperwork at the end of a 12-hour shift, my aunt waiting while staff manually searched through records — I kept thinking: why is this still so manual? I've also been on the other side. I was hospitalised with asthma as a kid, and I remember how chaotic it felt even as a patient — unclear timelines, staff who seemed overwhelmed, no sense of who knew what about your case. When I started looking at where AI was actually being used in meaningful ways, healthcare stood out for the opposite reason: it largely wasn't. Finance, logistics, customer service — all transformed. Hospitals? Still Excel sheets and verbal handoffs. That gap felt like the most honest place to build something. How I Built It I built PredVisit alone, over two weeks. The stack is intentional: Vanilla JS and HTML on the frontend, Node.js serverless functions on Vercel, Supabase for the database and real-time features, and Groq with Qwen for inference. I chose Groq specifically because speed wasn't a nice-to-have — nurses don't wait. Sub-second responses were a hard requirement from day one. The database ships as two .sql files. Anyone can clone the repo and have a fully working instance running on Supabase in minutes. What I Learned I learned that building for a specific person changes how you make decisions. Every time I was unsure about a feature, I thought about my sister at the end of a shift. Would this actually help her, or am I just making it look impressive? On the technical side — latency is a discipline. Getting consistent AI responses under one second meant profiling every layer: API calls, database reads, streaming. I also learned how much careful prompt engineering goes into making a model behave differently in two distinct modes without the contexts bleeding into each other. And I learned that multilingual voice input is harder than it looks. Kazakh medical terminology through Whisper was a real fight. Challenges The worst moment came when I started testing the English voice mode. The AI responses were fine — but Whisper kept misrecognising Kazakh-accented English in ways that broke clinical terms completely. Fixing that meant building post-processing logic I hadn't planned for, at a point when I thought I was almost done. Building alone has a specific kind of difficulty. There's no one to catch your blind spots, no one to tell you a bug you've been staring at for three hours has an obvious fix. You have to be your own reviewer, your own QA, your own product manager. Two weeks. One person. I'm proud of what came out. <div