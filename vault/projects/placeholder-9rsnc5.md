---
slug: "placeholder-9rsnc5"
url: "https://devpost.com/software/placeholder-9rsnc5"
title: "Nexus Maestro: 1 Case, 5 AI Agents, Seamless Orchestration"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 1422
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/supply_logistics"
  - "user/government_staff"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Nexus Maestro: 1 Case, 5 AI Agents, Seamless Orchestration

> Maestro Case turns a single fraud call into a live multi-agent investigation: AI scoring, parallel SIP calls to vendors and carriers, human-in-the-loop review, and a wire recall - in minutes.

[Devpost](https://devpost.com/software/placeholder-9rsnc5) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[housing_homeless]] [[supply_logistics]]
**user** [[government_staff]] [[legal_professional]] [[researcher]]
**substrate** [[financial_record]] [[web_dom]]

**stack** cartesiatts, deepgram, fastapi, googlecloudrun, openaigpt-4o, python, qubi, react, redis, uipathactioncenter, uipathagentbuilder, uipathapiworkflows, uipathcodedactionapp, uipathintegrationservice

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nexus maestro

## Body

GIF Inspiration Business Email Compromise (BEC) wire fraud is the #1 B2B payment crime - 76% of AP departments were targeted in 2024, with average losses between $47K-$130K per incident. Today, investigating a single suspicious wire takes 2-4 days across multiple teams: fraud analysts, vendor contacts, carrier confirmations, compliance review. The wire recall window? Just 24-48 hours. Most organizations miss it. We asked: what if a single phone call could trigger a fully governed, multi-agent investigation - and initiate the recall before the caller hangs up? That's what UiPath Maestro makes possible. Not as a concept - as a working system. What it does A treasury officer calls to report a suspicious $94,000 wire. From that single call: Qubi-Aria (a coded voice agent) verifies the caller's identity and pulls the wire from the core banking system - surfacing red flags: the beneficiary account is only 11 days old, and the receiving bank doesn't match the vendor's bank of record. Aria opens a UiPath Maestro case - the investigation brain. Maestro's Agent Builder fraud intelligence agent scores the wire at 92/100 (vendor impersonation). Aria speaks the score to the caller mid-call - but she didn't compute it. Maestro did. Maestro dispatches two more voice agents in parallel - Qubi-Merril phones the vendor on a real mobile line via SIP, while Qubi-Larry phones the carrier. Both confirm: no invoice was issued, no shipment was dispatched. The wire went to a fraudulent account. A second Agent Builder agent synthesizes all evidence into a determination, writes the exact words Aria should speak, and decides whether to initiate a wire recall and FBI referral. Aria reads the platform-authored resolution verbatim to the caller. The voice agents never decided anything - every determination was made inside the Maestro case. If the case is inconclusive, Maestro interrupts into a ManualReview exception stage, opening a task in Action Center rendered by our NEXUSReviewApp a UiPath coded action app - a fraud analyst confirms or overrides the AI determination. Total elapsed time: ~90 seconds. One phone call, five AI agents, one governed Maestro case. The War Room - a real-time React topology dashboard - makes the entire orchestration visible: every agent activation, every Redis pub/sub message, every Maestro stage transition, live. How we built it UiPath Maestro Case is the backbone - a 4-stage case definition (FraudIntelligence → MultiPartyVerification → ResolutionSynthesis → Resolution) plus an interrupting ManualReview exception stage, SLA rules, and conditional exit guards. Two Agent Builder agents (low-code, deterministic-prompt, temp 0) handle all decision-making: one for fraud scoring, one for resolution synthesis. Four API Workflows bridge Maestro stages to the voice backend: dispatching outbound calls, relaying the fraud assessment mid-call, fetching consolidated verification results, and relaying the final resolution. Integration Service HTTP Webhooks provide the event triggers - case creation, verifications-complete signal, and manual-review interrupt. Orchestrator Assets store runtime config (callback URLs, SIP dial targets). Action Center hosts the HITL escalation task, rendered by a Coded Action App (NEXUSReviewApp - React/TypeScript). The voice layer uses Qubi Agents (Python) with Deepgram STT, OpenAI GPT-4o, and Cartesia TTS. Three agents - Aria (inbound), Merril (vendor outbound), Larry (carrier outbound) - connect via WebRTC and SIP. They collect information and speak outcomes; they do not make decisions. The async bridge between Maestro and the voice agents is Upstash Redis (pub/sub) - the backend publishes fraud scores, verification results, and resolution text to Redis channels; the voice agents subscribe and speak updates mid-call with zero dead air. The FastAPI backend runs on Google Cloud Run , serving all NEXUS API endpoints and an SSE topology stream consumed by the War Room dashboard. The War Room (React + @xyflow/react) renders a live knowledge graph of every agent, data flow, and Maestro stage - idle → active → streaming → complete - with animated edges, payload chips, and agent waveforms. Use Coding Agents: Claude Code + UiPath Skills Maestro Case Plan - Claude Code scaffolded and iterated the caseplan.json case definition, including stage entry/exit conditions, SLA rules, conditional exit guards, and the interrupting ManualReview exception stage - all via uip CLI commands ( uip solution pack , uip solution publish , uip solution deploy ). Coded Action App - Claude Code built the NEXUSReviewApp (React/TypeScript) from the action schema through to uip codedapp pack and uip codedapp publish - the full cycle from code to Action Center deployment. UiPath CLI Skills - Claude Code operated the uip CLI to pack, publish, and deploy UiPath solutions, coded action apps, and orchestrator assets - acting as a development partner across both the low-code and coded layers. The CLAUDE.md and AGENTS.md files in NEXUSCase/ are part of this workflow - they serve as the coding agent's context files for understanding and modifying the UiPath solution structure. This project is a direct example of combining coding agents with low-code components : Claude Code built the coded agents and UiPath artifacts, while Agent Builder provided the low-code decision-making agents inside the Maestro case. Challenges we ran into Race condition on case exit: When the resolution synthesis agent returns escalated , the manual-review webhook must fire before the Resolution stage completes - otherwise the case closes and the ManualReview exception stage never enters. We solved this with a conditional exit guard: Exit Rule 1 checks resolutionAction !== "escalated" before marking the case complete. Verification results delivery: The original design had the verifications-complete webhook carry the actual vendor/carrier data. But webhook payloads are fire-and-forget - if the data was malformed or missing a field, the case stalled. We redesigned it as a two-step: the webhook is now a "results ready" signal that triggers Workflow_FetchVerificationResults , which pulls the consolidated verdicts via GET /api/verification-summary/{caseId} . More resilient, fully idempotent. SIP + WebRTC coexistence: Running three concurrent Qubi voice sessions (one WebRTC inbound, two SIP outbound) through the same backend required careful room isolation and participant identity management. Each sub-agent gets its own room keyed by {contactType}-{caseId} . Voice agents speaking platform-authored text verbatim: The resolution text comes from Maestro's synthesis agent - it's not generated by the voice agent's own LLM. Injecting externally-authored speech into an LLM-driven conversation agent without the LLM "improving" or paraphrasing it required a dedicated speak_verbatim pattern that bypasses the conversational pipeline. Accomplishments that we're proud of Five AI agents orchestrated by one Maestro case - coded agents (Python/Qubi), low-code agents (Agent Builder), and a human analyst (Action Center) - all governed by a single case definition with SLA rules, exit guards, and an interrupting exception stage. Parallel outbound SIP calls to real mobile phones - Qubi-Merril and Qubi-Larry dial actual phone numbers during the live investigation. No simulated calls, no mocked responses - real conversations with real people on real lines. Zero dead air - Aria speaks fraud scores and verification results the moment they arrive via Redis pub/sub, keeping the caller informed throughout a 90-second investigation that would normally take days. The War Room - a live topology dashboard that makes the invisible visible. Judges, stakeholders, and demo audiences can see the multi-agent orchestration happening in real time. Voice agents that never decide - the architectural principle that every determination is made inside the Maestro case, and voice agents only collect and speak. This is governance by design, not by policy. What we learned Maestro Case is genuinely powerful for dynamic, exception-heavy processes. The interrupting exception stage pattern (ManualReview) and conditional exit guards gave us production-grade control flow that would have been painful to hand-code. Agent Builder's are the right tool for regulated decisions. We initially considered having the voice agents run the fraud-scoring logic - but moving it into Agent Builder meant every decision is auditable, versioned, and governed by Maestro. That's the enterprise pattern. Redis pub/sub is the perfect async bridge for voice + workflow orchestration. The voice agents and Maestro operate on fundamentally different timescales - Redis lets them communicate without blocking either side. The "agents speak, platform decides" separation of concerns is not just architectural - it's a trust story. When we explain that Aria reads the resolution verbatim from Maestro, the response from enterprise stakeholders is immediate: "that's how it should work." What's next for Nexus Maestro Webhook authentication - HMAC signatures / UiPath external-app tokens on every callback (demo endpoints are currently unauthenticated). Multi-tenant deployment - supporting multiple bank customers on a single Maestro case definition with tenant-scoped Redis channels and room isolation. Expanded fraud types - extending the case definition to handle ACH fraud, check fraud, and account takeover scenarios with additional Agent Builder agents and verification sub-agent personas. <div