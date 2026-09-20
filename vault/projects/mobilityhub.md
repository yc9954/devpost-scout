---
slug: "mobilityhub"
url: "https://devpost.com/software/mobilityhub"
title: "MobilityHub"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 663
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/geospatial"
---

# MobilityHub

> Intelligent proximity-based medical services recommender utilizing Native CoreLocations Framework and Natural Language Processing

[Devpost](https://devpost.com/software/mobilityhub) · hackathon [[HackSwift 2024]]

## Facets

**domain** [[developer_tools]] [[elder_child_care]] [[finance_payments]] [[health_clinical]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** corelocations, mapkit, swift, swiftui, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mobilityhub

## Body

Displaying services relevant to user's query Showing directions to result destination Inspiration A few months ago, one of my friends’ parents suffered from a cardiac arrest in the middle of the night. In an effort to not disturb his wife or kids he attempted to drive to the hospital he usually goes to by himself, but unfortunately, it took him too long to get to the hospital and he wasn’t able to get treated on time. But had he known that there was an emergency health care provider closer than his hospital, he would have likely gotten treated sooner and could have survived. The importance of having accessible health care services inspired me to develop Mobility Hub - I wanted to make medical services more accessible and inclusive to everyone. Having accessible health care services is also of great relevance for elderly visitors and for people not as familiar with the area. What it does My app allows users to type what kind of service or location they are looking for, and then displays the locations of services closest to them relevant to their query in a scrollable list. For each result location, my app renders the route from the user's current location to the result location on to the map. In addition, my app also displays the street address and distance to each result location when selected from the list. How we built it I build this app using Swift on XCode. In developing this app, I leveraged Apple’s MapKit framework to help render an interactive map view on which the user can see their current location as well as the locations of and routes to each of the result locations. I also used Apple’s CoreLocation framework to make backend calls in determining the distance and route between locations. Challenges we ran into It was initially quite a challenge for me to figure out how my program could handle backend calls for routing information and reliable location data. I was able to deal with this difficulty by conducting research on existing location service frameworks and found the API of the CoreLocations framework offered by Apple’s Developer Documentation especially relevant for this purpose. Accomplishments that we're proud of My app allows the user to see all the hospitals located in the area filtered by the distance to it, enabling them to choose the hospital closest and most accessible to their current location and also get treated sooner. This way, my app allows the user to make a more informed decision of where to go. My app is also capable of displaying the directions to any user-specified category of medical service, and is also to specific street addresses entered by the user. Ultimately, my app allows the user to see all the hospitals located in the area filtered by the distance to it, enabling them to choose the hospital closest and most accessible to their current location and also get treated sooner. What we learned I gained a much better understanding of how Apple’s MapKit framework can be used to display an interactive map view, and how the Core Locations framework can be used in making backend calls to determine the distance and route between two locations. What's next for MobilityHub For a 2.0 version of my app, I would add support for more languages so people from other regions that may not have English as the primary language can also use my app to find the services they need. Moreover, the current version of my app recommends medical services and addresses close to the user’s location; however, in this day and age, the existing technology presents too much information to us users. In a future version, I will add the capability of my app to perform web scraping on multiple sources to recommend hospitals or health care providers covered by the user’s insurance provider and at an affordable pricepoint for the user. Attaching the Github project and a shorter demo clip below! <div