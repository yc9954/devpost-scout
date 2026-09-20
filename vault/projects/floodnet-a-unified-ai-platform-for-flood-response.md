---
slug: "floodnet-a-unified-ai-platform-for-flood-response"
url: "https://devpost.com/software/floodnet-a-unified-ai-platform-for-flood-response"
title: "FloodNet - A unified AI platform for flood response"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 434
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/general_public"
  - "user/government_staff"
  - "user/patient_family"
  - "substrate/geospatial"
---

# FloodNet - A unified AI platform for flood response

> AI-powered flood resilience network providing personalized survival playbooks, real-time radar, and crowdsourced incident reporting—ensuring life-safety even when the network goes offline.

[Devpost](https://devpost.com/software/floodnet-a-unified-ai-platform-for-flood-response) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]] [[disaster_emergency]] [[elder_child_care]] [[health_clinical]] [[security_privacy]] [[supply_logistics]] [[transportation]]
**user** [[general_public]] [[government_staff]] [[patient_family]]
**substrate** [[geospatial]]

**stack** clerk, drizzle-orm, google-places, inngest, mapbox-gl, neon-postgresql, next.js-16, openweathermap-api, perplexity-ai, tailwind-css-4.0, typescript, vapi-ai, vercel

## How they structured the write-up

- 💡 inspiration
- 🚀 what it does
- 🛠️ how we built it
- 🧠 challenges we ran into
- 🔮 what's next for floodnet - a unified ai platform for flood response :-

## Body

Global Map Landing Screen Command Center Emergency SOS 🌊 FloodNet: The Unified AI Platform for Flood Resilience 💡 Inspiration Every year, floods displace millions and claim lives because of a critical "last-meter" gap. While governments provide high-level forecasts, individuals on the ground lack personalized, actionable survival data. They don't know exactly what to do for their specific house, their elderly family members, or their specific street. We built FloodNet to turn abstract meteorological data into a human-centric survival coordinate system. 🚀 What it does Professional Command Center: A Mapbox-powered satellite interface with real-time OpenWeatherMap layers for Precipitation, Wind, Temperature, and Pressure. Personalized Survival Coach: Users input their household context (floor level, vulnerable family members, vehicle access). Our AI then generates a step-by-step Survival Playbook and a 48-hour Risk Timeline. Voice-First SOS: Integration with VAPI AI allows users to report emergencies hands-free. The AI understands the gravity of the situation and automatically coordinates a response plan. Community Sensor Network: Citizens can report "ground-truth" data (water levels, blocked bridges, landslides) which are then instantly visualized for all users. Authority Ops Center: A dashboard for NGOs and government officials to triage rescue incidents and monitor community-reported hazards in real-time. 🛠️ How we built it We engineered FloodNet using a high-density modern stack focused on speed and reliability: Frontend: Next.js 16 (App Router) with Tailwind CSS 4.0 for a high-performance, responsive UI. AI Brain: Perplexity AI (Sonar Pro) for real-time web-searched flood intelligence, with Gemini 2.5 Flash as a robust fallback layer. Voice: VAPI for the emergency dispatcher interface. Mapping: Mapbox GL JS for custom raster/vector tile orchestration. Data & Auth: Neon PostgreSQL with Drizzle ORM for the data layer, and Clerk for secure user management. Infrastructure: Inngest for background cron jobs (ingesting weather data) and Vercel for serverless deployment. 🧠 Challenges we ran into The JSON Reliability Gap: Getting LLMs to consistently output structured JSON for complex mapping markers was difficult. We built a robust custom parser to handle malformed outputs and citation markers. Offline Access: Ensuring users can access life-saving data without a connection required a strategic localStorage caching logic that triggers the moment a "Crisis" state is detected. Tile Rate Limits: Managing OpenWeatherMap tile requests during high-frequency map panning required implementing tile-size optimizations to prevent API exhaustion. 🔮 What's next for FloodNet - A unified AI platform for flood response :- SMS/WhatsApp Integration: Moving beyond email alerts to reach users on low-bandwidth channels. Volunteer Asset Matching: A full logistics engine to match specific rescue boats and medical supplies with the nearest reported incidents. Edge AI: Running local models on-device for even greater offline autonomy. <div