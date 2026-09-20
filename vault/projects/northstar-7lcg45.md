---
slug: "northstar-7lcg45"
url: "https://devpost.com/software/northstar-7lcg45"
title: "Northstar"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 842
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Northstar

> The light that guides you home.

[Devpost](https://devpost.com/software/northstar-7lcg45) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]] [[sensor_fusion]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[video_visual]]

**stack** elevenlabs, expo.io, fetch.ai, melange, react-native, twilio, zetic

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for northstar

## Body

Inspiration Over half of hiking-related injuries are caused by slips and falls, and the majority of those are ankle injuries. Especially on trails, where mobile data is limited, finding support after an injury can feel like a hopeless endeavor. With Northstar, we strive to fix that. What it does After detecting a fall, Northstar starts the assistance right away. First, beginning with a voice activated digital triage, our fully Zetic-based locally-run model decides the best course of action for quick recovery without the need for any external internet connection, while also building an injury assessment in the background. Next, Northstar uses an optical technique called Photoplethysmography to accurately determine the patient's heart rate and blood pressure using the phone's own back camera and flash. After this, Northstar manages a swarm of fetch.ai agents, each delegated to find important details for the patient, from the nearest care center to other vital pieces of information that could truly be the difference between life and death. Last but certainly not least, Northstar uses the injury assessment it has been perfecting over the triage process, and uses satellite connectivity to personally call the patient's emergency contact and give the assessment, both through audio call and through SMS, even if the patient isn't even conscious. How we built it Northstar is a multifunctional mobile app, build on React Native with Expo with an additional native module to handle the native optimized zetic LLMs. The fall detection was done through two different coinciding pathways. Using the built in accelerometer built into every phone, Northstar tracks drastic spikes or drops in accelerometer activity to estimate if there was a fall and check in with the user. Northstar also uses a Zetic based local audio-analysis model YAMNet in order to detect sounds of pain from the user and check in. The digital PPG was created by determining the changes in red shades from the back camera alongside the flashlight, a well known technique for low-cost efficient vitals determination called Photoplethysmography. The voice-based digital triage was done using Zetic's local Qwen 3.5-4B model, optimized for response time and accuracy, and summarized into the creation of the injury assessment. The agent swarm was done using a series of fetch.ai agentverse agents, each customized to have a specific speciality. After this, the satellite calling and SMS messaging was done through both Twilio and ElevenLabs, using a bridge process to connect the data and create the outgoing call transferring through the ElevenLabs voice model and the Twilio calling API. Challenges we ran into Initially, the implementation of the digital triage wasn't working correctly through the Expo framework, and we thought we would be forced to switch our project fully over to Swift. However, we were able to use Expo Prebuild to bridge between Swift and Expo so that to get the best of both worlds. We also had some trouble implementing the triage model, but we spent some time testing different implementations, until we perfected the implementation to a working level. The calling functionality was also quite a challenge, with the routing through Twilio being particularly hard to capture. However, after some time spent studying the documentation, we routed our data through Twilio and ElevenLabs and successfully created the calling and messaging functionality. Accomplishments that we're proud of We were particularly proud getting multiple optimzed AI models running on mobile hardware. Both the Qwen LLM and the sound classifying YAMNet models took a long time to get working but work surprisingly well. We are also proud of the agent swarm through which we could grab data in an incredibly efficient manner. It took a while to get it set up, but in the end, it brought our product to another level. We were also very proud of how hands-off our product ended up being. Injuries vary, so we were very proud of the way that we used the limited resources that our situation required. We had to build our app around the lack of internet on hiking trails, and have fallbacks in case the user was unable to physically type on their phone due to the damage they sustained. What we learned We learned a lot about project organization through this project. We were able to delegate tasks really efficiently, and each of us had an important role to play. We realized that some of the most important parts of the project aren't the actual lines of code that we were writing, but who is planning and writing what parts, as well as communicating so that when the puzzle pieces are all together, they fit seamlessly. We also realized how powerful local models can be, and not everything needs the internet to be impressive. What's next for Northstar As a team, we all really believe in the ability for Northstar to help hikers around the world, so we want to try and continue this app. We want to implement a deeper Twilio functionality, as well as lean into the ability that local models have, since we didn't realize how powerful they could be. <div