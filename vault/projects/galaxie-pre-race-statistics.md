---
slug: "galaxie-pre-race-statistics"
url: "https://devpost.com/software/galaxie-pre-race-statistics"
title: "Galaxie - Pre Race Statistics"
hackathon: "Hack the Track presented by Toyota GR"
organization: "Toyota Gazoo Racing"
winner: true
words: 256
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
---

# Galaxie - Pre Race Statistics

> Bayesian Monte Carlo race predictions power interactive tabs showing driver performance, track stats, and win probabilities—all before the race starts.

[Devpost](https://devpost.com/software/galaxie-pre-race-statistics) · hackathon [[Hack the Track presented by Toyota GR]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[sensor_telemetry]]

**stack** django, pymc, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration I built a system that uses historical data to predict outcomes, win probabilities, and performance metrics—similar to FiveThirtyEight's sports predictions but tailored for racing. What it does Pre-Race Statistics provides interactive tabs with: Driver Overview : Sortable driver cards with historical performance, track stats, and simulation projections Race Simulation : Monte Carlo predictions showing win probabilities, and finish position distributions The system runs 15,000 Monte Carlo simulations using Bayesian hierarchical modeling to predict race outcomes, stage finishes, and fastest lap winners before the green flag. How we built it Backend (Python/Django) : Bayesian hierarchical model using PyMC with Plackett-Luce ranking for multi-head predictions Feature engineering with temporal decay and track similarity weighting, stored in Arrow format for efficient frontend consumption Frontend (React/TypeScript) : Tabbed interface with Arquero for client-side data processing and real-time simulation progress tracking Challenges we ran into Model Complexity : Balancing sophistication with efficiency—reduced from 50k to 15k simulations while maintaining convergence Data Pipeline : Efficiently loading and processing large simulation datasets (15k simulations × 40 drivers) for frontend consumption Caching Strategy : Implementing robust cache invalidation based on model version, race entries, and simulation parameters Accomplishments that we're proud of Predictive Accuracy : Bayesian model captures driver skill, team effects, track-specific performance, and momentum Performance : Reduced simulation time by 3x (50k → 15k) while maintaining statistical precision What we learned Bayesian Modeling : Hierarchical models with proper priors can capture complex interactions while avoiding overfitting Simulation Efficiency : Convergence analysis showed diminishing returns beyond 15k simulations, enabling faster iteration <div