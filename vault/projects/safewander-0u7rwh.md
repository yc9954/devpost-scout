---
slug: "safewander-0u7rwh"
url: "https://devpost.com/software/safewander-0u7rwh"
title: "SafeWander"
hackathon: "Student Innovators Without Borders Hacks (Students; Open Ended)"
organization: "Batch 09"
winner: true
words: 430
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# SafeWander

> Wander safely, worry less

[Devpost](https://devpost.com/software/safewander-0u7rwh) · hackathon [[Student Innovators Without Borders Hacks -Students- Open Ended-]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[structured_db]]

**stack** fastapi, leaflet.js, lucidchart, next.js, pydantic, react, sqlite, swr, tailwind, typescript, uvicorn

## How they structured the write-up

- inspiration
- what it does
- 🛠️ how we built it

## Body

Inspiration SafeWander was born from a deeply personal need—watching loved ones with dementia struggle with the balance between independence and safety. Traditional GPS trackers only tell you where someone is, but they don't understand why their movement matters. We envisioned a system that could learn individual behavior patterns and provide intelligent, proactive care rather than just reactive alerts. The name "SafeWander" embodies our core philosophy: everyone deserves the freedom to move while staying protected . What it Does SafeWander is an AI-powered GPS tracking and safety monitoring system designed specifically for patients with dementia, Alzheimer's, or other cognitive conditions. It goes beyond simple location tracking by: Behavioral Learning : Establishes baseline movement patterns using statistical analysis Intelligent Geofencing : Creates safe, home, and caution zones with automatic anomaly detection Real-time Risk Assessment : Calculates risk scores based on: Distance from safe zones: \( d_{safe} = \min(\text{distance to each safe zone}) \) Speed anomalies: \( \Delta v = |v_{current} - \mu_{speed}| \) Time-based patterns: \( \text{risk}_{time} = f(\text{hour}, \text{historical patterns}) \) Movement entropy: \( H = -\sum p_i \log p_i \) where \( p_i \) is the probability of visiting location cluster \( i \) Multi-level Alert System : Critical, high, medium, and low severity alerts with smart escalation Caregiver Dashboard : Beautiful, intuitive interface with live maps, activity feeds, and vital statistics Comprehensive Reporting : Exportable data for medical professionals and family members The risk engine combines multiple factors into a unified risk score: $$ \text{Risk} {total} = w_1 \cdot R {distance} + w_2 \cdot R_{speed} + w_3 \cdot R_{time} + w_4 \cdot R_{zone} $$ Where weights \( w_i \) are dynamically adjusted based on patient history and current context. 🛠️ How We Built It Frontend (Next.js + TypeScript) Built with Next.js 14 using App Router for optimal performance Shadcn/ui component library for a polished, accessible interface Leaflet.js for interactive map visualization with custom markers and zone overlays Real-time updates using React hooks and automatic polling Custom demo simulator for realistic movement pattern generation during development Backend (Python + FastAPI) FastAPI REST API with automatic OpenAPI documentation SQLite database with SQLAlchemy ORM for reliable data persistence Haversine formula for accurate distance calculations: $$ d = 2r \arcsin\left(\sqrt{\sin^2\left(\frac{\phi_2-\phi_1}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\lambda_2-\lambda_1}{2}\right)}\right) $$ Where \( r \) is Earth's radius, \( \phi \) is latitude, \( \lambda \) is longitude AI/ML Components Baseline Learning Algorithm : Tracks movement patterns over 7-day rolling windows Anomaly Detection : Statistical deviation analysis using z-scores State Machine : Manages alert states (pending → acknowledged → resolved) Risk Engine : Multi-factor scoring with configurable thresholds Architecture Highlights <div