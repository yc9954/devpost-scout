---
slug: "afrifarm"
url: "https://devpost.com/software/afrifarm"
title: "AfriFarm"
hackathon: "Microsoft Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 228
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# AfriFarm

> Let's help end world hunger

[Devpost](https://devpost.com/software/afrifarm) · hackathon [[Microsoft Azure AI Hackathon]]

## Facets

  <sub>weak: realtime_stream</sub>
**domain** [[agriculture_food]] [[civic_government]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** azure, java, kotlin, machine-learning, python

## How they structured the write-up

- how i built it
- how to test

## Body

Africa is home to over 200 million small holder farmers who are dependent on farming not only for consumption but also their livelihoods. These farmers face numerous challenges when it comes to crop production, chef being the recognition and treatment of crop diseases. NGOs and Government agencies provide support to these rural farmers, however this help usually arrives late when farmers have lost their crops. Afrifarm plans on solving this issues. Afrifarm is an app that recognizes crop diseases from images and publishes the findings on a public dataset where anyone can view the breakout and movement of diseases. From there Government agencies can have a real time or historical view of crop disease outbreaks and provide support to the affected community immediately an out break occurs. Crop disease outbreaks can be viewed by location and timeline at any time. How I built it The app uses a custom Tensorflow model which is trained to detect various diseases on the following crops. -Apple -Blueberry -Cherry (including sour) -Corn (maize) -Grape -Orange -Peach -Pepper, bell -Potato -Raspberry -Soybean -Squash -Strawberry -Tomato The app uses ArcGis' Android API to display reports across African map and to allow NGOs to interact with them How to test -Download the app the attached files of this submission https://alexaforgood.s3.amazonaws.com/app-debug.apk -Test with an image containing a crop disease e.g https://drive.google.com/file/d/1LSkPC5Zp9uxT7BmtN7g4mbrnlXaAHuJ_/view?usp=sharing which contains corn rust <div