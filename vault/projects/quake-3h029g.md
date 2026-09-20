---
slug: "quake-3h029g"
url: "https://devpost.com/software/quake-3h029g"
title: "Quake"
hackathon: "MEGA Hackathon 2025"
organization: "MegaHackathonLeague"
winner: true
words: 950
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/housing_homeless"
  - "domain/supply_logistics"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Quake

> 🆘 Using geospatial data and real-world risk factors, Quake helps people escape safely after an earthquake.

[Devpost](https://devpost.com/software/quake-3h029g) · hackathon [[MEGA Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]] [[climate_energy]] [[disaster_emergency]] [[housing_homeless]] [[supply_logistics]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** flask, geopandas, google-maps, google-places, javascript, networkx, numpy, osmnx, pandas, python, scipy

## How they structured the write-up

- "because the fastest route isn’t always the safest."
- 🌍 inspiration
- 🛠 what it does
- 🔬 how it was built
- ⚠️ challenges overcome
- 🚀 what’s next for quake?
- why this matters
- final thoughts

## Body

Because the fastest route isn't always the safest. Why Quake? Quake vs. Traditional Navigation Data Processing & Risk Factors Future Scope of Quake Assigning Risk Scores to Roads Risk-Aware Routing in Action Risk-Optimized Routing Using Pre-Processed Data Shelter Suggestions along the Route Seamless Map Experience 🆘 Quake – Smart Evacuation Routing "Because the fastest route isn’t always the safest." 🌍 Inspiration Earthquakes are among the most devastating natural disasters, capable of causing widespread destruction and loss of life. California alone experiences over 10,000 earthquakes annually , with major metropolitan areas like San Francisco at constant risk due to their location on fault lines. Traditional navigation tools focus solely on speed , guiding users through the fastest routes, which may not be the safest during an emergency. Roads may be blocked, infrastructure may collapse, and people may need secure shelters rather than just an endpoint. Quake was developed to address this critical gap by providing safe route navigation that considers real-world risk factors in the aftermath of an earthquake. This project also aligns with the United Nations' Sustainable Development Goals (SDGs) by contributing to: ✔️ Goal 9: Industry, Innovation, and Infrastructure – Enhancing disaster resilience in urban areas ✔️ Goal 11: Sustainable Cities and Communities – Providing a safer navigation system for earthquake-prone cities ✔️ Goal 13: Climate Action – Leveraging technology to mitigate natural disaster risks With increasing urbanization and climate change-related disasters, solutions like Quake will play a crucial role in disaster preparedness and response. 🛠 What It Does Quake maps out the safest possible route between two points in the aftermath of an earthquake. Unlike conventional navigation tools, which prioritize speed, Quake optimizes routes based on multiple risk factors , such as: ✅ Road conditions – Avoiding blocked or high-risk routes ✅ Building density – Identifying roads with lower collapse risks ✅ Proximity to emergency shelters – Suggesting the nearest safe locations Key functionalities include: 🔹 Enter a location and destination 🔹 Receive an optimized safe route 🔹 View nearby emergency shelters and choose an alternative destination 🔹 Automatically adjust routes to safer locations when necessary Safety takes priority over speed , ensuring that users reach safety without unnecessary exposure to hazards. 🔬 How It Was Built Building Quake required a combination of geospatial data processing, risk analysis, and smart navigation algorithms. The system was structured into three core stages: 📊 Pre-Processing: Risk Factor Analysis Before real-time routing could be implemented, an extensive pre-analysis of city infrastructure was conducted. The goal was to assign risk scores to each road segment to influence navigation decisions. Risk factors were derived from: OSMnx (OpenStreetMap) – Providing real-world street networks Geospatial datasets – Analyzing road types, building density, and open spaces Government hazard maps – Identifying earthquake-prone areas Each road segment was assigned a combined risk score , factoring in proximity to buildings, road type, and width. These scores were then integrated into the navigation system to influence route selection dynamically. 🗺 Mapping & Route Calculation With risk analysis completed, the system was designed to efficiently compute safe routes. The core components include: ✔️ A* search algorithm – Modified to prioritize both distance and safety ✔️ Shelter integration – Identifies nearby safe locations dynamically ✔️ Interactive UI – Allows users to enter locations, receive routes, and select alternative safe zones The system was designed to be scalable , ensuring that additional data sources (such as real-time hazard reports) can be integrated in the future. ⚠️ Challenges Overcome Developing Quake required overcoming several technical and logistical challenges: 1️⃣ Pre-processing massive geospatial datasets Assigning risk scores to every road and intersection required extensive data wrangling and optimization to ensure fast computations. 2️⃣ Building a routing algorithm that prioritizes safety Unlike conventional navigation tools, Quake required a unique weighting system to balance risk and distance, ensuring users avoid high-risk areas while still reaching their destination efficiently. 3️⃣ Balancing speed and complexity The initial integration of heatmaps slowed down the system, leading to a focus on pre-processed risk data instead of real-time rendering to optimize performance. These challenges were addressed through iterative improvements, ensuring Quake remains reliable, fast, and effective in emergency situations. 🚀 What’s Next for Quake? The foundation for Quake is in place, but several key expansions are planned: 🔹 Integration of real-time hazard updates – Incorporating live earthquake reports and damage assessments to dynamically update routes. 🔹 Expanded geographic coverage – Extending safe route navigation to other seismic hotspots like Los Angeles, Tokyo, and Istanbul. 🔹 Crowdsourced emergency reports – Allowing users to report blocked roads, collapsed buildings, and hazards in real time. 🔹 Collaboration with governments & disaster response teams – Partnering with emergency services to integrate official alerts and ensure better coordination during evacuations. 🔹 Dynamic Risk Computation – Moving from pre-processed risk factors to real-time analysis based on live sensor data, weather conditions, and emergency broadcasts . Why This Matters Every second counts in a disaster. Quake fills the critical gap between standard navigation apps and real-world emergency needs. ✔️ Lives can be saved by optimizing routes to avoid collapsed infrastructure. ✔️ Disaster response teams can leverage the tool for better evacuation planning. ✔️ Urban planners can use risk analysis to improve city resilience. In the face of increasing natural disasters, Quake represents a vital step toward technology-driven emergency preparedness. Final Thoughts Quake is not just a navigation app—it is an intelligent disaster response system that helps people reach safety faster and smarter. By integrating real-time risk factors with advanced route planning, it bridges the gap between emergency response and modern technology. 🚀 With further development, Quake has the potential to become a global emergency navigation system, ensuring that when disaster strikes, people always have a safe way out. <div