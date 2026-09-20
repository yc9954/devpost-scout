---
slug: "covid-cam-tv"
url: "https://devpost.com/software/covid-cam-tv"
title: "Covid Cam TV"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 279
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/video_visual"
---

# Covid Cam TV

> The COVID Cam TV regulates the flow of people entering and exiting a building to allow for social distancing. The sensor eliminates distractions and increases human potential of the employees.

[Devpost](https://devpost.com/software/covid-cam-tv) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: realtime_stream, vision_ocr</sub>
  <sub>weak: transportation</sub>
**substrate** [[video_visual]]

**stack** anaconda, opencv, python, tensorflow, vscode

## How they structured the write-up

- inspiration: many businesses are struggling to currently find employees. many of them don’t want to pay employees to stand outside throughout the day counting as customers enter the doors to regulate the flow of traffic.
- what it does: through a connected wireless camera, the software tracks the number of people who enter and exit the building. once a critical number of people have entered the room, the software will , alerting the last person who entered of their mistake.
- how we built it: python, anaconda, opencv, tensorflow.
- challenges we ran into: it was incredibly difficult to actually make the opencv model to track people in real time instead of just detecting their presence in a video frame. this kept on giving us errors such as there being thousands of people in a room at a time, when only one person was in front of the camera. we cycled through not only half a dozen computer vision models, but we were eventually able to settle on one that would perform well enough for our prototype.
- accomplishments that we're proud of: the camera was working. it recognizes humans and it tracks the movement.
- what we learned: we learned about hardware components such as arduino ov7670, uno r3. then how to use anaconda and more of python, opencv, and tensorflow.
- what's next for covid cam tv: building it in tensorflow js to not only make it compatible with more devices, but also run faster and on lighter systems for a smoother experience. we would also like to integrate more cameras and build a web app around it that would allow it to seamlessly integrate into the security system of the building.

## Body

Inspiration: Many businesses are struggling to currently find employees. Many of them don’t want to pay employees to stand outside throughout the day counting as customers enter the doors to regulate the flow of traffic. What it does: Through a connected wireless camera, the software tracks the number of people who enter and exit the building. Once a critical number of people have entered the room, the software will , alerting the last person who entered of their mistake. How we built it: Python, Anaconda, OpenCV, Tensorflow. Challenges we ran into: It was incredibly difficult to actually make the OpenCV model to track people in real time instead of just detecting their presence in a video frame. This kept on giving us errors such as there being thousands of people in a room at a time, when only one person was in front of the camera. We cycled through not only half a dozen computer vision models, but we were eventually able to settle on one that would perform well enough for our prototype. Accomplishments that we're proud of: The camera was working. It recognizes humans and it tracks the movement. What we learned: We learned about hardware components such as arduino OV7670, UNO R3. Then how to use anaconda and more of python, OpenCV, and tensorflow. What's next for Covid Cam TV: Building it in Tensorflow JS to not only make it compatible with more devices, but also run faster and on lighter systems for a smoother experience. We would also like to integrate more cameras and build a web app around it that would allow it to seamlessly integrate into the security system of the building. <div