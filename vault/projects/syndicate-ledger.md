---
slug: "syndicate-ledger"
url: "https://devpost.com/software/syndicate-ledger"
title: "Syndicate Ledger"
hackathon: "LMA EDGE Hackathon"
organization: "LMA"
winner: true
words: 976
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Syndicate Ledger

> AI-powered payment reconciliation for syndicated loans. Single source of truth replacing Excel chaos with real-time transparency, LMA compliance, and automated dispute resolution.

[Devpost](https://devpost.com/software/syndicate-ledger) · hackathon [[LMA EDGE Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[finance_payments]]
  <sub>weak: developer_tools, housing_homeless, security_privacy</sub>
  <sub>weak: developer, government_staff</sub>
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** next.js, postgresql, prisma, tailwind

## Body

Inspiration In syndicated lending, payment reconciliation remains stubbornly manual. Agent banks distribute payments to 5, 10, or 50+ participant banks, each maintaining their own Excel spreadsheets, each calculating their expected share independently. When numbers don't match (and they often don't), the reconciliation begins: emails, phone calls, more spreadsheets, and hours of detective work to find a $0.02 rounding difference. We spoke with loan operations professionals who described spending 40% of their time on reconciliation tasks that add zero value, just verifying that everyone agrees on the same numbers. The industry processes $4.7 trillion in syndicated loans annually, yet relies on workflows designed in the 1990s. Our inspiration : What if Agent and Participant banks could see the exact same truth, in real-time, with AI handling the tedious work? What it does Syndicate Ledger provides a single source of truth for syndicated loan payment reconciliation: For Agent Banks: Create payments and automatically calculate pro-rata distributions based on participation percentages Upload payment notices (PDF) or paste email content, AI extracts all payment data instantly Anomaly scanner flags discrepancies before banks even see them When disputes arise, AI analyzes the delta and drafts professional resolution responses For Participant Banks: Real-time visibility into their distributions across all loans One-click status updates: Agree, Dispute, or Request Review Complete audit trail showing every action and status change Analytics dashboard with payment history and trends The AI Advantage: Document Extraction : Upload a PDF payment notice → AI extracts borrower, amounts, dates, rates, and bank distributions in seconds Anomaly Detection : Two-phase scanning (rule-based + AI-enhanced) catches rounding errors, participation mismatches, statistical outliers, and duplicate payments Discrepancy Assistant : When a bank disputes, AI analyzes historical patterns, suggests reason codes, and generates draft responses, accelerating resolution from hours to minutes How we built it Architecture: Next.js 15 with App Router for a modern, performant full-stack application PostgreSQL + Prisma ORM for robust data persistence with type-safe queries Azure OpenAI (GPT-5-mini) powering all AI features through a unified client Azure Blob Storage for secure document handling with SAS token authentication Tailwind CSS v4 for a polished, professional UI AI Implementation: azureAI.js - Centralized Azure OpenAI client with support for text, PDF, and image inputs aiExtractor.js - Document parsing with structured JSON output and confidence scoring anomalyDetector.js - 8 anomaly types with statistical analysis + AI enhancement aiAssistant.js - Discrepancy analysis with reason codes and resolution suggestions LMA Aligned: Data structures align with LMA Agent Data Format (ADF) standards ISO 20022 compatibility for future SWIFT integration Complete audit trail meeting regulatory requirements Challenges we ran into 1. Learning an Entirely New Domain As software developers, syndicated lending was completely foreign territory. Terms like "day count conventions," "participation percentages," "pro-rata distributions," and "accrual periods" required significant research. We spent the first phase reading LMA documentation, watching industry webinars, and consulting with finance professionals to understand what we were actually building. 2. Translating Financial Logic into Code Understanding the domain was one thing—implementing it correctly was another. Financial calculations have zero tolerance for error. We had to learn why ACT/360 differs from 30/360, how rounding affects multi-party distributions, and why a $0.01 discrepancy matters when you're dealing with $500M loans. 3. Designing for Two Different Users Agent banks and Participant banks have fundamentally different workflows but need to see the same data. Balancing these perspectives—one creating and distributing payments, the other receiving and validating—required careful UX thinking to ensure both sides felt the platform was built for them. 4. Making AI Contextually Relevant Generic AI responses weren't useful. We had to craft prompts that understood syndicated loan terminology, standard reason codes for discrepancies, and professional communication norms in banking. The AI needed to "speak finance" to be genuinely helpful. 5. Building Trust Through Transparency In financial services, trust is everything. Every design decision had to consider: "Would a compliance officer approve this?" This led us to implement comprehensive audit trails, clear status indicators, and LMA-compliant data structures—features that aren't glamorous but are essential. Accomplishments that we're proud of ✅ Complete Working System : Not a mockup, real database persistence, full CRUD operations, and production-ready code ✅ AI That Actually Works : Three integrated AI features (extraction, anomaly detection, discrepancy analysis) with fallback modes when credentials aren't available ✅ Role-Based Transparency : Instant switching between Agent and Bank perspectives shows how the same data serves different stakeholders ✅ Professional Polish : PDF exports with charts, LMA compliance badges, and a UI that wouldn't look out of place in a Bloomberg terminal ✅ Audit Trail : Every action logged immutably, essential for regulatory compliance in financial services What we learned Domain Knowledge Matters : Understanding LMA standards, day count conventions, and syndicated loan workflows was essential. Technical skill alone wouldn't solve a problem we didn't fully understand. AI Augments, Doesn't Replace : Our best results came from combining rule-based logic (fast, predictable) with AI enhancement (contextual, intelligent). The anomaly scanner runs rules first, then offers AI-enhanced analysis. Transparency Builds Trust : The single-source-of-truth concept resonated because it addresses a real pain point, not knowing if your counterparty is looking at the same numbers. Fallbacks Are Essential : AI features gracefully degrade when Azure credentials aren't configured. The discrepancy assistant uses rule-based analysis as a fallback, ensuring the app remains functional. What's next for Syndicate Ledger Immediate (Post-Hackathon): Multi-tenant authentication with bank-specific API keys Webhook delivery to external systems (currently simulated) Email/SMS notifications for SLA warnings and breaches Medium-term: SWIFT MT/MX message parsing for automated payment ingestion Mobile companion app for on-the-go approvals Integration with treasury management systems Vision: Syndicate Ledger could become the industry utility for syndicated loan servicing, a shared platform where Agent banks, Participant banks, and even Borrowers access the same truth. No more reconciliation. No more Excel. Just transparent, AI-assisted loan operations. Built for LMA EDGE Hackathon 2026 | Azure OpenAI + Next.js + PostgreSQL <div