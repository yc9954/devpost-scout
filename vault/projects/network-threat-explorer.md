---
slug: "network-threat-explorer"
url: "https://devpost.com/software/network-threat-explorer"
title: "Network Threat Explorer"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 257
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
---

# Network Threat Explorer

> Insightful Network Traffic Visualization and Analysis

[Devpost](https://devpost.com/software/network-threat-explorer) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[education]] [[transportation]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]]

**stack** arkime, cohere, duckdb, flask, malcolm, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the project

## Body

Inspiration As students with no prior experience in data analysis or cybersecurity, we were eager to broaden our skill set and deepen our understanding of these fields. We saw an opportunity with this challenge not only to learn but also to support other aspiring professionals like ourselves in developing these skills for the industry. What it does Our project is made to help analyze threats and anomalies within network traffic. We used the legacy MACCDC dataset as the premise to build our tools from. How we built it We used flask, duckdb and python to create a simple app to help analyze the network traffic data from the dataset. We also setup a Malcolm suite (Dashboards, Arkime, CyberChef, Netbox) locally for manual visualization and manipulation on the dataset. Challenges we ran into Ram space (16GB is not enough) File size of dataset Analyzing and visualizing the network traffic at scale Sleep + time management Accomplishments that we're proud of We're proud of integrating an AI API (cohere) to help assist with visualizing and analyzing network traffic, as well as integrating Malcolm into the project as well. What we learned We learned network traffic analysis techniques, docker and docker compose, back-end processes and how to work with/manipulate large enterprise scale network traffic data. What's next for the project The next thing for this project is to generate/automate reports for network traffic anomalies, alerts and CVE's, to help improve productivity for SOC analysts. Additionally, also updating the Suricata rules is a must do on the list as well. <div