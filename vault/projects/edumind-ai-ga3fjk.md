---
slug: "edumind-ai-ga3fjk"
url: "https://devpost.com/software/edumind-ai-ga3fjk"
title: "Edumind Ai"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 593
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
---

# Edumind Ai

> EduMind AI — Free AI-powered STEM learning for 500M Indian students. 7 AI providers, 10+ features: quizzes, flashcards, mentor, resume & interview prep. Zero cost. Maximum impact.

[Devpost](https://devpost.com/software/edumind-ai-ga3fjk) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]]

**stack** apis, backend, css-?-frontend-(react.js-+-vite-+-tailwind)-node.js, express.js, javascript, jsx, provider, sqlite

## Body

Inspiration India has 500 million students but only a fraction can afford quality STEM coaching. Growing up in Jaunpur, UP, I saw brilliant minds held back not by lack of talent but by lack of access. Coaching institutes charge ₹5,000–15,000/month — impossible for most families. I built EduMind AI because I believe every student deserves a world-class AI tutor in their pocket, completely free. PreetBeacon already serves 10,000+ AKTU students — EduMind AI is the next evolution. What it does EduMind AI is a free, all-in-one AI-powered STEM learning platform featuring 10+ tools: an AGI Mentor that personalises lessons to your learning style, Smart Quiz Generator, Spaced-Repetition Flashcards, AI Notes Summariser, Deep Research Assistant, Resume Builder, Interview Prep with real-time feedback, Study Planner, Gamified Leaderboard with XP and streaks, and a Referral Engine. Powered by a 7-provider AI rotator (Gemini, OpenAI, Groq, Cerebras and more) ensuring 99.9% uptime with zero cost to students. How we built it Frontend: React.js + Vite + Tailwind CSS + Zustand for state management. Backend: Node.js + Express + SQLite. AI Layer: Custom 7-provider rotator that automatically switches between Gemini, OpenAI, Groq, Cerebras, and other free-tier providers based on availability — ensuring zero downtime. Auth: JWT + bcrypt. Deployed on Vercel (frontend) and Render (backend). Built solo as a full-stack developer over several months of iterative development and real user testing. Challenges we ran into Managing 7 different AI provider APIs with different response formats, rate limits and model names was the biggest challenge — building a unified rotator that handles failover seamlessly took significant engineering effort. Keeping the entire platform free while maintaining performance required creative use of free tiers across every service. Building a gamification system (XP, streaks, leaderboard) with real-time sync on a zero-budget backend was another major hurdle. As a solo developer handling frontend, backend, DevOps, and product design simultaneously, prioritising features for maximum student impact was a constant balancing act. Accomplishments that we're proud of Successfully built and deployed a production-ready AI education platform as a solo developer with zero budget. The 7-provider AI rotator is a genuinely novel architecture ensuring students never face a "service unavailable" error. PreetBeacon — our earlier platform — already serves 10,000+ active AKTU students, validating real demand. Achieved Google AdSense approval and built a PWA with push notifications. Every single feature — from flashcards to resume builder — was designed based on direct feedback from real students in our WhatsApp community of 195+ members. What we learned Building for real users is completely different from building for demos. Every feature had to survive contact with actual students who had real exams tomorrow. We learned that reliability matters more than features — a platform that works 99% of the time beats a feature-rich one that crashes. We also learned that gamification dramatically increases retention — students return daily for streaks and XP in ways they never would for a plain study tool. Most importantly: constraints breed creativity. Zero budget forced us to find elegant solutions that paid platforms never need to discover. What's next for EduMind AI Expanding beyond AKTU to all Indian universities and competitive exams (JEE, NEET, GATE, UPSC). Adding voice-based AI tutoring for students in low-literacy environments. Integrating AR-based STEM visualisations for complex physics and chemistry concepts. Launching a teacher dashboard so professors can assign AI-generated quizzes to entire classrooms. Partnering with state governments to deploy EduMind AI in government schools across UP and Bihar. Long-term vision: become the world's largest free AI education platform — starting from Jaunpur, reaching every student on earth. <div