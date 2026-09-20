---
slug: "smart-well-monitoring-system-for-villages"
url: "https://devpost.com/software/smart-well-monitoring-system-for-villages"
title: "SMART WELL MONITORING SYSTEM for Villages"
hackathon: "Intel Hacks 2017"
organization: "Intel"
winner: true
words: 951
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/education"
  - "user/educator_student"
  - "user/frontline_worker"
---

# SMART WELL MONITORING SYSTEM for Villages

> let wells be smart now

[Devpost](https://devpost.com/software/smart-well-monitoring-system-for-villages) · hackathon [[Intel Hacks 2017]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[civic_government]] [[climate_energy]] [[education]]
**user** [[educator_student]] [[frontline_worker]]

**stack** arduino, bluemix, dissolved-oxygen-sensor, gprs-module, nodered, ph-sensor, temperature-sensor, turbidity-sensor, ultrasonic-sensor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- lets see how people can access this data..
- challenges we ran into
- accomplishments that we're proud of
- testing at different lakes of udaipur
- testing at goverdhan sagar
- testing at doddh talai lake udaipur
- testing at pichola lake
- testing setup
- what we learned
- what's next for smart well monitoring system for villages
- outcomes of the project
- acknowledgement (very important)

## Body

Prototype Setup Prototype Sensor Box Final Product Setup Bluemix Dashboard The Team Testing at Goverdhan Sagar: A beautiful and peaceful lake of Udaipur System rippling with waves at Pichola Lake Testing at Fatah Sagar Testing @ Pichola Lake Testing at Doodh Talai Lake Inspiration India is the country of villages. As India consumes largest amount of ground water in the world (230 cubic kilometres of groundwater per year), and main source of ground water in villages are 'wells'. 95% of these wells are in very bad condition and contains bad quality water. Villagers and farmers with lack of knowledge use this water in their daily life for general use like bathing, washing and also plantation which affects the health of people and also quality and quantity of the field production. It is very difficult to monitor the quality of each well on daily basis and hence IoT based systems can be very helpful for authorities to monitor the condition of water and take remedial measures for betterment of water quality. What it does We have built an IoT based SMART Well Monitoring System with various sensors and analytics to make the villagers and authorities aware of the quality of water before use. The Well monitoring system will be sensing Turbidity, water level, dissolve oxygen, temperature of water and possibly pH value. The values are displayed over a dashboard on IBM Bluemix cloud and a mobile app is built for villagers/authorities. The system is ready to implement on well and the final aim is to build many system which will collect data from multiple wells and perform multiple analytics using bluemix APIs which will be predictive in nature. The system is powered by Solar panels to make it independent of any power needs from electricity supply. The system is communicating using GSM/GPRS packet and the reason for choosing this communication protocol is it is the only way to access network in villages (at least in India ). In case of water being not usable a visual alarm will warn the villagers. How we built it We built this Internet of Things application by integrating various hardware and software. We chose Arduino as our micro controller (µC) (Thanks to Intel Corporation for providing the same) and GSM module as gateway device. By interfacing different sensor to µC mentioned below we constructed a complete data collector unit. -> HC-SR04 Ultrasonic Sensor to measure level of water -> DS18B20 Temperature Probe -> Generic pH Probe -> SEN0189 Turbidity Sensor -> ENV-40-DO Atlas Scientific Dissolve Oxygen Probe Lets see how people can access this data.. In order to store this data and perform various analytics on it we interfaced this system with cloud using GPRS packet. We choose IBM Bluemix cloud to store and analyse data because Bluemix enables web and mobile applications to be rapidly and incrementally composed from services. An application to collect received data was created using Node-RED which is supported by many services on bluemix along with a beautiful dashboard link . This application performs various analytics like where is the system located?, What is the average temperature in a day, week and year?, Is the water pH and DO2 are under the range recommended by WHO or not? , Is the Water Drinkable? Challenges we ran into Well, I can write a book regarding the challenges :D , As challenges are certain while chasing a big target but they teaches us a lot. When we were in prototyping phase, circuits built over breadboard used to cheat us everyday. We lost 2 turbidity sensor who falls into water bucket and died. f We also faced problems in using some of the AT commands to communicate with GSM but this problem was resolved later. Fund could be a big problem but we are in such a campus where prioritiy is learning. Accomplishments that we're proud of The same project can be implemented for water monitoring of lakes. As we live in city of lakes-Udaipur (The Venice of the east) which is listed in worlds top 15 tourist destination. Soon we are going to demonstrate this system to Municipality of the city for its approval. Testing at Different Lakes of Udaipur Testing at Goverdhan Sagar Testing at Doddh Talai Lake Udaipur Testing at Pichola Lake Testing Setup Testing Setup What we learned We learned various aspect of Internet of Things. Initially we have planned to make only a prototype of the system for presentation in Intel hacks 2017 but because of stubborn behaviour of our director and head of department, they bring out an industrial product out of it. It was their determination which forced us to learn more and explore new things (Thanks to them). What's next for SMART WELL MONITORING SYSTEM for Villages Implementation on large scale. Making it affordable for the village. More Data! --------> More Analytics! ----------> Better Decisions Outcomes of the Project Villagers with awareness of water quality (Reduced cases of Disease) Better farming Effective Real Time monitoring of wells from multiple and remote villages. Acknowledgement (very important) Firstly we would like to thank Intel Corporation for providing hardware. Thanks to Mr. RS Vyas, Director , Techno India NJR Institute of Technology for making available labs 24*7. Special Thanks to our mentors and teachers who contributed to our project: :):):):):):):):):):):):):):):):):):):):):):):):):):):):):) Prof. Pradeep Chhawchharia, Prof. Vivek Jain, Prof. Yogendra Singh Solanki, Mr. Chandra Shekhar Sharma, Mr. Rajendra Singh Chouhan, Mr. Sorabh Chaturwedi & whole ECE Department of Techno NJR :):):):):):):):):):):):):):):):):):):):):):):):):):):):):) We also thank our crazy:) friends who were always there in IoT Lab to help us _ Prateek, Pankaj, Harshita, Tanvi, Kritika, Devashish, Akash _ All our dedicated Teachers and passionate friends. Thank You Once Again :) :) :) <div