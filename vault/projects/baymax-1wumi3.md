---
slug: "baymax-1wumi3"
url: "https://devpost.com/software/baymax-1wumi3"
title: "baymax"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 976
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# baymax

> Baymax is a network of hospital AI agents that supports abrupt crises using weather, disease, and inventory data, then coordinates hospital-to-hospital supply transfers before crises peak.

[Devpost](https://devpost.com/software/baymax-1wumi3) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[disaster_emergency]] [[finance_payments]] [[health_clinical]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]]

**stack** arize, claude, fetch.ai, html5, javascript, poke, python, redis

## How they structured the write-up

- at a glance
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next

## Body

Baymax When a heatwave strikes, a disease outbreak surges, or a mass casualty event unfolds, hospitals are suddenly competing for the same scarce supplies, and the phone-call coordination that's supposed to fix it is far too slow. Baymax is a network of hospital AI agents built on Fetch.ai that sees crises coming by fusing live weather, disease, and inventory signals. Using Claude for reasoning, it autonomously negotiates and settles inter-facility transfers on-chain before shortages peak. Every decision is traced through Arize Phoenix, allowing the system to learn from each event and improve future responses. Baymax doesn't just respond to emergencies - it learns to anticipate them. At a Glance Baymax predicts shortages before they happen, negotiates inventory transfers between hospitals, settles them on-chain, and learns from every crisis it handles. Inspiration The supply crisis starts long before a hospital runs out. It starts hours earlier, when a weather forecast converges with rising illness signals and a facility that's already running lean. By the time a supply manager notices the pattern—let alone makes phone calls to neighboring facilities, negotiates terms, and arranges a transfer—the shortage has already peaked. The perception problem (counting what's on a shelf) is largely solved. The harder problem is autonomous coordination under surge conditions : seeing a crisis before it happens, negotiating transfers across institutions under real constraints, settling them quickly, and improving the system after every event. That's a multi-agent systems problem. Fetch.ai provides the agent network. Claude provides the reasoning layer. Arize Phoenix closes the learning loop. Baymax is what happens when all three work together. What it Does Baymax runs one agent per hospital. Each agent continuously combines: Live inventory from edge vision systems Weather forecasts and disease-burden signals Historical surge patterns and outcomes When a shortage is predicted: Claude detects a surge risk before inventory reaches critical levels. The requesting hospital broadcasts a transfer request through the Fetch.ai agent network. Nearby hospitals respond with constrained offers. Claude evaluates quantity, urgency, ETA, distance, and expiry dates. If no single offer satisfies demand, Baymax automatically creates a split transfer plan. The transfer is settled through the Fetch Payment Protocol on Dorado testnet. Arize Phoenix traces the entire decision process and outcome. The result is a system that can identify shortages earlier, coordinate faster, and continuously improve over time. How We Built It Baymax has two user-facing surfaces: ASI:One for natural-language interaction and approvals A live Flask dashboard for real-time monitoring and visualization Both are powered by the same Fetch.ai agent network and synchronized through Redis. Core Stack Component Technology Agent Network Fetch.ai uAgents Agent Discovery & Chat Agentverse + ASI:One Settlement Fetch Payment Protocol Reasoning Claude Haiku + Claude Sonnet Vision Claude Vision State Management Redis Stack Forecasting Signals Open-Meteo + disease.sh Observability Arize Phoenix Dashboard Flask Agent Network Agent Role baymax_front Requester, ASI:One interface, settlement coordinator baymax_hospital_b Surplus inventory provider baymax_hospital_c Secondary surplus inventory provider Negotiation Flow Signal Detection ↓ Shortfall Predicted ↓ Request Broadcast ↓ Offer Collection ↓ Offer Ranking ↓ Transfer Planning ↓ On-Chain Settlement ↓ Outcome Logging Challenges We Ran Into ASI:One Echo Loops ASI:One occasionally interpreted our own agent narration as new user intent. We built filtering, cooldowns, and heuristics to prevent agents from responding to themselves. Payment Card Rendering The Fetch payment card depended on very specific metadata fields. Missing metadata caused silent failures with no visible error messages. Python 3.14 Event Loop Changes uAgents still relied on behavior removed in Python 3.14. We had to carefully manage initialization order to ensure a valid event loop existed before agent creation. Long-Running On-Chain Verification Transaction verification could stall agent execution for up to 20 seconds. We moved verification into background threads using asyncio.to_thread() . Accomplishments We're Proud Of Live End-to-End Settlement We successfully demonstrated: Natural-language intent → surge prediction → multi-hospital negotiation → on-chain payment → confirmed transfer Real Predictive Signals Baymax combines: Live weather data Real illness data Current inventory levels to generate structured shortage forecasts before a shortage is declared. Constraint-Aware Negotiation Baymax doesn't simply match one requester to one provider. It can automatically compose split transfers when multiple facilities are required to satisfy demand. Full Decision Traceability Every prediction, ranking decision, transfer proposal, and outcome is captured in Arize Phoenix. Parallel Development The forecasting, vision, dashboard, observability, and agent teams all built independently against a shared Redis schema and integrated successfully. What We Learned The defensible technology isn't the camera. The real value comes from creating a network that can detect, negotiate, and settle across institutional boundaries before a crisis peaks . We also learned that observability is essential for autonomous systems. The ability to trace every decision made by the system transforms Baymax from a coordination tool into a platform that can improve with experience. Finally, we learned that fail-closed design makes live demos possible. Every major dependency has deterministic fallbacks, allowing the system to remain reliable even when external services are unavailable. What's Next Predictive Pre-Positioning Move inventory before shortages occur when confidence in an incoming surge becomes sufficiently high. Disaster Response Coordination Extend the network to support regional responses for mass-casualty incidents and natural disasters. Ambulance & Patient Routing Apply the same negotiation framework to patient transfers and hospital capacity balancing. Blood & Biologics Logistics Support temperature-sensitive and blood-type-constrained transfers. Cross-System Federation Allow independent health systems to participate in a regional mutual-aid network without exposing internal inventory systems. Supplier-Side Agents Bring distributors into the negotiation process so Baymax can choose the globally optimal resolution between purchasing and transfer options. Baymax sits on top of existing hospital workflows. It doesn't replace clinical decision-making—it helps ensure critical supplies arrive where they're needed before shortages impact patient care. ## Built with fetch.ai · uagents · agentverse · asi:one · chat-protocol · payment-protocol · claude · claude-code · anthropic · redis · arize-phoenix · opencv · open-meteo · disease.sh · flask · python <div