---
slug: "cryptoagent-cfo"
url: "https://devpost.com/software/cryptoagent-cfo"
title: "Cryptoagent - CFO"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 420
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/housing_homeless"
  - "user/educator_student"
---

# Cryptoagent - CFO

> Analyzes crypto portfolios and generates smart liquidation strategies based on risk tolerance.Uses real-time Gemini Exchange data and Fetch.ai agents to help decisions about converting crypto to cash

[Devpost](https://devpost.com/software/cryptoagent-cfo) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[housing_homeless]]
**user** [[educator_student]]
  <sub>weak: financial_record, sensor_telemetry</sub>

**stack** python

## Body

PROJECT NAME: CryptoAgent CFO TAGLINE: AI-powered crypto liquidation advisor helping students make smart financial decisions with autonomous agents CryptoAgent CFO addresses a critical financial challenge facing 10+ million crypto-holding college students: deciding which cryptocurrency assets to liquidate when they urgently need cash for rent, tuition, or emergencies. Currently, students make these decisions blindly, often resulting in $50-$500 in opportunity losses per transaction due to poor timing or asset selection. My solution leverages three cutting-edge technologies: FETCH.AI AUTONOMOUS AGENTS: We built a true autonomous agent using the uAgents framework that independently reasons about portfolio composition, market volatility, and user risk tolerance. The agent implements the ASI:One Chat Protocol, making it discoverable on Agentverse and capable of complex multi-step decision-making without human intervention. POSTMAN FLOWS ORCHESTRATION: We visually orchestrated the entire workflow using Postman Flows, employing the AI Agent block (GPT-4) for natural language parsing, HTTP Request blocks for API calls, and Evaluate blocks for data transformation. The flow is deployed as a public Action, allowing anyone to access it via a simple API call. REAL-TIME MARKET DATA: Integration with Gemini Exchange's public API provides live cryptocurrency prices and 24-hour volatility metrics for Bitcoin, Ethereum, and Solana, ensuring recommendations are based on current market conditions. HOW IT WORKS: Users describe their situation in plain English: "I have $1000 in crypto and need $400 for rent, I'm risk-averse." The Postman AI Agent parses this input to extract key parameters (runway, expense amount, risk tolerance). Simultaneously, we fetch live market data from Gemini Exchange. Both data streams feed into our Fetch.ai autonomous agent, which applies sophisticated risk-aware algorithms: CONSERVATIVE STRATEGY: Sells volatile assets first (SOL → ETH → BTC) to preserve stable holdings BALANCED STRATEGY: Proportional liquidation across all assets AGGRESSIVE STRATEGY: Sells stable assets first (BTC → ETH → SOL) to preserve high-growth potential The agent returns a detailed liquidation plan including which specific assets to sell, in what amounts, with clear rationale explaining the strategy. Response time is under 3 seconds. TECHNICAL ACHIEVEMENTS: Multi-API orchestration with real-time data processing Autonomous decision-making (not just an API wrapper) ASI:One Chat Protocol implementation for agent discoverability Error handling, CORS support, and comprehensive documentation Public deployment accessible to anyone The project demonstrates both technical excellence and practical utility, combining Postman's powerful orchestration capabilities with Fetch.ai's autonomous agent framework to solve a genuine problem facing millions of young investors. POSTMAN ACTION: https://volume-nebula-descent.flows.pstmn.io/api/default/cryptoagent-cfo POSTMAN WORKSPACE: https://www.postman.com/yuktaasri-addanki-7766311/workspace/blitz-s-workspace GITHUB: https://github.com/YOUR-USERNAME/cryptoagent-cfo AGENT ADDRESS: agent1qfhnmhjwxjjs43970rqjhsw00ds054v8gt0d0735m5x6h3pttpcewy2wugj AGENT ENDPOINT: https://jussive-lonnie-gallantly.ngrok-free.dev DEMO VIDEO: [Upload and paste link here] SPONSOR TRACKS: ✅ Postman ✅ Fetch.ai <div