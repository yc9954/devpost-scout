---
slug: "roomie-vp4m6t"
url: "https://devpost.com/software/roomie-vp4m6t"
title: "Roomie"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 317
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# Roomie

> A web app that takes in data regarding all class times, classroom reservations, and motion detected in a room to display a list of available rooms. Students can use the available rooms for studying.

[Devpost](https://devpost.com/software/roomie-vp4m6t) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** c++, esp32, mongodb, node.js, nodemcu, react, sensor

## How they structured the write-up

- inspiration and function
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for roomie

## Body

Mobile Interface Whiteboard Whiteboard Inspiration and Function As college students, we are always looking for a place to study. The issue is, that spending so much time looking around buildings for unoccupied rooms is something that is extremely inefficient and tiring. We decided we wanted to put an end to this arduous endeavor by creating an application that takes into account the classes that are currently going on and rooms that are currently taken to reveal rooms that are available to be used for studying immediately. How we built it We used NodeJS to build a REST API backend that interfaces with official Coursebook data, accesses API data from a React frontend, and uses TCP to communicate motion sensor data to the server, and MongoDB Atlas to store room reservations. Challenges we ran into Ensuring data checking server side was consistent and deciding on and implementing data structures and formats of class data was also difficult for early React learners. Additionally, some of our hardware came defective from the factory and we didn't have duplicates. We developed the code for a screen that would show what the schedule for a room looked like as you walked by, but it didn't make it into this design. On the plus side, we never would have added the occupancy indicator LED with the screen present in that area of the board. It allows you to see if someone is in a room from a significant physical distance. Accomplishments that we're proud of Instant communication between server and motion sensor, a React interface that displays all rooms available in the building, and the robustness of the developed REST API. What we learned API pagination, TCP communication, React, and the integration of motion sensors with Arduinos. What's next for Roomie Further flesh out the reservation system, improve the reliability of search results, check values at different times, and add the screen. <div