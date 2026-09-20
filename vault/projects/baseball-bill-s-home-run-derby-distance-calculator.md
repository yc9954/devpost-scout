---
slug: "baseball-bill-s-home-run-derby-distance-calculator"
url: "https://devpost.com/software/baseball-bill-s-home-run-derby-distance-calculator"
title: "Statcast CV Model: Performs like the Pirates!"
hackathon: "Google Cloud x MLB(TM) Hackathon – Building with Gemini Models"
organization: "Google"
winner: true
words: 372
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "user/developer"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Statcast CV Model: Performs like the Pirates!

> Utilize 2 models, an DNN with advanced feature engineering and a Spatiotemporal NN, to more accurately predict Stat Cast metrics on historical videos.

[Devpost](https://devpost.com/software/baseball-bill-s-home-run-derby-distance-calculator) · hackathon [[Google Cloud x MLB-TM- Hackathon - Building with Gemini Models]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**user** [[developer]] [[researcher]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** colab, opencv, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for baseball bill's home run derby distance calculator

## Body

Inspiration I am a Pirates fan and an aspiring Data Scientist with a career trajectory pretty much in line with the Pirates season the past two-three decades. I wanted to test my hand at some computer vision modeling and designing a solution involving data. What it does Generate Statcast Data from Old Videos: Create a tool that extracts fundamental Statcast metrics (e.g., pitch speed, exit velocity) from archival game videos using computer vision. How we built it Build Hit Distance Regression Model from Tabular Data & Advanced Feature Engineering Build Exit Velocity & Launch angle prediction model from video. The goal therefore is to limit the number of frames the Video processing model has to handle since it would only need to see those on which the batter makes contact with the ball. One advantage of this is to reduce computational constraints and potentially allow real time distance traveled forecasts! Challenges we ran into Turns out some videos even in 2024 do not have a distance calculated! Also, some players are exceptionally athletic! Able to make within the park home runs through sheer speed. Computational demands exceeded colab notebook capabilities quite often. Accomplishments that we're proud of Neural Network Regression Hit Distance Prediction Model Key Innovations: Extract ball direction from play by play title Add physics kinematics properties from projectile motion Spatiotemporal Neural Network Video Exit Velocity & Launch Angle Prediction Model Key Innovations: Designed frame efficient Video Data Generator for Tensorflow model Utilized transfer learning on lightweight MobileNetV2 What we learned Optimized NN model is nearly a 20% performance improvement over the Linear Regression model which has a Mean Squared Error of 275.40. Pure physics model needs more inputs from effects of Air resistance and friction. Video processing models require a LOT of GPU memory. What's next for Baseball Bill's Home Run Derby Distance Calculator Possible Improvements: Engineer more features related to game conditions. Ie. Could get time of day, month game is played, field game is played at, temperature, wind speed, etc. More efficient frame extraction (ie. have another meta model that only captures frames when the bat is in the strikezone) Image preprocessing techniques like masking to isolate the baseball and bat or other enhancements for frame quality <div