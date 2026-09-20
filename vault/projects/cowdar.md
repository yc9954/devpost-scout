---
slug: "cowdar"
url: "https://devpost.com/software/cowdar"
title: "Cowdar"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 477
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Cowdar

> A free, open-source iOS application that uses LiDAR technology to provide small scale farmers with accessible and accurate cow weight estimations.

[Devpost](https://devpost.com/software/cowdar) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[agriculture_food]] [[civic_government]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** arkit, fastapi, lidar, python, roboflow, swift, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for cowdar

## Body

View Past Scans and Predictions LiDAR / Photo Input View Prediction Labelled Points of Interest with Custom Trained YOLO v8 pose estimation model Labelled Points of Interest with Custom Trained YOLO v8 pose estimation model Additional feature input Example of LIDAR data Example 2 of LIDAR Data Example 2,Labelled Points of Interest with Custom Trained YOLO v8 pose estimation model Cowdar Inspiration Our research into cattle management revealed that existing automated weight prediction systems for livestock often fall into one or more of these categories: Prohibitively expensive Subscription based Low quality Many government-funded projects in this space have been abandoned or remain unavailable to the public. We wanted to bridge this gap for small time farmers by creating a free, open-source tool that leverages the hardware already in their pockets. What it does Estimates the weight of cows using a LiDAR snapshot and a photo. How we built it Trained a custom yolov8m-pose model with 100 epochs using a dataset of labelled cow poses created by Sorin Workspace — 1042 total images ( 729 training, 209 validation, 104 testing) — to analyse points of interest on the cow (approx 30 min on Nvidia T4) This model outputs a set of normalised coordinates (normalised refers to a relative x,y value range of 0–1 , as opposed to pixel measurements) The 3D LiDAR point cloud is mathematically projected onto a 2D image plane The server matches the normalised coordinates to the closest projected 3D LiDAR points to determine (estimate) the physical distance between points of interest on the cow 3D Euclidean distances are extracted between these coordinates (e.g., body length and radius) Weight is predicted using a variant of Schaeffer's Formula Challenges we ran into Figuring out how to get LiDAR data of a moving object The dark hide of Angus cows is much harder to parse points of interest on Our limited knowledge with maths and AI limited the approaches we could use to predict weight Labelled cow pose datasets were limited in availability, quality, and size — the time scope of our project meant we couldn't hand-label poses on Angus cows Schaeffer's Formula doesn't account for features like body fat, breed, sex, or age Accomplishments we're proud of Successfully creating a functional proof of concept that integrates LiDAR hardware sensors with modern AI models Developing a pipeline that transforms raw LiDAR and photo data into a meaningful physical measurement (weight) Keeping the project entirely open source to ensure it remains accessible to the farmers who need it most Developing an extensible project What we learned iOS Development Interacting with phone hardware sensors Using Cloud VMs to speed up parallelisable neural network training What's next for Cowdar Increase prediction feature count and make a more accurate prediction Manually annotate pose data to grow community cow pose datasets Pre-process LiDAR and photo data further to improve model accuracy <div