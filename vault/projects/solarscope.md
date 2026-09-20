---
slug: "solarscope"
url: "https://devpost.com/software/solarscope"
title: "SolarScope"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 475
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# SolarScope

> Design Solar Smarter — From Satellite to System in Minutes. AI-powered solar design: analyze rooftops remotely, generate reports, and optimize systems—no site visit needed.

[Devpost](https://devpost.com/software/solarscope) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]

**stack** boltai, google-maps, google-solar, netlify, react, superbase, tailwindcss, typescript

## How they structured the write-up

- what's next for solarscope
- inspiration
- what it does
- how we built it
- what we learned
- challenges we ran into
- accomplishments we're proud of

## Body

homepage auto design manual design What's next for SolarScope Inspiration We got a solar installation project in Germany, which required us to travel there multiple times during the planning phase. We also had to rent a drone to survey the high rooftop — capturing roof segments and checking for shading from trees and nearby buildings. That got us thinking: Isn't there a way to plan installations without all this hassle? That question inspired us to build SolarScope . What It Does Enter a property address and get real-time modeling of a solar installation on the roof. SolarScope automatically: Measures the roof dimensions Calculates the maximum number of solar panels the roof can accommodate Generates the optimal system installation size Estimates the annual energy generation capacity Recommends ideal panel placement for maximum sunlight exposure, highest efficiency, and minimal shading Allows users to modify the number of panels and panel wattage to match specific energy requirements How We Built It I built SolarScope from start to finish using: Bolt.dev for the fullstack development Supabase for the backend Google API for location data and modeling GitHub for version control What We Learned I learned how to use Bolt.dev to build a fullstack application from scratch. I also learned how to interact with Bolt AI to: Add new features Modify existing ones Make improvements without breaking the codebase Challenges We Ran Into Prompt Accuracy: One of the major challenges was issuing the correct prompt so that Bolt AI would deliver the exact feature we needed. Token Limits: As the project codebase grew, token consumption per prompt increased. I eventually started running out of tokens, so I began fixing minor issues manually instead of issuing new prompts. Accomplishments We're Proud Of With auto design - Solar installers can now remotely analyze any property for solar installation using real-world data (currently available in Europe and North America). With Manual design - The tool can model shading patterns, sunlight direction, solar irradiance, and annual solar generation for any location. Accomplishments We're Proud Of Auto Design: Enables solar installers to remotely analyze any property's rooftop for solar installation using real-world geographic and structural data — currently available across Europe and North America. It automatically handles panel placement , estimates the system installation size , and predicts annual energy generation capacity based on rooftop conditions. Manual Design: Think of it as a digital sandbox for solar engineers — the tool allows manual fine-tuning to model shading patterns , sunlight direction , solar irradiance , and panel layout . Users can also calculate installation size and estimate annual generation capacity , giving them precise control over every aspect of the solar planning process for any location. What's Next for SolarScope We’re preparing for a public launch , and we aim to connect with more customers and investors to bring SolarScope to a wider audience. <div