---
slug: "dispatch-u7fwrv"
url: "https://devpost.com/software/dispatch-u7fwrv"
title: "Dispatch"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 437
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
---

# Dispatch

> A novel VR locomotion solution to provide accessible immersive training experiences for first responders

[Devpost](https://devpost.com/software/dispatch-u7fwrv) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[disaster_emergency]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]]

**stack** c#, c++, platformio, python, steamvr, unity

## How they structured the write-up

- inspiration:
- what it does:
- how we built it:
- challenges we ran into:
- accomplishments that we're proud of:
- what we learned:
- what's next for dispatch:

## Body

Inspiration: First responders need rapid, realistic training that prepares them for high-stress, unpredictable environments. Traditional VR training systems often rely on treadmills, fixed setups, or limited forward-only movement. This restricts realism, especially in high-stakes scenarios like navigating burning buildings. We built Dispatch — a VR training experience that uses motion sensors and natural locomotion to prepare first responders for high-stress, life-or-death scenarios inside a burning building. Dispatch enables cost-effective, at-home, or on-site VR training for firefighters, EMTs, and rescue teams improving accessibility. Research shows the need: Arxiv 2301.13124 & 2410.14140 : Highlight VR’s role in scalable first responder training. FIT 2023 Firefighter Study : Demonstrates that firefighters can use VR for drills outside of costly in-person sessions. What it does: Dispatch offers a VR training scenario inside a maze-like burning building where: Novel locomotion : instead of using a physical joystick, your body becomes the joystick. By walking/running in place the system estimates your speed and direction. Dynamic environment : Fires spread over time — starting with smoke, then flames, with sounds of cracking beams and obstacles. Sensory immersion : Players hear fire grow louder and victims cry for help as they get closer. Objectives : Rescue dummies trapped in rooms (randomized each round), make rapid situational decisions, and escape. HUD stats : Track maze progress, survival time, and decisions. Fail state : Screen fades to black with heartbeat and heavy breathing audio, mimicking collapse. How we built it: Unity + C# for maze creation, particle effects, colliders, and VR setup. SteamVR/OpenVR Driver in C++ for integrating with external hardware PlatformIO in C++ for firmware to read IMU data and communicate wirelessly 3D printed tracker casings and velcro straps for customizable wearability (we made trackers for the chest and both knees but only used the chest one) Challenges we ran into: Communication between microcontroller and SteamVR was difficult to implement Balancing realism with hackathon time constraints (e.g., scalable maze vs. simple proof-of-concept). Accomplishments that we're proud of: Building a functional VR demo in just a hackathon sprint. Creating a locomotion system that can scale beyond first responder training — potentially into gaming, rehab, and VR fitness. Combining research-backed needs with a practical, lightweight prototype. What we learned: Simple and working is better than complicated and not working Never give up What's next for Dispatch: Better gait analysis with knee and foot trackers Physiological tracking (heart rate to gauge stress) Expand to adaptive training programs with different dififculty levels AI/LLM feedback on performance — e.g., highlighting weak spots like hesitation or poor route choice Pilot with first responder groups to validate effectiveness view our pitch here: https://www.canva.com/design/DAG0O43r9ug/YQv7im-jHmJN4KTk9l8Tmw/view?utm_content=DAG0O43r9ug&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hc58c1f20c6 <div