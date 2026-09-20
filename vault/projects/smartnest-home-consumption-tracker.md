---
slug: "smartnest-home-consumption-tracker"
url: "https://devpost.com/software/smartnest-home-consumption-tracker"
title: "Smartnest Plus - Water and Energy Consumption Tracker"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 1058
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
---

# Smartnest Plus - Water and Energy Consumption Tracker

> Smartnest Plus allows you to keep track of your water and energy consumption, avoid surprises, and detect leaks or high consuming devices fast, get your day, week, or month consumption reports.

[Devpost](https://devpost.com/software/smartnest-home-consumption-tracker) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[educator_student]]

**stack** javascript, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for smartnest plus - water and energy consumption tracker

## Body

UI medium size start Water report example UI medium size Electricity report example UI medium size Water report small size UI small size Ultrasonic smart watermeter bought from china for the tests Testing communication of water meter Electricity meter bought from Germany for the tests Bulk production of water meters for a block of apartments in the Czech Republic Block of new apartments to use smart metering devices that can be connected to the skill Inspiration I live in the Czech Republic, where the water and electricity are charged with a monthly fixed payment, and at the end of the year, people pay for the extra water and energy they used. One year the water bill was almost 6 times the normal value and it was because one of the water valves was broken and was supplying water to a water heater without stopping for almost a year. We realized that it would be really useful if Alexa could give short water and electricity reports to let us know that everything is normal or warn us about higher consumptions on time. What it does Smartnest Plus allows Smartnest users to keep track of their water and energy consumption. Users can ask Alexa to tell them Water or Electricity reports and these can be a day, week, or month report depending on the period the user is interested in. Alexa would start by telling them if the consumption for the selected period is normal or is higher or lower than the average. this would be an example of a basic report: USER: Tell me my weekly electricity consumption report. ALEXA: Your electricity consumption this week has been higher than your weekly average by 15% Users can also ask for a detailed report in which Alexa would tell them the exact consumption value for the selected period. for example: USER: Tell me a detailed electricity report. ALEXA: Your electricity consumption this week has been 123kWh, 15% higher than your weekly average. Users can use Alexa conversations to switch between report types, periods, average or detailed reports. How I built it Smartnest Plus was built using Nodejs and Amazon Lightsail for the back end. Smartnest provides an MQTT Broker that allows different types of devices for smart homes and IoT to connect and interact with other devices. Two new device types were added to the service, Water meter, and Electricity meter. After users create these virtual devices they have to connect them to real devices using any compatible board than can communicate using MQTT. Then the devices can send daily updates about water or electricity consumption, this data is stored and processed to generate the user reports. The skill was build using the new Alexa Conversations as the core component of the functionality, this made us save a lot of development time and let us focus on the experience we wanted to offer to the users. We also had time to build a User Interface using Alexa APL language. This UI was designed inspired on futuristic UIs like from Iron Man movies, it was necessary to build Vector graphics, add transparencies, and make the whole interface responsive to adapt to all screen sizes. We also added special animations to some components to create a better futuristic feeling. Challenges I ran into The first Challenge was to find a way to get the data from the metering devices, after doing big research we found that some water and electricity meters can be read using an external microcontroller, this allowed us to start sending data to Smartnest cloud. Another challenge was after receiving the data from the devices, it was necessary to store them in an optimized way and to calculate the right consumption in order to create reports in the future. Another challenge was to get used to the new feature Alexa Conversations but the Slack channel and the Alexa developer Console helped me through it. Another challenge was to make the user interface responsive to make sure it would work in all Alexa devices no matter their screen size, so I learned to resize and reorganize components depending on the screen size. A huge challenge was certification because I was not aware of some requirements mi skill had to fulfill but after some attempts, the certification team helped me to fix the issues and to have my skill ready for publishing. Accomplishments that I'm proud of After overcoming all the mentioned challenges we were really proud of the user interface and how it can show a lot of useful information about the consumption, the user is able to compare the current consumption with up to three previous periods, it is also possible to see the average consumption and if the consumption is higher than the average the bar would turn red. The communication with the real devices is something we are also proud of and the algorithm to receive and process consumption data. We are also proud to be able to offer this service free of charge for anyone interested in having control over their home resources. Smartnest Cloud service has more than 2000 users and more than 4000 connected devices, we expect that in the future many more devices will be added because of this new feature. What I learned I have learned many useful techniques to properly build Alexa skills and how to work with the new feature Alexa conversations. also to create User Interfaces using Alexa APL, and create consumption reports. What's next for Smartnest Plus - Water and Energy Consumption Tracker We will send an update to the web, Android, and iOS App to allow the users to input the consumption data manually. Ther is a project of 1000 apartments in the Czech Republic where they will install these smart meters, we will provide this skill so the users of these flats can have their consumption over control. We will improve the service for this project in the Czech Republic by adding the European units of water and electricity consumption. We will provide youtube tutorials to teach everyone how to keep track of their water and electricity consumption using this skill. We would like to start offering the service of installing these smart metering system in any house. And as a long term objective we would like to start selling smart meters all over the world. <div