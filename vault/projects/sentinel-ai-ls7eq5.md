---
slug: "sentinel-ai-ls7eq5"
url: "https://devpost.com/software/sentinel-ai-ls7eq5"
title: "Sentinel.ai"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 543
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Sentinel.ai

> Always Watching

[Devpost](https://devpost.com/software/sentinel-ai-ls7eq5) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[developer_tools]] [[health_clinical]] [[labor_employment]]
**user** [[researcher]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** api, atlas, cloud, cloudinary, compute, dlib, elevenlabs, embeddings), face-recognition, fastapi, gemini, gemma, git, github

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sentinel.ai

## Body

successful classification with 90%+ confidence! training our custom res_net model (83% accuracy for notable events)! training image (finding a snack thief!) Inspiration Security cameras generate 24/7 footage, but in practice humans review only a tiny fraction of it. We wanted Sentinel.ai to act like an AI security analyst: detect notable moments in near real time, explain what happened in 1 concise alert, and produce a verifiable event trail instead of storing hours of video nobody watches. What it does Sentinel.ai monitors live camera streams and flags important activity. In our deployed run, it watched 2 active streams simultaneously and produced structured events with timestamps, confidence, media URLs, and on-chain transaction references. It detects people/objects, runs an event-notability gate, identifies known faces, generates a natural-language summary, and logs event metadata. The result is a real-time alert pipeline that turns raw frames into understandable, searchable, and auditable events. How we built it We built a FastAPI backend deployed on Vultr (4 vCPU / 16 GB RAM), with a stream manager ingesting camera feeds and buffering context frames (up to 60 seconds). The event cascade uses: YOLOv8n (downloaded model size ~6.2 MB) for person/object detection ResNet-18 for notable-event gating Face embeddings for identity matching Gemma 4 for reasoning ElevenLabs for narration Cloudinary for media storage MongoDB for event persistence Solana devnet transaction hashes for tamper-evident provenance Frontend clients subscribe via WebSockets for live updates. Challenges we ran into The biggest challenge was balancing model quality with hackathon time constraints. Our first broad-label pass used 8,068 labeled frames and landed around 53.19% best validation accuracy, which was too noisy. We pivoted to a incident-specific dataset and hand-labeled 19 unique event intervals; that improved best validation accuracy to 83.10% after a 20-epoch run. We also hit deployment friction around Python/toolchain compatibility and Solana devnet rate limits (429 / 403 responses), so we added fallback behavior and resilient startup paths. Accomplishments that we're proud of We shipped a full end-to-end, multi-service AI system under hackathon constraints, in only 36 hours!: Live streams resumed automatically at startup (2 streams active in production run) Event pipeline writes to MongoDB and returns queryable history (/events?limit=5) Cloudinary frame uploads succeeded with public URLs Solana logging produced real transaction signatures Custom ResNet model training and deployment worked end-to-end (ml/models/sentinel_resnet18.pt) We also designed the pipeline so each stage can fail gracefully without taking down the entire system. What we learned We learned that architecture wins: a cascade (detect -> gate -> reason) is more practical than forcing one giant model to do everything. Data quality mattered more than model depth: moving from weak auto-labeling to focused labels raised validation performance from ~0.53 to ~0.83. We also learned to design reliability first: async boundaries, service fallbacks, and explicit interfaces let us keep the system live even when one API degraded. What's next for Sentinel.ai Next steps: Improve identity accuracy with stronger vector-search matching Upgrade from deprecated google.generativeai to the newer Gemini SDK Add threshold calibration per camera (confidence tuning by context) Improve operator UX (triage controls, confidence sliders, false-positive feedback) Harden production with worker queues, retry policies, and monitoring dashboards Target outcome: support more cameras per instance, lower false positives, and produce richer alerts (image + summary + narration + proof) with the same pipeline <div