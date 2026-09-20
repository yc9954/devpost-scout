---
slug: "heartbeat-hero"
url: "https://devpost.com/software/heartbeat-hero"
title: "Heartbeat Hero"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 876
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/geospatial"
---

# Heartbeat Hero

> Heartbeat Hero turns iPhone and iPad into a CPR coach. Learn the theory, practise rhythm and depth, simulate a 999 or 911 call, and find real AEDs. Works offline. Students get full access free.

[Devpost](https://devpost.com/software/heartbeat-hero) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[accessibility]] [[developer_tools]] [[education]]
  <sub>weak: transportation</sub>
**user** [[developer]] [[educator_student]] [[frontline_worker]]
**substrate** [[geospatial]]

**stack** ai, ar, django, ios, openai, postgresql, railway, revenuecat, swift, swiftui

## How they structured the write-up

- where it began
- why i built it
- what i built
- how i built it and challenges i faced
- what i learned
- why it is different
- whats next for heartbeat hero
- final note

## Body

About the project Where it began Heartbeat Hero began as my Swift Student Challenge project for 2024. It was selected as one of 50 Distinguished Winners ( https://developer.apple.com/swift-student-challenge/distinguished-winners/ ) at WWDC24, but I never shipped the prototype. Over the last year I rebuilt it for a full public release, improving the overall experience and redesigned the app for iOS 26. Why I built it A few weeks before that original build, my uncle - a firefighter - told me how he saved someone's life with CPR. It made me realise most people want to help but have never practised or have the confidence to, as at the time I myself had no idea how to perform CPR. Heartbeat Hero aims to change that with an easy, memorable, interactive, and accessible way to learn the essentials, feel correct rhythm and depth, and rehearse the emergency call. What I built An iPhone and iPad CPR coach with five modes: Learn, Rhythm, Depth, an AI-guided 999 or 911 call rehearsal, and a real AED map. The app opens with the users live address, what3words and GPS for quick handover to responders if needed. All the training runs on device for privacy and reliability - allowing the app to function offline, with the Learn mode and AED map free for all users and lifetime full access to all features for verified students. How I built it and Challenges I faced Depth Practice is the core innovation. I combine ARKit visual-inertial odometry, high-frequency IMU data and feature tracking, then stabilise it with adaptive filtering to estimate compression depth in real time. This allows users to perform CPR on a soft surface using their device, and recieve real-time, accurate feedback down to the mm - all without any extra equipment. Demo video: https://youtu.be/eYicwcjoOKQ Sampling and fusion: 200 Hz accelerometer streams align to AR pose for a gravity-stable depth signal that is both responsive and robust. Calibration: 60 samples over roughly 3 seconds with median statistics lock a solid reference and reject outliers. Dual-mode tracking: Feature-rich scenes use a full adaptive Kalman filter with 5-sigma outlier rejection and drift compensation. In sparse or plain ceiling cases a simplified Y-axis tracker is used. State machine: 200 Hz IMU signals detect compression start and end with millisecond precision to gate evaluation and feedback. This was by far the most complex feature of the app, and took many, many sleepless nights to get working, but I am very proud and happy with how it turned out! Rhythm Practice uses a low-latency AVAudioEngine tap for tempo detection, allowing users to simply clap to the rhythm, or, use a CPR dummy or practice surface that produces noise on compression. Accessibility and feedback are multi-modal: haptics, voice guidance and torch pulses for hearing accessibility, plus VoiceOver labels across the UI. In addition, I also engineered a 'focus' mode for the learning sections of the app to allow users who have ADHD, Dyslexia, or other reading difficulties to easily complete and comprehend the theory of CPR. By focusing on one small section at a time, and eliminating all other distractions, the Focus mode makes it much easier to learn the theory - even allowing the app to read out the sections and auto-progress if the user requires. What I learned Building accessibility early helped everyone, as not all users can see, hear, or are able to read long bouts of text. I used VoiceOver, Dynamic Type and clear haptics, and I kept testing with those settings to make sure it was inclusive for all. Planning for offline made the app simpler. I stopped assuming a signal and chose features that work anywhere, this is as not everyone has signal all the time, especially in a crowded room where one day I hope everyone is there to learn CPR using Heartbeat Hero. Feedback changed the product. I removed ideas that looked clever but slowed people down, its easy to get blinded by something I want in the app, but my users do not. Keeping some features free matters. Learn mode and the AED map stay free, and students get full access. Just because someone can't afford the fancy stuff, does not mean they should not be able to have access to potentially life-saving information. I designed the app for people in stressful moments. I put the users location right at the start and is always available from the home screen. I did not do this alone. Firefighters, mentors, family, and friends shared time and advice, for which I am very grateful. ❤️ Why it is different To my knowledge, no other mobile CPR trainer offers this level of depth accuracy with environment-aware sensor fusion, adaptive filtering and real-time mode switching - all private and on device without the need for any extra equipment. Whats next for Heartbeat Hero I hope to get Heartbeat Hero into the hands of as many people as possible, doing this by partnering with training providers, foundations, charities and schools to give them the tools to share the knowledge. Final note Heartbeat Hero is not a substitute for certified training. It is a bridge from zero to confident action - helping anyone practise rhythm and depth, rehearse the emergency call, and step forward when seconds count. <div