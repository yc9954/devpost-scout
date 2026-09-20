---
slug: "zoom-education-suite-zest"
url: "https://devpost.com/software/zoom-education-suite-zest"
title: "Zoom Education Suite (ZEST)"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 571
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Zoom Education Suite (ZEST)

> A series of Zoom enhancements designed to augment the remote learning experience.

[Devpost](https://devpost.com/software/zoom-education-suite-zest) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** gcp, google-cloud, python, selenium, tkinter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zoom education suite (zest)

## Body

screenshot of the final working state screenshot of video feed going to our facial expression analysis system screenshot of results of facial expression analysis Closed Captioning Example Inspiration A worldwide pandemic has pushed education out of the classroom and into online forums for much of the world. Zoom has emerged as one of the services leading the way in the transition to internet lessons. While certainly a capable platform in its current state, Zoom possesses some inherent limitations as a classroom substitute. We at Zest believe optimizations could be made to improve user accessibility along with providing better engagement metrics to the instructor. What it does Zest helps professors better interact with those in their class and track their students' comprehension of the material with numerous ways to collect more data about classroom engagement. (i.e. Total number of hands raised, class attendance, call on students) Zest creates a more accessible online classroom with its closed captioning service. This allows users with limited hearing to follow along more closely which improves usability. How we built it As a result of the fact that Zoom offers no API for a lot of what we wanted to track (see the next section for details), we built a bot using python and selenium to join the call (headless-ly) and collect all the information from the browser client in the background of the host's computer. The data gathered using our python + selenium component is fed into our python + tkinter interface that is displayed on the host's computer, alongside their Zoom client. Connected the Twilio API with Google's Speech to Text API to call into and get live audio from the Zoom call and provide live closed captioning during calls Used Google's Computer Vision for Image Recognition: Using Google Video Intelligence to locate frames that included a person, this would then be passed onto Vision API which would assess the emotions exhibited by those in the frame. Challenges we ran into Zoom has no API for accessing a lot of the features we wanted to use, like the number of people raising their hands, the ability to send messages, the ability to get current users, etc. While we had success with actually doing recognition of facial expressions and live closed captioning, while they do work, we did not have time to integrate their results directly into our local client that contains the rest of the features. Unfamiliar with Google's cloud computing platform, we had some struggles integrating their Vision API for emotion detection. One of the bigger issues here was in extracting single frames from Zoom to run analysis. Accomplishments that we're proud of Built a self-contained, fairly full-featured client to interface with the Zoom client headless-ly Got live closed-captioning working in Zoom (see streamable link in additional links section for demo video of that, separately) What we learned Throughout the hackathon we were in contact with the Google Cloud API through various manners, whether for subtitles or image recognition. We were also able to better grasp how large scale third-party applications can make use of API's such as Zoom's to offer a different experience and/or a better one. What's next for Zoom Education Suite (ZEST) Full integration of the results of all of our features (closed-captioning and facial expression analysis) into the main python + tkinter client that already serves everything from our python + selenium interface Bot-prompted activities, games, live-video labeling, etc. <div