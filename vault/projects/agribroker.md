---
slug: "agribroker"
url: "https://devpost.com/software/agribroker"
title: "AgriBroker"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 550
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# AgriBroker

> You need 500 tomatoes under $250? AgriBroker's agents optimize prices and pays the best order. Farmer's produce surplus reduced and customers happy with cheap organic food.

[Devpost](https://devpost.com/software/agribroker) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[on_device_local]] [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[finance_payments]] [[retail_commerce]] [[supply_logistics]]
**user** [[frontline_worker]] [[general_public]] [[legal_professional]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]]

**stack** agentverse, asi, fetch.ai, multi-agent, python, stripe

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agribroker

## Body

Drafting Productivity Agent Inspiration Produce procurement is still surprisingly manual. A restaurant, co-op, or bulk buyer may know they need 500 tomatoes, but they still have to find suppliers, compare prices, check inventory, split orders, and coordinate payments. We saw this as a coordination problem that autonomous agents are well-suited to solve, as working with small farmers to reduce waste, produce can be optimized in bulk. USDA's Economic Research Service (ERS) estimates that about 30 percent of food in the United States goes uneaten at the retail and consumer level. Promoting locally grown and organic food, we wanted to build a system where a buyer could simply state their intent and let agents handle the discovery, optimization, and transaction workflow. What it does AgriBroker is an autonomous produce procurement marketplace built on the Fetch.ai ecosystem. A buyer can ask for produce in natural language, such as "I need 500 tomatoes under $250." AgriBroker discovers seller agents, gathers inventory and pricing information, computes the cheapest feasible split across suppliers, coordinates payment, and returns a single transparent receipt. In live agent mode, the orchestrator communicates with a Registry agent and multiple Farmer agents to source the order through agent-to-agent messaging. How we built it We built AgriBroker in Python using Fetch.ai uAgents, ASI, and Agentverse. The system consists of an orchestrator agent, a registry agent for seller discovery, and farmer agents that manage inventory, pricing, invoices, and receipts. We implemented a deterministic optimizer that selects the lowest-cost supplier combination, integrated Stripe Checkout for buyer funding, added simulated Stripe Connect-style payouts for sellers, and created onboarding tools that allow new farms to join the marketplace without modifying the orchestrator. Challenges we ran into The biggest challenge was balancing reliability with live integrations. ASI, Agentverse, Stripe, Business Agents, and agent networking all introduce external dependencies that can fail during a demo. To address this, we built a deterministic local workflow and layered live integrations on top of it. We also had to make agent coordination visible to judges, so we added progress updates and an agent trace that shows discovery, quoting, purchasing, and receipt generation across multiple agents. Accomplishments that we're proud of We're proud that AgriBroker demonstrates a complete intent-to-action workflow. A buyer can start with a simple natural-language request, and the system autonomously discovers suppliers, gathers quotes, optimizes an order split, coordinates payment, and returns a final receipt. We also successfully implemented live Registry and Farmer agent communication, farmer self-onboarding, Stripe Checkout integration, and visible agent traces that make the multi-agent architecture easy to understand. What we learned We learned that building agentic commerce is about more than making agents communicate. The system also needs to be reliable, transparent, and auditable. Designing clear protocols, deterministic optimization logic, fallback mechanisms, and user-facing receipts was just as important as integrating ASI and Agentverse. We also gained experience coordinating multiple independent agents within a marketplace workflow. What's next for AgriBroker Our next steps are to deploy the agents in a hosted environment, enable fully automated payment confirmation, expand beyond tomatoes into broader produce catalogs, add seller reputation and quality metrics, support delivery and logistics workflows, and make seller onboarding completely self-service. The long-term goal is to create an autonomous procurement network where buyers can source produce from a large ecosystem of independent farm agents. <div