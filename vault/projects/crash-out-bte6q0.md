---
slug: "crash-out-bte6q0"
url: "https://devpost.com/software/crash-out-bte6q0"
title: "CRASH OUT!"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 574
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
---

# CRASH OUT!

> lets you crash out, whenever, wherever, whatever (on the drums).

[Devpost](https://devpost.com/software/crash-out-bte6q0) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]] [[immigration_refugee]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]

**stack** adc, ar, audacity, blender, chatgpt, circuits, embedded, javascript, lego, python, qnx, raspberry, redbull, rtos

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for crash out!

## Body

Made with love The kicker Inspiration Coming into Hack The North, all four of us were hyped to do a hardware-based project. We couldn't resist checking out the AR glasses Snap Spectacles, the Raspberry Pi running a blazing fast RTOS from QNX, and, of course, the LEGO! After a long night of brainstorming, we had so many intriguing ideas, but we had to pick only one. Of all the things we could present in an augmented world, we chose one of the most expressive instruments to play: the drum kit! What it does CRASH OUT! brings you a full drum set wherever you are. Many people wish to learn or at least to try playing the drums, but small apartments, sleepy neighbours, and empty wallets forbid our dreams of being rock stars. With the augmented reality capabilities of the Snap Spectacles, CRASH OUT! turns your air drumming into an immersive experience with realistic audio and minimal gear. To keep it interesting, you can imagine any variety of drumsticks and they'll materialize in front of you to play with. How we built it All video analysis, physics simulation, and audio/video generation is performed inside the Spectacles in front of your eyes! Borderless interactions are facilitated by physics principles, collision detection, and audio directed straight to your senses. The optional kick drum pedal uses a Raspberry Pi running the QNX real-time operating system for seamless responses. A pressure sensor helps you express your inner emotions, transmitting the exact strength of your strike to the Spectacles over a speedy web socket for instant feedback. The Snap 3D generative AI system turns voice commands into creative and unexpected models, which are loaded into the environment for interaction. Challenges we ran into Setting up the 3D environment was difficult, especially in the unfamiliar Lens Studio SDK, but with help from the passionate hearts of the experts around, we deftly adapted. Moreover, despite the expansive hardware inventory, we had trouble finding the components to interface between the pressure sensor and the Spectacles. We worked our way through Bluetooth incompatibilities and confounding electronic bugs to create a swift and stable linking circuit. Accomplishments that we're proud of We leveraged modern LLM development tools to accelerate the development of a driver for the MCP3008 ADC chip, which finally bridged the gap between the analog sensor and the digital RTOS. We're very proud of the real-time audio triggered by robust collision detection between drums and sticks. To achieve this, we had to transform and segment existing models into multiple meshes, then compose them back into a cohesive whole. One of our biggest and most relieving accomplishments was tuning the hand posture to mimic a natural grip on the drumsticks; a serious improvement over pinching them like darts. What we learned We were surprised to find how much we could achieve in the 24 hours between formulating our idea and submitting it as a polished product. We also learned the importance of developing a healthy team culture early. We discussed our goals, priorities and values to avoid misunderstandings. Thus, we agreed to focus more on creating a fun, meaningful and impactful project than optimizing prizes. What's next for CRASH OUT! In all our brainstorming, there were always some brilliant ideas left behind. CRASH OUT! is not limited to percussion instruments, but is open to further growth for other instruments. In the future, maybe people can jam together with CRASH OUT! on Snap Spectacles. <div