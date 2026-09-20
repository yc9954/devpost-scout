---
slug: "govalert"
url: "https://devpost.com/software/govalert"
title: "GovAlert"
hackathon: "MongoDB World Hackathon"
organization: "MongoD"
winner: true
words: 598
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/labor_employment"
  - "substrate/geospatial"
---

# GovAlert

> Be in the know when weather impacts your mission.

[Devpost](https://devpost.com/software/govalert) · hackathon [[MongoDB World Hackathon]]

## Facets

**domain** [[civic_government]] [[labor_employment]]
**substrate** [[geospatial]]

**stack** css3, es6, esri, html5, javascript, mongo-atlas, mongo-compass, mongo-stitch, mongodb, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for govalert

## Body

Using the map to see contracts, some free and some impacted by weather alerts. Viewing details of impacted contracts. Applying the agency filter to see contracts of interest. Viewing a list of active alerts. On loading, the map indicates distance to the closest alert. Inspiration Through our work with the Federal Government, we know that contractors are a critical part of an agency's ability to accomplish its mission. When major weather events occur, it disrupts the lives of those contractors and impacts the money involved. We want contractors and agency officials to be in the know when weather warnings will impact the contractor workforce. What it does GovAlert brings together publicly available data, combining it into a single, streamlined process, and adding new meaning to the data. We make identifying the impact of a weather alert is as simple as searching on a map. How we built it See the code at https://github.com/540co/govalert . Mongo's Atlas cloud store provides the core of this data-driven application. The contracts collection contains a recent copy of government contract data ingested via a python script . Mongo Stitch made it simple to stand up endpoints to access our data while also tying into external data sources and APIs . We used Mongo Compass along the way to analyze and understand the data. We coupled these Mongo technologies with ArcGIS to generate an interactive map overlaid with meaningful, interpreted data. Challenges we ran into Right out of the gate, we struggled to contextualize and ingest the huge amount of contract data necessary for our system. Data analysis let us generate an ingestion script that pared down the government contract data to its necessary elements. Our most difficult challenge lay in coupling the weather data with that of the contracts. The National Weather Service data uses industry-specific geocodes to indicate location -- data not present in the contracts. We worked both ends of the problem, processing the data as it was ingested, to provide geographic context, while using our API to interpret and compare the data on the fly. Additional challenges included providing enough continuous data to the front-end to make the map useful, while limiting the load to keep things speedy. Finding geographic distances efficiently also presented difficulties, as did extracting the geographic area of the map that the user sees for use in filtering the data. Accomplishments that we're proud of We started our project halfway through the allotted time, with very little idea of what steps would be necessary to accomplish our goal. Despite new challenges at every step, through collaborative research and a good amount of grunt-work, we stood up a functional, useful application in a brief time -- and made it look good, too. What we learned The upside of facing so many challenges is that we all encountered a cross-cutting view of the solution. Besides gaining an understanding of data that has relevance to our work as a company, we learned how to interpret and apply geographic data in new contexts. We also learned much more about what's offered by various Mongo tools, and got a chance to dive into some of the newer features, such as Stitch's static hosting. What's next for GovAlert From the start, we developed a broad set of user stories to help contractors and agency officials limit the impact of weather events. Due to time constraints, as predicted, we focused on implementing the most critical and useful features. We'd love to continue to build out the system, making it more robust, more full-featured, and more beneficial to government contractors across the country. <div