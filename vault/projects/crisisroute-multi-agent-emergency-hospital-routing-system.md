---
slug: "crisisroute-multi-agent-emergency-hospital-routing-system"
url: "https://devpost.com/software/crisisroute-multi-agent-emergency-hospital-routing-system"
title: "CrisisRoute AI –|Right Patient |Right Hospital |Right Time."
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 419
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
---

# CrisisRoute AI –|Right Patient |Right Hospital |Right Time.

> A Gemini-powered emergency healthcare routing platform and MCP-integrated Elasticsearch that intelligently matches patients to the most clinically appropriate hospital using multi-agent reasoning

[Devpost](https://devpost.com/software/crisisroute-multi-agent-emergency-hospital-routing-system) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[health_clinical]]
  <sub>weak: disaster_emergency</sub>
**user** [[patient_family]]
**substrate** [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** css, elasticsearch, fastapi, google-cloud-run, google-gemini, html, javascript, mcp, python, react, rest-apis, vite

## Body

Inspiration In emergency situations, patients are often transported to the nearest hospital rather than the most clinically appropriate hospital. For conditions such as cardiac arrest, stroke, trauma, or neurological emergencies, arriving at a facility without the required specialty team, ICU capacity, or treatment capability can delay care during the critical golden hour. We built CrisisRoute AI to demonstrate how AI agents, real-time hospital intelligence, and cloud infrastructure can work together to help patients reach the right hospital faster. What it does CrisisRoute AI is a multi-agent emergency response platform that: Accepts patient symptoms Performs AI-powered triage using Gemini Determines required medical specialty Searches nearby hospitals Evaluates real-time capacity Calculates routing scores using ETA, ICU availability, specialty capability, and capacity Reserves beds Notifies hospitals Displays emergency operations through a live dashboard How we built it Frontend: React Vite Backend: FastAPI Python AI: Gemini 2.5 Flash Search & Data: Elasticsearch Infrastructure: Google Cloud Run Google Cloud Pub/Sub Architecture: MCP (Model Context Protocol) Multi-Agent Pipeline Server-Sent Events (SSE) The platform is organized as a multi-agent workflow: Triage Agent Specialty Match Agent Hospital Search Agent Capacity Agent Routing Agent Admission Agent Notify Agent Agents communicate through an MCP-powered Elasticsearch layer that exposes tools for specialty matching, hospital discovery, capacity verification, reservations, and analytics. Routing Intelligence Unlike traditional nearest-hospital routing, CrisisRoute evaluates: Travel ETA Available beds Available ICU beds Specialty match Capacity status Critical emergencies prioritize travel time and clinical capability over pure geographic proximity. Challenges Major challenges included: Designing safe emergency routing logic Building explainable AI recommendations Integrating Elasticsearch through MCP Modeling realistic hospital capabilities and capacity Building low-latency multi-agent orchestration Creating reliable real-time notification workflows Accomplishments Gemini-powered emergency triage MCP-integrated Elasticsearch architecture Explainable hospital ranking AI-generated emergency briefings Google Cloud Pub/Sub notification pipeline Real-time emergency operations dashboard Telugu and English accessibility support Cloud-native deployment on Google Cloud Run Comprehensive automated testing What we learned We learned that emergency healthcare routing is fundamentally a systems problem rather than a single-model problem. Effective decision support requires combining AI reasoning, hospital discovery, capacity awareness, routing intelligence, explainability, and real-time communication into a unified workflow. We also learned how MCP creates a clean separation between AI agents and search infrastructure, enabling scalable multi-agent architectures. Future Work Future versions will include: Ayushman Bharat Digital Mission (ABDM) integration Live ambulance dispatch integration Real hospital occupancy feeds Predictive bed availability forecasting Voice-first multilingual emergency interface Expansion beyond Andhra Pradesh Hospital information system integration Our goal is simple: help patients reach the right care faster when every minute matters. <div