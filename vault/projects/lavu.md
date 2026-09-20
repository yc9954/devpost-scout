---
slug: "lavu"
url: "https://devpost.com/software/lavu"
title: "LavÜ"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 490
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/frontline_worker"
---

# LavÜ

> An eHealth device consisting of a wearable electromyogram (EMG) sensor that monitors muscle tension and sends haptic feedback. It includes an app that guides you towards managing your stress levels.

[Devpost](https://devpost.com/software/lavu) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[mental_health]] [[transportation]]
**user** [[frontline_worker]]

**stack** 3d-printing, arduino, c++, emg, figma, haptic

## How they structured the write-up

- intro
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lavü

## Body

LavÜ - Stress detection in real time & receive haptic feedback Intro Have an upcoming exam? Planning a wedding? Or have a tight deadline? "I'm really stressed right now! Help!" Well, with LavÜ, we've gotchyou! Inspiration After experiencing stressors in everyday life and speaking with members of the community, we found that many people experience stress physically—particularly, through tightness in the neck and shoulders. Research backs this up. A study by Jacqueline Wijsman et al. published in Wireless Health found "significantly higher amplitudes of the EMG signals [from the Trapezius muscles] during stress compared to rest and fewer gaps (periods of relaxation) during stress," making it a useful indicator of stress in real time. What it does LavÜ Device : A wearable electromyogram (EMG) sensor that monitors muscle tension and sends haptic feedback . By analyzing trends in muscle tension over time, LavÜ detects changes in stress levels. Using this data, we can notify users through a gentle tap if it's time to do haptic-assisted breathing exercises or take a break. LavÜ App : In addition, the LavÜ App, displays a chart of your stress levels over time throughout the day. The app provides features to take care of your mental health reducing your stress levels such as providing journal entries, nutritional values, breathing exercises, and more. How we built it LavÜ is powered by the Nicla Sense ME microcontroller and a LiPo battery, while a Gravity EMG Sensor takes measurements of muscle tension. A DRV2605 Haptic Driver assists in generating gentle vibrations. The device itself is enclosed in a flexible 3D printed chassis, which is sewn into clothes for comfort. Challenges we ran into Creating a hardware project results in many practical challenges. Powering the device (working with multiple power sources) Mounting the device - ensuring that proper contact is made between the sensor and the body Writing code to interpret data from the EMG Developing haptic breathing sequences Accomplishments that we're proud of We are extremely proud of the ability to record data that can be converted into stress levels in real time. Additionally, we were able to design an interactive prototype of our envisioned app that goes hand-in-hand with the device. What we learned Working on a project that requires both technical aspects of both hardware and software requires a strong understanding of how we can integrate the data together. Coming from different backgrounds, we learnt how to collaborate cohesively and efficiently to build this project. We also have a better understanding of the users we design for and the various forms of stress relieving exercises. We have thoroughly enjoyed this project as it has given us multiple perspectives of technology. What's next for LavÜ Create greater awareness of points system that can provide positive reinforcement ML model that can learn stress patterns from each individual for personalized detection and feedback Include better accessibility software on different mobile applications Try out LavÜ for a better you! <div