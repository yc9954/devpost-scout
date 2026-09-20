---
slug: "stretchbreak"
url: "https://devpost.com/software/stretchbreak"
title: "stretchBreak"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 871
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# stretchBreak

> With stretchBreak, we aim to improve the quality of life of students and working professionals by helping them get a break from their routine meetings, flex and open up their body!

[Devpost](https://devpost.com/software/stretchbreak) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[educator_student]] [[patient_family]]
**substrate** [[code_repository]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** api, azure, cognitive, css, html, javascript, posenet, services

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stretchbreak

## Body

Inspiration Sitting is the new smoking! With the pandemic setting in, most of the communication is taking place online which demands us to spend long hours at the desk. Not moving is the biggest health hazard as our body has been naturally designed to move. With stretchBreak, we aim to improve the quality of life of students and working professionals by helping them get a break from their routine meetings, flex and open up their body! Get moving with StretchBreak and improve your productivity and efficiency at work! What it does Our application gives the workaholics a reminder every three hours to leave their desk and do some stretches. We have linked some agility and mobility videos in our application. We first ask the user to input the duration(5 mins, 10 mins or 15 mins) of the stretch break he wants and his current fitness level(beginner, intermediate or advanced). According to his selection, we show him a video which he can follow along. We then capture the user’s movements as he’s doing the stretches by connecting to his webcam. Through this captured data, our model calculates the energy expended by the user as he is doing the exercise. Additionally, our model also compares the user’s movements to the movements in the stretching video. At the the end of the stretching session we display two things to the user His energy score How accurate his movements were Further, we have used the Microsoft Azure Cognitive Services API to read the facial expressions of the person as he’s taking his stretch break to detect extreme distress or fatigue on his face. If such signs are displayed, the user is prompted to stop his exercise and is given the option of quitting the follow along video. How we built it We build our model using Posenet(a machine learning model which allows for real-time human pose estimation). Alongwith this, we have also use the Microsoft's Pose API to find the key-points like nose, eyes, shoulders and knee as the person in exercising. Our model primarily works for a single pose detection The pose estimation happens in two phases: An input RGB image is fed through a convolutional neural network. A single-pose decoding algorithm is used to decode a pose(which is an object that contains a set of key points and an instance-level confidence score for each detected person), pose confidence scores, keypoint positions (A part of a person’s pose that is estimated, such as the nose, right ear, left knee, right foot, etc. ), and keypoint confidence scores from the model outputs. We built and deployed our model on the Microsoft Azure Platform by syncing our Github repo to the platform. Thus, whenever we committed any code in the Github repo, this was automatically built and deployed on the Microsoft Azure Platform. Further, we used the Microsoft azure cognitive services api to detect the facial expressions of the person when doing their workout. Challenges we ran into Direct support for libraries like opencv, tensorflow, posenet was not provided, hence we needed to create a Docker Image and then deploy that Accomplishments that we're proud of We were able to help the user understand the accuracy of his movements as he doing the follow along video We were able to display the energy level of the user as he was doing the workout We were able to detect if there was extreme fatigue or distress as the person was doing the workout and thus advise them how to proceed. What we learned The discussion posts and communication done via the Microsoft slack channel spearheaded by the Microsoft employees were very helpful. We got inputs on how we could resolve our issues and improve our code. We learned how to deploy our docker containers to Microsoft Azure App services and further learnt how to use use the Visual Studio Code IDE. We also learnt how to connect our Microsoft Azure directly to our Github repo. This was very beneficial because whenever we committed any changes to the Github repo, our model would automatically be built and deployed in the Microsoft Azure Platform. We also learnt how to create a Docker Image and by creating our own start.sh file, we were able to customize the runtime environment What's next for stretchBreak Improve the workout suggestions by taking into account the underlying health conditions and fitness goals of the person. For instance, a person may be experiencing a stiffness in his neck at some point, thus we would want to understand that and suggest a follow along video which could help him relieve that pain. We want to be able to help doctors use our application to detect the level of distress displayed when a person using stretchBreak while exercising and make inferences about their current health status. We want to tweak our model so that physiotherapists can use our application to inform patients how well they are doing the exercises prescribed to them. Additionally, we also want to extend our application to sports champions to help them improve their game. For instance, our application can tell a tennis player if he is holding his racket in the correct position and hitting the ball with the correct speed. <div