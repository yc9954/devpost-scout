---
slug: "sinkmate"
url: "https://devpost.com/software/sinkmate"
title: "Sinkmate"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 518
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "substrate/structured_db"
---

# Sinkmate

> Protect you and others without even thinking about it.

[Devpost](https://devpost.com/software/sinkmate) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**substrate** [[structured_db]]

**stack** adafruit-feather, c, esp8266, firebase, ios, realtime-database, swift, vibration-sensor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sinkmate

## Body

Sinkmate Homepage. iOS application Data and Analytics. iOS application logo Inspiration The increasing threat that COVID-19 poses to everyone around the world inspired my partner and I to come up with a solution to mitigate the spread of the deadly virus. Research has shown that upwards of 95% of people wash their hands improperly. This simple yet powerful device can be easily implemented to assist people's remembrance to wash their hands for a full 20 seconds. These vital seconds serve as the difference between having the virus stay on your hands or not. What it does The microcontroller and vibration sensor are attached to the sink faucet. Whenever someone begins to wash their hands a counter begins. The attached speaker will then give a brief chime to remind the user if they washed their hands for the proper amount of time. The then on-board ESP8266 wifi chip will then log the length of washing data to a backend server. This server then can be accessed through our front-end iOS application which shows real-time hand-washing stats. How we built it The Adafruit feather microcontroller with the ESP8266 is housed on a breadboard accompanied by an external LED, speaker, and vibration sensor. The C code for the controller was developed in the Arduino IDE. The backend was hosted on the cloud using Google's Realtime-Database. The front-end iOS application was built using XCode and Swift. Challenges we ran into Everything... But seriously working with a microcontroller that has an on-board Wifi chip was a first and a big challenge overall. Making sure every electrical component communicated correctly with the controller took a large amount of time. Integrating Google's database with the iOS application and the microcontroller proved to be difficult but an interesting challenge. Formatting and parsing through JSON was a difficult task to do in C. Accomplishments that we're proud of This was our very first hardware hack! It proved to be difficult yet very awarding since the solution we came up with has a tangible component to it. It was great to finally apply the knowledge we learned in our electrical engineering classes to a real-life solution. Most importantly, I feel like we made a realistic solution to a big problem the world is facing right now. What we learned On the microcontroller's software side, we learned how to use HTTP requests to get and post data onto a backend server through the ESP8266 wifi module. Hardware-wise, we learned how to use a serial port to transmit data from a vibration sensor to the controller. We also had to work with and format JSON for the first time in order to send data from the controller and receive data on the iOS application. What's next for Sinkmate We think it is very possible for every sink to have some sort of variation of Sinkmate in the future. This product is low-cost and if bought in a large quantity, has a cost-per-unit lower than $2. The affordability of this infection-reducing device could very likely show up in large, commercial areas (airports, stadiums, etc.) or countries with underdeveloped sanitation systems. <div