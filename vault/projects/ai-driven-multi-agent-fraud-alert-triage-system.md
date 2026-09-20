---
slug: "ai-driven-multi-agent-fraud-alert-triage-system"
url: "https://devpost.com/software/ai-driven-multi-agent-fraud-alert-triage-system"
title: "AI-driven, multi-agent fraud alert triage system"
hackathon: "AWS AI Agent Global Hackathon"
organization: "AWS"
winner: true
words: 569
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/researcher"
  - "substrate/financial_record"
---

# AI-driven, multi-agent fraud alert triage system

> AI-driven, multi-agent fraud alert triage system using AWS AgentCore and Bedrock that automates alert evaluation, reduces false positives, and improves investigation efficiency.

[Devpost](https://devpost.com/software/ai-driven-multi-agent-fraud-alert-triage-system) · hackathon [[AWS AI Agent Global Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
  <sub>weak: deterministic_policy</sub>
**domain** [[finance_payments]] [[health_clinical]]
  <sub>weak: developer_tools</sub>
**user** [[researcher]]
**substrate** [[financial_record]]

**stack** apigateway, athena, bedrock, bedrock-agentcore, lambda, langgraph, python, s3

## Body

Inspiration Traditional fraud monitoring systems produce thousands of alerts every day - yet over 90% turn out to be false positives. This overwhelms compliance teams, delays genuine investigations, and drives up operational costs. We set out to build an intelligent, explainable, and self-learning system that reduces analyst fatigue and enhances risk detection accuracy - starting not from raw transactions, but from the alerts themselves that demand smarter triage. What it does Our solution is a multi-agent AI system that automates end-to-end alert handling using AWS AgentCore and Amazon Bedrock. It begins by retrieving alerts stored in Amazon Athena, enriching each alert with customer, account, and transaction data from Athena. The Alert-Triage Agent applies a multi-layered evaluation process — checking allowlist and historical alert outcomes, calculating a composite risk score by combining rule-based and LLM-generated assessments, and producing an explainable decision on whether to auto-dismiss, queue for analyst review, or escalate for deeper investigation. Escalated alerts are routed to the Investigation Agent, which performs entity-level analytics, identifying cross-account linkages, transactional velocity patterns, and fund-flow relationships to determine the potential fraud typology. It leverages Bedrock reasoning to summarize suspicious behaviors, classify risk categories, and recommend SAR escalation when warranted. Confirmed suspicious cases are then passed to the Report Agent, which automatically compiles structured Suspicious Activity Report (SAR) summaries — including facts, rationale, entities involved, and confidence scores — and stores them securely in Amazon S3 for compliance review. How we built it We designed a three-agent architecture - Triage, Investigation, and Report - using AWS AgentCore Runtime. Integrated Claude 3.5 Sonnet on Amazon Bedrock for reasoning, decision-making, and report generation. Connected with Amazon Athena for real-time access to alerts, transactions, and customer data. Used S3 and Athena for data storage and retrieval of generated SARs. Deployed each agent as a containerized microservice using the AgentCore SDK and Amazon ECR. Built a React-based analyst UI to review alerts and provide feedback, which automatically refines allowlists and improves accuracy. Built the REST APIS in AWS API gateway and integrated with the AI. Challenges we faced Balancing LLM reasoning with deterministic rule-based logic to ensure reliability. Designing prompt templates that consistently return structured JSON for automation. Handling inter-agent communication. Accomplishments we’re proud of Implemented a fully autonomous triage workflow that reduced false positives by up to 60% in pilot testing. Built an explainable decision pipeline, where every AI-driven action is supported by contextual evidence and narrative reasoning. Seamlessly integrated AWS Bedrock LLMs with Athena and S3 in a modular, production-ready architecture. Delivered a working end-to-end system in in a short span, demonstrating measurable business impact. What we learned Hybrid AI systems - combining LLMs with rule-based frameworks - deliver the best results in enterprise use cases. Prompt clarity and schema enforcement are key to reliable automation. Multi-agent architectures enhance modularity, scalability, and explainability. AWS AgentCore greatly simplifies orchestrating and scaling intelligent agent systems. What’s next Analyst feedback on outcomes feeds back into the system, can continuously refining allowlist patterns, risk calibration, and decision thresholds to further reduce false positives over time. Introduce a real-time streaming interface using Amazon Kinesis for continuous alert ingestion. Apply graph analytics to reveal hidden entity relationships and complex fraud networks. Add multi-language report generation to support global compliance teams. Package the system as a reusable AWS Solution Accelerator for rapid adoption by financial institutions. Keep upgrading the agent capability by additional analysis and fed it to the LLM <div