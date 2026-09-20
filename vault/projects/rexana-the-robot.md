---
slug: "rexana-the-robot"
url: "https://devpost.com/software/rexana-the-robot"
title: "Rexana the Robot"
hackathon: "PyTorch Summer Hackathon 2020"
organization: "Facebook"
winner: true
words: 721
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Rexana the Robot

> More than a voice assistant, this project is the foundation for physical household robot trained to autonomously complete basic tasks

[Devpost](https://devpost.com/software/rexana-the-robot) · hackathon [[PyTorch Summer Hackathon 2020]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
  <sub>weak: realtime_stream</sub>
**user** [[educator_student]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** python, pytorch, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for rexana the robot - pytorch

## Body

Hardware Dashboard UI Real-time Object Detection and 3D pose estimations from robot to Cloud AWS server to infer then results returned back to robot using sockets Base Electronics Rexana / Dashboard Inspiration 1) The idea of having a Voice Assistant like Alexa or Siri that could extend into the physical world for tasks around the house 2) Having an interactive robot for fun and immersive language education, She understands and can reply in Spanish 3) The Idea of having a personal robot that in the future as the ability to be a useful care giver/ physical assistant What it does Rexana is a voice-activated personal assistant robot that currently does the following tasks: Autonomous navigation around the house, using distance and location data (landmarks) from the 2D lidar, her cardinal/compass bearing, the wheel encoders that track each wheel's distance and object detection Rexana knows where she is around the house and using voice commands to navigate around the house. Why? Paranoid you left the oven on after leaving the house... Rexana can be accessed on my phone via a browser to give text or voice command to "go to the oven" I can then view the oven via the web cam. Forgot to water the plants "Rexana water the pot plant in the lounge room"..feeling lazy... "Rexana bring me the Pringles". Rexana has custom "hands" that can be switched for purpose fit tasks, watering can, magnets, grippers. More demo here: https://rexanapaperai.wordpress.com/demos/ As Rexana is navigating around the house she takes note of detected objects (using Detectron2 + some custom object detection) I divided her viewpoint into left, straight and right. So I can ask her about objects she can see, she stores data about each object (compass bearing, X,Y coordinates based on wheel encoders and distance-based on lidar) this allows her to recall objects or go to recently seen objects via voice or text command. Using the above data I can also practice Spanish in a fun, immersive way with her by asking her what she can see "Que puedes ver aqui", "A la izquierda hay libros" a la derecha el television". Programmatic training her hand movements is very tedious, using 3D human body pose estimation I can train her much faster and intuitively to do tasks, she can copy my actions waving, gestures or picking up objects. She also has a retro-inspired dashboard for monitoring, training and manually controlling. How I built it Build Blog: https://rexanapaperai.wordpress.com/ Rexana is a physical robot made from scratch using 3D printed parts, several plastic plant pots, 8 servo engines, camera, wheel encoders,2 dc engines a 2D LIDAR a magnetometer and a Raspberry PI onboard computer. I used Pytorch Detectron2, 3D human pose estimation and experimented with Pytorch Geometric. Data is captured and formatted on the onboard Raspberry Pi then sent to an AWS server for realtime inference over web sockets which then returns the pose/detected/inferred results. Challenges I ran into Her arm dimensions and joints are very different from a human so pose estimation is not very accurate (version 2 will be bigger and more closely resemble human joint positions and dimensions Ran out of spray paint, so she has the "I'm going to take over the world" evil A.I look, will be giving a fresh paint job (white and pink) as well as stronger arms (one of the arms now has some stripped gears making is jerky and unpredictable) Accomplishments that I'm proud of Working proof of concept! What I learned PyTorch is awesome, the tutorials and libraries are a huge time saving, using existing building blocks I was able to focus more energy on the unique parts of my project. I burnt our 3 servo engines trying to get the arms working well so learned a lot about servo motor torque and how to power them. Autonomous, human sized and genuinely useful robots are achievable, although some of the functionality is basic or rough I was able to complete a proof of concept and the lessons learned and existing groundwork will make the next version significantly better. What's next for Rexana the Robot - PyTorch V2 bigger size, human dimension arms for better pose estimation, create docs, improve code and open-source. Self annotation and improve automatic training by showing objects and giving names and locations. More info and demos here: https://rexanapaperai.wordpress.com/ <div