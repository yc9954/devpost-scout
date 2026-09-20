---
slug: "x-yiqm81"
url: "https://devpost.com/software/x-yiqm81"
title: "HarmoniQ"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 693
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# HarmoniQ

> A command-center for T-Mobile product managers to anticipate customer needs. See sentiment in real time, predict outages, and allocate resources—all to strengthen every customer connection.

[Devpost](https://devpost.com/software/x-yiqm81) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
  <sub>weak: cross_origin_web</sub>
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** fastapi, flask, gemini, python, react, scikitlearn, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for harmoniq

## Body

logo Landing Page Login Page Dashboard brainstorming main features Inspiration The inspiration for HarmoniQ came from two main ideas of: maintaining network reliability and understanding customer emotions in real time. Telecommunications companies often struggle to bridge the gap between technical performance data and customer satisfaction metrics. Through our literature review and dataset exploration, we identified a research gap: most existing models treat network data and sentiment as separate entities. Our team wanted to create a unified intelligence layer that helps product managers and network engineers in detecting early issues, anticipating user sentiment changes, and acting before service degradation becomes customer frustration. What it does HarmoniQ is an AI-driven dashboard that integrates live network performance analytics, social sentiment streams, resource allocation and predictive insights into a single workspace. It continuously tracks live sentiment from online forums like Reddit & X and compares it with historical network performance data from Kaggle. Using trained Random Forest and Gradient Boosting models, HarmoniQ predicts the likelihood of service outages across different regions. When anomalies or high-risk events are detected, the system’s built-in Gemini AI assistant interprets the data, explains correlations (e.g., “latency spikes correlate with negative keyword surges”), and generates suggested next actions or alerts for the user. The platform computes a Customer Happiness Index (CHI) that reflects the overall satisfaction level in real time. The dashboard gives a human-readable layer to complex data: visualizing hotspots, predicting outages, generating insights, allocating resources and automatically assigning tasks for resolution. How we built it We designed HarmoniQ as a modular, scalable React system enhanced with AI automation. The frontend was developed with React, Vite, and TailwindCSS, creating an interface inspired by modern PM tools but adapted to the telecom domain. The backend integrates network data from Kaggle datasets and live user sentiment from Reddit & X APIs. The machine learning layer was developed and trained offline using Random Forest Classifiers (RFC) and Gradient Boosting Models. Both were trained on custom-curated datasets based on publicly available Kaggle samples and augmented with simulated regional outage data. We engineered feature sets that captured latency, packet loss, and frequency of user complaints across time intervals. On the frontend, HarmoniQ integrates with the Gemini API, which powers the AI assistant. Gemini generates contextual summaries and actionable insights based on live data, enabling users to understand the “why” behind the “what.” Each dashboard module has Network Health, Sentiment analysis, CHI, AI Insights, and Outage Predictor. Challenges we ran into The biggest challenge was data scarcity. Public datasets for real network outages and correlated sentiment data are extremely limited. Most available data lacked real-time or event-based granularity, making it difficult to train supervised models with meaningful features. We overcame this by synthesizing realistic outage events, combining Kaggle data with time-based sampling from historical logs. Another challenge was integrating Gemini AI effectively. We needed responses that were context-aware and data-grounded, not generic. Fine-tuning prompt structure and adding intermediate reasoning layers improved the assistant’s interpretability. Accomplishments that we're proud of We successfully developed an end-to-end AI dashboard that unifies live sentiment data and historical outage prediction. Our AI-assisted dashboard reasons, predicts, and helps product teams act intelligently. Our trained models achieved strong accuracy in forecasting outage risks across regions, proving the value of combining emotional and technical data. What we learned Through building HarmoniQ, we learned the practical difficulties of working with incomplete datasets, the value of feature engineering in telecommunications data, and the importance of interpretable AI in user-facing systems. We also realized that emotional context can be a powerful signal for operational health when integrated correctly. On the development side, we gained experience in modular React architecture, integrating secure authentication with Auth0, and it was our first time training RFC and Gradient models. What's next for HarmoniQ We plan to expand HarmoniQ by integrating real telecom API feeds and fine-tuning the outage prediction models on continuously updated datasets. Our next iteration will introduce alert automation where Gemini not only generates insights but triggers workflow integrations (like Slack or Jira) for immediate action. Ultimately, our goal is to evolve HarmoniQ into a full-scale AI command center that helps telecom operators and product teams with customer experience management. <div