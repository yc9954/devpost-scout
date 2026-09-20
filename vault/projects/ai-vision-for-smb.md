---
slug: "ai-vision-for-smb"
url: "https://devpost.com/software/ai-vision-for-smb"
title: "AI Vision for SMB"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 441
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/small_business"
  - "substrate/video_visual"
---

# AI Vision for SMB

> Using AI Computer Vision to give SMB more insights on their business

[Devpost](https://devpost.com/software/ai-vision-for-smb) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[immigration_refugee]] [[retail_commerce]] [[supply_logistics]]
**user** [[small_business]]
**substrate** [[video_visual]]

**stack** alexa, azure, helium, movidius, visa

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for ai vision for smb

## Body

Current setup AI Vision Platform AI Vision Dashboard Azure Functions Entire IoT Hardware Inspiration Deep learning has been a pretty big trend for machine learning lately, and the recent success has paved the way to build project like this. We are going to focus specifically on computer vision and Single Shot Detection (SSD) on in this sample. And we want to use AI to build a practical application that can help Small Business owners around the globe. What it does In this project we will be building an AI vision kit that can be used to count items, and use multiple cameras on a single unit to track multiple things, and use Azure IoT Hub as a data storage for Small Businesses. To provide a deeper analysis using the computer vision data that can help owners to make right decisions. We can provide insights on how busy the store is vs. the revenue that it's generating, along with the wait time of the competitors through Visa Queue Insights. And we can track inventory through the same computer vision. How I built it We've built this project using Up2 board, Intel Movidius Neural Computing Sticks and Helium Kit. The software goes through the AI Computer Vision information is being passed into Helium IoT Platform, the Helium IoT platform and Azure IoT Hub is connected seamlessly, Azure IoT Hub is then connected to Azure Functions then push into Azure SQL. We also use Azure Functions to retrieve, analyze, and display the data to the SMB owners on the dashboard. Additionally, we use Visa Queue Insights and Merchant Measurement to provide additional insights to competitor research, and Alexa to ease the UI. The project is documented step by step on https://www.hackster.io/Nyceane/ai-vision-for-smb-74bffb Challenges I ran into Connecting to Azure IoT Hub was a little difficult in the beginning, using Helium IoT platform it seamlessly integrated the IoT platform to Azure IoT Hub, which is then connected to Azure Functions to store the data into Azure SQL Accomplishments that I'm proud of We have shown our demo to several SMB owners are they are very impressed and wanting to integrate. What I learned Training AI is difficult, but there are a lot of readily available neuro-networks out there that can be implemented in everyday applications that can help to run a business. We've also learned how to use Azure IoT from end to end through sever-less structure. What's next for AI Vision for SMB We want to start showcasing to more small businesses and see if they want such feature in their store. The project is open sourced and documented step by step at https://www.hackster.io/Nyceane/ai-vision-for-smb-74bffb <div