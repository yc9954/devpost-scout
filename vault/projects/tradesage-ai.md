---
slug: "tradesage-ai"
url: "https://devpost.com/software/tradesage-ai"
title: "TradeSage AI"
hackathon: "Agent Development Kit Hackathon with Google Cloud"
organization: "Google"
winner: true
words: 435
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# TradeSage AI

> TradeSage AI is an intelligent multi-agent financial analysis platform built using ADK, Agent Engine, Cloud Run and Vertex AI, that revolutionizes trading hypothesis evaluation.

[Devpost](https://devpost.com/software/tradesage-ai) · hackathon [[Agent Development Kit Hackathon with Google Cloud]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** adk, cloudrun, cloudsql, fastapi, gcp, gemini, python, react, uvicorn, vertex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tradesage ai

## Body

TradeSage AI Architecture Inspiration We were inspired by the recent advances in AI agents and the realization that different aspects of investment analysis - hypothesis formation, risk assessment, market research, and alert generation - could be handled by specialized AI agents working in concert. What it does TradeSage AI is a sophisticated multi-agent system that transforms raw trading ideas into comprehensive investment analyses. Users input a trading hypothesis, and the system orchestrates six specialized AI agents to: Hypothesis Agent: Structures and refines the trading idea into a clear, measurable hypothesis Context Agent: Extracts key information about the asset, including sector, competitors, and business model Research Agent: Gathers real-time market data, news, and financial metrics using integrated APIs Contradiction Agent: Identifies risks, challenges, and factors that could invalidate the hypothesis Synthesis Agent: Balances contradictions against confirmations to generate a confidence score and comprehensive analysis Alert Agent: Creates actionable alerts with specific entry points, risk management levels, and monitoring triggers The system provides a beautiful dashboard showing all active hypotheses with their confidence scores, supporting/opposing factors, and real-time price tracking. How we built it We used: Google's Agent Development Kit (ADK) for orchestrating AI agents Vertex AI/Gemini models for powering each specialized agent FastAPI for the REST API layer Cloud SQL PostgreSQL with pgvector for storing analyses and enabling RAG capabilities Real-time market data integration via Alpha Vantage, Yahoo Finance, and Financial Modeling Prep APIs React with TypeScript for a responsive, modern UI Google Cloud Run for serverless deployment Challenges we ran into collecting a large corpus of financial documents to serve as RAG deploying to Agent Engine, finally we put the backend on Cloud Run as an intermediate step ensuring agents produced consistent, high-quality outputs required extensive prompt engineering and response parsing logic moving from LangGraph to Google ADK required rewriting our agent orchestration not finding much free tier financial market APIs with generous rate limiting Accomplishments that we're proud of functional solution/tool with a nice dashboard learned to create a video with a voiceover audio overlay and embedding some slides seamlessly blending AI insights with live market data building on Google Cloud with proper separation of concerns and microservices architecture What we learned the quality of agent outputs depends heavily on precise, example-driven prompts raw LLM outputs need sophisticated parsing and validation to ensure consistency when dealing with external APIs and AI models, robust fallbacks prevent system failures What's next for TradeSage AI Features to be worked upon: real-time price tracking large corpus of documents for RAG, expanded data sources agent engine deployment integration with technical analysis indicators multi-user workspaces compliance and audit trails <div