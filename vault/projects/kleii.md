---
slug: "kleii"
url: "https://devpost.com/software/kleii"
title: "kleii"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 796
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# kleii

> "Sketch a rondavel on a napkin, watch it build itself in 3D, then get it physically made. One platform for designing, growing, and building anything on earth."

[Devpost](https://devpost.com/software/kleii) · hackathon [[Build with MeDo Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[agriculture_food]] [[climate_energy]]
**user** [[frontline_worker]]
  <sub>weak: legal_professional</sub>
**substrate** [[video_visual]]
  <sub>weak: geospatial, sensor_telemetry, structured_db</sub>

**stack** medo.dev

## Body

The Story Behind Kleii I built Kleii for the love of my life — my fiancée. She's an interior designer, and every single day I watch her pour her soul into creating beautiful spaces for her clients. She sketches on napkins at dinner. She photographs soil when we visit sites together. She hunts for artisans who can fabricate the furniture pieces she imagines. She juggles ten disconnected tools — Pinterest boards, CAD software, spreadsheets for costing, WhatsApp groups to find builders, separate apps for plant selection. I wanted to give her one platform that does it all. And honestly? I'm also building this because I'm about to propose to her (yes, judges — this is the project of a man madly in love, building the tool his future wife deserves to have). If Kleii wins, the prize goes straight toward our life together — and toward making this real for every designer, farmer, and maker across Africa and beyond who deserves better tools. How I Used MeDo MeDo was my co-architect for every layer of Kleii. Here's how I structured our conversations: Conversation 1 — The Spine : I told MeDo about the problem — designers in Africa working with disconnected tools, no platform that understands non-rectangular architecture, no connection between design and fabrication. MeDo helped me architect the entire project spine: Site → Structure → Interior → Land Intelligence → Artisan Marketplace → Business Layer. Conversation 2 — Lepako Engine : I described the material and crop recommendation challenge. MeDo generated the full Lepako intelligence engine — a context-aware recommendation system that considers GPS , climate, soil type, budget, and local material availability to suggest what to build with and what to plant. It structured the Random Forest classifier approach and the multi-factor input/output architecture. Conversation 3 — Sketch to Walls : This is where the magic happened. I asked MeDo to help me build the auto-wall generation pipeline — where a user uploads a hand-drawn sketch and Kleii interprets it into 3D walls automatically. MeDo generated the full CV + ML pipeline: preprocessing, line detection, interpretation, 3D extrusion, and auto-rendering. Most critically, it handled non-rectangular shapes — circular rondavels, freeform curves, organic architecture that most platforms ignore entirely. Conversation 4 — Artisan Marketplace + Get This Built : I described how my fiancée constantly struggles to find fabricators for her custom furniture designs. MeDo built the full commission pipeline — from parametric object design to cost estimation to artisan matching to fabrication tracking. Conversation 5 — Voice Integration : MeDo helped wire ElevenLabs into a Talk to Build voice-first design flow, a speaking Lepako advisor, and an artisan matchmaker voice agent. The Most Impressive Feature MeDo Generated The Sketch → Walls → Render pipeline. Without question. I gave MeDo the challenge: "A user photographs a hand-drawn floor plan — including circular/organic shapes common in African architecture — and Kleii must auto-generate 3D walls, place openings, apply locale-appropriate materials via Lepako, and produce a render. No manual modeling required." MeDo generated: The full computer vision preprocessing chain (deskew, perspective correction, noise removal) A line detection + classification model that distinguishes walls from partitions from openings Curve interpretation logic that recognizes circular plans as rondavel-type structures and auto-applies conical roofs The 3D extrusion pipeline with smart defaults (2.7m walls, 2.1m doors, 1.2m window sills) Auto-camera placement for renders based on detected rooms And the integration with Lepako so that materials are applied based on the user's GPS location — not generic white-box defaults This is the feature that makes people say wait, it actually did that? — and it's the feature that will change how my fiancée works with every client she has. What Problem Kleii Solves The fragmentation problem. Today, if you're a designer in Johannesburg — or a farmer in Limpopo, or a creative in Lagos — you need: One tool to sketch Another to model in 3D Another to render Another to find materials and costs Another to find builders/artisans Another to manage the project Another to understand your soil and climate Kleii is one platform that unifies design, intelligence, fabrication, and agriculture. It's the first platform that treats a rondavel with the same respect as a Manhattan loft. The first that connects what you design on screen to who can build it with their hands. The first that understands that in Africa (and increasingly worldwide), building, growing, and making are not separate activities — they're one continuous act of creation. Plugins and API Integrations ElevenLabs Voice API : Powers Talk to Build (voice-to-layout generation), Lepako's spoken recommendations, the Artisan Matchmaker voice agent, and the Farm Coach seasonal check-ins GPS /Climate APIs: Auto-fetch location data to power Lepako's material and crop recommendations Computer Vision pipeline: For sketch-to-wall interpretation and soil photo analysis <div