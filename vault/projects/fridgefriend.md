---
slug: "fridgefriend"
url: "https://devpost.com/software/fridgefriend"
title: "FridgeFriend"
hackathon: "Hack the North 2019"
winner: true
words: 267
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/retail_commerce"
  - "substrate/video_visual"
---

# FridgeFriend

> An automated ingredient tracker and recipe curator.

[Devpost](https://devpost.com/software/fridgefriend) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[agriculture_food]] [[retail_commerce]]
**substrate** [[video_visual]]

**stack** arduino, firebase, react, vision, visionai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fridgefriend

## Body

The team! Inspiration We wanted to build an app that would suggest recipes based on ingredients the user had, and the original idea was to let the user manually input the contents of their fridge. This would obviously be inconvenient to the user, so we decided to make the fridge automatically keep track of its contents. What it does FridgeFriend keeps tracks of the ingredients and food items in a fridge and displays them on a web application. This web application also allows the user to search for recipes based on the ingredients they currently have and to generate shopping lists for the ingredients they're missing. How we built it We use a webcam at the back of the fridge (connected to a laptop) to take a snapshot of its contents whenever the fridge is closed after it is opened. To detect whether the fridge is open or closed, we use an ultrasonic sensor connected to an Arduino. We get the list of ingredients from the snapshot of the fridge's contents using Google's Vision API, then store this list in Firebase. Our web application was built using React and is hosted on Firebase. Challenges we ran into Numerous technical challenges. Accomplishments that we're proud of We managed to have the project functioning minimally. What we learned We learned a lot about Arduino and Firebase. What's next for FridgeFriend In the future, FridgeFriend can allow the user to filter recipes based on dietary restrictions. It can also give nutrition facts on ingredients/recipes. We can also use more cameras in case one food item is completely blocking another. <div