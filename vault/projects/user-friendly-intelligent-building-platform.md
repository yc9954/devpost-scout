---
slug: "user-friendly-intelligent-building-platform"
url: "https://devpost.com/software/user-friendly-intelligent-building-platform"
title: "Smart Receptionist"
hackathon: "Junction 2016"
winner: true
words: 393
team_size: 5
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "substrate/geospatial"
---

# Smart Receptionist

> Intelligent receptionist for all buildings (office, school, bank, hospital even veihcles)

[Devpost](https://devpost.com/software/user-friendly-intelligent-building-platform) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]] [[finance_payments]] [[health_clinical]] [[retail_commerce]]
**substrate** [[geospatial]]
  <sub>weak: sensor_telemetry</sub>

**stack** chatbot, d3.js, ionic, java, java-nodejs, mongodb, node.js, spring

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for user friendly intelligent building platform

## Body

logo Smart receptionist assists a visitor who has an appintment with one of the employees Smart receptionist contacts the employee Building information from sensor data including temperature and air quality Personal reminder Inspiration We not only want buildings to be intelligent. We want the reception process to be automatic and intelligent. Imagine a new visitor to Tieto building who has an appointment with one of the employees. Our smart receptionist will arrange the appointment. The idea of smart reception also applies to other buildings such as shopping mall, hospital and bank. What it does In our demo, smart receptionist is a chat bot . It does, for example: queries the current status of the employee with appointment and notify the result ("I will be right there" or "five minutes late") to the visitor. check room status if requested if visitor needs to wait, it guides him to the nearest coffee machine through indoor map. when the appointment is ready, visitor will be shown to the meeting room as well. The idea can be easily extended to other scenarios such as: Taking electronic queues in banks/post offices. Waiting time estimation can be dynamically adjusted when people leave Register automatically during visit (without scanning ID barcode) to hospitals and other systems Detecting new passengers in busses and charging them based on their route How I built it Here is our architecture: The mobile app (in the center) is smart receptionist. It is driven by Java data rovider , Nodejs Slack Bot as well as the APIs provided by tieto Java data provider pulls from intelligent building sensors (720 api, etc) Nodejs Slack Bot communicates between the visitors (who use the mobile app) and employees (who use Slack) Challenges I ran into We want to make it available to all areas, including development countries. We made it so, that it could work without internet completely (using QR code on wall to initialize connection). But even bigger challenge was to find place for our team. We have moved like 5 times during event! Participated in hunt for table, chairs, and extension cords. Accomplishments that I'm proud of Worked out a cool demo Slept enough. What I learned From Hackathon perspective, it's better to start with some thing simple What's next for User Friendly Intelligent Building Platform Build a concrete product Involve more partners and go global <div