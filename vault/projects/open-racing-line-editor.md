---
slug: "open-racing-line-editor"
url: "https://devpost.com/software/open-racing-line-editor"
title: "Open Racing Line Editor"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 458
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Open Racing Line Editor

> The first 3D racing line visualization tool on the web, transforming motorsport training through immersive Google Maps-powered track tours.

[Devpost](https://devpost.com/software/open-racing-line-editor) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** fabric.js, firebase, gatsby, google-maps, javascript, react

## How they structured the write-up

- inspiration
- what i built
- how i built it
- challenges i faced
- what i learned
- what's next

## Body

3D Racing Line Racing Line Editor Inspiration Traditional racing analysis tools are limited to flat, static 2D views that make it difficult for drivers to understand optimal racing lines before track sessions. As a racing enthusiast, I always struggled to visualize the perfect line through corners when studying track layouts on paper or basic apps. When I saw Google's photorealistic 3D Maps running smoothly in the browser, I realized this technology could revolutionize how racers prepare for and analyze their performance. The idea of being able to "fly" through a racing line in 3D, seeing elevation changes and track features from a driver's perspective, was incredibly exciting. What I Built The Open Racer Racing Line Editor is the first 3D racing line visualization tool on the web. It allows racers to: Draw racing lines on over 1700 go-kart tracks and hundreds of racing circuits worldwide Import iRacing telemetry data with high-frequency precision (700+ data points per second) Experience cinematic track tours with smooth camera movement following racing lines Navigate instantly between corners with intelligent detection algorithms How I Built It The project is built on Google Maps Platform as its foundation: Google Maps JavaScript API provides high-resolution satellite imagery with custom racing-focused styling Google Maps 3D API enables WebGL-based terrain visualization with smooth, cinematic camera movements React/Gatsby powers the modern web interface with real-time capabilities Firebase handles authentication, real-time data synchronization, and community features Fabric.js manages the interactive drawing tools for creating racing lines Challenges I Faced Interactive Drawing Editor Creating an intuitive racing line editor was the biggest challenge. Integrating Fabric.js for smooth drawing interactions while maintaining performance required extensive optimization. Zoom and Pan Performance Handling zooming and panning smoothly across different track scales was technically demanding. Racing circuits vary dramatically in size - from small go-kart tracks to massive circuits like the Nürburgring. The editor needed to maintain drawing precision and performance across all zoom levels. Mobile Browser Optimization Making the editor responsive and quick on mobile browsers required significant optimization work. Touch interactions for drawing racing lines, gesture handling for zooming/panning, and maintaining 3D performance on mobile devices presented unique challenges. What I Learned This project taught me about: 3D map component lifecycles and the complexities of WebGL-based terrain rendering Motorsport telemetry data processing and the specific technical needs of racing communities Performance optimization for interactive drawing tools across different devices and browsers Community building around niche technical interests like racing line analysis What's Next I'm excited to expand the platform with: Additional telemetry format support for more racing simulators and data loggers Advanced analytics showing speed traces, G-forces, and other performance metrics in 3D space The goal is to make Open Racer the definitive platform for racing line analysis and motorsport training worldwide. <div