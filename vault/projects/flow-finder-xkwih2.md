---
slug: "flow-finder-xkwih2"
url: "https://devpost.com/software/flow-finder-xkwih2"
title: "Flow Finder"
hackathon: "EducateHacks 2024"
organization: "EducateHacks"
winner: true
words: 258
team_size: 5
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/education"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Flow Finder

> Flow Finder is a crowd sourced database of locations that give out free menstrual hygiene products.

[Devpost](https://devpost.com/software/flow-finder-xkwih2) · hackathon [[EducateHacks 2024]]

## Facets

**domain** [[education]]
**substrate** [[geospatial]] [[structured_db]]

**stack** geocoder, map-api, mapbox, ruby, ruby-on-rails, rubygems

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for flow finder

## Body

Inspiration I came up with idea when I was teaching a Girls Who Code club. The girls were creating variables when I heard two of them worrying about what would happen if they started their periods in public or at school. 1 in 10 girls miss school due to lacking essential menstrual hygiene products, and nearly 2/3 of low-income women can't afford them (a situation known as "period poverty"). Flow Finder seeks to address period poverty and keep girls in school. What it does Flow Finder is a crowd sourced database of locations that give out free period products. It finds the user's location and displays places that give out free period products near them on a map. Instead of staying home on their periods, girls and women can use the app to find products. How we built it We used Ruby on Rails in backend for the project mainly for storing the data of the person and we used Geocoder (a gem in Rails for tracking location of the address), and we used Mapbox library for creating the map that displays locations near the user. We used library like Bulma (a CSS library) to create the UI. Challenges we ran into Integrating the geocoder gem was challenging because none of us had used it before. What we learned We learned how to use Ruby on Rails - most of us had no experience with it. What's next for Flow Finder We hope to use PostgreSQL as well as implement a pagination gem to handle larger datasets. <div