---
slug: "mall-monitor"
url: "https://devpost.com/software/mall-monitor"
title: "Mall Monitor"
hackathon: "Hack the North 2020++"
winner: true
words: 608
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Mall Monitor

> What started off as a COVID-19 tracking system for malls, turned into something that tracks height and links each person with a unique tracking ID and their accessories. This uses the model YoloV3.

[Devpost](https://devpost.com/software/mall-monitor) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[transportation]]
**substrate** [[regulation_legal_text]] [[structured_db]] [[web_dom]]

**stack** angular.js, azure, css, flask, html, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for mall monitor
- check it out!

## Body

Tracking of people with unique ID's (green box represents incoming clients) Quick view of our web app! Inspiration Covid-19 has ravaged the World since early 2020. We know businesses have struggled to stay open. Mall Monitor aims to helps businesses stay open and adhere to public health guidelines by keeping track of the amount of people going in and out using an ML-powered system. What it does Mall Monitor allows owners and guests to monitor the entrance of a location. We allow those that have permission to monitor the statistics of the number of people, and set limits to how many are allowed (inspire!submit https://devpost.com/software/mall-monitord by the COVID restrictions). This will tack the lack of accountability in following the regulations of protocols and can be expanded further to marketing and security as we have extracted height information as well. Mall Monitor performs object detection and tracks incoming and outgoing people through a doorway. Traffic monitoring is not new, but our pipeline integrates object tracking along with detection and links unique ID's to each user. The accessories they hold (eg. handbag, backpack, etc) would also be detected through YOLOV3 and linked to their respective ID. How I built it We build a web app using HTML, CSS, Angular and hosted on Azure. We created the interactive prototype design here - https://www.figma.com/proto/725OYn6LXYUiCvJKx2DKBv/Lo-fi-Wireframe?node-id=5%3A2&scaling=min-zoom to guide our thought process. For the ML side of things, we used OpenCV for object detection through YOLOV3 ( https://www.researchgate.net/figure/Network-architecture-of-YOLOv3_fig1_339763978 ) and incorporated the object tracking using motpy ( https://github.com/wmuron/motpy ). Challenges I ran into We struggled to deploy our model as a REST API to Azure, because of environment conflicts in python. This made it difficult to integrate our project like we wanted to. With the data-intensive nature of neural network models, we were unable to have a fully integrated system in 36 hours. We felt well-prepared at first, but ran into unexpected issues of not being able to upload the model weights to github, therefore unable to deploy in the method we had first anticipated. Accomplishments that I'm proud of As a team, we worked hard and came together from a pool of diverse talent. We have specialties in backend, frontend, ML, and UX/UI. To be able to come together and build a project to near completion was something we are proud of. What I learned ML models come in different flavours. Deploying a face detection algorithm is not as easy as deploying a simple prediction app. We've learned to expect the unexpected. When things are expected to go one way, we need to have many plans laid out. What's next for Mall Monitor Actually deploying and consuming the REST API at the frontend. Security applications - Since the model detects objects, it can help guard against theft. We are able to calculate approximate heights and tag accessories to each unique person and not only detect, but also track each user. The next step is the fully integrate the systems together and reach out to those that could benefit from this project! Especially in the currrent pandemic, many stores could use the help to trace the number of people and ensure that we are all following the regulations. We could further this project into marketing (detecting the demographic information and know the traffic flow at certain times at specific doorways), and security (with heights calculated already, it is trivial to have a database with information that could increase security). Check it out! Check out our different sections of the pipeline! ML: https://github.com/timtinlong/HTN.git , Front-end: https://github.com/RemeAjayi/mall-monitor , Back-end: https://github.com/restia1230/HackTheNorth , Web app: https://socialdistancemonitor.azurewebsites.net/ Check it out here! YT: https://www.youtube.com/watch?v=dEP8Vio41e0&ab_channel=TimYu Check out our web app! https://socialdistancemonitor.azurewebsites.net/ <div