---
slug: "learnflow-aj4yi7"
url: "https://devpost.com/software/learnflow-aj4yi7"
title: "LearnFlow"
hackathon: "AI for Bharat 2026"
organization: "student"
winner: true
words: 688
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
---

# LearnFlow

> AI-Powered Adaptive Learning Platform

[Devpost](https://devpost.com/software/learnflow-aj4yi7) · hackathon [[AI for Bharat 2026]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** axios, bcrypt, css, css3, dom, eslint, fastapi, git, github, gsap, html5, javascript, jwt, lucide

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- accomplishments we’re proud of
- what we learned
- what’s next

## Body

LearnFlow - Hackathon Submission Inspiration LearnFlow was inspired by the widening educational inequality observed during the pandemic. While some students benefited from personalized tools and private tutoring, millions relied on generic, one-size-fits-all content with no adaptability. This led us to ask: What if AI could democratize access to personalized education? Three key observations strengthened our vision: Teachers spend 10+ hours per week creating learning materials and assessments Students forget 70% of newly learned content within 24 hours without reinforcement Over 1.2 billion students worldwide lack access to personalized learning support LearnFlow exists to ensure that every learner has access to a personalized AI tutor, and every educator has tools that amplify — not replace — their impact. What It Does LearnFlow is an AI-powered adaptive learning platform that converts any text into personalized learning materials within seconds. For Students Instant Study Material Generation: Upload or paste content to generate quizzes, summaries, and flashcards Smart Spaced Repetition: Implements the SM-2 algorithm to optimize review timing Adaptive Feedback: Prioritizes weak topics and adjusts difficulty based on performance Progress Analytics: Tracks mastery, recall patterns, and study behavior Gamification: Includes streaks, badges, and learning milestones Multi-language Output: Supports English, Spanish, and French For Teachers Class and Student Management AI-Generated Assessments with difficulty tuning Student Progress Dashboard Performance Insights and Alerts Reduced Content Creation Workload The Technology AI content generation using Mistral AI Custom implementation of the SM-2 spaced repetition algorithm Real-time analytics with adaptive difficulty Accessible and intuitive UI inspired by modern learning platforms How We Built It Frontend React 18 + Vite Axios Recharts for visual analytics Tailwind CSS for responsive UI React Router and Lucide Icons Backend FastAPI (Python) SQLite + SQLAlchemy ORM JWT authentication and Bcrypt for hashing Pydantic for validation Mistral AI integration Algorithms and Architecture Full SM-2 spaced repetition logic Adaptive learning rules based on performance trends Analytics engine using weighted scoring and indexed database queries Development Approach Research cognitive science methods and existing learning systems Design modular architecture with async API operations Build core learning and assessment features Layer advanced features: spaced repetition, analytics, and dashboards UI polish, user flows, and error handling Testing and deployment optimization Technical Highlights Fully working spaced repetition learning flow Real-time progress tracking with optimized database queries Clean, maintainable, and scalable API design Cross-platform friendly deployment adjustments Challenges We Faced 1. AI Response Consistency Mistral’s responses varied in structure. We solved this with stricter prompts, schema validation, and fallback parsing. 2. Spaced Repetition Edge Cases Handling first-time cards, failed reviews, and ease factor adjustments required extensive testing and iteration. 3. Efficient Progress Analytics Tracking trends for potentially large datasets required query optimization and caching. 4. Deployment Compatibility Platform differences caused build permission issues, resolved by updating run commands for portability. 5. Balancing Simplicity vs. Power We refined the UI with role-based views and progressive feature reveal. Accomplishments We’re Proud Of A complete, functional platform — not just a prototype Implemented a scientifically proven memory optimization technique (SM-2) Built a design experience that is both modern and accessible Delivered meaningful features for both educators and students Strong technical execution with secure authentication, analytics, spaced repetition, and AI generation What We Learned Technical Advanced React patterns, hooks, and performance optimizations FastAPI middleware, async programming, and scalable API design Prompt engineering and AI validation strategies Translating academic algorithms (SM-2) into production code Deployment troubleshooting and CI/CD workflows Product and Design User-centered feature prioritization Education psychology principles: spaced repetition, active recall Accessibility and effective UI/UX in learning platforms Scaling architectures and designing for real-world usage Soft Skills Collaboration, debugging under pressure, and iterative problem solving Vision alignment while still shipping an MVP Balancing feature ambition with time constraints What’s Next Short Term (1–3 months) Native mobile apps Offline learning mode Study groups and peer interaction Support for additional AI models Pre-built content library Medium Term (6–12 months) Voice-based learning Video and audio material extraction LMS integrations (Google Classroom, Moodle) Marketplace for educators Long-Term Vision Full adaptive personal learning paths Multi-modal learning (AR/VR) 50+ global languages supported Partnerships with research institutions and NGOs Open-source core for accessibility and collaboration LearnFlow — Democratizing Education Through AI <div