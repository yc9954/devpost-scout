---
slug: "drive-sense"
url: "https://devpost.com/software/drive-sense"
title: "Drive Sense"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 289
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Drive Sense

> Through CV models and LLMs, we are increasing road safety, and assessing a driver's safety rating, by correlating behavior with the road conditions.

[Devpost](https://devpost.com/software/drive-sense) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]

**stack** cohere, django, opencv, pytorch, react, replit, streamlit, yolo

## How they structured the write-up

- inspiration:
- what it does

## Body

DriveSense Inspiration: Our inspiration for this app comes from the critical need to improve road safety and assess driver competence, especially under various road conditions. The alarming statistics on road accidents and fatalities, including those caused by distracted driving and poor road conditions, highlight the urgency of addressing this issue. We were inspired to create a solution that leverages technology to enhance driver competence and reduce accidents. What it does Our app has a frontend, which connects to a GPS signal, which tracks the acceleration of a given car, as well as its speed. Such a React frontend also encompasses a Map, as well as a record feature, which, through the implementation of a LLM by Cohere, is capable of detecting alerting police, in the event of any speech that may be violent, or hateful, given road conditions. On the backend, we have numerous algorithms and computer vision, that were fine-tuned upon YOLOv5 and YOLOv8. These models take in an image through a camera feed, surrounding cars, the color of the surrounding traffic lights, and the size of the car plates in front of the drivers. By detecting car plates, we are able to infer the acceleration of a car (based on the change in size of the car plates), and are able to asses the driver's habits. By checking for red lights, correlated with the GPS data, we are able to determine a driver's reaction time, and can give a rating for a driver's capacities. Finally, an eye-tracking model is able to determine a driver's concentration, and focus on the road. All this paired with its interactive mobile app makes our app the ultimate replacement for any classic dashcam, and protects the driver from the road's hazards. <div