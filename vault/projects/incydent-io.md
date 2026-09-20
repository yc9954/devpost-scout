---
slug: "incydent-io"
url: "https://devpost.com/software/incydent-io"
title: "#Incydent"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 367
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# #Incydent

> Incydent combines the reach of the crowd and the power of machine learning to help municipalities with strained resources combat natural disaster, social injustice, and future health threats.

[Devpost](https://devpost.com/software/incydent-io) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]]
**domain** [[civic_government]] [[climate_energy]] [[disaster_emergency]] [[health_clinical]]
**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]]

**stack** firebase, javascript, node.js, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for incydent.io

## Body

Inspiration It's not difficult to imagine the profound difficulties that the future may bring. With a warming climate, each year brings the possibility that inadequately maintained utilities will spark the next firestorm and devastate the next or same community. With uneven policy and inadequate tracing, transmissible diseases that escalate to pandemic status with a devastating human and economic toll may become an uncommon and unwelcome future. Small incidents begin to spiral with exponential force. What it does Incydent allows each and every citizen to alert municipal services of dangerous situations while they are still small and tended to easily. With the simple act of capturing an image tagged with the #incydent hashtag, Incydent.io processes threats using machine learning for delivery to municipal services by governing region. Whether it is as small as a pot hole or as devastating as the next firestorm, Incydent streams allow health, safety, utility organizations to ingest, triage, and react to the next disaster. Built upon Quickbase's pipelines and simple, visual customizable logic, the clonable Incydent app allows the simple triaging of an Incydent stream for handling by the appropriate governmental on non governmental organization (using webhook egress). How I built it The Incydent stream is currently built upon Twitter ingestion (allowing multiple client ingestion solutions), custom real time database communications, and real time machine learning technologies to create labeled streams of incident data. Quickbase pipelines are used for ingestion of the streams as well as data export to the targeted service. Quickbase' simple kanban reports and easy visual record system forms the foundation of the human in the loop triage system. The simple, cloneable nature of Quickbase apps means an organization can quickly adopt and adapt a triage workflow into the smallest of departments. Challenges I ran into Building the system in a limited amount of time. The easiest part was integrating with Quickbase. Accomplishments that I'm proud of If it ends up being able to help someone in the real world, I will be very happy with the project. What I learned What's next for Incydent.io Bringing a real world test of Incydent to a municipality. The simplicity of the design needs to be verified for a simple use case. <div