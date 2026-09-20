---
slug: "live-it"
url: "https://devpost.com/software/live-it"
title: "Live-it"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 450
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# Live-it

> Live your imagination

[Devpost](https://devpost.com/software/live-it) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]]
  <sub>weak: geospatial, sensor_telemetry</sub>

**stack** cuda, gemini, node.js, python, react, typescript, veo3

## Body

Inspiration We wanted to give people the power to experience any image—real or imagined—as an explorable 3D world. Whether it's a childhood photo, a city street, or a prehistoric jungle, users should be able to reimagine the setting and step into it. This idea led us to build Live-it: a pipeline that lets users modify an image via prompt, generate a cinematic video using Veo 3, and turn that into a walkable 3D scene. What it does Live-it allows users to: Enter or upload an image, and optionally rewrite it using a creative prompt. Generate a stylized video from that image using Veo 3 (Gemini API). Reconstruct the scene into 3D using fast and high-quality Gaussian Splatting. Walk through the scene in a real-time 3D engine (Nitrode or web-based renderer). How we built it Frontend: React + TypeScript for the UI, including prompt editing, video preview, and 3D scene interaction. Backend: Node.js server that handles prompt submission, Veo 3 API calls, and routes for rendering. Veo 3 Integration: Gemini API for generating high-quality, 8-second stylized cinematic videos. 3D Reconstruction: Started with NeRFStudio but shifted to 3D Gaussian Splatting due to speed and quality. Used VGGT, a recent vision model, to infer accurate camera trajectories from Veo videos. Languages and Infra: Python, CUDA, C++, and Node.js running on a cloud instance (T4/Colab Pro/own server). Challenges we ran into Slow convergence of NeRF on T4 GPUs caused rendering lags and noisy outputs. COLMAP camera estimations were highly inaccurate on synthetic Veo videos, producing distorted splats. Integrating multiple models (Gemini → VGGT → GSP) in one unified pipeline required careful output formatting. Latency between prompt → video → 3D posed difficulty for live previewing during a 36-hour hackathon. Accomplishments that we're proud of Integrated end-to-end prompt-to-3D generation in a single user-friendly web app. Achieved real-time 3D previews using Gaussian Splatting + VGGT for fast camera estimation. Built a modular backend that can scale to new input modalities (videos, text descriptions, photos). Enabled scene-level creativity: users can style their environment before walking through it. What we learned Prompt engineering for Veo 3 affects not just visual tone, but downstream mesh quality. NeRF is powerful but impractical for hackathon-paced iteration—Gaussian Splatting wins on speed/quality tradeoff. VGGT-style direct trajectory inference significantly improves 3D fidelity on synthetic content. Splat rendering is a game-changer for demo-ready NeRF-based workflows. What’s next for Live-it Add VR or headset support to explore scenes with full immersion. Support temporal continuity (multi-video, scene stitching). Implement prompt-driven re-styling after 3D generation: switch from forest to cyberpunk in real-time. Experiment with Volumetric Audio + Soundscape AI to add dynamic sound layers to the 3D world. Extend to multiplayer walkthroughs—collaboratively explore a memory or place. <div