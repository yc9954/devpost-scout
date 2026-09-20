---
slug: "trip-planner"
url: "https://devpost.com/software/trip-planner"
title: "Trip Planner"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 344
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/education"
  - "user/educator_student"
---

# Trip Planner

> The only skill which allows you to plan trips locally and discover the local delights in a city whenever, wherever.

[Devpost](https://devpost.com/software/trip-planner) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[education]]
**user** [[educator_student]]

**stack** foursquare, google-places, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for trip planner

## Body

The only skill which allows you to plan trips locally and discover the local delights in a city whenever, wherever. Inspiration Our inspiration coms from the fact that we were students in a new city, which we wanted to explore but there seemed no application which would help us explore locally. All applications were geared towards planning long trips, there existed nothing to help us plan an exciting day to take in the local attractions. To fill this need, we decided to come up with an idea which helps users explore more intelligently and easily. What it does Trip planner is very simple to use. Just ask it to plan a trip in any city you want and it will plan an exciting trip for you. Just ask "Alexa, Ask Trip Planner to plan me a trip in New York”. How we built it We collect data from multiple sources such as FourSquare, Google Places, and we leverage the data we received to plan a trip based on various factors using our AI. Challenges we ran into Our job was essentially to get the user from their starting location and back with an amazing trip in between. This in essence is the Traveling Salesman problem which is a NP problem which does not have a polynomial time solution always. We had to come up with an efficient algorithm which goes around this problem. Accomplishments that we're proud of The fact that we essentially took an NP problem and made it work in a way such that the user does not notice any lengthy delays in the time it takes to receive their response is something we are proud of. What's next for Trip Planner We have planned to integrate a lot of exciting new features into the skill in the next few days such as more dynamic duration setting, allowing user to plan longer trips, setting the theme of a particular trip ( e.g. Hiking only trips, Clubbing ), making the skill more personal in the way solutions are tailored to the user. <div