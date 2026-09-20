---
slug: "pew-pew-9mi8pb"
url: "https://devpost.com/software/pew-pew-9mi8pb"
title: "Pew Pew"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 67
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/security_privacy"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Pew Pew

> Pew Pew is a FastAPI analyzer that turns the legacy CCDC intrusion dataset into a forensic-ready narrative by auto-mapping hosts, aggressive attackers, targeted victims, and an attack timeline.

[Devpost](https://devpost.com/software/pew-pew-9mi8pb) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[security_privacy]]
  <sub>weak: health_clinical</sub>
**substrate** [[geospatial]] [[structured_db]]

**stack** css, fastapi, html5, javascript, python, uvicorn

## How they structured the write-up

- features

## Body

Network Graph Intro A lightweight web application that is feed a completed Suricata fast.log security alert file (e.g., from an Hospital Network) and renders a network + alert graph with anomaly scoring of security alerts. Features Parses full Suricata fast.log once at startup Builds force-directed network graph (hosts + alert signature nodes) Simple z-score based anomaly detection on per-source alert volume Pure FastAPI + D3.js frontend <div