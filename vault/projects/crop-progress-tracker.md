---
slug: "crop-progress-tracker"
url: "https://devpost.com/software/crop-progress-tracker"
title: "Crop Progress Tracker"
hackathon: "Google Maps Platform Hackathon"
organization: "Google"
winner: true
words: 437
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Crop Progress Tracker

> This is a 3d visualization of the USDA's crop progress dataset for the 2021 corn growing season. Explore the map as corn crops progress through the weeks across the US!

[Devpost](https://devpost.com/software/crop-progress-tracker) · hackathon [[Google Maps Platform Hackathon]]

## Facets

**domain** [[agriculture_food]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** deck.gl, google-app-engine, google-earth-engine, google-maps, svelte, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for crop progress tracker

## Body

Inspiration Agriculture is one of OCI's strongest research domains, and as we grow our geospatial capabilities, we are looking for more sophisticated ways to show off our analytics results and visualize solution data to customers. During one of our projects, we found the USDA's crop progress data to be highly relevant to our domain, and whose temporal aspect offered itself up nicely for a time-based visualization. What it does This app visualizes the USDA crop progress dataset in a 3D-rendered mesh in weekly time steps throughout the 2021 corn growing season. Environmental context is given in the form of Elevation (meters), Latitude, Longitude, and State boundaries. The visualization can either play automatically with an animation, or can be cycled through manually by the user. How we built it We used Svelte typescript framework in Node JS to build the functionality and design of the website, Google AppEngine to deploy the website, and Google Earth Engine to style and generate map tiles of the USDA crop data. The Deck.GL library was used to create the 3D mesh ( TerrainLayer ) and state boundary ( GeoJsonLayer ) overlays, which were hosted inside the Google Maps API Maps object. Separate map tiles were produced for the elevation and texture for the 3D mesh. The Google Maps Elevation API is called every time the map moves and updates the elevation ticker with new data. Challenges we ran into Generating all the map tiles took a while in Earth Engine, so we had to figure out how to effectively test small units of data before generating the full set. Processing the Earth Engine data into a format that was faithfully displayed in the final map was also difficult. Accomplishments that we're proud of We are proud of achieving the design idea we had from the outset and learning so much about web-gl based interactive web mapping. What we learned Google Earth Engine is a convenient map tiling service, and we will likely use it in future projects. Also, we learned a lot about web image rendering, and how precise color mapping is needed to relate raster values to a final rendered output. What's next for Crop Progress Tracker We would like to add the full USDA Crop Progress and Condition dataset to visualize progress and condition layers for not only corn, but also for wheat, soy, and cotton for the years 2015-2022. We would also like to add a reverse geocoding feature that updates county and state along with elevation in the right-hand context panel. Furthermore, adding a flyover animation and smooth transitions would bring some more immersion into the application. <div