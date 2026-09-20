---
slug: "ai-mama"
url: "https://devpost.com/software/ai-mama"
title: "Motherly.ai"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 698
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/mental_health"
  - "substrate/sensor_telemetry"
---

# Motherly.ai

> Your mom knows you better than you do.

[Devpost](https://devpost.com/software/ai-mama) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[mental_health]]
**substrate** [[sensor_telemetry]]

**stack** next.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- challenges we ran into
- what we learned
- what's next for motherly.ai

## Body

Motherly.ai just wants to help! She knows how you're feeling, and how to help! Inspiration In the past year, 74% of people have felt overwhelmed by stress, and 30% of young adults in the U.S. experience loneliness multiple times a week. We wanted to create a large-scale solution and turned to what helps us most with both stress and loneliness: our moms. While AI companions like Character AI provide emotional support, they can’t truly take care of you. Our goal was to build an AI agent that deeply understands your emotions and takes action to help you. What it does Stress management is deeply personal - what works for one person might not work for another. That’s why we built Motherly.ai, an AI-powered agent that understands how you experience stress and takes real-world actions to support you. Using biometric data like EMG, heart rate, and blood pressure, it detects your mental state in real-time and responds with personalized interventions, whether it’s scheduling a break, ordering comfort food, or adjusting your environment to help you relax. Unlike traditional AI companions, Motherly.ai doesn’t just listen – it takes care of you. Some things Motherly.ai can do for you If reading the news makes you stressed out She can play calming music and surface good news in the world If you mention you’re stressed out and constantly doom-scrolling Motherly.ai can interrupt your scrolling, order food for you, give you a massage, and contact your friends so they can reach out to you To help your child stay motivated while studying Motherly.ai can automatically give them a YouTube break between problems on Khan Academy when they’re stressed, or alternatively nudge them back to studying when they spend too much time distracted. If you want her to help you stay productive and avoid distractions She can recognize when you’re on Instagram and bring you back to your work How we built it Accomplishments that we're proud of Hardware Hacking : We hacked a TENS unit to give an AI agent the capability of controlling the human body. Cutting-edge research : We used EMGs to create a stress monitoring system based on several papers that correlate EMG activity in the trapezius to stress with p<0.0001 Experimentally Induced Stress Validated by EMG Activity, A Comprehensive Analysis of Trapezius Muscle EMG Activity in Relation to Stress and Meditation The impact of adverse childhood experiences on EMG reactivity: A proof of concept study Trained an LSTM classifier to predict your emotions based on your stress levels and biometric data Live Biometric Processing : Manage 4 separate real time data streams. Distinct Agent Actions : Created several distinct actions for our agent to take: Close the tab you’re on Switch the music to match your mood Order a surprise Domino’s order Text a friend Order matcha Prescribe a massage (using TENS) Book a yoga class Find fun events in your area Interactive Avatar : AI mother makes eye contact with your cursor as she helps you Challenges we ran into To get the EMGs to have consistent readings, it took SOO many different sensor placements on the trapezius muscle in order to get any sort of reading. After learning a lot about anatomy of shoulder muscles and bones, we finally got the electrodes in the right place to measure stress from these muscles, and got really amazing readings from our sensor! We initially tried to use the same signal processing methods mentioned in the papers (bandpass and butter filters, extracting only low-frequency data, etc.) but these were too slow for real time feedback, so we had to create more optimized methods: We accidentally ordered $20 worth of Dominos while testing our Scrapybara automation Making the AI agent do the right thing based on its prompts was very difficult. What we learned How to take readings using EMG sensors and how to give massages using TENS stimulation How to stream data between different services in real time How to create agents with LangChain What's next for Motherly.ai Shrink the EMG sensor to be a 24/7 wearable to enable long-term stress / mental health tracking Allow the user to give Motherly.ai custom personalities, making help more familiar and comforting <div