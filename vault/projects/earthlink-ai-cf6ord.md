---
slug: "earthlink-ai-cf6ord"
url: "https://devpost.com/software/earthlink-ai-cf6ord"
title: "EarthLink AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 713
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/media_journalism"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# EarthLink AI

> 🛰️ An AI agent that thinks in maps transforming raw Sentinel-2 satellite data into live, explainable geospatial decisions from a single natural language prompt.

[Devpost](https://devpost.com/software/earthlink-ai-cf6ord) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[climate_energy]] [[disaster_emergency]] [[media_journalism]]
  <sub>weak: developer_tools</sub>
**user** [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** fastapi, geojson-spatial-grids, google-earth-engine-(scalable-architecture-design), google-gemini-(via-vercel-ai-sdk), google-generative-ai-api, harmonized-sentinel-2-level-2a-satellite-data, mapbox-api, mapbox-gl-(react-map-gl), next.js-16, python, react, recharts, tambo, tambo-ai-(agent-tools-+living-ui)

## How they structured the write-up

- the inspiration
- what we built
- 🛰️ the intelligence behind it
- how we built it
- challenges we faced
- what we learned
- 🌎 why this project deserves to win
- the vision
- 🛰️ earthlink ai

## Body

🌍 EarthLink AI The Inspiration Satellite imagery is one of humanity’s most powerful open resources. Through platforms like Google Earth Engine, we can access planet-scale environmental intelligence vegetation health, urban heat, built-up intensity, terrain structure updated continuously from space. Yet using it requires deep technical knowledge: Understanding spectral bands (B2, B3, B4, B8…) Performing atmospheric correction and cloud masking Writing band math expressions Running spatial joins and reducers This complexity keeps environmental intelligence in the hands of experts. We asked: What if satellite data could be explored the way we explore Google Maps just by asking questions? That question became EarthLink AI . What We Built EarthLink AI is an agentic geospatial intelligence system that converts natural language into real satellite-driven map actions. Instead of writing code, users can say: “Find the 3 hottest and 3 greenest areas near downtown and compare them.” And the system: Searches locations Performs spatial filtering Computes environmental metrics Updates the map Renders comparisons Explains the results All in a single conversational flow. The LLM doesn’t describe the map. It acts on it . 🛰️ The Intelligence Behind It Using Harmonized Sentinel-2 Level-2A surface reflectance data, we derive environmental metrics such as: NDVI (vegetation health) NDBI (built-up intensity) LST (land surface temperature) Fog Score Disaster Elevation Bare Soil Index etc These allow users to: Identify urban heat islands Compare environmental equity between neighborhoods Discover greener or cooler regions Analyze vegetation change over time We are not building a chatbot. We are building an AI environmental analyst . How We Built It 1️⃣ Agent-First Architecture The core innovation is that the agent loop is the product . Using an agentic tool system: The model selects tools dynamically Tools mutate real map state UI components render structured outputs Multi-step workflows persist context This enables: Stateful reasoning Multi-step chaining Real product behavior Map and sidebar synchronization The system behaves like software — not a chat demo. 2️⃣ Geospatial Data Pipeline Data source: Harmonized Sentinel-2 MSI Level-2A (Surface Reflectance) 13 spectral bands 10–60m resolution Precomputed GeoJSON grid for the MVP (San Francisco Bay Area) The architecture is designed to plug directly into live Google Earth Engine pipelines at scale. For the hackathon, we prioritized: Proving the agent intelligence over expanding geography. 3️⃣ Full-Stack Implementation Frontend Next.js Mapbox GL Dynamic visualization components Agent-controlled UI rendering Backend FastAPI GeoJSON spatial querying Metric aggregation Region & proximity analysis Tool-driven APIs The architecture is modular — any region with compatible GeoJSON can be integrated. Challenges We Faced Making the Agent Truly Agentic The hardest problem wasn’t maps — it was decision logic. We had to ensure the model: Doesn’t re-plot unnecessarily Preserves multi-step state Chains tools correctly Handles append logic Labels selectively (e.g., top 3 only) We encoded behavioral constraints directly into tool contracts and system logic. This transformed the model from a text generator into a structured decision engine. Translating Human Language into Spatial Logic Users think in: “Near the Marina” “Within walking distance” “Cooler than average” The system must translate that into: Radius buffers Threshold filters Metric comparisons Bounding boxes Bridging fuzzy language with strict geospatial computation was one of our biggest engineering challenges. Making Insights Explainable Raw metrics are not enough. We built structured, renderable components for: Comparisons Insight summaries Region aggregates Temporal trend charts Key takeaways The result isn’t just visualization — it’s interpretation. What We Learned Agent design is a product discipline. Tool constraints matter more than prompt cleverness. Maps combined with LLMs create a new UX category. Environmental data becomes powerful only when accessible. We realized something bigger: The future of geospatial interfaces is conversational. 🌎 Why This Project Deserves to Win EarthLink AI is: A working multi-step geospatial agent A real environmental intelligence tool A scalable architecture ready for Earth Engine integration A new interaction paradigm for satellite data It transforms raw spectral reflectance into actionable decisions. Most people will never write Earth Engine scripts. But everyone can ask: “Is my neighborhood getting hotter?” EarthLink AI makes that question answerable. The Vision We envision a future where: City planners simulate climate resilience in seconds Journalists explore environmental inequality live Communities advocate using satellite-backed evidence Anyone can interrogate planetary data All through natural language. 🛰️ EarthLink AI Turning raw satellite reflectance into insight — one prompt at a time. <div