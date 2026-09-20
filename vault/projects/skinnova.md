---
slug: "skinnova"
url: "https://devpost.com/software/skinnova"
title: "Skinnova"
hackathon: "AI Partner Catalyst: Accelerate Innovation"
organization: "Google"
winner: true
words: 938
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Skinnova

> Skinnova - Personalized skincare with operational AI trust and reliability.

[Devpost](https://devpost.com/software/skinnova) · hackathon [[AI Partner Catalyst- Accelerate Innovation]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]] [[legal_professional]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** certbot, datadog, docker, docker-compose, fastapi, github, github-workflow, google-bigquery, google-cloud, google-dataflow, husky, nginx, python, react

## How they structured the write-up

- inspiration
- what we built
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for skinnova

## Body

Skinnova Inspiration Skinnova was inspired by a critical but underexplored problem in AI observability: people increasingly rely on AI for domain-specific advice , yet most LLM monitoring systems fail to answer the question that matters most in production: If a hallucination occurs, how many users does it actually affect, and who are they? While building AI-driven experiences, we realized that traditional LLM observability treats hallucinations as a binary correctness issue , often evaluating every prompt uniformly. This approach is expensive, noisy, and misses the bigger picture. This insight led us to design Skinnova not just as an AI skincare assistant, but as a production-grade system where AI reliability, risk, and impact are fully observable — a pattern applicable to any high-stakes AI product. What We Built Skinnova is an AI-powered skincare assistant built on top of a novel LLM observability layer focused on two core innovations: selective hallucination evaluation and hallucination blast radius measurement . The assistant: Provides personalized skincare routines Explains ingredients and formulations Answers skin concern–specific questions Tailors responses using user attributes such as age, skin type, and skin concern These user attributes serve a dual purpose — personalizing responses and powering a persona-aware observability system that tracks how hallucinations propagate across different user cohorts. How We Built It System Architecture Google Cloud Used for LLM inference and backend infrastructure to ensure scalability and reliability, metric emission through Dataflow and BigQuery. Python + FastAPI Handles request orchestration, persona enrichment, and metric emission. React + Vite Facilitates the seamless user interface. Datadog Used as the central observability platform for metrics, dashboards, alerts, and runbooks. Selective Hallucination Evaluation Instead of evaluating hallucinations for every prompt, Skinnova introduces a risk-based prefilter that assigns a risk score to each prompt. Only prompts with a risk score above 0.25 are evaluated for hallucination. Importantly, the decision to evaluate is itself observable — a first-class signal in the system. This allows us to track: How often evaluation is triggered Why it was triggered Affected users along with prefilter accuracy Hallucination Blast Radius Detecting a hallucination alone is not enough. We wanted to understand real-world impact . We introduced the Hallucination Blast Radius Index (HBRS) , derived inside Datadog using observable signals: HBRS = HallucinationScore × ChatVolume × UserPersonaRiskWeight Where: Hallucination Score measures semantic deviation [Score: 0–1] Chat Volume represents real user exposure Persona Risk Weight reflects sensitivity based on age group and skin concern [Score: 1–2] By emitting atomic metrics and deriving impact dynamically, we keep the system transparent, tunable, and production-realistic. Persona-Aware Impact Visualization User attributes such as: user.age_bucket user.skin_type user.skin_concern are emitted as low-cardinality Datadog tags . This enables heatmaps and breakdowns that show: Which user personas are affected How hallucinations propagate across cohorts Why the same hallucination can be low-risk or high-risk depending on audience Challenges We Ran Into 1. Avoiding Metric Noise Evaluating hallucinations everywhere creates alert fatigue. Designing a selective pipeline required careful prefiltering without missing critical cases. 2. Balancing Simplicity and Novelty We had to ensure the system was explainable while still demonstrating deep AI observability and reliability thinking. 3. Designing Auditable Observability We avoided black-box scores by emitting only atomic, auditable metrics and deriving insights transparently in Datadog. 4. Mapping AI Reliability to Business Impact Translating hallucination scores into something operationally meaningful required rethinking traditional LLM monitoring approaches entirely. 5. GCP Hallucination Compatibility Since Datadog doesn't have native integration with GCP LLMs such as Vertex AI for hallucination evaluation, we built a dedicated LLM judge to fill that gap. Accomplishments We're Proud Of 1. Designed selective hallucination evaluation Instead of evaluating every LLM response, we built a risk-based prefilter that decides when and why hallucination evaluation happens — and made that decision itself observable. 2. Turned hallucinations into measurable impact We moved beyond raw hallucination scores by computing a hallucination blast radius, correlating severity with real traffic and user personas to understand who was affected and how far issues spread. 3. Built end-to-end AI observability with Datadog We integrated Datadog across APM, infrastructure, AI observability, and custom hallucination metrics to create a single, coherent operational view of the system. 4. Defined SLOs for AI behavior, not just uptime We established SLOs around hallucination impact, allowing AI reliability to be measured and enforced like any other production service. 5. Implemented actionable detection, alerts, and runbooks Detection rules trigger Slack alerts when blast radius thresholds are breached, each linked to a runbook that guides engineers through assessment and mitigation steps. 6. Delivered a production-grade AI reliability pattern Skinnova demonstrates a reusable approach for operating LLMs safely at scale — where hallucinations are managed as incidents with clear signals, thresholds, and response workflows. What We Learned Not all hallucinations matter equally — exposure and user context define risk Observability should measure impact , not just model behavior Making evaluation decisions observable is as important as evaluating outcomes Domain-aware personas dramatically improve interpretability of AI incidents Separating raw signals from derived metrics increases flexibility and trust What's Next for Skinnova Adaptive risk-aware evaluation Evolve selective hallucination evaluation by dynamically adjusting prefilter thresholds based on live SLO health, traffic patterns, and incident history. Feedback-driven reliability loops Use post-incident data and runbook outcomes to continuously refine detection rules, persona risk weights, and evaluation strategies. Deeper integration with Datadog AI features Expand use of Datadog's AI Observability to track prompt patterns, response drift, and long-term hallucination trends across model versions. Proactive user impact prevention Introduce automated mitigation actions, such as safe-response fallbacks or response throttling, before blast radius thresholds are breached. Model and prompt version observability Compare hallucination behavior across model and prompt versions to support safer rollouts and controlled experimentation. <div