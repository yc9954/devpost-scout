---
slug: "i-see-tp"
url: "https://devpost.com/software/i-see-tp"
title: "I See TP"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 417
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# I See TP

> Find locations that have emergency supplies including toilet paper, masks, & water.

[Devpost](https://devpost.com/software/i-see-tp) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** android, android-studio, firebase, geo-fire, google-directions, google-maps, java

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for i see tp
- future features

## Body

Map showing test data of different locations This location is reported to have all items at it. This location doesn't have lysol wipes, rice, or ramen. This location is reported to not have anything. We could hide it, but then we might get duplicate submissions. Instead users can update it. Inspiration Steve and Moksh both had been impacted by stores running out of essentials such as toilet paper and water. They knew that there had to be a way they could use technology to aid in this issue. What it Does I See TP is an Android app that allows users to find and submit stores or other locations that have emergency essentials available for purchase or trade. It will display whether an item is in stock or not. The items that the app currently display include toilet paper, masks, sanitizer, lysol wipes, water, rice, ramen, and milk. Users can also filter what the map shows if they are only looking for particular items. Any user can submit, edit, and report locations; nobody has to register to use the app. How We Built It Steve had an app very similar to this already made, the Outlet Finder. This app allowed users to find and submit locations where electrical outlets are available to charge your phone, laptop, etc. We modified that project to allow users to submit spots where they knew essentials were available. It took one week to setup two new databases (dev and production), build the app and website, write up a usage guide and FAQ, and create a basic store listing for download. Challenges We Ran Into A lot of time was spent trying to come up with a clever name for the app. One where the web domain was still available and would be easy to share with people. In retrospect, this is silly because we could've added other features to the app with that time instead. Accomplishments that We're Proud of We put a lot of effort into making the app update positions and details in real time as users interact with the app. What We learned We learned how to utilize Firebase more efficiently, not only to show data in real-time, but also how to load it faster than before. What's next for I See TP iOS Version Translated versions AI features Future features New items to track More detailed information regarding the types of items (quantity, quality, etc.) Account management options for gamified modes to encourage users to add/update locations <div