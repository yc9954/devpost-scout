---
slug: "shelterguard-the-national-homelessness-risk-monitor"
url: "https://devpost.com/software/shelterguard-the-national-homelessness-risk-monitor"
title: "ShelterGuard: The National Homelessness Risk Monitor"
hackathon: "BatchHacks (Students Only; Open-Ended)"
organization: "Batch 09"
winner: true
words: 679
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# ShelterGuard: The National Homelessness Risk Monitor

> Turning reactive crisis management into proactive prevention.

[Devpost](https://devpost.com/software/shelterguard-the-national-homelessness-risk-monitor) · hackathon [[BatchHacks -Students Only- Open-Ended-]]

## Facets

**domain** [[civic_government]] [[finance_payments]] [[housing_homeless]] [[labor_employment]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** ngrok, numpy, pandas, plotly, python, scikit-learn, streamlit

## How they structured the write-up

- challenges we ran into
- inspiration: the economics of prevention
- what shelterguard does
- how i built it
- challenges we faced
- accomplishments i am proud of
- what is next for shelterguard

## Body

Challenges We Ran Into Inspiration: The Economics of Prevention In the UK, homelessness is often treated as an inevitability rather than a solvable data problem. Every year, thousands of families are evicted, costing taxpayers billions in emergency accommodation while causing long term social and economic harm. I started with a simple question: Why do we wait for a family to lose their home before we help them? The current system is fundamentally reactive . A family presents as homeless, and the local council spends approximately £30,000 per year on emergency B&B accommodation and crisis management. If that same family could be identified three months earlier , the cost of intervention through mediation, rent arrears assistance, or early support drops to approximately £2,400 . (Reference: Crisis.org, including wider taxpayer and healthcare costs.) The formula is: Impact = Cost of Reactive- Cost of Preventative I built ShelterGuard to provide that three month head start . ShelterGuard acts as a smoke detector for housing insecurity , helping politicians, councils, and NGOs allocate resources before a crisis occurs. Note: ShelterGuard is currently a functional prototype. While the trends and Volatility Matrix logic are statistically sound, the forecasting values are derived from linear regression models trained on historical data and should be treated as estimates for this hackathon demonstration. What ShelterGuard Does ShelterGuard is a geospatial predictive analytics dashboard that aggregates fragmented UK government datasets to forecast housing stress. 1. Geospatial Risk Mapping Visualises the entire UK, highlighting councils in Critical (Red) condition where unemployment and claimant trends are accelerating most rapidly. 2. The Volatility Matrix This is the core innovation. By plotting Historical Volatility against Forecasted Growth , ShelterGuard identifies Wildcard councils , areas that appear stable on the surface but are statistically fragile. 3. Economics of Prevention Analysis Correlates Local Housing Allowance (LHA) rates with claimant count data to reveal where the widening gap between rent support and real rental prices is creating structural housing failure. 4. Council Inspector A granular tool allowing MPs, councillors, or housing officers to drill into their specific local authority and view a three month predictive trend line . How I Built It This project was as much a data engineering challenge as a coding one. Data Pipeline Python and Pandas were used to ingest inconsistent government CSV files, including Statutory Homelessness flows and Universal Credit claimant data. A fail safe ingestion engine was built using Regex to dynamically locate columns, regardless of how government file headers changed between 2019 and 2025. Machine Learning Scikit Learn was used to train Linear Regression models for every local authority in the UK . Each model learns from historical flow data to produce rolling three month forecasts. Visualisation The frontend was built in Streamlit for rapid prototyping. Plotly was used for interactive scatter plots and heatmaps. Deployment The application is currently tunnelled using Ngrok . Challenges We Faced Data Fragmentation UK homelessness and welfare datasets change structure almost every year, requiring robust preprocessing and adaptive ingestion logic. Prototype Scope There is significantly more that could be built, but the project was intentionally constrained to a realistic, simple, and effective prototype suitable for a hackathon environment. Accomplishments I Am Proud Of I am particularly proud of the Volatility Matrix , located in the Structural Analysis tab. It successfully distinguishes: High Growth / Low Volatility areas, which represent predictable and steadily worsening conditions High Growth / High Volatility areas, which are statistically unstable and at risk of sudden crisis This distinction is critical for policymakers. Councils experiencing rapid homelessness growth while simultaneously absorbing rising Claimant Count pressures often require different funding and intervention strategies than structurally stable areas. What Is Next for ShelterGuard Conduct deeper statistical and econometric analysis beyond simple linear regression Explore more robust forecasting approaches such as gradient boosting and time series models Improve deployment stability beyond Ngrok so the application can persist without manual intervention Expand the analytical depth while continuing to develop core data engineering and modelling skills Note: I am new to GitHub repositories and am still learning best practices for structuring and uploading code. <div