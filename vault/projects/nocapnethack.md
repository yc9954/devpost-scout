---
slug: "nocapnethack"
url: "https://devpost.com/software/nocapnethack"
title: "YeetThePacket"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 632
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# YeetThePacket

> From packets to plain‑English, actionable security narratives.

[Devpost](https://devpost.com/software/nocapnethack) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[labor_employment]] [[supply_logistics]] [[transportation]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** bash, cohere, docker, fastapi, python, streamlit, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for yeetthepacket

## Body

YeetThePacket Homepage Processing Queue Statistics Scan Results Information on Network Activity Event Details Overview Event Details Narrative Event Details Evidence Event Details Metadata Event Details Json Scan History Upload PCAP Files Information on Uploaded File Processing the Uploaded Packet File Uploading Data in Chunks Uncompressing and Ingestion using Tshark Ingesting and Detecting Events Generating Narratives For All The Detections Inspiration We’ve watched analysts spend hours sifting through packet captures, then struggle to communicate findings to non-technical stakeholders. We wanted to bridge that gap: turn raw network traffic into clear, defensible stories that responders and decision-makers can act on. Using the MACCDC 2012 dataset as a proving ground, we set out to show that AI can explain incidents without guesswork. What it does Detects events like port scans, brute-force attempts, beaconing/C2, suspicious connections, and data exfiltration from PCAPs. Generates evidence‑backed narratives with a one‑line summary, technical analysis, executive summary, severity, MITRE ATT&CK mapping, remediation steps, and a confidence score. Provides an interactive UI: timeline exploration, filters, search, and a network graph of host relationships. Exports incident reports (PDF) for briefings and documentation. How we built it Ingestion and ETL: tshark/pyshark to extract flows and features from PCAPs; pandas for normalization. Detection: lightweight heuristic rules (e.g., high unique destination ports, periodic beacons, failed-auth bursts). AI narratives: a pluggable LLM client (Cohere, Gemini, OpenAI) with evidence‑grounded prompts and structured outputs. Backend: FastAPI for upload, processing, and narrative endpoints; background tasks for longer jobs. Frontend: Streamlit for rapid iteration with timeline, detail panes, and graph visualizations. Packaging: Docker and docker‑compose for one‑command setup; JSONL storage (optional SQLite planned) for portability. Challenges we ran into Grounding LLM outputs to evidence to avoid overclaims. Keeping performance reasonable on larger PCAPs (batching/streaming). Consolidating noisy signals into coherent incidents with sensible severity. Maintaining UI responsiveness with thousands of flows and events. Handling provider rate limits, timeouts, and behavioral differences across LLMs. What we learned Evidence‑first prompts dramatically improve reliability and clarity. Simple, transparent detection rules are highly effective for a first pass. Clean UX (timelines and summaries) makes complex investigations approachable. Strong schemas for events and narratives unlock reporting and search features. Investing early in containerization and scripts pays off during demos. Accomplishments that we're proud of End‑to‑end pipeline from PCAP ingestion to evidence‑backed AI narratives, running reliably on real data (MACCDC 2012). Multi‑provider LLM integration (Cohere, Gemini, OpenAI) with a structured, grounded prompt design to minimize overclaims. Interactive UI with a timeline, filters, search, detailed event views, and a network graph for host relationships. Exportable PDF incident reports that combine executive summaries with technical evidence and remediation steps. One‑command Docker deployment and documented FastAPI endpoints with live docs, enabling quick setup and demos. Heuristic detection for port scans, brute force, beaconing/C2, suspicious connections, and data exfiltration. Background processing and streaming/batching patterns that keep the UI responsive on larger PCAPs. Clean event and narrative schemas (JSONL) that make reporting, search, and downstream integrations straightforward. A complete demo script and smoke tests to validate the flow and reduce demo risk. What we learned Evidence‑first prompts and structured outputs dramatically improve reliability and trust in AI narratives. Transparent heuristic rules are highly effective for a first‑pass detection layer and easy to reason about. Strong schemas are leverage: once the data model is right, features like reporting and search come naturally. Performance tuning (batching, streaming, and incremental processing) matters as PCAP size grows. UX clarity—timelines, severity, and concise summaries—makes complex investigations accessible to all stakeholders. What's next for YeetThePacket Real‑time analysis: streaming ingestion, incremental detection, and live narrative updates. Data layer: PostgreSQL/SQLite for indexing, queries, caching, and long‑term storage. Scalability: Redis task queues, horizontal workers, and Kubernetes deployment manifests. Detection depth: DNS tunneling, DGA, TLS fingerprinting/JA3, lateral movement, and exfil heuristics by protocol. ML‑assisted anomaly detection to complement heuristics with explainable features. <div