---
slug: "aerofreight-ai"
url: "https://devpost.com/software/aerofreight-ai"
title: "AeroFreight AI"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1189
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# AeroFreight AI

> AeroFreight AI: A multi-agent platform that plans smarter international shipments from origin to final delivery, whether through air or sea.

[Devpost](https://devpost.com/software/aerofreight-ai) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]]
**domain** [[climate_energy]] [[finance_payments]] [[legal_justice]] [[retail_commerce]] [[supply_logistics]] [[transportation]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]]

**stack** asi-one, bureau, claude, fetchai, gcp, pydantic, python, stripe, uagents, vscode

## How they structured the write-up

- fetch.ai track submission 🤖
- inspiration 💡
- what it does 🚀
- system architecture 🏗️
- how we built it 🛠️
- challenges we faced 🧩
- what we learned 🎓
- responsible ai and privacy 🔐
- environmental impact 🌱
- what's next 🔮

## Body

UI of the Project Using AeroFreight agent on FetchAI's ASI 1 platform Payment wall before receiving shipping quote Results Generated invoice PDF Fetch.ai Track Submission 🤖 Complete ASI:One Workflow: https://asi1.ai/shared-chat/3a7383cc-c9a7-412c-a473-0e0665ab97ea ASI Demo: https://youtu.be/EdWXfnOk8GI?is=RygbgCXSJ7HwRoXo **Agentverse Profiles: AeroFreight Orchestrator The central user-facing agent that handles ASI:One chat interactions, session state, and coordinates tasks among the sub-agents. Economic Constraints Agent Analyzes transport preferences and calculates necessary international taxes and customs requirements. Routing Agent The primary routing decision-maker that evaluates the extracted data to determine the optimal shipping method. Air Freight Sub-Agent Specialized agent responsible for quoting and logistics mapping for air-based transit routes. Ship Freight Sub-Agent Specialized agent responsible for quoting and logistics mapping for sea-based maritime freight. Treasury Agent Handles the final checkout pipeline, integrating the Stripe payment wall, generating PDF invoices, and managing documentation. GitHub: [ https://github.com/aniketggg/AeroFreight-AI ] Problem: International freight planning is fragmented across routing, cost estimation, and payment. Target User: Businesses importing goods into the United States. Outcome: AeroFreight AI produces a validated route, landed-cost estimate, and user-approved settlement workflow. We designed AeroFreight AI as a four-agent system: one central Orchestrator and three specialized agents . Each agent has a clearly defined responsibility, typed inputs and outputs, and an independent Agentverse-compatible interface, allowing the workflow to fit naturally within the Fetch.ai ecosystem and expand with additional logistics agents. The project demonstrates multi-agent collaboration, ASI: One integration, structured agent-to-agent messaging, external transportation data, failure handling, and a human-approved payment workflow. AeroFreight AI One shipment request. Specialized agents. One coordinated international freight workflow. Inspiration 💡 International shipping is fragmented across route planning, cost estimation, and payment systems. Before a shipment can move, businesses must compare freight modes, calculate tariffs, identify transportation hubs, plan inland delivery, and approve payment. We built AeroFreight AI to coordinate this workflow through a network of specialized autonomous agents. Each agent focuses on a specific task while a central orchestrator maintains the shared shipment state. What It Does 🚀 AeroFreight AI converts a natural-language shipping request into a structured freight plan for shipments traveling from an international origin to a destination in the United States. The user provides: origin and destination; cargo details; weight and volume; declared value; preference for speed or lower cost. If information is missing, the system asks a follow-up question before continuing. The completed request then moves through four coordinated stages. 1. Orchestrator Agent The Orchestrator acts as the central coordinator. It: connects the user experience to ASI:One ; converts natural language into structured shipment data; validates required fields; stores the shared shipment state; communicates with each agent in sequence. 2. Economist Agent The Economist Agent evaluates the shipment's financial and physical constraints. It determines: whether the cargo is high-value or luxury; estimated U.S. tariffs and entry taxes; whether the shipment should use AIR , SHIP , or EITHER . 3. Routing Agent The Routing Agent calculates route options, transportation cost, and estimated transit time. It coordinates two Fetch.ai sub-agents: AIR Agent — evaluates airport-based routes; SHIP Agent — evaluates seaport-based routes. Each sub-agent calculates: route nodes; countries visited; inland trucking; freight charges; route fees; estimated transit time. When both modes are allowed, the system prioritizes based on the user's SPEED or COST preference and returns a validated RouteData object. 4. Treasury and Settlement Agent The Treasury and Settlement Agent generates the final shipment summary, including: recommended route; transportation mode; itemized cost breakdown; total landed cost. The user must explicitly approve the transaction before settlement begins. System Architecture 🏗️ AeroFreight AI uses a centralized hub-and-spoke architecture. User ↔ Orchestrator | |--> (1) Economist Agent ───> EconData ───┐ | | |--> (2) Routing Agent ─────> RouteData ─┼──> Orchestrator | | (Updates State) |--> (3) Treasury Agent ────> Settlement ┘ The Orchestrator maintains the global shipment state, while each agent receives only the information required for its task. How We Built It 🛠️ Technology Stack Python 3.11 and 3.12 Fetch.ai uAgents ASI:One Pydantic airport and seaport datasets Structured Agent Communication Each workflow stage communicates through typed request and response messages. We created shared Pydantic models for: ShipmentRequest EconData RouteData SettlementStatus These shared schemas prevent inconsistencies between independently developed agents. Agent-to-Agent Messaging Agents communicate asynchronously through Fetch.ai protocols. The Orchestrator manages the flow, ensuring each agent receives validated input from the previous step. For dependent operations, we use: ctx.send_and_receive(...) Geographic Routing The Routing Agent uses airport and seaport coordinates to estimate great-circle distance with the Haversine formula. a = sin^2(delta latitude / 2) + cos(latitude 1) * cos(latitude 2) * sin^2(delta longitude / 2) distance = 2 * Earth radius * atan2(sqrt(a), sqrt(1 - a)) This includes inland transportation instead of comparing only airport-to-airport or port-to-port distance. Cost and Time Comparison The total landed cost is calculated as: Total Landed Cost = Freight and Toll Cost + Entry Tax Challenges We Faced 🧩 Agent Integration Small differences in field names, data types, or expected outputs could break the workflow. We solved this by treating shared Pydantic schemas as fixed interfaces between agents. Transportation Data Airport and seaport datasets use different identifiers, coordinate formats, country codes, and naming conventions. We added normalization and fallback logic so both routing agents could use a consistent process. Asynchronous Dependencies The workflow must execute in order: ShipmentRequest | v EconData | v RouteData | v SettlementStatus This required careful handling of asynchronous messages, validation, timeouts, agent addresses, and downstream failures. Human Control International shipping and payment decisions can have major legal and financial consequences. AeroFreight AI therefore requires explicit user confirmation before settlement. What We Learned 🎓 Multi-agent systems work best when every agent has: a clear responsibility; a limited and stable interface; validated inputs and outputs; access only to the data required for its task. This structure made AeroFreight AI easier to test, debug, integrate, and extend. We also gained experience with: Fetch.ai uAgents; ASI:One integration; asynchronous messaging; Pydantic validation; hub-and-spoke orchestration; geospatial routing; transportation data normalization; cost-versus-time optimization; human-in-the-loop approval; environment-based credential management. Most importantly, we learned that autonomous agents can do more than generate text. With structured data and reliable communication, they can collaborate on complex operational workflows. Responsible AI and Privacy 🔐 AeroFreight AI is designed as a decision-support platform rather than an unchecked autonomous authority. The system clearly displays: transportation mode; route nodes; countries visited; freight costs; entry taxes; total landed cost. Users can reject the proposed transaction, and explicit confirmation is required before settlement. Credentials and agent seeds are stored in environment variables, secrets are excluded from version control, and typed schemas limit unnecessary data sharing. Environmental Impact 🌱 Transportation mode affects a shipment's environmental footprint. A future version could add estimated carbon emissions so users can compare environmental impact alongside cost and delivery time. What's Next 🔮 Future improvements include: live freight pricing; real-time weather and port congestion; updated tariff and customs APIs; live shipment tracking; rail and trucking agents; carbon-emission estimates; sanctions screening; automated carrier bidding; dynamic route replanning; production-grade payment and escrow. Our long-term vision is for AeroFreight AI to become an intelligent logistics coordination layer that helps businesses plan, approve, and execute international shipments through a trusted network of specialized agents. One request. Multiple agents. One smarter freight workflow. <div