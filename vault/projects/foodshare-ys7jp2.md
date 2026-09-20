---
slug: "foodshare-ys7jp2"
url: "https://devpost.com/software/foodshare-ys7jp2"
title: "FoodShare"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 348
team_size: 0
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# FoodShare

> Share your Food, Share your Love.

[Devpost](https://devpost.com/software/foodshare-ys7jp2) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** css, express.js, firebase, firestore, html, javascript, map, ml, node.js, qr, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for foodshare

## Body

Inspiration Food wastage and hunger coexist in the same cities. While restaurants, hostels, and households discard surplus food daily, many communities struggle with access to meals. Existing donation platforms lack verification, coordination, and accountability, leading to fake listings, missed pickups, and misuse. FoodShare was inspired by the need for a trusted, real-time, and structured food redistribution system that connects donors, volunteers, and NGOs transparently and securely. What it does Verifies all users through SMS & email authentication. Provides role-based dashboards (Donor, Volunteer, NGO, Admin). Allows donors to post surplus food with history tracking. Enables volunteers to view donation requests via map access. Offers live location tracking after pickup acceptance. Uses QR-based delivery confirmation to verify handovers. Allows NGOs to create structured donation drives. Tracks user activity history for accountability. Rewards verified contributions through a points system. Uses a simple ML model to predict food demand based on past time and location data. How I built it FoodShare was built using a structured full-stack architecture: Role-based authentication with SMS and email verification. Built state-based workflow (Posted → Accepted → Picked → Verified). Integrated map-based location system with controlled coordinate visibility. Implemented live tracking after pickup acceptance. Generated unique QR codes for secure delivery verification. Built NGO-led structured donation drive module. A machine learning model trained on historical time-location data to predict demand. The backend manages authentication, role permissions, donation posts, drive creation, and activity tracking, while the frontend ensures smooth real-time interaction between all participants. Challenges I ran into Designing secure role-based access control. Preventing fake users and misuse of donation locations. Implementing controlled map visibility logic. Ensuring food cannot be falsely marked as delivered. Building real-time coordination without data conflicts. Designing strict role-based route protection. What I learned Designing secure authentication and role-based systems. Structuring real-time cloud databases using Firestore. Managing map-based coordination workflows. Preventing data misuse through permission control. Integrating ML logic into a practical social application. Building scalable architecture for multi-user systems What's next for FoodShare AI-based automatic matching between donors and nearby volunteers Brand CSR partnerships with reward-based coupon Multi-city expansion with regional drives <div