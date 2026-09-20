---
slug: "smart-plant-iot"
url: "https://devpost.com/software/smart-plant-iot"
title: "Smart Plant IoT"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 342
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
---

# Smart Plant IoT

> Auto watering the plant and tracking plant's health through Helium and Microsoft Azure IoT

[Devpost](https://devpost.com/software/smart-plant-iot) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[sensor_fusion]]

**stack** arduino, azure, azure-function, azure-iot-hub, helium

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for smart plant iot

## Body

GIF Smart Plant IoT GIF Smart Plant Android app Components Azure IoT Hub Azure SQL Azure Functions Inspiration I love plants, they make the air fresher in the house, they are pretty to look at. But I was never able to keep them alive, I believe that if the plants are more self maintainable, more people would have them around which would lead to healthier lifestyle for everyone. What it does Smart IoT Plant would auto water the plant when it needs, as well as track all the vital information (Temperature, Humidity, Moisture and UVLight) about the plant. So that users need little to no maintenance at all. How I built it I've built the project using Arduino, Seeed Shield, UV Sensor, temperature/humidity sensor and moisture sensor, along with Helium Atom and Helium Element. Helium platform is directly synced ups with Azure IoT hub and we upload information about once every minute. Once the data is being transferred to Azure IoT Hub, it passes through Azure Function to be stored inside Azure SQL. A separate Azure Function creates a RESTful API allows users to retrieve the SQL data. This way the information can be displayed over the OLED device attached to the device as well as Android can retrieve data via RESTful API A step by step guide on how to recreate the project is documented at https://www.hackster.io/Nyceane/smart-plant-iot-59cbc3 Challenges I ran into The pump requires 12V DC, it was a bit difficult as the Arduino device was only putting 5V, we've figured out how to Accomplishments that I'm proud of Our team was able to build out the entire project and have it documented in step by step, from IoT What I learned We are able to build out the entire project through severless infrastructure, Arduino connects directly to Helium platform which was able to connect to Azure IoT Hub. This allows What's next for Smart Plant IoT We will build out a better enclosure, possibly a pot so that users can easily just drop the plants into the smart pot. <div