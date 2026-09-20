---
slug: "diagnosx"
url: "https://devpost.com/software/diagnosx"
title: "."
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 532
team_size: 0
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# .

> .

[Devpost](https://devpost.com/software/diagnosx) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[graph_reasoning]] [[voice_speech]]
**domain** [[civic_government]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for diagnosx

## Body

DiagnosX Logo dx_schema Inspiration For 4.5 years, I worked in the Emergency Department of a Level II Trauma Center. I witnessed firsthand how medical conditions, such as High Blood Pressure, caused Heart Failure when exacerbated and left untreated. For a while, I believed this was secondary to the patients, not taking their health serious. Truthfully, they presented to the hospital because they wanted to live, our healthcare system simply failed to present critical information to them in a way they could understand. In the USA, 100% of physicians are highly educated. Only 36.5% of Americans have at least a bachelors degree according to a study by the census in 2019. I noticed that the information seemed to get through to the patients when doctors would draw out information on paper or dry erase boards. Although they have the best intentions, physicians are often not artists and only have a certain amount of time to spend with a patient. A solution was needed to combat this disparity along with the impending physician shortage. What it does DiagnosX uses Tigergraph graph database as well as 3D models to illustrate breadth and depth of a patient's diagnosis and medical history for thorough understanding. The interactive 3D models isolate the body system in question, for a full 365 degree view and marks critical regions pertinent to the medical condition. Patients can view the models of their diagnosis 24/7 and fully break down all aspects of their medical condition. How we built it DiagnosX was built using the Tigergraph Graph Database and Schema to store and show connections of over 15 different databases for full information coverage of all patient medical condition. The Three.js Javascript library was also leveraged for rendering of 3D models. GSAP library was also used for interactive and immersive animations of the body systems. Challenges we ran into This projects was a lot of firsts for me. In addition to using 3D models, I've never used a graph database before developing DiagnosX. I ran a litany of errors when setting up the database, running the queries and executing the REST APIs to connect the database. I am super thankful for the biweekly office hours and numerous Youtube videos. Accomplishments that we're proud of Having a functional prototype and getting an idea with the potential to impact millions via decreasing disparities in healthcare out there. What we learned Graph databases are not as intimidating as I thought going into this hackathon. I broke my graph a few times while developing it through GSQL Code, but found GraphStudio SUPER helpful in creating and visualizing schemas and connections. What's next for Diagnosx 1) Adding text to speech for a more connected experience. The application reading out information makes it feel slightly more like engaging with the doctor. 2) Getting models of every part of the human body. For the prototype, I just used a human model and the heart but I plan on having a detailed model for each organ of the body. 3) Add more animations to illustrate prognosis of medical condition as well as concerning symptoms. 4)Include 3D models of drugs to illustrate how they interact with the body. More information here: https://docs.google.com/document/d/1pVyHKQYpDJ3bLIF2hdZ97ZyHch90CmGprHHvusuqoGA/edit?usp=sharing <div