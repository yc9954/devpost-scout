---
slug: "s-kbd67"
url: "https://devpost.com/software/s-kbd67"
title: "S-KBD67"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 334
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# S-KBD67

> Why click a mouse when you can pull a trigger? We hacked a Nerf gun into an FPS controller; shooting, reloading, moving, aiming translates to game input, letting you play your favorite shooters IRL.

[Devpost](https://devpost.com/software/s-kbd67) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[sensor_fusion]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** c++, esp32, esp8266, hw504, mpu6050, nerfgun, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for s-kbd67

## Body

Side view of the modded nerf gun Holding the nerf gun Inspiration "What if you could play an FPS game IRL" was the question that inspired us. Our goal was to enhance the mechanics of an FPS (first person shooter) game into real life using a Nerf blaster. The gameplay turns into something significantly more realistic and immersive. What it does The system lets players control an FPS game using only a Nerf gun (and a bunch of other cool things). Inputs and motions are translated into the game: aiming, turning, pressing our feature buttons and joystick to move, reload and switch weapons. Instead of using a mouse, you can just shoot a (toy) gun, creating a smooth and satisfying connection between the physical and digital experience playing, How we built it We divided into hardware and backend teams. Hardware: Outfitted Nerf blasters with ESP8266 microcontrollers, gyroscopes, joysticks, and buttons to capture movement and input. Backend: Developed a Python application that receives sensor data over Wi-Fi using fast UDP packets, decodes it, and maps it to mouse/keyboard events. This pipeline allowed quick prototyping and tuning for low latency. Challenges we ran into Managing packet timing and size so the controls felt responsive Initial hardware limitations with the ESP8266, requiring a switch to ESP32 in some cases Ensuring stability and durability of the hardware during rapid movements Calibrating sensors for smooth and natural input Working around games with anticheat Accomplishments that we're proud of We’re proud of successfully integrating microcontrollers with PC software, achieving low-latency wireless transmission of high-frequency sensor data, and translating raw motion and analog readings into intuitive, responsive game controls. What we learned Through this project, we learned how to integrate hardware and software, optimize UDP communication for low latency, and calibrate sensors to create smooth, natural gameplay. What's next for S-KBD67 Next, we plan to expand hardware support for more blaster types, refine motion tracking for greater accuracy, and explore multiplayer and VR/AR integration to push the immersion even further. <div