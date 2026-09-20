---
slug: "corona-bluetooth-beacon-tracking"
url: "https://devpost.com/software/corona-bluetooth-beacon-tracking"
title: "corona-bluetooth-beacon-tracking"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 515
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# corona-bluetooth-beacon-tracking

> Anonymously trace possible infections using p2p bluetooth

[Devpost](https://devpost.com/software/corona-bluetooth-beacon-tracking) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[developer_tools]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** android, couchbase, docker, ios, javascript, node.js, xcode

## How they structured the write-up

- inspiration
- technical implementation
- our team
- what we achieved during #wirvsvirus and covid-19 global hackathon
- what's next with cochain?

## Body

inspiration Movement patterns can be extracted from cell phone movement data from network providers, which have to be anonymously processed . This data only shows where and how many people were in one place with an inaccuracy unworthy of droplet infection. At the same time, devices in Apple Stores speak to our cell phones as soon as they are close enough – without revealing the owner's personal information. Corona and other viruses are also transmitted in close proximity. So why not use the same technology to show reliable contact chains? technical implementation Our CoChain app works with iBeacons. It forms an individual code and exchanges it with other CoChain apps on the devices of our fellow human beings – in the background. The identity of the owner remains unaffected. Only the apps talk to each other. Micro-location is not a problem. CoChain remembers date, duration and distance and creates an individual history for each device. It also assesses the likelihood of infection risk. As soon as one of these "hit" devices reports as "infected", my app CoChain updates the information and shows this in my personal infection chain. our team We got together during #WirVsVirus in a team of five and divided up according to our abilities. Marcus: Idea, Repository, Docker, Database Lars: iOS Peter: Backend Patty: Android Katrin: UX, UI What we achieved during #WirVsVirus and COVID-19 Global Hackathon UX, UI Prototype Click dummy iOS app Working prototype that can be distributed via TestFlight. IBeacons are broadcast and received. The data is uploaded to the server, and the health status can also be set. Android app Prototype that broadcasts and receives beacons. The beacons should be compatible with the iOS version. Backend Docker environment on a test server with Couchbase and NodeJS , which (theoretically) can be scaled up (12factor, stateless, shared-nothing multimaster database) Anonymization Only anonymous BeaconIds are exchanged between devices via Bluetooth and uploaded to the server. The implications here are the same with a given SDK as for any device that sends ids. In order to prevent third-party tracking, the ids could still be rotated randomly in the future. The user can use the app to switch to "sick" or "healthy". Other users who have received beacons from a potentially infected user only find out when they were in contact, not with whom. Logic It is insane how complex it is to produce map-reduce views in a short time that compare the intervals in which a user could be infectious and in which he met another. All of this, of course, retrospectively to cover the unconscious incubation period. What's next with CoChain? The possibilities are many. We would start with this app. International available Interchangeable for all kinds of viruses Expandable for publicly visited places (Equip elevators, toilets, car sharing with iBeacons that contain information as to whether they are contaminated or not) Cooperation with Apple / Google to integrate the basic functionality into the respective operating / ecosystem without the need for an app in the foreground. This is the only way to reach a relevant number of users. <div