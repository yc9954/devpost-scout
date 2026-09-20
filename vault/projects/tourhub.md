---
slug: "tourhub"
url: "https://devpost.com/software/tourhub"
title: "tourhub"
hackathon: "Hack the North 2019"
winner: true
words: 319
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/education"
  - "domain/retail_commerce"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# tourhub

> Powered by Accenture's Accentours API, tourhub provides students and educational leaders access to affordable, reputable and personalized university tour packages.

[Devpost](https://devpost.com/software/tourhub) · hackathon [[Hack the North 2019]]

## Facets

**domain** [[education]] [[retail_commerce]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** accentours, css, firebase, html, javascript, python, react

## How they structured the write-up

- tourhub
- what it does
- how we built it
- accentours api usage
- challenges we ran into
- accomplishments that we're proud of
- what's next for tourhub

## Body

Welcome Menu Registration Screen Showcase Screen tourhub Powered by the Accentours API What it does tourhub is a web application that simplifies the organization of student university tours. The application gathers information about Universities, Hotels, Flights and Car Rentals, and puts together a personalized travel experience catered to each student's needs. The application ensures that customers are getting the best possible deals, and has a wide range of flexibility to support various travel situations. Educational staff can also benefit from tourhub's order system, which handles large class sizes to give teachers peace of mind. How we built it The front-end of the web application was developed using HTML/CSS, along with React and Bootstrap. Meanwhile, the client-side hosting, database hosting, and domain hosting were all handled by Firebase and Google Cloud. The vast majority of the API and back-end work was done through Node.JS and Postman. Accentours API Usage GET /get_universities: listing all potential tour destinations GET /get_tours: listing all potential tours GET /get_tours_by_city/: users can search up desired tours by destination GET /get_bookings/: user profile displays all previous bookings GET /get_availability/: users can filter out tours that do not fit their number requirements POST /create_user>username=: creates users in Accentours database as well as Firebase database POST /book_tour?tour_id=&spots_required=&username=: users can freely book tours Challenges we ran into Integrating Firebase's Authentication system into the React framework proved to be more difficult than expected. We also faced challenges with API integration, routing, and version control. Accomplishments that we're proud of We're proud of how we managed to integrate so many new and different systems together, and how we each managed to learn a new skill/technology through this event. However, we're most proud of our solid teamwork and collaborative spirit. What's next for tourhub The application has plenty of room for growth and improvement. Some possible next steps include: comprehensive booking for more educational activities, special themed trips/events, and more e-commerce technology. <div