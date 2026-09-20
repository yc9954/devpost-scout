---
slug: "polymarket-red1j0"
url: "https://devpost.com/software/polymarket-red1j0"
title: "Roly Poly"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 886
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Roly Poly

> An interactive educational sandbox that teaches users how prediction markets work through beautiful 3D visualizations and real Polymarket data!

[Devpost](https://devpost.com/software/polymarket-red1j0) · hackathon [[NexHacks]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[labor_employment]] [[transportation]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]]

**stack** arize, devswarm, docker, elevenlabs, fastapi, polyrouter, postgresql, python, react, twilio, typescript, vite, woodwide

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- how we built it
- what's next for roly poly!!

## Body

Home Sims Poly Inspiration Prediction markets like Polymarket are powerful tools for understanding real-world probabilities, but they're intimidating to newcomers. When users see prices like "$0.65 for YES," they don't understand what that means for their risk, potential profit, or why position sizing matters. The learning curve is steep, the math is hidden, and most people give up before they "get it." We were inspired by the gap between the potential of prediction markets and their accessibility. We saw that people wanted to understand these markets but were overwhelmed by the complexity. Our inspiration came from asking: What if we could make prediction markets as intuitive as playing with a 3D model? What if users could see, in real-time, how their beliefs and decisions affect outcomes, without any financial risk? We built Roly Poly to bridge that gap: turning abstract probabilities into something you can see, touch, and understand. What it does Roly Poly is an interactive educational tool that makes prediction markets intuitive through 3D visualization and AI-powered explanations. Here's what users can do: Explore Real Markets : Browse live Polymarket data with a beautiful, trading-style dashboard Interactive Sandbox : Enter a 3D visualization environment where users adjust parameters with sliders: Real-Time Visualization : Watch a 3D risk cube update instantly as you move sliders, showing: Expected value calculations Maximum gain and loss scenarios Risk surface across different outcomes Payoff curves and scenario trees AI-Powered Learning : Get instant explanations that answer: What happened? When you change a parameter Why does it matter? The implications of your choices Backend Architecture API Framework : FastAPI for high-performance async endpoints Database : Supabase (PostgreSQL) for market data caching External APIs : Polymarket Gamma API for market metadata and search Polymarket CLOB API for live pricing and order book data WebSocket connections for real-time price updates Sponsor Integrations We integrated four sponsor technologies to enhance the app: Arize Phoenix : LLM tracing and evaluation to monitor explanation quality and track performance Token Company : Context compression to reduce prompt sizes by 40%+ and cut API costs Wood Wide AI : Numeric reasoning engine for market recommendations and scoring logic DevSwarm : Agent orchestration for multi-agent workflows and reasoning visualization Sponsor Development: DevSwarm/Gemini Parallel Coding We used 4 specialised Gemini agents running in parallel as a "DevSwarm" for rapid development: │ Agent │ Role │ │ arize-phoenix│ Phoenix tracing, LLM-as-Judge evaluators, metrics & annotations │ token-company │ FastAPI endpoints, Polymarket integration, business logic, agent orchestration │ ui-polish │ Layout, styling, animations, responsive design, accessibility │ demo-ready │ End-to-end verification, bug fixes only, merge coordination Branch Strategy: Each agent operated on its own feature branch (backend-core, ui-polish, etc.) with coordinated merges to main. Execution Flow: Phase 1: token-company (parallel integrations) Phase 2: arize-phoenix (parallel integrations) Phase 3: ui-polish (styling with stable backend) Phase 4: demo-ready (final verification) This parallel approach allowed us to develop backend APIs, integrate sponsor technologies, polish the UI, and verify demo-readiness simultaneously and maximizing the 22-hour hackathon constraint. Gemini powers two core features: Primary AI Engine - Gemini 2.0 Flash Lite (google/gemini-2.0-flash-lite-001) via OpenRouter Generates educational market explanations Provides research-based probability analysis Powers the Avatar service for interactive learning LLM-as-Judge Evaluator - Gemini 1.5 Flash via direct API Evaluates explanation quality for Arize Phoenix Scores on 4 criteria: completeness, accuracy, clarity, actionability Enables automated quality monitoring Deployment Frontend : Railway with Railpack for static site hosting and FastAPI deployment Challenges we ran into Challenge : Polymarket APIs have strict rate limits, and we needed to fetch market data, prices, and order books without hitting limits or causing slow responses. Solution : Cache Gamma API responses for 5-15 minutes (metadata changes slowly) Cache CLOB orderbook data for 2-10 seconds (prices change frequently) Exponential backoff retry logic for failed requests Accomplishments that we're proud of We're proud of how smooth and responsive the 3D visualization feels. Users can drag sliders and see immediate, fluid updates across all visualizations without any lag. This required careful optimization, and our app was performant even with complex calculations. The AI explanations are genuinely helpful. Users can understand complex concepts like expected value, implied probability, and position sizing through clear, contextual explanations that adapt to their current view. We're proud that the app actually teaches, not just displays data. │ - +147% average quality improvement via Phoenix feedback loop │ - -79% failure rate reduction through automated experimentation │ - 40-60% token compression while preserving explanation quality │ - Real-time 3D visualization of complex financial risk surfaces │ - <500ms end-to-end latency for complete AI analysis pipeline How we built it Framework : Vite 7 + React 19 + TypeScript for fast development and type safety Styling : Tailwind CSS 4 with Framer Motion for smooth animations ## What we learned Rendering complex 3D scenes in the browser requires understanding WebGL, React Three Fiber's rendering pipeline, and when to use Web Workers for heavy computations. Working with multiple integrations had many difficulties and required a lot of testing and technical document reading. What's next for Roly Poly!! User Accounts : Save favorite markets, track learning progress, personalized recommendations More Market Categories : Expand beyond current categories to include sports, politics, crypto, and more Mobile Optimization : Responsive design improvements for tablet and mobile devices Tutorial Mode : Guided walkthrough for first-time users <div