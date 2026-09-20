---
slug: "the-kick-is-good"
url: "https://devpost.com/software/the-kick-is-good"
title: "The Kick is Good"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 959
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# The Kick is Good

> Ever watched a game of football and wanted to predict how far a field goal really went? We used Computer Vision to find the TRUE distance, and now you can bet on what the real numbers are!

[Devpost](https://devpost.com/software/the-kick-is-good) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**user** [[general_public]]
**substrate** [[geospatial]] [[video_visual]]

**stack** opencv, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the kick is good

## Body

Football coordinate projection: Pre kick Football coordinate projection: Highest position Football coordinate projection: Reaching the ground UI for the minigame to guess the distance based on the kick Inspiration As ball lovers and ball knowers, we've always wanted to do a sports project so innovative that ESPN and other sports giants haven't even done it yet. We consulted our friend, Dhruv, a football fanatic and source of our knowledge, to ask what was missing in his football watching experience, and our minds drifted to the thrilling end to the recent Georgia Tech football game ended by a 55-yard field goal. That field goal looked to be good from 65 yards...but how much further back was it good from, actually? What it does We built a semi-automatic football tracking system that determines how far a field goal was kicked from by analyzing video footage. It works by combining human input with automated computer vision. First, the user provides reference points on the football field (yard line intersections) to calibrate the field in real-world coordinates. Then, the user clicks on the football across certain frames to initialize tracking. From there, the program applies automated refinements: it detects the ball’s color, uses a CSRT tracker for motion, and smooths the path with a Kalman filter. With these inputs, the system reconstructs the ball’s 3D trajectory in yards, analyzes its flight path, and calculates key outcomes—like where the ball crosses a target height (e.g., 3.33 yards, representing the goalpost bar). Finally, it generates an annotated output video that shows bounding boxes, the ball’s trajectory, real-time 3D coordinates, and graphs of the flight path. From there, the consumer-facing frontend takes a look at the final output number and allows users to guess how far that kick really was. It uses the complex backend framework and creates an interactive experience for football fans. How we built it We built the system in Python using OpenCV and scientific libraries (NumPy, SciPy, Matplotlib). The workflow was structured in phases: Field Calibration (Phase 0) – The user clicks known yard line intersections and inputs their distances, letting the program compute a homography and camera calibration. This step ties pixel positions in the video to real-world yards. Interactive Annotation (Phase 1) – The user navigates frames and clicks on the football, marking beginning and end points as well as some intermediate positions. These annotations act as ground truth for initializing tracking. The user only marks a few points - most are interpolated in the next step. Automated Tracking & 3D Analysis (Phase 2) – The system refines annotations using HSV color-based ball detection, fills gaps with a CSRT tracker, and applies a Kalman filter for smoother trajectory estimates. It also accounts for camera motion by detecting field features and adjusts tracking dynamically. A physics-based ballistic model then fits the ball’s 3D trajectory, constrained so the ball always starts on the ground. Visualization (Phase 3) – The output video is rendered with bounding boxes, trajectory overlays, 3D coordinates in yards, and a live graph showing height vs. forward distance. It also marks the crossing point where the ball passes the required height. Gamification (Phase 4) – The output data on the final kick distance is sent to the cloud to be streamed to consumers in an interactive guessing game. Currently, we're just using React for this interaction, but this part is flexible and would be integrated into users' existing mobile sports apps. Challenges we ran into Neither of us had a lot of experience with OpenCV and computer vision in general, and we really did choose a hard CV project to take on. We had to deal with the following hurdles: pixelated footage, noisy backgrounds, color bleeding, tiny subjects to focus on, and the fact that we were creating a 3D projection from a 2D video. In the NFL, ball tracking is done via an RFID sensor inside of the ball, but we naturally don't have access to that information. We tested a lot of different solutions, and ended up having to pivot from a completely CV-based detection system to an assisted CV detection system, where the user marks a few points and the rest is interpolated. Accomplishments that we're proud of We're really proud of being able to put out this project despite our lack of resources. I was shocked to find that it hasn't been done before: the NFL does have models that project this information using the RFID chips inside of their footballs, but college ball does not, and the data isn't often released by the NFL. It's a unique and innovative project, and I had a lot of fun testing a million different methods of ball tracking. Like, I'd never heard of a Kalman filter or CSRT tracking before. What we learned Ky: I learned a lot about how to use OpenCV to track items, especially when they are just a dot on the screen. I also got to improve my skills in React to design the front end for this. Colin: I learned a million new frameworks for developing CV programs. CSRT tracking, Kalman filters, etc. I also learned new concepts in geometry, physics I'd never heard of before, like homography. I'm normally more of a design and frontend guy, but I've recently had an itch for learning how to develop complex backends and this project scratched it. What's next for The Kick is Good Connect the front end to use the back end data. Right now we are estimating that the kick would have been good between 1-3 yards out, but we want to be able to use the data we gathered using OpenCV. The UI would also be adapted for mobile - both Android and iOS to be integrated into PrizePick's system. <div