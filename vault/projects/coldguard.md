---
slug: "coldguard"
url: "https://devpost.com/software/coldguard"
title: "ColdGuard"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 957
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# ColdGuard

> AI-powered cold chain guardian that protects life-saving medicines whether online or offline, at the edge or in the cloud.

[Devpost](https://devpost.com/software/coldguard) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[developer_tools]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** agentskills, alibaba, c++, ecs, flutter, javascript, litertlm, mcp, python, qwen, typescript

## How they structured the write-up

- inspiration
- what we built
- how we built it
- challenges
- what we learned
- what's next

## Body

ColdGuard: AI-Powered Cold Chain Guardian Inspiration Nearly 50% of vaccines worldwide are wasted due to cold chain failures. In Ghana and across Sub-Saharan Africa, clinics and pharmacies often lack reliable monitoring equipment. A nurse manually checks the fridge temperature twice a day, sometimes forgets to, or closes the unit storage half way after checking. If the power goes out at 2am, nobody knows. By then, the Amoxicillin is compromised, the Hepatitis B vaccines are gone, and patients receive degraded medicine or nothing at all without warning. ColdGuard was built to fix that. Not with expensive imported hardware, but with a $15 ESP32, a phone that every pharmacist already owns, and Qwen AI running both on-device and in the cloud. What We Built ColdGuard is a dual-layer pharmaceutical cold chain monitoring system: Edge Layer (offline-first): A Flutter app running a quantized Qwen model locally on an Android phone communicates with an ESP32 microcontroller via MQTT over a local network. The pharmacist can ask in natural language: "What is the temperature?" or "Alert me if temperature goes above 25°C." The local agent generates Lua monitoring scripts that are pushed to the ESP32 and run autonomously. When a threshold is breached, the ESP32 responds immediately with physical alerts: a red LED, a buzzer, and a cooling fan, all without any internet connection required. Cloud Layer (intelligent oversight): When the pharmacist is away and connectivity is available, the ESP32 syncs sensor readings to Alibaba Cloud ECS via HTTP. A FastAPI backend powered by a Qwen frontier model via Alibaba Model Studio performs deep pharmaceutical viability analysis using the Arrhenius degradation equation: $$k(T) = k_{ref} \cdot 2^{\frac{T - T_{ref}}{10}}$$ The cloud agent reasons step by step: it retrieves historical sensor data, calculates average temperatures and cumulative hours above safe thresholds, applies the Arrhenius equation using a code interpreter, cross-references WHO cold chain guidelines via web search, factors in humidity exposure, and arrives at a potency estimate with a clear verdict: SAFE , MONITOR , or DO NOT USE . This multi-step reasoning chain produces a report that is medically grounded and immediately actionable, not a generic alert but a specific recommendation the pharmacist can act on. Graceful Degradation: If the internet goes down, ColdGuard keeps working. The edge layer handles real-time monitoring and physical alerts independently. The cloud enhances but never gatekeeps. How We Built It The stack spans four codebases: coldguard-edge (C++) — ESP32 firmware built on ASHABridge, a custom hardware abstraction library. Implements a Lua runtime on Core 0 for autonomous script execution, MQTT command handling, DHT11 sensor reading, and HTTP cloud sync every 2 minutes. Digital actuator control for LEDs, buzzer, and fan via MQTT commands. coldguard-app (Flutter/Dart) — Flutter mobile app running a quantized Qwen model via the flutter_litert_lm package with GPU acceleration. Implements manual tool-calling via <tool_call> tag parsing since smaller on-device models require prompt-injected tool definitions rather than native function calling. Three local tools: publish_command , get_sensor_reading , and send_lua_script . coldguard-backend (Python/FastAPI) — FastAPI server with FastMCP exposing pharmaceutical analysis tools. Deployed on Alibaba Cloud ECS. backend stores time-series sensor readings . The build_vaccine_report MCP tool fetches historical sensor data and calls a Qwen frontier model with web search and code interpreter enabled for WHO-grounded viability assessment. coldguard-frontend (TypeScript/Node.js) — A WhatsApp agent framework built on whatsapp-web.js. Connects to the ColdGuard MCP server, handles conversation history via Redis, and supports scheduled agent tasks for automated reporting. Challenges On-device tool calling with small models: Smaller quantized Qwen models do not reliably use native function calling formats. The solution was manual tool injection into the system prompt with Qwen's <tool_call> XML format, then regex parsing of the raw model output. This required building a robust dispatch map and handling parallel tool calls in a single model response. Local network MQTT architecture: Running a fully offline edge system requires the phone and ESP32 to share a local network with an MQTT broker. The phone runs the Flutter app as the agent interface while the ESP32 connects to the same network and broker. This setup keeps the entire edge layer self-contained with no cloud dependency for real-time monitoring and hardware control. Pharmaceutical chemistry integration: Translating the Arrhenius degradation equation into an actionable prompt required grounding the model with specific drug stability data. The system prompt includes WHO reference URLs and instructs the Qwen frontier model to use the code interpreter for calculations, ensuring mathematical accuracy rather than hallucinated estimates. Edge-cloud architecture inversion: Most IoT submissions treat the cloud as the primary layer and the edge as a thin client. ColdGuard inverts this. The edge is the primary operating mode. The cloud is the enhancement. Designing graceful degradation as a first-class architectural concern rather than an afterthought required rethinking the data sync strategy and tool separation between local Dart functions and remote MCP tools. What We Learned Building ColdGuard revealed that the real challenge in agentic IoT is not the AI or the hardware in isolation, but the boundary between them. Getting a language model to reliably generate valid Lua scripts that execute correctly on a microcontroller requires careful prompt engineering, hardware-aware examples, and robust error handling at every layer. We also learned that small quantized models can perform meaningful agentic reasoning when given clear tool definitions and constrained problem domains. The pharmacist asking "alert me if temperature goes above 25°C" and receiving a hardware-deployed monitoring script seconds later is not science fiction. It runs on a mid-range Android phone and a $5 chip. What's Next ColdGuard's architecture generalizes beyond pharmaceuticals. The same edge-cloud agent pattern applies to food storage, laboratory sample monitoring, and agricultural cold chain. The ASHABridge firmware library that powers ColdGuard is designed as a universal agent-to-hardware abstraction layer, with ColdGuard as its first production deployment. <div