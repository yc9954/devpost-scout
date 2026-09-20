---
slug: "securestep"
url: "https://devpost.com/software/securestep"
title: "SecureStep"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 750
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# SecureStep

> Helping you walk with confidence.

[Devpost](https://devpost.com/software/securestep) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[elder_child_care]] [[labor_employment]] [[transportation]]
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[geospatial]] [[web_dom]]

**stack** 3dprinting, c, caffeine, esp8266, friendship, github, google-cloud, javascript, mappedin, react, solidworks, unix

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for securestep

## Body

Cool hardware project!? :O Hardware Mount Webpage Client (No Fall Detected) Webpage Client (Fall Detected & Path to Geolocation) SecureStep Logo Inspiration With evolutions in bipedal robotics, balance has become something that we take for granted. Yet despite the many steps taken forward in advancing technological walking, we've neglected to innovate and support our elderly populations with their mobility issues. The older we get, the more dangerous a fall can become. We set out to create a solution that provides instant aid to seniors that have been involved in loss of coordination, applying advanced technology and APIs to locate and support them. What it does SecureStep is a smart walking cane designed for seniors in old age homes, responsible for notifying care workers when a fall has occurred. SecureStep's built-in sensors detect falls and transmit an exact geolocation of the incident. Paired with the power of the MappedIn SDK, the geolocation is published to an in-depth floor plan of the old age home, alerting caregivers of the incident, and the best indoor route to reach the victim. Communication over Wi-Fi between the cane's microcontroller and a local webpage ensures urgent care for a fallen senior. Any location covered by the Wi-Fi network will allow the cane to connect to the webpage, enabling long-range data communication. The webpage displays a list of the cane's acceleration and gyration data, along with the longitude and latitude. A map of the floor plans is also included and displays a route to a senior after a fall has occurred. How we built it SecureStep was developed with many technologies. The mechanical enclosure was designed in SolidWorks, with space allocated for an ESP-8266 microcontroller, a 6V battery pack, an MPU6050 accelerometer/gyro sensor, and an RGB LED used for displaying cane status (blinking blue - connecting to Wi-Fi, solid blue - searching for react webpage server, green - connected and upright, red - fall detected). The ESP microcontroller transmits the MPU data to a react webpage via a built-in Wi-Fi module, processing the acceleration of the cane to verify whether a fall has occurred. The ESP also calls the Google Cloud Geolocation API to triangulate its latitude and longitude based on other Wi-Fi devices on the network. The react webpage receives and displays all raw data, along with a MappedIn map of E7. The map is updated with the latitude and longitude of the cane only when a fall is detected, and a path is drawn from a dedicated medical zone to the incident location. Once the cane is returned to its upright position, the fall detection warning is removed along with the path. This ensures that a cane falling on its own and picked back up does not generate a false positive. Challenges we ran into The first (and definitely most annoying) challenge we ran into was uploading code to the ESP module. After an hour of verifying drivers, chugging coffee, and praying to C itself, we realized that our micro-USB cable was unable to transfer data... :/ Besides small annoyances and hurdles to overcome, a significant amount of time was spent trying to perfect the communication between the ESP and the webpage. With over 1000 people using the HTN Wi-Fi network, our solution had to find the right balance between polling for information and not blowing up our ESP! Accomplishments that we're proud of Our team is incredibly proud with the speed in which we developed our idea and brought a fully functional prototype to fruition over the course of the weekend. With no pre-planned idea or resources, we let the technology speak to us and guide us over the past two days! It's truly a reward to have finished a project that not only helped us to learn more skills but also created a solution to a very real problem that affects elderly people across the world. We were also excited to work with amazing sponsored technology, and implement solutions to expand on their API functionality, taking our project to the next level :) What we learned It wouldn't be a hackathon if we had learned nothing. SecureStep has been a fantastic opportunity for our team to try out new APIs, take a crack at web development with React, and expand on our understanding of network communication and synchronization. What's next for SecureStep Moving forward, there are a few changes we'd love to add: Make an enclosure that can withstand a full drop Create better compatibility for mobile devices Speed-up the Wi-Fi communication <div