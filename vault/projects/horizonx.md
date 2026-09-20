---
slug: "horizonx"
url: "https://devpost.com/software/horizonx"
title: "HorizonX"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 637
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# HorizonX

> HorizonX is a dual-purpose platform using !!on-device!! VLMs to empower blind people with real-time haptic guider while crowdsourcing anonymized data to help governments improve public safety.

[Devpost](https://devpost.com/software/horizonx) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[civic_government]] [[disaster_emergency]]
**user** [[general_public]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]]

**stack** docker, javascript, nextjs, python, pytorch, react, webgpu

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for horizonx
- tesla challenge

## Body

Theme Background UI - User UI - Government Inspo Inspiration GPT 4o sucks!! It is built for the visually impaired, but only with wifi!! Inspired by the potential of Video Language Models (VLMs) , we hope to bridge accessibility gaps. Over 2.2 billion people globally live with vision impairments, we built HorizonX an AI camera, a privacy-first real-time "sight partner" on mobile phone that help the blind individuals navigate crowded places. At the same time, our AI allows people to report hazards (potholes, broken signage) to government simultaneously improving public spaces for everyone, which facilitate government's reconstruction efficiency and transparency. What it does HorizonX is a two-part ecosystem: For User - Mobile App for Visually Impaired Users: Narrates surroundings in real time via camera (e.g., “A cyclist approaching from your left”). Guides navigation with obstacle detection and step-by-step audio cues. Reads text aloud (menus, signs, currency) and identifies products. For Governments - Centralized Platform for Public Safety Aggregates anonymized data from users to map hazards (potholes, broken signage) and crowds. Provides dashboards for infrastructure planning and emergency response. How we built it Running a VLM on a mobile device is a hefty task. After trying multiple approaches with MLX and WebGPU, we failed over and over to overcome the bandwidth and memory limits of our phones. We found a way to run a Linux emulator on the Galaxy S24 and mount it to local images, then installing core pytorch and tokenization libraries in a python environment to host a streaming API. We have a local endpoint hosted on the network to send the anonymized reported descriptions on a live map. This map also has information sourced from Sonar Research Pro calls to source live citizen complaints and create a centralized view. All of this is brought together with our locally hosted app, which—without connection—can navigate individuals around complex areas. Challenges we ran into Extreamly difficulty system integration MLX development of moondream in swift running moondream library: couldn’t install onnxruntime on Termux on Android finding smaller vlms: Moondream2B is by far the smallest model (other than Moondream0.5B) tried translating Moondream0.5B from custom ONNXVL wrapper to ONNX to Torch to serve directly from local safetensor, but would have to rewrite KV caching twice and serve custom KV caching also tried webGPU or running from browser, but don’t have enough RAM on Safari to do inference Accomplishments that we're proud of Getting a multi-billion sized VLM to run on a mobile device! This is a significant milestone in local-first and privacy-focused AI inference. Since mostly it's impossible to run a 2B model on mobile phones. What we learned Vim on a phone is easier than on a laptop What's next for HorizonX Speed up model on edge devices by further quantization or better integration with the current software. And provide more humanistic service to the special community and better verification experience for government. Tesla Challenge Also, we participated in Tesla Challenge, here's our statement: 1) inspiration Combine LLMs and CV could combine to provide richer insights than traditional image-processing pipelines alone. By leveraging GPT-based models, we hoped to produce human-like, context-aware answers to driving-related questions, going beyond standard object detection or classification tasks. 2) code https://github.com/bsflll/treehack2025/tree/main/tesla-real-world-video-q-a 3) methodology Data: We sample frames at fixed intervals from short driving videos—here, five frames from a nominal 5-second clip. This approach provides a concise but representative snapshot of each scenario. Prompt: Descriptive Prompt by GPT-4o: Generates high-level contextual awareness of each video. Expert Opinions (Model “o1”): Requests multiple “expert answers” in parallel (e.g., five completions) to encourage diverse perspectives. Consolidation (Model “o1” / Final Step): Summarizes or decides on the best single answer. Minimal Answer Extraction: Ensures only the final letter (choice) is returned for submission or scoring. Asynchronous Execution Failure check at the end: 4) kaggle links Submission by Zian Shi <div