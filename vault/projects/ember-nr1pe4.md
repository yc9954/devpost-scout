---
slug: "ember-nr1pe4"
url: "https://devpost.com/software/ember-nr1pe4"
title: "Ember"
hackathon: "Pixel Forge AI Hackathon ($18,000+ in Prizes)"
organization: "Pixel Forge"
winner: true
words: 348
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Ember

> Type your address. Get a grounded wildfire risk brief, a defensible-space checklist, and an escape route, all from live NASA, NOAA, and Cal Fire data.

[Devpost](https://devpost.com/software/ember-nr1pe4) · hackathon [[Pixel Forge AI Hackathon -18-000- in Prizes-]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[disaster_emergency]]
  <sub>weak: transportation</sub>
**substrate** [[financial_record]] [[geospatial]]

**stack** ai, cursor, detection, fastapi, fire, firms, openrouter, openrouteservice, openrouteserviceapi, railway, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ember

## Body

home page data accumulated escape route personalized checklist Inspiration Data about wildfires in California is openly available but scattered across different sources – NASA hotspot locations, Cal Fire zones, NOAA alert systems, defensible space guidelines, etc. Most people residing in fire-prone regions do not know their parcel’s true hazard rating. We aimed at creating one personalized solution. What it does Input your home address. Ember fetches live NASA FIRMS hotspots, NOAA weather and alerts, and Cal Fire incident and hazard zone data, provides a synthesized risk briefing, builds a checklist based on real Cal Fire guidelines, and shows a road-based evacuation route from the nearest active fire. How we built it A FastAPI backend fetches geodata in parallel, searches for the relevant Cal Fire guidelines by hazard zone, and runs it through Claude: first synthesizing the brief, then generating a checklist, and finally checking each statement in it against the retrieved text. A React/Leaflet frontend, OpenRouteService for routing. Challenges we ran into Maintaining the truthfulness of the AI was our key challenge – without the grounds, it would invent specific information about defensible spaces without any doubt. Creating retrieval and verification helped us overcome that problem. We replaced the unreliable public OSRM router for OpenRouteService midway through building our application. Accomplishments that we're proud of Implementing a generate and verify pipeline in less than a week as opposed to only generating from prompts. The escape route functionality, bearing computation, snapped routing, and live rendering of the route all worked in one sitting in an end-to-end way with real addresses. What we learned LLMs will boldly make up facts if you let them, and grounding and verification aren't nice-to-haves but rather the whole point of the process. We also learned how to combine several formats of inconsistent geodata provided by different governmental sources. What's next for Ember Actual Cal Fire Fire Hazard Severity Zone polygons as opposed to circles based off of distance, live updates with push notifications as the fire progresses, expansion to other states, and routing to multiple destinations that account for road closures during evacuation. <div