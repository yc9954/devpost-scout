---
slug: "taskwise-beydzx"
url: "https://devpost.com/software/taskwise-beydzx"
title: "Prismly"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 413
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Prismly

> See your projects in full spectrum)))

[Devpost](https://devpost.com/software/taskwise-beydzx) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[labor_employment]]
**user** [[developer]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: code_repository</sub>

**stack** python, qdrant, rag, react, spacy

## How they structured the write-up

- inspiration
- what it does
- how we built it?
- challenges we ran into
- accomplishments
- what we learned?
- what's next?

## Body

Project Assignment dashboard personalized calender github repository creation Inspiration Project management is broken. Teams spend 40% of their time firefighting problems they never saw coming. We watched brilliant engineers miss critical deadlines not from lack of effort, but from lack of foresight. Traditional tools show what already happened. Prismly predicts what will happen. Every intelligent feature in "Taskwise" runs on Prismly. This is the story of the AI backbone that transformed project management from reactive to predictive. What It Does Prismly is AI that thinks ahead. Speak your project vision, and our Gemini-powered system instantly generates professional specifications with tasks, dependencies, and realistic timelines. Semantic skill matching assigns work to the right person based on actual capabilities, not org charts. Every task auto-syncs across Google Calendar, Trello, GitHub, and Meet. Most importantly, predictive risk analysis warns you 72 hours before deadlines become impossible. While competitors manage tasks, Prismly illuminates risk before it destroys your timeline. How We Built It? Four Gemini pillars power intelligent execution: Text Generation creates detailed project breakdowns from casual input Embeddings enable semantic skill matching via vector similarity (0.75 threshold, 91% accuracy) Analysis evaluates team capacity, task complexity, and dependency chains Narrative Intelligence translates metrics into plain-language recommendations executives actually act on FastAPI handles async requests. MongoDB stores canonical state. Qdrant performs vector search. Redis caches responses and brokers Celery workers for background AI operations. Event sourcing with transaction IDs prevents infinite loops across platform integrations. Challenges We Ran Into Prompt engineering required 47 iterations to achieve consistent structured output. Embedding threshold calibration needed systematic testing across 200 ground-truth assignments. Balancing Gemini's analytical depth with real-time performance demanded three-tier caching strategy. Cross-platform synchronization risked infinite loops until we implemented event sourcing architecture. Accomplishments 47 actionable tasks in 8 seconds. 91% skill-matching accuracy. Prevented $120K in missed deadlines during beta. 99.7% uptime. Sub-second response times for 95% of operations while maintaining full AI depth. What We Learned? Embeddings unlock semantic magic that keyword matching cannot achieve. Narrative AI drives 6x more executive action than dashboards. Prompt engineering is system architecture. Caching multiplies performance. Users want augmentation, not automation. What's Next? Multimodal expansion extracts tasks from meeting recordings and whiteboard photos. Autonomous agents will update tasks and resolve blockers independently. Cross-project learning will benchmark against thousands of anonymized projects and recommend proven patterns. Prismly doesn't just manage projects. It sees through them. Built with: Gemini 3, FastAPI, MongoDB, Qdrant, Redis, Celery, React, TypeScript, Google Workspace APIs, GitHub API, Trello API <div