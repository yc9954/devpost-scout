---
slug: "my-et-economic-times-reimagined"
url: "https://devpost.com/software/my-et-economic-times-reimagined"
title: "My ET - Economic Times Reimagined"
hackathon: "Hackonomics 2026"
organization: "hackonomics"
winner: true
words: 1309
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/media_journalism"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/government_staff"
  - "user/researcher"
  - "user/small_business"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# My ET - Economic Times Reimagined

> AI-powered financial news assistant that translates complex articles into any language, verifies facts to stop fake news. Making financial knowledge accessible to everyone

[Devpost](https://devpost.com/software/my-et-economic-times-reimagined) · hackathon [[Hackonomics 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[vision_ocr]]
**domain** [[agriculture_food]] [[developer_tools]] [[education]] [[finance_payments]] [[media_journalism]] [[transportation]]
**user** [[developer]] [[educator_student]] [[frontline_worker]] [[general_public]] [[government_staff]] [[researcher]] [[small_business]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** agentic-ai, apify, google-cloud, langchain, langgraph, mapbox, mem0, nextjs, openai, postgresql, tavily

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for my et
- - ai news agents : autonomous agents that monitor your watchlist 24/7 and alert on critical changes

## Body

The Impact of Any News on Stock Market along with Stock Charts Flashcards to Better Understand any article Agentic Setup A Quick Story View of the Article Customized Articles and Sections brought to you Personalized News Dashboard with Generative UI - Search Engine Podcast Episode Created on Single Article Landing Page for the New ET Single Article in Multiple Languages with Regional Context AI Studio + Contextual Memory Based Chat Window Global Geopolitical Economic News at One Map System Architecture My ET: Your Personal Financial News Assistant Inspiration We noticed three big problems regular people face when trying to understand financial news: Too Much Information, Too Little Time : A small business owner has to read 8+ articles and spend 2+ hours just to understand how a new policy affects their business. Important information gets buried in long articles with complicated words. Language Barriers : Many people can't access financial news because it's only available in English. This locks out millions of people from learning how to grow their money and make smart financial decisions. Fake News Spreads Fast : Last month, a fake message claiming a major bank was going bankrupt went viral on social media. Thousands of people panicked and made bad financial decisions. Fake news spreads faster than real news, and people lose money because of it. We asked ourselves: What if reading financial news was as easy as talking to a friend who explains everything simply? What it does My ET transforms The Economic Times from a passive newspaper into an Active Financial Intelligence Operating System. Think of it as having a personal financial analyst, translator, fact-checker, and market strategist in your pocket. Generative UI Search Engine (Not Just Links!) Traditional search gives you 10 blue links. We give you intelligent dashboards : Query: "How is Tata Motors performing?" You get: Live stock price, real-time 7-day chart (Yahoo Finance API), AI-synthesized analysis from multiple articles, bull vs bear arguments, and affected sectors—all in one interactive view. Multi-Agent Pipeline : Query routing → Parallel data fetch (Yahoo Finance + Tavily News) → Grounded AI synthesis Zero hallucination : Stock prices are NEVER AI-generated; pulled directly from Yahoo Finance API Geopolitical Globe (Visual Intelligence) A 3D interactive globe that maps how local news impacts global markets: Middle East tensions? Instantly see impact on Indian oil stocks US Fed rate changes? View ripple effects across sectors Built with custom SVG mapping + Framer Motion for professional-grade visualization 🇮🇳 Vernacular Financial Inclusion (The "Next Billion") One-click translation into 10+ Indian languages—but NOT literal translation: Powered by GPT-4o-mini + Sarvam AI for cultural context "Bull market" becomes relatable regional metaphors Makes elite finance accessible to rural India Supports: Hindi, Marathi, Telugu, Tamil, Bengali, Kannada, Malayalam, Gujarati, Punjabi, Odia Truth Engine (Misinformation Defense) Upload a WhatsApp forward or screenshot → AI verifies if it's real or fake: Gemini 1.5 Pro Vision analyzes images Tavily Search cross-references against ET archives, SEBI filings, RBI announcements Returns "True/False/Misleading" verdict with clickable citations Real impact : Prevents wealth destruction from financial scams AI Studio (9 Intelligence Tools on Every Article) Executive Brief : 30-second summary tailored to YOUR persona (Founder/Investor/Student) Bull vs Bear Analysis : Multi-agent debate showing 3 growth drivers + 3 risk factors Story Arc Tracker : Interactive timeline mapping past → present → future predictions Context Engine : Hover over jargon, get instant definitions (HoverCards) 3D Flashcards : Interactive flip-cards for mastering financial concepts (UPSC/MBA ready) Contrarian View : "Devil's advocate" analysis challenging mainstream narratives Podcast Daily : 2-person conversational audio briefing for commuters Video Brief : 60-second TikTok-style news scripts with visual cues Impact Score : Numerical market impact validated by live 1-day stock sparklines Smart Dashboard (Personalized Command Center) Market Pulse Ticker : Live Nifty 50, Sensex prices with color-coded sparklines Daily Digest : AI scans your watchlist every morning, creates 3-bullet strategic briefing Category AI Dashboard : News filtered by your sector (Finance/Law/Startup/Student) Trending Radar : Real-time trending topics with sentiment analysis ⚡ Performance Innovation SHA-256 Caching : Repeat queries drop from 8 seconds to <40ms Cached in Neon Postgres using content-hash keys Professional-grade "snappy" terminal feel How we built it Tech Stack Frontend : Next.js 16 (App Router), Tailwind CSS v4, Shadcn UI, Framer Motion AI Models : GPT-4o-mini (reasoning, synthesis) Gemini 1.5 Pro (vision, misinformation detection) Sarvam AI (vernacular TTS + cultural translation) Real-Time Data : Yahoo Finance API (live stock prices, historical charts) Search & Verification : Tavily API (news aggregation, fact-checking) Database : Neon Postgres + Drizzle ORM (user profiles, caching) Authentication : Clerk (secure user personas) Visualization : Recharts (interactive stock charts, sparklines) Multi-Agent Architecture We built a sophisticated agent pipeline: Router Agent : Analyzes user query intent (stock lookup vs news synthesis vs fact-check) Data Agents : Parallel fetch from Yahoo Finance + Tavily (reduces latency) Synthesis Agent : Grounds AI responses with real data to prevent hallucinations Persona Agent : Customizes output based on user profile (stored in Neon) Key Technical Innovations Deterministic Data Guardrails : Never let AI make up stock prices Content-Hash Caching : SHA-256 hash of (query + tool_id) = instant cache retrieval Hybrid Translation : GPT for semantic accuracy + Sarvam for Indic linguistic nuances Real-Time Sparklines : SVG-based Recharts with 5-minute interval data points Challenges we ran into 1. AI Hallucination Crisis : Early versions generated fake stock prices. Solution: Implemented strict data guardrails—prices are ONLY from Yahoo Finance API, never AI-generated. 2. Translation Quality : Literal Hindi translations of "Bull Run" made no cultural sense. Solution: Built hybrid GPT + Sarvam AI pipeline that replaces Western metaphors with regional equivalents. 3. Performance Bottleneck : Initial AI searches took 8-12 seconds. Solution: SHA-256 caching system in Neon Postgres brought repeat queries to <40ms. 4. Misinformation Detection Accuracy : Vision models struggled with low-quality WhatsApp screenshots. Solution: Enhanced preprocessing + Tavily cross-reference against multiple authoritative sources (SEBI, RBI, ET archives). 5. Real-Time Data Integration : Yahoo Finance API rate limits. Solution: Intelligent caching + batch requests for watchlist updates. Accomplishments that we're proud of Zero Hallucination Guarantee : Professional-grade data integrity you can trade on Democratizing Finance : Making elite knowledge accessible to 600M+ rural Indians 4x Engagement : Interactive modules increase user session time from 3 minutes to 12+ minutes 40ms Response Time : Enterprise-grade performance on consumer hardware Misinformation Shield : Potentially saving crores by preventing fake news panics Technical Innovation : Multi-agent pipeline with parallel data fetching + grounded synthesis What we learned AI is only as good as its data : The most powerful LLM is useless if it's making up numbers. Real-time API integrations are non-negotiable for financial apps. Cultural context > Translation accuracy : Rural users don't want literal translations—they want explanations that fit THEIR world. "Bull market" means nothing to a farmer; "harvest season profits" does. Caching is UX magic : Users don't care about your AI costs; they want instant results. SHA-256 caching transformed our app from "slow" to "snappy." Misinformation is a technical problem : You can't fact-check with better journalism alone—you need multi-source verification, vision AI, and authoritative databases. Personalization drives retention : Generic news feeds are dead. Users stay when the platform understands THEIR portfolio, THEIR sector, THEIR language. What's next for My ET Immediate Roadmap (Next 3 Months) Portfolio Integration : Connect user bank/Demat accounts (via MCP) for ultra-personalized alerts Predictive Intelligence : Train models on ET's 40+ year archives to predict market trends Social Features : Let analysts share custom AI briefings with teams Mobile App : Voice-first interface for rural users Long-Term Vision Regional Expansion : Expand to 22 Indian languages + voice-based interfaces API for Developers : Let fintech startups build on our intelligence layer Corporate Tier : Geopolitical risk dashboards for enterprises (subscription model) - AI News Agents : Autonomous agents that monitor your watchlist 24/7 and alert on critical changes <div