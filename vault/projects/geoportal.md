---
slug: "geoportal"
url: "https://devpost.com/software/geoportal"
title: "GeoPortal"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 520
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# GeoPortal

> GeoFlightVR: Don't just track your flight—experience it.

[Devpost](https://devpost.com/software/geoportal) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[transportation]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** aviationstackapi, bluetooth, canvasapi, exoplayer, jetpackcompose, kotlin

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Flag Game Selecting a Flight to track World map with your flight Inspiration I conceived this idea on a flight to Rome. Frustrated by the lack of entertainment systems and the inability to know our location, I saw an opportunity to solve the boredom of air travel. I wanted to create a solution that turns the "stuck in a seat" experience into a journey of discovery. What it does The app transforms in-flight travel into an interactive exploration. At its core, it is a real-time flight monitor that visualizes the journey on a dynamic map. Using a database of over 14,000 cities, it intelligently detects landmarks to trigger "City Explorations"—immersive 360° VR video tours of the locations below. To keep passengers engaged, the app features a cyberpunk-inspired interface with educational mini-games like "Flag Challenge" and "Airport Rush." These can be played against an AI or nearby passengers via offline Bluetooth multiplayer, creating a complete in-flight entertainment ecosystem. How we built it I built the app using native Android technologies (Kotlin and Jetpack Compose). I engineered a custom data pipeline to cross-reference AviationStack API telemetry with local geospatial data. Visually, I developed a custom graphics engine within Jetpack Compose’s Canvas API. Instead of heavy 3D libraries, I used custom projection algorithms to render a holographic globe with scientifically accurate day/night cycles. For social features, I implemented a custom Bluetooth networking layer for direct socket connections, while ExoPlayer handles the 360° video playback. Challenges we ran into My biggest problem was time. I only saw the competition 4 days before the deadline and wanted to do something even if it is not completed. Although I was still able to add every feature I wanted with a huge success. Also optimizing the 3D rendering engine was quite the process. Implementing custom projection algorithms initially caused stuttering and battery drain; I had to rigorously profile the app and refactor drawing logic to ensure smooth performance. Additionally, managing offline Bluetooth multiplayer was difficult due to the variability of Android’s Bluetooth APIs. Establishing a stable handshake required building a custom logging system and a robust socket-management solution to handle interruptions and reconnect users seamlessly. Accomplishments that we're proud of I am proud of being able to build such useful application in just 4 day. Furthermore, establishing a stable peer-to-peer Bluetooth handshake in an offline environment was a major win. This robust local communication layer not only enables gaming but lays the groundwork for future synchronized in-flight media. What we learned I learned that with the right mathematical optimization, Jetpack Compose’s Canvas API is capable of high-performance complex visualizations without needing OpenGL. I also gained deep experience in offline-first architecture, realizing that building resilience against network failures—whether for API calls or Bluetooth packets—is essential for a polished user experience. What's next I plan to evolve the app into a comprehensive social platform. With our Bluetooth infrastructure in place, our next step is introducing "Shared Cinema" and "Music Lounge" features, allowing passengers to sync media offline. I also aim to expand the multiplayer ecosystem, using the holographic globe as a shared game board for deeper cooperative experiences. <div