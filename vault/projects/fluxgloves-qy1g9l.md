---
slug: "fluxgloves-qy1g9l"
url: "https://devpost.com/software/fluxgloves-qy1g9l"
title: "FLUXGLOVES"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 812
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# FLUXGLOVES

> THE INTERFACE IS YOU.

[Devpost](https://devpost.com/software/fluxgloves-qy1g9l) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
  <sub>weak: developer_tools, transportation</sub>
  <sub>weak: developer, frontline_worker</sub>
**substrate** [[sensor_telemetry]] [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** arduino, arduinoide, css3, flexsensors, html5, three.js, webgl, webserialapi

## Body

Inspiration For decades, we’ve relied on keyboards and mice to interact with computers. While these tools are excellent for typing and 2D navigation, they feel unnatural when trying to manipulate 3D objects or navigate virtual spaces. As the world moves toward Virtual Reality (VR) and Spatial Computing, we realized that our input devices needed to evolve. We were inspired by the idea of removing the barrier between human intent and machine execution. We wanted to build an interface that felt instinctive—where waving a hand or closing a fist translates instantly into digital action. Inspired by sci-fi interfaces like those in Minority Report and the growing accessibility of IoT components, Team MAASK set out to create an affordable, high-precision motion capture glove that runs entirely in the web browser. What it does FluxGlove is a wearable motion interface that digitizes human hand movements in real-time. Motion Tracking: It tracks the bending of individual fingers and the orientation of the wrist (tilt and rotation) with high precision. Web Integration: It connects directly to a web browser without needing heavy desktop software installation. 3D Visualization: It mirrors the user's physical hand movements onto a digital 3D model on the screen instantly. Gesture Control: It can detect specific gestures (like making a fist or pointing) to trigger commands, making it useful for gaming, robotics control, or virtual presentations. How we built it We built FluxGlove by converging embedded hardware systems with modern web technologies. The Hardware: The brain of the glove is an Arduino microcontroller. We attached flex sensors along the fingers to measure how much they bend. To track the hand's movement in 3D space, we used an MPU6050 sensor, which combines an accelerometer and a gyroscope. The Firmware: We wrote C++ code for the Arduino to read raw electrical signals from the sensors. Since raw sensor data is often "noisy" and jittery, we implemented smoothing algorithms directly on the chip to clean up the data before sending it out. The Software: We used the WebSerial API to create a bridge between the USB port and the Google Chrome browser. The Visuals: For the frontend, we built a responsive website with a modern glassmorphism UI. We used Three.js, a powerful 3D library, to render the virtual hand and map the incoming sensor data to the 3D model's "bones" in real-time. Challenges we ran into Building a project that combines hardware and software presented several unique hurdles: Sensor Jitter: The flex sensors were incredibly sensitive. Even when the hand was still, the virtual fingers would twitch due to minor electrical fluctuations. We had to implement software filtering (like a running average) to smooth out the signal without creating a delay. The "Gimbal Lock" Problem: When tracking 3D rotation, we initially faced an issue where the virtual hand would flip unpredictably when tilted at certain angles. We learned that standard rotation calculations can fail in 3D space, so we had to adopt a more complex rotation system (Quaternions) to ensure smooth, continuous movement. Web Compatibility: Getting a browser to talk to hardware is relatively new technology. We had to ensure that the data stream from the Arduino was parsed correctly and efficiently so that the 3D animations remained smooth and didn't lag behind the physical movements. Accomplishments that we're proud of Seamless Web Connectivity: We successfully implemented a "plug-and-play" experience where a user can simply plug the glove in and connect via a website, eliminating the need for complex driver installations. Real-Time Responsiveness: achieving a low-latency connection where the digital hand moves almost instantly with the physical hand was a huge win for us. Custom Prototype: We are proud of building the physical prototype from scratch, soldering the components, and managing the cable management to make it wearable and functional. What we learned This project was a massive learning curve for the entire team. Sensor Fusion: We learned that raw data from sensors is rarely perfect. We had to learn how to "clean" data mathematically to make it usable. Full-Stack IoT: We gained deep experience in connecting low-level hardware code with high-level web languages like JavaScript. User Experience (UX): We realized that functionality isn't enough; the device needs to be comfortable, and the visual feedback needs to be immediate for the user to feel "immersed." What's next for FLUXGLOVES Wireless Freedom: Our next major step is to replace the USB connection with Bluetooth functionality to make the glove completely wireless. Haptic Feedback: We plan to add small vibration motors to the fingertips so users can "feel" when they touch a virtual object. Game Integration: We want to build a simple web-based game or API so other developers can use FluxGlove as a controller for their own projects. Gesture Library: We aim to expand the software to recognize a wider library of complex gestures (like "thumbs up" or "peace sign") to trigger specific keyboard shortcuts or macros. <div