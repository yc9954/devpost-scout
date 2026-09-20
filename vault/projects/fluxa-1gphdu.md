---
slug: "fluxa-1gphdu"
url: "https://devpost.com/software/fluxa-1gphdu"
title: "FLUXA"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 627
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# FLUXA

> The trading workstation has not changed in 30 years. Fluxa changes it - bringing spatial, intuitive financial analysis into Mixed Reality for the first time.

[Devpost](https://devpost.com/software/fluxa-1gphdu) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** csharp, meta-quest-3, meta-xr-sdk, mx-ink-actions-sdk, unity, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what is next for fluxa

## Body

FLUXA — Spatial Trading Platform Stage: Ideation — DevStudio by Logitech Challenge 2026 | Stylus in XR, Meta Quest Category Inspiration The retail trading workstation has not meaningfully changed since the 1990s. Traders manage three or more flat monitors simultaneously, draw trendlines with a mouse, and constantly switch context between charts, news, and macro data. No professional charting platform offers pen-native input, and the Meta Quest Store contains no dedicated Mixed Reality financial application. These two gaps converging at the same moment — a mature stylus SDK and an untouched platform category — are the direct inspiration for Fluxa. What it does Fluxa is a Mixed Reality trading workstation for Meta Quest 3 / 3S with the MX Ink stylus as its primary input. It replaces the flat multi-monitor setup with a spatially arranged environment around the trader's physical desk, built around four features: 3D Chart Canvas — Multiple live charts float freely in MR space, repositioned and layered without physical screen constraints. MX Ink Stylus Integration — Trendlines, support and resistance levels, Fibonacci retracements, and annotations are drawn directly onto live charts with natural pen precision via the MX Ink Actions SDK. For a trendline defined by two price-time coordinates $(t_1, p_1)$ and $(t_2, p_2)$, the slope maps directly onto a 3D ray-surface intersection, making annotation placement both precise and physically intuitive. Macro Dashboard 3D — A spatial panel pinned in peripheral view displays live economic indicators, portfolio metrics, and market alerts — macro context always visible without a tab switch. Focus Mode — All panels collapse into a single immersive chart view, navigated entirely through stylus gestures. The full open-annotate-monitor-decide workflow executes inside one uninterrupted MR session. How we built it At the ideation stage, the architecture is designed around three layers: the Meta Quest 3 / MX Ink hardware layer using the MX Ink Actions SDK for 6-DOF stylus input; a Unity rendering layer using the Meta XR SDK for spatial anchoring, scene understanding, and passthrough compositing; and a data layer using a WebSocket bridge to market data providers with local session caching. No desktop companion app is required. Challenges we ran into The key technical challenges identified for development are stylus tip precision in 3D space (inside-out tracking drift compounds into annotation placement error), maintaining perceptual stability of world-locked chart panels during live tick-by-tick data updates, managing arm fatigue over extended trading sessions, and navigating real-time financial data licensing costs within a freemium distribution model. Accomplishments that we are proud of Fluxa identifies and addresses a genuine zero-competition gap on the Meta Quest platform. The four-step trader workflow maps cleanly onto MX Ink and Quest hardware without requiring unreleased APIs. The concept targets a market of over 35 million active brokerage accounts against a spatial computing market projected at $20B+ in 2025, growing at approximately 42.5% CAGR through 2030. What we learned Technical analysis has been artificially constrained by mouse-based input for decades. Traders have adapted to the tool's limitations rather than the reverse. The MX Ink stylus is not an accessory in this context — it is the correct primary interface primitive for a discipline that is fundamentally gestural and precision-driven. First-mover positioning on a platform with approximately 25 million installed headsets and no finance competition carries real strategic weight that narrows with each quarter. What is next for FLUXA The roadmap runs in four phases toward a Meta App Store-eligible release: a proof-of-concept Unity scene validating MX Ink trendline drawing on world-locked chart panels; live data integration via a paper-trading feed with candlestick rendering and annotation persistence; full four-step workflow with Macro Dashboard and Focus Mode; and structured user testing with active traders against existing platforms (TradingView, ThinkOrSwim) to validate precision, ergonomics, and workflow fit ahead of a Semi-Finals submission. <div