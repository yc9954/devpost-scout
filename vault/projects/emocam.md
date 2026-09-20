---
slug: "emocam"
url: "https://devpost.com/software/emocam"
title: "emoCam"
hackathon: "Microsoft Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 411
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# emoCam

> The face is more honest than the mouth can ever be. emoCam literally provides you with the best insights on how your customers or employees feel about your business.

[Devpost](https://devpost.com/software/emocam) · hackathon [[Microsoft Azure AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** azure, cognitivefacepythonsdk, faceapi, microsoftlifecam, opencv, powerbi, python, raspberry-pi, raspbianstretch, sql

## Body

emoCam Architecture power BI screeenshot Inspiration The opportunity of using a better understanding of customer perception of a brand to impact productivity has been a passion of mine. The breakthrough came with realizing that by analyzing customer facial expressions, I can understand what they failed to express verbally. This meant i could link people's feelings to productivity by interpreting their expressions. This was the birth of the idea, emoCam. What it does emoCam captures images in small time intervals, interprets the expressions and then sends this information to the intelligent cloud. The data on the cloud is further analyzed and visualization was done with Power BI to provide insights. Client-facing organizations such as restaurants and supermarkets can use emoCam to obtain feedback on their customer’s perceptions of their services as well as better assess workplace satisfaction of their staff. This ultimately leads to these organizations making insightful decisions that will impact productivity, appeal to customers and eventually improve profits. How we built it This prototype of emoCam architecture consists of the device, cloud and business insight application. A Microsoft HD Lifecam HD-3000 and Raspberry Pi 3 with Raspbian Stretch operating system were the major components of the device. OpenCV, Cognitive Face Python SDK, and Azure IoT Python SDK. OpenCV was used to access the camera for real time capturing. I created a Face resource after getting my free account and then copied the endpoint and key which i used in my python script to access the API. The reply from the API was parsed and the emotion data gotten was sent to the IoT hub. The IoT hub was created and the device was registered, a streaming job was created to stream data coming from the hub into a Datalake Gen1 Storage service. Power BI ties into these data and creates the final user-friendly visualization for providing insights. Challenges we ran into In building the prototype, deciding on which Azure resources should be selected was challenging as a thorough understanding alongside balancing cost with expected performance was needed. Accomplishments that we're proud of This hackathon spurred me to make use of Microsoft’s cognitive service APIs. My initial impression was that this was going to be a complex task, upon understanding the service, I was able to easily build this and see it work end-to-end. What's next for emoCam This working solution is a prototype of emoCam’s capabilities. The next stage would be to see it mass-produced and adopted by businesses.. <div