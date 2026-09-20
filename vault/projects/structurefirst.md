---
slug: "structurefirst"
url: "https://devpost.com/software/structurefirst"
title: "StructureFirst"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 647
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/disaster_emergency"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# StructureFirst

> Evidence-linked 3D structure briefings that help emergency teams understand observed spaces before entry.

[Devpost](https://devpost.com/software/structurefirst) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[disaster_emergency]]
**substrate** [[geospatial]] [[video_visual]]

**stack** apple-sharp, cuda, electron, fastapi, fastify, gaussian-splatting, loftr, lucidframe, maplibre, node.js, onnx-runtime, opencv, openstreetmap, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for structurefirst

## Body

Inspiration Emergency teams are often asked to make fast decisions with incomplete information. Before entering a house, they may not know the layout, where the stairs are, which rooms connect, or what areas have actually been seen. StructureFirst started with one question: what if a responder could open one workspace before entry and understand the building from real visual evidence instead of searching through separate photos, plans, and notes? What it does StructureFirst turns authorized property photos and floor plans into an evidence linked visual briefing for emergency teams. An operator adds a capture set and an optional blueprint. The system separates floor plans, property images, and unrelated photos before reconstruction. It only connects images when there is real visual overlap, then creates navigable Gaussian splat Rescue Views from the verified evidence. Responders can inspect rooms, source camera positions, and the House Map in one place. The map shows where a 3D scene is available, where placement is uncertain, and where there is no verified imagery. StructureFirst also runs local YOLO26 detection over the Rescue View. It can highlight visible objects such as beds, couches, stairs, and sharp objects as situational awareness cues. These are clearly shown as unverified visual observations, not claims that a person or danger is present. How we built it We built StructureFirst as a TypeScript desktop application using Electron, React, Vite, Fastify, Python, and FastAPI. For the 3D scenes, we integrated LucidFrame and Apple SHARP Gaussian splatting. We use SIFT, indoor LoFTR, VGGT camera estimation, and correspondence checks to decide which views can actually connect. Spark and Three.js render the Gaussian scenes in the Rescue View. The application supports local NVIDIA CUDA processing and local YOLO26 object detection through ONNX Runtime. MapLibre and OpenStreetMap provide the location and property map experience. Challenges we ran into The hardest challenge was making the system honest. Many images can look similar without belonging to the same room. A 3D reconstruction can also look convincing even when the source images do not support it. We did not want StructureFirst to invent a hallway, room, or safe route just because the result looked good. We focused on visual overlap, calibrated source cameras, room separation, and visible uncertainty. If the system cannot verify a connection, it should keep that space separate instead of pretending it is part of the building. Accomplishments that we're proud of We are proud that StructureFirst is more than a 3D viewer. It connects image organization, multi image reconstruction, room context, source evidence, object awareness, and a floor plan into one emergency focused workspace. We are especially proud of the Rescue View and House Map working together. A responder can see the observed 3D scene, understand where the original camera views came from, and use the plan to understand which rooms have usable visual coverage. Most importantly, the project treats uncertainty as useful information. Knowing what has not been verified can be just as important as knowing what has. What we learned We learned that building for emergency response means accuracy matters more than a flashy result. AI and 3D reconstruction are powerful, but they need clear boundaries. A system should show its evidence, preserve the original inputs, and avoid presenting assumptions as facts. We also learned that good multi image reconstruction depends on how photos were captured. Doorways, hallways, stairs, and overlapping views are essential for connecting a whole house. What's next for StructureFirst Next, we want to improve whole house reconstruction, room to blueprint alignment, doorway bridging, and smoother loading between connected scenes. The current product uses manually supplied, authorized photos and floor plans. In the future, StructureFirst could support permissioned responder uploads and rights reviewed property data integrations. We will not depend on unlicensed listing image scraping. Our goal is simple: help emergency teams enter with more evidence, better spatial context, and a clearer understanding of what is still unknown. <div