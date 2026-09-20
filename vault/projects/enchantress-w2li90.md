---
slug: "enchantress-w2li90"
url: "https://devpost.com/software/enchantress-w2li90"
title: "Enchantress"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 633
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/supply_logistics"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Enchantress

> The Potion Flow Monitoring Map

[Devpost](https://devpost.com/software/enchantress-w2li90) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[supply_logistics]]
**substrate** [[geospatial]] [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** css, html, javascript, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for enchantress

## Body

Discrepancy Detection Potion Network Map Inspiration Our inspiration for Enchantress came from the real-world challenges of monitoring distributed systems — like supply chains, fluid networks, and IoT sensor systems — where tracking resource flow and detecting inconsistencies in real time is critical. We wanted to reimagine that problem in a magical setting, transforming concepts like data synchronization, anomaly detection, and predictive scheduling into a fantasy world of potions and witches. What it does Our tool opens to a dynamic map displaying 12 cauldrons, each brewing potions at varying fill and drain rates, with witches randomly collecting their contents. By clicking on any cauldron, users can view live updates of potion levels — shown minute-by-minute over the course of a week — through an interactive time series graph. The dashboard also highlights the starting and ending potion volumes for each cauldron across the week. To ensure potion accountability, we implement discrepancy detection that compares Potion Transport Tickets (which record witch collections) with the actual drained volumes. If a ticket reports more or less than what truly left the cauldron — or if unlogged draining occurs — our system automatically flags it. A separate dashboard page provides a detailed view of these discrepancies, showing each cauldron’s state throughout the week. Cauldrons with inconsistencies are distinctly marked, allowing users to inspect and understand the exact nature of each discrepancy. We also integrated forecasting and route optimization logic that predicts when cauldrons might overflow and suggests efficient pickup schedules for witches. How we built it Frontend: React, TypeScript, CSS Backend: TypeScript Challenges we ran into Creating an algorithm to determine discrepancies was a major challenge. There were multiple factors to account for: each cauldron has a unique fill and drain rate, potion continues to accumulate during draining, and transport tickets only provide end-of-day totals without timestamps. Matching these tickets to actual drain events required careful handling of continuous flows and partial drains, as well as building a system that could adapt to changing data. In addition, displaying these discrepancies in a clear and user-friendly way was another challenge. Accomplishments that we're proud of Design and User Experience: We’re proud of creating an interactive, gamified dashboard that brings data to life. The animated map view, clickable cauldrons, and real-time potion graphs make complex information visually intuitive and fun to explore. Real-world Relevance: Our solution models real-world challenges found in supply chains, fluid networks, and IoT sensor systems. It was exciting to tie this creative topic to a real-world issue such as oil tracking, where discrepancies in transport and flow measurement are major challenges. It promotes a new way of thinking—merging magical creativity with real-world problem solving. Data Analysis and Discrepancy Detection: We’re proud of building logic that identifies when potion transport tickets don’t align with actual drain events. The system highlights suspicious activity, flags potential missing data, and provides visual explanations of where and why inconsistencies occur. What we learned Through this project, we gained hands-on experience in real-time data monitoring, anomaly detection, and dynamic visualization. We learned how to handle continuous flows and match incomplete or delayed data (like transport tickets) to actual events, a challenge that mirrors real-world supply chain and IoT problems. We improved our skills in frontend-backend integration, state management, and interactive graphing. We also learned how to merge storytelling and gamification with functional analytics to make complex data engaging. What's next for Enchantress For predictive analytics, we would use machine learning regression models to forecast potion levels in each cauldron based on historical data, fill/drain rates, and past drain events. Models like Random Forest could predict when a cauldron might overflow, so witches know when to collect potions before they overflow. For optimized courier scheduling, we would combine these forecasts with graph-based route optimization, considering travel paths, cauldron capacities, and unloading times. <div