---
slug: "human-environment-in-smart-buildings"
url: "https://devpost.com/software/human-environment-in-smart-buildings"
title: "Human environment in smart houses"
hackathon: "Junction 2016"
winner: true
words: 300
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "substrate/sensor_telemetry"
---

# Human environment in smart houses

> By joining together humanity and buildings we perfectly suite and adopt living and work places for our needs.

[Devpost](https://devpost.com/software/human-environment-in-smart-buildings) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**substrate** [[sensor_telemetry]]

**stack** 720?, excel, k-30, ouraring, perl, raspberry-pi, ruby

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for human environment in smart buildings.

## Body

working place Inspiration This project was inspired by new wearable low-energy sensors and smart building environments. What it does The main idea was to connect and include into common control loop for improving environment and human behavior two different data sources: wearable heath/fitness sensors and fixed smart house devices for better quality of live. By taking into account medical metrics like pulse, breathing frequency, MET metering and so on we achieve better understanding how environment can be tuned up to fit our individual activity and behaviors. As an example one can consider reducing ventilation air flow for helping get sleepy by increasing CO2 ppm rate rather then taking drugs against insomnia. How I built it I took logged records form different sensors https://ouraring.com/ (Oura) and http://www.720.fi/en/solution/ (Tieto), http://www.co2meter.com/products/k-30-co2-sensor-module (Junction) and make an attempt to synchronize them in time series for correlation analysis and decisions about air quality and blood flow. Challenges I ran into mismatching log and historical data specifications lack of data collected in the same time and place no low-energy Bluetooth on my smartphone/notebook required for connecting to wearable devices no straightforward access to raw time series data historical records instead of real-time data flow WiFi connectivity problems at working table Accomplishments that I'm proud of I proved conceptual possibility for getting together different by their nature data and formulate some use cases for development What I learned New hardware devices and software protocols. What's next for Human environment in smart buildings. I do believe that we can control only measurable things so one can not ignore any possibility for measures for better understanding how actually people feel and behave in the environments created for them. Wearable devices improving their actuality and data accuracy and using it looks looks very promising for adjusting and improving environment control. <div