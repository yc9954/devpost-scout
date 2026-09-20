---
slug: "flowstate-7ihg10"
url: "https://devpost.com/software/flowstate-7ihg10"
title: "Donair"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 929
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Donair

> Instant Agentic Crowdfunding

[Devpost](https://devpost.com/software/flowstate-7ihg10) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[finance_payments]] [[housing_homeless]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** embeddings, gemini, rag, react, sql, supabase, typescript

## How they structured the write-up

- 🧐 inspiration
- 🤯 what it does
- 💭 how it works:
- 👷‍♂️ how we built it
- key technical challenges:
- architecture highlights:
- deployment:

## Body

Landing page Dashboard Kanban board layout for lead tracking Donation Screen Instant Solana Payment Donair - Instant agentic crowdfunding 🧐 Inspiration Event-based fundraising is slow. You need big-ticket sponsors and manual donor profile research. We built Donair to make that process agentic, instantaneous, and versatile. Simply describe your event: Donair identifies high-potential supporters, enables rapid micro- to macro-scale transactions, and builds hype through real-time rewards. 🤯 What it does Donair is an agentic platform that transforms each fundraising, donation matching, and event planning on any scale. Before your event Tell Donair about your event, fundraising goal, and donation incentives Sit back as Donair identifies key target donors personalized to your mission During your event Hit Live Watch Donair seamlessly sets up a portal for rapid transactions in any currency and amount Enjoy audience engagement through live incentive trackers After your event Assess analytics across events Do it all over again (since Donair raised tons of money for you!) 💭 How it works: AI-Powered Donor Discovery Donair uses Google Gemini AI with vector embeddings to semantically match your event description against a database of >110,000 historical publicly-available philanthropic donations sourced from CharityCAN and Indiana University. The system generates embeddings from your event description, then performs Retrieval-Augmented-Generation (RAG) using vector similarity search in Supabase, along with web search for the latest results, to find recipients with aligned missions. From there, it identifies donors who have previously supported similar causes, filtering by capacity (gift size relative to your goal) and geographic relevance. Intelligent Agent Chat An interactive AI agent powered by Gemini 2.5 Flash acts as your fundraising assistant. It can: Search your historical donor database using semantic matching Perform web searches to discover new prospects Extract donor information from news articles and public sources Generate AI insights (capacity, affinity, timeliness scores) for each lead Research specific donors and provide detailed analysis All three scores are normalized to 0–100 and clamped to ensure valid ranges. They’re combined using weighted averaging: capacity and affinity each contribute 40%, timeliness contributes 20%, reflecting that financial ability and cause alignment matter more than timing. A timeliness score ≥80 adds a +10 bonus to the final relevance score, then the result is normalized to a 0–0.99 scale for database storage. The weighting prioritizes donors who can give and care about the cause, with timeliness as a tie-breaker for immediate opportunities. Real-Time Payment Processing During live events, Donair integrates with Solana Pay to enable instant donations. The platform: Generates QR codes for quick mobile donations Monitors Solana blockchain transactions in real-time via WebSocket connections Displays live donation feed with instant updates Supports major currencies with automatic conversion Tracks offline donations for comprehensive analytics Lead Management & Analytics A Kanban-style board helps you manage leads through the pipeline (Discovered → Contacted → Negotiating → Confirmed). Each lead includes: AI-generated relevance scores (capacity, affinity, timeliness) Contact information extracted from web sources Ethics flags (GREEN/YELLOW/RED) for risk assessment Real-time monitoring signals (awards, appointments, business success) Historical giving patterns and alignment analysis News Monitoring & Intelligence Automated scanning discovers new opportunities by: Monitoring news for awards, board appointments, and business milestones Tracking existing leads for capacity signals (IPOs, promotions) Identifying philanthropic activity and grant announcements Providing actionable suggestions for outreach 👷‍♂️ How we built it Frontend: Next.js 16 + React 19 TypeScript Tailwind CSS 4 Supabase Client - Real-time subscriptions for live updates, authentication, and database queries Google Gemini AI Integration : gemini-2.0-flash-exp for donor matching and SQL generation gemini-2.5-flash for agent chat with tool calling (web search, database queries) text-embedding-004 for semantic vector search Solana Pay Integration : @solana/pay for generating payment URLs and QR codes @solana/web3.js for blockchain connection and transaction monitoring WebSocket listeners for real-time transaction detection on Solana mainnet Recharts - Data visualization for analytics dashboards and fundraising progress React Context API - State management for authentication and notifications Backend: Express.js Server - RESTful API endpoints for donor queries and data processing PostgreSQL (Supabase) - Relational database with: Vector similarity search using pgvector extension Row Level Security (RLS) policies for multi-tenant data isolation Real-time subscriptions via Supabase Realtime Custom RPC functions for semantic matching ( match_recipients ) CSV Import Pipeline - Batch processing of historical donation data with indexing for fast queries Google Gemini API - AI-powered features: Embedding generation for semantic search Natural language understanding for event descriptions Structured data extraction from web search results Multi-dimensional scoring (capacity, affinity, timeliness, ethics) Key Technical Challenges: Vector Search Optimization - Implemented cosine similarity search with configurable thresholds (0.3) to balance recall and precision. Used Supabase RPC functions to efficiently query embeddings. Real-Time Transaction Monitoring - Built WebSocket connection to Solana mainnet to listen for on-chain transactions. Handles connection failures gracefully with fallback demo mode. AI Agent Tool Calling - Designed a flexible tool system where Gemini can call functions like find_similar_recipients , search_web , get_event_leads , and save_lead . Structured prompts ensure the agent only creates leads when explicitly requested. Multi-Currency Support - Implemented SOL-based conversion using current exchange rates, allowing users to think in dollars with Solana's rapid crypto payments. Lead Deduplication - Smart matching algorithm prevents duplicate leads by comparing names and checking existing database entries before insertion. Architecture Highlights: Serverless API Routes - Next.js API routes handle all backend logic, eliminating need for separate deployment Real-Time Updates - Supabase Realtime channels provide instant updates for donations, lead status changes, and event status Progressive Enhancement - Works offline with cached data, gracefully degrades when WebSocket connections fail Deployment: Frontend deployed on Vercel Supabase handles database, authentication, and real-time infrastructure Solana mainnet integration requires no additional infrastructure <div