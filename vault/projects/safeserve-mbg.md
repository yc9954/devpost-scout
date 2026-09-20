---
slug: "safeserve-mbg"
url: "https://devpost.com/software/safeserve-mbg"
title: "SafeServe MBG"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 709
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# SafeServe MBG

> The unified AI command center for the Makan Bergizi Gratis program. Real-time oversight for 83 million beneficiaries.

[Devpost](https://devpost.com/software/safeserve-mbg) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[civic_government]] [[education]] [[health_clinical]] [[supply_logistics]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** gemini, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safeserve mbg

## Body

About SafeServe MBG Inspiration "No child should ever have to trade their health for a meal." The inspiration for SafeServe MBG was born from a place of urgency and deep concern. As Indonesia embarks on the historic Makan Bergizi Gratis (MBG) program to nourish 83 million children, a darker reality has emerged: headline after headline reporting hundreds of students hospitalized due to food poisoning in regions like Tasikmalaya, Cianjur, and beyond. While the program is a beacon of hope for building the "Golden Generation 2045," the current reliance on manual, reactive supervision has proven fatal. We realized that for a parent, the joy of a free meal is quickly replaced by the terror of a phone call from the school clinic. We built SafeServe to be the Digital Shield that was missing—a system that moves beyond paperwork to provide real-time, uncompromising oversight. We believe that "Free" must never be an excuse for "Unsafe," and that technology is the only way to ensure every lunchbox served is a promise of health, not a hidden hazard. What it does SafeServe MBG is a unified intelligence platform that connects the entire food safety loop: For Regulators : Provides a national "Command Center" with AI-driven outbreak prediction, regional risk heatmaps, and deep "Reasoning Chains" that explain the logic behind vendor risk scores. For Vendors : Offers a portal for digital transformation, including AI-powered multimodal hygiene audits (vision), staff wellness tracking, and blockchain-verified supply chain traceability. For Schools : Empowers admins with SOS symptom reporting (linked to AI clinical triage), shipment verification, and nutritional compliance monitoring. For Sustainability Officers : Implements an "Active Governance" loop to reduce food waste through AI-suggested portion calibrations and district-level consumption analysis. How we built it The platform is built on a high-performance frontend stack designed for mission-critical reliability: Core : React 19 and TypeScript for a robust, type-safe architecture. Intelligence : Integrated the Google Gemini API ( gemini-3-flash-preview and gemini-3-pro-preview ) for multimodal vision analysis, text-based triage, and complex reasoning. Grounding : Utilized Google Search Grounding to inject real-time regional news and stability data into our risk models. UI/UX : Tailored with Tailwind CSS 4 and Lucide React , focusing on a "Command Center" aesthetic that remains accessible for local school staff and UMKM owners. Data Viz : Leveraged Recharts for real-time telemetry from IoT cold-chain simulators and waste benchmarking. Challenges we ran into AI Explainability : One of the biggest hurdles was ensuring the AI didn't just give a "Risk Score" but could explain why in a way a regulator could trust. We solved this using Gemini's reasoning capabilities and structured output. Multimodal Integration : Designing a system that could handle both real-time IoT sensor data and image-based hygiene audits required careful state management and resilient API handling (implementing circuit breakers for quota management). User Diversity : Designing a single ecosystem that caters to high-level government officials and hyper-local catering staff required a deep focus on intuitive UX and clear action-oriented design. Accomplishments that we're proud of Unified Safety Loop : Successfully creating a "Single Pane of Glass" where a report at a school in Jakarta can immediately update the risk profile of a vendor and alert a national regulator. AI Triage Accuracy : Developing a clinical triage system that maps reported symptoms to potential pathogens and provides immediate safety protocols. Simulation Mode : Building a fully functional "Outbreak Simulator" that allows officials to test their response systems in a "war-room" style environment. What we learned Building SafeServe MBG taught us the immense value of Grounding AI . Without real-world context (via Google Search), a safety model is just a calculator. With it, it becomes an intelligent partner. We also learned that in mission-critical applications, "Trust" is the most important feature—which is why every AI decision in SafeServe is backed by evidence chains and integrity hashes. What's next for SafeServe MBG Real-time Video Audits : Moving beyond static photos to live-streaming kitchen analysis using Gemini's Video capabilities. IoT Hardware Integration : Moving from simulated telemetry to real-world sensors in delivery trucks. Local Language Support : Enhancing the AI Assistant to support regional Indonesian dialects for broader inclusivity among UMKM vendors. Predictive Procurement : Using consumption data to help vendors pre-order ingredients, further reducing waste and costs. <div