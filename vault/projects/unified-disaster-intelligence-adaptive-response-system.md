---
slug: "unified-disaster-intelligence-adaptive-response-system"
url: "https://devpost.com/software/unified-disaster-intelligence-adaptive-response-system"
title: "Unified Disaster Intelligence & Adaptive Response System"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 1142
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Unified Disaster Intelligence & Adaptive Response System

> UDIARS unifies flood, wildfire, and earthquake intelligence into one live map that shows you real-time disaster risk and computes evacuation routes with voice navigation.

[Devpost](https://devpost.com/software/unified-disaster-intelligence-adaptive-response-system) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[developer_tools]] [[disaster_emergency]] [[health_clinical]] [[housing_homeless]] [[labor_employment]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** css3, gemini, geojson, html5, javascript, komoot, leaflet.js, netlify, node.js, nws, osrm, photon, usgs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for udiars

## Body

Default Page - Unified View for California Report a Hazard Emergency Help How Udiars Works Demo Mode - Historical Flood in New Jersey Demo Mode - Automatic Safe Evacuation Route in New York Inspiration Disasters do not arrive one at a time, but the tools we use to survive them are built as if they do. There is one app for weather alerts, a different site for earthquake feeds, and a separate map for traffic, and none of them talk to each other. During an actual emergency, when seconds matter and cell networks are strained, the last thing a family should be doing is juggling five tabs to figure out whether the road they are about to drive down is safe. We wanted a single screen that answers the only question that matters in a crisis: where is the danger, and how do I get away from it right now. That question became UDIARS, a Unified Disaster Intelligence and Adaptive Response System. What it does UDIARS pulls live data from three authoritative government feeds and turns it into a single, color-coded risk picture for a region. The National Weather Service feed drives flood and wildfire scoring, and the USGS earthquake catalog drives seismic scoring. Each hazard gets a transparent, rule-based risk percentage with plain-language reasoning attached, so a user can see not just that flood risk is at sixty percent but exactly why, which active alert or forecast signal pushed it there. From there the app becomes an evacuation tool. A user sets a starting point, by typing an address with autocomplete or tapping their live GPS location, and chooses a destination or a pre-loaded safety zone such as a community center or hospital. UDIARS calls a live road-network routing engine and returns up to three distinct routes, ranked, with the primary route favored to steer around known hazard zones. The selected route renders on the map and feeds a turn-by-turn navigation panel with spoken voice guidance, so a driver can keep their eyes on the road. The app adapts to who is using it through three operational tiers. A civilian sees one clear route and a short safety checklist. A first responder sees every computed route with a hazard-exposure score and a list of nearby shelters and hospitals. An emergency manager sees the full regional overlay and a simulated personnel-dispatch console for coordinating zones. There is also a community hazard-reporting feature, a built-in hotlines directory tailored to each state, and a Demo mode that replays real historical disasters like the Camp Fire and the Tubbs Fire so the system can be evaluated against known events. Tying it all together is the UDIARS AI Assistant, a chat helper grounded in the app's live state that can answer questions like "is my route safe" or "what should I do right now." How we built it The entire application is a single self-contained HTML file with vanilla JavaScript, which keeps it fast, portable, and dependency-light. Leaflet renders the interactive map and hazard overlays. Live risk comes from direct browser calls to the National Weather Service API for forecasts and active alerts and to the USGS earthquake API for recent seismicity, both filtered to per-state bounding boxes. Routing is handled by the OSRM road-network engine, with a haversine straight-line estimate as a graceful fallback if the service is unreachable. Address search uses the Photon geocoder for autocomplete, and turn-by-turn voice guidance uses the browser's built-in Web Speech API so there is no external dependency for audio. The risk engine is deliberately rule-based rather than a black box. Each hazard score is computed from explicit, inspectable signals, the count and type of active alerts, mentions of heavy rain or red-flag fire weather in the forecast, and the number and magnitude of recent quakes, so every number in the interface can be traced back to its source. The AI Assistant runs through a serverless function so the API key never touches the client, and that function builds a grounded prompt from the app's current mode, region, live risk levels, and any route the user has computed. The whole thing deploys to Netlify as static files plus one function, which means it can go live in under a minute with no server to maintain. Challenges we ran into Keeping the AI honest was harder than getting it to respond. An assistant that confidently invents the current weather is worse than no assistant at all, so we engineered the prompt to speak only in terms of the risk levels the app already computed and to defer to official 911 and local emergency management for anything urgent. Securing the API key was a second challenge solved by moving every model call behind a serverless proxy rather than exposing it in the HTML. Routing reliability was a third, since public routing and geocoding services can rate-limit or fail, so we built fallbacks at every external call: a straight-line estimate when routing is down, background risk levels when a feed is unavailable, and default safety-zone suggestions when geocoding returns nothing. Finally, fitting a desktop emergency-operations dashboard and a one-handed mobile evacuation tool into the same codebase took a genuinely responsive layout, including a draggable bottom sheet on mobile that relocates the same controls into a thumb-friendly form. Accomplishments that we're proud of We built a disaster tool that runs entirely on real, live, authoritative data rather than mockups, and every risk number in it is explainable down to the feed it came from. We are proud that it degrades gracefully instead of breaking when a service hiccups, that it serves three genuinely different user roles from one interface, and that the AI assistant is grounded enough to be trustworthy in exactly the moment when bad information is most dangerous. And we shipped all of it as a single deployable file that anyone can stand up for free. What we learned We learned that in safety-critical software, transparency beats sophistication. A simple rule-based risk score that a user can verify is more valuable than a complex model they have to trust blindly. We learned how to chain real government APIs together and design for their failure modes rather than their happy path. And we learned a lot about grounding language models, that the right move is to feed the model verified state and explicitly forbid it from inventing facts, rather than hoping it behaves. What's next for UDIARS Next we want to persist community hazard reports beyond a single session so neighbors can build a shared real-time picture, add live wildfire-perimeter and flood-gauge feeds for true hazard-avoidance routing rather than illustrative scoring, push critical alerts through service workers so they arrive even when the app is closed, and expand coverage from three states to nationwide with multilingual support so the people most often left behind in disasters are the first ones reached. <div