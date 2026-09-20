---
slug: "geoworx"
url: "https://devpost.com/software/geoworx"
title: "GeoWorx"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 683
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/immigration_refugee"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# GeoWorx

> A geo-localized service based marketplace to get things done!

[Devpost](https://devpost.com/software/geoworx) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**domain** [[disaster_emergency]] [[education]] [[elder_child_care]] [[immigration_refugee]]
**user** [[educator_student]] [[general_public]]
**substrate** [[geospatial]] [[web_dom]]

**stack** amazon-alexa, amazon-web-services, angular.js, firebase, heroku, tomtom, visa

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for geoworx

## Body

Inspiration Let's say you come back home tired and you want someone to walk your dog, or you walk into a conference and realized that you forgot your charger and you have a presentation coming up in half an hour! Or you just walked into an exam and forgot your calculator. We all run into scenarios where we can use some help from people around us but until now, there wasn't a centralized platform to create a localized service-based marketplace. That is where GeoWorx becomes the most powerful tool in your arsenal. What it does GeoWorx allows requesters to post jobs / errands / tasks that can be done by helpers around them. Helpers can see all the jobs in their vicinity in a map view and a list view along with job description, price/incentive, expiry time and tags. When helpers accept a job, they can interact with the requesters on GeoWorx's messaging service. So next time when you are in the office swamped with work and don't have time to get lunch, post your request on GeoWorx and someone will get lunch for you. On the Helper's side, let’s say you’re interested in accepting a job, but don’t know quite how to get started fulfilling it. This is where the Tom Tom API makes the entire experience a breeze. Using the Tom Tom points of interest service, we recommend the nearby places on the map that might be most useful in helping the job get done. For example, if someone is hungry and posts a job request and tags it with “food”, we will flag close by restaurants that the user sees once they accept a job. Usage Scenarios: Universities Conference Concerts Lending and borrowing Commodity exchange Services exchange Disaster relief How I built it Our core stack leverages a spectrum of technologies and frameworks to deliver a seamless experience to our users Firebase Angular JS Amazon Alexa AWS Google Maps API TomTom API - Get all Point of Interests related to a specific job. Visa API Challenges I ran into Creating a platform agnostic web application that shows localized results was challenging. We had to create an experience that was intuitive and seamless for everyone. As this application can pretty be used by anyone - Students, professionals, senior citizens, etc. we mapped out the core components and the core scenarios before mapping out the technologies to be used. Then finding the right set of frameworks and libraries was challenging as many required customizations without deteriorating the user experience. Accomplishments that I'm proud of We managed to get multiple sponsor APIs Integrated through which we learned a great deal about using their technologies as well as the pros and cons of them. We managed to get an end to end software product functionality along with integrating our solution to Alexa and have a working prototype that is already used by 30 users since launch and they are loving it. We also finished integrating our basic webpage with a dashboard template and explored AWS lambda and AWS Gateway API to expose rest endpoints. We also learned how to use serverless for the purpose of pushing code to aws cloud. What I learned We learnt how to integrate multiple components and run a project with end to end functionality- we built out a dashboard, rest services, a process to receive messages and have data persistence layer along with amazon alexa. We learnt how to divide a big project into small achievable milestones and delegating equal amount of work to reduce duplication or blockers for any person in the team. We also learnt how to find "hacks" and workarounds for problems that give us solutions as quickly as possible - we got better at optimizing our work besides our algorithms :) What's next for GeoWorx Adding more intelligence to our unique scenarios like querying for jobs, recommending prices, optimized for delivery time and distance. In future iterations, we would like to utilize NLP to parse out more exactly what the job requester wants and accordingly make more specific recommendations to the job accepter (helper). <div