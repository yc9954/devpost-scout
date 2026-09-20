---
slug: "guardian-2n7q3s"
url: "https://devpost.com/software/guardian-2n7q3s"
title: "Guardian"
hackathon: "Hack the North 2019"
winner: true
words: 1075
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "user/frontline_worker"
  - "substrate/structured_db"
---

# Guardian

> The number of firefighter injuries has increased by over 28% in the past 30 years. Our team sought to tackle this issue by creating a novel helmet utilizing IOT to improve firefighter safety.

[Devpost](https://devpost.com/software/guardian-2n7q3s) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**user** [[frontline_worker]]
**substrate** [[structured_db]]

**stack** apex-charts, arduino, bootstrap, c, c++, css3, firebase, google-cloud, hardware, html5, i2c, iot, javascript, vue.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for guardian

## Body

Inspiration We believe that the impact of ideas is the foundation on which we should build our world on. Our team was inspired to take on a challenge that would improve the lives of those around us while remaining true to our roots. When the Fort McMurray fires of 2016 destroyed over 3244 homes and caused 9.9 billion USD in damages, the lives of our team members were transformed. Coming from Alberta, the effects of the fire left a lasting impression on our views of how technology can be used for good and helped us discover a newfound sense of purpose. We sought to use new and novel technologies to make this a reality. Guardian is a novel helmet designed to advance current firefighting methods. By attaching various crucial sensors on the helmet, we are able to gather important vitals about the environment such as temperature, CO2 levels, atmospheric pressure, volume of total organic compounds, and much more while simultaneously sending this data in real-time over the Internet of Things platform to a remote database. We then retrieved this information and created a unique web user interface that responded to the real-time changes in data to relay information across all individuals over watching the situation. What it does The Guardian firefighter helmet sends and retrieves information by using six sensors connected to a central microcontroller capable of connecting to nearby WiFi networks. When information from the environment is extracted, we are capable of sending this information using WiFi following the IOT protocol to a remote real-time database where it is stored and processed. When this information is retrieved, it is used to create a web user interface that displays the information in a real-time framework to show changes as they happen. This interface allows all subscribers to the web app to monitor the situation different firefighters are and providing assistance when needed. How I built it The microcontroller we used for this project is the NodeMCU board which is an Internet of Things enabled board built on top of the Arduino framework. We then attached several sensors to the board (DHT11 Temperature and Humidity Sensor, CCS811 Air Quality Sensor, BME280 Atmospheric and Pressure Sensor, and VEML6070 UV Index Sensor) following the I2C (Inter-Integrated Circuit) protocol where we used a multi-master/multi-slave architecture to allow sensors to publish and receive data to the bus system. When the data is received by the NodeMCU microcontroller, the data is sent over WiFi to a real-time Google Firebase database where it is categorized by sensor and type of data. This information is then retrieved and displayed on a web app user interface updated in real-time. The web app is built using the Vue.js framework to process the real-time data. Other areas of the web app such as the front-end design are built using the HTML5, CSS3, and Javascript. Additional features were implemented using Bootstrap, and ApexGraphs. Challenges I ran into Throughout the project, our team ran into several challenges regarding the hardware aspect of the implementation of the helmet. As this was our first time using the IOT framework, we found it difficult in the beginning to find a method of connecting to WiFi. When we initially tried to use an Arduino Uno board and connected an ESP8266 WiFi module to it, we found that the setup required to connect to Google Firebase required several external frameworks that we were unable to implement. As a result, we switched over to the NodeMCU board which had the ESP8266 WiFi chip already built into the board. However, since this is a much smaller microcontroller, the number of input and output data pins was half of that of the Arduino Uno. In order to counteract this, our team members learned to use the I2C protocol which allowed us to connect several sensors to only one bus and save the input and output pins. Accomplishments that I'm proud of As a team, we overcame multiple challenges in order to produce a fully functional product. We were able to integrate both hardware and software into this project. On the hardware side, we implemented a total of six sensors: temperature, carbon dioxide concentration, total volatile organic compounds. We are very proud of connecting most sensors through the I2C protocol, making the product lighter and more portable. On the software side, we implemented real-time database using Google's FIrebase. By uploading real-time data collected from the sensors to the database and retrieving them to the web application, operators behind the screens will have an accurate picture of the fire scene. They will be able to make appropriate decisions to better exterminate the fire and possibly safe the lives of the firefighters. What I learned This project taught us the importance of communication protocols. Since we had team members working on the software side as well as team members working on the hardware side. It was crucial for us to establish a communication protocol early on in the project as it is difficult for both teams to work on the project simultaneously if the software team was not retrieving data from the hardware team. In order to overcome this, we made sure to establish a solid form of communication of data so the software team knew exactly how to fetch the data and what format it would be in. By doing this, as the hardware team was integrating more sensors, the software team was able to generate their own faux data following the same communication protocol before real data was provided. This made integrating the two sides of the project at the end very easy and efficient. What's next for Guardian In the future, we plan on implementing a full master-slave protocol between the web app and the microcontroller. Currently, the microcontroller is capable of sending information to Google Firebase and the web app is capable or retrieving it, however, the opposite is not possible. Having the web app alert firefighters of unstable or dangerous conditions is crucial in the safety for all parties involved, as a result, in the future we will want to implement the ability for the web app to publish to Google Firebase as well and allow the microcontroller to retrieve this data and provide feedback to the user. For example, if one helmet detects a dramatic increase in CO2 gas, a notification will be able to the sent to all helmets after the data has been parsed and sent to the web app. <div