---
slug: "complianceguard"
url: "https://devpost.com/software/complianceguard"
title: "ComplianceGuard"
hackathon: "Airia AI Agents Hackathon"
organization: "airia"
winner: true
words: 950
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# ComplianceGuard

> Autonomous AI compliance monitoring — detect GDPR, HIPAA, SOC2 & EU AI Act violations in 60 seconds

[Devpost](https://devpost.com/software/complianceguard) · hackathon [[Airia AI Agents Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[labor_employment]] [[media_journalism]]
**user** [[general_public]] [[patient_family]]
**substrate** [[regulation_legal_text]] [[sensor_telemetry]] [[web_dom]]

**stack** airia, anthropic, gmail, google, google-docs, mcp, next.js, slack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for complianceguard

## Body

airia agents pipeline Inspiration Enterprise AI adoption is accelerating faster than compliance teams can keep up. In 2025 alone, GDPR fines exceeded $4 billion. Every day, employees unknowingly share sensitive customer data, patient records, and financial information with unauthorized AI tools like ChatGPT and Gemini — and compliance teams have absolutely no real-time visibility into it. We asked: what if compliance monitoring could be as autonomous as the AI tools causing the risk? ComplianceGuard was born from that question. What it does ComplianceGuard is a fully autonomous 3-agent AI compliance monitoring system built entirely on Airia. When an AI usage event is detected — via Slack, API, or the dashboard — the system automatically: MONITORS: Agent 1 (ComplianceGuard Monitor) ingests and normalizes the raw event into structured data CLASSIFIES: Agent 2 (ComplianceGuard Risk Assessor) analyzes the event against 4 major regulatory frameworks using Sequential Thinking MCP for deep reasoning: • GDPR — EU citizen PII shared with unauthorized tools • HIPAA — Patient health data exposure • SOC2 — Financial and customer data leaks • EU AI Act — AI used for hiring, credit, biometrics REMEDIATES: Agent 3 (ComplianceGuard Remediator) automatically generates a formal 7-section incident report in Google Docs and dispatches professional compliance alert emails to the compliance team The entire pipeline — from Slack message to formal incident report — completes in under 60 seconds with zero manual intervention. A real-time dashboard built in Next.js shows live event feeds, severity trends, pending HITL approvals, and incident report archives. How we built it ComplianceGuard is built on Airia as the core orchestration platform, with a Next.js frontend for the compliance dashboard. AIRIA PLATFORM: 3 specialized agents built in Airia Agent Builder Claude Sonnet 4.6 as the reasoning engine Sequential Thinking MCP for deep compliance analysis Agents chained into a single automated pipeline Slack Bot deployment for real-world event triggering Gmail Tool for professional alert notifications Google Docs tools (Create + Update) for incident reports Policy ruleset uploaded as an Airia Data Source Google OAuth credential for all Google integrations FRONTEND: Next.js 14 with TypeScript and App Router Tailwind CSS dark mode design Recharts for severity trend and regulation breakdown charts Real-time event feed with severity badges HITL approval interface with Approve/Dismiss/Escalate Incident reports archive with direct Google Doc links Simulate Violation panel for live demos The pipeline works end-to-end: a Slack message triggers the Monitor agent, which feeds the Risk Assessor, which automatically calls the Remediator on HIGH/MEDIUM severity events — all chained within Airia's nested agent architecture. Challenges we ran into Gmail API configuration: The Gmail tool required specific "from" field configuration that wasn't immediately obvious — we debugged the Advanced API settings to get real emails delivering successfully Agent chaining: Understanding how to properly nest agents within Airia's canvas took experimentation — we discovered the AI builder could auto-connect nodes which saved significant time Slack webhook configuration: Getting the Slack bot to properly trigger the pipeline required careful configuration of Event Subscriptions, OAuth scopes, and the Airia webhook URL — particularly distinguishing between channel messages and direct messages Pipeline timeout: The full 3-agent pipeline takes 60-90 seconds end-to-end, which required handling async execution properly in the frontend API layer Structured output compatibility: Claude's JSON schema dialect conflicted with Airia's structured output enforcement — resolved by embedding format instructions directly in prompts rather than using schema enforcement Accomplishments that we're proud of Built a genuinely working end-to-end autonomous compliance system — not a demo, but a real pipeline that sends real emails and creates real Google Docs Achieved 99% confidence classification accuracy across all 5 test scenarios (GDPR, HIPAA, SOC2, EU AI Act, clean) The system correctly cites specific GDPR Articles (5, 28, 32, 33, 44) in generated incident reports — demonstrating genuine regulatory knowledge Real Slack integration: posting a message in #ai-usage-log automatically triggers the full compliance pipeline Generated incident reports include complete audit trails, sanitized evidence, and specific remediation timelines (e.g., "GDPR Article 33 notification deadline: 72 hours") Built a professional enterprise-grade dashboard that genuinely looks and feels like a real compliance product Full pipeline completes in under 90 seconds from Slack message to Google Doc incident report What we learned Airia's nested agent architecture is genuinely powerful for building multi-step autonomous workflows — the ability to chain agents as nodes inside other agents enables sophisticated pipelines with minimal code Sequential Thinking MCP dramatically improves compliance classification accuracy — the step-by-step reasoning catches edge cases that single-shot prompting misses Prompt engineering > schema enforcement: embedding structured output requirements directly in system prompts is more reliable than relying on schema validation layers Enterprise AI compliance is a genuine and urgent problem — every organization adopting AI tools needs exactly this kind of autonomous monitoring system The combination of Airia's agent orchestration with Google Workspace tools creates a surprisingly complete enterprise workflow without any custom backend infrastructure What's next for ComplianceGuard Microsoft Teams and SharePoint integration for organizations in the Microsoft ecosystem Real-time dashboard with live Airia API polling — showing violations as they happen across the organization HITL approval workflow wired directly into the dashboard — compliance managers approve/dismiss from the UI, triggering Agent 3 automatically Support for additional regulations: PCI-DSS, CCPA, ISO 27001, and sector-specific frameworks Browser extension (Airia Everywhere) that monitors AI tool usage directly at the browser level — detecting sensitive data before it's even submitted Integration with DLP (Data Loss Prevention) tools and SIEM systems for enterprise-grade event ingestion Automated employee training triggers — when a violation is detected, automatically enroll the user in relevant compliance training Multi-tenant support for compliance consulting firms managing multiple enterprise clients Airia Community Submission Reference ID: 51755a18-bfb6-4b45-ba95-3a3 Agent currently under community review. Submitted prior to deadline. <div