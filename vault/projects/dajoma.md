---
slug: "dajoma"
url: "https://devpost.com/software/dajoma"
title: "MeteoWatch"
hackathon: "Microsoft Fabric and AI Learning Hackathon"
organization: "Microsoft"
winner: true
words: 713
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/transportation"
  - "substrate/geospatial"
---

# MeteoWatch

> MeteoWatch is a real-time intelligence solution designed to monitor flights for potential weather hazards.

[Devpost](https://devpost.com/software/dajoma) · hackathon [[Microsoft Fabric and AI Learning Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[transportation]]
**substrate** [[geospatial]]

**stack** eventhouse, eventstream, fabric, kql, notebook, openai, pipeline, powerbi, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for meteowatch

## Body

Inspiration We brainstormed around use cases solvable with open data that we could tackle using real-time intelligence technologies, as none of us had experience with it and were eager to try it using Microsoft Fabric. We all work at Deutsche Bahn, but unfortunately, there isn’t much open railway data available. However, there is actually a lot of open aviation data! So, we began with the question, "What can you do with OpenSky Network data?" Then we discovered open data on weather hazards through OpenAviation, as well as route and vehicle reference data on ADSDB. We reached out to ADSDB and were granted permission to use their data for the hackathon. Then we put it all together: Why not build a monitoring and alerting system based on Fabric Eventhouse and use Azure OpenAI to customize alert messages? What it does The system consumes data from OpenSky Network, ADSDB, and AviationWeather. Using this data, MeteoWatch knows the current position of aircraft and their flight routes. The system is also aware of areas where weather hazards, known as SIGMETs (Significant Meteorological Information), are reported. MeteoWatch calculates whether a flight will be affected by a SIGMET and creates a natural language warning message, which could be tailored and sent to a specific aircraft. Additionally, MeteoWatch includes a dashboard where stakeholders such as air control or pilots can view the flight route, relevant weather hazards, and other useful information. How we built it The ingestion is handled with notebooks, and all data is accessed via web APIs. We send the data to EventStream to ingest it into an Eventhouse. Essentially, we built a real-time intelligence medallion architecture. We use update policies to perform basic transformations and cleanup from the bronze to the silver layer. On top of the silver layer, we use materialized views to create geometries in different formats, calculate intersections, track alerts, aggregate the latest information, and so on. We then use a notebook to send alerts to the Azure OpenAI API to generate more meaningful warning messages. These are sent to EventStream, and from there to Reflex, where alerting via email, Teams messages, etc., can be configured. Additionally, we built a dashboard on top of the gold layer, displaying all geometries (positions, trajectories, hazards) and other useful information. Challenges we ran into We encountered issues calling web APIs from Eventhouse using KQL. Although it provides some functionality in this regard, it wasn’t sufficient for our ingestion needs, so we opted to use notebooks instead, which we probably wouldn’t do in a real-life scenario. We also faced limitations with access to OpenAI models. We would have loved to experiment with text-to-speech to broadcast messages to aircraft, but this model wasn’t available in the hackathon environment. The rate limit also posed challenges in real-time scenarios, as the system couldn’t process all alerts in time under these constraints. We also used onmicrosoft accounts based on a personal Azure environment, so we didn’t have access to Teams and Outlook, which prevented us from testing alerting through those channels. Unfortunately, Copilots weren’t available in our Fabric trial environment, although we would have liked to use them. Finally, since we are not domain experts in aviation, there was an additional challenge in understanding and applying the domain knowledge required. Accomplishments that we're proud of We are proud that we managed to build such a complex system in our limited free time! What we learned Although we all have experience in big data, this was our first time building a complex system focused on real-time intelligence. We learned a lot about KQL and real-time processing. Furthermore, we learned about geospatial analysis, formats like GeoJSON and WKT, and how to use generative AI in a data solution. It was also exciting to explore the domain of aviation. What's next for MeteoWatch We plan to use this project for upcoming hackathons. For example, we have a private hackathon at Deutsche Bahn where we’ll use MeteoWatch to demonstrate the potential capabilities and benefits of Microsoft Fabric to our colleagues. In the future, we may experiment with text-to-speech for alert messages and develop a RAG architecture to enable an agent to provide tailored answers to questions about flight routes and weather hazards. If we find more time, we’ll also fix bugs and improve the dashboard! <div