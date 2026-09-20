---
slug: "storm-vision"
url: "https://devpost.com/software/storm-vision"
title: "Storm Vision"
hackathon: "Google Photorealistic 3D Maps Challenge"
organization: "Google"
winner: true
words: 488
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Storm Vision

> Storm Vision is an application that uses Google Photorealistic 3D Maps in Maps JavaScript API and Maps Platform APIs to provide advanced situational awareness to users before and after a hurricane.

[Devpost](https://devpost.com/software/storm-vision) · hackathon [[Google Photorealistic 3D Maps Challenge]]

## Facets

**domain** [[disaster_emergency]]
**user** [[researcher]]
**substrate** [[geospatial]] [[web_dom]]

**stack** css, html5, javascript, node.js, python, vite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for storm vision
- additional info

## Body

Home Page Peak Surge Routes Wind Field Inspiration Extreme weather events are increasing in frequency and severity. They pose a significant threat to life, infrastructure and a region’s economy. According to NOAA, “Of the 363 billion-dollar weather disasters since 1980 (as of August 2023), tropical cyclones (or hurricanes) have caused the most damage: over $1.3 trillion total, with an average cost of $22.8 billion per event. They are also responsible for the highest number of deaths: 6,890 since 1980.” NOAA Given the statistics above and the fact that some of the most severe hurricanes have occurred in the past decade, I decided to use hurricanes as a scenario to demonstrate a disaster resilience tool using 3D Maps in Maps JavaScript. What it does Photorealistic 3D Maps offers an advantage in terms of visualizing on the web information like peak storm surge and wind fields. Compared to 2D, 3D creates a more engaging and emotionally resonating way for users to engage with this critical information and personalizes the experience so that users can explore locations that may be affected in a storm that are crucial to their way of life. How I built it I initially conducted a lot of research in various problem spaces before deciding on extreme weather events and hurricanes. The demo was built mainly with HTML, CSS and Vanilla JavaScript. I had to use Node and a few Python scripts to convert/process large Geospatial datasets to suitable formats that would work with the alpha version of 3D Maps in Maps JavaScript. Challenges I ran into Working with large datasets and different geospatial file formats and finding ways to display the data. Accomplishments that I'm proud of That the demo is useful in its current front-end version and can still use data from any hurricane and Maps Platform APIs to create visualizations. The app has broad applications and can be useful for individuals, emergency and disaster managers, operators of critical infrastructure and even for scientists and researchers to visualize historic data or models. It can also be scaled to include other extreme weather events, like wildfires, and winter storms in the future. What I learned I learnt a lot during the process of developing Storm Vision including: Geospatial data formats and algorithms. Google’s Maps Platform APIs and how to access and integrate them into applications. A lot about development and deployment in general. What's next for Storm Vision -Integrating more APIs -Backend development Additional Info Storm Vision can fall both into the category of location discovery and sustainability and built environment. Both before and after a storm, layers of complexity are introduced in terms of navigating and accessing key resources within a community or a region, Storm Vision helps to simplify this process. Additionally, hurricane and extreme weather events interact with the built environment, visualizing their potential impact can help in sustainable design both on a small scale or a larger scale like natural barriers. <div