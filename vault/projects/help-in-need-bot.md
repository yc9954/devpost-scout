---
slug: "help-in-need-bot"
url: "https://devpost.com/software/help-in-need-bot"
title: "Help In Need Bot"
hackathon: "2018 Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 827
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/housing_homeless"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Help In Need Bot

> This bot will allow you to empower members of the community by fostering help for each other.

[Devpost](https://devpost.com/software/help-in-need-bot) · hackathon [[2018 Developer Circles Community Challenge]]

## Facets

**domain** [[housing_homeless]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** facebook, google-maps, mapquest, mongodb, node.js

## How they structured the write-up

- inspiration
- updates since the regional winners were announced
- what help in need does?
- current reports

## Body

Help In Need Say hello to the first humanitarian bot . This bot will allow to empower, help and bring communities together. Inspiration Living a changing economy, while walking in the streets of Buenos Aires we have witnessed the homeless population increasing day by day. That's when we thought we could do something to help, and we did it, the best way we knew. We created a tool using technology that allows us to help our community in an intuitive way. This is how "Help In Need" was born. Updates since the regional winners were announced Implemented a Web Application We created a Web Application that allows to show all the locations reported from a MongoDB Database. For doing that we did the following tasks: Integrated Customer Chat Plugin for Facebook Messenger Created an Express Application Implemented a View Engine ( Handlebars ) Implemented Google Maps API Migrated from a in memory database We migrated our database from a in "memory base" to a non relational database (MongoDB). We implemented the mLab online service that provide a Free MongoDB Database. Generate Schemas Creation of Script for Inserts and Deletions Implement MongoDB NPM Dependency Static Maps on Bot To improve the helping process, we changed Google Maps links for a "static image" map. In this way we can show some locations near by the location reported. To accomplish that we chose MapQuest (basically because it is free, and Gmap not) Posts on Facebook Page We also implemented the FB Graphic API to post on our Facebook Page when a user report a location. Hence, every user who follow our page will see reporting updates. What Help In Need does? This bot will empower members of the community by fostering help for each other. If you want to help someone, all you have to do is open Facebook Messenger and search for "Help In Need". Once a conversation is started, you will be able to choose: Report the location of someone in need Help someone close to you Report When the options appear you will be able to choose Report . Once you choose this option, you will see a button ( Send Location ) to share the location of someone in need. If you are close to the person just share your current location. You can search location by address or drag a waypoint on map. That`s it. Now other people or organizations can find and assist them! Help You can also search for people in need around you so that you can provide help. When the options appear you choose the option Help . So, using our database any person or organization could use this information to help someone in need. We provide an Static Image generated from an integration with MapQuest . This photo will show your location with a red marker. And it is going to show the top 5 near locations with violets markers. We are also providing you with a link to our Web Page that is going to show the map centered with the location that you shared. This will allow you to see all of the nearest locations reported. Text Intelligence We also provide a text parser that can identify keywords to detect if you want to report or help: Home Page We also have a Home Page . In this homepage you can visualize all the locations that have been reported using the Help In Need Bot. Current Reports We count with a World Report Count on the right side of the page: How we built it With a nail and a hammer... just kidding!. This application was created using NodeJS . These are the main packages that we are using: Facebook API NodeJS MongoDB Google Maps MapQuest Express Challenges we ran into Thanks to our technical experience, the challenge focused on how to provide the easiest flow. After several twists and turns we managed to find the best way to help. Accomplishments that we're proud of We are proud to have a functional bot that is able to tell us whether there is anyone nearby who needs our help. We believe that this bot can be used and tested in small cities. What we learned You do not have to be a millionaire; with will it is possible to help and encourage others to do it. What's next for Help In Need Bot We think that the information we received from all people on facebook, about ones another who need help, it is really useful and it could be used in different ways. Every organization which aim to fight against homelessness can use our database to find these people who really need their help. We could also think in a notifications system, in which you can subscribe it via REST api and you will receive the same locations that we received from our bot. License Released under the terms of the MIT license. About Ariel Rey Horacio Lopez <div