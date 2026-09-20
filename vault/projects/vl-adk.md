---
slug: "vl-adk"
url: "https://devpost.com/software/vl-adk"
title: "VL-ADK"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 395
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/video_visual"
---

# VL-ADK

> A "psuedo" VLA model leveraging a fleet of autonomous ADK agents.

[Devpost](https://devpost.com/software/vl-adk) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]] [[transportation]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** gemini, google-adk, jetson-orin, python, react, typescript, yolo

## How they structured the write-up

- 💡 inspiration
- 🕹️ what it does
- 💻 how we built it
- ‼️ challenges we ran into
- 🏆. accomplishments that we're proud of
- 🦾 what we learned
- 🤖 what's next for vl-adk

## Body

Logo Console 💡 Inspiration Over the past few months, agents have taken the world by storm - in the digital space as software agents, and now in the physical space as embodied intelligence. We wanted to get our hands dirty and earn the capabilities of combining the two, with a fleet of software agents piloting their physical agent vessel. 🕹️ What it Does A robot, a control panel, and a group of Google ADK AI agents controlling its every move. Ask the agents to find something, guide you, or just make you laugh. The Director, Pilot, and Observer agents will do their best to pilot the Jetson Orin Nano to victory. 💻 How we built it We used SSH tunnels to connect between our hosts and the Jetson Orin mounted on top of our Jetbot. We wrote Python API endpoints that we can call to control the robot remotely, and these endpoints would also be the basis of using ADK for controlling the robot. We created a control panel with react and typescript to analyze the view of the robot live using web sockets and to quickly be able to interact with it. YOLOE was used as a middle layer for image identification to reduce context bloat and token costs when interacting with Google Gemini, and made for some fun optimizations that found the right balance of abstraction with these highly complex and generalized models. ‼️ Challenges we ran into It was a challenge getting ADK to be precise in the actions it takes for autonomous robotics. Specific implementations of robotic movement were also difficult, and a lot of networking issues came up along the building process. Additionally, some more impactful hardware components like Lidar were out of our budget, so we were limited by what we had. We were able to tweak issues out by the end. 🏆. Accomplishments that we're proud of We're proud that we were able to build a proof of concept and a minimal version of a natural language autonomous robot, just like SOTA VLA models dropping lately. It is by no means industry-grade, but it is accessible to us as students and didn't cost the same as a new car. 🦾 What we learned Networking protocols, working with NVIDIA hardware, and Google ADK. 🤖 What's next for VL-ADK A Humanoid Robot (after we sell all of our belongins) <div