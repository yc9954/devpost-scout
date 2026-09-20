---
slug: "poke-sdr"
url: "https://devpost.com/software/poke-sdr"
title: "Poke SDR"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1076
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Poke SDR

> AI sales assistant you text like a coworker. 6 MCP tools handle enrichment, emails, and actions. Lava's multi-model routing cuts costs 80% - proving AI SaaS can be profitable from day 1.

[Devpost](https://devpost.com/software/poke-sdr) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
  <sub>weak: finance_payments</sub>
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** fastmcp, github, langchain, lavapayments, ngrok, openai, poke, python, react18, render, sqlite, tailwind, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for poke sdr

## Body

Detailed breakdown of endpoint performance and model utilization, providing insights into cost efficiency and API demand. Comprehensive view of user analytics, showcasing real-time activity trends, total usage over time, and customer engagement metrics. Live chat demo with Poke SDR using six MCP integrations — displaying the end-to-end automation and contextual intelligence in action. Inspiration Every founder at Cal Hacks has the same problem: AI is expensive, and SDR tools are even worse. Cold email platforms charge $200+/month while burning through expensive GPT-4 calls. We asked ourselves: What if we could build an AI sales assistant that's actually profitable from day 1? That's where Lava Build's multi-model routing changed everything. Instead of blindly sending every request to GPT-4o at $5/1M tokens, we could route simple tasks to GPT-4o-mini at $0.15/1M tokens (33x cheaper!) while keeping complex enrichment on GPT-4o. This unlocked 80% cost savings and turned AI SaaS from a pipe dream into a viable business. We paired this with Poke's MCP integration to create a conversational interface - no dashboards, no clicking, just text your AI SDR like you'd text a coworker. What it does Poke SDR is a conversational AI sales assistant you control entirely through text messages. It exposes 6 MCP (Model Context Protocol) tools that Poke's AI automatically routes based on your natural language: add_lead() - Add leads via text: "add lead john@startup.io met at Cal Hacks" enrich_contact() - AI-powered profile enrichment with company, title, context draft_cold_email() - Generate personalized cold emails using enriched data suggest_action() - Get next best action based on lead stage and context search_leads() - Full-text search across your pipeline get_billing() - Real-time cost analytics showing per-lead COGS, margins, and Lava savings Every operation is tracked in a persistent SQLite database with real-time cost monitoring. The dashboard shows: 79 real Lava API calls (verified in screenshot) $0.12 actual cost from Lava routing 27 leads processed with full enrichment pipeline 99.97% gross margins at $10/month SaaS pricing The business case is simple: $10/mo revenue × $0.0028 COGS = sustainable, profitable AI SaaS. How we built it Backend (MCP Server): FastMCP v2.12.5 - Python framework for Model Context Protocol servers Lava Build - Multi-model routing proxy that intelligently routes requests: GPT-4o ($5/1M tokens) for enrichment + email drafting GPT-4o-mini ($0.15/1M tokens) for action suggestions Result: 80% cost reduction vs. GPT-4o-only LangChain - OpenAI client configured to route through Lava's forward API SQLite - Persistent database with two tables: leads - Email, name, company, title, stage, context, enrichment status ai_costs - Per-operation cost tracking (operation,model, tokens, cost) Frontend: Poke - Conversational MCP interface (configured via HTTP endpoint) React + TypeScript + Vite - Dashboard showing pipeline and cost metrics Tailwind CSS - Modern UI with real-time cost tracking Infrastructure: Render - Deployed MCP server at https://poke-sdr-mcp.onrender.com/mcp GitHub - Version control and collaboration Key Architecture Decision: Instead of chaining MCP tools (which fails - tools aren't callable Python functions), we made each tool standalone. Poke's AI decides which tool to call based on user intent, making the conversation feel natural. Challenges we ran into MCP Tool Chaining Error Early on, we tried to auto-trigger enrich_contact() when adding a lead. This failed with "FunctionTool object is not callable" because FastMCP wraps tools for the protocol - they're not regular Python functions. Solution: Made each tool standalone and let Poke's AI orchestrate the workflow. Cost Tracking Accuracy We needed to track costs per operation in real-time, but different models have different pricing. Solution: Built a track_ai_cost() function that logs every LLM call with operation type, model, tokens, and calculated cost to the database. This enabled the get_billing() tool to show real business metrics. Database Connection Management Hit "Cannot operate on a closed database" when querying lead counts after closing the SQLite connection. Solution: Reorganized query order to execute all database reads before calling conn.close(). Multi-Model Routing Strategy Deciding which operations deserve GPT-4o vs. GPT-4o-mini was critical for cost optimization. Solution: Complex tasks (enrichment, emails) → GPT-4o for quality Simple tasks (suggestions, summaries) → GPT-4o-mini for cost Tracked everything to prove 80% savings Accomplishments that we're proud of ✅ 79 real Lava API calls tracked in production (see dashboard screenshot) ✅ $0.12 actual cost vs. estimated $0.60 without routing = 80% savings ✅ 6 fully functional MCP tools tested end-to-end via Poke ✅ Persistent database with 27+ leads and complete audit trail ✅ 99.97% gross margins proven with real cost data ($0.0028 COGS/lead) ✅ Real-time cost tracking showing exactly where every penny goes ✅ Conversational workflow - no dashboards needed, just text The killer metric: At $10/month SaaS pricing, we have $9.9972 profit per customer thanks to Lava's routing. That's not a demo stat - that's a real business. What we learned Multi-Model Routing is a Game Changer We didn't appreciate how much Lava's intelligent routing could save until we tracked real costs. The 33x price difference between GPT-4o and GPT-4o-mini means the right routing strategy is the difference between profitable and unprofitable SaaS. MCP Protocol is Powerful but Different Model Context Protocol isn't just an API wrapper - it's a conversational paradigm shift. Tools can't call each other; the LLM orchestrates the workflow. This forced us to think about UX differently and actually made the product better. Cost Transparency Builds Trust Showing users exactly how much each operation costs ($0.0025 to enrich, $0.0003 to suggest action) builds incredible trust. Customers want to know their AI tools aren't bleeding money. Hackathon MVPs Need Real Metrics Mock data is fine for enrichment APIs, but real cost tracking and real Lava usage (79 API calls) make the difference between a toy and a product. What's next for Poke SDR Near-term (next 2 weeks): Integrate real enrichment APIs (Clearbit, Apollo, ZoomInfo) Add batch operations - enrich all leads, draft emails for entire pipeline Build analytics dashboard - conversion rates, pipeline velocity, ROI tracking Implement Poke voice interface - truly conversational sales assistant Long-term (6 months): Multi-channel outreach - LinkedIn, email, SMS orchestrated via conversation AI-powered lead scoring - Prioritize high-value leads using GPT-4o analysis CRM integrations - Sync with Salesforce, HubSpot, Pipedrive Team collaboration - Shared pipeline with role-based access Advanced routing - Use Lava to route based on lead value (cheap models for cold leads, expensive models for hot prospects) The vision: Every founder should have an AI SDR that's smarter than a human, costs less than coffee, and actually makes them money. Lava's routing makes this economically viable. Poke's conversational interface makes it delightful to use. <div