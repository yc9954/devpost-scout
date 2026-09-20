---
slug: "nexevent"
url: "https://devpost.com/software/nexevent"
title: "NexEvent"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 875
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# NexEvent

> A clean, minimal event management system built for developers, meetups, and hackathons

[Devpost](https://devpost.com/software/nexevent) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** cloudinary, data-fns, lucid-react, mongodb, mongoose, next, nextauth, posthog, radix-ui**, react, reactbits, shadcn, sonner, typescript

## How they structured the write-up

- 🎟️ attendee experience
- 🛠️ organizer experience
- 🧩 core platform features
- tech stack
- architecture highlights
- 1. nextauth v5 beta behavior
- 2. serverless database stability
- 3. cloudinary upload pipeline
- 4. slug collision system
- 5. ai integration with gemini
- 6. full-stack type safety
- v1.1 ✅ (completed)
- v2.0
- v3.0
- 🤖 ai-powered attendee dashboard
- 🗣️ voice-enabled event forms
- 💬 enhanced chat-based event assistant
- 🎮 gamification layer

## Body

Home Page All Events Page with seach filter SignIn Page SignUp Page Oraganizer Form Event Description Page Bookings Page (Guest) - Attendee of Hackthon 💡 Inspiration As a solo builder attending hackathons and developer meetups, I kept noticing the same issue: platforms like Devpost , Devfolio , and Unstop are powerful, but the experience often feels heavy, cluttered, and not optimized for simple discovery. Finding good dev events should feel exciting, not overwhelming. I wanted a platform that: looks clean and modern feels fast and intuitive focuses specifically on developers and tech events removes friction for both attendees and organizers That's why I built NexEvent — a minimal, polished, developer-centric event platform created from scratch in a short time by a solo developer. This is the MVP, and the UI/UX will scale aggressively from here. 🎯 What It Does 🎟️ Attendee Experience Browse hackathons, meetups, workshops Filter by tags, track, & location One-tap booking using verified email Add directly to Google Calendar Save favourite events for later (new!) Manage all bookings and favourites in one place AI chatbot assistant to answer questions about events instantly (new!) 🛠️ Organizer Experience Create events with banners, tags, schedule, and full details Edit/update/share events anytime (Organizer booking analytics coming soon) 🧩 Core Platform Features Secure authentication via NextAuth.js Role-based access (Guest / Organizer) Google Gemini AI-powered chatbot for event discovery Server Components for fast performance Cloudinary upload pipeline Zod-validated forms across client + server Clean UI + subtle animations 🛠️ How I Built It (Solo) Tech Stack Next.js 16 (App Router) + React 19 + TypeScript MongoDB + Mongoose NextAuth.js v5 (JWT sessions) Google Gemini AI for intelligent chatbot Cloudinary CDN Tailwind CSS v4 , Radix UI, shadcn/ui ReactBits + MotionPrimitives for animations Zod for validation date-fns + React Day Picker Sonner for toast notifications Architecture Highlights React Server Components → minimal client JS, instant rendering AI-powered chat → context-aware event recommendations Connection pooling → stable serverless DB performance Middleware guards → authenticated routing Unique slug generation → SEO-safe + collision-proof Shared Zod schemas → strong type safety across the stack Modular UI architecture → scalable component system 🚧 Challenges I Faced (as a solo developer) 1. NextAuth v5 Beta Behavior Had to dive into source code to implement role-based JWT callbacks since docs are still evolving. 2. Serverless Database Stability Next.js API routes spawn multiple instances. I wrote a global cached connection layer to prevent MongoDB from hitting connection limits. 3. Cloudinary Upload Pipeline Handling File → Buffer → server-side FormData inside the new App Router required multiple redesigns. 4. Slug Collision System Events often share names. I implemented a Mongoose pre-save hook to auto-generate unique slugs like: devconf-2025 , devconf-2025-1 , devconf-2025-2 , etc. 5. AI Integration with Gemini Integrating Google's Gemini AI to provide context-aware responses about events required careful prompt engineering and database query optimization. 6. Full-Stack Type Safety Keeping DB models, server actions, and UI aligned required tight Zod + TypeScript integration. 🤖 AI Assistance Being a solo builder, I used AI assistance from Kiro to handle repetitive setup and styling work, which helped me allocate more time to design, logic, and performance. 🏆 What I Learned Building this solo taught me: Deep App Router + Server Component patterns Advanced session and JWT flows in NextAuth Integrating AI APIs (Google Gemini) for intelligent features Serverless database connection engineering Structuring a scalable Next.js monorepo-style architecture TypeScript best practices using shared schemas Designing UX intentionally for a developer audience The huge impact of validation + error handling on reliability This project heavily leveled up my full-stack engineering skills under real constraints. 🚀 What's Next v1.1 ✅ (Completed) ✅ AI chatbot assistant for event queries ✅ Favourite events system Full-text search + advanced filters Multiple login options (Google, GitHub, Facebook) + handling WebHooks Reminder emails Event capacity + waitlist v2.0 Smart event recommendations based on user history Comments and reviews system QR-based event check-ins Multi-image event galleries Ticketing + payments User profiles + following Public API Multi-language support v3.0 Mobile app for iOS + Android Community polls for trending events Advanced sorting: Most Attended, Fan Favourite, Cash Prize, etc. 🎛️ Long-Term Vision (Ambitious but achievable with support) 🤖 AI-Powered Attendee Dashboard A dedicated AI dashboard that: Analyzes user skills, interests, and project history Predicts ideal hackathons or meetups for them Scores events by difficulty, team size, prizes, relevance, personality, tech stack Learns user preferences over time with a lightweight ML model This shifts NexEvent from "event listing" → personalized dev event intelligence . 🗣️ Voice-Enabled Event Forms Text-to-speech + voice-based form filling Faster event creation Accessibility-friendly workflow 💬 Enhanced Chat-Based Event Assistant Expand current chatbot with multi-turn conversations Smart suggestions while browsing Instant event insights and comparisons Natural language event search 🎮 Gamification Layer XP for attending events Badges for categories (AI, Web, Cloud, Hardware, etc.) Seasonal leaderboards Event streaks and consistency rewards 🎯 Goal With proper support, NexEvent aims to grow from an MVP into a complete developer event ecosystem — combining clean UI, intelligent AI recommendations, voice assistance, and gamification to make tech event discovery genuinely fun and personalized. Built end-to-end by a solo developer, aiming to push the UX of developer events to the next level — powered by my favorite framework, Next.js. <div