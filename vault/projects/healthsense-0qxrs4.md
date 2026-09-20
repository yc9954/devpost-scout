---
slug: "healthsense-0qxrs4"
url: "https://devpost.com/software/healthsense-0qxrs4"
title: "HealthSense"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 453
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# HealthSense

> In a stressful, hot, overwhelming datacenter, you need reminders of when to relax. HealthSense tracks vitals and helps you understand when you might be in trouble or need to take a break.

[Devpost](https://devpost.com/software/healthsense-0qxrs4) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[developer_tools]] [[labor_employment]]
**substrate** [[structured_db]] [[web_dom]]
  <sub>weak: sensor_telemetry</sub>

**stack** arduino, c++, javascript, json, nemotron, python, raspberry-pi, sensors, vultr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

This is the front end displaying updated feedback on workers. This is sensor data for a singular worker. Picture of majority of the hardware and sensors used Inspiration We wanted to build a project using hardware and agentic AI to filter though data. We figured it would be a creative way to gather and make decisions based on data. Seeing the results in person, on an Arduino, puts into perspective what is possible with hardware and agentic AI. What it does HealthSense has 3 sensors: an accelerometer, a heart rate monitor, and a temperature sensor. The Arduino constantly checks the three sensors and sends the data to the Raspberry Pi 5. The Pi 5 then sends the data to Redis. Vultr is used to hold the Redis database and runs the Nemotron Agentic AI. The AI is used to make decisions based on the previous data and most recent data. If the most recent data is concerning, the AI sends an alert to the person wearing the sensors by vibrating a sensor. The person can say they are perfectly fine by clicking a button to turn off the vibrating sensor. How we built it The technologies we used for this were an Arduino UNO, Raspberry Pi 5, accelerometer, heart rate monitor, temperature sensor, button, and on the hardware side. On the software side, we used the languages C++, Python, HTML, CSS, JavaScript, Redis, Vultr, and NVIDIA Nemotron. Challenges we ran into The main challenge was getting the agentic AI to work. The other key issues were getting the board to board connections and software to software connections. The heart rate sensor was consistently inconsistent when debugging. The front end was also a struggle when we got to the point of trying to fetch data from the Vultr server. Accomplishments that we're proud of The amount we got done in this time frame is pretty insane. The amount of inter board connections and softwares we used is more than any of us have implemented on previous projects. For totals we used 5 sensors, 2 boards, 1 cloud service, 1 database, and 1 agentic AI. What we learned Dellie, who worked on the agentic AI, learned a significant amount about RAG while developing the model. Thomas, who worked on board to board communication and Redis, learned a lot about Redis streams and how to write to databases effectively. Molly, who worked on frontend, learned how to connect a frontend to a database and how to work with JSON. Nathan, who worked on the sensor connections and board to board connections, learned more about PlatformIO and a significant amount about git (branches specifically). We all learned about anomaly detection models using and encoder and decoder. <div