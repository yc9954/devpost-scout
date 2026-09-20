---
slug: "project-quench"
url: "https://devpost.com/software/project-quench"
title: "Project Quench"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 462
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/housing_homeless"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Project Quench

> Project Quench is a wildfire app showing real-time heatmaps and danger zones, guiding civilians to shelters safely and optimizing firetruck routes for faster, smarter firefighting during wildfires.

[Devpost](https://devpost.com/software/project-quench) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[housing_homeless]]
  <sub>weak: climate_energy</sub>
**user** [[general_public]]
**substrate** [[document_pdf]] [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** axios, css, express.js, google-cloud, html, javascript, nasa-firms, noaa-climate-data-online, node.js, papaparse, python, react, tensorflow, vite

## How they structured the write-up

- 🔥 inspiration
- 🌍 what it does
- 🛠️ how we built it
- 🌟 key features
- 🧗 challenges we faced
- 🏆 accomplishments
- 📚 what we learned
- 🚀 what’s next

## Body

🔥 Inspiration California wildfires have destroyed over 12,000 structures and forced 300,000 residents to evacuate. With over 58 square miles burned, our families have been directly affected. This inspired us to create a solution to mitigate the devastating impact of these wildfires. 🌍 What It Does Project Quench combines real-time heatmaps and danger zone visualizations to guide civilians to nearby shelters . It also simulates firetruck deployments to optimize routes for combating fires effectively. 🛠️ How We Built It Google Maps API Mapping, markers, and map overlays. javascript const map = new google.maps.Map(document.getElementById('map'), { center, zoom }); NASA FIRMS Fire data pulled from NASA FIRMS and rendered as heatmaps. javascript const heatmap = new google.maps.visualization.HeatmapLayer({ data, radius: 30 }); NOAA Weather Alerts Displays Red Flag Zones where Wildfire Alerts are active and spinning cat markers for the severity of each danger zone. javascript const marker = new google.maps.Marker({ position: centroid, icon: spinningCatGif }); GraphHopper API Calculates optimal fire-avoiding routes from your address to the nearest shelter. javascript const route = await fetchRouteAvoidingFires(origin, destination, avoidPolygons); TensorFlow.js Simulates firetruck deployment strategies using AI, from nearby firestations to large fires. Most effective when fires are mostly contained. javascript const model = tf.sequential(); model.add(tf.layers.dense({ units: 16, activation: 'relu' })); Nebius AI Powers "Burnie", our quirky wildfire safety chatbot. javascript const response = await nebiusClient.chat.completions.create({ messages: [...] }); 🌟 Key Features Interactive Toggles : Show/hide heatmaps, shelters, fire stations, and alerts. AI-Driven Firetruck Deployment : Optimized routing to extinguish fires, using neural networks to manage resources from nearby fire stations to efficiently put out fires Shelter Navigation : Find the route to your nearest evacuation shelter, avoiding the fires in the area. 🧗 Challenges We Faced API Integration : Merging multiple datasets seamlessly - compiling sources for all the data (Google Maps, NOAA, FIRMS, etc). Performance Optimization : Managing AI deployment models with large datasets without slowing down. Route Safety : Ensuring accuracy in dynamic danger zones - avoiding fires when travelling to shelters. 🏆 Accomplishments Successfully built an intuitive app that integrates real-time data with practical tools for civilians and emergency services. Developed a user-friendly chatbot for wildfire evacuation and preparation and optimized firetruck deployment algorithms. 📚 What We Learned How to merge various data sources into one cohesive system. The importance of user-centric design for critical situations. Optimization techniques for real-world constraints like dynamic fire zones. 🚀 What’s Next Predictive Fire Modeling : Map the potential spread of wildfires using AI, allowing accurate maps and routing suggestions. Advanced Evacuation Tools : Integrate detailed routes with live updates. Emergency Collaboration : Partner with agencies to improve responses - integrate data from more sources. Scalability : Expand the app to wildfire-prone regions globally, and even other disaster types. 🌟 Making wildfire mitigation smarter, faster, and safer! <div