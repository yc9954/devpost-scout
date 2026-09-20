---
slug: "death-dealer"
url: "https://devpost.com/software/death-dealer"
title: "Death Dealer"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 978
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Death Dealer

> "A dark, immersive Halloween experience where you make a fictional deal with the devil"

[Devpost](https://devpost.com/software/death-dealer) · hackathon [[Kiroween]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[document_pdf]] [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** apis:, framer, github, html, html5, javascript, localstorage, node.js, npm, react, tailwind, typescript, v4, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for death dealer

## Body

Landing Page Deal page (various fictional question) Confirmation for Soul Dealing (No back option) King of Hell Accept the contract and the fictional soul is now cursed Hell Ticket And countdown for his Punishment Inspiration Death Dealer was inspired by the desire to create an immersive, narrative-driven horror experience for Halloween. I wanted to explore what a "deal with the devil" would look like if it had a modern user interface—combining dark web aesthetics, gothic horror, and interactive storytelling. The Kiroween contest provided the perfect opportunity to push creative boundaries and experiment with atmospheric web design while leveraging AI-assisted development with Kiro. What it does Death Dealer is a fictional Halloween horror web application that takes users through a four-stage journey: Landing Portal - A creepy entrance with graveyard atmosphere, horror music, and glitchy title effects Devil's Interrogation - A 5-step form where users "register a soul" by answering questions about a fictional person (name, age, crime, location) Underworld Transition - A dramatic video showing the gates of hell opening Hell Ticket - The final contract display with a live countdown timer (6:66 minutes), random eternal punishment, and a Soul Ledger showing the last 5 deals stored in localStorage The entire experience features custom skull cursors, glitch text effects, Framer Motion animations, and a cohesive horror aesthetic. It's purely fictional and designed for entertainment—no real data leaves the user's browser. How we built it Tech Stack: React 19 + TypeScript for type-safe component architecture Vite for lightning-fast development and optimized builds Tailwind CSS v4 with custom horror theme (blood-red, neon-green, deep-black palette) Framer Motion for smooth animations and transitions localStorage for Soul Ledger persistence Development Process: Set up project structure with Vite and configured Tailwind with custom CSS variables Built component hierarchy: App → LandingPage → DealFlow → HellGateTransition → ResultScreen Implemented centralized audio control in App.tsx for music playback timing Created reusable GlitchText component with three intensity levels Added multi-step form with validation, slide transitions, and Enter key support Integrated video transition with loading states and skip functionality Implemented countdown timer with localStorage-based Soul Ledger Optimized assets (compressed 9.6MB video to 2.8MB) for Vercel deployment Key Technical Decisions: View-based state management ('landing' | 'deal' | 'gate' | 'result') Centralized audio control to manage music lifecycle Custom theme using CSS variables for consistent horror aesthetic Component-based architecture with clear separation of concerns Challenges we ran into Video Performance on Deployment The original 9.6MB video caused severe buffering on Vercel. Solution: Compressed using ffmpeg with H.264 codec, added preload="auto" and -movflags +faststart for streaming, implemented loading spinner, reduced file size by 70%. Browser Autoplay Policies Music wouldn't play automatically due to browser restrictions. Solution: Moved audio control to parent component, triggered playback on user interaction (button click), stopped music on form submission using refs. Form State Management Managing 5 steps with validation and animations was complex. Solution: Created step configuration array, used single state object for form data, implemented slide transitions with Framer Motion, added Enter key support. Glitch Effect Balance Creating authentic glitch effects without being distracting. Solution: Built reusable component with three intensity levels, subtle x-offset/skew/opacity variations, continuous loop with easeInOut timing. Asset Optimization Large files (1.6MB PNG, 9.6MB video) caused slow loading. Solution: Compressed all assets, added loading states, implemented proper caching headers, optimized build configuration. Accomplishments that we're proud of Immersive Atmosphere - Successfully created a cohesive horror experience where every detail (cursors, colors, animations, music) contributes to the narrative Smooth User Experience - Despite the dark theme, the UX is polished with loading states, skip functionality, keyboard shortcuts, and clear feedback Performance Optimization - Reduced total page size from ~15MB to ~5MB while maintaining visual quality Reusable Components - Built clean, type-safe components like GlitchText that can be used across the app AI-Assisted Development - Leveraged Kiro AI effectively to handle implementation details while focusing on creative direction Complete Documentation - Created comprehensive README, technical spec, and deployment optimization guide Production Ready - Successfully deployed to Vercel with proper error handling and fallbacks What we learned Technical Skills: Advanced Framer Motion animations with complex timing and sequencing Video optimization techniques and streaming best practices State management patterns for multi-view applications TypeScript best practices for component architecture Performance optimization for web deployment localStorage integration for persistent data Design Skills: Horror UI/UX design principles (balancing atmosphere with usability) Creating narrative-driven interfaces where UI tells a story Sound design integration for immersive experiences Custom cursor implementation for thematic consistency AI Collaboration: How to effectively communicate design requirements to AI Iterative refinement through conversation Rapid prototyping and experimentation The power of AI for handling implementation while focusing on creative vision Key Insight: Atmosphere is everything in immersive experiences. Every animation, color choice, and sound contributes to the feeling of entering a forbidden realm. The combination of human creativity and AI implementation can create polished experiences far faster than traditional development. What's next for Death Dealer Short-term Enhancements: Add sound effects for button clicks and transitions Implement multiple punishment variations with branching logic Create achievement system for multiple deals Add social sharing (without personal data) Medium-term Features: Multiple endings based on user choices Additional transition animations between screens Localization for multi-language support Backend integration for optional leaderboard (fictional contracts only) Mobile app version with native animations Long-term Vision: Expand into a series of "dark web" themed experiences Create a narrative universe with interconnected stories Add procedurally generated content for unique experiences Implement WebGL effects for more advanced visuals Build a community platform for sharing fictional contracts Technical Improvements: Migrate to Next.js for better SEO and performance Add PWA support for offline functionality Implement WebRTC for multiplayer "deals" Create admin dashboard for content management Add analytics to understand user behavior and optimize flow The ultimate goal is to evolve Death Dealer into a platform for immersive, narrative-driven horror experiences that push the boundaries of what's possible with web technology. <div