---
slug: "intellinotes-8gkmvd"
url: "https://devpost.com/software/intellinotes-8gkmvd"
title: "IntelliNotes"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 350
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/structured_db"
---

# IntelliNotes

> A unified database where a community of students can upload/access notes on a variety of subjects with an ai chatbot utilizing google gemini ingrained. Fully built with user auth, buckets, etc.

[Devpost](https://devpost.com/software/intellinotes-8gkmvd) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[education]] [[health_clinical]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[structured_db]]

**stack** amazon-web-services, css3, gemini, github, html5, hugging-face, javascript, node.js, render, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for intellinotes
- notes

## Body

Inspiration Our school currently offers a service called Peer Tutors, but it is limited to in‑person access. We realized that many students need flexible, on‑demand support outside of school hours. That sparked the idea for IntelliNotes: a platform where students can review study material anytime, upload their own notes to save and share, and even interact with an AI assistant to ask questions. By combining collaborative note‑sharing with intelligent support, IntelliNotes aims to extend the benefits of peer tutoring into a digital, always‑available space. What it does IntelliNotes is a fully built web application designed for students, teachers, and lifelong learners. Users can upload and access notes, organize them in a searchable database, and rely on a chatbot to clarify concepts or answer questions. The system also supports summarization, making long notes easier to digest, and encourages knowledge exchange across the community. How we built it We used Supabase for database management, authentication, and bucket storage. The backend was built with Node.js, Express, and CORS, while hosting is split between GitHub Pages for the frontend and Render for backend services. For AI, we integrated a Hugging Face summarizer and Google’s Gemini 2.5 Flash model. To accelerate development, we leveraged Claude for frontend assistance. Challenges we ran into Integrating multiple AI models was complex, especially ensuring they worked seamlessly with uploaded notes. We faced issues with rate limiting, filtering, and search optimization. Training a model directly on user‑uploaded notes also proved challenging. Accomplishments we’re proud of Most core features are functional: uploading, accessing, and searching notes works smoothly, and Gemini integration adds real value. What we learned This was our first time working with buckets and AI models. The learning curve was steep but rewarding, giving us hands‑on experience with modern tools. What’s next for IntelliNotes We envision training our own LLM on uploaded notes, enabling personalized, context‑aware conversations. We’ve already built a database of summaries to support this. Future plans include international collaboration features, a chat platform, and gamified elements like stats pages and leaderboards to motivate contributions. Notes Render takes 30-50 seconds to spin up, please be patient <div