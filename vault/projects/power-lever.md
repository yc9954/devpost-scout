---
slug: "power-lever"
url: "https://devpost.com/software/power-lever"
title: "Power Lever"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 310
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Power Lever

> Agentic inference optimization. Unlike static inference providers, we dynamically orchestrate GPUs and implement on-demand speculative decoding to deliver inference control, saving water and compute.

[Devpost](https://devpost.com/software/power-lever) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** claude, fastapi, modal, node.js, openai, vercel, vllm

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for power lever

## Body

Inspiration What's the derivative of arccos(x)? I asked Claude Opus 4.6. Too many times, we've overkilled our prompts by feeding simple tasks into state-of-the-art models. The fact that inference providers only allow a small number of model options means that every task is either underserved or overserved. There’s no way to precisely match compute to problem difficulty; you either spin up a sledgehammer or settle for something too weak . We wanted inference to behave less like a fixed menu and more like a tunable dial. What it does We introduce three core technical contributions: 1) On-demand speculative decoding (via vLLM) We implement speculative decoding as a first-class, runtime-configurable primitive using vLLM, dynamically adjusting draft model selection and tokens-ahead per request. Instead of statically enabling acceleration, speculative decoding becomes an adaptive service layer that optimizes acceptance rate, latency, and compute efficiency in real time. 2) Hardware flexibility (via Modal GPU orchestration) We decouple inference from fixed infrastructure by programmatically orchestrating Modal GPU profiles per request. The system can select between hardware configurations based on latency targets, utilization, and energy constraints, transforming GPU selection into a tunable parameter rather than a deployment-time decision. 3) Agentic routing (via Claude Agent SDK) We implement a Router Agent using the Claude Agent SDK that observes hardware state, user-defined performance constraints, and prior run metrics to plan and apply optimal inference configurations. The agent closes the loop between intent (“faster,” “cheaper,” “more efficient”) and execution by autonomously selecting hardware and speculative decoding hyperparameters before each inference call. How we built it Modal, vLLM, FastAPI, Claude Agent SDK, Vercel, Next.js Accomplishments that we're proud of Serving models with less water waste. What's next for Power Lever Use live telemetry (TTFT, throughput, early perplexity) to auto-escalate or downshift mid-generation. Improve speculative decoding instrumentation: report real per-token accept/reject rates and tune $k$ and $\tau$ automatically per request. <div