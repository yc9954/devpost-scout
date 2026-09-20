---
slug: "predictra"
url: "https://devpost.com/software/predictra"
title: "Predictra"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 872
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Predictra

> AI Industrial maintenance and failure prediction for any machine using anomaly-based RUL modelling from learned normal behavior.

[Devpost](https://devpost.com/software/predictra) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[climate_energy]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** html, javascript, mongodb, node.js, numpy, pandas, python, render, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for predictra

## Body

Dashboard for the User RUL Forecasting Sample (n = 10) Inspiration Every year, manufacturing companies lose over $50 billion to unplanned downtime. Shockingly, 70% of manufacturers still rely on outdated spreadsheets or manual logs instead of predictive maintenance. This isn’t just a big-company problem. Smaller factories, especially in North America and Europe, often don’t have access to scalable, affordable predictive tools, and they’re hit the hardest. Last year, the average maintenance response time across small and medium-sized factories exceeded 60 seconds, even when the signs of failure were evident. That’s simply, just too slow when every second means lost productivity, safety risks, and dollars down the drain. Manufacturing facilities majorly resort to pre-emptive maintenance tend to "over-schedule" maintenance checks for their machines, more than the machines actually require. This creates unoptimized maintenance schedules, where extra costs can be removed by schedulling more strategically provided data about when their machines will fail - instead of guessing when they will fail. It is evident that for increasing operational efficiency, neglecting the abundance of data provided from the labyrinth of sensors, becomes futile. If factory owners were to quantitatively understand and digest the state of their own , machine's health at the click of a button, any time of day; how sensor analytics contribute to machine degradation over time; capitalize on the goldmine of data accessible by control system architecture standards like SCADA; make use of the historical, time-series features; and custom-tailor their analyses to their factories own machines under their own setups and production lines, they can step away from reactive, pre-emptive maintenance strategies, to cost-effective, time-saving, data-driven strategies, getting one step closer to Industry 6.0 . What it does That’s why we built Predictra: a plug-and-play predictive maintenance platform that enables any manufacturer, regardless of size or budget, to detect anomalies and anticipate equipment failures in advance. Predictra helps factories: Upload raw machine data (time-series logs, spreadsheets, sensor readings etc.) Automatically convert it into structured sequences Detect early signs of degradation via adaptive AI Estimate Remaining Useful Life ( RUL ) of each machine Take timely, actionable steps before failure occurs All this is visualized in a clean, intuitive dashboard with live health metrics for every machine. How we built it We started by gathering and studying industry-grade datasets such as NASA’s CMAPSS dataset and CARE-to-Compare wind turbine SCADA logs. From there, we created a modular ML pipeline with the following components: Data Enrichment Engine: Automatically parses and transforms messy inputs (CSVs, logs, even PDFs) into usable structured data Standardizes time series across machines and sensor types LSTM Autoencoder: Trained on just a few days of healthy data Learns machine-specific behavior patterns Detects deviations in real time using reconstruction error Risk Score Normalization: Every timestamp receives an anomaly score (0 = normal, 1 = highly abnormal) No need for pre-labeled failure data Conservative RUL Estimation: Translates anomaly trends into underpredicted RUL bands (e.g. <5 days = urgent) Web Dashboard (Frontend handled separately): Presents current machine health status, risk alerts, and upcoming predicted failures We used Python, TensorFlow/Keras, Pandas, and joblib for the backend. Models are saved, versioned, and optimized for fast predictions. Challenges we ran into No unified format for sensor data across machines, solved with an extensible schema and preprocessing pipeline. Lack of labeled failure examples, solved by building models trained on normal-only data and flagging deviations. Many small manufacturers don’t have IoT pipelines, so we built compatibility with static uploads like CSVs and PDFs. Estimating Remaining Useful Life without ground truth, addressed with Bayesian-style conservative extrapolations based on anomaly scores. Accomplishments that we're proud of Built an end-to-end system in less than 36 hours that goes from raw CSV upload to actionable RUL predictions Successfully parsed real SCADA logs and verified model behavior on simulated failures Generated per-timestamp anomaly scores normalized to [0, 1] for use in dashboards Benchmarked LSTM Autoencoder against NASA CMAPSS testbeds Initiated conversations with real SMEs (small manufacturers) to explore pilot testing Generalized the models to make them much more accessible and cheaper solutions for companies What we learned You don’t need massive historical failure data to make useful predictions, you just need to model what “healthy” looks like. Conservative predictions are more trusted by factory operators than overconfident ML guesses. Making AI accessible starts with good UX and good defaults, not complicated dashboards. Web scraping for machine-specific metadata could enhance model initialization across industries. What's next for Predictra Build out the web scraping + autoencoding pipeline to enrich low-data environments Partner with 3-5 SMEs to deploy pilot versions and collect real-world performance data + collaboration with Local Enterprises for market experimentation and testing Fine-tune anomaly thresholds using contextual time-series trends (e.g. seasonality, workload) Expand support to real-time sensor streams and legacy machine connectors Raise pre-seed capital or grants to support early-stage deployment and integrations Leverage web-scraping of further relevant, available data of inputted machine ID's online for aggregation and data availability Experiment with synthetic data to create more robust Training-Set (extrapolations of SCADA, or web data) Incorporate multimodality within data pipeline: (e.g microvibration analysis using video streaming, anomaly recognition within sound output of machinery/audio data) Predictra is more than a project, it’s the beginning of real predictive intelligence for the companies that need it most. <div