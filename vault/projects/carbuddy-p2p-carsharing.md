---
slug: "carbuddy-p2p-carsharing"
url: "https://devpost.com/software/carbuddy-p2p-carsharing"
title: "CarBuddy: P2P Carsharing"
hackathon: "Junction 2016"
winner: true
words: 368
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/general_public"
---

# CarBuddy: P2P Carsharing

> A mobile app + hardware solution to let you share your car with other users and get paid instantly

[Devpost](https://devpost.com/software/carbuddy-p2p-carsharing) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[civic_government]] [[finance_payments]] [[housing_homeless]] [[labor_employment]] [[retail_commerce]] [[transportation]]
**user** [[general_public]]
  <sub>weak: geospatial</sub>

**stack** azure, embers, ios, remoto

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for carbuddy: p2p carsharing

## Body

Parking bays map Available cars list Chat Side menu Accept / Decline request My car profile Inspiration The evolution of transportation is running really rapidly nowadays. There appear new disruptive business models and governmental initiatives aiming to increase the efficiency of vehicle usage and provide new mobility options for citizens. And what about private cars ownership? They say that, in a few years, car ownership will be transformed into owning your time and mobility without the hassle of maintenance, repair, and insurance. Statistically, a private car is being used for less than 10% of its lifetime. So, we decided to re-think the traditional car ownership experience by combining existing offline car clubs mechanics link and the latest connected car and mobile technologies. What it does CarBuddy includes two main scenarios: Car owners can list their car for a short-term rent by other CarBuddy users. CarBuddy users can select / lock-unlock / drive and, finally, pay-as-you-drive using CarBuddy mobile app. Each rent starts and stops on dedicated municipal parking bays, equipped with parking sensors. Instant checkout is performed via P2P money transfer system upon the rent end. Communication between car owners and renters is performed using in-app messenger. Experts call CarBuddy "Airbnb for cars" :-) How we built it CarBuddy is a prototype of fully automated (keyless) P2P Сarsharing platform based on Remoto (smart car OBD-dongle and GPS-tracker), Embers (smart parking sensors) and TransferWise (money transfer between owners and renters). All powered by Microsoft Azure cloud backend. Challenges we ran into Enabling remote car access for multiple users for a limited time OBD dongle customization Designing and simplifying mobile user experience Accomplishments that we're proud of We've built a scalable product that fits multiple business models: from "friends and neighbors" car clubs to huge municipal initiatives involving corporate fleets We've found a viable combination of hardware and software solutions covering the whole customer lifecycle We've aligned our development process to fit the strict time limits of the hackathon What we learned Minimum viable product features prioritization Largest hackathon experience Finnish lifestyle ;-) What's next for CarBuddy: P2P Carsharing Code stabilization Hiring YOU Customer acquisition and business model validation Pilot projects Product improvements and growth Additional business requirements implementation <div