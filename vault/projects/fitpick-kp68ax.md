---
slug: "fitpick-kp68ax"
url: "https://devpost.com/software/fitpick-kp68ax"
title: "FitPick"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 388
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
---

# FitPick

> Discover top-rated fitness classes and instructors in your city with FitPick. Search by time, location, and category—save favorites and track your workouts, all in one mobile-friendly app.

[Devpost](https://devpost.com/software/fitpick-kp68ax) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[geospatial]]

**stack** bolt.new

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fitpick

## Body

Inspiration We noticed how hard it is to find reliable, well-rated workout classes and instructors in a new city or even within your own neighborhood. While booking platforms exist, there's a gap in discovery-focused tools that prioritize user experience, ratings, and convenience. FitPick fills that gap—combining the best of Yelp and ClassPass into a simple, mobile-friendly discovery platform. What it does FitPick allows users to search for fitness classes and instructors based on city, day, and time range. Users can view ratings, read reviews, and explore instructors across all locations via a clean card-based layout and interactive map. It includes a favorites section where users can save their top studios and trainers, rate completed workouts, and revisit recently viewed classes—all in one sleek interface. How we built it We designed FitPick as a frontend-only web app using React and Leaflet. All interactions are handled through local state, and data persistence is managed with localStorage. The UI is mobile-first, styled with a light grey and beige palette, and features smooth transitions. We used mock data to simulate a real fitness ecosystem while keeping the code modular for future backend/API integration. Challenges we ran into One of the main challenges was creating a realistic map-based search without relying on APIs that require keys. Leaflet with OpenStreetMap solved this smoothly. Another challenge was simulating user behavior—like ratings, favoriting, and browsing history—without a backend. We had to carefully manage localStorage and component state to mimic real user flows. Accomplishments that we're proud of We're proud of how intuitive and polished the platform feels, even as a prototype. FitPick doesn’t just function—it gives users an experience that feels personal and efficient. The recently viewed system, category-based filters, and dynamic map integration came together seamlessly. What we learned We learned how much can be done with a thoughtful frontend architecture and a strong focus on user experience. From localStorage management to responsive layout design, every feature required attention to detail to simulate a real platform without backend infrastructure. What's next for FitPick We plan to integrate real-time class booking systems and expand the platform to support instructor-side accounts. Eventually, users will be able to book spots directly through FitPick, and instructors will be able to manage listings and collect feedback. We’re also exploring AI-powered class suggestions and smarter filtering based on workout goals. <div