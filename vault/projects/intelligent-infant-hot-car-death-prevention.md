---
slug: "intelligent-infant-hot-car-death-prevention"
url: "https://devpost.com/software/intelligent-infant-hot-car-death-prevention"
title: "AI Powered Hot Car Death Prevention"
hackathon: "Microsoft Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 431
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/video_visual"
---

# AI Powered Hot Car Death Prevention

> This setup includes an AI based IOT edge device that can detect and notify people when an infant is left in a hot car.

[Devpost](https://devpost.com/software/intelligent-infant-hot-car-death-prevention) · hackathon [[Microsoft Azure AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[transportation]]
**substrate** [[video_visual]]

**stack** azure, azure-iot-suite, c#, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for intelligent infant hot car death prevention

## Body

Architecture Diagram Inspiration Every year on average 38 infants die from being left in the car. I can’t even imagine what goes through the family after an incident like this happens. In an age of AI and smart connected devices these type of deaths need to be prevented. Having an edge device run the CV modules is cost effective because device is not sending images for processing to the cloud and also addresses any privacy concerns. As a parent of a 2 year old I feel devastated when I see news like this and I wanted to propose a solution that prevents this. What it does Solution used Azure Custom Vision model that has been trained to run on Azure IOT Edge runtime. This device predicts the presence of a child in a car and continuously monitors the temperature to provide Realtime alerts and phone calls to designated numbers. Also provides exact street address and vehicle details. How I built it I used the following components to build this solution. Configured Raspberry Pi to run Debian Buster and installed Azure IOT edge Runtime on it. Using the custom vision demo model for running AI module on edge devices as reference I created a new custom model by tagging child in a car seat for prediction. Configured the temperature simulator module and deployed it to Azure IOT hub. Azure IOT hub as a response to the IOT device messages is setup to trigger a function to call the Twilio API for making emergency calls and send messages with Car Details and location. Challenges I ran into I ran into lot of issues with GPRS / GPS raspberry had to get internet capability to the raspberry PI. I had issue with debugging the custom vision module deployed on edge device using IOT edge run time in visual studio. Accomplishments that I'm proud of I came to know about this Hackathon 3 weeks before the deadline, inspite of my schedule I still managed to build a working solution. I am proud of the idea itself. What I learned Things I learned are, Azure IOT Hub service Docker Containers Azure Custom Vision module creation and debugging the exported files. Creating and debugging Azure Functions from Visual Studio Code. Tillio API. What's next for Intelligent Infant Hot Car Death Prevention Using streaming hub to consolidate the logs received from CV module and Temperature module. Build custom hardware that is packaged into a small form factor with built in LTE capability. Create a mobile app so that users can update emergency information and other configuration details. <div