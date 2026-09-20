---
slug: "vlml"
url: "https://devpost.com/software/vlml"
title: "VLML"
hackathon: "Sky’s the Limit - Cloud9 x JetBrains Hackathon"
organization: "Cloud9"
winner: true
words: 1255
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# VLML

> VLML turns raw Valorant match data into a fast, consistent analytics model and serves it through MCP so LLMs can generate explainable coaching insights

[Devpost](https://devpost.com/software/vlml) · hackathon [[Sky-s the Limit - Cloud9 x JetBrains Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[transportation]]
**user** [[developer]] [[frontline_worker]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** claude, duckdb, junie, mcp, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vlml

## Body

VLML: Building Moneyball for Valorant "It's about getting things down to one number. Using stats the way we read them, we'll find value in players that nobody else can see." — Peter Brand, Moneyball Inspiration This project is inspired by the work I've done internally as an analytics engineer. I've been experimenting with MCP (Model Context Protocol) as a way to let AI assistants understand business metrics in a structured way. The core insight is simple but powerful: Dashboards show numbers. AI explains them. A dashboard tile is static — it can't explain why something changed. But if the logic behind that tile is represented in a semantic layer, the AI can understand the metric definition, the filters, the join paths, and the meaning behind the numbers. This reduces hallucination and enables deeper exploration: break things down, compare time periods, find anomalies, explain drivers, and answer follow-up questions. My vision is to turn Claude into a complete AI assistant by connecting it directly to the database via MCP . No hallucinations. No made-up statistics. Just real data, queried in real-time, interpreted by a frontier AI that understands context. When Claude needs a number, it doesn't guess — it queries. When it makes a claim, it's backed by actual rows in a database. The same foundation unlocks multiple capabilities: semantic search, SQL generation, debugging helper, insight explainer. Sometimes you build something focused, and it ends up unlocking bigger possibilities. There's a scene in Moneyball that every data person remembers. Billy Beane is sitting across from his scouts, listening to them debate which players "look" like winners. Then Peter Brand walks in with a laptop and says something like: "The data says you're wrong. Here's who you should actually draft." That scene isn't about the laptop. It's not about the spreadsheet. It's about having someone who can translate raw numbers into decisions . When I saw the Cloud9 x JetBrains Hackathon and read the Category 1 prompt — "A Comprehensive Assistant Coach powered by Data Science and AI, inspired by Moneyball" — I knew exactly what I wanted to build. Not a dashboard. Not a custom AI model. I wanted to build the data foundation that lets a Peter Brand-level analyst work. And in 2025, the best Peter Brand available is Claude. What started as a "let's see what's in this data" weekend project during New Year's break turned into a full analytics modeling layer. Turns out, when you give an analytics engineer access to rich VCT event data and a long weekend, things escalate quickly. What it does VLML (Valorant Analytics Modeling Layer) is a structured data model for professional Valorant esports analytics that connects to frontier AI models via MCP. Moneyball VLML Baseball statistics VLML Analytics Model (DuckDB) Peter Brand Claude (via MCP) Billy Beane The Coach (user) The Architecture: Data Layer (VLML) : 21 analytics tables with 70+ pre-computed metrics at every grain — round, game, series, player, team. Opening duels, trade rates, KAST, clutch performance, economy patterns — everything a coach would want to ask about, already calculated. AI Layer (Claude via MCP) : Connected via Model Context Protocol, Claude can query the analytics model, reason over results, and have real conversations with coaches. Not just "here's a number" — but "here's what this number means for your next match." Coach Layer (User) : The decision-maker who asks questions, challenges analysis, and ultimately decides what to practice. Pre-computed Metrics Include: Category Metrics Opening Duels First bloods, first deaths, FB conversion rate Trading Trade kills, untraded deaths, trade window timing Impact Multi-kills (2k, 3k, 4k, ace), clutch attempts/wins Consistency KAST%, ADR, kill participation Economy Pistol win rate, eco rounds, thrifty conversions Splits Performance by agent, map, and side MCP Tools for AI Access: match_analysis_report — Post-match breakdown with VOD priority queue player_profile_report — Career stats, agent/map splits, clutch performance scouting_report — Pre-match opponent prep and tendencies pattern_detection_report — Recurring patterns across datasets query_sql — Ad-hoc SQL queries for deep analysis How I built it Tech Stack: DuckDB — Embedded columnar database optimized for analytical queries Python — Data pipeline orchestration and MCP server MCP (Model Context Protocol) — AI-to-data bridge for Claude and Junie GRID API — Official VCT esports data source Data Pipeline: GRID JSON → Download → JSONL → Load → Atomic Tables → Transform → Aggregation Tables The pipeline follows a layered architecture: Reference Layer — Lookup tables (agents, weapons, win probability factors) Atomic Layer — Raw events (series, games, rounds, base_events) Aggregated Layer — Pre-computed metrics at multiple grains Time-series Layer — Temporal aggregations (daily, tournament) Derived Layer — Pre-joined analytics tables for specific use cases Key Design Decisions: Denormalized for analytics : Dimension attributes repeated to avoid joins Pre-aggregated metrics : Computed during ingestion for instant queries Explainable metrics : Numerator/denominator outputs, not precomputed percentages For example, rather than storing a pre-calculated win rate, we store: $$\text{Win Rate} = \frac{\text{rounds_won}}{\text{rounds_played}}$$ This allows flexible aggregation and transparency in how metrics are derived. Challenges we ran into 1. Being Pragmatic About AI Early on, I had to decide: build a custom model or use what's already best? Fine-tuning a model = Teaching someone a new skill from scratch Connecting a model to the right data = Giving an expert the information they need Frontier models like Claude are trained on trillions of tokens with billions of dollars of compute. What they don't have is access to structured Valorant esports data. That's the gap I filled. 2. Making Metrics Coaching-Ready Raw events are noise. The challenge was identifying which 70+ metrics actually matter for coaching decisions and pre-computing them at the right grains for instant access. Accomplishments that we're proud of 1. Real Coaching Conversations The system doesn't just show stats — it identifies actionable insights. In testing, Claude flagged that "when OXY dies first, C9 loses 91.7% of their rounds." That's a coaching point that would normally take hours of VOD review to quantify. 2. Model-Agnostic Architecture Today it's Claude with MCP. Tomorrow it could be Gemini, GPT-5, or whatever leads the pack. The data layer is the foundation — the AI is interchangeable. 3. Multi-Surface Access The same data layer works with: Claude Desktop (conversational) JetBrains Junie (IDE-integrated) Any future MCP-compatible AI 4. Comprehensive Data Model 21 tables across 5 layers, with 70+ metrics covering every aspect of professional Valorant play — from micro-level kill sequences to macro-level economy cascades. What we learned The data model is the product. Anyone can call an API. Few can build the analytics schema that makes AI responses actually useful. Pre-compute everything. Coaches need answers, not 10 million rows to query. MCP is powerful — and portable. Connecting structured data to AI via MCP feels like magic, and it's an open standard. Conversation > Dashboard. The most valuable insights come from follow-up questions that emerge in dialogue: "Why did Round 8 go differently than Round 3?" "Is this a player problem or a team structure problem?" "What would you practice to fix this?" Be pragmatic about AI. Fine-tuning is expensive and gets outdated. Riding the frontier model wave is the smarter play. The right person still matters. Claude doesn't replace the coach — it augments them. The AI surfaces patterns; humans translate insights into practice drills and game plans. What's next for VLML Expand data access beyond VCT Americas to include Masters, Champions, Pacific, and EMEA Add real-time ingestion for live match analysis Build automated pre-match scouting report generation LookML-inspired semantic layer to reduce token usage and create a complete AI coaching tool <div