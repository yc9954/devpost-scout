---
slug: "truckrzzz"
url: "https://devpost.com/software/truckrzzz"
title: "TruckrZzz"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 588
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/web_dom"
---

# TruckrZzz

> An all-in-one smart solution for early drowsiness detection amongst truck drivers, providing smart solutions.

[Devpost](https://devpost.com/software/truckrzzz) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[web_dom]]

**stack** python, reflex, swift, terraapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for truckrzzz

## Body

Landing Page Manager Dashboard for Truckers Real Time Heartrate Graphing Mobile App that Receives and Sends Live Data Mobile Screen animating Webcam Alert Inspiration News frequently reports on vehicle crashes and accidents, with one statistic highlighting the prevalence of heavy truck accidents caused by driver fatigue. Truck drivers endure long hours on the road, delivering shipments nationwide, contributing to the tiredness that can lead to accidents. According to the National Transportation Safety Board, nearly 40% of heavy truck accidents originate from fatigue. In response, we pushed to develop a system capable of monitoring both facial expressions and heartbeats to detect early signs of fatigue among drivers. What it does Our web app boasts two features aimed at improving driver safety: one harnesses computer vision technology to track the driver's face, effectively detecting signs of drowsiness, while the other streams the driver's heartbeat in real-time, providing an additional layer of drowsiness detection. Accessible through our web app is a dedicated page for viewing the webcam feed, which ideally can be monitored via personal devices like smartphones. Should the webcam detect the driver falling asleep, it triggers an alert with flashing lights and a sound to awaken the driver. Additionally, our dashboard feature enables managers to monitor their drivers and their respective drowsiness levels. We've incorporated a graphing feature within the dashboard that dynamically turns red when a selected driver's drowsiness level drops below the acceptable threshold, providing a clear visual indication of potential fatigue. How we built it By combining Reflex and TerraAPI, as well as a companion mobile app in Swift, we were able to create a solution all within our ecosystem. The TerraAPI provided the crucial heartrate data in real time, which we livestreamed through a webhook that our Reflex website could read. The Reflex website also contains a manager-style dashboard for viewing several truckers and collect their unique data all at the same time. As a demo for future mobile usage, we also included a facial recognition and landmarking model to detect drowsiness and alert the user if they are falling asleep. The Swift app also provided additional information such as the heartrate in real time and establishing the connection to the webhook from the wearable device. Challenges we ran into In order to construct the complex data flow of our project, we had to learn several new technologies along the way. It started with developing on a new wearable device with limited documentation and support only through a Swift iOS app, which none of us had experience with. With Reflex, we also encountered some bugs, which all had workarounds, and the difficulties that come with developing any website. Accomplishments that we're proud of We're proud of being able to integrate such complex technologies and orchestrate them in a seamless way. At times, we were afraid that our product wouldn't come together since all the components depended on each other and we needed to complete all of them. However, our team made everything work in the end. What we learned Many of the technologies we worked with during TreeHacks were new and had a large learning curve in order to build our end goal. Along this journey, our team picked up valuable skills in Swift, Python, computer vision, web development, and how to work on 2 hours of sleep. What's next for TruckrZzz We hope to broaden our target audience and not only apply these technologies for truck drivers, but also every day drivers that might need some extra assistance staying awake on the road. <div