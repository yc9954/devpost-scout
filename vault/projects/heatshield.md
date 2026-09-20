---
slug: "heatshield"
url: "https://devpost.com/software/heatshield"
title: "Heatshield"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 351
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/security_privacy"
  - "substrate/geospatial"
---

# Heatshield

> HeatShield AI predicts neighborhood-level heat risk, estimates potential ER pressure, simulates intervention impact, and generates a city response playbook.

[Devpost](https://devpost.com/software/heatshield) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[health_clinical]] [[housing_homeless]] [[security_privacy]]
**substrate** [[geospatial]]

**stack** gemini, openmeteo, openstreetmap, react, tailwind, tanstack

## How they structured the write-up

- inspiration
- what we built
- how we built it
- what we learned
- challenges we faced
- what’s next

## Body

About the project Inspiration Extreme heat events are becoming more frequent, but response planning is still often reactive and city-wide instead of neighborhood-specific. We wanted to build a tool that helps emergency teams answer one critical question quickly: Where is the risk highest right now, and what should we do in the next 72 hours? What we built We built HeatShield AI , a real-time municipal heat response platform that: Pulls live weather and AQI signals Builds neighborhood-level risk views from open map data Simulates intervention impact (cooling centers, outreach, mobile clinics) Generates a structured 72-hour response playbook with Gemini If model generation fails, the app automatically returns a deterministic fallback plan so operations can continue. How we built it Frontend: TanStack Start + React + Tailwind CSS Backend: TanStack Server Functions + Nitro Node server Data: Open-Meteo (weather/AQI), OpenStreetMap Overpass (neighborhood/civic features) AI: Gemini API with multi-model failover Reliability: in-memory caching, source tracking, and graceful fallbacks Risk scoring combines heat pressure, vulnerability, and intervention effects. At a high level: $$ R_{adj} = \max\left(0,\; R_{base} - \Delta_{intervention}\right) $$ where: $$ R_{base} = \alpha \cdot H + \beta \cdot V + \gamma \cdot U $$ (H): heat pressure (temperature, humidity, AQI, grid stress) (V): social/health vulnerability (age, chronic illness, poverty, tree cover) (U): urban heat island component What we learned Live public data is messy; robust fallbacks matter more than perfect inputs. Model reliability is an engineering problem, not just a prompt problem. Clear UX for uncertainty (data source labels, fallback notes) builds trust. Fast iteration is easier when frontend and backend share one typed stack. Challenges we faced Model quota/rate limits: solved with model failover and transparent error reporting. Geospatial inconsistency: many places have sparse map tags; solved with derived features + synthetic fallback neighborhoods. Operational usability: raw LLM output was hard to consume until we added markdown + math rendering and structured sections. What’s next Add historical trend layers and forecast confidence intervals Add role-based operator workflows (health, utilities, emergency management) Integrate official city datasets for shelter occupancy and ambulance pressure Export machine-readable action plans for incident command systems <div