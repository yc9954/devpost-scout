---
slug: "intelliquiz"
url: "https://devpost.com/software/intelliquiz"
title: "IntelliQuiz"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 298
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "substrate/document_pdf"
---

# IntelliQuiz

> An AI powered quiz generator with real time leaderboard for participants.

[Devpost](https://devpost.com/software/intelliquiz) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**substrate** [[document_pdf]]

**stack** google-gmail-oauth, groq, javascript, postgresql, redis, socket.io, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for intelliquiz

## Body

Landing page Dashboard Page Quiz creation card Quiz created Live Quiz Inspiration Creating quality quizzes manually is tedious, while live quiz platforms often lack intelligent content generation. I wanted to combine AI with real-time multiplayer interactions to build a platform that can generate engaging quizzes instantly and make learning more interactive. What it does IntelliQuiz is an AI-powered real-time quiz platform where users can generate quizzes from natural language prompts, configure difficulty and question count, and host live multiplayer sessions. Participants can join using a room code and compete through synchronized timers and dynamic leaderboards. How I built it I built IntelliQuiz using Next.js, TypeScript, Tailwind CSS, and shadcn/ui for the frontend, with PostgreSQL and Prisma ORM for data management. Socket.IO powers the real-time quiz experience, while Redis Sorted Sets handle low-latency leaderboard updates. GROQ API is used for AI-based quiz generation. Challenges I ran into The biggest challenge was designing a smooth real-time architecture with synchronized timers and instant leaderboard updates. Managing AI API rate limits and planning a scalable approach for future PDF-based quiz generation also required careful system design decisions. Accomplishments that I'm proud of I'm proud of building a complete end-to-end AI quiz platform that combines AI-generated content with real-time multiplayer gameplay. Integrating WebSockets and Redis for live interactions with low latency while maintaining a clean and responsive user experience was a particularly rewarding achievement. What I learned This project helped me gain practical experience with WebSocket architectures, Redis-based real-time state management, and integrating LLM APIs into production workflows. I also learned how to balance scalability, performance, and user experience. What's next for IntelliQuiz I plan to extend IntelliQuiz by supporting PDF and YouTube-based quiz generation, AI-generated answer explanations, personalized learning insights, and improved real-time infrastructure to support larger live events and classrooms. <div