---
slug: "physiocare-6sjefu"
url: "https://devpost.com/software/physiocare-6sjefu"
title: "PhysioCare"
hackathon: "Hack the North 2019"
winner: true
words: 531
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# PhysioCare

> Feeling stiff? Bring relief to your fingertips.

[Devpost](https://devpost.com/software/physiocare-6sjefu) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** android, android-studio, arduino, chatbot, firebase, flex-sensor, force-sensor, imu, muscle-sensor, myoware, raspberry-pi, rviz, sensor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for physiocare

## Body

Muscle sensors Full Picture Inspiration As developers, we often immerse ourselves in technology, sitting in front of our screens for hours at a time. Reality often hits only when we stand up from our desks at the end of the day -- it often feels as if every joint has turned to stone, yet the stiffness seems to permeate our entire body, making it difficult to pinpoint the source. We created PhysioCare to help others identify and relieve this tension, so that they can continue to pursue the work they love. What it does Identifies source of stiffness Tracks movement and muscle tension by body part. Provides /instructions/feedback Alerts users on where muscles are tense and how they can be alleviated. Real-Time data: Firebase All sensor data are streamed onto cloud database and displayed in Android app real-time. How we built it Hardware Component 1) Raspberry Pi All calls and sending/receiving of data is conducted through raspberry pi. It's connected to an Arduino, the power source and the IMU, which provides accelerometer and gyroscope data. 2) Arduino 3 sensors are wired to the arduino: a) Muscle sensor (Myoware): produces raw EMG data, which we converted into Volts. b) Flex sensor: produces 2 parameters, resistance and degrees of bend c) Force sensor: produces output in Newtons when pressed 3) RViz (3D Rendering) Rendering a vector that traces orientation of the IMU 4) Wifi Hotspot Currently hooked onto router for demo purposes, do to the limited computing capacity of the raspberry pi, but hotspot can be done on the raspberry pi directly so that no routers would be needed Software Component 1) Firebase a) Real-Time Streaming PUT sensor data onto Real-Time Database and use API calls to retrieve and display data b) Smart Reply (Chatbot) Integrated chatbot function that allows users to converse with AI 2) Android Application a) Graphed Data Displays sensor data to users in real time b) User Authentication c) Interface Design for optimal user experience Challenges we ran into Firebase Smart Reply: dissatisfied with the level of intelligence in this feature, yet unable to modify responses for our purposes. Firebase Data streaming: compatibility issues from ROS to Firebase. Updated leaf node properties individually rather than merging all sensor data into a packet before sending. Accomplishments that we're proud of Muscle Sensor: actually responds to changes in flexation of arm muscles Fully integrating IoT (rPi, Arduino, Flex sensor, Muscle sensor, Force sensor, IMU, router) with Android app and Firebase. What we learned How to use Firebase features with Android Studios How to position/use biomedical sensors The significance of sensor data and what they indicate Quaternions What's next for PhysioCare Creating body-part specific devices with tailored calibrations & calculations intended for that muscle group (forces in legs are obviously far larger in value than those in arms) Creating detailed instructional guides and manuals for: Device Handling & Usage Stretching Exercises (by limb) & Advice ML (upgraded for Chatbot and implemented for data processing) developing a lighter and more accurate model user wear Developing a smoother user experience with more design considerations implemented tooltips, help icons, external links for more info more logical event flow sleeker aesthetics/styles more intuitive naming scheme <div