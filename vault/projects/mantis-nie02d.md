---
slug: "mantis-nie02d"
url: "https://devpost.com/software/mantis-nie02d"
title: "Mantis"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 572
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Mantis

> Mantis provides real time threat detection to help retail businesses identify and prevent shoplifting as it occurs, protecting your inventory and reducing loss.

[Devpost](https://devpost.com/software/mantis-nie02d) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: vision_ocr</sub>
**domain** [[retail_commerce]] [[security_privacy]] [[supply_logistics]]
**substrate** [[structured_db]] [[video_visual]]

**stack** baseten, convex, fastapi, fetch.ai, huggingface, livekit, next.js, opencv, python, react, tailwindcss

## How they structured the write-up

- inspiration
- what mantis does
- how we built it
- challenges we overcame
- accomplishments we’re proud of
- what we learned
- what’s next
- our vision

## Body

Video Analysis Mantis Mantis is an intelligent security system that transforms ordinary cameras into proactive theft prevention tools. By combining real-time computer vision and AI, Mantis detects shoplifting, weapons, and threatening behavior the moment they occur—alerting store owners before losses happen. Inspiration We started with one question: Why do most security systems only react after it’s too late? Retailers lose billions every year to theft, yet most cameras just record footage for later review. Humans can’t monitor every feed at once—and by the time incidents are noticed, the culprit is gone. So, we set out to make cameras that could think —systems that recognize suspicious behavior in real time and act before damage is done. What Mantis Does Mantis is an end-to-end intelligent monitoring platform that learns, detects, and alerts: Real-Time Threat Detection: Detects shoplifting, weapons, and aggressive actions within 2 seconds . Face Recognition System: Uses vector embeddings to identify and track repeat offenders across all footage—without storing private identity data. Live Dashboard: LiveKit-powered dashboard overlays detections on the video feed and streams alerts instantly. Smart Querying: Ask questions like “Who stole yesterday?” and get timestamped clips and summaries. Building Mantis taught us invaluable lessons about real-time video processing, multi-agent AI pipelines, and face recognition at scale. Balancing speed, accuracy, and privacy showed us what it takes to move from simple detection to true prevention . How We Built It Architecture Detection Engine: Processes frames at 0.5–1 FPS using specialized AI agents for theft, weapons, and face detection. Face Recognition: Generates and compares facial vector embeddings for cross-incident identification. Live Streaming: Combines LiveKit (for video delivery) and WebSockets (for detection metadata) for synchronized, low-latency updates. Analytics Layer: Uses ChromaDB for semantic vector search and natural-language querying. 💻 Tech Stack Backend: FastAPI + Python AI Models: Hugging Face + Ultralytics Video: OpenCV + LiveKit Database: ChromaDB (for face and clip embeddings) Challenges We Overcame Real-Time Performance at Scale: Achieved <2-second latency across multiple feeds using async job queues, frame sampling, and optimized inference. Accurate Threat Detection: Reduced false positives through a fusion approach combining multiple AI signals. Face Recognition & Privacy: Stored face embeddings separately from personal data, ensuring privacy without losing analytical power. Live Streaming Integration: Engineered a dual-channel pipeline—one for video, one for detection metadata—for seamless synchronization. Accomplishments We’re Proud Of Sub-2-second detection latency—true real-time prevention Face search that scans hours of footage in seconds Multi-agent fusion achieving high accuracy with minimal false alarms A live, intuitive dashboard built for instant response—no training required A system ready for production, not just a demo What We Learned Real-time AI demands millisecond-level optimization—batch processing principles don’t apply 1–2 FPS sampling is the sweet spot for retail: frequent enough to catch incidents, efficient enough for multiple feeds Vector embeddings are game-changing for semantic face tracking and event linking The best AI fails if the UX isn’t intuitive during stressful moments Privacy and ethics must be designed in, not patched later What’s Next Short-Term Mobile alerts with video clips POS integration to detect employee and self-checkout theft Predictive analytics for identifying high-risk locations and times Long-Term Cross-store networks to spot organized retail crime Behavioral analysis for professional shoplifters Edge-deployable systems for privacy-focused retailers Open API for integration with existing security infrastructure Our Vision We envision a world where retail theft becomes economically irrational —where prevention is instant, automated, and intelligent. Mantis isn’t just another security product. It’s the future of proactive protection . <div