---
slug: "debatemasterai"
url: "https://devpost.com/software/debatemasterai"
title: "DebateMaster-AI"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1103
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# DebateMaster-AI

> AI debate coach with real-time voice interaction and performance analytics

[Devpost](https://devpost.com/software/debatemasterai) · hackathon [[Kiroween]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[transcript_audio]]

**stack** css, framermotion, geminiapi, javascript, kiro, react18, tailwindcss, typescript, vite6

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for debatemasterai

## Body

Inspiration The inspiration for DebateMaster AI came from recognizing a fundamental gap in accessible debate practice. Traditional debate training requires coordinating schedules with human partners, joining organized clubs, and waiting days for feedback. We wanted to democratize debate education by creating an AI-powered platform that anyone could use anytime, anywhere. When we discovered Amazon Kiro and Google's Gemini Live API, we realized we could build something truly transformative—a voice-enabled AI debate coach that provides instant feedback and tracks progress over time. What it does DebateMaster AI is a real-time voice debate coaching application that transforms how people practice and improve their argumentation skills. Users engage in natural voice conversations with an AI opponent powered by Google's Gemini Live API, choosing between two distinct modes: Coach Mode for supportive learning and Fierce Mode for challenging practice. The application features real-time bidirectional audio streaming with WebGL-powered voice visualization that responds dynamically to audio levels. As users debate, the system transcribes the conversation in real-time with cascading visual effects. After each session, users receive comprehensive performance analysis across ten key metrics including vocabulary richness, argument clarity, persuasiveness, and adaptability. An innovative persona discovery feature analyzes debate patterns to identify user archetypes through interactive 3D character models. The system tracks persona evolution over time, showing how debate style and strengths develop with practice. Interactive charts display score trends, duration distributions, and activity heat maps that visualize practice consistency. How we built it We leveraged Amazon Kiro's spec-driven development system to structure the entire project into four major features: debatemaster-design (core application), persona-showcase (3D persona discovery), activity-view (analytics dashboard), and live-debate-ui-redesign (WebGL visualization). Each spec included detailed requirements, design documentation, and implementation tasks. The frontend is built with React 18 and TypeScript for type-safe component development, using Vite 6 for fast builds and Tailwind CSS for styling. We integrated Google Gemini API v0.21.0 for real-time voice interaction and implemented sophisticated audio processing using the Web Audio API at 16kHz input and 24kHz output with PCM format. Three custom steering rules in .kiro/steering/ automatically guided every Kiro interaction: product.md maintained product consistency, structure.md enforced code organization, and tech.md ensured technical standards. Five agent hooks automated quality control tasks including lint-on-save, npm-install-on-package-change, readme-update-check, unused-imports-scanner, and markdown-grammar-check. The architecture follows clean separation of concerns with 30+ React components, service classes for business logic (geminiLiveService, storageService, personaService), utility functions for shared functionality, and custom React hooks. All data persists locally in browser storage with no server-side requirements. Challenges we ran into Real-Time Audio Streaming : Implementing bidirectional audio streaming with proper synchronization and minimal latency proved challenging. We needed to handle microphone input, encode it to PCM format, stream it to Gemini Live API via WebSocket, receive audio responses, decode them, and play them back—all in real-time. We solved this by leveraging Web Audio API with ScriptProcessorNode for real-time processing and implementing efficient buffer management to maintain smooth conversation flow. Performance Optimization : Maintaining smooth WebGL voice visualization and animations across various devices without frame drops required careful optimization. We implemented performance monitoring utilities, optimized render cycles with React.memo and useMemo, added reduced motion support for accessibility, and used efficient animation techniques with Framer Motion. Complex State Management : Managing intricate application state across multiple views (Dashboard, DebateLive, SessionSummary, Activity, PersonaShowcase) with real-time updates was complex. We adopted a service layer pattern for business logic separation, used React hooks for component state, implemented callback patterns for child-to-parent communication, and centralized state management in App.tsx. TypeScript Strict Mode : Ensuring type safety with strict mode enabled and noUncheckedIndexedAccess required comprehensive type definitions. We defined detailed TypeScript interfaces in types.ts, added proper null checks throughout the codebase, and leveraged Kiro's steering rules to maintain type consistency automatically. Accomplishments that we're proud of We're incredibly proud of achieving 70% faster feature implementation compared to traditional development workflows through Amazon Kiro's integrated approach. The automated steering system maintained consistent code quality across the entire codebase and prevented architectural drift without manual oversight. Successfully implementing real-time voice interaction with natural conversation flow, including interruption handling, stands as a major technical achievement. The custom WebGL voice visualization that responds dynamically to audio levels creates an immersive experience that makes debates feel alive. The comprehensive analytics system with ten performance metrics calculated using custom algorithms provides users with actionable insights. The persona discovery feature with interactive 3D character models powered by Spline adds a unique gamification element that keeps users engaged. Most importantly, we created a fully functional application that genuinely solves the accessibility problem in debate practice. Anyone with a browser and a Gemini API key can now practice debating anytime, receive instant feedback, and track their improvement over time. What we learned We learned the transformative power of spec-driven development with Amazon Kiro. Structuring the project into well-defined specs with requirements, design documentation, and implementation tasks before coding began prevented scope creep and architectural inconsistencies. The automated steering rules ensured every component, service, and utility function followed consistent patterns without repeated instructions. Working with Google's Gemini Live API taught us the intricacies of real-time voice AI integration. We gained deep understanding of Web Audio API, PCM audio encoding/decoding, WebSocket communication, and buffer management. Implementing custom performance metrics algorithms enhanced our knowledge of natural language processing and debate quality assessment. We discovered the importance of performance optimization for real-time applications. Techniques like React.memo, useMemo, reduced motion support, and efficient animation strategies became essential for maintaining smooth user experiences across devices. The experience reinforced that great developer tools like Amazon Kiro don't just speed up development—they fundamentally improve code quality, consistency, and maintainability. Automated quality assurance caught issues immediately, comprehensive documentation was generated alongside code, and complex implementations were debugged and refactored while maintaining architectural consistency. What's next for DebateMasterAI We plan to expand DebateMaster AI with several exciting features. Multi-user debate rooms with real-time collaboration will enable users to practice with friends or join public debates. Advanced persona evolution with machine learning insights will provide deeper analysis of debate style development. Custom debate scenarios and topic libraries will offer structured learning paths for different skill levels and debate formats. Integration with additional speech recognition APIs will improve transcription accuracy and support multiple languages. Native mobile applications for iOS and Android will bring the debate coaching experience to smartphones, making practice even more accessible. A debate tournament mode with leaderboards will add competitive elements and community engagement. Export functionality for session transcripts and analytics will allow users to share their progress and review debates offline. We're also exploring partnerships with educational institutions to integrate DebateMaster AI into formal debate curricula, making high-quality debate coaching accessible to students worldwide. <div