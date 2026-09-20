---
slug: "moodwatch-ipzxaj"
url: "https://devpost.com/software/moodwatch-ipzxaj"
title: "MoodWatch"
hackathon: "PennApps XII"
winner: true
words: 518
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "user/clinician"
  - "user/educator_student"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/structured_db"
---

# MoodWatch

> Quick hassle-free mood and social rhythm tracking for your smartwatch!

[Devpost](https://devpost.com/software/moodwatch-ipzxaj) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]] [[health_clinical]] [[legal_justice]] [[mental_health]]
**user** [[clinician]] [[educator_student]] [[legal_professional]] [[patient_family]]
**substrate** [[structured_db]]

**stack** android, apple-watch, azure, ios, linode, mongodb, node.js, pebble, pop.co

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what i learned
- what's next for moodwatch

## Body

Inspiration In order to track his routine from sun-up to sun-down, our friend fills out an excel spreadsheet every day. His doctor asked him to do this as part of Social Rhythm Therapy (SRT) and mood tracking for bipolar disorder. Each week, they compare his ability to follow a routine and how events during the day affect his mood. Social Rhythm Therapy can be used to spot bad habits (and make good ones), find influences on moods that otherwise go unnoticed, and help provide structure to those suffering from mood or attention disorders. Since beginning SRT, this friend has gone from a student that struggled to get up for class to a Dean's List student. His only complaint? Spreadsheets suck! What it does After installing the native iOS or Android application and configuring their desired routine such as: Wake up @ 8:00AM How are you feeling (-5 to 5)? Take meds & Eat breakfast @ 9:00AM Arrive at work and say Hello to someone (social interaction) by 11:00AM etc. In bed by 10:00PM How was your day (-5 to 5)? The user receives push notifications to their Apple Watch or Pebble or other compatible wearable asking if they've completed the task by the desired time - if not the app will remind them later to tell us when they did complete the task if at all. This data can be shared inside the app to a Medical Care Professional subscribing to our premium service. The doctor can monitor the inputs of up to twenty patients and also receive analysis of any potential correlation between actions and mood swings. How we built it Storage: All non-medical user profile data of the "patient" is stored in a SQL database on Linode. All medical profile data (but no personally identifying information) is stored separately on Microsoft Azure using MongoDB. This was done to provide extra security (though is still not quite HIPAA compliant - yet) in case one system is compromised. Backend: A node.js express app serves as a simple API to communicate between the two databases and the three applications (iOS, Android, and web professional). Challenges we ran into The project was extremely ambitious to complete in a weekend (in total there are 7 different applications or services to manage). Having never written for the Pebble or Apple Watch, we had to learn on the fly and use the help of sponsors many times over (lots of trekking up and down the escalator with laptops in tow!) Accomplishments that we're proud of When we first announced the project to our friend in desperate need of a digital solution, he broke down in tears. What I learned Using agile practices in a hackathon REALLY WORKS - we held standup every 2 hours and the code just flew by. What's next for MoodWatch We're going to expand to more patients under the same doctor, but won't go public until after we can hire lawyers to make sure we're HIPAA compliant. After that, we plan to expand beyond SRT and mood tracking in order to capture all habit-forming and exercise planning activities. <div