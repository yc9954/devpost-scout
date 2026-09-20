---
slug: "greenpipe"
url: "https://devpost.com/software/greenpipe"
title: "GreenPipe"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 553
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# GreenPipe

> A carbon-aware CI/CD agent that measures, compares, and reduces the carbon footprint of your pipelines. Built on the GitLab Duo Agent Platform. Three specialist agents. One MR comment.

[Devpost](https://devpost.com/software/greenpipe) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]]
**user** [[developer]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** anthropic, azure-1.185, carbon, claude, eia, eia-egrid-for-the-us, entso-e, gcp-1.1, gitlab, iea, iso/iec, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for greenpipe

## Body

Inspiration Over 100 TWh of clean energy was curtailed globally in 2024 — thrown away because nobody was computing where the wind was blowing. Meanwhile, data centers in Virginia overwhelmed a grid never built for their load. We realized the same pipeline produces 88x different carbon emissions depending on where it runs, but developers have zero visibility into this inside GitLab. What it does GreenPipe posts a carbon report on every merge request. When a pipeline succeeds, the agent performs three analysis phases: Phase 1 — Carbon Scout identifies the runner region and looks up grid carbon intensity from a dataset of 21 cloud regions sourced from ENTSO-E, EIA eGRID, and IEA. Phase 2 — Green Analyst estimates energy consumption per job using Cloud Carbon Footprint methodology and computes the Software Carbon Intensity (SCI) score following the ISO/IEC 21031 standard. Phase 3 — Green Reporter formats the analysis as native GitLab markdown and posts it as an MR comment — including per-job breakdowns, cross-region comparisons, and a specific routing recommendation showing which region would produce the least carbon. How we built it GreenPipe is a custom agent on the GitLab Duo Agent Platform powered by Anthropic Claude. The agent uses GitLab's built-in tools (Get Job Logs, Create Merge Request Note, Get Project) to read pipeline data and post results. Carbon intensity data is embedded from a curated dataset compiled from government sources (ENTSO-E for Europe, EIA eGRID for the US, IEA for global coverage). Energy estimation follows the Cloud Carbon Footprint methodology: CPU wattage from SPECpower database power curves, 50% default utilization, and provider-specific PUE values (AWS 1.135, GCP 1.1, Azure 1.185, GitLab shared 1.2). The SCI formula is: $$SCI = E \times I \text{ per pipeline}$$ Where $E$ is energy in kWh and $I$ is grid carbon intensity in gCO2eq/kWh. Challenges we ran into The GitLab Duo Agent Platform is brand new — documentation is still evolving. We initially designed a multi-agent custom flow (v1 YAML spec with three chained AgentComponents), but pivoted to a single unified agent created through the UI when the flow execution infrastructure wasn't fully available. The single-agent approach actually produced better results because all context stays in one conversation. Getting accurate runner region identification was tricky — GitLab shared runners don't expose their region in pipeline metadata, so we default to the Virginia/us-east-1 equivalent and document this assumption transparently. Accomplishments that we're proud of GreenPipe posted a working carbon report on a real merge request within hours of building it. The report includes real energy estimates, SCI scores, cross-region comparisons with percentage savings, and actionable routing recommendations — all using established methodologies (CCF, SCI) and real government data sources. What we learned The biggest insight: the carbon difference between cloud regions is enormous (88x between Stockholm and Mumbai) and completely invisible to developers. Making this visible on every MR is a small intervention with outsized impact — especially as CSRD compliance makes Scope 3 reporting mandatory. What's next for GreenPipe Real-time carbon intensity via Electricity Maps API (replacing static annual averages) Weekly sustainability reports as scheduled issues Auto-routing: actually modify runner tags based on carbon data, not just recommend Embodied emissions (the $M$ component of the full SCI formula: $SCI = (E \times I + M) \text{ per } R$) CSRD-compatible export format for compliance teams <div