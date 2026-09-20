---
slug: "in-progress-2awbie"
url: "https://devpost.com/software/in-progress-2awbie"
title: "qAPIbara"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 640
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# qAPIbara

> qAPIbara — AI-Powered Regression Testing

[Devpost](https://devpost.com/software/in-progress-2awbie) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[sensor_telemetry]]

**stack** javascript, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for in progress

## Body

🧩 qAPIbara Version Smarter. Debug Faster. Inspiration APIs evolve fast—but debugging breaking changes, regressions, or inconsistencies between versions is slow, repetitive, and often manual. QA engineers spend hours testing the same endpoints, comparing JSONs, and writing endless test cases that could be automated. We built qAPIbara to transform API regression testing into an intelligent, explainable, and predictive process—bridging the gap between development speed and testing reliability. Who is affected: QA engineers managing large microservice systems DevOps teams deploying frequent API updates Backend developers debugging regressions Enterprises maintaining multiple API versions Why it matters: When APIs break, entire workflows fail—from insurance claims to banking transactions. Detecting and understanding why an API failed shouldn't take hours. qaPIbara makes regression detection, diagnosis, and recovery intelligent, fast, and explainable. What it does qAPIbara is an AI-powered regression analysis platform that automatically compares, tests, and explains API version differences. It enables users to: 🔍 Compare API Versions — Detect differences between v1 and v2 responses instantly 🧠 Generate & Run Tests Automatically — Let Nemotron design test cases and execute them in bulk 💬 Explain Regressions with Gemini AI — Receive human-readable explanations and fix suggestions 🌐 Visualize Trends & Health — Heatmaps, endpoint maps, and dashboards reveal overall service health Key Flows: Input two API versions → Run automated diff → Get visual comparison & AI-driven summary Generate, run, and export test cases automatically View and interpret service health using intelligent visualization Main Features 🧩 Version Comparison Engine — Detects key structural and semantic changes between API versions 🤖 Nemotron Workflow Automation — Plans and executes version comparison workflows end-to-end 🧠 Gemini Regression Insights — Explains issues in plain English and suggests fixes 📊 Regression Heatmap — Visual view of breaking changes across endpoints 📈 Service Health Scoring — Quantifies the stability of new releases 💬 AI Chat Interface — Natural language debugging and recommendations 🔐 Auth0 Security — Role-based access, audit logging, and consent-driven workflow How we built it Frontend: React with a modern dark-neon UI Interactive JSON diff viewer and comparison dashboard Framer Motion for smooth transitions and visual feedback Backend: FastAPI orchestrating version comparisons Integration with Nemotron for workflow planning Gemini API for regression explanations Firestore for data storage Auth0 for secure multi-user access Challenges we ran into Accurate Diffing: Designing a comparison engine that identifies meaningful API differences, not noise (like timestamps or IDs). Real-time AI Integration: Balancing response time with detailed, contextual explanations from Gemini. Workflow Automation: Letting Nemotron generate test cases that reflect realistic edge scenarios. Data Visualization: Building intuitive visual tools (like regression heatmaps) that QA engineers can act on instantly. Accomplishments that we're proud of Fully functional regression analysis platform built in under 24 hours Integrated Nemotron + Gemini for automated diagnosis and explanations Deployed modular, scalable backend with Vultr Cloud Delivered explainable AI for QA — not just detection, but understanding What we learned How to connect LLMs to structured testing workflows The power of explainable AI for debugging complex systems Effective visualization design for large-scale data comparison Seamless integration between FastAPI, React, and multi-LLM systems We were surprised by: How often small JSON schema changes caused large downstream regressions How effectively Gemini could explain subtle data mismatches in natural language How much faster QA cycles became with AI-in-the-loop What's next for in progress 🌐 Integrate live API monitoring and anomaly alerts 📱 Mobile dashboard for real-time regression insights 🧠 Predictive models for preventing regressions before they occur 🧾 Automated fix generation and pull request suggestions 🚀 Check It Out GitHub Repository: https://github.com/nathanhanxp/qAPIbara 📈 Impact Metrics Potential Users: 25,000+ QA engineers across enterprise software teams 10,000+ DevOps and backend engineers performing version testing daily User Value: Up to 80% faster regression diagnosis Automated test generation in under 1 minute Explainable summaries for non-technical stakeholders Cost savings from reduced manual QA hours and production rollbacks <div