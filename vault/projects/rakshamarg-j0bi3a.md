---
slug: "rakshamarg-j0bi3a"
url: "https://devpost.com/software/rakshamarg-j0bi3a"
title: "RakshaMarg"
hackathon: "AI for Bharat 2026"
organization: "student"
winner: true
words: 400
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "substrate/geospatial"
---

# RakshaMarg

> "Navigate the Night with Intelligence."

[Devpost](https://devpost.com/software/rakshamarg-j0bi3a) · hackathon [[AI for Bharat 2026]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**substrate** [[geospatial]]

**stack** fastify, gemini, google-directions, google-maps, gsap, node.js, react, three.js, typescript, vercel, vite, vps

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rakshamarg

## Body

landing page Enter source and destinations risk analysis report Inspiration Standard navigation apps prioritize speed , often sending users through dark, unsafe shortcuts. RakshaMarg was born to be a "street-smart" companion—answering the need for logic that asks not just "Which way is fastest?" but "Which way is safest?" What it does Safety Scoring : Assigns a 0-100 "Safety Score" to routes based on lighting, crime data, and crowd density. Smart Routing : Suggests Safety Corridors (well-lit main roads) over faster but riskier alleys. Time-Aware Risk : Dynamically adjusts safety scores based on the time of day (e.g., higher risk post-10 PM). Safety Tools : Features Live Tracking for trusted contacts, a one-tap SOS button , and highlights nearby Safe Havens (hospitals, police stations). How we built it Frontend : Built with React + TypeScript and Vite ; utilized Three.js for the immersive 3D landing page. Mapping : Leveraged Google Maps Platform (Directions & Maps API) for core routing. The Brain : A custom Node.js + Fastify backend algorithm that analyzes route segments (0.5km chunks) against historical crime data. We used a logarithmic penalty system weighted by time-of-day to calculate risk. AI : Integrated Gemini API to process and categorize unstructured safety reports. Challenges we ran into Defining "Safe" : Balancing objective data (lights/crime) with subjective factors to create a fair scoring algorithm was difficult. Spatial Performance : Efficiently querying thousands of incident points against a dynamic route without causing server lag required complex optimization (spatial "chunking"). 3D Rendering : Optimizing the Three.js map to run smoothly on standard browsers. Accomplishments that we're proud of The Algorithm : Successfully turning complex crime stats into a simple, understandable Safety Score . Dark Mode UX : Designing a purposeful, low-light interface that helps users maintain night vision. Real-Time Speed : Achieving millisecond-level analysis so safety checks don't slow down navigation. What we learned Spatial Indexing : Direct distance checks are too slow; bounding boxes are essential for scalable geospatial queries. Transparency Builds Trust : Users need to know why a route is red (e.g., "Poor Lighting"), not just that it is. Google Maps Depth : We mastered decoding complex polyline data to perform server-side analysis. What's next for RakshaMarg Crowdsourcing : Adding Waze-style real-time reporting for broken lights or suspicious activity. WearOS App : Haptic (vibration) navigation for discreet, hands-free guidance. Offline Mode : Saving "safe corridors" for navigation in low-network areas. <div