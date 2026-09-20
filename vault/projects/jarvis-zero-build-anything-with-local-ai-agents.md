---
slug: "jarvis-zero-build-anything-with-local-ai-agents"
url: "https://devpost.com/software/jarvis-zero-build-anything-with-local-ai-agents"
title: "MeDo Mental Health Agent: Emotionally Intelligent AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 240
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/legal_professional"
  - "user/social_worker"
  - "substrate/geospatial"
---

# MeDo Mental Health Agent: Emotionally Intelligent AI

> Because everyone deserves a listener who never sleeps, never judges, and always knows when to call for help.

[Devpost](https://devpost.com/software/jarvis-zero-build-anything-with-local-ai-agents) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[health_clinical]] [[mental_health]]
**user** [[legal_professional]] [[social_worker]]
**substrate** [[geospatial]]

**stack** ai-agents, asyncio, crisis-detection, fastapi, mental-health, natural-language-processing, pydantic, python

## How they structured the write-up

- the problem
- our solution
- clinical alignment
- privacy by design

## Body

The Problem Mental health care has a supply-demand crisis. Over 970 million people live with a mental health disorder globally, yet the median treatment gap reaches 70% in low-income countries. In the US, the average wait time to see a psychiatrist is 25 days. Our Solution MeDo Mental Health Agent is a conversational AI companion built on three coordinated agents: an empathy layer, a therapeutic response engine, and a crisis detection module. Core Features Conversational Mental Health Assistant ( POST /chat ) The empathy_agent analyzes messages for tone and distress signals. The therapeutic_response_agent selects the appropriate clinical technique: Grounding exercises for acute distress Psychoeducation for users seeking to understand symptoms Reflective listening for processing complex emotions Mood Tracker ( POST /mood-tracker ) The mood_insight_agent processes mood scores, emotion tags, sleep hours, and activity against evidence-based intervention logic. Crisis Support ( POST /crisis-support ) The crisis_assessment_agent scans messages for high-risk language. Based on severity: High: immediate crisis line routing Medium: warm handoff with counselor resource Low: supportive presence with continued conversation Technical Stack Backend : FastAPI + Python asyncio Validation : Pydantic v2 Concurrency : asyncio.gather() for parallel agent execution LLM Backend : Modular — OpenAI, Anthropic, or local models via Ollama Safe Messaging : Hardcoded guardrails independent of LLM output Clinical Alignment Grounded in CBT, DBT-informed grounding, Motivational Interviewing, and Exercise Psychiatry. Privacy by Design No persistent storage, ephemeral session IDs, no PII required, offline-capable with local LLM support. <div