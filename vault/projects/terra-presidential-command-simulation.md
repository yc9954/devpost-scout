---
slug: "terra-presidential-command-simulation"
url: "https://devpost.com/software/terra-presidential-command-simulation"
title: "TERRA: Presidential Command Simulation"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 913
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/disaster_emergency"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# TERRA: Presidential Command Simulation

> A real-time geopolitical strategy game where you play as the President of the United States. Make decisions on live world events, manage factions, and shape history.

[Devpost](https://devpost.com/software/terra-presidential-command-simulation) · hackathon [[Build with MeDo Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[disaster_emergency]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** api, cartodb, css3, html5, ibm, javascript, leaflet.js, medo, mono, news, openstreetmap, plex, plugin, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for terra: presidential command simulation

## Body

Inspiration The news cycle is overwhelming. Every day there are wars, economic crises, diplomatic standoffs, and humanitarian disasters but they all feel abstract and distant. We wanted to build something that made geopolitics feel real and personal . We were inspired by the idea of sitting in the Situation Room at the White House, surrounded by live intelligence feeds, satellite maps, advisors pulling you in different directions, and a clock ticking. What if someone could actually experience that pressure? What decisions would you make? How long would you survive? We also drew inspiration from games like Suzerain and Democracy 4 , which proved that governance simulators could be deeply engaging. We wanted to go further by grounding ours in real, live news instead of fictional scenarios. What it does TERRA is a real-time geopolitical strategy game where you play as the President of the United States. Every turn, real-world news headlines are pulled into the game as classified intelligence briefings, and you must respond using the tools of statecraft. Key Features: Live satellite map as the game board - click any crisis event and the map cinematically flies to that exact location on Earth Contextual Live Intelligence Feed - a matched YouTube Live stream (Al Jazeera, Bloomberg, NHK World, DW News) automatically appears on the map as a floating popup when you select an event Real news, real missions - The News plugin pulls live headlines every hour and converts them into actionable crisis briefings Full governance engine - budget allocation sliders, 8 political factions with satisfaction meters, presidential schedule, ideology compass, cabinet management, and an election countdown with a game-over screen Consequence chains - every decision generates a classified consequence assessment and ripples through the global simulation Intelligence Report - each crisis comes with a threat assessment, situation briefing, and recommended actions How we built it TERRA was built entirely through multi-turn conversations with MeDo , no manual coding. The stack MeDo generated: Leaflet.js for the interactive satellite map with overlay tabs (GDP, Tension, Approval, Development, Relations) The News plugin for live headline ingestion and mission generation YouTube iframe embeds mapped by a region and event-type lookup table for contextual news streams A hardcoded centroid-based circle system for country data overlays, bypassing unreliable GeoJSON fetches IBM Plex Mono + Orbitron for the tactical War Room typography A React component architecture for all modals, panels, and game state management The MeDo conversation approach: We used a highly modular prompting strategy, building the visual foundation first (the dark satellite UI), then layering in individual game systems one at a time (budget, factions, ideology compass, events engine), then integrating the live news and video feeds last. Each prompt targeted a single system without breaking what was already working. Challenges we ran into 1. Map data reliability GeoJSON country boundaries required property-name matching that kept failing silently. We solved this by switching to a centroid-based L.circle marker system with hardcoded lat/lng coordinates for every country. 2. Event location accuracy Live news events from The News plugin had no geographic coordinates. We built a getNewsEventLocation() keyword scanner with 60+ geographic patterns that extracts coordinates from headlines in real time. 3. React hooks violations DOM manipulation injected into React render cycles caused "Rendered more hooks than previous render" crashes. We resolved this by passing all dynamic content through state rather than direct DOM access. 4. YouTube channel matching Without a YouTube Data API key, dynamic search was not possible. We built a direct EVENT_CHANNEL_MAP lookup table keyed by event ID, and a region + type fallback matrix covering all major news channels. 5. Keeping systems from breaking each other With 15+ interconnected systems, every new feature risked cascading failures. We learned to isolate each fix with surgical prompting and explicit instructions to MeDo about which components to leave untouched. Accomplishments that we're proud of Building a fully playable geopolitical strategy game with zero code written manually The live news to satellite map to YouTube popup flow: clicking a crisis in Kashmir and watching the map fly there while NHK World appears as a floating stream on the map is genuinely cinematic A consequence assessment engine that generates narrative intelligence reports from the intersection of your action type and the event type A world where real events become your gameplay , updating as the world changes A UI that looks genuinely premium , a dark tactical aesthetic that rivals commercial games What we learned MeDo excels at generating complex, interconnected systems when you give it precise, modular instructions. Vague prompts produce vague results. Isolating fixes is critical: always tell MeDo exactly which components to leave untouched. The best features come from thinking about what the experience should feel like first, then engineering backward. The YouTube-on-map idea started as a UI feeling ("like a war room TV") not a technical spec. Real-time data integration transforms a simulation into something that feels alive . What's next for TERRA: Presidential Command Simulation Multiplayer - two players as rival nations competing on the global map simultaneously Full election campaign mode - manage polls, run ads, and debate your opponent across swing states Historical scenarios - play the Cuban Missile Crisis, the 2008 Financial Crisis, or the COVID-19 response with real constraints from that era AI-powered advisors - your Secretary of State and Defense Secretary give conflicting advice before every decision, powered by MeDo's AI capabilities Mobile responsive layout - optimized for tablet use so it feels like an actual command briefing tablet <div