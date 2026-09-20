---
slug: "netcraft-ai"
url: "https://devpost.com/software/netcraft-ai"
title: "NetCraft AI"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 685
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/labor_employment"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# NetCraft AI

> Analyze your data smarter with NetCraft AI — neural networks, clustering, Random Forest, and forecasting, all in a secure lightweight client-side browser app.

[Devpost](https://devpost.com/software/netcraft-ai) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]]
**domain** [[civic_government]] [[labor_employment]]
**user** [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** css, react-18, tailwind, typescript-5.2+

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for netcraft ai

## Body

Landing page Time Series Forecasting Artificial Neural Network Clustering Random Forest Results Summary Inspiration As a scientist, I often see colleagues struggling with data analysis tasks such as neural networks, time-series forecasting, or clustering. Many of them are not familiar with statistics or programming, making it difficult to use tools like R or Python. While MS Excel works for simple statistics, advanced packages like SAS or SPSS require expensive licenses and steep learning curves. The idea behind NetCraft AI was clear: 👉 Deliver machine learning capabilities through a simple, intuitive, client-side web application so that anyone can perform robust neural network prediction, clustering, or time-series forecasting in just a few clicks. What it does 🧠 Neural Network Predictor Custom multilayer perceptron in TypeScript Regression & classification support Configurable architecture (layers, neurons, activations) Real-time training progress (loss curves, epoch tracking) Evaluation metrics: MSE, MAE, R², accuracy, confusion matrix Built-in normalization and preprocessing Model serialization for persistence & deployment 🌳 Random Forest Classifier Decision tree ensembles with bagging Feature importance via impurity decrease Out-of-bag validation (OOB scoring) Regression & classification support Configurable parameters (trees, depth, sampling ratios, seed) Batch predictions with confidence scores Flexible feature sampling strategies 📈 Time Series Forecasting Moving Average with adjustable window sizes Exponential Smoothing (simple & Holt’s method) Linear trend & polynomial regression forecasting Metrics: MAE, RMSE, MAPE, R² Confidence intervals & uncertainty quantification Automatic frequency detection & preprocessing Train/test split for validation 🎯 Clustering Analysis K-means clustering (with elbow method & k-means++ init) Self-Organizing Maps (SOM) with multiple topologies Interactive U-Matrix visualization Metrics: silhouette score, inertia, topographic error PCA for dimensionality reduction Built-in normalization & standardization 📊 Data Management CSV upload with drag-and-drop & validation Auto column type detection (numeric, categorical, datetime) Preprocessing for time-series gaps & validation Data preview with stats & column selection Demo datasets (Iris, Sales, Temperature series) Data export to CSV 🎨 Modern UI/UX Responsive Tailwind CSS design, mobile-ready Smooth Framer Motion animations Accessibility-first with ARIA support Dark/light/system themes Professional dashboard layout with sidebar nav Interactive Chart.js visualizations Loading states & progress indicators 🌍 Internationalization (i18n) Bilingual UI (English & Ukrainian, full coverage) Lazy loading of translations for performance Preserves technical terms (e.g., RMSE, Random Forest) Locale-aware formatting for dates/numbers Accessibility announcements for language switch 💾 Export & Persistence Save/load models as JSON Export predictions, clusters, forecasts, feature importance to CSV LocalStorage project state with migration support Reports in JSON with metadata Export charts as images 🔄 Data Migration & Compatibility Backward compatibility & graceful fallbacks Seamless data preservation during updates Status tracking & error handling Safe cleanup of old keys How we built it Vibes → skeleton app, QA tests, targeted improvements Steering → steering docs & roadmap Specs → rebranding, UI design, added ML models, bilingual support Hooks → auto docs update & cleanup after testing Tech stack → React 18, TypeScript 5.2+, Tailwind CSS 3.3+ Challenges we ran into Daily/monthly request limit errors Kiro freezing on commands like npm run dev Occasional infinite loops during error fixing Misinterpretations of prompts causing incorrect builds Pre-revert, difficult to roll back bad changes Accomplishments we’re proud of Built a fully functioning client-side ML platform with almost no manual coding Implemented advanced ML workflows in a short timeframe Delivered bilingual support with smooth UI/UX What we learned How to build a web application from scratch with an AI coding assistant Effective use of Kiro features (vibes, specs, hooks, steering) Prompt engineering with Claude Sonnet 4.0 What’s next for NetCraft AI Version 1.2 (Q3-Q4 2025) New forecasting algorithms: ARIMA, SARIMA, Prophet More clustering: DBSCAN, Hierarchical, Gaussian Mixture Advanced neural nets (CNNs for images, RNN/LSTM for sequences) Automated benchmarking & model comparison framework Enhanced visualizations with D3.js Hyperparameter optimization (grid/random search) Model interpretability (SHAP, feature attribution) Version 1.3 (Q4 2025) Web Workers for background processing Advanced preprocessing & feature engineering Real-time model monitoring More languages (Spanish, French, German) Cloud deployment & API endpoints Improved mobile responsiveness Version 2.0 (2026) Real-time streaming (WebSockets) AutoML for automated model tuning Advanced ensembles (stacking, blending, voting) Integration with TensorFlow.js / ML5.js User accounts & project sharing Collaboration tools Cloud-native deployment (Docker, Kubernetes, serverless) <div