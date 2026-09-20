---
slug: "how-did-i"
url: "https://devpost.com/software/how-did-i"
title: "How Did I?"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 1067
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/legal_professional"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# How Did I?

> How Did I? is an agentic ecommerce operator that diagnoses daily revenue leaks across carts, ads, inventory, and support—then drafts owner-approved fixes in one tap.

[Devpost](https://devpost.com/software/how-did-i) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[human_in_the_loop]] [[on_device_local]] [[provenance_signing]]
**domain** [[finance_payments]] [[health_clinical]] [[retail_commerce]] [[supply_logistics]] [[transportation]]
  <sub>weak: developer_tools</sub>
**user** [[legal_professional]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** api, docker, drizzle-orm, firebase-auth, fivetran-mcp, fivetran-rest-api, gemini, google-adk, google-cloud-run, google-gen-ai-sdk, google-secret-manager, help-scout, meta-ads, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for how did i?

## Body

Inspiration Every ecommerce owner knows the feeling: you wake up, open Shopify, check Meta Ads, scan Stripe, look at support tickets, check inventory, refresh abandoned carts, and still end up asking the same question: “How did I do today?” That question sounds simple, but the answer is usually scattered across eight different dashboards. A store can be leaking revenue because a high-spend ad is sending traffic to a low-stock product, abandoned carts are spiking on one SKU, a support issue is blocking purchases, or a payout anomaly is hiding in plain sight. We built How Did I? because ecommerce owners should not need to manually reconcile every signal before they know what needs attention. They need an operator, not another dashboard. What it does How Did I? is an agentic ecommerce operations layer that diagnoses daily revenue leaks and prepares the fixes for owner approval. In one daily pulse, the agent can: Analyze orders, carts, inventory, ads, payouts, and support signals. Detect revenue leaks such as abandoned cart spikes, low-stock products receiving ad spend, stockout risks, and payment anomalies. Estimate the dollar impact of each issue. Explain the evidence behind every diagnosis. Draft concrete next actions, such as recovery emails, ad pause recommendations, supplier reorder messages, and support replies. Queue every action for manual owner approval. The core flow is: Diagnose → quantify leak → explain evidence → draft fix → owner approves. Nothing is positioned as an unsafe autonomous write. Every fix is prepared, reviewable, and approval-based. How we built it How Did I? is built as a hybrid TypeScript and Python application designed for reliability, auditability, and fast demoability. The frontend is a polished React/TanStack experience with a dark, glassmorphic brand system. The main product experience is organized around three views: Daily Pulse — a store health overview showing revenue leaks and urgent signals. Mission Console — a step-by-step reasoning feed showing what the agent analyzed and why. Approval Queue — pre-drafted fixes that the owner can review, edit, and approve. The backend runs through a Node/TanStack service layer with multiple agent execution adapters: A Google Cloud / Vertex AI Reasoning Engine path for the production agent runtime. A Gemini adapter for secure direct model reasoning and fallback execution. A deterministic mock adapter for stable local testing and hackathon demos. For the data layer, How Did I? is designed around Fivetran MCP as the trusted bridge into ecommerce systems. The agent can reason over connector-style evidence from platforms like Shopify, Meta Ads, Stripe, Help Scout, inventory sheets, and analytics data. When live credentials are unavailable, the app falls back to a seeded demo dataset that preserves the same diagnosis and evidence structure. The app is deployed on Google Cloud Run , uses Firebase Auth , stores secrets through environment-bound configuration, and keeps sensitive credentials out of source control. We also built an evaluation suite to score diagnosis quality across eight checks: Health score range. Checkout/cart focus. Severity assessment. Revenue impact accuracy. Action generation count. Manual approval requirement. Synthesis quality. Evidence attribution. Challenges we ran into The biggest challenge was making the product feel like a real operator instead of a generic analytics dashboard. It was not enough to show metrics. The agent needed to connect cause and effect: “Revenue is down” is not useful. “Meta is spending on a product that will stock out in five days, creating $1,280 at risk, and here is the supplier email we drafted” is useful. Another challenge was balancing autonomy and safety. Ecommerce actions can affect real customers, real ad spend, and real revenue, so we designed every output around owner approval . The agent can prepare high-context actions, but the human remains in control. We also had to support multiple execution modes. The project needed to work with live cloud infrastructure, direct Gemini reasoning, and deterministic demo data without breaking the user experience. That required consistent schemas, adapter boundaries, fallback logic, and clear runtime transparency. Finally, we spent a lot of time on the interface. The product needed to be understandable within seconds for hackathon judges, but still feel credible enough for real store owners. Accomplishments that we're proud of We are proud that How Did I? feels like a complete product, not just a prompt wrapper. Some highlights: A live, polished ecommerce operator interface. A clear agent workflow from diagnosis to approval. Google Cloud deployment through Cloud Run. Vertex AI / Reasoning Engine architecture for agent execution. Fivetran MCP-centered data strategy. Safe read-only diagnosis and approval-based action design. A multi-adapter agent layer for production, fallback, and demo modes. A structured evaluation suite with 8/8 correctness checks across the mock, Gemini, and Python ADK paths. A brand and UX direction that makes the daily ecommerce operations problem immediately understandable. Most importantly, we built a product around a real daily behavior: store owners already ask, “How did I do today?” How Did I? gives them an answer and the next action. What we learned We learned that the most valuable agents are not just conversational. They are operational. A useful ecommerce agent needs to: Pull together fragmented data. Prioritize what matters. Show evidence. Estimate business impact. Prepare the work. Keep the human in control. We also learned how important trust is in agent design. Users do not want a black box making changes to their store. They want a reliable operator that explains its reasoning, shows its sources, and waits for approval. From a technical perspective, we learned how to structure a multi-adapter agent system, how to keep schema outputs consistent across different reasoning paths, and how to design a cloud-ready agent architecture that still works locally for demos and testing. What's next for How Did I? Next, we want to turn How Did I? into a real daily operating system for ecommerce teams. Planned next steps include: Live production onboarding for Shopify, Meta Ads, Stripe, Help Scout, GA4, and inventory systems. Deeper Fivetran MCP connector support and richer evidence views. Brand-voice training for drafted customer emails and support replies. Approval workflows for teams, including roles, comments, and audit logs. More action types, including campaign budget shifts, reorder recommendations, support macros, and product-page fixes. Historical trend analysis so owners can see whether the agent’s recommendations improved revenue over time. A mobile-first morning briefing experience. The long-term vision is simple: Every ecommerce owner should start the day with one clear answer, one prioritized plan, and the fixes already drafted. <div