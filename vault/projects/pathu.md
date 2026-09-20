---
slug: "pathu"
url: "https://devpost.com/software/pathu"
title: "SentinelChain"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 713
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# SentinelChain

> Realtime Supply Chain Threat Monitoring Engine

[Devpost](https://devpost.com/software/pathu) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[disaster_emergency]] [[finance_payments]] [[security_privacy]] [[supply_logistics]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** fastapi, gnews, pathway, react.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sentinelchain
- tracks applied
- learn more

## Body

Landing Page Registration Page Computational Threats Operational and Geopolitical Threats Reputational Threats Inspiration The inspiration for Sentinel Chain stems from the critical need for "Live Intelligence" in global operations. Traditional Retrieval-Augmented Generation (RAG) systems often suffer from a "knowledge gap"—the time between a real-world event occurring and the system indexing that data. We realized that for supply chains and corporate compliance, a delay of even a few hours can lead to catastrophic disruptions. We set out to build a system that moves at the speed of the internet, transforming static data into a living, breathing sentinel that guards against geopolitical, operational, and reputational risks as they happen. What it does Sentinel Chain is a real-time intelligence and compliance monitoring platform that provides three core modules through a unified dashboard: Supply Chain Threat Monitoring: Detects geopolitical and operational threats (like strikes or disasters) in real-time using streaming CSV data and LLM validation. Compliance Engine: Integrates directly with Google Drive to analyze company documents against threat policies, providing AI-powered transaction risk assessments. Reputational Risk Monitoring: Monitors news streams to detect and categorize company-specific threats such as fraud, impersonation, or operational complaints. Adaptive RAG: Uses an iterative retrieval process that expands its search context if the initial data is insufficient to answer a query accurately. How we built it The platform is built on a high-performance streaming architecture orchestrated via Docker Compose : Core Engine: We used Pathway for its unique ability to perform real-time indexing and hybrid search (KNN + BM25) on data streams. AI/LLM: We integrated Gemini 2.0 Flash for threat validation and complex reasoning, ensuring that only genuine risks trigger alerts. Data Integration: Built custom connectors for Google Drive , real-time CSV streams, and JSONL news files. Backend: Developed multiple microservices using FastAPI to serve as proxies between the RAG engine and the user. Frontend: A production-ready React 18 dashboard with Tailwind CSS and Recharts for real-time data visualization. Challenges we ran into Data Sync Latency: Coordinating real-time updates from disparate sources—like Google Drive, live CSV streams, and local files—required careful management of Pathway's streaming state. LLM Consistency: Tuning the LLM validators to distinguish between "noise" and "genuine threats" across different categories (Fake vs. Legitimate companies) required extensive prompt engineering. Windows Compatibility: As Pathway is natively Linux-optimized, we had to build a robust multi-container Docker environment to ensure seamless performance and environment parity across different operating systems. Accomplishments that we're proud of True Real-Time RAG: Successfully built a system where adding a file to a Google Drive folder or updating a spreadsheet instantly updates the "knowledge" of the AI without manual re-indexing. Multi-Source Fusion: Our ability to cross-reference live threat alerts with internal company policies stored in the cloud to produce a single, coherent risk report. Adaptive Intelligence: Implementing an "Adaptive RAG" pipeline that knows when it doesn't have enough information and automatically digs deeper into the document store. What we learned The Power of Streaming: We learned that treating data as a "stream" rather than a "database" fundamentally changes how AI can be applied to time-sensitive industries like finance and logistics. Infrastructure over Models: While LLMs are powerful, the "plumbing"—Docker orchestration, Nginx serving, and data connectors—is what makes an AI application production-ready. Hybrid Search Utility: We discovered that combining vector search (KNN) with traditional keyword search (BM25) is essential for finding specific technical details in complex compliance documents. What's next for SentinelChain Multimodal Expansion: Integrating vision-language models (like GPT-4o) to parse complex tables and charts within financial reports more accurately. Predictive Alerting: Moving from reactive threat detection to predictive modeling, using historical logs to forecast potential supply chain bottlenecks. Enterprise Connectors: Adding native support for enterprise platforms like SharePoint, Slack, and SAP for automated remediation workflows.1 Tracks Applied We are submitting Sentinel Chain under the following tracks: AI-Driven Commercial Decision Systems Data Science & Business Analytics Business Management & Consultancy Solutions These tracks best align with our system’s core goal: enabling real-time, AI-powered decision-making for enterprises operating in dynamic and high-risk environments. Learn More For a deeper understanding of the system architecture, full data pipeline, and technical design: Detailed Technical Document (Architecture + Data Pipeline): https://drive.google.com/file/d/1wzJ7VheJi3i5X4VVtX4jUwijnSpevmdy/view?usp=sharing This document includes: End-to-end data flow (stream ingestion → indexing → validation → alerting) Adaptive RAG pipeline design Microservices architecture breakdown Deployment and scaling strategy <div