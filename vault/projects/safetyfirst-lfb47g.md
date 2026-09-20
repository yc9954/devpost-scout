---
slug: "safetyfirst-lfb47g"
url: "https://devpost.com/software/safetyfirst-lfb47g"
title: "SafetyFirst"
hackathon: "Junction 2017"
winner: true
words: 333
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SafetyFirst

> A smart system for recognizing safety hazards for civilians

[Devpost](https://devpost.com/software/safetyfirst-lfb47g) · hackathon [[Junction 2017]]

## Facets

**domain** [[disaster_emergency]] [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** javascript, jquery, python, react, sql

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for safetyfirst

## Body

Video demo: https://youtu.be/bIb28quoVLw?t=1h59m53s Inspiration I wanted to create an application that could make use of ESA's Sentinel satellite imagery data in order to determine obstacles along roads for civilian clearing purposes. What it does This program allows users to determine the most efficient path for drivers to take using Dijkstra's algorithm and machine learning optimization (two-class decision forest). Each of the coordinates along the polyline correspond to an image from satellite data, which is then scored based on relative safety. Users are also prompted to respond with realtime data regarding obstacles along roads which are then used to improve the algorithm. How I built it SafetyFirst was built in React Native and Javascript, with Python on the backend for handling REST API calls, database calls, and CORs. The backend is being hosted on an S3 instance and Elastic Beanstalk, with the database hosted on DynamoDB for easy access. Challenges I ran into It was difficult to work across datasets, parsing information from remote servers. It was also difficult to work on different domains for certain APIs that required authentication or headers for validation. Accomplishments that I'm proud of SafetyFirst is able to deliver results that are comparable to those of Google Maps, with the added feature that it improves the safety of drivers and civilians. What I learned I learned about how to develop for React Native, interfacing with CORs, and interacting with .tif images for ESA datasets. I also learned more about how to clean data and implement accurate and fast machine learning models (running the models took a long time, as expected). What's next for SafetyFirst I'm currently working on implementing a Unity extension that will map out a 3D path for the roads based on GeoJSON and encoded polyline data from SafetyFirst. This will allow drivers to search through a more updated version of their environment than Google Streetview can provide, which can be updated with current obstacles (snowbanks, leaves, traffic accidents, steep roads from natural disasters, etc.) http://baconcookies.net <div