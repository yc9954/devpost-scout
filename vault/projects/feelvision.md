---
slug: "feelvision"
url: "https://devpost.com/software/feelvision"
title: "FeelVision"
hackathon: "PennApps XII"
winner: true
words: 243
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/video_visual"
---

# FeelVision

> FeelVision is a cane-less navigation tool built for the blind, using Leap Motion's IR cam & Pebble's haptic feedback.

[Devpost](https://devpost.com/software/feelvision) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[video_visual]]

**stack** alchemyapi, bluemix, ibm-watson, leap-motion, node.js, pebble, python, wolfram-technologies

## How they structured the write-up

- what it does
- how it works
- what's next for feelvision

## Body

What it does FeelVision is a navigation tool built for the blind, who would normally rely on using white canes to walk. Using Leap Motions' IR cameras and Pebble Smartwatches' haptic feedback, we introduce a cane-free navigation environment while giving the blind ability to recognize what is in front of them through computer vision technology. How it works Two Leap Motion devices are attached to the user's gloves, which act as proximity sensors using the IR cameras. Close proximity to an obstace then triggers two Pebbles (one on each arm), warning the user of the direction (vibrating one of the pebbles) and the proximity (frequency and intensity of vibration) of the obstacle. At any time, the user can also press one of the buttons on Pebble to control a Leap Motion to take a photo, which is then passed thorugh IBM Watson's AlchemyVision API, AlchemyVision Face Detection/Recognition, and a custom-built image recognition API on Wolfram Cloud to be analyzed and converted into a string, which is read out loud by IBM Watson to notify the user. A Node.js server was deployed on IBM Bluemix to provide WebSockets as a mean to unify connections of all of these devices/services. What's next for FeelVision Our ultimate goal with this project is to make navigation as accessible as possible for the blind. We have ideas for more features, such as using image recognition and text analysis to read out loud any texts for the users. <div