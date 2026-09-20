---
slug: "auditease-4ub1mj"
url: "https://devpost.com/software/auditease-4ub1mj"
title: "AuditEase"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 727
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# AuditEase

> Eco Friendly AI-Powered Compliance Platform

[Devpost](https://devpost.com/software/auditease-4ub1mj) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[legal_justice]]
**user** [[developer]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]
  <sub>weak: code_repository</sub>

**stack** api, css, gemini, postgresql, react, shadowncn, supabase, tailwind, typescript, vite

## How they structured the write-up

- track selection
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments
- what we learned
- what's next for auditease

## Body

AuditEase Hero Section – AI-Powered Contract Analysis Personalized User Command Center & Sustainability Tracker Intelligent Support Hub with AI Assistant Access and FAQs Automated Compliance Pipeline – Document Upload & Selection Interactive Risk Assessment & Liability Exposure Analysis Context-Aware "Chat with Contract" Document Intelligence Automated Contract Remediation & Legal Rewrite Engine AuditEase Tiered SaaS Subscription Plans with Dark Mode Secure Compliance Repository & Standards Management Track Selection Primary Track: Artificial Intelligence and LLM Applications Secondary Tracks: Cybersecurity & Data Privacy / Productivity & Workflow Automation Inspiration As a team, we realized that legal compliance is often a "black box" for small to mid-sized businesses. We saw how hiring a legal team for a SOC 2 or GDPR audit costs thousands of dollars and takes weeks of manual back-and-forth. We were inspired to bridge this gap by building an "AI Auditor" that democratizes legal expertise—giving businesses a clear, instant look at their liabilities and compliance gaps without the prohibitive price tag. What it does We built AuditEase as an intelligent SaaS platform that automates the heavy lifting of legal auditing. The Auditor: Our system allows users to upload contracts and compare them against regulatory standards like HIPAA or GDPR. The AI identifies "Compliance Gaps," categorizes risks from Critical to Low, and even estimates potential financial liability. The Dashboard: We designed a centralized hub that visualizes a company's compliance health score through interactive, easy-to-read charts. Contextual Chat: We integrated a "Chat with Document" feature so users can ask our AI specific questions like, "What are the termination conditions?" or "Does this meet Article 5 of GDPR?" Secure Storage: Since we are handling sensitive legal data, we built a bank-grade environment where every document is protected by strict encryption and isolation. How we built it Our team prioritized a modern, type-safe stack to ensure AuditEase is as robust as it is fast. We used React 18 and TypeScript, powered by Vite for a snappy developer experience. For the UI, we leaned on Shadcn UI and Tailwind CSS to give the platform a professional, enterprise feel. We integrated Google Gemini 2.5 Flash as our core engine. We spent a lot of time on prompt engineering to ensure the AI returns structured JSON, allowing us to map risks directly to our dashboard components. We chose Supabase (PostgreSQL) for our database and authentication. We implemented Row Level Security (RLS) at the database level. This was a non-negotiable for us to ensure total user data isolation. We used Recharts for our data visualizations and jsPDF so users can download and share their audit reports instantly. Challenges we ran into Getting the AI to consistently output valid, structured JSON instead of conversational text was a major hurdle. We went through dozens of iterations to ensure our data pipeline wouldn't break. Legal contracts are long and complex. We had to optimize our text extraction process to ensure we stayed within model context windows while maintaining 100% accuracy across 50+ page PDFs. Implementing a freemium model was trickier than we expected. We had to write custom SQL triggers in Supabase to automatically track and enforce audit limits for our users. Accomplishments We are incredibly proud of achieving sub-10-second analysis for complex legal documents that would normally take a human hours to review. As a team, we successfully integrated a complex AI engine with a secure serverless backend, maintaining a "Security First" mindset throughout the build. We managed to take "dry" legal data and turn it into a beautiful, interactive dashboard that provides genuine value at a glance. What we learned We learned that LLMs are most powerful when used to turn unstructured "messy" text into clean, actionable data objects. This project deep-dived our understanding of database-level security. We learned that "Defense in Depth" is the only way to build trust in a SaaS product. Building AuditEase taught us how to quickly pivot our technical approach when faced with model limitations or integration bugs. What's next for AuditEase We want to allow users to audit entire folders of contracts at once to find inconsistencies across their whole company. Our next goal is to move beyond just finding risks. We want AuditEase to automatically suggest and rewrite clauses to make them 100% compliant. We plan to build "connectors" for Google Drive, Slack, and CLM tools so that compliance auditing becomes a seamless part of a company's existing workflow. <div