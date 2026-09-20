---
slug: "eco-pulse-fpbo15"
url: "https://devpost.com/software/eco-pulse-fpbo15"
title: "Eco-Pulse"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 926
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Eco-Pulse

> Mapping heat. Planting relief.

[Devpost](https://devpost.com/software/eco-pulse-fpbo15) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]] [[finance_payments]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** fastapi, gemini, google-maps, google-streetview, nextjs, python, railtracks, react, tailwind, typescript

## How they structured the write-up

- 💡 inspiration
- ⚙️ what it does
- 🛠️ how we built it
- 🌐 the google tech stack
- 📊 the metric: calculating carbon & energy reduction
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for eco-pulse

## Body

Example of the suggestion for the top priority area The map with the suggestions and the estimation Built with Railtracks 💡 Inspiration Climate change and dense concrete are turning cities like Toronto and Montreal into "Urban Heat Islands" (UHIs), leading to dangerous heatwaves and massive AC energy consumption. While city planners and politicians have thermal maps that show them where the city is dangerously hot, they suffer from operational stagnation. Calculating exactly what to do on a specific street corner requires expensive consultants and months of 3D thermal physics simulations. Between the prohibitive costs, the time lags of modeling wind and heat flux, and the bureaucratic friction of stakeholders not being able to "see" the impact until it's built, progress stalls. We wanted to build a tool that replaces months of consulting with instant, actionable math. ⚙️ What it does Eco-Pulse is a generative, multimodal AI tool that converts thermal data into instant intervention blueprints. A user opens an interactive map showing the city's thermal hotspots. When they click on a specific severe "hot zone" (like a massive, unshaded concrete plaza), the application doesn't just say "it's hot here." Instead, it uses Gemini to analyze the street-level and rooftop data, instantly generating a fully costed Intervention Blueprint. It spits out a visual overlay of proposed tree canopies and green roofs, alongside a calculated dashboard showing the estimated temperature drop (e.g., -4°C) and the projected cost of the intervention. It gives city planners instant, actionable, and visual solutions. 🛠️ How we built it We split the architecture into a deterministic data pipeline and a generative visual engine: The Data Engine: We built a rigorous financial risk model using an unsupervised ML clustering algorithm (K-Means). It ingests geospatial heat and canopy data, intersects it with population density, and mathematically isolates the Top 10 most critical zones, removing any arbitrary guesswork. The Backend Orchestration: We orchestrated the AI logic using the Railtracks framework on a FastAPI backend, wrapping our LLM calls into reliable, repeatable agentic workflows. The Visual Engine: We passed localized coordinates to Google's mapping APIs to pull street-level imagery, which our AI then semantically analyzed and visually reconstructed to show photorealistic green infrastructure. 🌐 The Google Tech Stack Eco-Pulse relies heavily on the Google ecosystem to bridge the gap between geospatial data and Generative AI: Gemini 2.5 Flash (via Google GenAI SDK): Acts as the core Urban Planner logic engine, analyzing structural Street View geometry, identifying "plantable" surfaces versus "fixed" infrastructure, and calculating the financial/botanical metrics. Gemini 3.1 Flash Image (Nano Banana 2): Powers our Generative Style Transfer pipeline. It takes baseline street views and instantly inpaints photorealistic green infrastructure (like mature oak trees or reflective roofs) while perfectly maintaining structural building geometry. Google Maps Static API & Street View API: Provides the baseline visual data and precise geospatial bounding-box fallbacks for our ML-identified hot zones. 📊 The Metric: Calculating Carbon & Energy Reduction Eco-Pulse does not just guess the environmental impact; it integrates the Natural Capital Project's InVEST Urban Cooling Model methodology to project exact temperature reductions and carbon emission savings. First, we calculate the Cooling Capacity Index. Instead of arbitrary heuristics, our model evaluates three core biophysical parameters for every targeted hot zone: Shade (canopy cover), Evapotranspiration (moisture release from vegetation), and Albedo (surface reflectivity). By mathematically weighting these factors, we generate a specific Cooling Capacity score for the new AI-generated green infrastructure. Second, the Temperature Reduction. Using the InVEST heat mitigation equations, we map the Cooling Capacity against the city's baseline maximum temperatures to calculate the exact localized temperature drop achieved by the AI's blueprint. Finally, the Energy and Carbon ROI. Leveraging urban energy physics, we calculate the building cooling demand reduction based on the newly lowered ambient temperature. If a commercial block in our ML-identified Critical Zone consumes 250,000 kWh per year, the InVEST-calculated temperature drop directly translates into kilowatt-hours of AC energy saved. We then convert those saved kWh into exact metric tons of CO2 averted based on the local energy grid's carbon intensity, giving city planners a mathematically bulletproof environmental ROI. 🚧 Challenges we ran into Initially, we tried to build our generative image pipeline using Google Cloud Vertex AI, but we were constantly blocked by complex IAM permissions and organization policies. We successfully pivoted to the native Google GenAI developer API (google-genai), which allowed us to access the bleeding-edge Gemini 2.5 Flash and 3.1 Flash Image models seamlessly. We also had to work hard to constrain the LLM so it wouldn't invent fake construction costs, fixing this by injecting a strict financial rulebook into the system prompt. 🏆 Accomplishments that we're proud of We are incredibly proud of merging hardcore financial risk management with generative AI. Rather than just building a wrapper that says "plant trees here," we built a mathematically sound pipeline. The K-Means clustering ensures we are targeting the right neighborhoods, and the strict unit economics ensure the city planner gets a budget they can actually take to city hall. 📚 What we learned We learned how to orchestrate multi-step LLM chains using the Railtracks framework, which made our backend significantly cleaner. We also experienced the massive generational leap of Gemini 2.5 Flash—its speed and native multimodal vision capabilities are exactly what make a real-time UI slider possible. 🚀 What's next for Eco-Pulse We want to move beyond static Google Street View images and integrate real-time drone LiDAR data. We also plan to expand the financial dashboard to include municipal tax incentives and water-runoff savings, turning Eco-Pulse into the ultimate end-to-end procurement tool for global city councils. <div