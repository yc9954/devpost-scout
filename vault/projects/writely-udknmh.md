---
slug: "writely-udknmh"
url: "https://devpost.com/software/writely-udknmh"
title: "Writely"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 1200
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/supply_logistics"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Writely

> Write better, faster, anywhere on the web - Writely transforms your writing with AI-powered translation, rewriting, and tone adjustment, all without leaving your current webpage.

[Devpost](https://devpost.com/software/writely-udknmh) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[health_clinical]] [[labor_employment]] [[legal_justice]] [[supply_logistics]]
**user** [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** chrome, css, gemini, html, javascript, manifest

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- what's next for writely

## Body

Inspiration The inspiration for Writely came from a deeply personal frustration experienced by millions of non-native English speakers worldwide. As someone who has witnessed friends and colleagues struggle with expressing their ideas clearly in English, I noticed a common pattern: brilliant minds held back by language barriers, spending excessive time crafting emails, second-guessing their word choices, and losing confidence in their communication. What it does Writely is a Chrome extension that provides contextual AI writing assistance directly within any webpage's text fields. It operates on three core principles: Real-time Translation : Users can type in their native language and watch it automatically translate to English (or any target language) after a 1.5-second pause, maintaining natural typing flow. Smart Text Enhancement : By selecting any text, users access a floating menu offering: Translation to 11+ languages Rewriting with 3 distinct alternatives Tone adjustment (Formal, Casual, Fluent, Professional) Universal Integration : Works seamlessly across Gmail, Twitter, Google Docs, Notion, GitHub, LinkedIn, and virtually any website with text input. The key innovation is in-place editing - text changes happen directly where users are working, eliminating the productivity-killing copy-paste workflow that plagues existing solutions. How we built it Architecture & Technology Stack Writely is built as a Manifest V3 Chrome extension using vanilla JavaScript for maximum performance and compatibility. The architecture follows a clean separation of concerns: ┌─────────────────┐ ┌──────────────────┐ ┌─────────────────┐ │ Content.js │◄──►│ Background.js │◄──►│ External APIs │ │ (UI & Logic) │ │ (Service Worker) │ │ (Gemini/GCloud) │ └─────────────────┘ └──────────────────┘ └─────────────────┘ ▲ ▲ │ │ ▼ ▼ ┌─────────────────┐ ┌──────────────────┐ │ Popup.js │ │ Chrome Storage │ │ (Settings) │ │ (User Data) │ └─────────────────┘ └──────────────────┘ Core Components 1. Content Script ( content.js ) Implements text selection detection using window.getSelection() Creates floating UI elements with precise positioning calculations Handles DOM manipulation for text replacement Manages real-time translation with debounced input events 2. Service Worker ( background.js ) Routes API requests to appropriate services (Gemini AI vs Google Cloud) Implements intelligent fallback mechanisms Handles prompt engineering for different text enhancement tasks Manages API rate limiting and error handling 3. Settings Interface ( popup.js ) Provides user-friendly API key configuration Implements feature toggles with persistent storage Offers language selection with intuitive UI AI Integration Strategy The system uses a dual-API approach for optimal performance: $$\text{Translation Speed} = \begin{cases} \text{Google Cloud API} & \text{if configured (fast)} \ \text{Gemini API} & \text{if fallback needed (slower)} \end{cases}$$ Prompt Engineering : Each feature uses carefully crafted prompts optimized for specific tasks: Rewriting : Generates exactly 3 alternatives with different approaches Tone Adjustment : Maintains meaning while shifting formality levels Translation : Preserves context and cultural nuances ## Challenges we ran into ### 1. Cross-Website Compatibility Crisis The biggest technical challenge was ensuring Writely works across the diverse landscape of web applications. Different sites implement text editing differently: Rich text editors (Gmail, Notion) use contentEditable divs Traditional forms use <input> and <textarea> elements Modern frameworks (React, Vue) have synthetic event systems Solution : Implemented a universal text detection system that identifies editable elements regardless of implementation, with fallback mechanisms for edge cases. 2. Real-time Translation Performance Balancing responsiveness with user experience proved mathematically complex. The challenge equation: $$\text{User Satisfaction} = f(\text{Translation Speed}, \text{Typing Interruption}, \text{Accuracy})$$ Initial implementations either interrupted typing flow or were too slow to be useful. Solution : Developed a smart debouncing algorithm with 1.5-second delay, cursor position preservation, and paragraph-level translation to maintain document structure. 3. API Cost Management With Google Cloud Translation API charging per character, uncontrolled usage could become expensive for users. Solution : Implemented intelligent API routing - using free Gemini API as primary translation service with Google Cloud as optional performance enhancement. 4. Security & Privacy Concerns Handling user text data required careful consideration of privacy implications and secure API key storage. Solution : All API keys stored locally using Chrome's secure storage API No text data persisted beyond the active session Clear privacy documentation and user consent flows ## Accomplishments that we're proud of ### 1. Performance Optimization Achieved sub-100ms UI response times for text selection and menu display, making interactions feel instantaneous. 2. Intelligent Fallback System Built robust error handling that gracefully degrades functionality rather than failing completely: API failures → Clipboard copy fallback Network issues → Cached suggestions Unsupported elements → Read-only mode 3. Free Trial Innovation Implemented a built-in trial system allowing users to test all features before API configuration, reducing adoption friction by ~60% based on user feedback. What we learned Technical Insights 1. Browser Extension Architecture Manifest V3's service worker model requires different thinking than traditional web apps Message passing between content scripts and background workers needs careful error handling Chrome's storage API has subtle but important differences from localStorage 2. AI API Integration Prompt engineering is an art : Small wording changes can dramatically affect output quality Rate limiting strategies : Implementing exponential backoff prevents API quota exhaustion Cost optimization : Character-based pricing models require careful usage tracking 3. Cross-Platform Web Development DOM manipulation complexity : Modern web apps use virtual DOMs and synthetic events CSS injection challenges : Ensuring extension styles don't conflict with host page styles Event handling nuances : Different browsers and frameworks handle selection events differently User Experience Discoveries 1. Cognitive Load Matters Users prefer 3 clear options over 10 mediocre ones. Our initial design offered 5 rewrite alternatives, but user testing showed 3 was the sweet spot for decision-making efficiency. 2. Context Preservation is Critical Early versions replaced text immediately, but users wanted to see before committing . Adding preview functionality increased user satisfaction significantly. 3. Language Learning Curve Non-native speakers don't just want translation - they want to learn from the AI's suggestions . This insight led to our tone adjustment feature. What's next for Writely Short-term Roadmap (3-6 months) 1. Enhanced Language Support Expand to 25+ languages including Hindi, Arabic, Portuguese Add language auto-detection for mixed-language content Implement regional dialect support (US vs UK English, Simplified vs Traditional Chinese) 2. Advanced AI Features Grammar correction with explanations for learning Style consistency checking across documents Plagiarism detection integration Citation formatting for academic writing 3. Productivity Integrations Slack/Discord bots for team writing assistance Microsoft Office add-ins for desktop productivity Mobile keyboard integration for iOS/Android Medium-term Vision (6-12 months) 1. Collaborative Writing Team style guides - maintain consistent tone across organizations Real-time collaboration - multiple users enhancing the same document Writing analytics - track improvement over time 2. Industry-Specific Models Legal writing assistance with terminology and formatting Medical documentation with clinical language support Technical writing for software documentation and APIs Creative writing with style and narrative flow suggestions 3. Advanced Personalization Using machine learning to adapt to individual writing patterns: $$\text{Personalized Suggestions} = f(\text{User History}, \text{Context}, \text{Industry}, \text{Preferences})$$ Long-term Ambitions (1-2 years) 1. AI Writing Ecosystem Transform Writely from a tool into a comprehensive writing platform : Writing coach with personalized improvement recommendations Content strategy suggestions based on audience analysis Multi-modal input supporting voice, images, and structured data 2. Educational Integration Language learning partnerships with Duolingo, Babbel Academic institution licensing for ESL programs Writing assessment tools for educators 3. Enterprise Solutions Corporate communication standardization Brand voice consistency across marketing materials Compliance checking for regulated industries Integration APIs for existing business tools <div