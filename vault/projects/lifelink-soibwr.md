---
slug: "lifelink-soibwr"
url: "https://devpost.com/software/lifelink-soibwr"
title: "LifeLink"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 969
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# LifeLink

> Clinicians ask ASI:One for blood in plain English, a swarm of Fetch.ai agents finds blood centers, allocates units, manages payment, and proves delivery through SLA.

[Devpost](https://devpost.com/software/lifelink-soibwr) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]]
**domain** [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[retail_commerce]] [[supply_logistics]]
**user** [[clinician]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]]

**stack** aevs, agentverse, asi:one, fetch.ai, mcp, mongodb-atlas, pydantic-ai, python, react, stripe, typescript, uagents, ucp, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lifelink
- additional links/resources

## Body

Inspiration On June 14th, World Blood Donor Day was observed globally. Many individuals participated, social media engagement increased significantly, and donor turnout was substantial. Five days later, hospitals were still in crisis. Blood supply was down 35% in a month. Some hospitals had less than a two-day reserve. This situation was impactful for our team. The core issue is not a lack of donors or available blood, but rather the challenge of efficiently delivering the correct blood units to the appropriate hospitals in a timely manner — complicated by testing windows, donor eligibility, cold chain requirements, and the need for verified delivery. No patient should be lost due to a lack of coordination among centers that possess the necessary blood units. We developed LifeLink to address these critical moments — enabling hospital staff to request what they need and ensuring the system responds promptly and effectively. What it does LifeLink is a multi-agent blood coordination network built on Fetch.ai . Its sole interface is ASI:One — clinicians communicate in natural language, not structured forms. Try it: "Need 5 units B+ whole blood within 72 hours." A network of specialized agents takes over from there: Hospital Agent — receives the request and checks the hospital's own inventory first Discovery Agent — identifies blood centers capable of fulfilling the balance Center Agents — provide real inventory and pricing (American Red Cross, Stanford Blood Center, and Leukolab in our demo) Donor Agents — participate when fresh donations are required, contingent on eligibility Custody Agent — records a hash-chained trail from dispatch to receive Two paths, both real: Normal SLA — planned restock over days; fresh donation when safe, tested stock as backup Emergency QSLA — minutes matter; pre-tested stock only — you cannot use a fresh donation in an ER in 30 minutes Pay only for units that arrive verified. Donors are never paid. Blood always flows donor → licensed center → hospital . How we built it We built LifeLink on Fetch.ai — not as a chatbot wrapper, but as a real multi-agent network that coordinates blood supply end to end. ASI:One + uAgents Chat Protocol — Hospital staff communicate in plain English. The Hospital Agent on ASI:One interprets requests and manages the full workflow — no custom apps, no forms, just conversation. Agentverse — Hospital, Center, and Donor agents are hosted with mailbox registration and Almanac manifests, making them discoverable and reachable from anywhere — not just locally. uAgents with real roles — Discovery, Centers, Donors, Payment, Courier each handle one part of the chain and pass messages to the next. The Orchestrator holds authoritative order state so nothing gets double-allocated. Stripe (test mode) — When a hospital commits to units, we authorize a PaymentIntent per center and hold funds. MongoDB Atlas — Shared state for hospitals, centers, inventory, orders, allocations, payments, and an append-only event log. Falls back to a local JSON store when Atlas is not configured — same code, same flow. *UCP *— Centers expose commerce-style offers and checkout. MCP enrichment — Geo/Maps for real distance and ETA, Notifications for donor booking confirmations. Challenges we ran into AEVs Integration Memory management Stripe Enbedded into the chat interface Accomplishments that we're proud of We turned a real-world crisis into a working agent network in one weekend. A nurse types "Need 5 units B+ within 72 hours" into ASI:One, and LifeLink runs the full chain — stock check, center discovery, tiered quotes, allocation, donor eligibility, Stripe escrow, hash-chained custody, and payment capture only on verified delivery. No fake order IDs. No invented inventory. Every number comes from persisted state and real agent outputs. We built specialized Fetch.ai agents — Hospital, Discovery, Courier, three Center agents, and Donor agents — each with a distinct job, real message schemas, and Agentverse-ready hosting. This is not one chatbot wearing different hats. We integrated the full stack for real — uAgents Chat Protocol on ASI:One, Agentverse mailbox and Almanac manifests, Stripe, AEVs, UCP-style center offers, MongoDB Atlas. What we learned uAgents aren't just wrappers — they're the product. Agents, each owning one real role, each passing real messages. That is what makes LifeLink a network, not a script. Multi-agent coordination on Fetch.ai is the reason a single nurse's message can trigger discovery, allocation, payment, and custody across multiple centers without anyone managing it manually. ASI:One + Agentverse changes who can use AI. A nurse does not need an app, a login, or training — she just talks. ASI:One routes it to the right agent. Agentverse Almanac makes it discoverable. That is the real impact: AI that reaches people in moments that matter, without friction. Autonomous agents can save lives at scale. Every blood shortage is a coordination failure. With Fetch.ai's multi-agent stack, we showed that you can automate the entire procurement chain — from request to verified delivery — with agents that act, decide, and settle autonomously. That is not a demo trick. That is what this technology is for. What's next for LifeLink LifeLink is built to grow — from hackathon demo to regional blood network. Regional scale-out — connect real blood banks and hospital systems across the Bay Area and beyond; our multi-tenant architecture already supports multiple hospitals and centers on one orchestrated network Voice-first clinical UX — hands-free ASI:One for nurses in the OR and ER who cannot stop to type Donor experience at scale — mobile onboarding through the Donor Personal Agent, with calendar booking and notifications when a center needs help National shortage visibility — agent-driven dashboards that surface where supply is low before a crisis hits a single hospital Partnership path — designed to align with blood banking associations and hospital procurement workflows, not replace them Additional Links/Resources ASI1 Chat Session https://asi1.ai/chat/efbfe259-8663-495d-8f95-649fc9741073 Agentverse agents profiles https://agentverse.ai/agents/details/agent1qvldvtmfuzp2zva8l402s0newmlksnptfu2lpz7ukf3ttaenpsagu0cgqcc/profile https://agentverse.ai/agents/details/agent1q2a48hvu2w8m77jkpknaqwzva2vjwa9apz34wac0rxfujmhxtk3rkm53ujw/profile https://agentverse.ai/agents/details/agent1qffmq3xzyrrmu5dd0cuysmhy2xst9tjekzers69aggg4ut6yqzmdqz5ztkq/profile https://agentverse.ai/agents/details/agent1qttnl2ukghx2vnxwjvjytdw6lr5jp0gnd77r9hq9hr3mcj59deafz8anpgh/profile https://agentverse.ai/agents/details/agent1qtqn30s8n7vrs25hqdua9s8u6kjujgcd44ajrxu4294655vnsj50kw02rll/profile https://agentverse.ai/agents/details/agent1q2pzyeqjav45ngflx000dq5axtal0prfplahjtfdl253pl555ek8wxxpu3k/profile https://agentverse.ai/agents/details/agent1qv7zuhlwfruxjdgz2fgz2h7w2rrzefapjp0u4euslhxfvmpsxq6l5f8c5w4/profile https://agentverse.ai/agents/details/agent1qgqv44m9qpn7u2845ha8fldjvwtwwr5tdc26wen2uyh8dc2z3waq7j77l8w/profile https://agentverse.ai/agents/details/agent1qw227ydzx53sencjtn4gllttc2e3wgs2kh8yamfnu5kvvstjfx5sj4l8drl/profile https://agentverse.ai/agents/details/agent1qtsm4etrctgk576lfk4ut3dwgck67r8hapt6srnkjd5frqwnk8jdsxzzlmt/profile https://agentverse.ai/agents/details/agent1qgm3t7gtwu7lu0mr67fps7u3chky22pmcn24mrc3qhc0dn7nh04tss89k0f/profile <div