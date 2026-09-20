---
slug: "gradientguard-dora-compliance-intelligence-platform"
url: "https://devpost.com/software/gradientguard-dora-compliance-intelligence-platform"
title: "GradientGuard — DORA Compliance Intelligence Platform"
hackathon: "DigitalOcean Gradient™ AI Hackathon"
organization: "DigitalOcean"
winner: true
words: 1120
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "user/developer"
  - "user/government_staff"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# GradientGuard — DORA Compliance Intelligence Platform

> AI-powered DORA compliance platform for EU fintechs. 4 multi-agent system on DigitalOcean Gradient™ AI — monitors infrastructure 24/7, detects ICT incidents, auto-generates audit evidence.

[Devpost](https://devpost.com/software/gradientguard-dora-compliance-intelligence-platform) · hackathon [[DigitalOcean Gradient- AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[labor_employment]] [[legal_justice]] [[mental_health]] [[security_privacy]]
**user** [[developer]] [[government_staff]] [[legal_professional]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[regulation_legal_text]] [[structured_db]] [[web_dom]]

**stack** boto3, claude-sonnet-4-5, claude-sonnet-4-6, digitalocean-app-platform, digitalocean-gradient-ai, do-adk-traces, do-agent-evaluate, do-gradient-knowledge-bases, do-managed-postgresql, do-serverless-inference, do-spaces, drizzle-orm, express.js, github-actions

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gradientguard — dora compliance intelligence platform

## Body

Inspiration 22,000 EU financial institutions. €2.4 million average annual compliance cost. January 2025: DORA became law. Most SMB fintechs still manage this manually — spreadsheets, quarterly scrambles, 4–8 hours per incident to produce audit evidence. I spent 15+ years at ING Netherlands and ABN AMRO watching compliance teams drown in paperwork after every ICT incident. When DigitalOcean launched Gradient™ AI, I saw a chance to build the tool I always wished existed: a platform that treats compliance as a real-time engineering problem, not a quarterly audit ritual. DORA isn't optional. It's law. And the penalty for non-compliance isn't just a fine — it's operational shutdown. GradientGuard changes the economics of compliance from €120,000/year to €2,160/year. That's a 98% cost reduction. What it does GradientGuard is a production-ready, multi-agent AI compliance intelligence platform that: Monitors cloud infrastructure 24/7 for DORA Article 11 threshold breaches (RTO ≤ 4h, RPO ≤ 1h, availability ≥ 99.5%) Detects ICT incidents in real time and auto-classifies by severity (P1/P2/P3) with DORA article mapping Generates PDF audit evidence packages in < 2 minutes, complete with incident timeline, log evidence, and DORA regulation citations — stored in DO Spaces Advises on root cause analysis and step-by-step remediation with estimated recovery times Answers natural language compliance questions via RAG over DORA, NIS2, GDPR, and MAS TRM regulations The live dashboard shows a real-time compliance score (0–100), live incident feed via SSE, LangGraph agent execution traces, and a built-in ROI calculator. Judges can hit the "Simulate P1 Incident" button to see the entire 4-agent pipeline fire in real time. Live demo: https://gradient-guard-74ijs.ondigitalocean.app/dashboard How we built it Built entirely on DigitalOcean Gradient™ AI in 72 hours using 8 DO products: 4 Gradient ADK Agents (Python + LangGraph): A1 DORASentinel — polls DO infrastructure via API v2 every 60s, detects threshold breaches, classifies incidents, triggers A2+A3 in parallel via A2A protocol. Model: llama3.3-70b-instruct A2 EvidenceForge — fetches app logs, builds chronological timeline, queries DORA KB via RAG, generates structured PDF with reportlab, uploads to DO Spaces. Model: claude-sonnet-4-5 A3 RemediationAdvisor — performs root cause analysis, queries DORA Article 17 KB, generates prioritized remediation plan, notifies Slack. Model: claude-sonnet-4-6 A4 ComplianceCounsel — multi-turn RAG Q&A over 4 regulation knowledge bases (DORA, NIS2, GDPR, MAS TRM), supports gap reports and incident history summaries. Model: claude-sonnet-4-5 Infrastructure: Node.js/Express API with SSE for real-time incident streaming Next.js 15 dashboard with animated compliance gauge, live agent trace visualizer, and streaming chat DO Managed PostgreSQL 16 for incident records and audit log DO Spaces for PDF evidence storage with presigned CDN URLs Terraform for infra-as-code + GitHub Actions CI/CD pipeline Every LangGraph node is instrumented with @trace decorators for full ADK Traces visibility. gradient agent evaluate runs weekly on ComplianceCounsel and DORASentinel. Challenges we ran into A2A protocol coordination — Getting A1 to reliably fire A2 and A3 in parallel under load required careful async handling. Early versions had race conditions where the incident record wasn't committed to PostgreSQL before A2 tried to read it. PDF generation quality — Building a court-admissible audit evidence document programmatically with reportlab required multiple iterations to handle edge cases: empty timelines, long citation text, Unicode from regulation PDFs. Drizzle ORM + DO Managed PG SSL — The managed PostgreSQL cluster requires sslmode=require but the Drizzle migration runner ( drizzle-kit push ) doesn't pass SSL config the same way as the runtime client. Required a custom SSL bypass for the db-migrate PRE_DEPLOY job while keeping SSL enforced at runtime. Gradient KB API — The knowledge base retrieval API was still in preview; the Python SDK required using access_token (DO API token) rather than the model access key for KB operations. Took time to figure out the dual-credential pattern. App Platform cold starts — The sentinel worker needs to call the DORASentinel agent endpoint every 60s. Ensuring the agent had warmed up before the first cron tick required a startup delay and retry logic. Accomplishments that we're proud of End-to-end in 72 hours : 4 deployed agents, seeded knowledge bases, live dashboard, Terraform-managed infra, GitHub Actions CI/CD — all production-grade Real DORA coverage : Articles 11, 17, 19, 25, 28 — not surface-level, but with actual regulation text in the KB and citation-backed evidence packages < 2 minute evidence generation : What takes a compliance team 4–8 hours is done in under 120 seconds, with a downloadable PDF that references specific DORA regulation text 8 DO products used : Gradient ADK, Serverless Inference, Knowledge Bases, Agent Evaluate, ADK Traces, App Platform, Managed PostgreSQL, DO Spaces — genuinely deep stack integration 98% cost reduction : €120,000 → €2,160/year for a 100-person fintech. Based on Deloitte 2024 DORA Compliance Cost Study. Agent-to-agent (A2A) : True multi-agent orchestration, not just sequential chaining — A1 dispatches A2 and A3 in parallel with full state handoff What we learned LangGraph is production-ready for compliance workloads. The ability to define clear state transitions and add @trace to every node gave us full observability into every agent decision — exactly what regulators want from AI systems in financial services. Domain expertise is a force multiplier for AI. My 15 years at ING/ABN AMRO meant I could write precise DORA threshold values, article mappings, and evidence requirements into the agent prompts from memory. The LLM outputs were dramatically better because the prompts were written by someone who has actually sat in DORA audit meetings. RAG quality depends on source quality. Seeding the knowledge bases with official EU regulation PDFs (not summaries) produced far more accurate citations than any fine-tuned model would — regulators care about the exact article number and paragraph. DigitalOcean's managed stack removes infrastructure anxiety. Using App Platform + Managed PG + Spaces meant zero time spent on Kubernetes, backup policies, or SSL certificate management. All engineering effort went into the product. What's next for GradientGuard — DORA Compliance Intelligence Platform Short term (Q2 2026): Live DO monitoring webhooks replacing poll-based detection (true real-time, sub-second MTTD) Automated DORA gap report generation — scheduled weekly PDF to compliance officer email Multi-tenant SaaS: organization isolation, role-based access (CISO / auditor / engineer) NIS2 and MAS TRM full coverage alongside DORA Medium term (Q3 2026): Integration with third-party ICT provider monitoring (AWS, Azure subcontractors) for DORA Article 28 compliance Regulatory reporting automation — pre-filled templates for DNB (Dutch Central Bank) and EBA incident reports Compliance score benchmarking: compare your DORA posture against anonymized sector peers Go-to-market: The target customer is a 50–500 person EU fintech paying a Big Four firm €80–200K/year for DORA readiness. GradientGuard delivers the same assurance at €2,160/year. The first 10 pilots will come from my network at Dutch fintech associations (Holland FinTech, FinTech NL). This is not a hackathon prototype — it's a company waiting to be incorporated. <div