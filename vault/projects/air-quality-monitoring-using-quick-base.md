---
slug: "air-quality-monitoring-using-quick-base"
url: "https://devpost.com/software/air-quality-monitoring-using-quick-base"
title: "Indoor Air Quality Monitoring - The New Normal"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 654
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "substrate/structured_db"
---

# Indoor Air Quality Monitoring - The New Normal

> A Quick Base that helps to monitor indoor and outdoor Air Quality in real-time

[Devpost](https://devpost.com/software/air-quality-monitoring-using-quick-base) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]]
**substrate** [[structured_db]]

**stack** api, jinja, python, quickbase, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for air quality monitoring using quick base

## Body

Default Dashboard with Indoor and Outdoor AQI Reports AQI Category configured with Color codes that are with other tables to have the same color-coding based on AQI category My City view to show AQI data based on the configuration added for the current user Inspiration In these recent times when Remote working / Work from home is the new normal, ensuring that an employee is healthy and gets a productive environment is the highest focus for all organizations. One such parameter for high productivity is Air Quality. The measure of various factors such as CO2, O2, Humidity, PM2.5, PM10 etc. are all contributing factors for better work conditions. While working from home these factors require regular monitoring and control. Measuring AQI (Air Quality Index) needs sophisticated devices and visualization tools at real-time basis. We chose Quick Base to solve this problem and provide real-time monitoring and health advisory for better results. What it does The Indoor AQI monitor (Quick Base) integrates with multiple platforms/databases including Government of India Open Data API for real time city wise AQI levels, Raspberry PI and AQI sensors (SDS011 and DHT22) to track indoor AQI levels. The tool also uses data aggregation and visualization features readily available within Quick Base to generate useful and insightful reports which can be used by Organization/companies to help support their employees with equipments to improve their indoor air quality and thereby productivity. How we built it Raspberry-pi device is used along with the sensors SDS011 (measures PM2.5 and PM10 real-time) and DHT22 (measures real-time temperature and humidity). Python scripts were created to read the sensors' data and push them at fixed intervals to Quick Base when executed. The data aggregated in Quick Base are then used for creating reports related to indoor AQI. Along with it, the Govt of India Open Data API is queried using Pipelines to fetch the Outdoor AQI that is gathered periodically at multiple stations installed in different cities across the country. The pipeline is also configured to add stations and cities automatically if any new ones come up. There are 2 dashboards created to add the generic AQI and the city-specific AQI reports respectively. The city-specific view is configured to show the maximum PM2.5 clocked in the city configured for the current user, in the last 24 hours. The aligned city can be changed directly from the dashboard view. All the tables in the app are related to each other to create reports for indoor AQI and outdoor AQI at station, city, and state-levels. Challenges we ran into Finding the right sensors for measuring indoor AQI, configuring Raspberry Pi along with sensors, and to deploy the python scripts were the challenges faced in the initial stages. The availability of good sensors needed was also a big concern in India. Accomplishments that we're proud of Implementing the mini-IoT project with Quick Base by integrating it with Raspberry-PI real0-time gave a sense of fulfillment. Along with it, we created pipelines with only 3 steps to sync 1500+ records every day to Quick Base using Jinja expressions. This is also a first-of-kind implementation we tried and got hands-on with it. It opened up new opportunities to use Pipelines with the powerful Jinja expressions added. What we learned 1) Efficient ways of creating a pipeline with minimal steps 2) Using new JSON-based QB RESTful APIs, upsert data in QB using python script What's next for Air Quality Monitoring using Quick Base 1) To control the IoT devices like humidifier/AC directly from Quick Base based on the temperature/humidity readings 2) To sync the CO2 levels using the sensors to QB that helps to find and alert if the room is suffocating. 3) To link AQI data from other countries around the world and convert this solution into a global offering. 4) Integrate the QB tool with MS Teams to provide health advisory to employees at real time basis over their daily communicator. <div