---
slug: "futurebusstation"
url: "https://devpost.com/software/futurebusstation"
title: "FutureBusStation"
hackathon: "Junction 2016"
winner: true
words: 336
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/sensor_fusion"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
---

# FutureBusStation

> Microsoft Face recognition API for target advertising & cool features such as bus and traffic info.

[Devpost](https://devpost.com/software/futurebusstation) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[cross_origin_web]] [[sensor_fusion]]
**domain** [[housing_homeless]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]]

**stack** css3, html5, javascript, microsoft-face-api, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for "your project"

## Body

Interactive menu Showing incoming busses with interaction Showing targeted advertisement Inspiration Ads in bus shelters are mostly static and the same for everyone. By being able to detect the characteristics of the person viewing the ad we are able to show them something more relevant and also have more effective campaigns. What it does Our smart billboard offers a right mix of advertisement with information. It detects the age, gender and facial expression of the person or people looking at the bus shelter billboard, and shows the most relevant ad for them. We also detect when someone is looking at the ad. It also has a menu which can be easily expanded and shows information about the bus timetable, live map, weather, and news. We've included a button that allows the passenger waiting at the station to request the bus to stop. In this way, they no longer need to flash their card at the driver. How I built it We built an HTML5 app that gets the webcam stream of the bus stop and sends it to Microsoft Face API. With it we are able to detect the gender, age, facial expression of the viewer, as well as if they are looking at the screen. We have set different ad campaigns for each target group, depending on gender and age. We get the bus timetable information using the HSL API. We interact with both APIs by means of our own Node.js server running on Heroku. Challenges I ran into Cross-origin request problems when accessing APIs from a local HTML5 app. Accomplishments that I'm proud of Being able to design a user experience that combines ads and information in a non-obtrusive manner. What I learned A lot of front-end development, APIs and bus shelters. What's next for "YOUR PROJECT" Improve webcam resolution and include other type of sensors to detect more accurately who is at the shelter. Then store all this information to be able to offer analytics for the advertisers about their campaign reach <div