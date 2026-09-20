---
slug: "eyelink"
url: "https://devpost.com/software/eyelink"
title: "Eyelink"
hackathon: "NextStep Hacks 2025"
organization: "HackAlphaX"
winner: true
words: 495
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Eyelink

> Bridging Hearts, Paving Ways

[Devpost](https://devpost.com/software/eyelink) · hackathon [[NextStep Hacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]] [[transportation]]
**substrate** [[geospatial]] [[video_visual]]

**stack** controlnet, lstm, mediapipe, next.js, opencv, openstreetmap, python, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eyelink

## Body

Inspiration The spark for EyeLink came from observing how everyday experiences—catching a bus, chatting with a stranger, or rolling across a busy intersection—can become daunting when public spaces, devices, and information channels assume everyone can see, hear, and move in the same ways. We wanted an all‑in‑one platform that hands real independence back to visually impaired, deaf/mute, and mobility‑impaired users, instead of forcing them to juggle separate, single‑purpose tools. What it does EyeLink bundles four complementary services in a single mobile app + wearable ecosystem: Audio Navigation for the Visually Impaired AI object detection gives turn‑by‑turn voice prompts and hazard alerts (e.g., “bicycle approaching from left”). Real‑Time Speech ↔ ASL Translation A bidirectional ASL model renders spoken words as on‑screen signing and converts live ASL gestures to synthesized speech. Wheelchair‑Friendly Route Planner Maps highlight ramps, lifts, and curb cuts; automatic re‑routing steers users around steps or blocked sidewalks. Travel‑Assistant Booking With two taps, users can summon a vetted human assistant (airport meet‑and‑assist, railway transfers, etc.) and track them in‑app. How we built it Computer Vision + Edge AI YOLOv8 pruned & quantized with TensorRT for 30 FPS inference on an NVIDIA Jetson Nano; depth cues from an Intel RealSense camera refine obstacle distance. ASL Translation A 3‑stage pipeline (MediaPipe for hand‑pose landmarks → Transformer encoder → Tacotron‑2 TTS) produces smooth, real‑time captions/voice. Routing Engine OpenStreetMap data enriched with crowdsourced accessibility tags; Dijkstra variant penalizes stair segments and boosts ramp segments. Cloud & App Python FastAPI micro‑services, Firebase auth, React Native front‑end, WebRTC for low‑latency audio/video streaming. Challenges we ran into Pain Point Why it was hard Our fix Noisy ASL predictions Lighting & background shifts tanked model confidence Aggressive data augmentation, frame‑to‑frame smoothing, 0.8 confidence threshold Moving‑object detection on low‑power hardware Cars & cyclists blurred at 30 FPS, Jetson overheated TensorRT acceleration, motion‑priority filter, thermal throttling guard Sparse wheelchair metadata in maps Only 27 % of POIs had ramp tags Built a crowdsourcing flow that awards in‑app points for verified contributions Accomplishments that we're proud of Achieved 93 % top‑1 ASL sign accuracy in the wild, up from 68 % baseline. End‑to‑end latency for obstacle alerts is <200 ms , meeting WHO mobility‑aid guidelines. Piloted with 15 users across three disability groups; 100 % said EyeLink made them feel “more independent.” What we learned Accessibility isn’t a feature toggle—it reshapes every design choice, from color contrast to battery life. Edge‑first AI demands ruthless model optimization yet offers huge privacy and latency wins. Real‑world testing with the community surfaces nuances that lab datasets never capture (e.g., reflective surfaces fooling depth sensors). What's next for EyeLink Hardware integration — snap‑on smart‑glasses module for hands‑free navigation. Multi‑language sign support — extend models to Indian Sign Language, BSL, and more. Live environment crowdsourcing — reward users who report new obstacles or accessible entrances. Partnerships — integrate with transit operators for priority assistance booking and platform‑level accessibility data feeds. With EyeLink, independence is no longer the exception—it’s the default. <div