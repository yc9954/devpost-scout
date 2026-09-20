---
slug: "autoir-agentic-incident-response-on-tidb-aws"
url: "https://devpost.com/software/autoir-agentic-incident-response-on-tidb-aws"
title: "AutoIR: Agentic Incident Response on TiDB + AWS"
hackathon: "TiDB AgentX Hackathon 2025"
organization: "TiDB"
winner: true
words: 481
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# AutoIR: Agentic Incident Response on TiDB + AWS

> AutoIR turns noisy AWS logs into actionable incidents using TiDB vector search and an agentic LLM. Ingest, embed, detect spikes, and route alerts—serverless, fast, safe.

[Devpost](https://devpost.com/software/autoir-agentic-incident-response-on-tidb-aws) · hackathon [[TiDB AgentX Hackathon 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]] [[housing_homeless]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, cli, kimi-k2, llm, node.js, sagemaker, tidb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for autoir

## Body

Architectural Diagram Automated Reports GIF AutoIR Fargate TUI LLM Chat TUI AutoIR — Agentic Incident Response on TiDB + AWS Inspiration Operations teams drown in noisy logs, brittle regular-expression alerts, and dashboards that miss context. We wanted a single command-line tool and backend that ingests logs, embeds them, searches semantically, and produces an explainable incident report instead of just flagging a metric spike. TiDB’s VECTOR(384) support plus serverless embeddings on AWS made this practical for a build that still feels production-ready. What it does Turns raw CloudWatch logs into incidents. Ingest → embed (384-dimensional vectors) → semantic search → tool-assisted analysis → incident summary. Agentic triage. An LLM orchestrator calls safe tools ( tidb_query , analysis ) to gather evidence, compute ratios, and draft a concise write-up. Fast, cost-aware, explainable. TiDB handles both vector search and SQL; SageMaker Serverless hosts BAAI/bge-small-en-v1.5 . Optional SNS routes alerts to humans. Typical performance: 50–400 ms per embedding, under 100 ms vector search, end-to-end semantic query under 2 s on a warm path. How we built it Data plane Ingestion: ECS Fargate task tails CloudWatch Logs and batches lines. Embeddings: SageMaker Serverless feature-extraction endpoint (HF DLC, BGE-small). Storage and retrieval: TiDB Serverless with VECTOR(384) and vec_cosine_distance . Reasoning plane Agent orchestrator: Node.js (TypeScript, oclif) tool-calling loop. Safety rails: tidb_query is SELECT-only with enforced LIMIT ; analysis is a pure expression evaluator. Command-line usage autoir logs tail --embed to ingest and embed autoir logs query --query "timeout contacting DB" for semantic search autoir daemon --alerts-enabled to run the loop and optionally page via SNS Challenges we ran into Cold starts and batching: Tuning batch size to keep latency low without driving up cost. Vector-aware schema design: Letting TiDB handle approximate-nearest-neighbor-style search and relational filters without complex queries. Safe tool calling: Allowing exploration without writes or runaway scans. Incident deduplication: Designing a stable dedupe_key across near-duplicate spikes. Accomplishments that we're proud of Vector-native log analytics inside a standard SQL database—no extra vector service. Explainable incident reports with evidence (sample IDs, time windows, counts) and confidence. Serverless components end to end: TiDB Serverless, SageMaker Serverless, optional SNS. Operational guardrails: SELECT-only SQL, automatic LIMIT , constrained analysis tool. What we learned TiDB’s vector column plus SQL joins is a strong foundation for context-first incident response. Small, fast embeddings (BGE-small) are often sufficient for triage when paired with targeted filtering. Guardrails reduce speculative investigations: limiting tool I/O and shaping prompts matters. Streaming partial responses to the terminal makes the system feel responsive even when upstreams add latency. What’s next for AutoIR Multi-tenant controls and RBAC: scoped DSNs, per-team log groups, API tokens. Richer tools: latency SLO calculators, automatic baselines, cost anomaly detection. Playbooks: map incident types to templated, one-click runbooks. More sources: Kinesis, S3 access logs, VPC Flow Logs, Kubernetes events. Lightweight web console: incidents, evidence, and replay. Benchmarking: evaluation suite for precision and recall on public log corpora. <div