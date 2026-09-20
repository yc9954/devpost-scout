---
slug: "golfgreen"
url: "https://devpost.com/software/golfgreen"
title: "GolfGreen"
hackathon: "The HCL-Pega Pathbreaker Hackathon"
organization: "HCL"
winner: true
words: 347
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# GolfGreen

> Control Panel for Watering of Fairways , greens, tees and synchronize e-sustainable watering plan

[Devpost](https://devpost.com/software/golfgreen) · hackathon [[The HCL-Pega Pathbreaker Hackathon]]

## Facets

  <sub>weak: sensor_fusion</sub>
**substrate** [[structured_db]]

**stack** api, appstudio, pega, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for golfgreen

## Body

control by sensor generate Flexible water plan course organized by sprinkler days plan fairways Inspiration It was inspired by Pega Golf challenge on Sustainability . by the lack of data driven environment-process in Water sustainability and uses on Golf Courses and lack of water management. Its funny, that lot of waste of water in golf courses going on . With water sources such as deep well or reclaimed water how you get the water matters less than how much and when the course is watered process . Attached below shows the research of Usga. . Increase in Water usage will increase cost What it does Define Watering of Tees , Fairways , greens, roughs. Roughs are natural with irrigation. Set and sychronize a watering plan thru a Control Interface that open and closes valves by an electro charge. The hardware used is either A Raspberry Pi connected to Node-red app backend or Photon . That controls and activates a sprinkler is open or closed. The Vue fronted provides course staff the Data set to feed the Control interface the water schedule. How we built it Pega’s easy to use drag-and-drop development gives the ease to user to adapt to their club use. Used Vue to build the schedule frontend. and the web mashup water plan . the API for syncing course data. With App Studio used Case Type to design a Waterplan .It allows to choose a duration of 8 to 15 minutes per Area, for flexible watering plan. Features : Decision to disable Option to disable watering if it Will rain Water instructions sync to conditions Challenges we ran into One of the challenges is connecting Waterplan and Vue app . Accomplishments that we're proud of developed Case-Based water management.that improves and tweaks golfcourse watering.with Pega’s easy to use drag-and-drop development gives ease to user to adapt to their club. What we learned How to setup Case Type How to setup Raspberry Pi I learned you can water course area by switching on internet connected device . What's next for GolfGreen scale to more sprinklers. <div