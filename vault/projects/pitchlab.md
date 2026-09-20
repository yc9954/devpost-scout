---
slug: "pitchlab"
url: "https://devpost.com/software/pitchlab"
title: "PitchLab - Professional-Grade Baseball Pitch Tracking"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 870
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PitchLab - Professional-Grade Baseball Pitch Tracking

> PitchLab is an innovative computer vision application for baseball pitchers. We use deep learning models to match the accuracy of radar based ball flight tracking technology for 1/100th the price.

[Devpost](https://devpost.com/software/pitchlab) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**user** [[developer]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** firebase, posthog, revenuecat, stripe, swift, swiftui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pitchlab

## Body

Video playback with ball tracer and metric overlay. Live capture screen while you're throwing for real time feedback. Movement plot and charts to easily see all metrics in one place. List view for managing, editing, and exporting data & videos. PitchLab — Professional Grade Pitch Analysis Using Just Your iPhone Camera Inspiration As a professional baseball pitcher, I spent the last 10 years training with expensive radar-based systems like Trackman and Rapsodo. These tools provide useful insights into pitch velocity, movement, and spin, but they cost upwards of $20,000 (not to mention the thousands in annual fees) and require bulky hardware. Using this data as immediate feedback while training changed my career and got me to the Major Leagues. I know how valuable this data is, which led me to democratize this information so that any pitcher, anywhere, with just an iPhone can have access to pro-level data. This is how PitchLab was born. What it does PitchLab transforms an iPhone into a portable pitch tracking system that has competitive accuracy to radar based systems. By analyzing high resolution video in real time, PitchLab calculates: Velocity Induced vertical and horizontal break Spin rate & Spin axis Pitch location Pitch Type In short, it gives pitchers the same type of advanced metrics they see on MLB broadcasts, but from their pocket. How we built it We combined computer vision , machine learning , and iOS performance engineering : Custom trained deep learning model to track the baseball in flight. A physics engine that reconstructs 3D trajectories using only a single camera angle. CoreML deployment optimized for real-time inference on iPhones at up to 60fps. Firebase + RevenueCat for subscription management, cloud storage, and document based database. All of this is wrapped in a clean SwiftUI experience designed to feel like a natural part of a pitcher’s training routine and a native Apple ecosystem app. Challenges we ran into Performance bottlenecks : Running ML inference on-device at 60 fps while also recording video at high bitrates was a huge pain. We struggled for months trying to get this to run in real time with the level of accuracy we were targeting. We couldn't just throw a huge model at this problem because we wanted this to work in real time on the device itself. Data scarcity : It took a long time for our accuracy to pick up. This was another huge piece to the puzzle, because obviously, if the accuracy isn't good then the app doesn't hold much value. We had to figure out how to obtain the right data to train our model on, and then figure out how to get enough of it for it to be useful. Scaling beta testers : We reached over 300+ total beta testers (200+ of which are monthly active users). One of our beta testers video's gained some traction on Instagram (~20,000 views) which gave us our first big influx of testers (I invited ~100 people at once). That weekend was stressful, as everything broke down and I spent the weekend fixing it all. This showed me the importance of thinking at scale and how we can adopt better systems to accommodate future rapid growth. Accomplishments that we're proud of Achieved 1.2mph average absolute error on pitch velocity, and 1.5in average absolute error on vertical / horizontal break based on a test dataset provided by our beta testers. Our velocity error competes with Trackman & Rapsodo, and our movement data is actually more accurate than Rapsodo devices based on a study performed by Tread Athletics (4:50 timestamp) . Deployed a fully functional ML-powered pitch tracking system to iOS in under a two years with a three-person team. Currently being used by several colleges, facilities, and MLB teams as early adopters as a first step in getting PitchLab into training centers nationwide. What we learned Anything is possible : Let me preface this with: I am not an engineer, I am a baseball player. I know how to code, but I'm not very good at it. You can make up for a lack of skills by dedicating an outrageous amount of time towards something. And with that time, you start to learn. Nobody thought it was possible to compete with a $20,000 device using just a phone. There were plenty of times where I also thought that it might not be possible. But every time we hit a road block, we just kept trying new things until we eventually found something that worked. There ended up being a lot of similarities between a hard tech startup and my baseball career - long term goals / vision, consistently working on improving each day, and most importantly, belief that it can work and never giving up. What's next for PitchLab We’re just getting started: Expanding to coaches’ dashboards , enabling facilities to manage entire teams and track player progress remotely. Launching affiliate programs with baseball facilities to accelerate growth. Extending our ML models for softball and hit tracking , turning PitchLab into a complete pitching + hitting analytics system. Ultimately, PitchLab’s mission is to make pro level analytics accessible to everyone, everywhere. We started with baseball, but will expand to other sports in the future. <div