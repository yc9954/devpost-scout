---
slug: "autoaegis"
url: "https://devpost.com/software/autoaegis"
title: "AutoAegis"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 948
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# AutoAegis

> AutoAegis-"Self-Diagnostic Immunity System" that eliminates the Watermelon Effect by using Zero-Touch Shadowing

[Devpost](https://devpost.com/software/autoaegis) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[genomic_bio]] [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** cesium, express.js, next.js, node.js, ollama, playwright, supabase

## How they structured the write-up

- inspiration: the watermelon effect
- what it does: self-diagnostic immunity
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for autoaegis

## Body

Dashboard Monitor Dashboard 1 Geographic Visualization Monitor Dashboard 2 Landing Page "npm" published page Inspiration: The Watermelon Effect The core inspiration for AutoAegis is the "Watermelon Effect"—a common phenomenon in DevOps where system dashboards glow green (100% uptime), but the internal user experience is "bleeding red" due to silent failures. The Visibility Gap: Traditional monitoring focuses on infrastructure (CPU/RAM) rather than the Integrity of the Transaction. The Revenue Risk: A "Buy" button that is visually present but functionally dead due to a 500-series API error is a "Silent Killer" of revenue. The Diagnostic Delay: When a failure occurs, developers often spend hours sifting through logs to find the "Why" behind the "What". What it Does: Self-Diagnostic Immunity AutoAegis acts as a Self-Diagnostic Immunity System for businesses by shifting from passive "pinging" to active "journey validation". A. Shadow Recording (Learning the DNA)The system learns the Healthy DNA of an application by "shadowing" a real human user for 30 seconds.It maps CSS Selectors, API Dependencies, and Human Latency Baselines.It establishes a Golden Path map that serves as the immutable standard for future tests. B. Synthetic Stress-TestingA Guardian Fleet of headless browsers replays these Golden Paths from 20+ global regions. Performance Delta: It calculates the degradation between the recorded human baseline ($L_{base}$) and the live simulation ($L_{live}$):$$\text{Degradation} = L_{live} > (L_{base} \times 1.5)$$ Silent Sentinel: It intercepts 400/500-series network errors that occur behind functional-looking UI elements. C. Automated Forensics:If a journey fails, the system doesn't just send an alert; it delivers an Evidence Locker. HAR Files: A complete "Network X-Ray" of every request and response. Trace Logs: A "Flight Recorder" of the DOM and console state at the exact millisecond of failure. Virtual SRE: An AI-powered diagnostic that provides a human-readable root cause and recommended fix. How we built it The project is built on a high-fidelity, three-tier architecture designed for scale and forensic accuracy. The Aegis Observer (Frontend & Recording) Next.js 15 & React 19: Powers the high-performance dashboard. Shadow Script: A lightweight recorder that captures DOM mutations and user intent without overhead. Cesium.js: Provides the Bhoomi Latency Map, a 3D visualization of global system health. The Guardian Fleet (Execution & Automation) Playwright: Used for deep-link browser automation and replaying journeys. Self-Healing AI (Groq/LLM): Generates resilient scripts that automatically adapt to UI changes by intelligently updating CSS selectors. Chaos Engineering: A middleware that artificially introduces latency and failures to test system resilience. The Central Hub (Backend & Storage) Node.js/Express: Manages the multi-tenant API and monitor lifecycle. Supabase (PostgreSQL & JSONB): Stores high-velocity journey data and forensic artifacts. Security & Privacy: Implements Zero PII Leakage by automatically masking sensitive data (passwords, credit cards) during recording. Challenges we ran into Building a system that "shadows" human intent and replays it with 100% accuracy presented significant technical obstacles: DOM Flakiness and Dynamic Selectors: Modern web apps change class names frequently, which typically breaks synthetic scripts; we had to engineer an LLM-powered self-healing logic to intelligently update CSS selectors on the fly. The "Noise" Problem: Real-world applications are full of non-critical errors (like analytics timeouts); we struggled to distinguish this "Baseline Noise" from actual Business Failures until we implemented our recording-phase "blood test". High-Velocity Data Ingestion: Managing the massive influx of journey logs, HAR files, and traces required a highly optimized pipeline using PostgreSQL JSONB to ensure real-time dashboard updates without latency. PII Security: Capturing user journeys naturally risks recording sensitive data; we had to build an automated masking layer to ensure Zero PII Leakage of passwords or credit card info during the 30-second shadowing phase. Accomplishments that we're proud of We moved beyond simple monitoring into the realm of Automated Forensics and proactive defense: Zero-Touch Shadowing: We successfully built a recorder that learns an application's "Healthy DNA" in just 30 seconds of human use, removing the need for developers to write a single line of test code. The Virtual SRE: We are incredibly proud of our AI-powered diagnostic engine, which analyzes technical wreckage (HAR files and DOM traces) to deliver a human-readable root cause and fix in seconds. Global Visual Transparency: Integrating Cesium.js to create the Bhoomi Latency Map allowed us to visualize system health across 20+ global regions in a professional 3D environment. The "Avocado" Metric: We created a new standard for health—the Journey Integrity Score—which proves that the "core" of a transaction is functional even when external dashboards are misleading. What we learned This project pushed our understanding of Outside-In Observability and human-centric engineering: Uptime is a Vanity Metric: We learned that a site can be "100% Up" while being "100% Broken" for the user; validating the integrity of the transaction is the only metric that truly matters. Context is King: A stack trace alone is useless; by capturing the "Preceding Events" (what happened before the crash), we learned that we could automate the entire causal chain of debugging. AI as a Maintenance Layer: We discovered that LLMs are most powerful when used for Resilience—automatically fixing broken selectors so that monitoring remains "set it and forget it" for the developer. What's next for AutoAegis We are just beginning to build the ultimate "Immunity System" for the web: Predictive Anomaly Detection: We plan to implement machine learning models that can predict a "Silent Red" failure before it happens by analyzing subtle shifts in Performance Deltas. Multi-Platform Shadowing: Expanding our 30-second recorder to support Mobile Web and React Native environments. Automated PR Fixes: Integrating directly with GitHub to not only diagnose the bug but automatically open a Pull Request with the recommended fix generated by our Virtual SRE. Global Chaos Simulations: Enhancing our Chaos Middleware to simulate large-scale regional ISP failures, ensuring AutoAegis users are prepared for the most extreme global outages. <div