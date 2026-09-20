---
slug: "online-student-s-face-recognition-emotion-detection-system"
url: "https://devpost.com/software/online-student-s-face-recognition-emotion-detection-system"
title: "Online Student's Face Recognition & Emotion Detection System"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 439
team_size: 5
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Online Student's Face Recognition & Emotion Detection System

> "Face is the index of mind" - Facial features helps to read a student's mind whether he is interested in the classroom or not. This is a great way to analyze the student's involvement.

[Devpost](https://devpost.com/software/online-student-s-face-recognition-emotion-detection-system) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** azure, faceapi, machine-learning, powerbi, python, sql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for online student's face recognition & emotion detection system

## Body

Face Registration Portal image Video Analysis Portal Image Json in Azure Blob Sample json Power BI report 1 Power BI report 2 Power BI report 3 Inspiration We were inspired to create this app based on real life scenario where online classes are happening to be the new normal during Covid times. What it does This app captures the student's emotion like happiness, sadness, neutral, disgust, fearful, contempt, surprise and facial attributes like headpose, eye gaze, height, left, top and width which would help the lecturer to deliver better content to the students based on their mood. How we built it We have built this app using Face Azure cognitive service. Initially, all the students face will be registered in the portal. After registering the students face, in the Video analysis portal, lecturer will upload the class recordings and submit it. Once, the lecturer submits the video in the front end, the controller which uses python code will start splitting the video as frames per minute. Then, each frame is analyzed using Face API for finding the student's attributes and generate the output in json format. Json's will be stored in the Azure Blob. Json will comprise of student's emotion and facial features. In the next step, Json file is sent as an input to the Azure data factory. In Azure data factory, mapping is done between json from Blob and tables in Azure SQL database. Once, the mapping is done, pipeline is run and when the pipeline is successful, the records will be stored in the table in Azure SQL database with all the attributes and emotions. The table is then connected with Power BI to generate visualizing reports pertaining to each student. The power BI reports will then be used by the lecturer to understand the students and deliver the content based on their likes. Challenges we ran into Challenges to get deployed the web site in Azure for Public access. Challenges to publish the Power BI reports as these are licensed features. Challenges to break the video clip into Frames Accomplishments that we're proud of We are proud that we have built an app successfully which would be beneficial for both the students and the lecturer. What we learned We learnt how to build an app using Azure Cognitive Services (Face API) and Azure services (Azure VM, Azure data factory, Azure SQL server and Azure deployment tools). What's next for Online Student's Face Recognition & Emotion Detection System We can extend this app for further analysis on the students behavior for finding their eye ball movements, and also can be done for live online streaming. <div