---
slug: "polku"
url: "https://devpost.com/software/polku"
title: "Smart City Maintenance"
hackathon: "Junction 2017"
winner: true
words: 365
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/scientific_research"
  - "user/general_public"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
---

# Smart City Maintenance

> Serving citizens faster with smart task processing

[Devpost](https://devpost.com/software/polku) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[scientific_research]]
**user** [[general_public]]
**substrate** [[genomic_bio]] [[geospatial]]

**stack** ibm-watson, node.js, vue.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for polku

## Body

Solution screen 1 Solution screen 2 Solution screen 3 Solution screen 4 Solution screen 5 Mapping history data and geodata to service tickets. This gives risk estimate for a ticket Inspiration Imagine being in customer service receiving hundreds of feedback tickets every day from multiple sources and trying to forward the problems to the right teams. This manual task processing is slow prolonging the maintenance services arrival on site. We wanted to improve this process by applying analytic and cognitive services. What it does A simple analytics engine that can be easily integrated with existing Stara & CoH operational systems using our APIs. The system is able to process and analyse received work requests and make decisions based on: History data Geolocation data User feedback sentiment System can be easily extended to include other data sources or new analytics elemensts making it even smarter. The system consists of the following analytics components: data-enrichment component: Uses damage compensation history and geolocation data to estimate a cost risk related to a new service request Analytics component: Analyzes service request sentiments using Watson cognitive services, keywords, concepts, entities to see automatically see what the service request is related to. Decision-making component. Makes use of analytics component to route the service request to the correct team. How I built it System connect to Helsinki city API or you are able to simulate a new service request. We had to do simulation because current city of Helsinki systems are not real-time and have few days delays. System then reads service requests and applies analytics on them. We use commonly available open source mechanisms and IBM Watson analytics services for this. Challenges I ran into Stara map coordinates were in uncommon format. Accomplishments that I'm proud of Emptied 5 protein puddings - Sakari. We produced suprisingly a lot of code in this short time. This is because solution architecture is flexible and easily extendable thus we wanted to improve analytics further and further. What I learned We had opportunity to see the wide variety of information that Stara has to deal with daily to maintain City of Helsinki. What's next for Polku Sleep! Then party. Or first party, then sleep. <div