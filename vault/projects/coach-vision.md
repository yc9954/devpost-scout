---
slug: "coach-vision"
url: "https://devpost.com/software/coach-vision"
title: "Coach Vision"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 520
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Coach Vision

> CoachVision is a real-time indoor cycling command center that centralizes live athlete metrics and uses Logitech’s Actions SDK to enable physical control of performance during coaching sessions.

[Devpost](https://devpost.com/software/coach-vision) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** asp.net-core, c#, css3, d3.js, html5, javascript, react, recharts, signalr, three.js, typescript, webgl, webrtc

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coach vision

## Body

COACHVISION Inspiration As both an endurance athlete and a technology professional, I have experienced how fragmented indoor coaching environments can be. During live remote training sessions, coaches constantly switch between video calls, dashboards, spreadsheets, and analytics platforms. This reduces situational awareness and slows real-time decision-making. I was inspired to create CoachVision to answer a simple but critical question: How can we give coaches faster, more intuitive control over performance data during structured indoor cycling sessions? The idea evolved into transforming the coach’s desk into a real-time performance command center powered by physical interaction through Logitech devices. What it does CoachVision is a real-time indoor cycling performance command center designed for remote coaching. It centralizes live athlete metrics such as: Power output Heart rate Cadence Training zones All athletes are displayed in a unified dashboard optimized for rapid visual scanning. By integrating Logitech’s Actions SDK, coaches can: Instantly switch between athletes Toggle performance views Activate comparison mode Highlight athletes outside prescribed zones Instead of navigating multiple windows, coaches use programmable Logitech controls to manage sessions physically and efficiently. How we built it CoachVision is designed as a real-time web-based platform with three main components: 1. Real-Time Data Simulation We implemented a streaming layer using WebSockets to simulate live cycling metrics for multiple athletes. 2. Unified Dashboard Interface A responsive web UI displays athlete tiles with dynamic graphs and zone indicators. The interface prioritizes clarity and low cognitive load. 3. Logitech Actions SDK Integration The Logitech device acts as a physical command layer. Each programmable action triggers UI state updates such as changing the active athlete or toggling metric overlays. Training intensity zones are dynamically calculated using standard performance ratios: [ Zone = \frac{Current\ Power}{Functional\ Threshold\ Power} ] This enables automatic highlighting when athletes deviate from target ranges. Challenges we ran into One major challenge was designing an interface that balances information density with clarity. Coaches need to monitor multiple athletes simultaneously, but excessive data can reduce effectiveness. Another challenge was ensuring that Logitech integration felt essential rather than decorative. Every hardware action had to meaningfully reduce friction and improve workflow speed. Managing real-time multi-athlete state synchronization was also technically demanding, requiring careful event handling to maintain smooth UI updates. Accomplishments that we're proud of We successfully: Designed a clean, multi-athlete real-time dashboard Implemented live metric streaming simulation Integrated Logitech’s Actions SDK as a physical control layer Created meaningful hardware-to-software mappings that improve coaching workflow Most importantly, we demonstrated how physical interaction can enhance digital performance monitoring. What we learned We learned that in high-performance environments, speed and clarity of interaction are as important as data accuracy. Introducing a programmable physical control layer significantly reduces cognitive load when managing complex live data. We also discovered that thoughtful UX design is critical when building tools for real-time decision-making. What's next for Coach Vision Future development includes: Integration with real smart trainers and wearable APIs Support for structured workout import and session recording AI-driven alerts and performance insights Expansion into structured remote endurance training ecosystems CoachVision represents a new approach to indoor coaching — where real-time performance monitoring becomes intuitive, tactile, and efficient. <div