---
slug: "safe-trace"
url: "https://devpost.com/software/safe-trace"
title: "Safe Trace"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 401
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Safe Trace

> Analyse your trace for a safer workplace.

[Devpost](https://devpost.com/software/safe-trace) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** claude, fastapi, flask, gemini, node.js, python, ultralytics, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safe trace

## Body

Inspiration Computer vision is a really powerful technology. There are many accidents in the workplace that could be avoided with correct PPE and following of procedures. We decided we could apply modern technology to create a safer work environment. What it does Using computer vision, Safe Trace determines the use of correct PPE in a work environment, and calculates a "safety score". The tool can be used by employers to ensure procedures are being followed, and dangerous work environments are much safer. How we built it We used a Raspberry Pi with a camera module and streamed that to a home computer acting as a server via the WiFi network. We trained a computer vision model on a large dataset of Personal Protective Equipment, which then scans the footage to determine what PPE a person is or is not wearing. We created a node.js user interface to watch the footage, and choose which PPE the model would look for, and then calculates a safety score at the end of the day based on the number of violations that did occur, divided by the total number of violations that could have occured. Challenges we ran into None of us had worked with computer vision extensively in the past, and this was our first time training an AI model, which was quite challenging. Having to download the correct older versions of various softwares to be able to run on our hardware limitations also took quite some time, as well as the usual headaches that occur when using multiple devices (Raspberry Pi, home computer) together. Accomplishments that we're proud of We're really proud of being able to have trained our own model, as well as being able to produce such a nice user interface in such a short amount of time. What we learned Dealing with large datasets can be very difficult. Often the most time consuming part of the programming is ensuring that all the versions, modules, packages, programs are correct and cooperating with one another, and not necessarily the programming itself. What's next for Safe Trace We want to be able to expand this to detect more hazards, using more AI models, and want to be able to implement a 'heat map' of a work environment that could help show the danger zones of an area and aid in being able to prevent future hazards, rather than just detect current ones. <div