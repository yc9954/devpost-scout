---
slug: "evident-ai"
url: "https://devpost.com/software/evident-ai"
title: "Evident AI"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 466
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "domain/transportation"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Evident AI

> Automatically transforms bodycam footage into professional evidence reports using AI.

[Devpost](https://devpost.com/software/evident-ai) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[human_in_the_loop]] [[provenance_signing]] [[voice_speech]]
**domain** [[developer_tools]] [[legal_justice]] [[transportation]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** css, django, javascript, openai, openai-agents-sdk, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments
- what we learned
- what’s next

## Body

Inspiration Evidence processing is the bottleneck. Officers spend hours transcribing body-cam footage and writing reports, which is time not spent serving the community. Vendors charge thousands and take days for basic transcripts. I realized there’s a better way: automate the grind while preserving legal standards. Evident AI was born, an AI evidence-processing copilot that turns body-cam video into a professional, review-ready report in minutes, anchored with blockchain proofs. What it does Evident AI orchestrates specialized AI agents across the full evidence lifecycle: Full-stack analysis: Extracts audio and transcribes speech with Whisper + error correction and speaker tagging. Visual intelligence: Key-frame analysis (GPT-4V) to surface people, vehicles, objects, and salient actions. Professional reporting: Generates a structured draft with a timeline, entities, action summaries, and narrative* with citations and confidence scores * for quick human review (no legal determinations made by AI). Blockchain integrity: XRPL anchoring + XLS-70 credentials for officer identity, producing cryptographic attestations and a tamper-evident chain of custody. Court-ready output: One-click PDF/Docx with officer checklist, digital signatures, and an audit log (hashes, model versions, timestamps). TL;DR: Body-cam in → transcript + key frames → cited, structured report → signed & anchored. Minutes, not days. How we built it Backend: Django 5.2.6 (REST) behind Gunicorn + Nginx AI Agents: OpenAI Agents SDK coordinating transcription, vision, and report-writer roles with structured JSON I/O Video: OpenCV + MoviePy for frame sampling and audio separation Blockchain: XRPL integration; officer XLS-70 creds; memo-based anchors with SHA-256 hashes per stage Database: PostgreSQL (prod), SQLite (dev) Deployment: Dockerized; runs on Heroku/Railway/Vercel Security: Fernet encryption for secrets; audit trails with immutable source hashes Challenges Agent orchestration: Retries, schema validation, and timeouts across multiple models/services Large files: GB-scale videos; streamed processing and memory-safe chunking Evolving standards: XLS-70 is emerging: DevNet only with limited use case examples Security & compliance: Encryption at rest/in transit, RBAC, and explicit human-in-the-loop review Production hardening: Containerization, DB tuning, back-pressure and job queues Accomplishments End-to-end demo: Upload → transcript + key frames → cited report → signed PDF with XRPL anchor Human-in-the-loop UX: Confidence chips and inline citations (hover to see the exact timestamp/frame) Integrity by design: Original media hash preserved; every export logs model versions and anchors What we learned Practical agent hand-offs with the OpenAI Agents SDK (tools, structured outputs, recovery paths) XRPL anchoring patterns and XLS-70 credential flows for attestations Real-world video optimization and keeping AI pipelines responsive Building for policing means: assist, cite, and log What’s next Pilot with agencies: Run side-by-side with existing RMS workflows to measure minutes saved per report and edit-accept rates Model upgrades: Domain-tuned entity recognizers and policy-aware templates (traffic stop, use-of-force, etc.) Mobile ingest: Secure field upload from camera to case Analytics: Case stats, throughput, and time-savings dashboards RMS adapters: Push approved drafts into Axon/Mark43/Tyler/Niche via export & API connectors <div