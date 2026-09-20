---
slug: "aperture-ai-smart-event-photo-curator"
url: "https://devpost.com/software/aperture-ai-smart-event-photo-curator"
title: "Aperture AI: Smart Event Photo Curator"
hackathon: "DigitalOcean Gradient™ AI Hackathon"
organization: "DigitalOcean"
winner: true
words: 967
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Aperture AI: Smart Event Photo Curator

> A cloud-native SaaS that automates the grueling process of event photo culling and uses a DigitalOcean Agent to write your social media captions.

[Devpost](https://devpost.com/software/aperture-ai-smart-event-photo-curator) · hackathon [[DigitalOcean Gradient- AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[labor_employment]] [[transportation]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** celery, digitalocean, digitalocean-adk, digitalocean-droplets, docker, fastapi, google-gemini, llama-3, mediapipe, opencv, postgresql, python, react, redis

## How they structured the write-up

- 💡 inspiration
- ⚙️ what it does
- 🏗️ how we built it
- 
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for aperture ai
- 💻 tech stack
- * frontend: react.js (vite), axios, custom css3 glassmorphism

## Body

User login page Bulk images upload Dashboard Showing the features and culling results Aperture AI found images from prompt Captions generated for the image 📸 Aperture AI: Smart Event Photo Curator 💡 Inspiration Anyone who has ever photographed a wedding, a corporate event, or a hackathon knows the absolute dread of the "cull." You take 2,000 photos, but ~40% are blurry, ~20% have people blinking, and ~20% are near-identical burst shots. Sorting them manually takes hours of tedious, soul-crushing work. We wanted to build an enterprise-grade AI pipeline that doesn't just automate this painful sorting process, but transforms the entire album into an interactive, semantic database. We envisioned an autonomous event archivist, powered by DigitalOcean Gradient™ AI , that can cull the trash, recognize VIPs, search by visual meaning, and act as an on-demand social media copywriter. ⚙️ What it does Smart Photo Curator is a highly optimized Multi-Agent Orchestration platform built entirely on the DigitalOcean ecosystem. It operates in two major phases: Phase 1: The Local Telemetry Cull Users upload massive raw event folders. Our asynchronous hardware-aware workers instantly: Trash blurry images using OpenCV Laplacian Variance. Reject blinking subjects using Google MediaPipe Eye Aspect Ratio (EAR) calculations. Group identical burst shots using Perceptual Hashing (pHash), keeping only the sharpest frame. Isolate VIPs by calculating exact Cosine Distances from a reference selfie. Phase 2: Gradient™ AI Orchestration (The Magic) Once the album is cleansed, we unleash the true power of DigitalOcean Gradient™ AI : Semantic Vector Search: Every kept photo is mathematically embedded into 768-dimensional vectors and stored in a DigitalOcean Managed PostgreSQL database using the pgvector extension. Aperture AI (Agentic RAG): Users can chat directly with their album using a fully-managed Gradient™ AI Agent (powered by Meta Llama 3). Ask "Find photos of us laughing at sunset," and the backend calculates the cosine distance, injects the matching visual telemetry into the Agent, and streams back a conversational response with the exact photos. AI Social Copywriter: Clicking "Generate Caption" in the cinematic UI triggers Gradient™ AI Serverless Inference , instantly writing context-aware, hashtag-ready Instagram copy based on the specific pixels of that image. 🏗️ How we built it We engineered a decoupled, cloud-native architecture explicitly optimized to push DigitalOcean's infrastructure to its limits. DigitalOcean Gradient™ AI Platform: We heavily utilized both Managed Agents (for stateful, RAG-powered chat) and Serverless Inference (for rapid, stateless caption generation). DigitalOcean Managed Databases: Spun up a robust PostgreSQL cluster with the pgvector extension to handle rapid, high-dimensional similarity searches. DigitalOcean Droplets: Hosted our Dockerized stack, FastAPI backend, and Nginx React frontend. Redis & Celery: Act as our high-speed asynchronous message broker and task queue. VIP Matching Mathematics To keep compute costs low without sacrificing accuracy, we calculate Cosine Similarity natively for facial recognition: $$Distance = 1 - \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$ This allows us to enforce strict mathematical identity thresholds directly on the CPU. System Design Architecture 🚧 Challenges we ran into Challenge 1: The Cloud CPU vs. Machine Learning Death Match Running heavy C++ computer vision libraries (TensorFlow, MediaPipe) on cloud CPUs caused catastrophic Out-Of-Memory (OOM) crashes and segmentation faults. The Linux kernel was mercilessly killing our Celery workers when 4K smartphone images spiked the RAM. The Fix: We engineered aggressive Memory Leak Eradication . By configuring Celery with --max-tasks-per-child=1 , workers are forced to safely self-destruct and return 100% of their memory to the Droplet after every album. We also implemented strict Lazy Loading for our AI models and swapped heavy deep-learning networks for the ultra-lightweight OpenCV SFace model. Challenge 2: Bypassing Free-Tier API Rate Limits (JSON Multiplexing) To achieve semantic search, we needed to pass our kept photos through Google Gemini 2.5 Flash to extract visual context before vectorizing them. However, hitting the API sequentially resulted in instant 429 Quota Exceeded bans. The Fix: We invented Batch Vision Multiplexing . Instead of sending 30 photos in 30 requests, our Celery worker chunks images into batches of 15. We send one massive request to the Vision model, forcing it to analyze all 15 images simultaneously and return a strictly typed JSON array. This cut our API footprint by 95% and reduced processing time from 5 minutes to under 30 seconds. 🏆 Accomplishments that we're proud of We successfully deployed a heavy, multi-model AI pipeline on standard cloud CPUs without relying on expensive GPU instances. Flawlessly chained local OpenCV telemetry into DigitalOcean Gradient™ Serverless Inference . Built a highly accurate Semantic Search Engine using DO Managed PostgreSQL + pgvector . Designed a breathtaking, animated React UI featuring a sliding manual-override lightbox. Engineered a seamless OAuth workflow allowing users to securely export curated VIP folders directly to their Google Drive. 📚 What we learned We learned the hard reality of hardware-aware ML engineering. An AI system that runs perfectly on a local developer laptop often suffocates when deployed in real-world cloud environments. We mastered managing C++ memory behavior inside Python wrappers, safely casting NumPy float64 tensors into PostgreSQL vector storage, and effectively orchestrating DigitalOcean's Agent Development Kit (ADK) . 🚀 What's next for Aperture AI Infinite Photo Scaling: Migrating our raw image storage from local Docker volumes directly to DigitalOcean Spaces (S3-compatible object storage) for enterprise scalability. Auto-Scaling Infrastructure: Migrating our docker-compose stack to the DigitalOcean App Platform to automatically spin up additional stateless Celery worker nodes during heavy traffic spikes (like wedding season). 💻 Tech Stack AI/ML: DigitalOcean Gradient™ AI (Agents & Serverless), Gemini 2.5 Flash, OpenCV, MediaPipe, DeepFace (SFace) Cloud: DigitalOcean Droplets, DO Managed PostgreSQL ( pgvector ) Backend: Python 3.12, FastAPI, Celery, Redis, SQLAlchemy * Frontend: React.js (Vite), Axios, Custom CSS3 Glassmorphism The Future of Event Photography Aperture AI transforms event photography from manual sorting chaos into a fully automated AI workflow . From raw photos → curated albums → social media ready content in minutes. <div