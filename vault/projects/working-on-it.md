---
slug: "working-on-it"
url: "https://devpost.com/software/working-on-it"
title: "Vectr"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 483
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Vectr

> We turn chaotic 911 calls into continuously updated, critical insights for EMS. By cutting fluff, paperwork, and cognitive load, we help crews arrive safer, faster, and less burned out.

[Devpost](https://devpost.com/software/working-on-it) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** bear-1, gemini, google-maps, python, react, trae.ai, wispr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Vectr "See the scene before you get there" Inspiration We are inspired by our friends who are EMTs. They've talked about the flaws in their navigation and dispatch systems. What it does Vectr is a comprehensive situational awareness tool designed specifically for Emergency Medical Services (EMS). It bridges the critical information gap between the initial dispatch call and arrival at the scene. Key features include: AI-Powered Intel: By combining Wispr and Bear-1 , the system listens to the dispatch audio and transcribes it, then uniquely uses Bear-1 to cut through the fluff that comes with voice transcripts and feed only the most vital information into Gemini AI , which generates actionable notes on everything the EMS team needs on the ground. Satellite & Interior Visualization: When dispatched, EMS responders receive a high-resolution satellite image of the destination. Uniquely, Vectr also attempts to guide responders through ideal entry points. Real-Time Caller Location: The system captures the GPS ping from the 911 caller’s phone and overlays it directly onto the satellite imagery, pinpointing the exact location of the accident—not just the street address. Automated Reporting: Throughout the situation and once the call is resolved, Gemini processes the event details to auto-generate the necessary medical and incident reports, drastically reducing paperwork time for EMTs. How we built it The core of the application was built using Trae AI , which allowed us to rapidly iterate on the interface and logic. Frontend/Navigation: We integrated dynamic mapping APIs to handle the satellite imagery and navigation routing. AI & Audio Processing: We utilized Wispr to handle real-time audio transcription and ingestion from the dispatch feed. Intelligence Layer: This data is piped into Bear-1 , which analyzes the context to extract specific location details (floor, room, entry obstacles) and Gemini summarizes them for the dashboard. Location Services: We implemented a GPS handshake protocol to visualize the caller's specific coordinates relative to the building footprint. Challenges we ran into Data Integration: Synchronizing the live GPS ping with static satellite imagery to ensure accuracy was difficult, as a margin of error of even a few meters matters in emergencies. Floor Plan Availability: Sourcing reliable data for interior floor plans is a complex problem; we had to design the UI to handle cases where blueprints might be incomplete or unavailable without breaking the user flow. Latency: Ensuring that the Wispr and Bear-1 processing happened in near real-time was critical. We had to optimize our API calls to ensure responders got the "scene notes" before they arrived. Accomplishments that we're proud of Successfully integrating the Wispr and Bear-1 pipeline to turn raw audio into structured, life-saving context. Instead of just using Bear-1 for AI prompts, we thought to use it to compress audio transcripts which are usually bloated with a lot of unecessary information. We tested it on several transcripts and it consistently saved the vital information and shaved off the rest. * <div