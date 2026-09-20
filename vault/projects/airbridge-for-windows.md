---
slug: "airbridge-for-windows"
url: "https://devpost.com/software/airbridge-for-windows"
title: "AirBridge for Windows"
hackathon: "OpenAI Build Week"
organization: "OpenAI"
winner: true
words: 550
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "user/government_staff"
  - "substrate/geospatial"
---

# AirBridge for Windows

> AirBridge turns an AirPlay-compatible speaker into a practical wireless audio output for a Windows PC and puts a GPT-5.6 agent in the control loop.

[Devpost](https://devpost.com/software/airbridge-for-windows) · hackathon [[OpenAI Build Week]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[realtime_stream]] [[structural_withholding]] [[voice_speech]]
**user** [[government_staff]]
**substrate** [[geospatial]]

**stack** .net, airplay, apple-tv, audio-streaming, c#, chrome, codex, firefox-extension, gpt-4o-transcribe, gpt-5.6, homepod, javascript, multi-room-audio, naudio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- what i learned

## Body

AirBridge for Windows Windows has never spoken AirPlay. AirBridge teaches it — live system audio straight to HomePods, Apple TVs, and Macs. No virtual audio cable, no temp files. Inspiration My PC and my HomePods sit in the same room and can't talk to each other. macOS gets AirPlay natively; Windows gets nothing but hacks that route audio through virtual cables or hijack your default output. I wanted the thing Apple never shipped: click a speaker in the tray, and whatever your PC is playing comes out of it. What it does AirBridge captures the live Windows system mix (or a single app), normalizes it to 44.1 kHz stereo PCM, and streams it to one or more AirPlay receivers — each with its own session and volume, controlled from a tray flyout. On top of that: multi-speaker playback with acoustic delay calibration, silence standby that frees the speakers when you're done, a browser extension that fixes video lip sync by delaying only the picture , and an optional GPT-5.6 voice assistant ("airplay to the kitchen speaker") with a local policy layer and a real-time activity inspector. How I built it Built during OpenAI Build Week with Codex as the primary implementation partner, across three runtimes: C#/.NET 9 (WASAPI capture, tray UI, policy layer), Python (the RAOP host), and JavaScript (the browser extension). The core trick: pyatv's RAOP support expects a finite media file. Codex traced its internals to find the seam where a permanently open, file-free AudioSource could be injected — so live PCM flows from WASAPI to the speaker entirely in memory. For multi-room, one shared pump sends 20 ms blocks to every receiver on a single sender clock, with a readiness gate that bounds start skew to one block. Receivers add latency RAOP never reports, so AirBridge measures it with five chirps through your actual room and mic; each faster speaker gets a silent trim of $$\text{trim}_i = \max_j d_j - d_i$$ where each speaker's d is its median measured delay — so every leg stays on one sender clock. The assistant runs GPT-5.6 on the Responses API with strict JSON-schema tools. A local allowlist classifies every call (read-only / reversible / needs-confirmation / forbidden), fixes are verified against real underrun counters, and the model never sees raw audio or network details. Challenges The calibration feedback loop. Early calibration re-captured its own chirps through the loopback path, corrupting the measurement. Fix: synthetic chirp blocks replace capture blocks at exactly 1× rate on the sender clock. Multi-room without Apple's clock. AirPlay 2 uses a shared PTP clock; a Windows sender gets none of that. I shipped an honest model — anchor-aligned starts plus measured trims — and say plainly it isn't AirPlay 2 sync. Lip sync can't be fixed on the audio side. Pausing a video delays the captured audio too. The inversion — leave audio alone, delay only the rendered frames — then had to survive seeks, fullscreen, SPA navigation, and DRM. What I learned Measure what protocols won't tell you — a microphone recovers latency that RAOP hides. Bound every buffer, or "slightly behind" becomes "thirty seconds behind." And an LLM near real hardware needs a policy layer it can't argue with: local enforcement plus deterministic verification is what made handing GPT-5.6 the controls feel safe. <div