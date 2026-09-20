---
slug: "meddevice-cyberguard"
url: "https://devpost.com/software/meddevice-cyberguard"
title: "MedDevice CyberGuard"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 820
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# MedDevice CyberGuard

> AI-powered multi-agent system that produces FDA-ready cybersecurity risk dossiers for medical devices in minutes — using Amazon Nova to automate 6 weeks of manual compliance work.

[Devpost](https://devpost.com/software/meddevice-cyberguard) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[developer_tools]] [[health_clinical]] [[security_privacy]] [[supply_logistics]]
**user** [[patient_family]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** c, css, docker, html, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for meddevice cyberguard

## Body

MedCyberGaurd Architecture Overview Inspiration In 2024, the FDA mandated cybersecurity documentation for all new medical device submissions under the Consolidated Appropriations Act. As a team with hands-on experience shipping medical device firmware under IEC 62304 in production, we have seen firsthand how manufacturers struggle with this requirement. Compliance teams spend 6 to 12 weeks manually preparing cybersecurity risk dossiers: mapping code vulnerabilities to FDA guidance, analyzing communication protocols, building threat models, and generating SBOMs. Meanwhile, hospitals are deploying thousands of connected devices with unknown security postures. A compromised infusion pump or sterilizer is not just a data breach. It is a patient safety issue. We saw an opportunity: what if AI agents could automate the entire cybersecurity assessment workflow and produce an FDA-ready dossier in minutes? What it does MedDevice CyberGuard is a multi-agent system powered by Amazon Nova that performs end-to-end cybersecurity assessment of connected medical devices. Input: Device firmware (C/Python), IoT communication logs, network architecture diagrams, device specifications Output: A structured cybersecurity risk dossier containing: SAST findings with medical device context (patient safety impact, IEC 62304 safety class) Protocol conformance analysis (IoT communication deviations from spec) Regulatory compliance mapping (FDA, IEC 62443, IEC 62304, Health Canada) STRIDE threat model Software Bill of Materials (SBOM) Architecture security analysis with IEC 62443 zone/conduit violations Risk score and prioritized remediation roadmap How we built it Multi-Agent Architecture (Strands Agents + Amazon Nova 2 Lite): Code Security Analyst: Runs real Semgrep static analysis and Syft SBOM generation, then uses Nova to contextualize each finding for medical device risk (patient safety impact, attack vectors, exploitability) Protocol Conformance Analyst: Parses IoT communication logs and validates against the device specification, identifying deviations such as unauthorized clients, schema violations, forbidden topics, and QoS mismatches Regulatory Compliance Mapper: Uses RAG over FDA/IEC regulatory documents (Bedrock Knowledge Bases + S3) to map every finding to specific regulatory requirements Report Synthesizer: Uses Nova Multimodal Understanding to analyze architecture diagrams for zone segmentation issues, then merges all agent outputs into a unified dossier Key Design Decision: Agents use real security tools (Semgrep, Syft, JSON Schema validators). Nova reasons over tool outputs rather than attempting raw code analysis. This ensures findings are accurate and defensible. Infrastructure: Amazon Bedrock (Nova 2 Lite for reasoning, Nova Multimodal for diagram analysis) Bedrock Knowledge Bases with S3 data source (regulatory documents) AWS Lambda (containerized agents with Semgrep/Syft) DynamoDB (scan state), S3 (artifacts/reports) React + Tailwind UI with real-time agent status Cost optimization: Used S3 + Bedrock Knowledge Bases instead of OpenSearch Serverless, reducing RAG infrastructure cost from $700/month to ~$8 total for the hackathon. Challenges we ran into LLM reliability for security findings: We initially considered having Nova perform SAST directly, but this produces hallucinated vulnerabilities. Solution: agents invoke real tools and Nova only interprets results. IoT protocol anomaly detection: LLMs cannot do statistical anomaly detection reliably. We reframed this as protocol conformance analysis: Nova compares logs against a specification document, which it excels at. Regulatory document copyright: We cannot distribute full IEC standards. We created comprehensive regulatory summaries that capture requirement structure and citations for RAG without violating copyright. Multimodal prompt engineering: Getting consistent structured output from Nova Multimodal for architecture diagrams required careful prompt design with explicit JSON schema and IEC 62443 zone/conduit terminology. Agent orchestration complexity: Coordinating 4 agents with inter-agent data dependencies. Strands Agents SDK made this manageable with clean tool definitions and structured output schemas. Accomplishments that we're proud of Real tools + AI reasoning: Not just "ChatGPT for security." Every finding is backed by actual static analysis, then enriched with medical device context. Regulatory accuracy: RAG over real FDA/IEC guidance produces defensible citations that would hold up in a submission review. End-to-end automation: From firmware upload to FDA-ready dossier in ~3 minutes. This genuinely solves a 6-week manual process. Credible medical device expertise: The system understands IEC 62304 safety classes, IEC 62443 zone models, and FDA premarket requirements, not generic security advice. What we learned Multi-agent systems need real tools: LLMs are excellent at reasoning over structured data, poor at generating it from scratch. The best agent architectures combine classical tools with AI interpretation. RAG quality depends on document preparation: Regulatory summaries with clear section structure and metadata outperformed raw PDF ingestion. Bedrock Knowledge Bases are underrated: S3-backed RAG with zero ops overhead is ideal for early-stage products. Medical device cybersecurity is massively underserved: Every manufacturer we have spoken to about this problem immediately wants it. The market need is real. What's next for MedDevice CyberGuard Open-source the core: Publish the agent orchestration and medical device Semgrep rules so small manufacturers can self-assess CI/CD integration: Run assessments automatically on every firmware commit Hospital procurement integration: Enable hospitals to request CyberGuard dossiers as part of vendor due diligence Expand protocol support: Beyond current IoT protocols to cover CoAP, BLE, Zigbee, and cellular for broader connected device coverage Continuous monitoring: Webhook-triggered re-assessment and drift detection as device software evolves post-market <div