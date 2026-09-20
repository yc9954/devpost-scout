---
slug: "mirr-wait-for-it-or"
url: "https://devpost.com/software/mirr-wait-for-it-or"
title: "Mirr...wait for it... or!"
hackathon: "Junction 2017"
winner: true
words: 466
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Mirr...wait for it... or!

> We created a behaviour for Pepper that allow him to recognize some human's actions and repeat them.

[Devpost](https://devpost.com/software/mirr-wait-for-it-or) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[agriculture_food]]
**substrate** [[structured_db]] [[video_visual]]

**stack** machine-learning, opencv, pepper, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mirr...wait for it... or!

## Body

Inspiration Pepper is a great robot possibly capable of such things that we can't even imagine. But he still has some problems with learning it. It can do pre-defined things like showing an elephant or tracking something, but we want to make him more impressive. So we decided to add a bit of knowledge to his brain - knowledge about how to repeat after a human. What it does This project allows robot to recognize human movements and try to repeat after him. It use image recognition and neural networks capabilities to find out how do you move your hands and then ask Pepper to make same movements with his hands. How we built it Project consist of 2 parts - robot behaviour project and server that classify human movements. Robot behaviour Robot behaviour project do next things: Provides voice interface between human and Pepper Takes pictures of human and send them to server that tell robot what to do Translate server's commands into hands movements and some speech Inside the robots there's behaviour's project with Python scripts and hands animation Server Server is responsible for classifying human's hands movements and sending a robot commands how to move his hands. How it works: Server receive an image from robot Then server find human's hands (with OpenCV lib) and crop image to classify them Tensorflow-built network classify movements and answer with some hand's action that's sent back to robot Challenges we ran into There were some difficulties during our work: How to write code for Pepper properly in order to make his movements more human-like, not to lock unnecessary resources and make it rather optimized? How to organize proper client-server interaction using only built-in libraries and functions? How to collect and prepare dataset for neural network that will teach it in most proper way? How to plan and built such neural network that it'll be capable of classifying human movements and not-so-much-slow-while-training in the same time? Accomplishments that we're proud of Rather high accuracy of human movements recognition (in an ideal situation - about 96%. in real - ~83%) Fully working behaviour (it really works as expected :D) Combining multiple technologies in single app to achieve our goal Our own dataset! What we learned Pepper programming OpenCV knowledge and usage Low-level client-server architecture on Python Team spirit and conflict avoidance improvement ^^ What's next for Mirr...wait for it... or! Our project - just first step on the track of extending Pepper's capabilities by machine learning. It can be used in such areas like Pepper's teaching, performing simple human-like autonomous tasks and some other things that you can imagine. Right now it capable of mirroring your hands movements but it's rather simple to add other behaviour like moving back/forth or even trying to dance with you =) <div