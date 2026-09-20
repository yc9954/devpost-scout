---
slug: "nimbus-pulfzh"
url: "https://devpost.com/software/nimbus-pulfzh"
title: "Nimbus"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 403
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Nimbus

> Using Google Maps to plan mission routes for autonomous hovercrafts that deliver medical supplies.

[Devpost](https://devpost.com/software/nimbus-pulfzh) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[health_clinical]] [[transportation]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** c++, css, html, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- the math (with latex)

## Body

Waypoint Route Planner Using the Google Maps API Hovercraft Front View Hovercraft Back View Nimbus — Amphibious Mission Planner An immersive mission planner for hovercraft and ground teams. Nimbus mixes direct (hover) legs over water/flat terrain with driving legs (Directions API), compares ETAs, shows nearby hospitals, overlays elevation + weather, and previews the route with a 3D flythrough. Inspiration In flood-prone and coastal areas, the fastest path isn’t always a road. During coastal events we saw responders juggling multiple apps to answer: “How fast can we get there, and where do we hand off to a hospital?” Nimbus turns that workflow into a single, map-first experience for amphibious missions . What it does Click-to-plan: Add waypoints by clicking the map or searching. Drag to reorder; right-click to delete. Hybrid routing: For each leg Nimbus chooses Driving (roads) or Direct (straight line for hovercraft) using a simple ratio test. Compare routes: One tap compares Driving vs Hybrid vs Direct ETAs. Destination support: Shows nearby hospitals (Places API). Context: Elevation sparkline (Elevation Service) + weather at destination (Open-Meteo). Immersion: 3D tilt/heading flythrough and an animated HUD during simulation. Share & save: Export/import mission JSON and share links that encode waypoints + mode. How we built it Frontend: HTML/CSS (Orbitron), vanilla JavaScript. Google Maps Platform: Maps JavaScript, Directions, Places, Elevation, Geometry libraries. Data/Viz: Open-Meteo for live weather; Chart.js for the elevation sparkline. UX choices: Fixed sidebar (only Waypoints list scrolls), color-coding ( white = driving , cyan = direct ), compact action bar, cinematic camera for briefings. The math (with LaTeX) We model ETA as a sum over legs, selecting the faster of road vs straight-line hover. Direct (hover) leg $$ t_{\text{hover}} \;=\; \frac{d_{\text{straight}}}{v_{\text{hover}}}, \qquad v_{\text{hover}} = 45~\text{km/h}\; \text{(configurable)} $$ Driving leg (from Directions API) $$ t_{\text{drive}} \;=\; \frac{d_{\text{road}}}{v_{\text{drive}}^\ast} $$ where ( t_{\text{drive}} ) comes directly from the API’s time estimate (traffic-aware where available). Leg selection heuristic $$ \text{choose Direct if}\quad \frac{d_{\text{road}}}{d_{\text{straight}}} > \tau, \qquad \tau = 1.25 $$ Total ETA $$ T = \sum_{i=1}^{N-1} \min\left( t_i^{d},\, t_i^{h} \right) $$ Pseudo-logic const THRESH = 1.25; // road vs straight-line ratio for (let i = 0; i < waypoints.length - 1; i++) { const A = waypoints[i], B = waypoints[i + 1]; const straight = distance(A, B); // Geometry lib const road = directionsDistance(A, B); // Directions API if (road > straight * THRESH) useDirect(A, B) // hover segment else useDriving(A, B) // road segment } <div