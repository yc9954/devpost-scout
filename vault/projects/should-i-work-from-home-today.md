---
slug: "should-i-work-from-home-today"
url: "https://devpost.com/software/should-i-work-from-home-today"
title: "Should I work from home today?"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 246
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/transportation"
  - "substrate/geospatial"
---

# Should I work from home today?

> This collection helps you decide whether you should go to the office or work from home, based on environmental factors such as weather, air pollution, coronavirus cases, traffic and your ISP status.

[Devpost](https://devpost.com/software/should-i-work-from-home-today) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[transportation]]
**substrate** [[geospatial]]

**stack** api, google-maps, javascript, moment.js, postman

## How they structured the write-up

- inspiration
- what it does
- what's next for the project

## Body

Inspiration With the COVID-19 infection numbers fluctuating many employers have decided to move to a hybrid work arrangement, where you have the flexibility to choose whether you prefer to work from home or from the office on a given day. Both of these options has its advantages, but some days the environmental factors make the decision easier - is my service provider having some problems today? I probably don't want to risk teleworking today. Am I going to be stuck in traffic for hours going to the office? Better telework today. With this collection the process will be reduced to one simple recommendation - "stay home" or "all clear to go to the office"! What it does It collects data from various APIs and outputs the recommendation with some details to a Slack channel. The data is gathered from: Downdetector - to check your ISP status positionstack - to translate your home and work addresses into geographical coordinates openweather - to get the information about weather and pollution Google's distancematrix API - to calculate the traffic on the route to work COVID-19 API - to get information about COVID-19 cases in your country What's next for the project Many improvements can be made to the logic of the final recommendation - at the moment it a simple yes/no recommendation taking hardcoded thresholds and it won't provide custom results based on personal preferences (e.g. the weather is a more important factor if you cycle to work). <div