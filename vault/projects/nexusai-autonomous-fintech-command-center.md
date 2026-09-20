---
slug: "nexusai-autonomous-fintech-command-center"
url: "https://devpost.com/software/nexusai-autonomous-fintech-command-center"
title: "NexusAI: Autonomous FinTech Command Center"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 661
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# NexusAI: Autonomous FinTech Command Center

> An AI-powered financial intelligence platform with real-time portfolio optimization, behavioral biometrics fraud detection, and multi-framework compliance monitoring in one command center.

[Devpost](https://devpost.com/software/nexusai-autonomous-fintech-command-center) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[legal_professional]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]]

**stack** api, chart.js, css3, git, github, google, html5, javascript, pages, speech, web

## How they structured the write-up

- 💡 inspiration
- 🔍 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🎉 accomplishments that we're proud of
- 🧠 what we learned
- 🚀 what's next for shieldnet

## Body

💡 Inspiration In the fast-paced world of modern finance, institutions and individuals are forced to juggle separate, disconnected tools for portfolio management, fraud prevention, and regulatory compliance. This fragmentation creates dangerous blind spots. We were inspired to build ShieldNet (powered by the NexusAI architecture)—a unified, autonomous financial intelligence command center. Our goal was to bridge the gap between high-performance asset optimization and enterprise-grade security, proving that AI can actively defend capital while simultaneously growing it. 🔍 What it does ShieldNet is an autonomous financial intelligence and security platform featuring over 38 advanced tools integrated into a single, high-fidelity command center: 🛡️ Fraud Shield: Real-time behavioral biometrics and threat stream analysis that flags transaction anomalies, card skimming patterns, and potential wire fraud. 📈 Portfolio Optimizer: An interactive environment showing the Efficient Frontier, Sharpe ratios, and active rebalancing recommendations based on AI optimization models. 🔮 Predictions Engine: Multi-horizon predictive projections (1-day, 7-day, 30-day, and 90-day) simulating LSTM and Transformer confidence bounds. ⚖️ Compliance & ESG Radar: Live multi-framework audit ratings (AML, KYC, GDPR, SOX, Basel III) alongside deep environmental, social, and governance portfolio tracking. 💬 NEXUS AI Advisor: An integrated conversational interface supporting text and voice queries (via the Web Speech API) to guide user decision-making. ⚠️ Risk Command: Dynamic Monte Carlo simulations and historical crisis stress tests (such as the 2008 Financial Crisis and 2020 COVID Crash). 🛠️ How we built it To ensure maximum reliability, speed, and cross-platform compatibility, we built the platform as a modular, pure-frontend Single Page Application (SPA): Architecture: A robust 4-layer separation of concerns: data.js : The simulated engine powering real-time asset prices, threats, and metrics. ai-engine.js : The natural language processor and scoring algorithms. charts.js : The visual layer configuring over 20 dynamic Chart.js instances. app.js : The central orchestrator managing global search, voice input, and page routing. Design System: Built using semantic HTML5 and vanilla CSS. The interface utilizes a premium glassmorphic dark mode design, custom Google Fonts, and smooth micro-animations optimized for performance. Deployment: Version-controlled with Git and deployed to GitHub for easy access. 🚧 Challenges we ran into API Bulletproofing: Connecting directly to real-time financial APIs during a live hackathon introduces rate limits, quota issues, and connection failures that can ruin a judge's experience. We overcame this by writing a high-fidelity client-side simulation engine that mimics real market volatility and transaction patterns seamlessly. Complex SPA State Management: Coordinating active updates across 13 pages, a global Cmd+K search bar, voice command integration, and dozens of auto-updating charts in plain vanilla JavaScript required strict structural discipline to avoid spaghetti code. Visual Performance: Rendering multiple complex charts and live data tickers simultaneously can cause browser lag. We optimized chart configurations and decoupled visual updates to keep interactions performing at a smooth 60fps. 🎉 Accomplishments that we're proud of Engineering Depth: Writing over 6,000 lines of original, clean, modular JavaScript and CSS without relying on heavy external frameworks. Feature Integration: Seamlessly blending 38 distinct features—spanning quantitative finance, behavioral security, and regulatory compliance—into a cohesive user experience. Robust Voice Controls: Successfully integrating browser voice command capabilities that allow hands-free navigation and system queries. 🧠 What we learned The Power of Mock Fidelity: We learned that a highly realistic, self-contained client-side simulation is often superior for hackathon demonstrations because it is 100% reliable, runs instantly, and requires zero complex environment setup from judges. Vanilla JS Scalability: Building a large-scale project without frameworks like React or Tailwind taught us how to write clean, reusable, and efficient vanilla design patterns and modular scripts. 🚀 What's next for ShieldNet 🔌 Live API Integrations: Transitioning the data layer from simulations to live market feeds using the Alpha Vantage and Polygon.io APIs. 🔒 Secure LLM Integration: Moving from keyword-based responses to live conversational AI by hosting a lightweight Node.js backend to securely proxy requests to the Gemini developer API. 💳 Real Portfolio Syncing: Implementing the Plaid API to allow users to securely link, monitor, and defend their actual bank accounts and brokerage holdings. <div