---
slug: "safetank"
url: "https://devpost.com/software/safetank"
title: "SafeTank"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 681
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "substrate/sensor_telemetry"
---

# SafeTank

> Real-time monitoring and AI-powered predictive maintenance for factory plants.

[Devpost](https://devpost.com/software/safetank) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]] [[disaster_emergency]] [[labor_employment]]
**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** c++, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safetank

## Body

Demo website Inspiration Chemical storage failures can have serious consequences for workers, facilities, and nearby communities. Recently, a chemical tank incident in Southern California led to large-scale evacuations and highlighted the risks associated with inadequate monitoring and delayed maintenance. We wanted to build a system that could continuously monitor hazardous chemical containers and identify warning signs before they become emergencies. Our goal was to move facilities from reactive inspections to proactive safety management. What it does SafeTank is an AI-powered chemical container monitoring and predictive maintenance platform. Using a network of sensors, SafeTank continuously tracks environmental and container health metrics such as gas concentration, temperature, humidity, and other indicators of abnormal behavior. The system visualizes real-time data on a dashboard and automatically alerts operators when dangerous conditions are detected. Beyond monitoring, SafeTank analyzes historical trends to estimate the likelihood of future failures and recommends maintenance actions before a leak, overheating event, or container failure occurs. How we built it We built SafeTank using a Raspberry Pi connected to an MQ-2 gas sensor, temperature and humidity sensors, and a vibration sensor. These sensors continuously collect data about the condition of chemical storage containers and their surrounding environment. A key part of our system is QNX RTOS, an industry-grade real-time operating system commonly used in safety-critical and industrial applications. QNX handles sensor data collection and processing, ensuring reliable and responsive monitoring of potentially hazardous conditions. We developed software to read sensor values, detect abnormal conditions based on safety thresholds, and send the data to a monitoring dashboard. The dashboard provides real-time visibility into gas levels, temperature, humidity, and vibration activity, allowing operators to quickly identify potential issues and respond before they escalate. In addition, we integrated AI-driven predictive maintenance capabilities to analyze sensor trends and identify early warning signs of potential equipment failures. By learning from historical and real-time sensor data, the system can help anticipate maintenance needs and reduce the risk of unexpected chemical storage incidents. By combining IoT sensors, QNX real-time processing, AI-powered predictive maintenance, and a user-friendly monitoring interface, SafeTank provides a reliable solution for improving chemical storage safety. Challenges we ran into We encountered difficulties with integrating the sensors together, as more sensors were added to the project there was a higher computational burden that affected the Raspberry Pi's processing power. This led to us pivoting away from a polling technique we used initially for the vibration sensor to event based instead. This makes for a much more responsive workflow and simplified the overall code architecture. Accomplishments that we're proud of Built a complete end-to-end chemical container monitoring prototype. Successfully integrated temperature, humidity, and vibration sensors into a working monitoring system. Used QNX Neutrino RTOS for reliable real-time sensor data processing. Connected sensor data processing with a dashboard for live monitoring and visualization. Integrated an AI predictive maintenance component with the model running on the Raspberry Pi to analyze sensor data and identify potential maintenance concerns. Combined hardware, real-time operating systems, AI, and software visualization into one unified safety platform. What we learned Through building SafeTank, we learned how challenging it is to develop reliable real-time systems that combine hardware, software, and AI. We gained experience with sensor integration, handling multiple real-time events, embedded processing, and building communication pipelines between devices and applications. We also learned how predictive maintenance can enhance traditional monitoring systems by using data patterns to identify potential issues earlier and support proactive decision-making. What's next for SafeTank Our next steps are to continue improving sensor reliability and expand the capabilities of the platform. We are currently testing and calibrating the MQ-2 gas sensor to integrate hazardous gas detection into the system alongside our existing temperature, humidity, and vibration monitoring. Future improvements include expanding the sensor suite with additional chemical-specific sensors, improving our AI predictive maintenance model with more real-world data, and enhancing the system's ability to identify early warning signs of equipment failures. Our long-term vision is to scale SafeTank into a complete industrial safety platform that combines real-time monitoring, edge AI, and predictive maintenance to help prevent chemical storage incidents before they occur. <div