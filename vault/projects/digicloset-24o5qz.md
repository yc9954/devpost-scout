---
slug: "digicloset-24o5qz"
url: "https://devpost.com/software/digicloset-24o5qz"
title: "DIGICLOSET"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 626
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# DIGICLOSET

> AI powered Virtual Try On Software

[Devpost](https://devpost.com/software/digicloset-24o5qz) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[climate_energy]] [[developer_tools]] [[retail_commerce]] [[supply_logistics]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[video_visual]]

**stack** javascript, python, script, typescript

## How they structured the write-up

- inspiration problem of waste generated due to returned clothing products
- what it does digicloset is an ai-powered personal wardrobe and smart shopping assistant that aims to reduce clothing returns and fashion waste.
- how we built it backend (python)
- challenges we ran into handling images reliably: dealing with different lighting, angles, clothing textures, and user-uploaded noise.
- accomplishments that we're proud of built a working ai size recommendation and wardrobe classifier prototype.
- what we learned fashion-tech requires a balance between ai, ux, and personalization.
- what's next for digicloset advanced virtual try-on: more accurate body mesh models, ar try-on, and 3d garment simulation.

## Body

Inspiration problem of waste generated due to returned clothing products The fashion industry faces a massive sustainability issue: over 30–40% of online clothing purchases are returned, and a significant portion of those returns never make it back to shelves. Reasons include incorrect sizing, poor fit, unexpected texture, or color mismatch. Many brands find it too expensive to reprocess returns, so perfectly usable clothing ends up in landfills, adding to global waste and carbon emissions. DIGICLOSET was inspired by the opportunity to: Reduce return-related waste Help customers choose clothing that fits them the first time Empower brands with smart sizing and virtual try-on Support circular, eco-friendly fashion What it does DIGICLOSET is an AI-powered personal wardrobe and smart shopping assistant that aims to reduce clothing returns and fashion waste. It provides: 👗 1. Digital Wardrobe Upload your clothes and manage them virtually — organize, search, and plan outfits effortlessly. 📏 2. AI Fit & Size Prediction Using ML-based body measurement estimation and garment dimension analysis, DIGICLOSET predicts: The user’s ideal size for a brand Fit confidence and areas of mismatch Purchase recommendations that reduce size-based returns How we built it Backend (Python) Flask/FastAPI (depending on version) ML models for size prediction & clothing classification Image processing with OpenCV / MediaPipe Vector search for outfit recommendations 🎨 Frontend (React / Next.js) Clean UI design for wardrobe and try-on interfaces API integration for real-time recommendations Tailwind CSS for responsive stylingBackend (Python) Flask/FastAPI (depending on version) ML models for size prediction & clothing classification Image processing with OpenCV / MediaPipe Vector search for outfit recommendations 🎨 Frontend (React / Next.js) Clean UI design for wardrobe and try-on interfaces API integration for real-time recommendations Tailwind CSS for responsive styling Infrastructure Docker containerization for consistent deployment Redis for caching recommendation results Cloud storage for user images and wardrobe items GitHub Actions CI/CD for automated builds and tests 📡 Monitoring & Observability OpenTelemetry Logging dashboards Metrics to track system health and model accuracy Challenges we ran into Handling images reliably: Dealing with different lighting, angles, clothing textures, and user-uploaded noise. Measurement accuracy: Predicting body size from limited images required careful tuning and model experimentation. Model generalization: Ensuring the AI works across diverse body shapes, clothing brands, and regional size standards. Directory and code inconsistencies: The project had multiple versions, spacing issues in paths, and a mixed structure (fixed in upgrade pack v2). Deployment complexity: Mixing Node + Python + ML models required clean containerization and CI/CD improvements. Time & resource constraints: High-quality virtual try-on requires complex 3D modeling — challenging in early stages Accomplishments that we're proud of Built a working AI size recommendation and wardrobe classifier prototype. Created a clean digital wardrobe UI with real-time outfit suggestions. Reduced return likelihood in user testing by predicting the correct size. Developed a sustainability-first solution with measurable impact. Containerized the entire system for smooth deployment. Implemented a scalable pipeline + monitoring stack. Demonstrated tangible potential to reduce fashion waste at scale What we learned Fashion-tech requires a balance between AI, UX, and personalization. User-generated content (wardrobe photos) demands strong preprocessing. ML bias and sizing variations across brands are major challenges. Clean repository structure and CI automation dramatically improve velocity. Cross-functional design (backend, ML, UI/UX) is essential for real user impact. What's next for DIGICLOSET Advanced virtual try-on: More accurate body mesh models, AR try-on, and 3D garment simulation. Brand integrations: API to connect with online stores for size prediction at checkout. User social features: Outfit sharing, style communities, virtual fashion boards. Carbon-saving dashboards: Track personal sustainability footprint. Inventory scanning: ML to detect clothing automatically from photos. Generative AI stylist: Personalized styling, closet augmentation, outfit generation. Mobile app (iOS & Android): Bring DIGICLOSET to users’ fingertips everywhere. Machine-learning pipelines: Continual model improvement with feedback loops. <div