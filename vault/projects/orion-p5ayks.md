---
slug: "orion-p5ayks"
url: "https://devpost.com/software/orion-p5ayks"
title: "Orion"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 678
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Orion

> AI-powered wildfire operations dashboard with autonomous agents, live video streaming, and voice control—transforming emergency response through real-time intelligence.

[Devpost](https://devpost.com/software/orion-p5ayks) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[human_in_the_loop]] [[provenance_signing]] [[realtime_stream]]
**domain** [[disaster_emergency]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, clsx, composio, date-fns, eslint, fetch-ai, lightning-css, lucide-react, mapbox, mapbox-directions-api, mapbox-gl-js, next.js, open-meteo, postcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orion

## Body

Inspiration In California, 81% of residents (26M+) live with wildfire risk , and 2025 alone has seen 7,500+ fires that burned ~ 500,000 acres . In late-night ride-alongs and debriefs with emergency volunteers, one theme kept coming up: incident commanders are forced to stitch together radios, spreadsheets, texts, and maps while the fire grows by the minute . Orion was born to replace that chaos with a single, AI-powered command center—so responders can act faster, smarter, and safer. What it does Orion is an AI wildfire operations dashboard that turns raw data into decisions: 🗺️ Live 3D Situational Awareness — Real-time fire incidents, wind-aware spread prediction, weather/AQI overlays, and embedded live video on the map. 🤖 Autonomous Agents — Background Python + Fetch.ai uAgents monitor incidents, compute risk, and continuously propose optimal routes for responders and evacuations. 🗣️ Voice Operations — VAPI-powered hands-free control: “Status of Pine Ridge? Dispatch two teams. Read me wind for the next hour.” 🚒 Dynamic Dispatch & Containment — One-click deploy from nearest station, animated units along routes, on-scene detection (Haversine), and visual containment progression. 🚨 Multi-Channel Alerts — Telegram/SMS notifications with formatted incident payloads, delivery confirmation, and retry logic. Outcome: a unified command center that cuts coordination time, reduces guesswork, and helps protect people and property when every second counts. How we built it Frontend & UX Next.js 16 + React 18 + TypeScript for fast, type-safe UI Tailwind + Radix UI + shadcn for accessible, production-ready components Mapbox GL JS + react-map-gl for 3D terrain, custom layers, and route rendering Realtime & Data Supabase (Postgres + Realtime) for incidents, firestations, responders; sub-second sync via WebSockets Open-Meteo for weather/AQI (no key), Mapbox Directions for routing AI, Agents & Voice Python uAgents (Fetch.ai) : monitoring agent (risk scoring, anomaly detection) + route agent VAPI (@vapi-ai/web) : domain-tuned prompts, low-latency voice queries & responses Comms & Integrations Composio + Telegram Bot API for one-click alerts, message IDs, retries Fire Spread Modeling Custom multi-octave noise + wind vectors to generate organic, non-circular boundaries and time-based growth. Deployed with Vercel/AWS Amplify ; strict ESLint/TypeScript rules, cleanup on unmount, and debounced updates to keep the UI crisp. Challenges we ran into Realistic fire behavior without jank: Getting organic, wind-influenced edges that don’t “flicker” or become perfect circles required multi-octave noise, normalization, and careful animation timing. Keeping everything in sync: Incidents, responders, routes, weather panels, and voice state had to update in lock-step. Memory leaks were a risk—solved with disciplined subscription cleanup and state batching. Smooth responder movement + arrival detection: Interpolating along polyline routes while computing precise on-scene thresholds (Haversine) and status transitions. Voice in crisis contexts: VAPI needed wildfire terminology, context injection (active incidents, weather), and graceful fallback when mic/connection issues occurred. Video performance in map popups: Ensured codecs/fallbacks didn’t tank FPS; isolated rendering paths. Accomplishments that we're proud of ✅ A complete, working workflow : detection → analysis → dispatch → alerts → containment visualization. ✅ Sub-second realtime across clients with Supabase Realtime—and zero critical leaks. ✅ Agent ecosystem that actually runs unattended (monitoring + routing) with actionable recommendations. ✅ Voice-first operations that meaningfully reduce clicks in high-stress moments. ✅ Designed for scale : 25+ active incidents, many concurrent users, 60 FPS animations on commodity hardware. What we learned Geospatial math is everything: Haversine distance, bearings, and interpolation underpin user trust. Realtime demands discipline: WebSocket lifecycles, debouncing, optimistic updates, and teardown patterns are non-negotiable. Voice shines when hands are busy: In command roles, conversational ops beat menus—if latency stays <2s and context is accurate. Agents ≠ background tasks: Orchestration, retries, and human-in-the-loop UX are product features, not just infra. What's next for Orion 🛰️ NASA FIRMS satellite ingestion for earlier detection 📱 Native iOS/Android apps for field teams with offline sync 🗺️ Automatic evacuation zone mapping + geofenced public alerts ⚡ Predictive resource staging (AI forecasts for pre-positioning crews/equipment) 👥 Multi-agency roles & audit trails (CAL FIRE, local, federal) 📊 Historical analytics : response times, allocation efficiency, and after-action insights Orion’s mission: put actionable intelligence in the hands of first responders—when it matters most. <div