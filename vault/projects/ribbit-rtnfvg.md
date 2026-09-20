---
slug: "ribbit-rtnfvg"
url: "https://devpost.com/software/ribbit-rtnfvg"
title: "Omniscient"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 722
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/transportation"
  - "substrate/video_visual"
---

# Omniscient

> Supervision layer for robot fleets. A VLM watches each robot against its task and flags failures the second they happen; the operator pilots from anywhere via real-time hand tracking.

[Devpost](https://devpost.com/software/ribbit-rtnfvg) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: deterministic_policy</sub>
**domain** [[health_clinical]] [[transportation]]
  <sub>weak: labor_employment, supply_logistics</sub>
**substrate** [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** act, antropicstructuredoutput, claude, depthanythingv2, esp32, espidf, fastapi, lerobot, mediapipe, pca9685, piperx, pydantic, python, three.js

## Body

Title Slide Hard at work tuning the Media Pipe to Piperx flow Robot hand we built (horns up!) At Ace hardware making the rig Zedx cam attachment piece we designed to connect to tripod Rig setup ACT we trained collecting filament spools and putting it into a box robot fleet management we developed (close up zoomed) Full view of robot fleet management system Inspiration Robots are entering factories, warehouses, and lines everywhere, but no robot is ever 100% reliable. They fail on edge cases nobody prepared them for. Today that means a stopped line and a human running over with a controller, which collapses the moment you have more than a handful of robots. We built the layer that catches those failures, lets one human fix any robot from anywhere, and captures the data that can prevent the next one. What it does Omniscient supervises a fleet of autonomous robots and keeps one operator in control of all of them. The loop: robots run their tasks on the line. Omniscient samples each robot's camera frames and sends them to a VLM along with that robot's predetermined task goal, asking in real time, is this task being done correctly? When the answer is no, the robot is flagged in the fleet dashboard with a diagnosis, before any human noticed. The operator clicks in and takes over the failing robot from hundreds of miles away, driving its arm with their bare hands via real-time hand tracking with depth perception. They fix it, hand control back, and the robot resumes autonomy. Every takeover, the failure frames plus the human correction, is captured, and that data can be fed back to improve the policies that failed. How we built it Control plane: a FastAPI WebSocket hub with a pure state machine (AUTO → ALERT → MANUAL → AUTO) as the single source of truth. Every cross-process message is a typed Pydantic schema in one file, so four people built in parallel with zero integration drift. Supervision layer: a two-tier VLM watchdog. A fast, cheap model checks every frame against the task goal as an always-on gate; only when it flags a failure does a stronger model run a full diagnosis, structured JSON, parses every time. You pay for the expensive model only when a robot actually breaks. Teleop: real-time hand tracking off a webcam, with depth-perception algorithms recovering the hand's position in 3D space, not just a flat 2D plane. That maps five finger closures and hand pose onto a custom ESP32 five-servo hand we built from scratch. The host sends the tracked motion; the firmware owns all safety (calibrated ranges, slew limiting, auto-relax on signal loss). Data: each takeover logs the failure frames, the task goal, and the human correction, an edge case that can be fed back into policy retraining. The full failure→flag→takeover→recovery loop runs headlessly with 22 passing tests, no hardware or API key required. Challenges we ran into Splitting latency: teleop needs near-instant response while VLM supervision tolerates ~1s, so we ran them as two separate loops sharing no resources. Keeping VLM cost proportional to failures, not frame rate, drove the two-tier design. Recovering reliable 3D hand position from a webcam took real work on the depth-perception side. And building a working five-servo hand with real safety in 24 hours, after burning out one servo early. Accomplishments that we're proud of A full autonomous → VLM-flagged failure → human hand-takeover → recovery loop, running end to end and verified in CI. A physical five-finger hand that mirrors an operator's webcam hand live, with depth-aware tracking. And a system that captures exactly the edge-case data a robotics team would want, the moments their robots fail. What we learned Contract-first development is the only way to parallelize hardware and software on a 24-hour clock. And the right use of AI here isn't "AI does everything", it's a cheap model for always-on watching, a strong model for diagnosis, and a human for physical judgment. What's next for Omniscient Close the data loop, feed captured failures and corrections back into policy retraining automatically. Upgrade to a stereo-depth camera (ZED-class) for full 6-DOF wrist pose. Scale the supervision so one operator runs an entire line, that 1-to-many ratio is the commercial story. Omniscient is the deploy-and-recover infrastructure for a world running on robots that almost work. <div