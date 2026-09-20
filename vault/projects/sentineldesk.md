---
slug: "sentineldesk"
url: "https://devpost.com/software/sentineldesk"
title: "SentinelDesk (Phase1)"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 1348
team_size: 0
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/general_public"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SentinelDesk (Phase1)

> SentinelDesk turns MX Creative Console & Master 4 into a tactile CCTV cockpit. Scrub footage with the dial, feel AI alerts via haptics, and switch cameras instantly.

[Devpost](https://devpost.com/software/sentineldesk) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[health_clinical]] [[supply_logistics]] [[transportation]]
**user** [[general_public]] [[small_business]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** .net, actions-ring, c#, docker, fastapi, ffmpeg, frigate-nvr, haptic-feedback, hls-streaming, logitech-actions-sdk, mosquitto, mqtt, mx-creative-console, mx-master-4

## How they structured the write-up

- inspiration
- what it does
- how we plan to build it
- design challenges we're exploring
- what makes this unique
- what we learned
- what's next for sentineldesk

## Body

Inspiration My cycle was lost in our society's parking lot. Our residential complex has 50 flats and 16 CCTV cameras surrounding the building. When the incident happened, I — just a regular resident — spent 2 hours of frustrated clicking alongside the building manager: overshooting timestamps, losing our position when switching between the 16 cameras, and squinting at a tiny timeline bar — just to find a 30-second clip. Our building uses a standard NVR system. It has playback, speed controls, and multi-camera views. But every action requires precise mouse clicks on a tiny timeline bar, navigating through menus, and staring continuously at screens for hours. We overshot the timestamp dozens of times and clicked through hundreds of frames one by one — trying to read the number plate of the suspect's vehicle in the moment the cycle left the parking area. This is the reality for millions of people who own cameras but only touch the NVR software once something goes wrong — a residential society member, a school principal, a shop owner, a small business manager. They aren't professional CCTV operators. They are ordinary people who need to find a moment in hours of footage, fast, under stress, after something already happened. Research confirms the scale of this challenge — security operators miss an estimated ~95% of events after just 22 minutes of continuous monitoring, a finding repeatedly cited by the surveillance industry in 2025 (fortixai.com; intelexvision.com; mycontrolroom.com). ~73% of organizations cite false positives as their #1 detection challenge — up from previous years and still climbing (2025 SANS Detection & Response Survey). And not a single product in the global video surveillance market — estimated at $62–85B in 2026 across multiple research firms — offers physical, tactile controls to make forensic footage review fast and intuitive. Video editors have had jog wheels for decades. Security camera owners have nothing. I looked at the Logitech MX hardware and realized: this problem was designed for this hardware. What it does SentinelDesk is a proposed Logitech Actions SDK plugin that transforms the MX ecosystem into a tactile surveillance control surface for Frigate NVR — designed for anyone who owns cameras and needs to review footage quickly after an incident. Target users — anyone who owns cameras and needs to review footage: 🏠 Home & residential owners — reviewing incidents at their property, apartment complex, or gated community 🏪 Retail & hospitality — shop owners, restaurants, hotels reviewing footage after incidents during or after hours 🏫 Institutions — schools, hospitals, offices managing multi-camera setups without a dedicated security team 🏢 Small & medium businesses — warehouses, factories, co-working spaces wanting situational awareness 🚗 Parking & fleet operators — monitoring vehicle access, tracking incidents across outdoor camera grids 💻 Homelab & privacy-first users — self-hosting Frigate instead of cloud camera services 🔒 Security consultants — professionals who set up and review NVR systems for clients 🎛️ MX Creative Console — The Command Surface Dial = Timeline Scrubber : Rotate slowly for frame-by-frame precision. Rotate fast to skim hours. Analog control that's physically impossible with discrete 1x/2x/4x speed buttons on a screen LCD Keys = Camera Rack : Up to 9 LCD buttons can each show a live camera thumbnail . One press switches cameras — keeping you at the same moment in time, zero context loss Dial Press = Next AI Event : Press the dial to jump directly to the next person/vehicle detection. Skip hours of empty footage in seconds 🖱️ MX Master 4 — The Awareness Layer Existing NVR alerts are all screen-and-phone-based: a notification badge you can swipe away, an app alert you silence along with 50 others. None of them reach you when your hands are busy and your eyes are elsewhere. The MX Master 4 can close this gap: Haptic Event Alerts : When Frigate's AI detects a person, the mouse buzzes in your hand — different vibration patterns for different events (person vs. vehicle vs. zone violation). Eyes-free awareness Haptic Timeline Markers : While scrubbing through recorded footage with the dial, the mouse provides tactile feedback at every AI event — you feel where incidents are in time, without looking at the screen Scroll Wheel = Event Triage : The scroll wheel can jump between AI-detected events for fast review without touching the keyboard 🔄 Actions Ring — The Mode Controller The Actions Ring is an on-screen radial overlay invoked by the MX Master 4 thumb button. SentinelDesk proposes using it as a mode switcher and camera selector : Hold thumb button → ring appears. Rotate to choose: Review Mode , Live View , PTZ Mode , Zone Arm/Disarm Camera jump : rotate to a camera name on the ring, press to switch — staying at the same moment in time across all camera angles How we plan to build it We chose Frigate NVR as the backend because, unlike proprietary CCTV systems (Hikvision, Dahua, CPPlus) that lock down their APIs, Frigate is fully open-source with a REST API and real-time MQTT events — making a deep Logitech hardware integration possible. Frigate NVR (Docker, local) → REST API + MQTT events ↓ SentinelDesk Plugin (C#, Logitech Actions SDK) ↓ MX Creative Console + MX Master 4 + Actions Ring The plugin will use: Logitech Actions SDK (C#) to receive dial rotation events, render camera thumbnails on LCD keys, trigger haptic feedback, and manage Actions Ring states Frigate's REST API to fetch live camera snapshots and recorded footage Frigate's MQTT events to receive real-time AI detections and trigger haptic alerts on the MX Master 4 We have already set up a working Frigate NVR instance with 5 cameras using real CCTV footage (VIRAT surveillance dataset), running local AI detection for person, vehicle, and motorcycle — which we use to validate the pain points and demonstrate the problem space. Design challenges we're exploring A haptic language for surveillance: How to map different event types to distinct vibration patterns that users can learn intuitively — person vs. vehicle vs. zone violation — so the mouse becomes a data channel, not just a generic buzzer Timestamp preservation across cameras: When you switch from entrance_cam to parking_cam, the playback position must stay at the same moment in time . Even a 1-second drift during a fast-moving incident means missing the moment Making dial scrubbing feel natural: Mapping analog dial rotation to digital timeline seeking — slow rotation for frame-by-frame precision, fast rotation for skimming hours — requires careful velocity scaling to feel right What makes this unique First surveillance plugin proposed for Logitech Marketplace. As of Feb 2026, zero of ~47 existing plugins target security or cameras. This opens an entirely new category for Logitech hardware. A real story, not a hypothetical. The cycle loss actually happened. The 2-hour review actually occurred. Real Frigate NVR screenshots document the pain. This is a real problem that millions of people experience. Haptic timeline markers — a novel concept. No hardware or software — surveillance or otherwise — currently uses haptic feedback to communicate position in time during scrubbing. Feeling where events are, without looking at a screen, is genuinely new. What we learned Haptics can be a data channel, not just an alert. The idea of mapping event timestamps to tactile clicks during scrubbing could transform the mouse into a timeline sensor — communicating where in time events occur, not just that something happened. The UX problem is access, not features. Frigate already has playback, AI events, and filtering. Nothing is missing functionally. The gap is that every feature requires mouse clicks and menus. Physical controls can democratize access to tools that already exist. What's next for SentinelDesk Phase 2 Build (by April 1): Working C# Actions SDK plugin with dial timeline scrubbing, camera switching on LCD keys, and MQTT-based haptic alerts Logitech Marketplace Launch: Freemium — Free (2 cameras, basic scrubbing) → Pro at ~$1.99/month (all cameras + AI haptics + event triage) → Team at ~$4.99/month (multi-user + audit export). Priced for global accessibility Multi-NVR Support: Expand beyond Frigate to any ONVIF-compatible camera system, broadening the addressable market <div