---
slug: "farmer-force"
url: "https://devpost.com/software/farmer-force"
title: "Farmer Force"
hackathon: "Slack Agent Builder Challenge"
organization: "Salesforce"
winner: true
words: 881
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/housing_homeless"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Farmer Force

> Free satellite crop-health intelligence, delivered as an AI agent inside Slack. It catches disease and drought early — and explains it in plain English.

[Devpost](https://devpost.com/software/farmer-force) · hackathon [[Slack Agent Builder Challenge]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[agriculture_food]] [[housing_homeless]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]

**stack** block-kit, claude, computer-vision, fastapi, google-cloud, mcp, model-context-protocol, next.js, python, rasterio, redis, remote-sensing, satellite-imagery, sentinel-2

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for farmer force

## Body

The AI agronomist that lives in your Slack. How it works: free Sentinel-2 data, analyzed in the cloud, delivered as an AI agent inside Slack through a custom MCP server. A flagged field's satellite health map, with its exact traced boundary. Green is healthy; orange and red flag stress. A healthy field seen from space. Farmer Force checks each field against a seasonal baseline to catch trouble early. The Farmer Force dashboard inside Slack: every field at a glance, ranked by health, with one-click scan, report, and re-scan. Ask how your fields are doing and Farmer Force answers like an agronomist in plain English: what needs action, what to do, and what is fine. A verified alert card with the field's satellite heatmap, the recommended action, and one-tap buttons to plan it, assign it, or confirm. One tap turns the finding into a dedicated task channel, where each step of the fix gets assigned to a specific teammate. Inspiration Crop disease and drought quietly wipe out billions of dollars of harvest every year. The tools to catch them early (drones, lab tests, agronomists on retainer) are expensive and out of reach for the co-ops and smallholder farmers who grow most of the world's food. Meanwhile the data to catch these problems has been overhead the whole time. Satellites photograph every field on Earth, for free, over and over. The problem was never the data. It is that no farmer could actually use it. We built Farmer Force to close that gap. What it does Farmer Force turns free satellite imagery into plain-language crop intelligence, and delivers it in the two places a farm team already works: a web command center and Slack. See every field on the web. Every field sits on one map. Trace a field's exact shape and Farmer Force turns the latest satellite pass into a clear picture of crop health, thriving in one part of the field, stressed in another. Ask it anything in Slack. Type @Farmer Force how are my fields? or /scout why is the vineyard flagged? and it answers like a real agronomist, in plain English, with the heatmap attached. No charts, no jargon. Every alert is AI-verified. Before it cries wolf, Claude's vision model checks the real imagery and weather to confirm the problem is genuine, not a harvested strip, a road, or normal seasonal change. So the team trusts every alert. Plan it and assign it. When a field needs attention, one tap writes an action plan and spins up a dedicated channel for that field, where each task is assigned to a specific person by name. It watches while you sleep. On its own schedule, Farmer Force re-scans every field and posts an alert the moment something changes. Nobody has to ask. How we built it The Slack agent. A custom MCP (Model Context Protocol) server with six tools exposes the whole platform to Claude Opus 4.8, which drives it in natural language via Anthropic's MCP connector. Built across Slack's Events API, slash commands, Block Kit, App Home, interactive buttons and user pickers, channel creation, and Canvas. The satellite brain. A Python and FastAPI service on Google Cloud Run pulls free Sentinel-2 imagery (via AWS Earth Search, no auth), computes vegetation and moisture indices, detects anomalies against a per-crop seasonal baseline, infers the likely cause, runs a Claude vision verification pass, and renders annotated heatmap tiles. Plain language everywhere. Every layer is prompted to write for a farmer with no technical training, so zero jargon reaches the user. The stack. Next.js and TypeScript on Vercel (Slack app, MCP server, web dashboard), Python and rasterio on Cloud Run, Upstash Redis and Vercel Blob for storage, Open-Meteo for weather, OpenStreetMap for geocoding. Challenges we ran into Making satellite science trustworthy. Spectral indices alone produce false alarms, so we added a Claude vision tier that reviews the real imagery and stands down fields that only look stressed. It genuinely does not cry wolf. Making it readable. Our first alerts were full of index values and z-scores. We stripped every technical term at every layer so the output reads like advice from a neighbor. Making it one coherent product. The hard part was not answering questions. It was the autonomous monitor, the task channels, and the assignments, and keeping every surface (chat, dashboard, report, alerts) telling one consistent story. Accomplishments that we're proud of A real, working, end-to-end system on live infrastructure, not a mockup. Free satellite data goes in. Plain-English, AI-verified guidance comes out, and it does not stop at the alert. It writes the fix, opens a workspace for it, and hands the tasks to people. That full loop, from orbit to a named person walking the field, is what we are most proud of. What we learned The winning move for AI for good is not a smarter model. It is meeting people where they already work and speaking their language. The agent is only useful if the farmer trusts it, understands it, and can act on it without leaving the tools they already use. What's next for Farmer Force Multi-tenant support for whole co-ops, per-crop disease models, SMS fallback for low-connectivity regions, and closing the loop with ground IoT sensors that auto-confirm satellite alerts, turning "confirm on the ground" literal. <div