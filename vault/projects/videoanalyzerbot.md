---
slug: "videoanalyzerbot"
url: "https://devpost.com/software/videoanalyzerbot"
title: "MyViewAssistant"
hackathon: "Junction 2016"
winner: true
words: 263
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
---

# MyViewAssistant

> This Bot is developed to help people with vision difficulties by analyzing videos and describing their content

[Devpost](https://devpost.com/software/videoanalyzerbot) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]

**stack** azure, azure-web-app, cognitive-services, computer-vision-api, luis, microsoft-bot-framework, opencv, signalr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for myviewassistant

## Body

Bot on Skype Inspiration Almost every family has a visual impaired person. Their daily life quality is highly improved over the past years, due to technology capabilities. Although, some things are still not figured out. For example, visually impaired people can use social media like Facebook thanks to Digital Narrators, but what if they stumble upon a video? Wouldn't it be great to be able to analyze it somehow frame-by-frame and get an overall description of its content? What it does MyViewAssistant is a Skype Bot that helps people understand the content of a video by analyzing it frame-by-frame and sending back descriptions How we built it We used: Microsoft Bot Framework and Azure and tailored the design for Skype. Azure App Service to host the Bot code WebJob to download and save the video OpenCV to analyze and extract the scenes from the video Azure Storage to store them Computer Vision API to get the description of each frame Language Understanding Intelligence Service for the User-Bot Interaction. Challenges we ran into A few difficulties binding all the different technologies and projects together OpenCV requires the video to be stored locally but the Bot was running on Azure Accomplishments that we're proud of Despite the difficulties, we managed to connect all the projects and create a solution that is scalable on the cloud What we learned To start simple and add functionalities on the way Work as a team Explored new technologies What's next for MyViewAssistant Beta testing for Intelligence and flow improvement Publish on Skype and other channels for public use <div