---
slug: "track-my-bike"
url: "https://devpost.com/software/track-my-bike"
title: "Track My Bike"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 563
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Track My Bike

> A network of bike trackers where bikes work together to safely, securely, and automatically share locations to deter theft and aid in fast recovery. Easy to add to bike, easy to use.

[Devpost](https://devpost.com/software/track-my-bike) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[finance_payments]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** arduino, astra, cassandra, css3, datastax, esp32, express.js, gps, html5, javascript, node.js, solidworks, svelte

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for track my bike

## Body

Track My Bike Website Service Node Module GPS Node Module GPS Node Module Tracker API Inspiration In 2019, over 2 million bicycles were stolen from their owners in North America alone. Recovering those stolen bicycles is very unlikely, with only about 5% being returned to their rightful owners. With the rise in popularity of bicycling in the past year, this number of stolen bikes is likely to further increase. Track My Bike is a simple, low-cost, cheap GPS tracker for bicycles. While some trackers do exist in varying capacities, they often have high monthly service fees and limited coverage. Track My Bike seeks to solve these two problems in a novel fashion. What it does Track My Bike utilizes mesh networking to create a massive, interconnected network of bicycles within an area. Participating cyclists attach a small module including the GPS tracker to the frame of their bike. An existing water bottle mount can be used. Every bike records their own id number, location, time, and date data and broadcasts it through the mesh to other bikes it passes. Some bikes are known as service node bikes and will include additional code that reports data collected to the main database. This database can then be searched to find lost bikes and their last locations. Additionally, service nodes will be placed throughout the city so service node bikes can report regularly. How we built it Track My Bike consists of several projects: Electrical: GPS module was used to collect GPS information to an ESP32. The ESP32's were connected to wifi and transmitted data. Mechanical: A 3D printed case was designed in SolidWorks and printed. Easily mounts on a water bottle screw mounts on bikes. API: GPS location data was transmitted from service node ESP32's to the DataStax Astra database to hold GPS data, trackers, and user data. Front End: An easy interface designed for users to find their bike. Challenges we ran into Some big challenges were getting the GPS module to work. During the whole hackathon the sky was cloudy or raining so getting initial GPS connection was difficult. Additionally, transmitting GPS data from one node to the service node was tough because we wanted discrete points of data and not a constant stream. Accomplishments that we're proud of We are very proud of how finished the final product looks. The node is very simple to attach to a bike and does not add any bulk. The data collected from the GPS module is also very accurate and will help bikers accurately find their bike. What we learned We have learned that it is best to split up and work on different parts of the project but also communicate clearly between the groups. Additionally, we have not worked with GPS modules or ESP32s before so that was a fun time. What's next for Track My Bike There are several hardware improvements that could be implemented: Compact, integrated battery with wide range of charging options Integrate an IMU to determine when the bike has started/stopped moving to only report data when necessary Further modifications in design to lower overall power consumption to extend battery life LoRaWAN and mesh in place of WiFi mesh network to reduce power consumption Improved casing for robustness and protection Deploying the service nodes: Work on partnerships for deploying service nodes in high-density areas Improve robustness of service nodes <div