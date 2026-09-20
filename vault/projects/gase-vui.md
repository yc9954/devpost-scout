---
slug: "gase-vui"
url: "https://devpost.com/software/gase-vui"
title: "Gaze VUI"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 419
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Gaze VUI

> Gaze VUI notices your intention by detecting your gaze and start to listen your voice to communicate with Alexa.

[Devpost](https://devpost.com/software/gase-vui) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[agriculture_food]]
**substrate** [[geospatial]] [[video_visual]]

**stack** amazon-alexa, opencv, python, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into / accomplishments that i'm proud of
- what's next for gase vui

## Body

Gaze VUI GIF Demo GIF Inspiration How many times have you said "Alexa" or "Hey, Google" in your life?? Wakeup word is a great invention and great tool to kick start conversation. However, this is not the only way for to do that. I would like to propose a new trigger for starting conversation with AI assistants. What it does Gaze VUI notices your intention by detecting your head pose and eye contact. When detecting your gaze, Gaze VUI starts to listen for your voice command. So you just look at the device and order what you want. This is a simple, easy and intuitive way. Users don't need to learn new things like gesture and so on. Like human to human communication, you just look at and communicate. How I built it Gaze VUI captures 1024x768 images from night vision camera stream. 2.Gaze VUI resizes the images to 320x240. It detects your frontal face from the smaller image. When the face is detected, Gaze VUI crops your frontal face from the larger image(1024x768) by mapping from smaller image(320x240). It detects your frontal eyes from the cropped image. When eyes are detected, Gaze VUI checks your gaze by using template matching. When gaze is detected, Gaze VUI starts to listen for your voice and communicates with Alexa(*). (*) To implement the function works with Alexa Voice Service, this project is forked by AlexaPi. https://github.com/alexa-pi/AlexaPi Challenges I ran into / Accomplishments that I'm proud of By using two sizes of images, I accomplished both accuracy and speed in the detection phases. By introducing night vision camera, accuracy in dim environment is improved drastically. (But it's still not perfect.) What's next for Gase VUI Here are some features from the original plan had to be dropped/ended up being dropped. Handling false positive cases For handling false positive case, I wanted to introduce far-field microphone array module. By using this, Gaze VUI can compare the direction of audio source and your gaze. So your Alexa can avoid purchasing a doll house by accident :) LED indicator Wanted to install LED module which can notify the recognition status of Gaze VUI. 360 camera By introducing 360 camera, it can be place anywhere you want. But as of now, stitching is too heavy for real time processing on Raspberry Pi. And more In the original plan, I wanted to use Neural Compute Stick(*) to recognize gaze. By introducing edge AI technology, it could be more smarter without worrying about privacy issue. (*) https://www.movidius.com/ <div