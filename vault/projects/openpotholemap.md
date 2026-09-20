---
slug: "openpotholemap"
url: "https://devpost.com/software/openpotholemap"
title: "OpenPotholeMap"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 279
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# OpenPotholeMap

> Leverages computer vision, GPS, and crowdsourcing to detect potholes, warn drivers, and share data with city authorities in real time.

[Devpost](https://devpost.com/software/openpotholemap) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[disaster_emergency]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** ai, express.js, gcp, github-actions, google, google-maps, mongodb, node.js, react, roboflow, shadcn, tailwindcss, typescript, vite

## How they structured the write-up

- 🫳 what it does
- 👊 how we built it
- 💪 challenges we ran into
- 🙌 accomplishments we’re proud of
- 🫶 what we learned
- 🤞 what’s next

## Body

Dashboard Map Pothole 🚧 OpenPotholeMap 🫳 What it does OpenPotholeMap is a crowdsourced pothole mapping system. Using a phone camera and AI, it detects potholes in real time, logs them to a central database, and visualizes them on a live interactive map. Drivers get instant alerts (“⚠ Pothole 50m ahead”), and admins can verify reports or export data to authorities. 👊 How we built it Backend: Node.js + Express, MongoDB (Mongoose), Socket.io for real-time events, Roboflow Universe for detection, Firebase Auth + JWT for login. Frontend: React + TypeScript + Vite, Google Maps integration, camera streaming with WebSockets, REST + Socket.io clients. Infra: GitHub Actions for CI/CD, hosting via Vercel, cloud inference via Roboflow. 💪 Challenges we ran into Keeping video streaming stable while sending frames at a usable rate. Tuning the AI model confidence threshold (p > 0.6) to reduce false positives. Matching detections with GPS coordinates reliably. Designing a scalable geospatial data model that avoids duplicate entries. 🙌 Accomplishments we’re proud of A working end-to-end pipeline: camera → AI → DB → live map → alerts. Clean Google Maps–like UI that feels intuitive. Admin dashboard and verification tools for data integrity. Bridging AI and geospatial mapping into a real safety tool. 🫶 What we learned Real-time distributed system design is harder than it looks. Best practices in WebSocket communication, rate limiting, and recovery. Handling geospatial queries and data visualization at scale. Trade-offs between cloud inference and edge AI deployment. 🤞 What’s next Detect more hazards (speed bumps, flooding, debris). Add gamification for user engagement. Direct integration with FDOT/authority APIs for repair reporting. Native mobile app for better performance. On-device inference to cut latency and cloud costs. <div