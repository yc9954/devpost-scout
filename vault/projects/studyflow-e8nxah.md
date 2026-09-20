---
slug: "studyflow-e8nxah"
url: "https://devpost.com/software/studyflow-e8nxah"
title: "StudyFlow"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 1090
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# StudyFlow

> AI-powered learning companion that creates structured learning paths with live web research, curated resources, and citation-backed answers

[Devpost](https://devpost.com/software/studyflow-e8nxah) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]] [[general_public]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** react, tailwind, typescript, you.com, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for studyflow

## Body

StudyFlow welcome page Creating a Learning Path A complete course with free resource and AI assistant (1) A complete course with free resource and AI assistant (2) Inspiration Learning new technical topics often feels overwhelming. You start with a Google search, open 20 tabs, get lost in rabbit holes, and struggle to distinguish quality resources from noise. I wanted to solve this for myself and other developers who constantly need to learn new technologies. The breaking point came when trying to learn React Server Components—I found myself searching the same questions repeatedly, losing track of articles I'd read, and not knowing if I was following a logical learning path. What if an AI could do the research, organize the learning path, and remember everything I learned? That's how StudyFlow was born. What it does StudyFlow transforms any topic into a structured, personalized learning experience: Smart Learning Paths : Enter any topic and AI breaks it into 3-5 progressive sub-modules (Fundamentals → Intermediate → Advanced), each with curated resources Dual Learning Modes : Deep Explanation - Rich content with superscript citations, code examples, and mathematical notation for comprehensive understanding Media Resources - Curated video tutorials from YouTube and educational platforms, separated from articles for visual learners Context-Aware Q&A Tutor : Study Assistant sidebar maintains conversation per module, answering questions with citations from module-specific resources Integrated Resource Viewing : Click any article to read clean content or watch videos without leaving the app Persistent Sessions : All learning paths and conversations saved locally to continue learning anytime How we built it Frontend Stack: React 18 + TypeScript + Vite for fast, type-safe development Zustand for state management with localStorage persistence Tailwind CSS + shadcn/ui for beautiful, accessible components Framer Motion for smooth animations react-katex for LaTeX math rendering You.com API Integration: Search API : Finding high-quality learning resources with citations Agents API : Two-stage orchestration - first generates module structure, then populates each module with resources in parallel Contents API : Extracting clean article content for in-app reading Key Technical Implementations: Two-Stage Learning Path Orchestration : Stage 1: LLM analyzes topic and generates 3-5 structured sub-modules with optimized search queries Stage 2: Parallel Search API calls populate each module with articles and videos Result: Serialized, progressive learning path instead of flat search results Intelligent Video Detection : URL pattern matching for YouTube/Vimeo Dual Search API strategy: general query + video-focused query per module oEmbed enrichment for thumbnails, duration, channel metadata Dedicated Media Resources grid separating videos from articles Context-Aware Q&A System : Tutor agent receives module content, available resources, and conversation history Answers reference specific module content and cite from module resources Separate conversation threads per module with persistence Superscript Citation System : Citations rendered as superscript numbers (¹²³) in Deep Explanation content Clickable citations scroll to Key Citations sidebar Citation metadata pulled from You.com Search API results Smart State Management : Separated ephemeral UI state from persistent data Module conversations persist per learning path Auto-saving with optimistic UI updates Challenges we ran into Orchestrating Parallel API Calls : Fetching resources for 5 modules simultaneously required using Promise.allSettled for resilience—one module's failure shouldn't break the entire learning path. Implemented graceful degradation with error states per module. Parsing LLM-Generated Module Structures : The agent returns free-form JSON that needed validation. Built a flexible parser with retry logic, JSON fence stripping, and schema validation while gracefully handling imperfect responses. Video Content Discovery : Standard searches don't surface enough videos. Solved by running two Search API calls per module—one general, one video-focused—then deduplicating and filtering by URL patterns. Context Management for Q&A : The tutor needs to know current module content without overwhelming the prompt. Implemented smart context windowing: module description + first 800 chars of content + last 4 conversation messages + available resources list. Citation Rendering Complexity : Making superscript citations (¹²³) clickable while preserving all markdown features required custom react-markdown components that intercept rendering, detect citation patterns, and inject click handlers without breaking code blocks or math rendering. Module Navigation UX : Horizontal scrolling cards needed to auto-scroll active module into view, handle touch interactions on mobile, and visually distinguish active/inactive states without being overwhelming. Accomplishments that we're proud of ✅ Intelligent Module Generation : Instead of dumping search results, StudyFlow creates a thoughtful curriculum that progressively builds knowledge—showing deep understanding of pedagogical structure ✅ Video-First Learning Philosophy : Recognizing that visual learners need different content types, we built a dedicated Media Resources section that treats videos as first-class citizens, not afterthoughts ✅ Three-Column Architecture : Left (navigation), Center (content), Right (tutor)—information architecture that scales from simple topics to complex courses without feeling cluttered ✅ Transparent AI Orchestration : Users see "Analyzing topic structure" → "Finding best resources" instead of generic spinners—building trust through transparency ✅ Production-Quality Polish : Superscript citations, LaTeX rendering, syntax-highlighted code blocks, dark mode, keyboard shortcuts, responsive design—this feels like a real product, not a hackathon prototype ✅ Zero Backend MVP : Delivered full persistence, multi-module learning paths, and conversation history with just localStorage—proving complex apps don't need infrastructure to start What we learned Technical Deep Dives: Two-stage API orchestration patterns for complex workflows Promise.allSettled for resilient parallel operations Context windowing strategies for LLM prompts URL pattern matching and oEmbed protocols for video enrichment Custom markdown renderers with component interception UX Insights: Progressive module navigation reduces overwhelm—users tackle one section at a time Separating Deep Explanation from Media Resources respects different learning styles Context-aware Q&A feels magical when done right—users don't need to repeat themselves Horizontal module cards work better than vertical lists for showing progression Superscript citations (¹²³) are more elegant than inline brackets [1][2] Product Strategy: Two-stage orchestration creates better structure than one-shot generation Parallel API calls are worth the complexity—users get complete paths in 10-15 seconds Dedicated video handling signals quality—treating all resources equally is lazy Three-column layout works for this use case—left for navigation, center for learning, right for assistance What's next for StudyFlow Short-term Enhancements: Cloud sync with Supabase for cross-device access Progress tracking: checkmarks for completed modules, time-spent analytics Enhanced video features: timestamp notes, transcript search, "explain this section" Module completion quizzes generated from content Shareable learning paths with unique URLs Long-term Vision: Learning communities: find others studying the same topic, share notes Spaced repetition system: intelligent review reminders based on forgetting curves Learning analytics: insights into your learning patterns and knowledge gaps Adaptive difficulty: modules adjust based on quiz performance Multi-language support for global learners Mobile native apps with offline-first architecture API for developers to build on StudyFlow's learning infrastructure <div