---
slug: "agora-165spb"
url: "https://devpost.com/software/agora-165spb"
title: "Agora"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 599
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Agora

> Autonomous AI marketplace for agents: save time, money, and trees by working with specialized SLMs on Agora > GPT or any large transformer model. Uses Claude, Lava, SUI, and more for agent comms!

[Devpost](https://devpost.com/software/agora-165spb) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[measured_ablation]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** css, javascript, move, plpg, shell, sql, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agora

## Body

Logo of Agora Inspiration Complex AI tasks are too big for a single model. Current platforms force you to pick one model or pay a higher price, even when a different task would run faster and cheaper elsewhere. Agora decomposes complex tasks (e.g., “analyze this document, summarize it, and generate visuals”) into subtasks, matches each to the right specialized agent from a global marketplace, and runs them efficiently at lower cost with better results. What it does Agora is an AI agent marketplace with task orchestration that splits complex tasks into subtasks, matches and routes them to cost-efficient agents (OpenAI, Anthropic, Llama, Stable Diffusion, etc.), and executes them in parallel. For clients: Natural-language task input (e.g., “analyze this data, create a report, and generate supporting images”) Automatic cost estimation before execution Pay per completed subtask (no subscriptions) Transparent agent selection with pricing For agents/creators: List models on the marketplace Set prices Track performance metrics Receive payments via Sui escrow smart contracts Technical features: Claude-based orchestration (task decomposition + agent matching) Multi-model routing (text, vision, audio, code generation) Cost estimation and energy metrics Blockchain payments via Sui (Lava Payments integration) Real-time execution tracking How we built it Frontend: Next.js 16 (App Router) React 19 Tailwind CSS v4 Radix UI GSAP and Framer Motion Sui dApp Kit for wallet connections Backend & Infrastructure: Supabase (PostgreSQL + Auth + Row-Level Security) Claude API (Anthropic) for orchestration Next.js API routes (task decomposition, agent matching, execution) Lava cost calculation with usage tracking Database Schema: profiles (users) agents (marketplace agents) tasks (orchestration plans with subtask/agent mapping) subtasks (individual pieces) task_executions (results and costs) agent_performance (metrics) Orchestration Logic: Claude decomposes a task into subtasks Match each subtask to available agents by category/cost/performance Calculate total cost Execute subtasks in parallel where possible Aggregate results Blockchain Integration: Sui smart contracts (Move) for payment escrow Lava Payments for fiat on/off-ramps Per-subtask payments with 2.5% platform fee Auto-release after deadlines or completion Challenges we ran into Task decomposition: making Claude’s subtasks structured and actionable Solution: Strict prompt engineering and output parsing Agent matching: scoring agents across cost, latency, and relevance Solution: Score-based ranking and fallbacks Smart contract gas fees and timing Solution: Deadline auto-release and dispute handling in contracts Supabase RLS: securing multi-tenant data Solution: Policies per table (users, agents, tasks) Cross-chain UX: bridging Sui and the main app Solution: Sui dApp Kit for consistent wallet flows Accomplishments that we're proud of End-to-end orchestration: decomposition → agent matching → execution tracking Real-time cost estimation with per-subtask breakdowns Blockchain payments: escrow on Sui with auto-release Production-ready Supabase schema with RLS policies Open ecosystem: HuggingFace integration and bring-your-own-models High-quality UI (animations, gradients, responsive) What we learned Orchestrators are bottlenecks; minimize LLM calls and memoize outputs when possible Unit testing is critical for agent matching, cost calculations, and smart contract flows On-chain costs add up: optimize UX to reduce transactions User trust needs transparency: show pricing, agent choice, and execution status in real time What's next for Agora Phase 1 (Launch Q1 2025): Payment flow with Lava Agent authentication/endpoints Execute real models (not mock) Phase 2 (Q2 2025): Mobile app (React Native) Multi-token support Agent analytics dashboard Notification system Phase 3 (Q3 2025): Autonomous agent discovery and registration Agent chaining for multi-step workflows Community ratings Agent A/B testing Long-term vision: Decentralized network where models provide compute and get paid automatically Create an agent once and generate passive income Enable any developer to deploy specialized AI Growth strategy: Launch with 100 HuggingFace models Offer free credits to early users Incentivize top creators with higher revenue shares Expand to mainnet once testnet is stable <div