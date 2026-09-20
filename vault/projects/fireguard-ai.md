---
slug: "fireguard-ai"
url: "https://devpost.com/software/fireguard-ai"
title: "FireGuard AI"
hackathon: "FusionHacks 2"
organization: "FusionHacks"
winner: true
words: 252
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# FireGuard AI

> Preventing wildfires before they ignite through AI-powered prediction

[Devpost](https://devpost.com/software/fireguard-ai) · hackathon [[FusionHacks 2]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[disaster_emergency]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]

**stack** lucide, mapbox, nasa-firms, node.js, openweather, react, shadcn, tailwind, tensorflow.js, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we overcame
- achievements
- what we learned
- what's next

## Body

Home Dashboard Inspiration The horrific 2023 wild fire season that destroyed thousand of houses and lives. Current fire alarm systems only pick up on fires after they have started burning - what we really require is prevention, not reaction. What it does FireGuard AI predicts wildfire danger 72 hours ahead using machine learning and live data from NASA satellites, weather stations, and fire cameras sourced from thousands of locations. How we built it React frontend with real-time dashboard and interactive maps TensorFlow.js machine learning models trained on massive datasets Integrating with NASA FIRMS, weather APIs, and fire camera networks CORS proxy service for data aggregation from thousands of sources Mapbox for satellite imagery and showing fires Challenges we overcame CORS limitations when calling government APIs Training ML models in the browser with limited compute power Handling and normalizing thousands of disparate sources of data Creating realistic fire prediction algorithms Creating responsive maps which can handle real-time data updates Achievements 94% accuracy using neural network ensemble Real-time data aggregation from 8000+ sources Interactive live fire risks and predictions dashboard Browser-side end-to-end ML training pipeline Production-ready error-handling architecture What we learned Browser-based ML is full of surprises using TensorFlow.js Fire prediction is less about quantity, more about quality of data Sophisticated real-time applications have support from modern web APIs CORS proxies are required for government data integration What's next Add SMS/email alert system for fire departments Worldwide extend fire monitoring Work with fire departments for field testing Firefighter and emergency responder cell app <div