---
slug: "runconcierge-powered-by-neurun"
url: "https://devpost.com/software/runconcierge-powered-by-neurun"
title: "RunConcierge powered by Neurun"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 770
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# RunConcierge powered by Neurun

> RunConcierge AI connects runners preparing for race day with essential event details, route-specific/local knowledge, and product recommendations/tips from brands and local speciality stores.

[Devpost](https://devpost.com/software/runconcierge-powered-by-neurun) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]] [[supply_logistics]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** cloudsql, gemini, google-cloud, google-maps, javascript, linux, nextjs, postgresql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for runconcierge powered by neurun

## Body

Inspiration Building RunConcierge: Redefining the Way Runners Experience Races As lifelong runners, my team and I noticed a persistent problem: runners lack rich, contextual, and immersive tools to prepare for race event courses. The course is the centerpiece of any race event, yet most participants only see static maps and PDFs that fail to capture the reality of elevation changes, tight turns, aid station logistics, and where to expect cheering crowds. This gap often leaves participants, especially first-timers, feeling unprepared and anxious. We asked ourselves: What if runners could truly “experience” the course before race day, guided by an intelligent assistant that understands every detail of the race event, from the course layout, event logistics, and race-weekend activities to on-course activations and nearby sightseeing opportunities? By surfacing points of interest, local culture, and must-see landmarks along the route and in the surrounding area, participants could turn race preparation into a richer travel experience. And what if this same approach could later extend to other outdoor event verticals like cycling, triathlon, and hiking, transforming how participants prepare for and immerse themselves in any adventure? That vision inspired RunConcierge. What it does RunConcierge combines Google Maps’ Immersive View with Gemini-powered voice/text search to deliver a deeply interactive race experience. Runners can explore courses in full 3D, ask questions in natural language, and receive local race-specific guidance (route-specific and local knowledge). Key differentiators include: Conversational map interaction with course overlays. 3D visualization of routes, elevation profiles, and landmarks. Race-specific insights (e.g., aid station details, bathroom locations, historic weather patterns) Integration with major global race registration platforms for a seamless user experience. How we built it Our stack leverages the following Google technologies: Google Maps APIs for POI overlays, directions, and route data Geocoding GenCast for weather Soon "Maps Grounding" for incorporating data like user reviews of places. Immersive View for life-like 3D course exploration. Gemini voice/NLP for intuitive conversational search (Gemini live being implemented soon). Custom backend integrations to pull event metadata from race registration partners. We are also in the process of implementing dynamic overlays for highlighted route features, sponsor activations, and weekend itineraries. Challenges we ran into We faced significant hurdles in embedding RunConcierge into the runner’s journey from the moment they register for a race all the way through race day: Integrating race registration flows: Each platform had its own APIs, data structures, and user experiences. We built custom middleware to ensure RunConcierge appeared fully native and added value without disrupting the sign-up process. Building trust with race directors: Many were unsure how conversational AI tools could positively impact their events. We demonstrated value by showing how AI could answer participant questions, reduce support requests, and drive stronger engagement. We also trained directors to curate responses and upload complete race details, including accurate course routes. Standardizing data across thousands of events: Race details such as course maps, aid stations, and race-weekend logistics were often inconsistent or scattered. We developed processes and tools to centralize and continuously update this information so runners could rely on RunConcierge for everything they needed leading up to race day. Overcoming these challenges enabled us to deliver a product that feels like a natural part of a runner’s journey from registration through the start line. Accomplishments that we're proud of Many of the world’s major races are now coming onboard, recognizing RunConcierge as a valuable extension of their runner experience. In beta with over 20,000 initial users, runners consistently expressed how much they love having a single, interactive hub for all course and race-weekend information, driving significantly higher engagement compared to traditional static maps. Multi-million and multi-billion dollar brand partners across key categories such as fueling, hydration, recovery, performance, and hospitality are also integrating directly into the map experience, creating meaningful touch points with participants at the moments that matter most. This combination of event adoption, participant enthusiasm, and brand activation is firmly establishing RunConcierge as a new standard in the race ecosystem. What we learned Runners crave contextual insights, not just maps. Partnerships with race organizers are critical for data accuracy. Focusing on the course as the centerpiece deepens engagement with both participants and sponsors. What's next for RunConcierge powered by Neurun We’re expanding RunConcierge to support: Live race-day voice features, including real-time navigation and motivation. Crowd-sourced tips from fellow participants and spectators during the race and race weekend. Expansion to other recreation events, bringing immersive intelligent mapping to cycling, triathlon, and other event types. Over the next 6 months, we are leveraging the infrastructure we’ve built to roll these capabilities out across thousands of races across the globe through our global registration partners. <div