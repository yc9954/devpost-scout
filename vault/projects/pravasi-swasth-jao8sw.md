---
slug: "pravasi-swasth-jao8sw"
url: "https://devpost.com/software/pravasi-swasth-jao8sw"
title: "MEDIBUDDY"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 502
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
---

# MEDIBUDDY

> secure Health data like Bitcoin

[Devpost](https://devpost.com/software/pravasi-swasth-jao8sw) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]
  <sub>weak: financial_record, medical_record, structured_db, video_visual</sub>

**stack** ai, amazon-web-services-(aws)-or-google-cloud-platform-(gcp)-for-hosting-the-application, and-ai-models.-services-like-aws-lambda-for-serverless-functions, aws-s3-for-media-storage, databases, fabric, gcp's, hyperledger

## Body

MediBuddy: Enterprise Healthcare Intelligence 🌟 Inspiration The pharmaceutical landscape is a labyrinth of rapidly changing prices, complex insurance formularies, and critical safety data. Healthcare professionals often spend hours toggling between disparate portals to find out if a drug is covered or what its real-world cost will be for a patient. We built MediBuddy to consolidate this "fragmented intelligence" into a single, real-time clinical co-pilot that puts patient access and safety first. 💊 What it does MediBuddy is an AI-powered platform providing instant pharmaceutical and reimbursement intelligence: Real-Time 5-Layer Pharma Brain: Monitors 40,000+ data sources to give live updates on drug shortages, price drops, and formulary changes. Payer Coverage Intel: Instant tier and PA (Prior Authorization) status for over 4,800 commercial, Medicare, and Medicaid plans. Pricing Intelligence: Transparent access to AWP, WAC, NADAC, and cash prices (GoodRx/CostPlus) to find the most affordable patient options. Clinical Guardrails: Built-in major interaction checking and automated Prior Auth form generation with clinical justification. AI Chat Assistant: A specialized LLM agent that can answer complex queries like "Is there a cheaper alternative to Eliquis covered by Aetna?" 🏗️ How we built it Backend: Powered by FastAPI for high-performance asynchronous request handling. AI Engine: Implemented using LangChain with Hugging Face (Mistral-7B) to provide accurate, data-backed pharmaceutical responses. Intelligence Layer: A custom-built Atomic Knowledge Graph that handles real-time data ingestion and validates changes before they hit the UI. Frontend: A sleek, premium dashboard built with Vanilla JS/CSS, featuring a command palette (Ctrl+K) for rapid medical lookups. Deployment: Optimized for both Docker (containerized performance) and Vercel (serverless scalability). 🚧 Challenges we ran into Real-Time Data Ingestion: Building a "Firehose" that can simulate and handle thousands of updates without performance degradation. Serverless Nuances: Adapting a system designed for persistent background agents (Pharma Brain) and WebSockets to work within the ephemeral environment of Vercel Serverless Functions. Data Integrity: Ensuring the AI agent cites specific data points (NDC codes, Tier levels) rather than hallucinating, which we solved through a "Context-Injection" fallback mechanism. 🏆 Accomplishments that we're proud of The 5-Layer Architecture: Creating a system that separates raw data ingestion (Firehose) from the validated source of truth (Knowledge Graph). Prior Auth Automation: Successfully generating clinical justifications that match insurance-specific criteria in under 2 seconds. Global Pricing Engine: Implementing a geographic multiplier system that adjusts drug costs based on local markets (UK, India, US States). 📚 What we learned We deepened our understanding of the FHIR/HL7 conceptual space and the criticality of National Drug Codes (NDC) as a universal identifier. Learned how to design high-performance FastAPI-lifespan events to initialize complex internal engines (like the Pharma Brain) during startup. Gained significant insight into Serverless-First architecture and how to manage persistent state in ephemeral environments. 🚀 What's next for MEDIBUDDY EMR Integration: Connecting directly to hospital systems via HL7/FHIR for patient-specific coverage checking. Predictive Analytics: Implementing ML models to predict future drug shortages or price spikes before they happen. Multi-Modal AI: Adding the ability for pharmacists to upload prescription photos or insurance cards for instant AI analysis. <div