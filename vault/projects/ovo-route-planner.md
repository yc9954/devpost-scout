---
slug: "ovo-route-planner"
url: "https://devpost.com/software/ovo-route-planner"
title: "OVO Route Planner"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 698
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# OVO Route Planner

> The OVO Route Planner uses the Google Route Optimization API to automatically plan routes for same and next-day deliveries across Switzerland.

[Devpost](https://devpost.com/software/ovo-route-planner) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** geocoding-api, gmpro, navigation-sdk, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ovo route planner

## Body

Inspiration Easy to park and inexpensive to operate, cargo bikes are an increasingly popular option for logistics companies looking for a carbon free alternative to traditional delivery vans. In this project, we partnered with OVO , a leading urban logistics provider in Switzerland, to develop an automated route planner that efficiently schedules same-day and next-day deliveries by cargo bike. What it does Customer orders are retrieved from Airtable at scheduled intervals and sent to the planner, where they are optimized (with the Google Route Optimization API or GMPRO) at the designated cutoff time. OVO’s operations team can then view the planned routes and make adjustments as needed - such as rearranging stops or moving them between drivers using drag-and-drop. Once the operations team is satisfied with the route, they dispatch it to the driver app so that the driver can view the route on his phone. In-app turn by turn navigation is supplied by the Google Navigation SDK which allows the driver to stay in the OVO app and receive in-app notifications and route updates in real time. On successful delivery, the drops off the package and takes a photo proof of delivery (POD). The time of delivery, location and POD are saved on the backend. Admin staff can use this information to confirm that the package was delivered safely and resolve any disputes. How we built it The OVO Route Planner was built with a Node.js backend and a React frontend, following a clean separation of concerns by organizing the frontend and backend codebases into separate folders. On the backend, we used Express.js to handle HTTP requests and built out APIs that interface with both MongoDB and PostgreSQL for storing and retrieving customer and operational data. The backend is also responsible for sending customer addresses and vehicle details to GMPRO (Google Maps Platform Route Optimization) and handling route updates in real time. On the frontend, we used Vite as our build tool for fast development and optimized bundling, while React powers the user interface. All key components - including the map, drag-and-drop Gantt chart, and other interactive UI elements - are built in React. The frontend communicates with the backend through API calls, enabling features like live route updates to be displayed dynamically without reloading the page. This architecture provides a responsive, efficient user experience for OVO’s operations team. Challenges we ran into One of the biggest challenges we encountered was updating route ETAs in a cost-efficient manner. Initially, every time a driver completed a stop, we reoptimized the remaining route using GMPRO. While this ensured high accuracy, the frequent API calls quickly became cost-prohibitive. To address this, we implemented new business logic that required drivers to complete their stops in the order presented. Instead of reoptimizing the route after each stop, we adjusted the ETAs of the remaining stops by calculating the time difference between the scheduled ETA and the actual completion time. For example, if a driver was scheduled to complete a stop at 08:00 but actually completed it at 08:30, we would add that 30-minute delay to the ETAs of all subsequent stops. This allowed us to maintain reasonably accurate timing while significantly cutting down on GMPRO usage. Accomplishments that we're proud of For OVO, route optimization isn’t just about improving efficiency or reducing costs - it also plays a key role in achieving their environmental sustainability goals. By calculating the most efficient paths for delivery vehicles, route optimization minimizes unnecessary mileage, which is very important because their cargo bikes are electric and have limited range. What we learned Elevation has a significant impact on battery usage for e-bikes, especially larger cargo bikes. Climbing steep hills isn’t practical and can quickly drain the battery. To address this, we plan to enhance GMPRO-generated routes with topographic data of the urban areas where OVO operates, helping us avoid routes with major elevation gains. We’ll achieve this by applying penalties to route segments between stops that involve steep uphill climbs, effectively guiding the planner to prefer flatter, more energy-efficient paths. What's next for OVO Route Planner Afi Labs will be working with OVO in the coming months to expand their operations across Switzerland and the EU. <div