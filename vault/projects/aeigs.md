---
slug: "aeigs"
url: "https://devpost.com/software/aeigs"
title: "AEIGS"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 611
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# AEIGS

> AEGIS is a real-time satellite monitoring and conjunction detection system that predicts close approaches between space objects and visualizes orbital activity on an interactive 3D globe.

[Devpost](https://devpost.com/software/aeigs) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]] [[structured_db]]

**stack** celestrak, css, next.js, numpy, react, sgp4, tailwind, three.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aegis

## Body

AEGIS : Space Situational Awareness System Inspiration With the rapid growth of satellites and orbital debris, Earth's orbit is becoming increasingly congested. Modern satellite constellations such as Starlink and OneWeb have significantly increased the number of active objects in space, making conjunction monitoring more important than ever. We wanted to build a system that could not only track satellites visually, but also analyze potential close approaches and make this information understandable through interactive visualization and AI-assisted insights. The goal was to create an accessible and complete end-to-end space situational awareness platform using open data and modern web technologies. What it does AEGIS is a real-time satellite tracking and conjunction detection system that monitors thousands of satellites orbiting Earth. The platform: Fetches TLE (Two-Line Element) data from public satellite sources Predicts satellite positions using orbital propagation models Detects conjunctions (close approaches between satellites) Calculates: Miss distance Relative velocity Time of Closest Approach (TCA) Classifies events into: HIGH risk MEDIUM risk LOW risk Displays satellites and conjunctions on an interactive 3D globe Generates AI-powered summaries and recommendations for conjunction events The system currently visualizes approximately 17,000+ tracked objects in Earth orbit. How we built it The system follows a modular client-server architecture. Layer Technology Frontend Next.js 16, React 19, TypeScript Backend FastAPI (Python) Visualization react-globe.gl, Three.js Database SQLite Orbit Propagation sgp4 Spatial Search scipy.spatial.cKDTree AI Analysis Gemini 2.5 Flash Scheduling APScheduler Orbit Propagation Satellite positions are propagated using the SGP4 model from TLE data: $$\mathbf{r}(t), \mathbf{v}(t) = \text{SGP4}(TLE, t)$$ Where: $\mathbf{r}(t)$ = position vector $\mathbf{v}(t)$ = velocity vector Closest Approach Calculation The distance between two satellites is computed using Euclidean distance: $$d = |\mathbf{r}_1 - \mathbf{r}_2|$$ Relative velocity: $$v_{\text{rel}} = |\mathbf{v}_1 - \mathbf{v}_2|$$ Efficient Conjunction Search Instead of brute-force $O(n^2)$ comparison, the system uses a KD-Tree for efficient nearest-neighbor search: $$\mathcal{O}(n \log n)$$ This allows the system to process large satellite datasets efficiently. Challenges we ran into One of the biggest challenges was handling large-scale satellite datasets efficiently. Rendering and processing thousands of satellites simultaneously introduced performance bottlenecks both in the backend and frontend. Another challenge was accurate conjunction detection. Small timing or coordinate conversion errors could significantly affect closest-approach calculations. Careful validation and synchronization of propagation windows were required. Integrating AI analysis also introduced reliability issues due to external API rate limits and high-demand failures. To address this, caching and fallback mechanisms were implemented. Frontend interaction with WebGL-based rendering created additional issues such as tooltip event handling and rendering optimization for large object counts. Accomplishments that we're proud of Successfully tracking and visualizing 17,000+ satellites Implementing efficient conjunction detection using KD-Tree optimization Building a complete end-to-end pipeline from raw TLE ingestion to visualization Integrating AI-powered conjunction summaries and recommendations Creating a responsive and interactive 3D globe interface Optimizing rendering and backend processing for large-scale datasets Designing a modular architecture that cleanly separates computation, APIs, and visualization What we learned Through this project, we gained practical experience in: Orbital mechanics and satellite propagation Space situational awareness concepts Efficient spatial search algorithms Full-stack system architecture Real-time data visualization WebGL and 3D rendering optimization API integration and caching strategies Handling large-scale datasets in interactive applications We also learned the importance of balancing computational accuracy with frontend performance and usability. What's next for AEGIS Future improvements planned for AEGIS include: More accurate collision probability estimation Historical conjunction analytics Advanced orbit filtering and satellite categorization Better AI-assisted event interpretation Performance scaling for larger datasets Real-time alert and notification systems Improved orbital prediction accuracy using additional perturbation models Multi-user monitoring dashboards and collaborative analysis features The long-term goal is to evolve AEGIS into a more advanced and scalable platform for accessible space situational awareness and conjunction analysis. <div