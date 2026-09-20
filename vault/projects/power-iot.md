---
slug: "power-iot"
url: "https://devpost.com/software/power-iot"
title: "Power IoT"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 1117
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Power IoT

> Your IoT Platform on Quick Base

[Devpost](https://devpost.com/software/power-iot) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[simulation_digital_twin]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** .net, grafana, influxdb, powerbi, quickbase

## How they structured the write-up

- power iot
- what it does
- data flow
- how we built it
- key features of quick base used
- challenges we ran into
- what we learned

## Body

Features Quick Base Data Model Solution Architecture Quick Base Features Used Quick Base Base Components Used Home Page Management Summary Dashboard Area Summary Dashboard Site Summary Dashboard Equipments Summary Dashboard Work Orders Summary Dashboard Alarms Summary Dashboard ML Predictions Summary Dashboard Power BI Dashboard Grafana Dashboard - For Site and it's Equipments Grafana Dashboard - For Equipment Power IoT Power IoT is your IoT Platform on Quick Base , leveraging multiple features of Quick Base for an effective Business need. It connects your Sensor Data to Quick Base and provides a 360 degree view of your Plants - Be it low level time series data monitoring or Management level view of your entire company KPIs. It also acts as your Equipment Management System, as well as can be used by Field Users for Work Order Management System. Responsiveness - This app is meant for organizations to swiftly react to changes in their equipment and plants through intelligent monitoring via Alarms and automated Work Orders. Any issues detected are raised and notified to users who are assigned to the sites immediately and can take relevant actions to ensure seamless working of their plants. What it does The Quick Base Entry is created for the Power Industry, but is relevant for all such Industries, since it is all configuration driven. It serves as your: Site and Equipment Management System - You can create your Site hierarchy and add all the Equipment & Sensors on the Site – to enable capture of IoT Sensor Data onto your IoT platform on Quick Base Work Order Management System - You can generate Work Orders and assign them to individual and track it through its entire life-cycle, along with required analytics Monitor Key KPIs - You can monitor your Power Plant Performance with summarized KPIs available right within Quick Base – Power Generated, Equipment Up Time, Power Consumed, Cost, Equipment Efficiency, etc. More KPIs can be easily configured through the power of Formula Fields Alarm and Machine Learning Prediction Management - Monitor the Alarms generated and any Prediction raised by Machine Learning algorithms and track them to closure External Integrations - Robust .NET Microservice to connect Sensor Data to Quick Base using JSON APIs Integration with external dashboards like Grafana and Power BI for in-depth analytics Please Note: All data in entry is fictional and simulated, however inserted into Quick Base, as if actually coming in from Sensors. Predictions are also simulated and ML algorithms are out of scope of this hackathon entry. Also, data is entered for future dates, since data entry is to be avoided during judging period Data Flow Sensor Data from various Power Plants/Sites are transmitted either directly or via a Hub to an MQQT based Server . This is a queue mechanism to ensure no data is lost. We have built a .NET Core based micro-service which listens on this queue. Whenever a new sensor data packet is received, it will query Quick Base Tables using QB Restful JSON APIs to get relevant data for Site, Equipment, Equipment Type and Alarms. It then, stores the Sensor Data to a Time Series database - InfluxDB and then calculates a daily summarized value. This summarized value is stored back to Quick Base table for Reporting. Time Series data is used by Grafana dashboards to view granular Sensor Data on dashboards, for Site and it's equipment. There is direct linking to these dashboards from the Quick Base Lists using Formula Fields . Quick Base data in also imported to Power BI Desktop using QB connector to generate complex dashboards. These reports are published on to Power BI Cloud Service, which are then embedded back into Quick Base pages. How we built it The application is built using Key Quick Base Components as below: Quick Base Application The Quick Base Application maintains: Area & Site Hierarchy Equipment, Sensors & Alarms Master Summarized Sensor Data (KPIs) Work Orders Alarm Logs ML Predictions Quick Base Pipelines Advanced Pipelines are created to Assign Work Orders when ever an Alarm/ML Prediction is raised The Pipeline is intelligent enough to understand when to raise it and to whom to assign the Work Orders Restful JSON APIs Advanced use of Quick Base Restful JSON APIs to: Read Master Data from QB Tables Write back Data to Sensor Data Table Write back Alarms to Alarms Table Data The API framework is written with POCO classes for easy integration Add-on Code A .NET Core based Micro service is written to listen to MQQT Queue, which sends Sensor Data to Influx DB Summarizes Daily data and writes to Quick Base Checks the data against QB Alarm Master and raises Alarms Key features of Quick Base used Role Based – Personalized Dashboard Each User can see data relevant to them: Area Manager – Looks at his assigned Sites from Area perspective Site Manager – Gets relevant data for his Site Field User – Gets his TODO worklist Management User – Can see how his company is performing Customized UI, Forms & Formula Fields Customized color coded UI to understand the data instantly Customized Forms to enter data easily, with the required validations KPIs created using Formula Fields – More KPIs can be easily added Pipelines, Notifications & Subscriptions Use of Pipelines to automatically generate Work Orders whenever a new Alarm / ML Prediction is raised Intelligent assignment of WO to the right Field User using Pipelines Use of Automation to store Audit History of each WO Use of Notifications & Subscriptions to notify Field users, whenever a new WO is assigned to them External Integration .NET Core based Micro service connects Sensor Data to Quick Base using Restful JSON APIs Integrates with Time Series Dashboard on Grafana using Formula Fields. Each Equipment/Site can see its own data through a single click on the Formula Field Integrated with Microsoft Power BI and users can see the reports embedded in their Quick Base application Challenges we ran into There was not much information available on connecting MQQT Parcels to Quick Base. We went ahead with a Micro Service approach, which can be deployed on any cloud/on-premise. Because of large number of tables involved, coding was taking time and so we went ahead and created a generic module for .NET to connect to Quickbase - via configuration only, which is available on the Github link below. What we learned Being new to Quick Base, it was great to learn how easy it is to design and develop solutions. We were skeptical of how it will fit into IoT landscape, but at the end of the project, we found out that it's a perfect fit, thanks to ease of development and robust integrations and pipelines. <div