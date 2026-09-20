---
slug: "updatemy-tech"
url: "https://devpost.com/software/updatemy-tech"
title: "UpdateMy.Tech"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 319
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "substrate/video_visual"
---

# UpdateMy.Tech

> Update your IoT devices over the air, all in one place.

[Devpost](https://devpost.com/software/updatemy-tech) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[sensor_fusion]]
**substrate** [[video_visual]]

**stack** c, flask, google-cloud, mongodb, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for updatemy.tech

## Body

Select your device Upload your firmware Your IoT devices will now automatically update over the air Inspiration Our project was conceived out of the need to streamline the outdated process of updating IoT devices. Historically, this was an unmanageable task that required manual connections to each device, a daunting challenge when deploying at scale. Moreover, it often incurs significant expenses, particularly when relying on services like Amazon IoT Core. What it does UpdateMy.Tech addresses these issues head-on. Gone are the days of laborious manual updates and the high Amazon costs. With our system, you can effortlessly upload your firmware and your IoT device will flash itself with zero downtime. How we built it To realize this vision, we used Taipy for the front and back end, MongoDB Atlas for storing binary images, Google Cloud to host the VM and API, Flask to communicate with Mongo and IoT devices, ESP-IDF to build firmware for the ESP32, all to enable OTA (Over-The-Air): The underlying technology that enables automatic updates, eliminating the need for manual intervention. Accomplishments that we're proud of Our proudest achievement is creating a user-friendly and cost-effective IoT device management system that liberates users from the complexities and expenses of previous methods, including reliance on costly services like Amazon IoT Core. Technology should be accessible to all, and this project embodies that ethos. What we learned This project served as a profound learning experience for our team. We gained insights into IoT device management, cloud technologies, and user-centric interface design. Additionally, we honed our expertise in firmware development, skills that will prove invaluable in future endeavours. What's next for UpdateMy.Tech Our goal is to reduce the barrier of entry for hardware hacks by simplifying IoT device management. The future of "UpdateMy.Tech" is to enhance and broaden our solution's capabilities. This includes adding more features on top of updates and extending compatibility to a broader array of IoT devices. <div