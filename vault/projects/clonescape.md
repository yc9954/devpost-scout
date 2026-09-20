---
slug: "clonescape"
url: "https://devpost.com/software/clonescape"
title: "eye♥webvr"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 403
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "user/researcher"
  - "substrate/sensor_telemetry"
---

# eye♥webvr

> we put the "eye" in internet

[Devpost](https://devpost.com/software/clonescape) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**user** [[researcher]]
**substrate** [[sensor_telemetry]]

**stack** adhawk-sdk, three.js

## How they structured the write-up

- inspiration
- our first game
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eye♥webvr

## Body

Inspiration We thought Adhawk's eye tracking technology was super cool, so we wanted to leverage it in a VR game. However, since Adhawk currently only has a Unity SDK, we thought we would demonstrate a way to build eye-tracking VR games for the web using WebVR. Our first game You, a mad scientist, want to be able to be in two places at once. So, like any mad scientist, you develop cloning technology that allows you to inhabit your clone's body. But the authorities come in and arrest you and your clone for violating scientific ethics. Now, you and your clone are being held in two separate prison cells. Luckily, it seems like you should be able to escape by taking control of your clone. But, you can only take control of your clone by blinking . Seemed like a good idea at the time of developing the cloning technology, but it might prove to be a little annoying. Blink to change between you and your clone to solve puzzles in both prison cells and break out of prison together! How we built it We extracted the blinking data from the Adhawk Quest 2 headset using the Adhawk Python SDK and routed it into a Three.js app that renders the rooms in VR. Challenges we ran into Setting up the Quest 2 headset to even display WebVR data took a lot longer than expected. Accomplishments that we're proud of Combining the Adhawk sensor data with the Quest 2 headset and WebVR to tell a story we could experience and explore! What we learned Coming up with an idea is probably the hardest part of a hackathon. During the ideation process, we learned a lot about the applications of eye tracking in both VR and non-VR settings. Coming up with game mechanics specific to eye tracking input had our creative juices flowing; we really wanted to use eye tracking as its own special gameplay elements and not just as a substitute to other input methods (for example, keyboard or mouse). And VR game development is a whole other beast. What's next for eye♥webvr We want to continue developing our game to add more eye tracking functionality to make the world more realistic, such as being able to fixate on objects to be able to read them, receive hints, and "notice" things that you would normally miss if you didn't take a second glance. <div