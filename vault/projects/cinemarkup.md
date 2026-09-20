---
slug: "cinemarkup"
url: "https://devpost.com/software/cinemarkup"
title: "Cinemarkup"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 555
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/vision_ocr"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Cinemarkup

> A video annotation service, to upload and/or record videos and make time synced playback of annotations. The video content is automatically tagged, clasified and described using congitive service.

[Devpost](https://devpost.com/software/cinemarkup) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[vision_ocr]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** angular.js, azure, css, express.js, mongodb, mongoose, node.js, webrtc

## How they structured the write-up

- inspiration
- how we solved the problem
- how we built it
- differentiator
- what's next for cinemarkup

## Body

home page view annotations on the video AI tagging on a pre recorded video AI tagging on a recorded lecture video AI tagging on webrtc recorded video HLL diagram Inspiration Making time synced notes from an online lecture or video meeting is a challenge as it requires screen recording or heavy system installation for custom software. probelm we are trying to solve Reprocessing a video to preserve a sequence of notes is problematic because: it takes up space it infringes intellectual property rights and the textual DOM context is lost in the video file How we solved the problem Building a video file annotation editing and playback software which annotates video on the web interface and stores the annotations in a time labelled custom file format * Personalized time and position synced video annotation * Self annotating a video for frame specific notes and replaying the notes in time-sequenced and position correlated fashion. Save multiple custom notes for each individual viewer Each user can save notes separately and return them to them for reference later. * Lightweight and browser-based interface * Browser supported elements and resources to build an interactive user interface for editor and player. How we built it We built the front end in Angular.js and the backend in Nodejs and Express. We used MongoDB for the database and mongoose to manage the relationships between data and provides schema validation. We also used the Azure Computer Vision API to autogenerate tags and descriptions for videos. Challenges we ran into Manually classifiying the video . This was later solved by tagging from Azure AI Randomizing snapshots from long videos and compressing the video files for storage. This was solved using Azure blob storage Accomplishments that we're proud of Solvinig real world problem such as taking notes on recording videos lectures :) Appreciation from our professor and peers in the University Differentiator Taking notes on e-learning sites are usually in a separate text area referenced in one go, no matter how long the video MOOC platforms do not provide time synced notes with respect to the frame. Conventional Video Editors are heavy and system installation based A Service timeline.ly produces a time recorded notes JSON file but does not overlay notes / such as annotations and does not record coordinates Cinemarkup system Content creators can upload videos and record videos and edit annotations that sync up with the video. Users can easily search video annotations, so that they can go to the exact spot in a video where a certain annotation begins. A timeline below the video also shows the beginning and ending of each annotation. Users can add comments on videos to give feedback to content creators. When users record and upload videos, a snapshot is taken and this is run through the Azure Computer Vision API to auto generate tags and descriptions. No Intellectual property infringement or redundant screen recording of video content to save contextual notes information. Administrators have access to a dashboard that shows the number of videos and users, so that they can keep track of user engagement. The site uses single-sign on with Google for authentication. What's next for Cinemarkup We plan to add a recommended video section on the homepage, where users have custom content recommended based on the videos they watch and the comments they make. <div