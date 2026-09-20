---
slug: "ergolearn-e6mf3x"
url: "https://devpost.com/software/ergolearn-e6mf3x"
title: "Ergolearn"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 993
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Ergolearn

> ErgoLearn AI turns standard webcams into local 3D biomechanical sensors for all. Built on Tauri + Python, it tracks slouching, asymmetry, and screen distance via edge AI, keeping data 100% private.

[Devpost](https://devpost.com/software/ergolearn-e6mf3x) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** python, tuari

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ergolearn

## Body

Inspiration As a student and software developer, I spend upwards of 8 to 10 hours a day glued to my laptop screen, hunched over lines of code and technical text. Over time, I noticed recurring shoulder fatigue, a stiff neck, and a massive drop in my mental focus during long study blocks. When I looked at existing posture tracking apps on the market, I realized they all shared the same major flaws: they were either massive resource hogs that drained laptop batteries, or they required streaming raw webcam feeds to external cloud servers. For a workspace utility, that felt like an unnecessary privacy violation. I wanted to build a solution that treated my camera as a fully localized, private biomechanical sensor—giving me deep workspace wellness insights without sacrificing my data or melting my computer's CPU. What it does ErgoLearn AI converts a standard 2D laptop webcam into a real-time, privacy-first, edge-computing biomechanical sensor suite. Operating completely offline, it strips out and deletes raw camera pixel streams to protect user privacy, projecting a minimalist 3D vector wireframe skeleton onto a clean, non-glaring Matte Obsidian grid canvas. The application tracks vertical spine compression (Slouching), shoulder plane alignment errors (Lateral Asymmetry), and uses real-time interpupillary distance mapping to calculate the exact distance between the user's face and the monitor in centimeters. These data pipelines feed a highly responsive 10-second rolling Concentration Index sparkline chart. Additionally, the app features an integrated AI Coach panel that acts as an interactive workspace wellness companion, providing contextual posture advice and stretches based on real session logs. How we built it I architected ErgoLearn AI using a lightweight, decoupled multi-process stack to keep its runtime footprint as tiny as possible. The Frontend Interface: Built using standard HTML5, CSS3, and vanilla JavaScript styled with a flat, sophisticated matte slate and ink aesthetic. I wrapped the interface using Tauri , which compiles directly into the operating system's native web rendering engines (WebKit on macOS / WebView2 on Windows) instead of bundling a heavy browser core like Electron does. This keeps the frontend shell framework under a tiny 20 MB container footprint. The AI Sidecar Backend: A local background Python process managed natively by Tauri that ingests local hardware camera frames and passes them through an optimized MediaPipe skeletal pipeline. The IPC Bridge: The frontend interface and Python backend communicate locally via a high-speed, secure loopback WebSocket connection ( ws://localhost:8765 ) running at up to 30 frames per second. Every frame is processed using localized vector geometry to create anatomical invariants, meaning the math scales automatically even if the user moves around. For example, vertical spine collapse is checked by calculating a normalized Slouch Fraction : $$\text{Neck Ratio} = \frac{y_{\text{shoulder}} - y_{\text{ear}}}{w_{\text{shoulder}}}$$ $$\text{Slouch Fraction} = \frac{\text{Neck Ratio} {\text{current}}}{\text{Neck Ratio} {\text{calibrated}}}$$ By dividing the vertical distance between the ear and shoulder midpoints by the overall 3D shoulder width ($w_{\text{shoulder}}$), the equation ensures that sitting slightly closer or further away from the lens never breaks the calculation accuracy. Challenges we ran into Building a multi-language app that spans JavaScript, Rust, and Python brought up some real engineering hurdles: The Tab-Throttling Lag: Early on, when I switched away from the app to type code in another window, the OS would automatically throttle the background frontend JavaScript animation loops. The WebSocket packets from the Python backend would back up in the network buffer. Switching back to the app triggered a crazy, fast-forward "replay" lag. I solved this by stamping millisecond UTC timestamps on the backend data packets, forcing the frontend to immediately drop any frame older than 200ms upon waking up. Notification Fatigue: Posture apps can get incredibly annoying if they trigger alerts too quickly. If a developer leans forward for a single second to analyze a complex line of code, they don't want a loud alarm. I had to design a custom Hysteresis state machine with a 30-second continuous failure buffer and a strict 60-second cooldown timer so the app remains a silent, helpful companion rather than a constant desktop distraction. Hardware Constraints: I initially intended to track eye blinking using Eye Aspect Ratio (EAR) maps to prevent dry eyes, but real-world testing proved that standard laptop webcams at normal screen distances ($50\text{--}70\text{ cm}$) are simply too low-resolution for reliable blink data. Rather than shipping a glitchy feature, I made the engineering call to strip out the blink code entirely and focus heavily on rock-solid 3D skeletal posture layout tracking. Accomplishments that we're proud of I am incredibly proud of creating a cross-platform machine learning app that values user privacy above everything else. Successfully implementing the pinhole camera approximation formula using the pixel delta between landmarks 468 and 473 (the center of human irises) allowed us to calculate absolute screen proximity in centimeters without forcing the user to own expensive depth cameras or LiDAR hardware. Additionally, re-engineering our Concentration Index from a sluggish 60-second moving average down to a responsive 10-second window means the data visualization reacts to sudden fatigue drops smoothly and dynamically in under two seconds. What we learned This project completely shifted how I approach systems architecture. It taught me that building software with AI components doesn't mean you have to plug everything into expensive, cloud-hosted API endpoints that compromise user data. By leveraging highly optimized edge frameworks, local WebSockets, and on-device logic routines, you can build incredibly robust, low-latency, and highly secure software that runs completely on your own machine. What's next for Ergolearn The immediate next step for ErgoLearn AI is expanding our conversational ecosystem. Our current AI Coach features a dual-tiered architecture that targets a local Ollama instance (running an optimized, quantized LLM model) or falls back to an offline rule-based NLP parser that reads the local posture_history.json logs when Ollama is closed. I want to build out custom, interactive desktop stretch routines where the neon 3D skeleton actively guides the user through shoulder rolls and cervical stretches, updating the UI in real-time as they complete each physical movement correctly. <div