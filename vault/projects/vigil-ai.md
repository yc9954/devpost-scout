---
slug: "vigil-ai"
url: "https://devpost.com/software/vigil-ai"
title: "Vigil AI"
hackathon: "GKE Turns 10 Hackathon"
organization: "Google"
winner: true
words: 744
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Vigil AI

> Vigil AI: Securing financial microservices with autonomous, real-time fraud mitigation.

[Devpost](https://devpost.com/software/vigil-ai) · hackathon [[GKE Turns 10 Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
  <sub>weak: sensor_fusion</sub>
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]] [[structured_db]]

**stack** a2a, adk, docker, fastapi, gemini, gke, go, google, kubernetes, postgresql, python, uvicorn

## Body

Inspiration: A Personal Fight Against a Rising Tide of Fraud The inspiration for Vigil AI is deeply personal and rooted in a growing problem in my home country, Brazil. The rapid adoption of digital banking and instant payment systems like Pix has been revolutionary, but it has also triggered a massive spike in sophisticated scams, credit card cloning, and digital fraud. This isn't just a headline for me; just two months ago, I experienced a fraudulent transaction attempt on my own digital bank account. That experience, combined with my passion for how AI is revolutionizing every industry, crystallized the idea for this project. I wanted to build something that could fight back — not just a reactive tool, but a proactive, intelligent system that could stand guard over a financial application. This hackathon was the perfect opportunity to channel that motivation into a real-world solution. How We Built Vigil AI Vigil AI is a proactive, hierarchical multi-agent system designed to enhance the security of the Bank of Anthos application, all orchestrated on Google Kubernetes Engine (GKE) . The core principle was to add this security layer without modifying the existing application's code , interacting with it only through its databases. The architecture is composed of several specialized agents working in concert: GKE Foundation: GKE serves as the backbone of the entire system, managing the deployment, scaling, and networking of all our agent microservices. GenAI Toolbox for Databases: This component acts as a secure data access layer. It exposes predefined SQL queries as callable tools that our agents use to safely interact with the Bank of Anthos's ledger-db and accounts-db . TransactionMonitor Agent: The system's frontline sensor. Built with Python and asyncio, it continuously polls the database for new transactions and uses a predefined threshold ( $1000.0 ) to flag suspicious activity, sending alerts via the A2A protocol. Orchestrator Agent: The central "brain" of the operation. Powered by Google ADK's LlmAgent with Gemini 2.5 Flash, it receives alerts, delegates investigations, evaluates risk scores, and decides whether to trigger enforcement actions. Investigation Agent: Also powered by ADK's LlmAgent with Gemini, this agent acts as a digital detective. It gathers context by pulling the user's profile and transaction history, then uses the LLM to analyze the data and produce a structured "case file" with a risk score and justification. Actuator Agent: The enforcement arm. A FastAPI service that receives commands from the Orchestrator and executes actions — such as locking the user's account to prevent further damage. Inter-agent communication uses the A2A (Agent-to-Agent) protocol , while agents access databases through REST API calls to the GenAI Toolbox. Challenges We Faced & What We Learned Building a multi-agent system in such a short timeframe came with significant challenges: Partial ADK Adoption: My original vision was to use Google's Agent Development Kit (ADK) across all four agents. In practice, only the Orchestrator and Investigation agents ended up using ADK's LlmAgent — the TransactionMonitor and Actuator were implemented as simpler Python services. Time constraints forced pragmatic tradeoffs. MCP vs REST Reality: I initially planned to use the GenAI Toolbox's MCP (Model Context Protocol) interface for agent-database communication. However, getting MCP working end-to-end proved complex under time pressure, so I pivoted to the Toolbox's REST API ( /api/tool/{tool}/invoke ). The integration works, but it's a simpler approach than originally envisioned. A2A Communication Debugging: Establishing reliable communication between agents was complex. I faced CrashLoopBackOff errors in the Orchestrator due to outdated API usage and had to refactor to a FastAPI-based architecture for handling A2A messages. LLM Output Sanitization: The Orchestrator's LLM would sometimes return valid commands wrapped in prose or Markdown code blocks. I had to build a robust sanitizer to extract clean JSON payloads — a great lesson in real-world LLM integration. Coordinating AI Coding Assistants: Much of the development was done by coordinating AI coding agents (Jules, Codex, Claude) through prompts. This introduced its own challenge: the agents would sometimes implement things differently than specified, requiring careful review and iteration. Through this process, I learned an immense amount about the practicalities of building agentic AI systems : that ambitious architectures often need to be simplified under time pressure, that debugging distributed systems requires patience, and that GKE provides a solid foundation for managing complex containerized applications. This project was a challenging but incredibly rewarding journey — turning a personal pain point into a functioning, AI-powered solution. The gaps between vision and implementation are now clear opportunities for future improvement. <div