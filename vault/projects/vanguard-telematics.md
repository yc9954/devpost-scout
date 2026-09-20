---
slug: "vanguard-telematics"
url: "https://devpost.com/software/vanguard-telematics"
title: "Vanguard Telematics"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1091
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Vanguard Telematics

> Fire truck crash? Radio too slow. Rescuers in danger!We build smart tech. Fast sensors feel crash right now. Save the savers fast!

[Devpost](https://devpost.com/software/vanguard-telematics) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[education]] [[health_clinical]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** deepgram, fastapi, framer-motion, motionfx, openai, python, qnx, raspberry-pi-5, react, recharts, redis, stm32-(nucleo-f401re), stmicroelectronics-iks5a1, three.js-(react-three-fiber/drei)

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

telemetrics dashboard redis stream architecture diagram agentverse agents GitHub Link: https://github.com/bencejdanko/VanguardTelematics Public ASI:One Shared Chat Link: https://asi1.ai/invite?channelInviteKey=EUZbyUu8nbYVK2xhekQN3EtGY60i_5mh0dGM9UuKV7I https://asi1.ai/invite?channelInviteKey=5Mb2Ov6_U4rAzxkd5rPNcIdd2zxD5tkx_E99IssFui4 Agentverse Profile: https://agentverse.ai/agents/details/agent1q05xhz7crc75lwt84v0u78mt2lswwr2a7n0wntp0zpuyedum80m3qwm4rnu/profile https://agentverse.ai/agents/details/agent1qgsr563q7gy2y97s4wp8rp3hjw3979xhcdjpnzu3f2vmf4c8pda0jkgsdsv/profile https://agentverse.ai/agents/details/agent1q0sfkv77ye39d8ctsj6rxgzapmulas4lx0ygd8ek2lxuw2ks3p3659kj04g/profile Inspiration 82% of U.S. fire departments are all- or mostly-volunteer. Together they protect roughly 30% of the U.S. population — about 100 million people — concentrated in exactly the rural, lower-density areas where cell and radio coverage is weakest. Federal studies have found that communications outages hit within the first 24 hours in more than half of recent major U.S. wildfires. That gap is already being worked on, but not solved. FirstNet is the dominant public-safety connectivity platform and is investing in satellite extension and deployable cell sites — but those are ground-based assets an agency has to request , not something that rides on every truck by default. goTenna Pro/Pro X is real, proven off-grid mesh tech already used by humanitarian responders and law enforcement — it relays a message; it doesn't sense or diagnose anything on its own. We kept circling back to the same question: what happens in the minutes after an incident, before anyone has even picked up a radio? A vehicle that can sense and describe what just happened to it — without needing a human to triage it first — felt like a real, underserved piece of the problem. What it does Our project watches a vehicle's vitals in real time — accelerometer, vibration, temperature, and pressure from an industrial sensor rig, plus a proximity sensor and a camera that feeds live video the moment something gets too close. All of it streams into a live dashboard with a 3D model of the vehicle (we used a model Cybertruck) that visually reacts to the incoming data, so a human can see exactly what the truck is "feeling" at any moment. Underneath that, a custom Fetch.ai multi-agent system watches the same streams and decides, on its own, when something anomalous has actually happened — then generates a free-text, situation-specific description of the event instead of picking from a small, hardcoded list of crash types. The same pipeline is meant to generalize across first-responder vehicle types — an ambulance and a fire engine have very different normal operating signatures, and the system is built to account for that rather than assume one vehicle profile. How we built it On the hardware side: an industrial Nucleo sensor rig feeding accelerometer, vibration, temperature, and pressure data, plus a proximity sensor and camera, all running on a Raspberry Pi 5 under QNX — a real-time OS providing first responders reliability they need. Hence, event detection stays low-latency and deterministic instead of fighting a general-purpose scheduler. Redis sits behind everything as the live telemetry store both the dashboard and the agent pipeline read from. The crash-detection brain is a layered Fetch.ai (uAgents) pipeline. Since we didn't have a pre-built "sentry" crash-detection signal to lean on, the trigger agent had to derive one itself: it keeps a rolling, per-vehicle baseline (mean and standard deviation) for each sensor feature and computes a z-score, $$ z = \frac{x - \mu}{\sigma} $$ flagging an event only when multiple sensors cross threshold together, for several consecutive samples — which filters out single-sensor noise like a pothole or a slammed door while still catching real multi-sensor anomalies. That trigger hands a buffered pre/post-event window to downstream agents, which extract physics features, pull context for the specific vehicle, and feed an LLM-grounded synthesis step that writes an open-ended incident description rather than forcing the event into one of a few fixed categories. Challenges we ran into We originally wanted true off-grid relay — in the spirit of what goTenna does for mesh comms — so the system could report out even with no cell or wifi coverage. We tried wiring a radio link to the Pi 5 and hit a wall on two fronts at once: regulatory limits on unlicensed RF transmission, and practical RF interference that made it unreliable to get clean text through to and from the board. We made the call to descope it for the weekend and treat it as the natural next step rather than a hackathon deliverable. The other real challenge was the crash detector itself. Without an existing crash-detection signal to wrap, we had to build trigger logic from raw sensor physics — and do it in a way that wouldn't quietly bake in assumptions about one specific vehicle or one specific kind of accident. Getting a rolling baseline that adapts per vehicle, instead of a single hardcoded threshold, took more iteration than we expected, especially separating real signal from sensor noise without throwing away genuine events. Accomplishments that we're proud of Building a dashboard visualizer that showed us our data is realistic and reliable to actually generate meaningful analytics from. Getting real sensor hardware talking to a real-time OS on actual embedded hardware, end to end, in a weekend. Building an anomaly detector from first principles — rolling baselines and multi-sensor z-scores — instead of a hardcoded if/else crash classifier, paired with a reasoning layer that produces open-ended, vehicle-specific incident descriptions instead of forcing every event into one of three canned labels. And doing the homework before writing code: we went in with real numbers on who this actually affects and a clear-eyed, so we knew what gap we were actually trying to close. What we learned Radio is a much harder problem than "just send a signal" — between licensing and interference, it's a real compliance and RF-engineering problem, not a wiring exercise you can finish in a weekend. We also learned that you can't shortcut crash detection with a single magic threshold number if you actually care about it generalizing across vehicles — you have to understand what a real anomaly looks like across multiple sensors at once, which pushed us toward a statistically grounded approach instead of guessed constants. And splitting the pipeline into agents — deterministic, testable signal processing in one layer, open-ended LLM reasoning in another — made the whole system much easier to debug than one big classifier would have been. What's next Solving off-grid relay properly — likely by pairing with certified mesh hardware like goTenna rather than rolling raw radio from scratch, so we're not fighting licensing and interference ourselves. Real-world impact and drop testing across more vehicle types (ambulance, fire engine) to calibrate the rolling baselines per vehicle class instead of relying on bench simulation. And closing the loop with multi-agent system to gain more meaningful analytics to aide second responders, and inform authorities of the disaster. <div