---
slug: "vitalguard-ai"
url: "https://devpost.com/software/vitalguard-ai"
title: "VitalGuard.ai"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 479
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
---

# VitalGuard.ai

> VitalGuard is an AI-powered real-time patient monitoring system that predicts medical deterioration using wearable vitals and autonomously coordinates alerts, first-aid guidance, and doctor response.

[Devpost](https://devpost.com/software/vitalguard-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]]

**stack** api, biomistral, bluetooth, bot, calendly, email, firebase, firestore, galaxyppg, gatt, langchain, langgraph, n8n, next.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- key innovations
- challenges we ran into
- what we learned
- what's next for vitalguard

## Body

Signin/signup initial version of stability in patient Features Calendly Inspiration Most existing patient monitoring systems react only after vitals cross dangerous thresholds. We kept asking a simple question: What if a system could warn families and doctors before a medical emergency actually happens? VitalGuard was built to shift healthcare monitoring from reactive alerts to predictive, autonomous decision-support. Our goal was to design a system that not only detects deterioration early, but also coordinates response automatically — even in low-connectivity environments. What it does VitalGuard is an AI-powered real-time patient monitoring system that predicts medical deterioration using wearable vitals and autonomously coordinates emergency response workflows. It ingests vitals from: Bluetooth wearable devices (HR, HRV, SpO₂, temperature) GalaxyPPG real signal streams Synthetic simulator scenarios for testing Each reading flows through a LangGraph agent pipeline that: computes risk scores (0–100 severity index) predicts deterioration using trend analysis retrieves 7-day patient memory generates AI clinical reasoning provides personalized first-aid guidance dispatches multi-channel alerts discovers nearby doctors automatically escalates if the patient does not respond enables offline diagnosis using local medical LLMs How we built it VitalGuard is built as a state-machine driven agentic healthcare pipeline using: LangGraph for orchestration BioMistral for clinical reasoning MedLlama2 (Ollama) for offline diagnostics Firebase Firestore for longitudinal medical memory Web Bluetooth GATT for wearable vitals ingestion SerpApi for nearby doctor discovery Twilio, Telegram, Email for escalation alerts n8n for autonomous recovery workflows Calendly for consultation scheduling Vitals flow through a 12-node agent pipeline: ingest → risk → trend prediction → memory retrieval → reasoning → first aid → escalation → triage → doctor discovery → persistence Key innovations VitalGuard introduces five major agentic capabilities: Predictive deterioration detection Trend analysis predicts CRITICAL conditions before thresholds are crossed. Longitudinal medical memory AI reasons using 7-day patient history instead of single readings. Autonomous triage coordination Alerts, reasoning, and first-aid instructions execute in parallel. Recovery workflow automation If alerts go unacknowledged, consultations are auto-booked and voice calls triggered. Offline diagnostic intelligence MedLlama2 enables differential diagnosis without internet connectivity. Challenges we ran into Integrating real-time wearable vitals with an autonomous agent pipeline during a hackathon environment was one of the biggest challenges. Designing a system that works both online and offline required building fallback reasoning layers using local LLM inference. Coordinating multiple escalation channels while maintaining deterministic routing inside the LangGraph pipeline also required careful architecture design. What we learned We learned how agentic AI can move healthcare systems from passive dashboards to autonomous decision-support infrastructure. We also explored how wearable sensing, longitudinal patient memory, and recovery workflows can be combined into a single scalable pipeline. What's next for VitalGuard We plan to extend VitalGuard into a deployable remote patient monitoring infrastructure for: rural telemedicine networks ambulance triage systems elderly home monitoring ICU early-warning assistants Our long-term vision is to build predictive healthcare systems that act before emergencies happen , not after. <div