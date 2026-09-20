---
slug: "energidot"
url: "https://devpost.com/software/energidot"
title: "EnergiDot"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 508
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "domain/scientific_research"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# EnergiDot

> DePIN + DAG Energy Grid Management Parachain

[Devpost](https://devpost.com/software/energidot) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[climate_energy]] [[finance_payments]] [[scientific_research]]
  <sub>weak: developer_tools</sub>
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]
  <sub>weak: sensor_telemetry, web_dom</sub>

**stack** aiohttp, api, apscheduler, asyncio, asyncpg, aura, authentication, axios, bcryptjs, blockchain, cargo-(rust), cargo-test-(rust), chart.js, copernicus-era5

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for energidot

## Body

Architecture & System Design Diagram of EnergiDot Inspiration he project addresses the gap between decentralized blockchain infrastructure and physical energy grid requirements. Renewable energy adoption requires market mechanisms that enable small-scale producers to participate directly without centralized intermediary fees. Polkadot's parachain architecture provides the scalability and interoperability needed for real-world energy trading applications. What it does EnergiDot enables peer-to-peer renewable energy trading through blockchain smart contracts. Users register energy-producing devices, list excess energy for sale, purchase energy from verified renewable sources, stake tokens for rewards and contribute verified grid data. The platform integrates real-time data from NREL, EIA, ENTSO-E and weather services to inform pricing and grid coordination. How we built it The system uses Substrate FRAME to build three custom pallets for energy trading, DAG consensus and tokenomics. A Node.js API gateway bridges the React frontend with the Substrate node through Polkadot.js API. Python services collect data from external energy and weather APIs on scheduled intervals. PostgreSQL and Redis provide data persistence and caching. Kubernetes orchestrates containerized services for production deployment. Key Databses Used in Project, National Renewable Energy Laboratory Datasets (PVDAQ, NSRDB, WIND Toolkit)- NREL (Solar/Wind data) Open Power System Data (Europe) - OPSD (European grid data) U.S. Energy Information Administration Open Data - EIA (US energy data) European Network of Transmission System Operators for Electricity Transparency Platform - NTSO-E (Grid transparency) National Oceanic and Atmospheric Administration – Climate Data Online - NOAA (Weather data) Copernicus Climate Data Store (ERA5, environmental data) - Copernicus (Climate data) Pecan Street Dataport – Smart Meter and Solar Data - PPecan Street (Smart meter data) Global EV Charging Infrastructure Database - Open Charge Map (EV infrastructure) Global Weather and Forecast API - OpenWeatherMap (Forecasts) Challenges we ran into Implementing hybrid GRANDPA and DAG consensus required careful state management to prevent conflicts between global and local finality mechanisms. Integrating multiple external data sources with different API rate limits and data formats needed robust error handling and retry logic. Optimizing Substrate runtime weights for custom pallet operations required iterative benchmarking to prevent block congestion. Accomplishments that we're proud of The platform successfully integrates live renewable energy data from eight external sources including NREL, EIA, and ENTSO-E. The hybrid consensus achieves sub-second local transaction finality while maintaining global security through GRANDPA. Three production-ready custom pallets implement complete energy trading, reputation, and staking logic with comprehensive test coverage exceeding 80%. What we learned Substrate's modular pallet architecture enables rapid development of domain-specific blockchain logic compared to general-purpose smart contract platforms. Real-world data integration requires sophisticated caching strategies to balance freshness and API costs. Effective parachain design must carefully balance on-chain computation costs with off-chain data aggregation to achieve acceptable transaction fees for micro-transactions. What's next for EnergiDot Integration with Phala Network for privacy-preserving smart meter data processing. Implementation of AI-powered prediction models for optimal energy trading timing using historical grid data. Deployment to Polkadot mainnet through slot auction participation. Partnership development with solar panel manufacturers for native device integration. Expansion of cross-chain bridges to Energy Web and Bitgreen parachains for carbon credit trading. <div