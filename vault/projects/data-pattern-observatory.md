---
slug: "data-pattern-observatory"
url: "https://devpost.com/software/data-pattern-observatory"
title: "Data Pattern Observatory"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 324
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Data Pattern Observatory

> Data is power

[Devpost](https://devpost.com/software/data-pattern-observatory) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** elasticsearch, mongodb, python, redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for data pattern observatory

## Body

Inspiration We were inspired to by Title Sponsor PNC Bank's problem statement: As organizations increasingly rely on data to drive decision-making, ensuring a clear understanding of how data is created, accessed, moved, and used is critical for security, performance, and governance. Yet, many organizations struggle to maintain visibility into these data flows, leading to inefficiencies, security risks, and compliance challenges. We challenge you to design an innovative solution that enhances the observability of data patterns throughout its lifecycle. Your solution should allow organizations to monitor and analyze how data is created, accessed, moved, and used – with business context. What it does Data Pattern Observatory combines real-time data tracking with statistical modeling to not only monitor but also predict data flow patterns. It uses historical data and statistical analysis to identify trends, detect anomalies, and predict future data movement patterns, helping organizations proactively manage their data infrastructure. How we built it We built the system using: MongoDB, Elasticsearch, and TimescaleDB for different aspects of data tracking Python for backend processing and pattern detection Statistical models for pattern prediction Streamlit for an interactive dashboard Docker for containerization Redis for real-time monitoring Challenges we ran into Handling different types of data patterns. Dealing with varying data volumes and patterns across different timeframes Accomplishments that we're proud of Created a functioning data observability system from scratch Successfully implemented statistical modeling for pattern prediction Built an intuitive interface that visualizes both current and predicted patterns What we learned The value of combining real-time monitoring with predictive analytics The importance of data observability in modern systems What's next for Data Pattern Observatory We have created a crewai based agent that can predict a market crisis based on data patterns We also have an ensemble of ML models in mind that perform risk management We also have a Random Forest Regressor based data flow pattern prediction system Our future goal is to integrate these into the current working application <div