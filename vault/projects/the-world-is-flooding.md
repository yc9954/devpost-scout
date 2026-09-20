---
slug: "the-world-is-flooding"
url: "https://devpost.com/software/the-world-is-flooding"
title: "The World is Flooding!"
hackathon: "Google’s Immersive Geospatial Challenge"
organization: "Google"
winner: true
words: 447
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# The World is Flooding!

> The World is Flooding! Visualize a realistic flooding view of your neighbourhood.

[Devpost](https://devpost.com/software/the-world-is-flooding) · hackathon [[Google-s Immersive Geospatial Challenge]]

## Facets

**mechanism** [[benchmark_measured]] [[sensor_fusion]]
**domain** [[climate_energy]] [[disaster_emergency]]
  <sub>weak: finance_payments</sub>
**user** [[general_public]]
**substrate** [[geospatial]] [[video_visual]]

**stack** cesium, geojson, google

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the world is flooding!

## Body

Charleston South Carolina Flooding - 2015 2040 Flood Prediction data visualized in 3d via Cesium JS and Google Maps 3d Tiles Charleston South Carolina Flooding - 2015 - AOI Charleston South Carolina Flooding - AOI via Cesium 2060 Flood Prediction data visualized in 3d via Cesium JS and Google Maps 3d Tiles 2d Flood Mapping for Charleston South Carolina Google 45 imagery for reference Google 45 imagery for reference Precipitation Change Mapping by 2100 - World Bank Inspiration According to a recent study, the percentage of the global population at risk from flooding has risen by almost a quarter since the year 2000. By 2030, millions more will experience increased flooding due to climate and demographic change. What if we had a way to visualize the potential impacts of flooding in a hands on easy to visualize medium? What it does This app presents a paradigm shift when it comes to flood mapping visualization. Traditionally, flood maps are 2d paper maps that show areas that may be covered by water or show where the water reaches during a specific flood event. Displaying this flood data in a realistic virtual 3d world provides a way to actually see how deep the water will be in certain areas. Seeing the water level in 3d against recognizable object such as your front stairs, or you car provides a comprehensible realistic picture of the event. How we built it Open data depicting the predicted levels of sea level rise was developed and provided by NOAA Coastal Services Center in Charleston, SC using 2007 and 2009 LiDAR data for Berkeley, Charleston and Dorchester counties. This data was imported and rendered alongside the Google Maps Photorealistic 3D Tiles using the Cesium JS platform. Challenges we ran into Lack of support for animations on entity based datasets in Cesium JS Large complex flood datasets render slowly Elevation projection of GIS based flood data needed some tweaking to correctly render against the Google Maps Tile terrain elevation. Accomplishments that we're proud of Being able to incorporate visual effects such as animated rainfall and cloud cover enhances the user experience for this app. Having real world Coast Guard helicopter based imagery of a recent flood event provided an excellend benchmark from which to compare the realism and accuracy of the Google Maps Photorealistc Tiles. What we learned Using the Google Maps Photorealistc Tiles as a basemap in an interactive 3d medium is an excellent method for engaging the public when it comes to visualizing flood events. What's next for The World is Flooding! Expanding the usability of the app by providing a way for jurisdictions to upload their own flood modelling data for quick visualization. <div