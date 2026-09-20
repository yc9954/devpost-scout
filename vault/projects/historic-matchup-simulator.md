---
slug: "historic-matchup-simulator"
url: "https://devpost.com/software/historic-matchup-simulator"
title: "Historic Matchup Simulator"
hackathon: "Google Cloud x MLB(TM) Hackathon – Building with Gemini Models"
organization: "Google"
winner: true
words: 301
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/sensor_telemetry"
---

# Historic Matchup Simulator

> Imagine creating matchups between any MLB teams throughout baseball history. With MLB StatsAPI data and Google Gemini, you can.

[Devpost](https://devpost.com/software/historic-matchup-simulator) · hackathon [[Google Cloud x MLB-TM- Hackathon - Building with Gemini Models]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** flask, gemini, google, html, javascript, python, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for historic matchup simulator

## Body

Inspiration My curiosity and love of statistics drove me to create a tool that could answer the age-old question: "What if Team X from Year Y played Team Z from Year W?" The project combines advanced statistics, machine learning, and real-time simulation to bring historical matchups to life. What it does The MLB Historical Matchup Simulator creates pitch-by-pitch baseball games between any MLB teams from 1920 to present. It: Normalizes statistics across different eras for fair matchups Simulates realistic pitch sequences and outcomes Tracks detailed game states including baserunners and fielding Generates AI-powered game analysis and commentary Provides comprehensive post-game statistics and highlights How we built it The simulator was developed using: Python/Flask backend for game logic and statistical processing Socket.IO for real-time updates Hosted via Google Cloud Run Google Gemini API for natural language generation Advanced statistical models for era normalization MLB Stats API for historical data Custom algorithms for: Exit velocity calculations Hit distance estimation Pitch selection and outcomes Defensive positioning Challenges we ran into Normalizing statistics across vastly different eras of baseball Creating realistic pitch sequences that reflect historical tendencies Implementing real-time game state management Balancing simulation speed with detail Handling edge cases in baserunning and scoring situations Developing accurate physics models for hit outcomes Accomplishments that we're proud of Created a statistically accurate simulation engine Successfully normalized player performance across 100+ years Implemented realistic physics-based hit outcomes Developed natural language game summaries Built an engaging real-time interface Maintained historical accuracy while ensuring entertaining gameplay What we learned Advanced baseball statistics and sabermetrics Real-time web application architecture Historical data normalization techniques Physics modeling for sports simulation Natural language processing integration Complex state management in simulations What's next for Historic Matchup Simulator Season simulation mode Custom team creation Historical playoff brackets Player career trajectory modeling Advanced weather effects <div