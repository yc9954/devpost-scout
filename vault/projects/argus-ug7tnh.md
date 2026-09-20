---
slug: "argus-ug7tnh"
url: "https://devpost.com/software/argus-ug7tnh"
title: "Argus"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 191
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/video_visual"
---

# Argus

> Assisting blind people in navigating the world

[Devpost](https://devpost.com/software/argus-ug7tnh) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[video_visual]]

**stack** azure, javascript, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for argus

## Body

screenshot Inspiration This project is inspired by the YouTube channel 'Stuff Made Here' in this video What it does Argus helps blind people navigate the world by providing haptic feedback to the user. How we built it I first created a prototype React web app that can activate camera in both desktop and mobile. After that, I had to extract the frame, turn it into an image, then feed it to the Azure Computer Vision API. Challenges we ran into This is my first time working with video and cameras in a web application, and I had not expected it to be so different to images. From the styling to transforming it to a format that the Azure Computer Vision API can understand. Accomplishments that we're proud of Progressive Web Apps are very new and I am happy that I'm able to leverage its capabilities to record videos and generate haptic feedback on a mobile phone through a web application. What we learned Azure AI ecosystem and how to deal with videos and canvasses. What's next for Argus The application can interact with the user to better understand their needs <div