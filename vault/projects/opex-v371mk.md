---
slug: "opex-v371mk"
url: "https://devpost.com/software/opex-v371mk"
title: "Opex"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 1037
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Opex

> OPEX is a startup focusing on providing solutions for contact tracing. Our long term vision is to provide asset tracking solutions.

[Devpost](https://devpost.com/software/opex-v371mk) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: realtime_stream</sub>
**domain** [[education]] [[finance_payments]] [[health_clinical]] [[labor_employment]] [[supply_logistics]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** azure, c#, css, javascript, python, react

## How they structured the write-up

- health check
- contact tracing
- occupancy detection
- for institutions
- for employees

## Body

Context With institutions open across the country during this pandemic, we are increasing the risk of outbreaks. On-location activity is particularly important for traders who need robust, real-time communication and sales teams that are subject to specific compliance monitoring. In the event of an outbreak, a financial institution may not be able to accurately identify every employee at risk and in turn, can be forced to shut down completely. There is a huge opportunity cost due to a loss of revenue from shutdowns. The ability to control an outbreak and immediately trace down which employees should quarantine is crucial. Recent studies have shown that 80% of transmissions can be prevented through immediate contact tracing. Manual contact tracing can take days, reducing the efficiency all the way to 5%. New innovations by Apple & Google to help with contact tracing aren’t working either, because only 3 in 5 Americans report a willingness to use the software. These applications have ranges of hundreds of feet and in a closed setting would not efficiently track user interactions. Our technology can be used to help institutions as well as schools and other workplaces make data-driven decisions such as what areas to monitor, which employees to send home, and how to predict when an outbreak will happen. What is OPEX? OPEX is a startup focusing on providing solutions for contact tracing. Our long term vision is to provide asset tracking solutions. Health Check Through Health Check, employees answer questions about symptoms they may be experiencing to indicate their risk of having COVID-19. Our survey is logged daily and is formatted based on CDC guidelines. Contact Tracing Our contact tracing feature reports an office's overall safety, contact risk, COVID risk, & the risks for each employee. This information enables banks to control an outbreak by notifying them which employees may have COVID & where to schedule deep cleanings. Occupancy Detection Analyzing Bluetooth signals received from personal devices such as wearables and phones enables Opex to report the occupancy of a room. If a room occupancy exceeds limits set based on size, staff are notified Azure ML Applications Our solution was built and deployed using Azure Machine Learning Designer. Over the past few months, we have collected our own dataset from which we trained the model to estimate the distance of a user from any given receiver. Azure AI made the training and creation of our model straightforward. Unlike other platforms, the software assists you in creating the right model and its easy to use interface allowed us to quickly set up and train our models. With the accessibility of API's and their simple production deployment, we developed the model's API with ease. Furthermore, Azure AI increased estimated accuracy far above any other platform we have used. State of Advancement After over 6 months in development, the Occupancy Detection solution is fully functional, and Contact Tracing is 1 month away from 100% accuracy within a 6 ft range over a period of 10-15 minutes (CDC definition for “contact”). The solutions are currently being modeled at our houses, with the ability to deploy immediately. Opex has been given permission to conduct beta tests of our technology at Interlake High School, accompanying the school’s reopening in April. Furthermore, the project has generated interest from Washington State University, The University of Washington, Mazik Global, North Idaho College, and Bellevue School District. Key Benefits For Institutions Disruptively Cost-Effective Solution for Contact Tracing. Fast & Easy Deployment: Deploy this solution within days. Safe: All hardware meets US standards & certification requirements. Endless Possibilities: Our platform is "expandable" so you can leverage your infrastructure investment for twin solutions in inventory management, asset tracking, and more. For Employees Peace of mind for employees. Captures location & interaction events helping employees avoid routes through highly congested office spaces. The system maintains user privacy by randomizing data ID's. Solution Summary in Technical Terms Bluetooth signals are sent as electromagnetic waves from beacons to receivers. Beacons come in many shapes and forms, including wearables, phones, watches, and more. Using Received Signal Strength Indicator (RSSI), a relative measurement indicator of the strength of a signal we have developed an advanced Neural Network that can predict a user’s location. OPEX’s contact tracing software operates in four steps. First, our beacons advertise Bluetooth signals. Second, these signals are detected by wave scanners. Third, these readings are sent to the cloud and inserted into our SQL database. Finally, OPEX’s proprietary deep learning model is used to evaluate distance values based on these readings. Using a sophisticated filtering algorithm, we can accurately determine occupancy and communicate this on OPEX’s Connected Platform. Our occupancy detection software incorporates the same Neural Network, determining if a user exists in a room based on the movement of a signal. Methodology We took over 1 million data points from 24 different distances staggered between 0-6m to train the Neural Network. The Neural Network applies a parametric nonlinear regression model. We collected the average of each 10 data points per distance. After collecting the average for each 10 data points, we collected the average of all data points per distance. From the Weighted Average, we were able to derive 26 different factors all incorporated into the Neural Network-based. The program scans for readings every tenth of a second. Once it finds readings, (2 readings per scan) it stores the device on memory. Every 30 seconds the software calls an API that sends data to the Azure Cloud (About 600 readings). The data is then inserted into a Sequel table. Then, an Azure Worker (Function App) converts Raw Data into Weighted Averages in the Cloud. At the same time, the Second Azure Worker is predicting the estimated distance for each data point. This is added to the final data table. Finally, a Third Azure Function App goes through all the different services and traces users in services by triangulating user distance between receivers. These distances will be compiled to determine employee proximity. If interactions are recorded, they will be sent to the OPEX database. These interactions will be deleted from our platform after 14 days. Behind Our Build React/Java Script/CSS (UI) SQL (Database Queries) C# (Data Processing & API) Python (Machine Learning & Data Collection) <div