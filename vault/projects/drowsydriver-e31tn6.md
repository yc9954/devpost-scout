---
slug: "drowsydriver-e31tn6"
url: "https://devpost.com/software/drowsydriver-e31tn6"
title: "DrowsyDriver"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 529
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DrowsyDriver

> Real-time computer vision software with fatigue detection system to improve accessibility of the technology and alert drivers in danger of sleepy driving, preventing accidents.

[Devpost](https://devpost.com/software/drowsydriver-e31tn6) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[transportation]]
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** azure, dlib, flask, opencv, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for drowsydriver

## Body

Inspiration Inspired by the alarming number of accidents caused by drowsy driving, many of us have experienced late nights on the road, where fatigue can dangerously affect attention and reaction time. We want to create a solution that enhances road safety and prevents accidents caused by drivers falling asleep. The goal is to provide an accessible, reliable tool that can alert drivers before they reach the point of exhaustion, making the roads safer for everyone. What it does The system monitors and detects signs of drowsiness in the driver by analyzing facial landmarks and expressions. Through real-time video feed, it continuously checks for signs like drooping eyelids, prolonged blinks, or yawning, which are early indicators of fatigue. Upon detecting these signs, the system issues an alert to help the driver stay alert and warn them of their safety. This proactive approach helps reduce the risk of accidents by ensuring that drivers are attentive and aware of their condition before it's too late. How we built it We used a Kaggle dataset of facial images for detecting facial landmarks, such as eyes, mouth, and head position using OpenCV and dlib, we implemented a system that classifies signs of drowsiness based on these landmarks. The software tracks key features like eye closure duration and yawning to recognize patterns of sleepiness. A dynamic front end using React, enabling real-time monitoring and alerts, and the back end, built with Flask, integrates all the components, handling communication between the video feed, model, and user interface. Challenges we ran into FLASK!!! we spent much time connecting our front end with a backend. we had developed both separately simultaneously and when it was time to learn how to use flask to connect them, it came out to be more intensive than expected. tweaking the python script for the cv part was also challenging but fun. we kept tweaking and tweaking the cv script so it could be more accurate according to what we thought signs of drowsiness should be classified as. moreover, fixing the audio api that alerts the user was difficult because we ran into bugs where it would continuously alert more than once and not at the exactly correct times. Accomplishments that we're proud of Our grit and dedication during these 32 hours of hacking. We all strived for more and more during engineering our project. We are proud of our teamwork in this (and how we effortlessly merged with git). What we learned We all started with different skills and learned from each other. Some of us learned flask, computer vision libraries, or front end development. We learned more about git and version control as well. we learned how to make a full-stack application. What's next for DROWSYDRIVER In the future, we aim to make DrowsyDriver accessible to everyone. With more time, we envision developing a compact device that can be easily mounted on dashboards, catering to concerned family members, friends, and truck drivers alike. Additionally, we plan to gather data from this device to create an application that alerts family members about their loved ones’ safety. Our goal is to enhance road safety and ensure peace of mind for all users. <div