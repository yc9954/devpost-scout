---
slug: "aside-ai"
url: "https://devpost.com/software/aside-ai"
title: "Aside.ai"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 521
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "substrate/video_visual"
---

# Aside.ai

> It's a wearable narrator AI that watches your day and announces it out loud in any personality you want.

[Devpost](https://devpost.com/software/aside-ai) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[developer_tools]] [[mental_health]]
**substrate** [[video_visual]]

**stack** libjpeg-turbo, python, raspberry-pi, tcp, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aside.ai

## Body

Hardware Inspiration Wearables today either surveil you (cameras, trackers) or quantify you (steps, sleep, heart rate). None of them are fun. We kept joking that everyone deserves "main-character energy" — a narrator who makes your boring Tuesday sound legendary. So we asked: what if a wearable didn't record your life or coach you through it, but performed it back to you in real time? Walk into a room and get announced like a champion. Trip over a chair and hear a goth mommy gently fuss over you. That idea was too funny not to build. What it does Aside is a clip-on camera + mic that watches the world around you and narrates it out loud in real time in a personality you choose. The same moment becomes wildly different depending on the vibe: Hype Man: "AYO they're BACK and they brought the FUEL, let's GOOO!" female therapist: "Look at you, my little raven returning with your potion of warmth." Epic Quest Narrator: "Lo! The hero returns from the Bean Mines, sacred elixir in hand." How we built it Three machines, three jobs: Eyes: Raspberry Pi (QNX): captures camera frames and streams them over Wi-Fi. Brain: Laptop (Python): the orchestrator. It sends each frame to Claude Haiku 4.5 vision, which acts as both eyes and brain — looking at the image and writing one short in-character line in a single call. Deepgram handles speech-to-text (ears) and text-to-speech (voice), and Redis stores memory + which personality is active. Voice: Phone (React Native / Expo): the personality switcher and live feed that plays the narration. Challenges we ran into Our first "eyes" didn't pan out. We planned to use a dedicated vision service; it fell through. We pivoted to sending frames straight to Claude which turned out simpler and better. QNX is unforgiving. MediaPipe (our planned on-device detector) doesn't build on QNX, and writing native C++ camera capture was slow. We found a pragmatic path using QNX's built-in viewfinder + screenshot tools to grab JPEGs from Python. Accomplishments that we're proud of It actually works end-to-end, live: Pi camera → laptop → Claude → voice → phone, in ~1–2 seconds. The narration is genuinely funny and stays in character — and the voice changes with the personality. Swappable personalities on the fly, with the AI remembering and calling back to earlier moments. We turned a stack of "this doesn't work on QNX" problems into a clean, modular system and shipped real engineering (change-gating, color correction, a custom Pi↔laptop protocol) under hackathon time pressure. What we learned Split capture from compute. Letting the Pi just see and the laptop think sidestepped a mountain of embedded/cloud-SDK pain. Modern vision models can be eyes and brain collapsing "detect the scene" and "describe it" into one call removed an entire service. Fix the input, not the output. Color-correcting the camera beat any amount of "please don't say fluorescent" prompting. For hardware demos, the network is the hardest part not the AI. A lot about prompt-engineering personality and comedic timing getting an AI to be funny and know when to stay quiet. What's next for Aside.ai Greatness <div