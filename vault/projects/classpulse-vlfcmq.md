---
slug: "classpulse-vlfcmq"
url: "https://devpost.com/software/classpulse-vlfcmq"
title: "Classpulse"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 630
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Classpulse

> An end-to-end IoT microclimate monitor and bi-directional real-time telemetry dashboard that tracks classroom air stagnation and occupancy to optimize indoor study environments.

[Devpost](https://devpost.com/software/classpulse-vlfcmq) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[education]] [[transportation]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** arduino, c++, chart.js, dht11, esp32, html5, javascript, postgresql, supabase, tailwind-css

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for classpulse

## Body

view 1 supabase view 3 view 2 arduino ide Supabase demo Inspiration While researching urban environmental conditions and indoor microclimates for a geography and social science class, I started looking into how public schools in Bishkek and across Kyrgyzstan handle classroom environments. During local winters, doors and windows are kept tightly shut to keep out the extreme cold, but classrooms end up packed with students. CO₂ levels, heat, and humidity build up quickly, causing headache, fatigue, and lower concentration during lessons. Most schools here lack central ventilation monitoring or real-time indoor air quality systems. I wanted to build a practical, low-cost tool using accessible hardware to measure this exact spatial issue and give real-time feedback when a classroom needs fresh air. What it does An ESP32 microcontroller tracks classroom temperature and humidity via a DHT11 sensor while counting room occupancy using an infrared obstacle sensor. Front-end interactive sliders allow teachers to calibrate maximum capacity alerts and temperature comfort limits dynamically. The ESP32 pulls these limits back down over Wi-Fi every 5 seconds to adjust its physical desk alert parameters. Calculates a single, aggregate air health metric (0–100%) using a custom weight-based mathematical model. Tracks crowd entry speed to estimate how long before the room hits critical air stagnation if conditions don't change. Pushes raw telemetry from the database to the dashboard instantly, rendering live updates on dynamic Chart.js plots without page reloads. How I built it ESP32 Microcontroller wired to a DHT11 temperature/humidity sensor, infrared break-beam obstacle sensor (GPIO 18). Supabase (PostgreSQL engine) configured with Realtime WebSockets replication enabled on the desk_telemetry table. Challenges I ran into Translating physical sensor pulses on an ESP32 microcontroller into structured data frames that a web browser can render cleanly without crashing the hardware loop. Setting up low-latency PostgreSQL replication in Supabase to eliminate polling delays so live data streams into the web interface sub-second. Synchronizing web slider changes back down to the microcontroller so threshold edits on the screen immediately update the physical buzzer trigger logic on the desk unit. Crafting a clear mathematical formula that balances temperature ratios and occupancy density without giving skewed warnings during short spikes. Filtering out noisy signals and calibrating infrared beam breaks to prevent duplicate counts when multiple people move past the sensor. Accomplishments that I'm proud of Built a fully working hardware-to-cloud pipeline that streams classroom metrics in under a second. Applied geography and social science research into a working physical product that solves a real issue in local schools. Connected web dashboard controls directly to physical edge hardware. What I learned Studying classroom conditions in Bishkek showed me that geography and social issues often need simple, low-cost physical fixes rather than expensive commercial systems. Writing code for a microcontroller that handles input sensors, screen updates, and Wi-Fi requests all at once takes careful timing so the chip doesn't freeze up. Real-world sensors are messy. I had to learn how to clean up noisy IR data in code and write a balanced formula so the room score actually makes sense. I got hands-on experience wiring components in C++, handling real-time data in PostgreSQL, and displaying live graphs on a web page. What's next for Classpulse Replacing the basic DHT11 with high-precision NDIR CO₂ sensors (like the SCD30 or MQ-135) to measure exact carbon dioxide concentration. Adding two infrared sensors side-by-side at the door to track bidirectional entry and exit traffic simultaneously without count drift or latency. Connecting smart relay modules to automatically open motorized window vents or turn on fans when the Stagnation Index hits critical levels. Training predictive time-series models on historical data to anticipate classroom crowding based on timetable schedules. Refining the prototype into a polished, low-cost kit to pitch to local education boards, school administrators, and grant programs for public school deployments. <div