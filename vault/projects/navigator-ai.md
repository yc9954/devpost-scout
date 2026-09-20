---
slug: "navigator-ai"
url: "https://devpost.com/software/navigator-ai"
title: "Navigator-AI"
hackathon: "The AI Champion Ship "
organization: "LiquidMetalAI"
winner: true
words: 475
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# Navigator-AI

> AI-powered healthcare referral automation tackling the $150B annual industry crisis. Automates document extraction to appointment confirmation using Raindrop orchestration and Vultr cloud deployment.

[Devpost](https://devpost.com/software/navigator-ai) · hackathon [[The AI Champion Ship]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[medical_record]] [[structured_db]]

**stack** node.js, raindrop, react, vultr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for navigator-ai

## Body

Navigator AI Inspiration Healthcare systems in the U.S. are hemorrhaging over $150 billion annually due to referral mismanagement. Nearly half of all referrals never complete , costing individual hospitals $200-500M per year while patients waste $1.9B in unnecessary expenses. We set out to solve this crisis with AI-powered automation. What it does Navigator-AI automates the entire healthcare referral workflow from document upload to appointment confirmation: AI-Powered Extraction : Automatically extracts patient and provider information from referral documents using multi-model AI (95%+ accuracy) Smart Orchestration : Uses Raindrop's workflow engine to intelligently route referrals, schedule appointments, and track status Real-Time Dashboard : Provides coordinators with live visibility into every referral's progress Patient Portal : Enables patients to confirm appointments and receive notifications Cloud-Native : Deployed on Vultr infrastructure for enterprise scalability How we built it Technology Stack: Backend : Node.js API server with Raindrop integration (SmartSQL, SmartMemory, AI, Object Storage) Frontend : Next.js with React for responsive UI AI/ML : Raindrop's multi-model AI for document extraction Cloud Infrastructure : Vultr for production deployment (VM, storage, networking) Database : PostgreSQL via Raindrop SmartSQL Storage : Raindrop Object Buckets for document management Architecture: Mono-repo structure with separate frontend, backend, and extraction service components. Backend handles RESTful API endpoints documented with OpenAPI, while frontend provides intuitive upload forms and real-time dashboards. Challenges we ran into Document Variability : Medical referral forms come in dozens of formats - we had to train our extraction pipeline to handle diverse layouts State Management : Coordinating complex workflows across multiple stakeholders required careful orchestration design HIPAA Compliance : Ensuring secure data handling throughout the pipeline Cloud Deployment : Setting up production-ready infrastructure on Vultr with proper networking and security Accomplishments that we're proud of ✅ End-to-end workflow completion in under 2 minutes ✅ 95%+ extraction accuracy on structured medical forms ✅ Successfully deployed production system on Vultr cloud ✅ Addressing a $67.92B market opportunity (projected by 2034) ✅ API-first design ready for EHR integration ✅ Complete demo with real referral documents (anonymized) What we learned How to leverage Raindrop's powerful orchestration capabilities for complex healthcare workflows Best practices for deploying scalable cloud infrastructure on Vultr The critical importance of healthcare referral management and its massive economic impact Techniques for handling diverse document formats with AI extraction What's next for Navigator-AI EHR Integration : Connect with Epic, Cerner, and other major EHR systems Advanced Analytics : Predictive insights for referral leakage prevention Multi-language Support : Expand to serve diverse patient populations Mobile App : Native iOS/Android apps for coordinators and patients Enterprise Features : Multi-facility management, custom workflows, advanced reporting AI Improvements : Fine-tune models for specialty-specific referral types Market Validation : With the patient referral management software market growing from $16.14B in 2025 to $67.92B by 2034 (17.31% CAGR), Navigator-AI is positioned to capture significant value while solving a critical healthcare problem. <div