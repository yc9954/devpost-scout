---
slug: "apartment-monitoring"
url: "https://devpost.com/software/apartment-monitoring"
title: "Eco Fast Track"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 428
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/housing_homeless"
  - "substrate/web_dom"
---

# Eco Fast Track

> A smart water management tool that helps households and property managers optimize water usage, save on utilities, and promote conservation through personalized insights and community-driven data.

[Devpost](https://devpost.com/software/apartment-monitoring) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[housing_homeless]]
**substrate** [[web_dom]]

**stack** 3d-printer, arduino, c++, cad, canva, figma, gemini, iot, next.js, node.js, pinata, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eco fast track

## Body

Proof-of-concept-graph-generation Proof-of-concept-email-warning Figma-web-design Front-Hardware-assembled Top-hardware-assembled Front-angled-hardware-assembled 3D-printing-encasement Brainstorm session Inspiration After conducting research on the primary expenses faced by property managers, we identified faulty water gauges as a significant issue. Property managers often depend on tenants to report problems or must coordinate inconvenient check-ins to identify issues. To address this, we developed an intuitive web application designed to streamline the process, allowing property managers to proactively manage water usage without awkward tenant interactions. At the same time, tenants gain an engaging, community-focused experience that promotes sustainability. Drawing inspiration from the popularity of visually appealing and personalized data presentations, we aimed to create a solution that’s both practical and fun—combining functionality with a touch of a "Spotify Wrapped" vibe to make data meaningful and enjoyable. What it does Our tool uses smart gauge sensors to monitor water temperature and flow, providing real-time insights into usage. It aggregates data over time, compares it to global benchmarks, and uses AI to offer personalized water-saving recommendations. Property managers can proactively address inefficiencies, while tenants receive automated email alerts if their usage exceeds the average. With an optional community-sharing feature and engaging, user-friendly visuals, the platform promotes accountability, sustainability, and collaboration. How we built it Using the IoT grover kit (specifically the temperature, potentiometer, and an LCD) as our smart gauge sensor to provide the data to a webpage via serial. On the software end python, Node.Js, Gemini, Pinata, and Next.Js are used to give tenants personal advice based on their own sensor aggregations and for plot development. Challenges we ran into Originally planning to use wifi module however a successful connection was very rare Spent 3 hours trying to get the LCD to turn on and it turned out being due to an incompatible arduino board with the grove kit. 3D printed encasement did not fit all components so there was a bit of improvising there. Accomplishments that we're proud of Getting past all of the challenges Finding a solution that incorporated gathering a community and using software, hardware and data presentation. What we learned How to work with a wifi module, to account for clearance next time when Cad-ding a part, and lastly how to debug IoT devices. What's next for Eco Fast Track Incorporating other renewable elements like using solar to encourage a minimized use of electricity when it comes to natural lighting. This includes, Incorporating renewable solutions, such as solar power, to reduce electricity consumption by maximizing natural lighting. Another feature is a drop in water pressure may indicate a leak and detect pressure spikes from freezing expansion. <div