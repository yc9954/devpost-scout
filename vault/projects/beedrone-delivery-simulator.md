---
slug: "beedrone-delivery-simulator"
url: "https://devpost.com/software/beedrone-delivery-simulator"
title: "BeeDrone Delivery Simulator"
hackathon: "Google Maps Platform Hackathon"
organization: "Google"
winner: true
words: 536
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# BeeDrone Delivery Simulator

> Drone delivery is already here, with many startups and large enterprises invested in the area. This hack lets companies use Google maps to simulate scenarios and track their drone fleets in real time

[Devpost](https://devpost.com/software/beedrone-delivery-simulator) · hackathon [[Google Maps Platform Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[transportation]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** html5, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for beedrone delivery simulator

## Body

Inspiration Drone and other aerial-vehicle simulations are hard to build, since they require many complicated features including high definition maps, real-time telemetry and the ability to integrate with software and hardware simulations. With several startups and enterprises investing in drone delivery, a common simulation environment would be great to have and build on. Applications include drone delivery, rescue missions, local organ and blood transport as well as air taxi or Unmanned Aerial Mobility solutions. What it does The scene is setup in New York city, where a ground station (in the form of a space needle) houses several "bee" drones for on-demand deployment. The demo uses a custom vector map style and 3D models of drones to simulate a package pickup-and-delivery use case. Drones leave the ground station, pick up and deliver packages, and return to recharge when needed. The drones follow a kinematic model that lets them fly at a specific altitude above ground level, and orient themselves correctly when flying. The demo shows a floating dashboard above the map to keep track of the on-time delivery percentage (the aim is to be at 100%!) and the amount of demand for pickups and deliveries. For a live demo , please click - https://tinyurl.com/beedronemapdemo - after a minute you can try clicking the "spawn BeeDrone" button to spawn more bees for deliveries. http://ec2-50-19-44-139.compute-1.amazonaws.com/ points to the above url as a backup How we built it A custom map style was built using the no-code editor on the Google maps console, and then this was visualized through an app written in Node.js. Drones and objects like the space needle are of GLTF files that are placed according to the simulation parameters. Controls on the map and the floating dashboard were also added through HTML/JS. I also thought it would be fun to put a space needle ground station in the center of NYC ( this would never happen, I know! :) ) . PS: APIs used are google.maps.Map to initialize, google.maps.WebGLOverlayView for 3D overlays, google.maps.ControlPosition for controls and functions within map such as setOptions, . Also used DeckOverlay , SceneGraphOverlay , PathLayer from deck.gl, and Highcharts for live charting. Challenges we ran into One challenge was to track individual objects on demand using clicks (if you saw the demo, I am not sure how a user can click on a bee and track it from a third person view). That is something that drone companies can use to monitor their fleet in a more interactive way. Accomplishments that we're proud of Having never used the Google maps API, building this in a few days was a very rewarding experience. What we learned Read the docs and refer to examples how much it costs to run complicated apps through Google maps API (very less! My cost while developing the project was $1.14, and that was included as credits) How easy it is to customize maps, including what happens at various levels of zoom in the no code editor What's next for BeeDrone Delivery Simulator Open sourcing, followed by perhaps its own dedicated website and and easier way to set up and manage simulations and real-time drone fleet tracking. On the side, definitely more google maps hacking :D <div