---
slug: "sauron-zvo2je"
url: "https://devpost.com/software/sauron-zvo2je"
title: "Sauron"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 780
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/general_public"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Sauron

> What if you could build a time machine to find who hurt you and your loved ones? We want to reduce the amount of cold cases by making police work 10x more efficient.

[Devpost](https://devpost.com/software/sauron-zvo2je) · hackathon [[Hack the North 2025]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[general_public]] [[researcher]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** apis, cohere, flask, geocode, gps, nextjs, react, reverse-engineering, supabase, wps

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sauron

## Body

Tracking the devices of the past Inspiration The clearance rate for violent crime is only about 50% in the US and Canada. Non-violent crime? Forget about it. Time and time again, ordinary citizens are told law enforcement doesn't have the resources to help them and their families. Could you imagine going through a tragedy without any closure? We set out on a mission to solve this problem, by making police investigative work 10x more efficient. What it does Sauron is a surveillance and investigation platform that functions like a temporal-spatial time machine, building a vast database of device movements over time. Its core features include: Trajectory Visualization: An interactive Mapbox interface displays the historical paths of thousands of devices, allowing an investigator to see where any device has been over any period of time. Crime Track: Intelligent path estimation using location data - crime committed at a specific location? See who was there, and where they went! AI-Powered Investigation: A natural language chatbot, powered by Cohere, allows users to ask complex questions like, "Who was near the bank at 43.47°N, -80.54°W between 2:00 PM and 2:15 PM? Where did they go?" How we built it Sauron is a full-stack application built with a modern, robust technology stack. The tech stack Backend : Python, Flask, PostgreSQL with PostGIS, Psycopg2 Frontend : Next.js 15 (with Turbopack), React 19, TypeScript, Mapbox GL JS, Tailwind CSS, shadcn/ui AI & Data : Cohere for the AI chatbot Infrastructure & DevOps : Supabase for the managed PostgreSQL database Challenges we ran into Making AI Actionable: Simply having a chatbot isn't enough. We needed it to interact with our specific dataset. The challenge was implementing Cohere's Tool Use feature effectively. This involved writing a precise tool definition, creating a Python function that could be called by the model, and ensuring the data passed between the LLM and our database was correctly formatted. Frontend Complexity: Building a highly interactive, map-centric application is non-trivial. We had to manage complex state between the map viewport, the search components, and the data filtering panels, ensuring a smooth and responsive user experience in a resizable layout (resizable-layout.tsx). Accomplishments that we're proud of Executing Real-World Device Tracking: Our proudest accomplishment is the successful execution of the live tracking phase. We built a system that could actively monitor and record the real-world movements of hundreds of devices simultaneously, generating a unique and powerful dataset for investigation. Creating a True AI Analyst: We successfully integrated a Cohere-powered LLM that goes beyond simple chat. By using Tool Use, our chatbot acts as an intelligent data analyst, allowing non-technical users to perform complex spatio-temporal queries using plain English. What we learned This project was a deep dive into the practical challenges of large-scale data engineering. Generating hundreds of thousands of location pings was just the first step; managing, querying, and visualizing that data proved to be a significant undertaking. We learned that with a massive spatio-temporal dataset, naive queries are unacceptably slow, making database performance paramount. This underscored the importance of proper database indexing, specifically with PostGIS's GIST indexes, and writing efficient SQL to query by both location and time simultaneously. We also encountered significant bottlenecks in transferring and rendering the data on the frontend. Sending hundreds of thousands of points to a web browser is not feasible, which taught us to design our backend API to be intelligent, performing the heavy lifting of filtering and aggregation on the server side. This ensures that the frontend only has to render data relevant to the user's view, preventing the map from freezing. Finally, we learned about the complexity of maintaining data integrity at scale. Ingesting data at high frequency requires atomic database transactions to prevent partial writes and robust error handling to deal with API failures without corrupting the dataset. Managing this volume of data taught us to think defensively about every step of the data pipeline. What's next for Sauron Moving forward, our primary focus is on enhancing the platform's accuracy and reliability. To increase the richness of our data, our next step is to integrate additional data sources, exploring implementations similar to Geospy to fuse location data from multiple providers and create a more comprehensive picture of device movements. We also plan to engage directly with potential customers in law enforcement and private investigative sectors to ensure our development aligns with their real-world needs and workflows. To make the platform more bulletproof against future changes to the undocumented APIs we rely on, we will build a dedicated iOS emulator. This controlled environment will allow us to safely analyze the API's behavior in-depth, ensuring our data ingestion process remains stable and reliable for the long term. <div