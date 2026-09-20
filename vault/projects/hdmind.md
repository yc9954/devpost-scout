---
slug: "hdmind"
url: "https://devpost.com/software/hdmind"
title: "HDMind"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 295
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "substrate/web_dom"
---

# HDMind

> Leverage immersive VR with brain EEG to enhance focus for children with ADHD.

[Devpost](https://devpost.com/software/hdmind) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]] [[mental_health]]
**substrate** [[web_dom]]

**stack** api, dataflow, godaddy, google-cloud, machine-learning, mongodb, python, unreal-engine, vr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hdmind

## Body

Inspiration Approximately 9.8% (6 million) of US children ages 3 to 17 are diagnosed with ADHD, leaving a considerable impact on their education, career, and day-to-day life. Many interventions are pharmacological or require expensive therapy sessions. We wanted to build an application to aid these children by leveraging VR and a wearable brain EEG band in a cost-efficient way delivered at the comfort of their homes. What it does The app initially baselines the brainwave pattern of the user and recommends activities to reach the target brainwave pattern, which is determined by implementing machine learning on the baseline. The app then sends this data into the Quest VR to tailor a game to improve the user's focus. How we built it The data is acquired through the Muse EEG headband, the data is then streamed through API calls to GCP's DataFlow. The data is then stored on MongoDB Atlas. We built a VR game using Unreal for Meta Quest, and as the attention gets better when Muse senses the game is designed to go smoother and faster. As this delivers an immersive game experience, the user's focus increases faster. Challenges we ran into We had some trouble with the Unreal engine because it was relatively new to all us. We also spent some time trying to figure out the data streaming. Accomplishments that we're proud of We're proud that we were able to deliver the data on our website in an understandable way from the Muse band. We're also happy with the progress we have on our VR game. What we learned We learned how to use Unreal, GCP, and python. What's next for HDMind Next, HDMind will focus on building more VR challenges tailored to fit the user's needs and improve their focus. <div