---
slug: "brainhack-wheelchair-smart-brain-controlled-wheelchair"
url: "https://devpost.com/software/brainhack-wheelchair-smart-brain-controlled-wheelchair"
title: "BrainHack Wheelchair - Smart Brain Controlled Wheelchair"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 435
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# BrainHack Wheelchair - Smart Brain Controlled Wheelchair

> Reading your thoughts is now a reality.

[Devpost](https://devpost.com/software/brainhack-wheelchair-smart-brain-controlled-wheelchair) · hackathon [[MongoDB World Hackathon]]

## Facets

**domain** [[accessibility]] [[elder_child_care]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** android-studio, mongodb-mobile, neurosky-eeg-headset, python, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what's next for brainhack wheelchair - smart brain controlled wheelchair

## Body

Brain Computer Interface Actual Wheelchair Prototype Prototype Prototype + Brainwave Headset Android App with MongoDB Mobile Raspberry pi console flowchart Inspiration Millions of people across the world suffer from various mobility impairments caused by Amyotrophic Lateral Sclerosis (ALS), brainstem stroke, brain or spinal cord injury, cerebral palsy, muscular dystrophies, multiple sclerosis, and many other diseases. A large portion of these people heavily rely upon wheelchairs to get on with their day to day activities. These people are dependent on others in order to move A large number of patients are not prescribed wheelchairs at all, either because they find it physically difficult to control the manual wheelchair. In our work with Brain Controlled Wheelchairs, we target a population who are—or will become—unable to use conventional interfaces, due to severe motor–disabilities. What it does BrainHack Wheelchair is a Smart Wheelchair controlled with your Brain. It uses a Brainwave Reader to read your Brainwaves. The Brainwaves are then decoded into the Android app into Attention, Meditation, Eye Blink Strength and Raw values. The direction of the Wheelchair is then controlled with your Attention Level and Eye Blinks. JUST FOCUS to move the robot FORWARD, and Blink your eyes twice to turn it LEFT !! The Wheelchair is controlled with a Raspberry pi... And it has a Camera too for live image processing ! How I built it The mobile App contains the necessary libraries to process the incoming Brainwaves. The Headset measures our Attention Values on a scale of 0-100 When the attention of the subject reaches a predefined threshold, the Wheelchair starts moving forward In Order to turn Right, the user blinks twice in a span of 1 second above a threshold of 100. The Attention and Eye Blink values are also stored in the MongoDB Mobile Database every second as the data comes from the Brainwave Headset. The data in the database is then processed to calculate the Average Attention and Average Meditatiion values of the user also also to determine what Attention and Eye Blink thresholds would be best for a particular user since it varies from user to user. What's next for BrainHack Wheelchair - Smart Brain Controlled Wheelchair Future possible implementation: Obstacle Avoidance -Automatically detect and avoid Obstacles. Auto Pilot Mode - Think about a Destination such as Kitchen or Hall and it will get the user there in Autonomous Mode. Emergency Braking System - If user abruptly closes his eyes sensing some danger, then the Wheelchair will stop Staircase Climbing Mode - To assist the elderly to help climb the stairs. Medium Post : https://medium.com/@vinit.todai/brain-controlled-wheelchair-b69a9969787d Actual Wheelchair Implementation : https://www.youtube.com/watch?v=u65aZ6zmeqM <div