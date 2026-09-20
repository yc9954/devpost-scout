---
slug: "caltrack-i0pq3n"
url: "https://devpost.com/software/caltrack-i0pq3n"
title: "CalTrack"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 701
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/geospatial"
---

# CalTrack

> Using mass surveillance to keep people safe - predicting impact, affected areas, and coordinating faster emergency response in disasters.

[Devpost](https://devpost.com/software/caltrack-i0pq3n) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]]
**domain** [[disaster_emergency]] [[health_clinical]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[geospatial]]

**stack** docker, earth2studio, fastapi, nvidia, python, pytorch, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for caltrack

## Body

CalTrack Inspiration Disaster response today is fragmented. While emergency managers prepare evacuation and fire rescue plans, they often lack a unified system driven by real-time updates from 911 operators and population density signals to coordinate operational decisions effectively. We were influenced by recent research ( https://arxiv.org/abs/2405.14975 ), which demonstrates how large-scale Apple Wi-Fi Positioning System (WPS) datasets can reveal infrastructure disruptions and population movement patterns over time. The paper highlights both the power and the privacy risks of connectivity-derived signals. This research shows that WPS signals can be used to infer device locations on a network, and that any system leveraging such signals must operate at an aggregated, privacy-conscious level. CalTrack applies these ideas ethically, focusing on community-level resilience modeling, not individual tracking. What it does CalTrack is a disaster intelligence platform focused on forest fires in California. Our platform: Visualizes population density using aggregated WPS device signals Overlays real-time and predictive fire risk across geographic regions Provides data-driven recommendations for allocating emergency resources Keeps human operators in the loop with AI-assisted data extraction, including addresses, medical conditions, and triage levels Spins up an AI voice call center for emergency triage and coordination when demand exceeds available operators Instead of asking “Who is affected?” , CalTrack answers: Where should resources go first, and why? How we built it We utilized the WPS API to retrieve aggregated location data for devices on the network. A majority of these devices are mobile devices such as phones and tablets. We use this data to estimate population density and provide critical situational awareness to emergency responders. We deployed NVIDIA’s DGX Spark systems to host NVIDIA open models, including the Nemotron-class Personaplex model and Earth-2. Our fire-risk overlay is powered by NVIDIA Earth-2, which provides predictive weather patterns that indicate conditions conducive to forest fires. For our demo, we mapped historical data over Palo Alto to demonstrate how predictive modeling enhances situational awareness. Our original plan was to power the AI voice 911 operator using the Personaplex model for natural, fluid emergency communication. However, due to onboarding and troubleshooting challenges with the DGX Spark systems in collaboration with NVIDIA and ASUS representatives, we prioritized successfully deploying Earth-2 within the 36-hour hackathon window. As a result, we integrated VAPI ( https://vapi.ai/ ) for voice orchestration to meet our deadline. To deliver a data-driven experience for operators, we utilized CrewAI, an agent mesh framework that orchestrates specialized agents with defined tasks. During a 911 phone call, our agent mesh parses the conversation in real time and extracts critical information: Healthcare agents gather patient conditions and triage levels so ambulatory services and hospitals can prepare for surges. Geolocation agents , powered by HERE API, extract address information from the call and place a notification marker directly on the operator’s map interface. Together, these agents provide operators with structured, actionable intelligence to improve emergency response coordination. Challenges we ran into Serializing and deserializing Protobuf headers for the WPS location system Onboarding and configuring NVIDIA DGX Spark systems within a tight timeframe Collaborating with NVIDIA and other participants during a productive Saturday feedback session to troubleshoot deployment issues Parsing and validating spoken address data from live 911-style phone calls Accomplishments that we're proud of Mapped 650,000 network devices within 6 hours, covering the greater Palo Alto region Integrated predictive disaster modeling using weather patterns associated with forest fire risk Prototyped a voice-based 911 operator integrated with an agentic framework that extracts critical details in real time Designed a system that balances AI automation with human-in-the-loop oversight during high-demand emergency scenarios What we learned Connectivity and infrastructure-derived signals are powerful tools in emergency contexts Research like https://arxiv.org/abs/2405.14975 highlights both the opportunity and responsibility associated with infrastructure-derived data Emergency AI systems must be transparent, auditable, and privacy-conscious Ethical system design strengthens both real-world impact and public trust What's next for CalTrack Add predictive outage modeling for electricity, blocked roads, and terrain accessibility Expand from single-county to statewide deployment Integrate hospital capacity and supply chain stress indicators by interfacing with healthcare systems Deploy a hardened multi-agent orchestration framework for production environments Build a public-facing transparency and accountability dashboard Long term, CalTrack can generalize globally wherever public alerting systems and infrastructure data feeds exist. <div