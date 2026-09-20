---
slug: "get-well-holiday"
url: "https://devpost.com/software/get-well-holiday"
title: "Hospital Adventure"
hackathon: "Junction 2016"
winner: true
words: 434
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
---

# Hospital Adventure

> Reinvent a child's and parents' hospital experience by making the whole process transparent and fun!

[Devpost](https://devpost.com/software/get-well-holiday) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]]

**stack** ge, javascript, lots-of-love, python, react-native, redux, ruby-on-rails

## How they structured the write-up

- demo
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hospital adventure

## Body

Child View - Intro Child View - Stroyline Child View - Task Hospital Adventures Login Parent View - Dashboard Parent View - Live Surgery Updates Parent View - Packing List Demo Inspiration A child's hospital experience is often frightening, exhausting and overall unpleasant. We change that by creating a unique storyline for a child's hospital stay. Using the GE Adventure Series as inspiration, we wanted to imbed the awesome settings into a comprehensive use case. What it does Our application allows us to portray a child's hospital stay in a unique story, while simultaneously informing the parents about all necessities and the status of the treatment. Parents and children are able to login into different views, using the child's unique patient ID. Child's view : The child receives a virtual guide through his journey, mapping the upcoming treatment steps to a fun storyline. By integrating the hospital's environment and equipment, the child looses its fear of upcoming procedures. An avatar accompanies the child on his journey and explains every step in a simple and visual manner. Parents' view : By including the GE Opera API, parents receive live updates about the treatment progress and scheduled examinations. Furthermore, parents have a dashboard, allowing them to support the child during the whole affair, as well as being prepared for all eventualities. In stress situations, things tend to get overlooked. By providing extensive checklists, the parents are able to focus on more important aspects. How we built it Using react-native, we simultaneously built one app for IOS and Android devices. It connects to our simulated GE Opera API, allowing us to display realtime status updates. Challenges we ran into Having no example data or mocked API from GE Healthcare, we built an API simulation based on the data given. On a non-technical level, we were forced to translate medical terms to easy-to-understand descriptions. The mapping of different treatments to colourful storylines required a lot of imagination and creativity. Accomplishments that we're proud of We hope to make an impact in the lives of future patients and strengthening their trust in modern medicine. By digitizing a major part of a hospital's overhead, we take stress from the parents and allow for a smoother workflow. What we learned A hospital does not have to be an exhausting, frustrating or even frightening experience. Many people have put a lot of thought into creating a patient friendly experience, especially for young people. What's next for Hospital Adventure Sharpen our prototype and include more storylines for different treatment plans. Doing user studies in order to get feedback from our small patients. <div