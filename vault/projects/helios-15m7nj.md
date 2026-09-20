---
slug: "helios-15m7nj"
url: "https://devpost.com/software/helios-15m7nj"
title: "Helios"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 933
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/scientific_research"
  - "domain/transportation"
  - "user/general_public"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Helios

> Helios is a IoT Swarm Orchestration tool using Simulated Hardware in Loop testing to allow LLM agents to develop and test full IoT systems, before actually deploying and monitoring these systems

[Devpost](https://devpost.com/software/helios-15m7nj) · hackathon [[NexHacks]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[scientific_research]] [[transportation]]
**user** [[general_public]] [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, claude, claudeai, embeddedc, esp32, fastapi, iot, machine-learning, mqtt, platformio, python, qemu, react, renode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for helios

## Body

Helios Logo Helios Homepage Helios Design Helios Build Helios Deploy Inspiration We were inspired by the complexity barrier in IoT development. IoT is a rising field for its ability to create realtime data sets for AI/ML from real world sensors, however creating a network of microcontrollers traditionally requires deep embedded systems knowledge, understanding register-level programming, memory management, and hardware-specific quirks. We asked: "What if anyone could build distributed sensor networks just by describing what they want in plain English?" The Pittsburgh traffic monitoring use case hit close to home - cities need real-time traffic data for smart infrastructure, but deploying 50+ sensors with custom firmware is prohibitively complex and expensive. We wanted to make this accessible to urban planners, researchers, and citizen scientists. What it does Helios is an AI-powered platform that transforms natural language descriptions into working embedded systems: Natural Language to Firmware : Describe your system ("Temperature sensor with CSV logging") and Claude AI generates optimized embedded C code that respects memory constraints Automated Build & Test : Compiles firmware, simulates in QEMU/Wokwi, and iteratively refines until tests pass Smart Data Export : Automatically integrates CSV logging via serial, SD card, or HTTP endpoints using Woodwide AI Full Deployment Pipeline : Flash real hardware (ESP32/STM32) and provision cloud infrastructure with one click How we built it Backend (Python) FastAPI for REST API with WebSocket real-time updates Claude AI (Anthropic) to generate embedded C firmware from natural language prompts QEMU for ARM simulation and Wokwi for ESP32 WiFi/sensor simulation Woodwide AI for intelligent CSV data analytics and predictions Terraform for automated AWS infrastructure provisioning Custom orchestration layer with iterative refinement (generates → compiles → tests → retries) Frontend (React + TypeScript) Visual design canvas with drag-and-drop device placement Real-time build monitoring via WebSockets Multi-stage workflow (Design → Build → Simulate → Deploy) Built with Vite, Tailwind CSS, and shadcn/ui components Hardware Integration Direct USB flashing using esptool.py (ESP32) and stm32flash (STM32) Automatic device detection and board identification Support for 7+ board types (ESP32, STM32 family, Arduino, LM3S6965) Challenges we ran into Memory Constraints : Generated code often exceeded Flash/RAM limits on smaller boards (STM32F103 has only 20KB RAM). We solved this by prompting Claude to track memory usage and avoid dynamic allocation. Simulation Reliability : QEMU's semihosting is fragile - timing issues caused flaky tests. We implemented robust timeout handling and output parsing to make simulations deterministic. ESP32 WiFi Simulation: QEMU doesn't support WiFi. We integrated Wokwi's cloud simulator, which required learning their API and handling asynchronous compilation with PlatformIO. Iterative Refinement : Teaching the AI to learn from compilation errors was tricky. We built a feedback loop that provides error context to Claude, dramatically improving success rates from ~40% to ~85%. WebSocket State Management : Coordinating real-time updates across multiple build sessions while maintaining clean session state required careful architecture with proper cleanup and error handling. CSV Data Extraction : Parsing CSV from mixed simulation output (debug logs, test results, actual data) required smart pattern matching and buffer management. Accomplishments that we're proud of It actually works end-to-end! Natural language → working firmware → real hardware deployment 85% success rate on first-try firmware generation across diverse use cases Pittsburgh traffic system : Generated and simulated 50 sensor nodes with realistic traffic data - a real-world demo that showcases the platform's power Automatic CSV integration : Detects data logging requirements from natural language and automatically injects CSV buffer management code Sub-minute generation : From prompt to tested firmware in under 60 seconds for simple systems Full stack integration : Working API with WebSocket real-time updates, visual frontend, hardware flashing, and cloud deployment Smart iteration : The AI learns from compilation errors and test failures, getting better with each attempt Production-ready architecture : Clean separation of concerns, background task execution, comprehensive error handling What we learned Technical How to prompt LLMs for constrained code generation (no stdlib, fixed memory limits) QEMU's internals and semihosting for bare-metal simulation The complexity of cross-compilation toolchains and linker scripts WebSocket state management for long-running background tasks Terraform for reproducible infrastructure provisioning AI/LLM Iterative refinement dramatically improves success rates over one-shot generation Providing concrete constraints (memory limits, compilation errors) helps Claude generate better code Few-shot examples in prompts are crucial for embedded code generation LLMs can understand hardware concepts surprisingly well with proper context Product The importance of real-time feedback - users need to see progress during 30+ second build times Visual design tools make complex systems more approachable End-to-end demos (like Pittsburgh traffic) are more compelling than toy examples CSV export is a killer feature - everyone needs their data somewhere Teamwork Clear API contracts enable parallel frontend/backend development Good documentation (like our INTEGRATION.md) saves hours of explanation WebSocket events are great for coordinating distributed systems What's next for Helios Short-term (Next Month) Inter-node communication: Enable microcontrollers to talk to each other via CAN bus, I2C, or UART Mobile app: Monitor deployed systems and view live sensor data Template library: Pre-built systems (weather station, smart home, industrial monitor) User accounts: Save projects, share designs, and collaborate Medium-term (3-6 Months) Multi-user collaboration: Real-time co-editing like Figma Advanced analytics: Woodwide AI integration for predictive maintenance and anomaly detection Edge ML: Generate TensorFlow Lite models for on-device inference OTA updates: Push firmware updates to deployed devices remotely Custom board support: Let users define their own board configurations Long-term Vision Industrial partnerships: Deploy in real smart cities, factories, and research facilities Educational platform: Teach embedded systems through natural language Marketplace: Community-contributed sensors, templates, and integrations Hardware-as-a-Service: Order pre-flashed devices delivered to your door Multi-architecture: Support RISC-V, AVR, and custom ASICs <div