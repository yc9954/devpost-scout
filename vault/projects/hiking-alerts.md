---
slug: "hiking-alerts"
url: "https://devpost.com/software/hiking-alerts"
title: "Hiking Alerts"
hackathon: "Microsoft Fabric and AI Learning Hackathon"
organization: "Microsoft"
winner: true
words: 468
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Hiking Alerts

> Hiking alerts aims to standardize events issued by institutions for hiking trails in a global context. By linking the events with geospatial data users have a better overview on trail conditions.

[Devpost](https://devpost.com/software/hiking-alerts) · hackathon [[Microsoft Fabric and AI Learning Hackathon]]

## Facets

**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** angular.js, openai, python, spring-boot, tsql

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for hiking alerts

## Body

System Setup Inspiration When viewing and planning tracks, popular hiking apps do not display current information by official institutions for hiking tracks in a standard format. Instead, those apps heavily rely on their respective communities updating the information manually. This relevant information for hikers from institutions might include dangers, weather impacts, closures etc (in the following called events). When planning hiking tours solely via apps, there is a risk of overseeing important events. What it does Microsoft's AI and Fabric services enable to standardize the events issued by different institutions in a global context and connect the events with geospatial data. The purpose of the website and the API is to provide transparency on the accessibility of hiking tracks, making hiking safer and a more enjoyable experience ( https://www.hiking-alerts.org ). How I built it Essentially, there are three types of fabric notebooks extracting raw data from country specific data sources: Raw Event Parsers, which query the events every four hours Trail Parsers, which query trail geodata every month Region Parsers, which query boundaries for regions, e.g. parks, every month All those parsers insert the data into an Azure SQL database. For the raw events, there is a separate table (dbo.raw_events_CT) which tracks updates, insertions and deletes. An additional notebook job queries data from the raw_events_CT table every 4 hours and asks Open AI to standardize the raw events. The responses from Open AI are pushed to an Azure Blob Storage Queue. A Spring Boot application is responsible for querying the queue every 5 minutes and then mapping the input provided by Open AI to trail geodata. Any matches are then saved into an Azure SQL database. The Spring Boot application also serves the REST endpoints for the Angular frontend and a public facing API which allows users to insert, query and delete events from the database. Challenges I ran into One challenge were varying Open AI responses and correctness of the responses. The service handles those cases by making matching configurations in the Spring Boot application very strict. The intention is to make the service as accurate as possible. This means that not all events / alerts are mapped. Accomplishments that I am proud of Design of a scalable setup which allows to extend the service to further countries, thereby providing a unique service. What I learned Very valuable lessons were how to make Azure services available to Fabric notebooks and how to integrate Azure services with on-premise servers (here: the Spring Boot server). What's next for Hiking Alerts Onboarding further institutions. Switzerland / Swiss Alpine Club and Ireland / Sportireland are in progress. Reaching out to institutions which don't have a public facing endpoint, but collect data centrally, e.g. Finland / Metsähallitus & Canada / Parks Canada. Integrate a translation service to connect non-english data providers <div