---
slug: "study-hub-5nk0xq"
url: "https://devpost.com/software/study-hub-5nk0xq"
title: "Study-Hub"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 583
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# Study-Hub

> Study smarter, not harder — with AI that knows your plan.

[Devpost](https://devpost.com/software/study-hub-5nk0xq) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
  <sub>weak: developer_tools</sub>
**user** [[educator_student]]
**substrate** [[document_pdf]]
  <sub>weak: code_repository, geospatial, structured_db</sub>

**stack** css3, html5, react, typescript

## Body

Inspiration The inspiration behind Study-Hub came from the universal struggle students face: managing time effectively while trying to master complex subjects. We noticed that students often juggle multiple apps—one for scheduling, one for flashcards, another for notes, and generic AI tools for help. We wanted to forge a unified platform where intelligence meets productivity, creating a central "hub" that not only organizes your study life but actively helps you learn through context-aware AI. What it does Study-Hub is a futuristic, all-in-one productivity platform designed to gamify and optimize the learning process: Intelligent Study Planner: Uses AI to generate personalized schedules based on your specific subjects and difficulty levels. AI Subject Tutor: A dedicated chat interface that acts as a 24/7 tutor, capable of explaining complex topics in simple terms. Auto-Generated Flashcards: Instantly creates study decks from topics or notes using Gemini AI, saving hours of manual entry. Gamified Quests: Turns studying into an RPG-like experience where completing tasks earns you XP, helping you level up your profile. Deep Analytics: Visualizes your study habits, focus time, and subject mastery with interactive charts. Social Connectivity: Allows you to find study partners and track peer progress to stay motivated. How we built it We built Study-Hub using a modern, high-performance tech stack: Frontend: React 19 with TypeScript for a robust and type-safe user interface. Styling: Tailwind CSS was used to craft the immersive, dark-mode "glassmorphism" aesthetic. AI Integration: We leveraged Google's Gemini API (@google/genai) to power the intelligence behind the planner, flashcard generator, and tutoring chat. Backend & Auth: Supabase handles our secure user authentication and real-time database needs. Data Visualization: Recharts brings the analytics page to life with responsive graphs. Motion: Framer Motion adds fluid transitions and animations to make the app feel alive. Challenges we ran into Structured AI Outputs: Getting the Gemini API to consistently return valid JSON for things like Flashcards and Study Plans was a challenge. We had to refine our prompt engineering to ensure the UI wouldn't break due to malformed AI responses. Real-time State Sync: syncing the gamification elements (XP, Levels) across the Dashboard, Quests, and Profile pages in real-time required careful state management with Supabase. Authentication Flows: Implementing protected routes that seamlessly handle session persistence and redirects took several iterations to get right. Accomplishments that we're proud of The "Crafted" Feel: We're incredibly proud of the UI/UX. It doesn't look like a standard bootstrap app; it feels like a futuristic tool for elite students. Seamless AI: The integration of Gemini is smooth—it feels like a native part of the application logic rather than just a bolted-on chatbot. Functional Gamification: We successfully implemented a system where productivity directly translates to in-app progress, making studying genuinely more engaging. What we learned Prompt Engineering: We learned that the quality of AI output is directly tied to the specificity of the system instructions. Supabase RLS: We gained a deeper appreciation for Row Level Security policies to ensure users can only access their own study data. Modern React Patterns: Using the latest React features and hooks helped us keep the codebase clean and performant. What's next for Study-Hub Voice Mode: Utilizing the microphone permissions to enable oral quizzes and voice-based tutoring sessions. Collaborative Study Rooms: Adding real-time multiplayer rooms where users can study together on a shared whiteboard. Document Analysis: Allowing users to upload PDF textbooks (using our PDF.js integration) so the AI can generate quizzes directly from their course material. Mobile Native: Porting the experience to React Native for on-the-go studying. <div