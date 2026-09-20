---
slug: "geospatial-route-check"
url: "https://devpost.com/software/geospatial-route-check"
title: "Geospatial Route Check"
hackathon: "Google’s Immersive Geospatial Challenge"
organization: "Google"
winner: true
words: 307
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Geospatial Route Check

> This app provides a user with a route to a destination but also checks for additional requested locations along the way such as convenience stores, bus stops, or toilets.

[Devpost](https://devpost.com/software/geospatial-route-check) · hackathon [[Google-s Immersive Geospatial Challenge]]

## Facets

**substrate** [[geospatial]]

**stack** google-geospatial, google-maps, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for geospatial route check

## Body

Inspiration I use Google maps almost everyday to check routes while walking around the city. While it is very convenient, the standard routing on the Google Directions API is very sober and navigation is given without superfluous information. I thought it might be useful for planning journeys and encouraging wandering off the usual path if directions given by the Google API could be enhanced by checking what points of interest (POIs) appear along the route. What it does The app uses Google Maps to allow users to tap on a destination they wish to walk to. The app then uses the Google Directions API to generate a route that is visualised on the Google Map. Then the app checks for POIs along the route using the Geoapify API. The resulting POIs are then displayed on the Google Map and in AR using the Google Geospatial API. How we built it The app is built using Unity, the Google Geospatial and Directions API, Google Maps, and using Geoapify to check for POIs. I chose Geoapify due to the granularity of the types of places you could search for. Challenges we ran into One of the main challenges I faced was that occasionally the Directions API would return a strange polyline to display the whole route on Google Maps. However I solved this by visualising the polyline of each step rather than relying on the whole route one supplied by the Directions API. Accomplishments that we're proud of Having tested this out all across the city I found it useful despite its simplicity. What's next for Geospatial Route Check This app only contains 6 POI types to highlight along a route as a proof of concept. The next stage of development would be to expand the POI types to cover most of the categories available on the API. <div