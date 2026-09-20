---
slug: "tgrna-race-telemetry-and-driver-comparison-ai-analysis-1"
url: "https://devpost.com/software/tgrna-race-telemetry-and-driver-comparison-ai-analysis-1"
title: "Driver Training & Insights: Telemetry/Driver Comparison AI"
hackathon: "Hack the Track presented by Toyota GR"
organization: "Toyota Gazoo Racing"
winner: true
words: 471
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Driver Training & Insights: Telemetry/Driver Comparison AI

> Utilize VBOX data to provide AI augmented insights to a driver based on on a meter-by-meter assessment of brake pressure, throttle application, G-forces, steering angle, braking and more.

[Devpost](https://devpost.com/software/tgrna-race-telemetry-and-driver-comparison-ai-analysis-1) · hackathon [[Hack the Track presented by Toyota GR]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** postgressql, react, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tgrna race telemetry and driver comparison ai analysis

## Body

professional telemetry traces Driver and Race Selection lap coaching Inspiration Amateur race car drivers rely on their gut feel and the "seat of the pants" to. Pros use complicated telemetry systems such as Vbox, on a local computer on track and expensive coaches. We built a cloud-based system that gives amateur drivers professional-grade data analysis and AI coaching - accessible from any internet browser, at a fraction of the cost. What it does Cloud based Telemetry Analytics with an AI coach. Compare lap to all other drivers, meter-by-meter, lap by lap (or by race, or by season) Time delta analysis showing exactly where you gain or lose time against another driver. Works with dataset of VBOX data provided by TGRNA data at 23 Hz (1,380 samples/minute) Also ingested all other datasets for a wholistic view of the entire series. How we built it Tech Stack: React + TypeScript + Supabase (PostgreSQL) + AI Edge Functions Data Pipeline: Ingested 23.2M raw telemetry rows from Toyota GR Cup races Built TypeScript scripts to pivot CSV data from "long" (1 row per sensor) to "wide" format (1 row per timestamp) Stored 2.9M optimized records in PostgreSQL with smart indexing (reducing data without loss by 88%) Created interactive visualizations with Recharts and Leaflet maps Added AI analysis that understands racing context (corner names, track layouts, techniques) Challenges we ran into Inconsistent data: Only 2 of 7 tracks have GPS. Speed/distance sensors update 5x less frequently than throttle/brake (276 vs 1,380 samples/min) Scale: Processing multi gig CSV files - built streaming ingestion with batching to avoid browser crashes Missing data: Some cars had incomplete laps - added pre-flight data quality checks for user. Performance: Can't render 100,000+ data points smoothly - implemented smart sampling and progressive loading AI coaching: Made it racing-specific, not just a ChatGPT wrapper - injected track context and cached results Accomplishments that we're proud of Handled pro-level data: 23.2M rows → 2.9M optimized records, sub-second queries Matched $10K systems in the cloud Same capabilities as VBOX, accessible via browser 23 Hz precision: Millisecond-level timing with centimeter GPS accuracy AI that helps: Context-aware coaching with official corner names and racing terminology Real impact: Amateur drivers now have access to data previously only available to pros What we learned Technical: Amateur racing generates professional-quality data (23 Hz, sub-centimeter GPS) Performance requires smart design: sample intelligently, load progressively, cache AI results Racing: Milliseconds matter: at 180 km/h, 23 Hz = one reading every 2.2 meters Context is everything: "Turn 5 entry" means more than "2,450m mark" Objectivity beats intuition: "You brake at 150m, the fast driver brakes at 130m" > "I feel slow" What's next for TGRNA Race Telemetry and Driver Comparison AI Analysis Will use to ingest VBOX data and unbundle it from their "Circuit Tools" to help coaches provide objective driving feedback. <div