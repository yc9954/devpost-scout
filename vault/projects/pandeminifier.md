---
slug: "pandeminifier"
url: "https://devpost.com/software/pandeminifier"
title: "Pandeminifier"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 840
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Pandeminifier

> Messenger bot that collects data of users health, uses those to create real-time symptoms map, which will help users and government to minimize the risk of pandemic in a country or community.

[Devpost](https://devpost.com/software/pandeminifier) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** facebook-messenger, html, javascript, jquery, leaflet.js, mysql, php

## How they structured the write-up

- inspiration
- what it does
- how it can help with contact tracing
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for pandeminifier

## Body

Answering Health Questions Daily notification of people having symptoms in the area Map of population having symptoms Map of population having symptoms Map of population having symptoms Area that seems to be most likely infected Area that seems to be most likely infected View personal health or symptoms records Inspiration The name Pandeminifier simply means Pandemic + Minifier. Because Coronavirus is spreading exponentially, we, as a team from Cambodia, came up with an idea on how to minimize the risks by providing users a real-time map that shows where the population is having a cough, high temperature, difficult breathing, etc. As an example, we might want to go to some area, but we don't know if we will be exposed to the risks or not. That's why we came up with a real-time map from the data that is collected from every user of the Pandeminifier. This application works best as long as everybody in a community provide their health data daily. In this proof-of-concept application, we will only focus on the map of Phnom Penh City, Cambodia. What it does Pademinifier is an application based on Facebook Messenger. We decided to use Messenger because it can reach more people easily and people don't need to download or install (people like that because it takes less time so they are most likely to use and participate). It daily sends a form to users that ask them if they are coughing, having a high temperature, difficulty in breathing, having headache, has been in close contact with the patient, or went to the infected area. Then, it collects those user heath data along with the latitude and longitude of the location to generate a real-time map that shows to users. With this real-time map of COVID-19 symptoms, other users can easily look at the map and have an idea of how large the population is having symptoms in the area around them (or specific area they want to look at). Moreover, related authorities such as government or ministry of health can look at the map of the symptoms and see which area might be potentially infected , so that they can take actions accordingly. What is more, this application will also send alerts daily to users about how many people are coughing, having a high temperature, having a headache, difficult to breathe, etc, within the range of 1 kilometer square around them. Last but not least, with the health information provided by each user, they can also look up their records(coughing, high temperature, headache, etc) within the past 14 days. They can use that to follow up their health, or show them to the doctor in case they are going to the hospital. How it can help with Contact Tracing The next function we would like to integrate is how related authorities can use it to do Contact Tracing. The way it will work is that the latitude and longitude location of the tested-positive patient is put in the system and the application will send alerts to those other users that live within 1 kilometer square from the patient and ask them if they have previously had close contact with the patient in the past 14 days. If so, further actions are needed. How we built it We built Pandeminifier using PHP, JavaScript, CSS, Jquery, leaftlet.js API, phpMyAdmin, and Facebook Messenger API. Two of us worked for the frontend UX and UI, and one of us worked with backend, algorithms, map data plotting and databasing. Challenges we ran into Time is the biggest challenge for us. We have only 3 days to do this, so it is not nicely polished. Moreover, we have never worked with the map. Thus, we did not have enough time to work on algorithms of plotting data with the map. Accomplishments that we are proud of We are really proud that we finally made this. We are hoping that if this application goes in the real-run, it will drive big impacts to users and the world to fight this pandemic. What we learned We have learned how to do teamwork and how to be responsible for the tasks we have. Moreover, we learned how to effectively use the 3 days time period to create this application. What's next for Pandeminifier We are a team that lacks of machine learning knowledge. If this goes in the real-run it is a good idea to implement machine learning and artificial intelligence. With that, the application can learn the user health data and predict if their symptoms are coronavirus-related, and send alert to them. We need to create a dashboard for related authorities such as government to view specific data and details(such as age and gender) in our database. This project needs very massive users to be effective. Thus, if it is funded by organizations, it is effective to boost it inside Facebook. With that, people don't have to download or install anything, they just click on the advertisement and answer the questions which will take only approximately 30 seconds. <div