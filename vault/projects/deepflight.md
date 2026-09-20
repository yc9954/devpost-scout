---
slug: "deepflight"
url: "https://devpost.com/software/deepflight"
title: "DeepFlight"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 491
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DeepFlight

> Autonomous tracking of objects using a swarm of drones with soft handoff procedure

[Devpost](https://devpost.com/software/deepflight) · hackathon [[MongoDB World Hackathon]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[developer_tools]] [[transportation]]
**substrate** [[structured_db]] [[video_visual]]

**stack** deep-sort, faster-rcnn, mongodb, mongodb-stitch, neural-networks, person-reidentification, pymongo, vehicle-reidentification

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for deepflight

## Body

drone movidius stick Inspiration Public surveillance has been around for a very long time. But the technology currently in use is fast becoming outdated and modern instruments such as UAVs are invading the space. UAVs are unmanned aerial vehicle than can be fitted with capabilities of autonomous flight, camera coverage and a lot more if given enough computing power. UAVs are mobile and they can perform actions such as target following based on the input feed through camera. What it does In this project, we've built such a system which does active tracking and can drive itself to follow the target. But what happens if the target escapes the UAV regardless? In a public surveillance scenario, we would have several drones monitoring their respective sectors. The Ground control station (GCS) relays communication between these drones to re-identify an escaped target. When a target goes off the frame of one of the drones, the tracking information collection helps to identify which neighbouring drone should come in to acquire the target again. This is what we call handoff! We have achived Multiple Object Tracking using Faster-RCNN, with which our drones are able to detect and track any and every object that enters or exits the frame. With vehicle and human re-identification we are able to re identify the lost object such that we can track the object after hand-off. We used movidius neural compute stick with raspberryPi on our drone to detect pothole. The movidius stick is used by deploying the layers before the fully-connected layer into it. The output of this deployed network is then transferred to the ground station to pass through fully connected layers and further tracking using deep sort. How we built it Deep sort algorithm is used for the actual tracking assisted by faster RCNN and reidentification. Dronekit is used for simulating quadcopters and controlling them. YOLO object detector is used for pothole detection. Raspberry Pi fitted with Movidius Neural Stick is used for online inference. PyMongo used with stitch connection string pushes the data of potholes to MongoDB Atlas Cluster. Client application receives flight and tracking data on socket.io. It also receives server sent events from Atlas for changes in mongodb database using Stitch-js SDK. Challenges we ran into Training of faster rcnn with visdrone dataset was a big challenge. Accomplishments that we're proud of We trained our tracker on Visdrone dataset. We also used change streams of mongo and server sent events of MongoDb Atlas. Our soft handoff procedure is able to make efficient assignments while choosing another drone for relocation of target. What we learned We now understand Dronekit-python library inside out. We learned to use mongodb cloud tools. What's next for DeepFlight DeepFlight features a soft handoff procedure for assigning a UAV for the task of relocation of target. We will be able to build it out further. Along with that, we can implement detection models for traffic violations like improper lane changes. <div