---
slug: "gallop"
url: "https://devpost.com/software/gallop"
title: "Gallop"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 719
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/sensor_telemetry"
---

# Gallop

> Stop breaches in real-time. Gallop is a multi-agent, AI-native cybersecurity control platform that detects intrusion activity and converts security signals into immediate defensive actions.

[Devpost](https://devpost.com/software/gallop) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[security_privacy]]
  <sub>weak: health_clinical</sub>
**user** [[researcher]]
**substrate** [[sensor_telemetry]]

**stack** codex, ebpf, elastic, elasticcloud, elasticsearch, framer, jina, lucide, next-themes, next.js, openai, radix, react, recharts

## How they structured the write-up

- inspiration
- solution
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- looking forward

## Body

Gallop Agent Management Gallop Detection Log Gallop Security Overview Gallop Installation Gallop Triage with Jina Inspiration In today’s world of big data, where it becomes increasingly difficult to distinguish between pertinent and irrelevant information, identifying meaningful threats under time-pressure is essential. Many current cybersecurity operations are hindered by tedious manual investigation, fragmented tool usage, and delayed bureaucratic remediation—all of which result in attacker advantages as they seek to exploit the gap between detection and action. Signal overload, where analysts must interpret large volumes of telemetry and alerts under severe time constraints, is one of the most significant burdens for modern security operations. Solution Gallop is a real-time cybersecurity control platform that autonomously converts security signals into immediate defensive actions. By galloping through security data, our tool detects intrusion activity through continuous system telemetry monitoring. Once detected, an appropriate response is quickly deployed as determined by the autonomous multi-agent architecture. Gallop seeks to limit the detection-to-action gap and contain threats in real time. Instead of relying solely on manual investigation workflows, the AI-powered platform builds contextual understanding from live telemetry and validates threats through Elasticsearch-driven signal correlation. Finally, it executes containment and remediation actions in real time. Using Elasticsearch's advanced vector search capabilities with Jina models via Elastic Inference Service (EIS), Gallop utilizes context retrieval through a multi-agent architecture, managed by an orchestrator agent triggered by Elasticsearch workflows. This event-driven workflow automation makes autonomous, human-free decisions. Essentially, Elastic provides the necessary retrieval and sensing system, and Gallop provides the reflexes and operational control plane, compressing detection-to-action cycles from human to operational timescales. Gallop’s specialty and central thesis lie in its continuous decision-making and response optimization, which result in latency compression and system stabilization. Rather than rigid, predefined rules, Gallop’s multi-agent model uses contextual reasoning to autonomously decide on and execute security protocol. How We Built It We dove deep into new tools and programs this weekend. We primarily utilized Elastic’s many services, including Elasticsearch running on Elastic Cloud as our telemetry aggregation and reasoning function. Jina models were used for embeddings generation and vector similarity, in order to better classify events to match with pre-defined threat categories. Using Elastic’s Agent Builder and Workflow functions, we deployed a multi-agent architecture with event-triggering loops. The individual agents running on Gallop-defended machines are powered by the OpenAI API, and the orchestrator is built with Elastic AI Agent Builder, which oversees event-driven workflows and response actions. Data collection is done using an eBPF-based framework, inspired by the execsnoop.bt tool that comes with BPFTrace. We utilized this technology because it allowed us real-time access to what is actually being executed on a computer, allowing us to have significantly more visibility into security-relevant data. To test the efficacy of our project, we also created a simulated intrusion platform to test how quickly Gallop could detect and mitigate exploits. Challenges We Ran Into This was our first time using the Elastic product suite, so familiarizing ourselves with the ecosystem took a significant portion of our attention and time. A primary difficulty in this project was creating the multi-agent infrastructure. Given the fact that many observed behaviors were non-deterministic, ensuring the accuracy of the agents’ autonomous decision-making proved rather difficult during initial tests. Erroneous false positives and false negatives presented themselves during early tests; a significant number of tests and iterations were required to ameliorate these issues and yield far more accurate decision-making results. Accomplishments We're Proud Of Utilized Elasticsearch for telemetry ingestion and low-latency querying. Integrated Jina models for data analysis. Used Elastic Agent Builder to design an autonomous multi-agent architecture Made a dashboard for system visibility What We Learned On the technical front, we gained experience with Elastic’s low-latency querying abilities, vector search, and workflow and agent interactions. This project taught us how embeddings and reranking models can turn massive datasets into a manageable decision-making context. Navigating Elastic API demonstrated the tool’s full abilities and versatility for wide-ranging objectives. We also gained great insight into creating a clean, user-friendly UI whilst integrating real-time updating backend capabilities. Looking Forward We are excited to see Gallop’s future potential. With additional time and resources, we envision creating a more robust framework for Gallop’s risk-awareness and decision-making abilities. These additions would enable Gallop to act with precision and stability across wide-ranging industries—bringing security to our modern and fast-changing world. <div