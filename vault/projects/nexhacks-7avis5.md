---
slug: "nexhacks-7avis5"
url: "https://devpost.com/software/nexhacks-7avis5"
title: "Flowly AI"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 569
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/multi_agent"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Flowly AI

> Flowly AI automates E2E front-end testing with agentic, vision-based UX analysis. It continuously learns your codebase and uses deltas to build tests that cover code requirements and user intent.

[Devpost](https://devpost.com/software/nexhacks-7avis5) · hackathon [[NexHacks]]

## Facets

**mechanism** [[cross_origin_web]] [[multi_agent]] [[sensor_fusion]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** arize, crux), datadog, devswarm, gemini, json, node.js, opentelemetry, phoenix, playwright, typescript, woodwide, yaml, zod

## How they structured the write-up

- inspiration
- what we built
- technical architecture
- overall difficulty

## Body

Inspiration FlowGuard came from a recurring frustration we kept seeing in frontend teams—especially small to mid-sized startups and solo developers. Features would pass QA, Playwright tests would be green, and yet real users still struggled. Buttons existed but weren’t visible. API calls were silently failing. Console errors were piling up unnoticed. The deeper issue wasn’t bad engineering—it was a mismatch between what we test and what we understand. Traditional E2E testing validates that actions complete. It doesn’t capture the full execution context: the DOM state, network behavior, console output, and performance characteristics that explain why something failed or how users actually experience a flow. At NexHacks , with its AGI-first mindset, this felt like the right moment to rethink frontend testing entirely—not by adding more assertions, but by giving AI agents the tools to autonomously execute, observe, and analyze. What We Built FlowGuard is an AI-native testing platform that captures comprehensive execution data and enables AI agents to autonomously analyze UX flows. Instead of writing assertion-heavy scripts, developers describe what a user should be able to do, for example: "Test the checkout flow for UX issues and performance bottlenecks." FlowGuard: Exposes Playwright operations as MCP tools that AI agents can call Executes flows in a real browser while capturing everything—DOM snapshots, network requests, console logs, and performance metrics Stores execution data in a queryable format Enables AI to analyze the captured data for accessibility violations, performance issues, and error patterns Produces human-readable insights with clear recommendations and visual evidence The result is testing that captures the full picture, removes manual analysis, and turns raw execution data into actionable insights. This is especially valuable for teams who want AI to do the debugging—not just the clicking. Technical Architecture FlowGuard was challenging to build because it combines MCP-based tool abstraction , comprehensive execution data capture , multimodal AI analysis , and production-grade observability into a single system. Building this in a short timeframe required rapidly learning and integrating multiple complex tech stacks simultaneously. DevSwarm DevSwarm was used to develop and orchestrate all of FlowGuard’s components. The MCP server, execution data capturer, AI analyzer, and dashboard were each implemented as modular pieces that could be developed and tested independently. This made FlowGuard agent-native from day one —AI agents interact with the system through well-defined MCP tools rather than brittle APIs. Arize Phoenix Arize Phoenix was used for AI observability and execution tracing. Every flow execution is instrumented with OpenTelemetry , creating detailed traces that show each step, the captured DOM state, network activity, and AI analysis results. This ensures the entire testing pipeline is transparent and debuggable instead of a black box. Model Context Protocol (MCP) MCP powers the abstraction layer between AI agents and Playwright. Tools like execute_flow , get_execution_data , and analyze_flow_execution allow any MCP-compatible AI to autonomously run tests, retrieve results, and generate insights. This design means FlowGuard works with Claude—or any future agent that speaks MCP. Datadog Datadog was used for system-level monitoring during development and demo preparation. We tracked execution time, browser pool performance, and database query latency to ensure FlowGuard remained stable and responsive under live demo conditions. Overall Difficulty The hardest part was designing an execution data schema rich enough for AI analysis while keeping captures fast and storage-efficient. Coordinating real browser execution, comprehensive data capture, and AI-powered analysis—all exposed through clean MCP interfaces—required careful system design and rapid learning across several production-grade tools. <div