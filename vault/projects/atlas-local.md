---
slug: "atlas-local"
url: "https://devpost.com/software/atlas-local"
title: "Atlas Local"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 999
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Atlas Local

> Your community's potential, mapped.

[Devpost](https://devpost.com/software/atlas-local) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[climate_energy]] [[developer_tools]] [[education]]
**user** [[developer]] [[researcher]]
**substrate** [[geospatial]] [[web_dom]]

**stack** api, javascript, maps, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- things we're really proud of
- what we learned
- what's next for atlas local

## Body

Inspiration We realized that when people make huge life decisions, like where to live, they're missing a big piece of the puzzle. We all look at old data like school ratings, but what about the things that will affect our quality of life in the future? The lightbulb moment for Atlas Local was a simple question: "What if you could actually see how healthy a place is?" We got really excited when Google Maps Platform released its new Environment APIs. Suddenly, all this cool data that only scientists used to have, like air quality and solar potential, was available for anyone to build with. We started with the idea of a "Future-Proof Score" for a single house, but then we thought bigger. What if you could analyze an entire neighborhood? That's what really got us going: the idea of helping not just one person, but whole communities. What It Does Atlas Local is a website that turns a regular map into a tool for exploring the environment. It's built for everyone, from someone buying a home to a community group planning a new garden. Here's how it works: Check Out Any Single Spot: You can click on a building or just double-click anywhere on the map to get an instant analysis. For that exact spot, we calculate a "Future-Proof Score" that looks at: Solar Savings: How much money you could save each month by putting up solar panels. Air Quality: The current air quality score and what the main pollutant is. Pollen Levels: A heads-up on grass, weed, and tree pollen in the area. See the Big Picture: This is where things get really cool. You can use a drawing tool to select a whole area, like your block or a local park. The app then calculates the total potential for that entire zone: Total Solar Power: It adds up the solar potential of all the buildings to see how much energy the neighborhood could create. Community Rainwater: It estimates how much water could be collected from all the rooftops, showing a real path to water conservation. How We Built It We built Atlas Local as a modern website that runs completely in your browser. We used React and the Next.js framework, which means it’s super fast and doesn't need a clunky backend server. The Map: The interactive map is built with the Google Maps JavaScript API , which we connected to our app using a popular library for React. The Data Engine: The real magic comes from Google's Environment APIs. We make live calls right from the website to: The Solar API to get the financial and energy details for buildings. The Air Quality API to grab the latest air conditions. The Pollen API for the allergy forecasts. To keep things snappy, we made sure all the data loads at the same time so you're not left waiting. Challenges We Ran Into We definitely hit a few snags along the way. Keeping our API Key Safe: Our biggest worry was that since the app runs in the browser, our API key would be visible. To fix this, we went into our Google Cloud settings and locked the key down so it would only work on our website's domain. Problem solved. Creating One Score from Different Data: How do you mix apples and oranges? We had to figure out how to combine dollar savings, an air quality index, and a pollen count into a single score. We spent a lot of time on this, creating a formula that turns everything into a simple 0-100 scale before averaging them into the final "Future-Proof Score." Analyzing a Whole Area: Figuring out the solar potential for a whole neighborhood without making a thousand API calls was a puzzle. It would be way too slow and expensive. We built a smarter system that grids up the area you draw and takes a few clever samples to give a solid estimate for the whole zone, almost instantly. Things We're Really Proud Of The "Future-Proof Score": We're most proud of this core idea. Taking all that complicated environmental data and boiling it down to one number that anyone can understand feels like a huge win. The User-Friendly Panel: We love that our info panel works just as well whether you click on a specific building or a random spot in a park. Getting that to work smoothly in React took some effort. The Community Tool: Seeing the area analysis tool work for the first time was a true "wow" moment. Watching it calculate the combined solar power of an entire neighborhood in a few seconds showed us our bigger idea was possible. What We Learned First off, these new Environment APIs are a total game-changer. They give developers the power to build things that just weren't possible before. We also learned that just showing data isn't enough; you have to visualize it in a way that tells a story and helps people make decisions. And on the tech side, we got way better at handling all the moving parts of a complex app that runs entirely in the browser. What's Next for Atlas Local We feel like we're just getting started. Here's where we're headed next: Better Rainwater Calculations: We want to make our rainwater estimates even more accurate by adding local rainfall data to the roof size information we get from the Solar API. Tracking Trends and Sending Alerts: We plan to build a simple backend with Firebase to start saving environmental data each day. This will let us show people how their area is changing over time and even offer alerts for things like a drop in air quality. Tools for City Planners: We have a vision for an "Atlas Local Pro" version. It would let city planners simulate new projects, like drawing a new park to see how it might improve the local climate, or modeling a solar co-op to see how it helps the city meet its green energy goals. <div