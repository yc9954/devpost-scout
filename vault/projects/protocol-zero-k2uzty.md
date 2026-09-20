---
slug: "protocol-zero-k2uzty"
url: "https://devpost.com/software/protocol-zero-k2uzty"
title: "Protocol Zero"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 905
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Protocol Zero

> Protocol Zero: Bridging AI intelligence with on-chain trust. Our agent uses ERC-8004 to prove behavior, earn reputation, and safely manage capital.

[Devpost](https://devpost.com/software/protocol-zero-k2uzty) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]]

**stack** amazon-bedrock, amazon-nova-(tool-use-workflow), amazon-nova-lite, amazon-nova-sonic, eip-712-typed-data-signatures, erc-8004-registries, github, hugging-face-spaces, keccak256-hashing, merkle-audit-artifacts, numpy, pandas, plotly, python

## How they structured the write-up

- headline
- inspiration
- project overview
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned
- what's next for protocol zero

## Body

PROTOCOL ZERO OFFCIAL LOGO Headline PATH TAKEN FOR PROTOCOL ZERO Protocol Zero — Teaching an AI Trader to Be Accountable Inspiration The inspiration came from a simple tension I kept seeing in Web3 and AI: AI systems are becoming powerful enough to take autonomous actions. DeFi systems are powerful enough to execute those actions instantly. But users still ask the most human question: “Can I trust this thing with real money?” Protocol Zero is my answer to that question. I wanted a system where autonomy is exciting, but never reckless. Where every action can be traced. Where “black box” becomes “auditable glass box.” Project Overview Category,Details Core Mission,"Transforming ""Black Box"" AI trading into an ""Auditable Glass Box.""" Primary Stack,"Python, Streamlit, Amazon Nova, ERC-8004, EIP-712." Key Innovation,Fail-closed risk routing and Merkleized audit traces. What it does Protocol Zero is a real-time autonomous trading dashboard and execution pipeline featuring:Amazon Nova-powered reasoning for market analysis and trade intent generation.Fail-closed risk routing before every execution.On-chain identity + reputation + validation (ERC-8004 flow).EIP-712 typed signing for accountable intents.Validation artifacts + Merkleized audit trace.Live dashboard observability (market state, cognitive stream, trust panel, performance analytics).Runtime DEX execution control (manual/autonomous operational mode switching).The Core LogicThe heart of the system is the following principle:$$\text{Execute Trade} \iff \bigwedge_{i=1}^{n} \text{RiskCheck}_i = \text{PASS}$$If any critical check is uncertain, execution is blocked. No “almost safe.” No optimistic shortcuts. How we built it I built Protocol Zero as a Python + Streamlit application with modular services for intelligence, risk, trust, and execution: Intelligence Layer: Nova modules generate decisions from live market context and structured prompts/tools. Risk Layer: Multi-step guardrails enforce position caps, confidence floors, daily loss limits, frequency controls, and emergency halt behavior. Trust / On-chain Layer: The agent can register identity, link reputation feedback, and produce validation signals tied to immutable records. Execution Layer: A DEX executor handles real trade paths, with runtime toggles for safe demo and production behavior. Observability Layer: The UI exposes every critical state: decision rationale, confidence, risk outcomes, tx references, and system health. Challenges we ran into This project was built under real hackathon pressure, and the hardest part was not writing features—it was making them reliable under live conditions. Runtime Constraints: I had cloud-provider edge cases where a model endpoint looked configured but was partially blocked at runtime. I implemented graceful fallback behavior and truthful status signaling so the UI never faked readiness. Live Hosting Instability: I hit a painful “dark-blue blank screen” issue triggered by rerun/reload timing in hosted UI state transitions. I tracked it to aggressive client refresh patterns, removed unstable loops, and redesigned refresh behavior for host-safe operation. On-chain Proof Consistency: Some tx references could be stale or absent depending on chain responses. I added robust tx normalization, fallback search links, and token discovery recovery logic. Human Factors under Deadline: The biggest challenge was staying calm while debugging production behavior minutes before submission. I learned to prioritize stability over flash, and truthful UX over optimistic assumptions. Accomplishments that we're proud of: Building a "Fail-Closed" Reality We are incredibly proud of successfully implementing a strict safety-first architecture. In a world where most bots are "optimistic" (executing first and asking questions later), we successfully built a pipeline where: $$Execution \implies \text{Verified Integrity}$$ If the risk layer detects even a minor anomaly or a 1% dip in model confidence, the system halts. We didn't just talk about safety; we encoded it into the runtime. Sophisticated Reasoning with Amazon Nova Integrating Amazon Nova allowed us to move beyond simple "if/then" trading scripts. We are proud of how the agent handles complex, qualitative market data—turning messy sentiment and dense metrics into a structured "Cognitive Stream" that a human can actually read and audit in real-time. ** Bridging the "Trust Gap" via EIP-712 & ERC-8004** We successfully bridged the gap between off-chain AI logic and on-chain accountability. By using EIP-712 typed signing, we ensured that every "intent" generated by the AI is cryptographically bound to its identity. This means the AI isn't just a ghost in the machine; it’s a registered entity with a verifiable reputation. Technical Resilience Under Pressure During the final hours of the hackathon, we faced critical "dark-blue screen" UI crashes and API blocks. We are proud not just of the code we wrote, but of the stability we maintained. Instead of cutting corners to finish, we:Refactored the state management to handle aggressive refreshes.Built a robust "Truthful UX" that signals system health accurately rather than masking errors.Prioritized a rock-solid, auditable demo over a flashy but fragile one. Radical Observability Finally, we are proud of the Protocol Zero Dashboard. We turned a complex "Black Box" into an "Auditable Glass Box." Seeing the live cognitive stream sync perfectly with on-chain validation proofs was the "Eureka" moment of this project—proving that autonomous finance can, and should, be transparent. What we learned This project taught me that “AI + DeFi” is not just a technical problem—it is a trust design problem. "I learned to build systems that degrade gracefully instead of crashing dramatically, and to treat observability as a feature, not a dev-only tool." Protocol Zero is not just a bot that can trade; it is a statement that autonomous finance should be auditable, bounded, and human-centered. What's next for Protocol Zero Stronger cross-chain trust proofs and expanded policy-based risk governance. Richer multimodal anomaly detection to spot market manipulation. AWS regional account block fix to ensure 100% uptime. Production-grade agent memory + post-trade learning loops. <div