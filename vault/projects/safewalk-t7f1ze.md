---
slug: "safewalk-t7f1ze"
url: "https://devpost.com/software/safewalk-t7f1ze"
title: "SafeWalk"
hackathon: "AmpliCode Hackathon 2025"
organization: "AmpliCode"
winner: true
words: 405
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# SafeWalk

> SafeWalk: AI-powered route planner that finds the safest path to your destination using real-time crime data. Stay safe whether you're walking, cycling, or driving.

[Devpost](https://devpost.com/software/safewalk-t7f1ze) · hackathon [[AmpliCode Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]

**stack** axios, bun, css3, eslint, git, github, html5, javascript, json, leaflet.js, markdown, next.js, node.js, npm

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safewalk

## Body

Home Page 1 Home Page 2 Route Planning Input Route Planning Output 1 Route Planning Output 2 Inspiration SafeWalk was born from a personal experience of navigating through unfamiliar neighborhoods. We realized that while most navigation apps focus on speed and efficiency, they often overlook a crucial aspect: personal safety. This led us to create a solution that helps people make informed decisions about their travel routes by considering both efficiency and safety. What it does SafeWalk is an intelligent route planning application that: Integrates real-time crime data from NYC Open Data Provides both fastest and safest route options Supports multiple transportation modes (walking, cycling, driving) Visualizes crime density through interactive heatmaps Calculates route safety scores based on crime severity Saves and manages route history for future reference How we built it Frontend : React/Next.js with TypeScript for type safety Maps : OpenStreetMap with react-leaflet for interactive mapping Routing : OpenStreetMap routing API for path calculation Data : NYC Open Data API for crime statistics Styling : Tailwind CSS for modern, responsive design State Management : React hooks for efficient state handling Data Visualization : Custom heatmap implementation for crime density Challenges we ran into Data Integration : Combining crime data with routing algorithms while maintaining performance Route Optimization : Balancing safety scores with reasonable travel times Real-time Updates : Ensuring crime data stays current without overwhelming the API UI/UX : Creating an intuitive interface that presents complex safety data in an accessible way Performance : Managing large datasets and complex calculations without compromising user experience Accomplishments that we're proud of Successfully implemented a weighted scoring system for different types of crimes Created an intuitive interface that makes safety data accessible to all users Developed a responsive design that works seamlessly across devices Built a robust routing system that considers both safety and efficiency Implemented real-time crime data visualization through heatmaps What we learned Advanced data visualization techniques for crime mapping Complex routing algorithms and their optimization Best practices for handling large datasets in real-time Importance of user experience in safety-focused applications Effective ways to present complex data in an accessible format What's next for SafeWalk Expand crime data coverage to more cities Add real-time safety alerts and notifications Implement machine learning for better route predictions Add community reporting features for local safety updates Develop a mobile app for on-the-go safety navigation Integrate with public transportation systems Add accessibility features for different user needs <div