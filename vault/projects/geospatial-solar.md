---
slug: "geospatial-solar"
url: "https://devpost.com/software/geospatial-solar"
title: "Geospatial Solar"
hackathon: "Google’s Immersive Geospatial Challenge"
organization: "Google"
winner: true
words: 265
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "user/legal_professional"
  - "substrate/geospatial"
---

# Geospatial Solar

> Combining the Google Geospatial API with the Google Solar API for instant analysis of a building's solar potential by simply tapping it.

[Devpost](https://devpost.com/software/geospatial-solar) · hackathon [[Google-s Immersive Geospatial Challenge]]

## Facets

**domain** [[climate_energy]]
**user** [[legal_professional]]
**substrate** [[geospatial]]

**stack** google-geospatial, google-solar-api, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for geospatial solar

## Body

Inspiration A few months ago I was looking through the various APIs Google had available and noticed the Solar API. Reading the documentation I was inspired to create a tool that let you choose a location to analyse in augmented reality. I made a simple prototype which I have expanded on and improved to enter into this hackathon: https://twitter.com/mechpil0t/status/1701828592374825020 What it does The app used the Google Geospatial Geometry to allow the user to tap on a building. The app then uses the Google Geospatial API to get the location of the tapped building and then queries the Google Solar API using that location. Once the app receives the data it visualises the potential area and number of solar panels in AR. How we built it It is built using Unity, the Google Geospatial API and Google Solar API. Challenges we ran into The main challenge was how best to display the information. In the initial prototype I simply showed some text to the user, but I wanted to better display the area and number of solar panels to the user. It was challenging to show this dry data in an interesting way. Accomplishments that we're proud of The simple but effective tap to select a building mechanic feels very satisfying. What we learned Don't judge a building’s solar potential by its cover. Some large buildings have very little potential while some modest size buildings seem ripe for solar. What's next for Geospatial Solar Being able to log the results would be useful in turning this from a novelty to a useful survey tool. <div