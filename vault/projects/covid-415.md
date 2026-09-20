---
slug: "covid-415"
url: "https://devpost.com/software/covid-415"
title: "COVID-415"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 412
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/geospatial"
---

# COVID-415

> A service to match individuals in SF under self-isolation (e.g., vulnerable seniors) with local volunteers to deliver essentials like food and medicine.

[Devpost](https://devpost.com/software/covid-415) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[elder_child_care]] [[finance_payments]] [[security_privacy]] [[transportation]]
**user** [[general_public]]
**substrate** [[geospatial]]

**stack** express.js, google-maps, javascript, mapbox, mongodb, node.js, react, redux, turf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for covid-415

## Body

COVID-415 is a service to help deliver essential items to those under self-isolation. An interactive map and task list lets you browse delivery requests which are sorted by proximity. Contact details of the individual (e.g., name, phone, address) are revealed after a delivery has been claimed by a volunteer. Self-isolating individuals can request a delivery. We've also made the site mobile friendly. We've also made the site mobile friendly. Inspiration After hearing stories on the news of fearful senior citizens flagging down strangers in grocery store parking lots to shop for them and seeing posts online of people who wanted to help but didn’t know how, we decided to build a service to match these two parties together. The goal is to allow vulnerable populations who don’t have strong support systems to stay at home and reduce their risk of infection while ensuring they can still get access to essentials like food and medicine. What it does COVID-415 lets those under self-isolation in San Francisco post requests for deliveries and allows local volunteers to sort through, claim, and complete those deliveries. How we built it Backend : MongoDB, Express, Node, Passport, Validator Frontend : React, Redux, Javascript APIs : Google Maps Geocoding, Turf, Mapbox Challenges we ran into Providing smooth interactivity between the task list and the map (e.g., ensuring clicks on map reveal more information in task list and vice-versa) Privacy considerations for those who may feel stigmatized for being infected (e.g., displaying neighborhood and distance away only until a delivery has been accepted by another party, at which time more specific contact information is displayed). Securely retrieving the current user's location using that to provide value such as distance from available requests, sorting requests by proximity to the user, and providing directions. Accomplishments that we’re proud of Interactive map and task list that makes it simple to discover neighbors nearby who you can help Intuitive design that motivates volunteers to stay involved and rewards them for their contributions by tracking and displaying a record of all deliveries completed by a volunteer. What we learned We are all relatively new to software engineering and this was our first time working with a few of these technologies - MongoDB, Express, Passport, Validator. What's next for COVID-415 SMS notifications and GPS tracking to allow delivery recipients to track delivery. Masked, temporary phone numbers to safe communication between volunteer and delivery recipient. Payments integration to facilitate contactless payments between parties. Vendor payment integration. <div