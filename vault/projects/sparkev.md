---
slug: "sparkev"
url: "https://devpost.com/software/sparkev"
title: "SparkEv"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 278
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# SparkEv

> Plan Ev trips Worldwide

[Devpost](https://devpost.com/software/sparkev) · hackathon [[Atlas Madness]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**substrate** [[geospatial]] [[structured_db]]

**stack** flutter, google-bigquery, google-maps, mongodb, realm

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i am proud of
- what's next for sparkev

## Body

figma design architechture Inspiration As the world pivots to green energy some parts of the world have low infrastructure to support the shift. This is laid bare in industries such as the electric automotive industry where developing countries have the most need but the least resources. Some countries have a dozen charging stations compared to thousands in developed countries. What it does The project aims to boost the adoption of Electric vehicle technology by allowing users to plan trips from a starting point, a charging point, and a finish point across any country and get the feedback on distance, duration, and cost of the trip. How I built it The project is a flutter app compiled for Android. The realm package is used for local storage and authentication and synced with MongoDB atlas services on a GCP cluster. GCP SDKs for maps, reverse geocoding, and routes are used to display maps, markers, polylines and the country of the middle marker. A dataset containing the Kilowatt price of electricity per country is loaded into big query and analyzed using SQL. When a user plans a trip, a query is processed by big query and returns the price of a kWh for the specified country. A method is executed to show the duration, time, and cost of the trip. Challenges we ran into Doing research to get the dataset for each country was tough. The dataset is actually from 2021 so yeah. I am hoping to get a better dataset for future updates. Accomplishments that I am proud of Learning all the technologies and implementing them successfully. What's next for SparkEv The sky is the limit : ) Cheers <div