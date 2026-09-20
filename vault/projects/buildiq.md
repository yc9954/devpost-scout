---
slug: "buildiq"
url: "https://devpost.com/software/buildiq"
title: "BuildIQ"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 499
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
---

# BuildIQ

> BuildIQ integrates IoT monitoring and sustainability insights to optimize energy consumption, enhance occupant well-being, and streamline operational efficiency into a building.

[Devpost](https://devpost.com/software/buildiq) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[climate_energy]]
**user** [[frontline_worker]]
**substrate** [[sensor_telemetry]]

**stack** fastapi, framer-motion, git, google-antigravity, influxdb, next.js-14, npm, numpy, pandas, postgresql, postman, pydantic, python, react-18

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for buildiq

## Body

Inspiration Buildings today are responsible for a significant portion of global energy consumption and directly impact the health and productivity of the people inside them. However, most facilities still operate on static, "dumb" systems with zero real-time visibility. I was inspired to build BuildIQ because I wanted to bridge the gap between physical structures and data-driven intelligence. What it does BuildIQ is my comprehensive Smart Building Intelligence Platform. It allows an operator to: Manage a Digital Twin: Visualize and configure floors, zones, and rooms in real-time. Customize its Dashboard: Use a fully dynamic, drag-and-drop interface to create tailored views of my building's operations. Track Health & Wellness: Monitor CO2, temperature, humidity, and noise to calculate a live "Wellness Score." Analyze Sustainability: Track energy consumption, power distribution, and carbon footprint (kg CO2/day). Secure Operations: Access real-time security logs and automated maintenance tracking to ensure nothing breaks down. How I built it Frontend: I built the UI with Next.js 14 and TypeScript. I used Tailwind CSS and Framer Motion to achieve a premium enterprise aesthetic, and Recharts for all the data visualizations. Backend: I developed a high-performance FastAPI server in Python to handle all the heavy data processing and business logic. Real-Time Data: I implemented WebSockets to push live telemetry from my custom-built IoT Sensor Simulator directly to my dashboard. Challenges I ran into One of my biggest hurdles was real-time state synchronization. I had to ensure that any change I made in the "Manage Building" tab (like adding a new floor or renaming a room) reflected instantly across the entire dashboard without requiring a refresh. I also spent significant time navigating tricky React hydration errors caused by the mismatch between server-side rendering and my dynamic grid layouts. Finally, I had to solve a "ghost dragging" bug where duplicate room names caused multiple elements to move at once; I solved this by implementing a UUID-based identification system. Accomplishments that I'm proud of I am incredibly proud of successfully integrating all hackathon themes into a single, coherent platform. It was a major goal for me to create a "prosumer" UI that feels like a high-end enterprise tool rather than a basic prototype. Additionally, my custom IoT simulator works pretty well I think, at least enough that the platform feels truly "alive,". What I learned I gained deep experience in building scalable real-time architectures and learned how critical "Digital Twin" integrity is for a system like this. I also refined my ability to balance aesthetic design with data density, learning how to make an application looks good while keeping it a usable tool for a facility manager. What's next for BuildIQ Hardware Integration: Adding support for industry-standard protocols to connect my software to real-world sensors. Predictive Maintenance: Implementing advanced LSTM neural networks to predict equipment failure before it happens. Mobile Suite: Building a dedicated app for on-the-ground technicians so they can receive my alerts and manage logs on the go. Green Benchmarking: Developing built-in reporting tools for LEED and BREEAM sustainability certifications. <div