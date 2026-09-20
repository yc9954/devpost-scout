---
slug: "theteamwithnoname"
url: "https://devpost.com/software/theteamwithnoname"
title: "team-bratwurst"
hackathon: "Tableau Next Virtual Hackathon"
organization: "Tableau"
winner: true
words: 269
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/supply_logistics"
  - "domain/transportation"
---

# team-bratwurst

> Next Level Tableau Nexting

[Devpost](https://devpost.com/software/theteamwithnoname) · hackathon [[Tableau Next Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[supply_logistics]] [[transportation]]

**stack** google, python, raspberry-pi, salesforce, snowflake, tableau, tableau-next

## How they structured the write-up

- inspiration
- what it does
- whats next

## Body

Overview Overview Chart in App Page Tableau Next in Action Open Information Section Workspace Inspiration The core inspiration for this project was to bridge the gap between sustainable energy generation and sustainable consumption. We have a balcony solar power plant generating clean energy and an electric vehicle that needs charging. The key question was: "Can I use the sun from today to power my commute for tomorrow?" We wanted to move beyond simple historical tracking and create a predictive tool that provides actionable insights, optimizes our use of self-generated power, and ultimately reduces our reliance on the grid. What it does The Solar Drive Forecaster is a complete, end-to-end data pipeline and analytics solution. In its final form, it: Collects live data every 15 minutes from a local solar inverter, capturing real-time power generation. Fetches hyper-local weather forecasts (GHI, DNI, DHI, Cloud Cover) for the next 48 hours from the Open-Meteo API. Calculates a precise power forecast in Watts, using the pvlib library to model the expected output on our specifically tilted and oriented solar panels, while respecting the 800-watt limit of the inverter. Stores and processes all data in a robust Snowflake data warehouse, creating clean, analysis-ready views that seamlessly blend historical live data with the latest forecast. Feeds a daily-updated Google Sheet which serves as a data source for a public-facing Tableau dashboard, visualizing the expected energy yield for today and tomorrow. Ultimately, it answers one simple question: "Based on today's sun, how many kilometers can I charge into my EV to cover the required driving distance for tomorrow?" Whats next See you at the Dreamforce <div