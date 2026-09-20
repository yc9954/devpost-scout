---
slug: "nova-insurance-claims-ai"
url: "https://devpost.com/software/nova-insurance-claims-ai"
title: "Nova Insurance Claims AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 725
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "user/government_staff"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Nova Insurance Claims AI

> Multi-agent AI pipeline that automates insurance claims processing using Amazon Nova 2 Lite - from document review to fraud detection to decision letters, with full explainability

[Devpost](https://devpost.com/software/nova-insurance-claims-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[legal_justice]]
**user** [[government_staff]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[medical_record]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, bedrock, docker, huggingface, python, strands, streamlit

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for nova insurance claims ai

## Body

Problem features Pipeline Architecture Impact Inspiration Insurance companies process millions of claims every year. Each claim passes through document review, fraud investigation, underwriting assessment, compliance checks, and customer communication - mostly manually. This is slow (weeks per complex claim), expensive, and error-prone. As an analytics leader working in insurance, I see this problem daily. I built Nova Insurance Claims AI to demonstrate how Amazon Nova's reasoning capabilities can automate the entire claims lifecycle with full transparency and regulatory compliance. What it does Nova Insurance Claims AI is an agentic AI platform that processes insurance claims through a 5-stage multi-agent pipeline : Document Review Agent - Gathers all relevant data: claim details, applicant profile, policy coverage, medical records, and similar historical claims Fraud Detection Agent - Analyzes fraud indicators, timing patterns, claim history, and red flags with a risk score (0-100) Decision Agent - Makes the final approve/deny/investigate decision with a settlement recommendation and confidence range Compliance Agent - Reviews the decision for regulatory compliance, bias, fair claims practices, and legal risk Decision Letter Agent - Auto-generates a professional policyholder notification letter Additional Modules Settlement Recommendation Engine - Data-driven settlement amounts based on historical comparables with confidence intervals Risk Dashboard - 8 interactive charts showing portfolio analytics, fraud distribution, and risk heatmaps Smart Claim Intake - AI-powered form with pre-fill from policy data and real-time validation Free-form Chat - Ask anything about the insurance data using natural language Key Differentiators Explainable AI : Every decision includes Nova's full reasoning chain for regulatory audit trails Real Data : Tested on 1,000 real insurance claims from Kaggle with 247 confirmed fraud cases (24.7%) 6 Specialized Agents with 11 custom tools working autonomously End-to-end automation : From claim intake to decision letter in minutes, not weeks How I built it Amazon Nova 2 Lite ( us.amazon.nova-2-lite-v1:0 ) via Amazon Bedrock for all AI reasoning Strands Agents SDK (AWS open-source) for agent orchestration - each agent has a distinct role, system prompt, and tool set 11 Custom Tools : data lookup, policy validation, similarity search, settlement benchmarking, damage photo analysis (multimodal), portfolio analytics Streamlit for the interactive web UI with 9 modules Real Kaggle dataset (1,000 auto insurance claims with fraud labels) converted into our app format Docker deployment on Hugging Face Spaces Architecture Streamlit UI (9 modules) | Strands Agents SDK (6 agents) | 11 Custom Tools (data, search, analysis) | Amazon Nova 2 Lite (Bedrock) Challenges I ran into Agent prompt engineering : Getting each agent to stay focused on its specific role without overstepping into other agents' responsibilities required careful system prompt design Pipeline data flow : Passing structured context between agents while keeping token usage efficient - earlier agents' outputs feed directly into later agents' prompts Fraud score calibration : Mapping the Kaggle dataset's binary fraud labels to a nuanced 0-5 fraud indicator scale that gives agents more signal to work with Settlement benchmarking : Building statistical comparison tools that find genuinely similar historical claims by type and amount range Accomplishments that I'm proud of Full end-to-end pipeline : A claim goes in, and a professional decision letter comes out - fully automated Real-world data : Not synthetic demos - 1,000 actual insurance claims with real fraud patterns Explainable AI : Every decision is transparent and auditable, which is a regulatory requirement in insurance 6 agents working together : Each agent trusts the previous agent's output and builds on it Production-ready architecture : Dockerized, deployed, and publicly accessible What I learned Strands Agents SDK makes it remarkably simple to build sophisticated multi-agent systems - an agent is just a model + tools + prompt Amazon Nova 2 Lite delivers impressive reasoning quality at very low cost - ideal for high-volume claims processing The key to multi-agent systems is clear role separation - each agent must know exactly what it's responsible for and what it's not Insurance AI needs explainability above all else - regulators and customers both demand it What's next for Nova Insurance Claims AI Nova Sonic integration for voice-based claim intake (policyholders call and describe their claim) Nova Act for automated browser-based policy comparison across carrier websites DynamoDB/S3 backend replacing local JSON for enterprise-scale deployments Amazon Bedrock AgentCore for managed, serverless agent deployment Fine-tuned Nova models trained on proprietary insurance data for higher accuracy Multi-language support leveraging Nova 2 Lite's 200+ language capabilities <div