---
slug: "fire-tracker-d9uokc"
url: "https://devpost.com/software/fire-tracker-d9uokc"
title: "Anchor"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 464
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Anchor

> What Anchor does essentially is we aim to create an app which alerts users of emergencies in their area, but also to explain why taking action is necessary to the user and assist them in taking action

[Devpost](https://devpost.com/software/fire-tracker-d9uokc) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[disaster_emergency]]
**user** [[developer]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** australian-bureau-of-meteorology, claude, css3, expo.io, html5, javascript, jsx, nasa-firms, node.js, openai, openweathermap, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for anchor

## Body

Inspiration The main insipration for this app came to one of our members before UNIHACK last year as his house was burnt down due to the forces of nature with family members having trauma due to the situation. This lit a spark in our group making us think about what we could do to keep others from experiencing the same thing as one of our members. What it does So we decided to create Anchor, the reason for its name is the feeling of being grounded and safe. Anchor is an emergency alert system which warns users of nature disasters which could cause them harm, producing personalised messages specific to users locations and generating evacuation plans for them, and telling them why they are at risk to the situation. How we built it The entire project is built with JavaScript — React Native and Expo for the mobile app which runs on iOS, Android, and web from a single codebase, and plain HTML and CSS for the website, demo, and pitch animation. External APIs include NASA FIRMS for satellite fire data, OpenWeatherMap for weather alerts, and OpenAI GPT-4o which powers the personalised WHY explanations that make Anchor different from every other emergency app. Challenges we ran into The biggest challenges were getting Expo's SDK version to play nicely with Expo Go on the phone, managing dependency conflicts between packages, and figuring out how to take raw satellite and weather data from multiple sources and turn it into something a person under stress at midnight can actually read and act on — which is ultimately what the whole risk engine and AI layer exists to solve. So we ended up scrapping the whole mobile demo on the phone altogether and created a mobile demo run from the computer. Accomplishments that we're proud of We are proud of our ability to deliver a prototype of our Anchor (AlertAU for now) app within 48 hours as well as creating a pitch for our product in the same timeframe, being first years we take losts of pride in attending our first ever hackathon. What we learned We learnt many things about DevOps as well as deployment of our application on web. Through working in a team, we learnt and expanded upon our collaborative skills, preparing us for the corporate world where we need to develop and deploy a solution in a team, and the though time frames which software developers work under. What's next for Anchor We plan to expand our regions from not just state but also internationally such as in the EU or North America. We also would want to implement the evacuation routes using pathfinding algorithms so that users can view optimal evacuation paths in real time based on their current location and hazards. <div