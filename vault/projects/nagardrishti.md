---
slug: "nagardrishti"
url: "https://devpost.com/software/nagardrishti"
title: "NagarDrishti"
hackathon: "Gemini Live Agent Challenge"
organization: "Google"
winner: true
words: 996
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/legal_justice"
  - "user/general_public"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# NagarDrishti

> AI-powered road hazard detection for Pune — citizens report via video or voice using Gemini Live API, while PMC officers manage hazards through an AI chat dashboard on Google Cloud.

[Devpost](https://devpost.com/software/nagardrishti) · hackathon [[Gemini Live Agent Challenge]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[civic_government]] [[legal_justice]]
  <sub>weak: developer_tools, disaster_emergency, finance_payments, transportation</sub>
**user** [[general_public]] [[government_staff]]
  <sub>weak: frontline_worker</sub>
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** dart, docker, fastapi, flutter, gemini-live-api, google-bigquery, google-cloud, google-cloud-run, google-container-registry, google-gemini-api, mapbox, next.js, open-meteo-api, python

## Body

Inspiration Pune, India has over 7 million people across the metropolitan region and 2,273 km of municipal roads spanning four jurisdictions (PMC, PCMC, PMRDA, Cantonment). During monsoon season, potholes and waterlogging cause hundreds of accidents. In October 2025, the Bombay High Court mandated that every pothole must be repaired within 48 hours after multiple fatalities, with personal liability on senior officials for delays. Yet citizens have no efficient way to report hazards, and municipal officers lack real-time situational awareness. We built NagarDrishti ("City Vision" in Hindi) to bridge this gap — an AI-powered platform where citizens report road hazards through video or natural voice conversation, and municipal officers manage them through an intelligent dashboard with AI chat capabilities. What it does For Citizens (Flutter Mobile App): Video Reporting: Record a 5–10 second video of any road hazard. The AI pipeline automatically classifies the hazard type (pothole, waterlogging, damaged road, etc.), assigns severity (1–5), identifies the responsible municipal jurisdiction from GPS, detects duplicates within 20 meters, checks weather forecasts to adjust severity during monsoon, and estimates physical dimensions. Commute Mode (Gemini Live API): A hands-free, always-listening voice mode for drivers and riders. Speak naturally — "There's a big pothole ahead" — and the Gemini Live agent creates the report instantly using real-time audio streaming + GPS, responds via audio ( "Got it. Pothole logged. Stay safe." ), and handles interruptions gracefully. No screen tapping needed. Voice Hazard Alerts: Proximity-based TTS warnings when approaching known hazards while driving — severity-aware, heading-aware, and speed-gated. Heatmap: Real-time severity-colored map of all hazards with drop-pin exploration. Gamification: Points system (submit +10, verify +5, endorse +2) with tier progression (Bronze → Diamond). For Municipal Officers (Next.js PMC Dashboard): Hazard Hotspot Map: Live Mapbox visualization with severity filtering, video evidence playback, and deep-link to report details. AI Chat (Gemini Function Calling): Officers ask natural-language questions — "Which areas have the most overdue potholes?" or "Generate report for ward 15" — and the AI autonomously selects from 11 BigQuery query tools to answer. The generate_ward_report tool is an AI sub-agent that queries BigQuery + Gemini to produce structured ward reports on demand. Area Response Leaderboard: Public accountability rankings by jurisdiction, tracking resolution rates against the Bombay HC 48-hour SLA mandate. Export: CSV and KML exports for GIS integration and offline analysis. Repair Verification: AI-powered before/after comparison using Gemini Vision to detect fraudulent repair claims. How we built it AI Pipeline (5-step classification + Dashboard Chat Agent): Classification — Gemini Vision analyzes video frames to classify hazard type and severity (1–5) Jurisdiction Routing — GPS-based deterministic routing to PMC/PCMC/PMRDA/Cantonment municipal boundaries Deduplication — BigQuery spatial query within 20m radius + Gemini LLM similarity comparison Weather Intelligence — Open-Meteo 48h rain forecast with severity multipliers (1.0×–2.0× based on flood risk) Dimension Estimation — Visual reference-based size estimation (length/width/depth in cm) and repair cost Additionally: Report Description Generation — Gemini generates human-readable descriptions from structured classification data Dashboard Chat Agent — Gemini with 11 BigQuery function-calling tools + agent-as-tool pattern for ward reports Commute Mode (Gemini Live API): Bidirectional real-time audio streaming via WebSocket Voice Activity Detection (VAD) with 800ms silence threshold for natural conversation flow Function calling for structured hazard report creation during live audio session Supports English, Hindi, and Marathi with language-specific system prompts 2–4 second response latency Infrastructure: Backend: Python FastAPI on Google Cloud Run (asia-south1) Frontend: Next.js 16 on Google Cloud Run Database: Google BigQuery (hazard reports, users, verifications) Storage: Google Cloud Storage (video evidence, thumbnails) Mobile: Flutter (Android) with Riverpod state management Infrastructure-as-Code: Terraform for all GCP resources CI/CD: Docker images pushed to Google Container Registry, deployed via gcloud run deploy Challenges we faced Gemini Live API latency: Initial voice response took 10–15 seconds. Reduced to 2–4 seconds by tuning VAD parameters (silence_duration from 1800ms → 800ms, prefix_padding at 300ms) and disabling dynamic thinking in the Live API config. Jurisdiction routing accuracy: GPS coordinates near municipal boundaries gave incorrect jurisdiction assignments. Solved with deterministic polygon-based routing instead of AI classification. Duplicate detection at scale: Simple distance-based matching caused false positives. Added Gemini LLM comparison of hazard descriptions + hazard type matching for precision. Weather severity calibration: Open-Meteo API occasionally returns stale data. Added fallback logic — pipeline continues with multiplier 1.0× if weather API fails. Monsoon data realism: Our team physically traveled across Pune to collect 24+ real field reports from actual road hazards (PCMC: Dapodi, Sangvi, Pimple Saudagar, Chinchwad; PMC: Aundh, Baner, Kothrud, Pashan). Every report in the system is from a real location — no synthetic or mock data. We drove through these areas on bikes and recorded hazards using both video capture and Commute Mode voice reporting. Accomplishments we're proud of Real data, real roads: Every report in the system is from actual road hazards in Pune — no synthetic or mock data Sub-4-second voice interaction: Gemini Live API responds naturally with function calling in real-time 5-step AI pipeline + chat agent: End-to-end automated hazard processing from video to actionable municipal intelligence Bombay HC compliance: The 48-hour SLA tracking directly addresses the October 2025 Bombay High Court mandate on pothole repair timelines Agent-as-tool pattern: Dashboard chat can invoke the ward report generator as a sub-agent, demonstrating composable agent architecture What we learned Gemini Live API's native audio capabilities are remarkably good at understanding Indian English accents and Hindi/Marathi mixed speech Voice Activity Detection tuning is critical for real-world driving conditions — default settings are designed for quiet environments BigQuery's serverless architecture handles the read-heavy pattern of a dashboard perfectly — no infrastructure management needed Real field data collection is irreplaceable — AI models behave very differently with actual monsoon road conditions vs. clean test videos What's next for NagarDrishti FCM push notifications when report status changes (backend implemented, mobile token registration pending) Multi-city expansion beyond Pune (Mumbai, Nagpur boundary data) Integration with PMC's existing grievance portal (SARATHI) for official status tracking Background sync improvements for low-connectivity areas (basic offline queue already implemented) Community verification rewards with blockchain-anchored proof <div