---
slug: "routobahn-80g9tw"
url: "https://devpost.com/software/routobahn-80g9tw"
title: "Routobahn"
hackathon: "MLH Local Hack Day (2018)"
winner: true
words: 290
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
---

# Routobahn

> Decreasing air pollution, traffic congestion, and travel costs. What else!

[Devpost](https://devpost.com/software/routobahn-80g9tw) · hackathon [[MLH Local Hack Day -2018-]]

## Facets

**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]]

**stack** ajax, c#, css3, google-maps, html5, javascript, json, postgis, postgresql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for routobahn

## Body

Inspiration One day when riding on the bus, we have seen that most of the cars have only one seat, the driver, occupied in the car. When there is a possibility of using all five seats in a compact car, why do we only use one? We will decrease traffic congestion, air pollution (every car causes 260 pounds of air pollution in a year), and travel costs by 500% by using all five seats. While Uber is only making transportation easier, it is too expensive. From Irondequoit to RIT it costs around 25 dollars, and the calculation we did for our project is around 1.75 dollars per ride making it more cost effective than public transportation. What it does The web app is a prototype that gets the shortest distance between two points. The users selected by the driver are picked up, and then the shortest path to the destination is calculated. The price of gas usage is calculated by the distance every user will travel. All the costs are gathered and given to the drive and 20% goes to the application owner. How we built it We used the Google Maps API's to get the shortest path between two points, and to get our current location, and directions to get to the final destination. The longitude and latitude values are stored as hashed values using postgis. Challenges we ran into While using the Google Maps API, we had some trouble figuring out how to find the closest people to the users location. What's next for Routobahn Today we have got this far prototyping this project. Building this project in the IOS and Android platforms and improving the design and backend development of the product is the next goal. <div