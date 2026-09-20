---
slug: "project-lpha"
url: "https://devpost.com/software/project-lpha"
title: "Project αlpha"
hackathon: "Hack the Track presented by Toyota GR"
organization: "Toyota Gazoo Racing"
winner: true
words: 677
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Project αlpha

> Live weekend brain for race series and teams: ranks pace and consistency, replays races with AI commentary, and surfaces standout drivers, trends, and anomalies in real time.

[Devpost](https://devpost.com/software/project-lpha) · hackathon [[Hack the Track presented by Toyota GR]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[transportation]]
**user** [[developer]] [[frontline_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]]

**stack** javascript, openlayers, python, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for project αlpha

## Body

Inspiration Modern race weekends generate huge amounts of timing, telemetry, and video, but most stakeholders only see static PDFs and basic timing screens that miss the real story. Project αlpha was born from wanting a single live brain for the weekend that can explain who is actually fast, who is improving, and how the race unfolded, in a way that is useful for engineers, drivers, organizers, and storytellers. It treats data not as a by product of the event but as the foundation for competitive insight and engaging narrative. What it does Project αlpha is a live weekend brain that ingests timing, scoring, and telemetry to rank drivers and teams on raw pace, sector performance, optimal laps, and consistency across every session. It reconstructs races as true to life replays with accurate positions, gaps, overtakes, and anomalies, then adds AI generated commentary and audio on top so that teams, series, and fans can relive the event from any driver view. On top of that, it provides race compare tools, talent and anomaly insights for organizers, and a shared, dynamic weekend schedule hub so everyone in the paddock stays aligned. How we built it We built a data pipeline that normalizes timing and scoring feeds, car telemetry, simulator traces, and geospatial inputs into a single lap and sector aware model for each series. Analytics services sit on top of that model to compute rankings, optimal laps, consistency metrics, race event detection, and driver versus driver deltas, which then feed a visualization layer for race replay, race compare, and weekend dashboards. Finally, an AI layer consumes structured race events and performance insights to script commentary, generate voices, and present digestible insights through web, desktop, and trackside displays. Challenges we ran into Synchronizing different data sources at scale was a major challenge, since timing systems, telemetry loggers, and simulator outputs all use different clocks, formats, and levels of precision. We also had to design interfaces and workflows that work for very different users, such as series directors, engineers, drivers, and media teams, without overwhelming them with graphs or burying critical insights. Building AI commentary that is aligned with the actual data, stays credible to experts, and still feels engaging and human was another key challenge that required careful event modeling and constraints. Accomplishments that we're proud of We can now reconstruct a full race timeline with accurate car positions, gaps, passes, and incidents, then filter that experience down to a single driver, a team, or the whole field with one click. The platform surfaces standout drivers, big improvers, unusual pace gains, and consistency outliers across a full weekend, which lets organizers spot talent and potential rule issues while helping teams and drivers understand performance quickly. Turning raw analytics into watchable race replays with AI voiceover created a bridge between deep performance data and broadcast grade storytelling that did not exist before. What we learned We learned that clarity beats complexity; people want a fast answer to questions like who was actually the fastest, who executed the cleanest race, and where pace was found, not just more charts and exports. We also learned that combining a rigorous data model with a narrative layer is powerful, because series executives and commercial partners engage much more with replay, stories, and simple rankings than with raw telemetry plots. Finally, we saw that something as simple as a live, trusted weekend schedule with countdowns and status can remove a surprising amount of friction across the paddock. What's next for Project αlpha Next we plan to deepen integrations with timing vendors, simulators, and onboard systems so that more series can adopt Project αlpha with minimal setup and higher data fidelity. We will expand anomaly detection for stewards and organizers, add richer talent development views that track improvement over multiple events, and introduce configurable automated reports for teams and drivers after every session. Longer term, we want to ship lightweight mobile and paddock screens so that everyone in the ecosystem, from drivers to partners, can see the same live brain of the weekend in real time. <div