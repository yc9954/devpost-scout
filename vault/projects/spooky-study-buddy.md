---
slug: "spooky-study-buddy"
url: "https://devpost.com/software/spooky-study-buddy"
title: "Spooky Study Buddy"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 793
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Spooky Study Buddy

> Transform boring study materials into engaging Halloween-themed stories and interactive quizzes. AI-powered learning with spooky characters, gamification, and progress tracking. Makes studying fun!

[Devpost](https://devpost.com/software/spooky-study-buddy) · hackathon [[Kiroween]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** 1.5, actions, ai, api, css, css3, docker, eslint, express.js, flash, framer, gemini, git, github

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spooky study buddy

## Body

Inspiration As students ourselves, we've experienced the struggle of staying engaged with dry, technical study materials. We noticed that gamification and storytelling make learning stick, but existing EdTech solutions lack personality and fun. With Halloween approaching and the Kiroween Hackathon announced, we saw an opportunity to combine spooky aesthetics with serious learning outcomes. We wanted to prove that education doesn't have to be boring - it can be thrilling, memorable, and effective when wrapped in an engaging theme. What it does Spooky Study Buddy transforms any educational content into engaging Halloween-themed stories and interactive quizzes. Students upload study materials (text files, PDFs, or paste directly), and our AI generates a spooky narrative featuring animated Halloween characters - ghosts, vampires, witches, and skeletons - while preserving all key learning concepts. After reading the story, students take interactive quizzes hosted by these characters, receiving immediate feedback and explanations. The app tracks progress with gamification features including XP levels, achievement badges, learning streaks, and Halloween-themed metrics. It works instantly without any API key using Template Mode, or users can add their own OpenAI/Gemini API key for enhanced AI-powered stories. How we built it We leveraged Kiro AI Assistant for rapid, spec-driven development, creating comprehensive requirements, design docs, and task breakdowns before writing code. The frontend uses React 18 with TypeScript, Tailwind CSS for styling, and Framer Motion for smooth animations. We integrated three AI modes: Template Mode (no API key needed), OpenAI GPT-3.5/4, and Google Gemini 1.5 Flash for story generation. The backend runs on Node.js/Express with TypeScript, handling file uploads, content processing, and progress tracking. We implemented a complete gamification system with XP, levels, badges, and streaks. The app is deployed as a static site on GitHub Pages with automatic CI/CD. We achieved 90%+ test coverage using Vitest and Testing Library, ensuring production-ready quality. Challenges we ran into AI Integration Complexity: Implementing three different AI modes (Template, OpenAI, Gemini) with seamless fallbacks required careful architecture. We solved this by creating a unified service layer with mode detection and graceful degradation. GitHub Pages Routing: SPA routing caused 404 errors on page refresh. We fixed this with dynamic basename configuration and a 404.html redirect strategy. Performance Optimization: Large study materials caused slow generation times. We implemented chunking, caching, and progress indicators to maintain smooth UX. Gamification State Management: Syncing progress across components and persisting to backend required careful state management. We built a dedicated gamification service with optimistic updates. Animation Performance: Complex Halloween effects impacted mobile performance. We optimized with CSS transforms, reduced motion preferences, and lazy loading. Accomplishments that we're proud of ✨ Complete Full-Stack App in 5 Days: From concept to production-ready deployment with professional polish 🎨 Immersive Halloween Experience: 30+ animated components with consistent spooky aesthetic throughout 🤖 Flexible AI Integration: Three AI modes including a no-API-key Template Mode for instant use 📊 Comprehensive Gamification: Full XP system, badges, streaks, and progress tracking with backend persistence 🧪 90%+ Test Coverage: Production-quality code with extensive unit, integration, and E2E tests 🚀 Kiro AI Showcase: Demonstrated spec-driven development, saving 40+ hours (62% faster) with 8,000+ lines of generated code 📱 Cross-Platform Excellence: Responsive design working flawlessly on desktop, tablet, and mobile 🎯 Real Educational Value: Preserves learning concepts while making content memorable and engaging What we learned Spec-Driven Development Works: Using Kiro AI's spec system (requirements → design → tasks) dramatically accelerated development and maintained code quality. Breaking features into properties and tasks made complex features manageable. AI Fallbacks Are Essential: Not everyone has API keys, so Template Mode makes the app accessible immediately while still offering premium AI options. Gamification Drives Engagement: Even in a learning app, XP, badges, and streaks significantly increase user motivation and retention. Animation Performance Matters: Smooth 60fps animations require careful optimization - CSS transforms over JS, reduced motion support, and lazy loading are crucial. Testing Saves Time: Comprehensive tests caught bugs early and gave confidence to iterate quickly without breaking existing features. Theme Consistency Is Powerful: A cohesive Halloween aesthetic throughout the entire app creates a memorable, professional experience that stands out. What's next for Spooky Study Buddy 🎓 Multi-Subject Templates: Pre-built story templates for math, science, history, and languages 👥 Collaborative Learning: Share stories with classmates, compete on leaderboards, and study together 🎤 Voice Narration: Spooky character voices reading stories aloud for auditory learners 📚 Study Sets & Flashcards: Generate flashcard decks from stories for spaced repetition 🏆 Advanced Gamification: Guilds, tournaments, seasonal events, and rare collectible badges 🌍 Multi-Language Support: Translate stories and quizzes to reach global learners 📊 Teacher Dashboard: Analytics for educators to track student progress and assign content 🎨 Theme Customization: Unlock different seasonal themes (Christmas, Space, Fantasy) as rewards 💰 Freemium Model: Free tier with Template Mode, premium subscriptions for unlimited AI stories <div