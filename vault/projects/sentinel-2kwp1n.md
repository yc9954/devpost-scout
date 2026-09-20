---
slug: "sentinel-2kwp1n"
url: "https://devpost.com/software/sentinel-2kwp1n"
title: "Sentinel"
hackathon: "LMA EDGE Hackathon"
organization: "LMA"
winner: true
words: 661
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Sentinel

> Protecting lender capital from collateral stripping and priming risks using bank-grade Agentic AI.

[Devpost](https://devpost.com/software/sentinel-2kwp1n) · hackathon [[LMA EDGE Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[realtime_stream]]
**domain** [[civic_government]] [[finance_payments]] [[legal_justice]] [[mental_health]] [[security_privacy]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** docker, fastapi, framer-motion, generative-ai, google-gemini, next.js, pdfplumber, postgresql, python, react, render, sqlalchemy, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sentinel

## Body

Inspiration The leveraged loan market is facing an existential crisis. Since the landmark J.Crew (2016) and Serta Simmons (2020) transactions, lenders have lost billions of dollars to "Liability Management Transactions" (LMTs). Aggressive financial sponsors are exploiting minute loopholes in credit agreements to strip collateral ("Dropdowns") or prime existing lenders ("Uptiers"). Reviewing a 400-page credit agreement for these specific, often hidden, risks takes senior legal counsel days of expensive billable hours. We realized that in a high-speed syndication process, manual review is a dangerous bottleneck. We built Sentinel to be the autonomous shield that never sleeps—providing bank-grade defense against capital destruction. What it does Sentinel is an Agentic AI platform tailored for Syndicate Desks, CLO Managers, and Credit Risk Officers. It autonomously analyzes credit agreements to detect specific LMT vulnerabilities. Autonomous Vulnerability Detection: It instantly flags "True Serta Gaps" (missing lien subordination protections) and "J.Crew Trapdoors" (uncapped investment baskets). Nuanced Legal Analysis: Unlike generic AI, Sentinel distinguishes between a missing protection (Critical Risk) and a weakened carve-out (High Risk). Automated Remediation: It doesn't just find the problem; it drafts the fix. Users get specific "Blocker Language" redlines to paste directly into the draft. Portfolio Comparison: Benchmarks new deals against historical precedents (e.g., Titan vs. Atlas) to visualize relative risk. Executive Intelligence: Generates C-suite summaries focusing exclusively on financial exposure and recovery scenarios. How we built it We rejected the standard "Chat with PDF" approach in favor of a sophisticated Multi-Agent Architecture : The Engine: We built a Python/FastAPI backend that orchestrates five specialized AI Agents using Google Gemini Pro . Agent 1 (Lien Specialist): Scans Article IX for unanimous consent gaps. Agent 2 (Basket Specialist): Calculates leverage-based capacity in Section 6.04. Agent 3 (Structure Specialist): Checks for Unrestricted Subsidiary designation loopholes. The Brain: We developed a proprietary Risk Scoring Engine that weighs vulnerabilities based on LSTA and LMA market standards to calculate a composite "Risk Score" (0-100). The Interface: The frontend is built with Next.js 15 and Tailwind CSS , featuring a "Glassmorphism" aesthetic designed to look and feel like a premium institutional terminal (Bloomberg/Palantir). We used Framer Motion for data visualization to make risk tangible. Challenges we ran into The "Negative Detection" Problem: AI is good at finding text that is there. It is terrible at finding text that isn't there. Detecting a "Serta Gap" requires identifying the absence of a specific clause in a list of 10+ items. We solved this by prompt-engineering a "Missing Protection Check" agent that validates against a negative template. Legal Nuance: Early versions flagged standard market terms as risks. We had to fine-tune the agents to understand "Permitted Liens" and standard carve-outs so that the system only flags material deviations from market standards. PDF Parsing: Credit agreements are dense, poorly formatted, and often 300+ pages. We implemented a robust parsing pipeline using pdfplumber with fallback strategies to ensure we captured every footnote and schedule. Accomplishments that we're proud of Commercial Viability: The tool produces output that is immediately actionable. The "Blocker Language" feature directly reduces legal drafting time. The "True Gap" Logic: Successfully teaching an AI to differentiate between a "Missing Protection" (Severity 10) and a "Carve-out" (Severity 7). Speed: Reducing a 2-day manual legal review process to a 45-second automated scan. What we learned We learned that Loan Documents are essentially code that compiles into money. Just like software has security vulnerabilities, credit agreements have bugs. We learned that by treating legal text as structured data, we can apply the same rigor to financial contracts that we apply to software security. What's next for Sentinel LMA Specifics: While currently benchmarked heavily against US LSTA precedents (where LMTs originated), we plan to fine-tune the model specifically for EMEA-based LMA documentation as these risks migrate to Europe. LMS Integration: Integrating directly with Loan Management Systems (like Finastra or LoanIQ) to scan portfolios in real-time. Negotiation Bot: An agent that not only suggests blockers but negotiates terms via email drafts based on the lender's risk appetite. <div