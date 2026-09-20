---
slug: "stem-lens"
url: "https://devpost.com/software/stem-lens"
title: "STEM-Lens"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 360
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# STEM-Lens

> STEM-Lens is an AI visual tutor transforming STEM education. It breaks down complex science, math, and engineering questions into easy-to-understand explanations with dynamic, visual data points.

[Devpost](https://devpost.com/software/stem-lens) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
  <sub>weak: on_device_local, sensor_fusion</sub>
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: sensor_telemetry</sub>

**stack** gemini-api, python, streamlit

## How they structured the write-up

- 💬 inspiration
- ⚙️ what it does
- 🛠️ how we built it
- 🏆 challenges we ran into
- 🎉 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for stem-lens

## Body

STEM-Lens Nexus: Advanced Cyberpunk Interactive AI Matrix with Local Math Core Fallback System. STEM-Lens Nexus running locally on Streamlit with interactive Plotly telemetry graphs and optimized dynamic physics engine mapping. 💬 Inspiration Standard textbooks and traditional textual AI models often fail to capture the true visual essence of STEM (Science, Technology, Engineering, and Math) subjects. Complex physics simulations, advanced mathematical formulas, and deep data patterns are best learned when students can actually see them. We built STEM-Lens to bridge this massive gap between abstract textbook theories and intuitive visual learning. ⚙️ What it does STEM-Lens is an intelligent AI visual tutor built specifically for students and educators. When a user inputs a complex STEM query, the core engine processes the request and breaks it down into clear, highly rigorous academic explanations. Crucially, instead of just generating plain text, STEM-Lens extracts structural data sequences and automatically generates dynamic plots, charts, and mathematical graphs to illustrate the concept visually in real time. 🛠️ How we built it The application is entirely powered by Python. We used Streamlit to create a seamless, responsive, and minimalist user interface. The intelligence of the tutor is driven by the Google Gemini Pro API, which handles complex prompt parsing and data structuring. For the visual mapping and plotting components, we integrated robust Python data visualization libraries to render interactive graphs. 🏆 Challenges we ran into One of the toughest challenges was ensuring that the AI model returns data in a perfectly structured, strict format (like JSON arrays) that our frontend can reliably parse and plot every single time without crashing. We solved this by implementing rigorous system instructions and advanced prompt engineering constraints within the API pipeline. 🎉 Accomplishments that we're proud of We successfully built a functional, beautifully designed educational platform that combines world-class AI explanations with real-time visual tracking under tight hackathon timelines. 📚 What we learned We gained deep insights into structuring LLM responses for dynamic visual components and mastering frontend layouts using Python Streamlit. 🚀 What's next for STEM-Lens We plan to introduce interactive physics simulator toggles, LaTeX mathematical proof rendering, and an offline database for instantly caching common high-school STEM questions. <div