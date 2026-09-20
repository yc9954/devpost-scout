---
slug: "auditease-f1pqzw"
url: "https://devpost.com/software/auditease-f1pqzw"
title: "AuditEase"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 754
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# AuditEase

> Eco Friendly AI-Powered Compliance Platform

[Devpost](https://devpost.com/software/auditease-f1pqzw) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[climate_energy]] [[developer_tools]] [[finance_payments]] [[legal_justice]] [[security_privacy]] [[supply_logistics]]
**user** [[developer]] [[government_staff]]
**substrate** [[document_pdf]] [[geospatial]] [[regulation_legal_text]] [[structured_db]]
  <sub>weak: code_repository</sub>

**stack** api, css3, gemini, postgresql, react, shadowcn, supabase, tailwind, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments
- what we learned
- what's next for auditease

## Body

AuditEase Hero Section – AI-Powered Contract Analysis Personalized User Command Center & Sustainability Tracker Intelligent Support Hub with AI Assistant Access and FAQs Automated Compliance Pipeline – Document Upload & Selection Interactive Risk Assessment & Liability Exposure Analysis Context-Aware "Chat with Contract" Document Intelligence Automated Contract Remediation & Legal Rewrite Engine Secure Compliance Repository & Standards Management AuditEase Tiered SaaS Subscription Plans with Dark Mode Inspiration As a team, we realized that while companies make bold promises about sustainability, enforcing environmental compliance in corporate contracts and supply chains is a "black box." We saw how businesses struggle to verify if their vendors actually comply with environmental standards like the EPA guidelines, the EU Deforestation Regulation, or Corporate Sustainability Reporting Directives (CSRD). We already knew how hard standard legal compliance was, so we were inspired to use our technical expertise to build an "AI Environmental Auditor." AuditEase democratizes green legal expertise—giving businesses an instant look at their environmental liabilities, supply chain eco-compliance gaps, and "greenwashing" risks without the prohibitive price tag. What it does We built AuditEase as an intelligent SaaS platform that automates the heavy lifting of legal auditing. The Auditor: Our system allows users to upload vendor contracts or supply chain agreements and compare them against regulatory standards. The AI identifies "Compliance Gaps," categorizes risks from Critical to Low, and estimates potential financial liability for violations (including environmental and governance breaches). The Dashboard: We designed a centralized hub that visualizes a company's compliance health score through interactive, easy-to-read charts. Contextual Chat: We integrated a "Chat with Document" feature so users can ask our AI specific questions like, "Does this supplier agreement mandate zero-deforestation?" or "What are the waste management liabilities?" Secure Storage: Since we are handling sensitive corporate data, we built a bank-grade environment where every document is protected by strict encryption. How we built it Our team prioritized a modern, type-safe stack to ensure AuditEase is as robust as it is fast. We used React 18 and TypeScript, powered by Vite for a snappy developer experience. For the UI, we leaned on Radix UI and Tailwind CSS to give the platform a professional, enterprise feel. We integrated Google Gemini 2.5 Pro as our core engine. We utilized the Google Gemini API to ingest extracted contract text and cross-reference it against regulatory frameworks, leveraging its large context window and fast inference to perform real-time legal analysis and calculate liability exposure. We chose Supabase (PostgreSQL) for our database and authentication. We implemented Row Level Security (RLS) at the database level—a non-negotiable for us to ensure total user data isolation. We used Recharts for our data visualizations. Challenges we ran into Getting the AI to consistently output valid, structured JSON instead of conversational text was a major hurdle. We went through dozens of iterations to ensure our data pipeline wouldn't break. Legal and compliance contracts are notoriously long and complex. We had to optimize our text extraction process to ensure we stayed within model context windows while maintaining 100% accuracy across 50+ page PDFs. Implementing a freemium model was also trickier than we expected, requiring us to write custom SQL triggers in Supabase to automatically track and enforce audit limits. Accomplishments We are incredibly proud of achieving sub-60-second analysis for complex legal documents that would normally take a human hours to review. As a team, we successfully integrated a complex AI engine with a secure serverless backend, maintaining a "Security First" mindset throughout the build. We managed to take "dry" compliance data and turn it into a beautiful, interactive dashboard that provides genuine value to a CFO or Sustainability Officer at a glance. What we learned We learned that LLMs are most powerful when used to turn unstructured "messy" text into clean, actionable data objects. This project deep-dived our understanding of database-level security and Prompt Engineering. We learned that "Defense in Depth" is the only way to build trust in a SaaS product. Building AuditEase taught us how to quickly pivot our technical approach when faced with model limitations or integration bugs. What's next for AuditEase The Environmental Library: Expanding our AI's standard library to specifically ingest and map global climate regulations (Clean Water Act, Carbon Emission mandates, CSRD). Greenwashing Detector: Building a feature that compares a company's public marketing claims against the actual environmental clauses enforced in their legal contracts. Auto-Redlining for the Earth: Moving beyond just finding risks, we want AuditEase to automatically suggest and rewrite contract clauses to ensure 100% eco-compliance (e.g., auto-inserting mandatory recycling or emission-cap clauses into vendor agreements).. <div