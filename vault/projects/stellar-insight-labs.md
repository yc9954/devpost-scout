---
slug: "stellar-insight-labs"
url: "https://devpost.com/software/stellar-insight-labs"
title: "Stellar Insight Labs"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 518
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "user/researcher"
  - "substrate/structured_db"
---

# Stellar Insight Labs

> AI that sees beyond the stars — accelerating exoplanet discovery through explainable machine learning.

[Devpost](https://devpost.com/software/stellar-insight-labs) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[media_journalism]]
  <sub>weak: education, scientific_research, supply_logistics, transportation</sub>
**user** [[researcher]]
  <sub>weak: educator_student</sub>
**substrate** [[structured_db]]
  <sub>weak: sensor_telemetry</sub>

**stack** built-with-languages:-python, config, fastapi-libraries:-scikit-learn, github-other-tools:-jupyter-notebook, javascript-frameworks:-react, json-based, lightgbm, lightkurve-frontend-tools:-tailwindcss, mast-lightkurve-api-platforms-&-hosting:-netlify-(frontend), matplotlib, pandas, render-(backend-/-model-api)-version-control-&-collaboration:-git, tensorflow, typescript

## Body

AI EXOPLANET DETECTION SYSTEM ARCHITECTURE DASHBOARD GRAPHS Inspiration We’ve always been fascinated by how astronomers detect planets orbiting distant stars by observing subtle changes in brightness. While exploring NASA’s exoplanet archives, we realized that despite the availability of massive datasets, the process of identifying true planetary signals remains slow and heavily manual. This inspired us to build an AI-driven system that combines astrophysical methods with machine learning to make exoplanet detection faster, transparent, and scientifically interpretable. What it does Stellar Insight Labs is an end-to-end pipeline that detects potential exoplanets using a mix of classical analysis and modern machine learning. It automatically processes light curve data, identifies possible transits, and classifies them using multiple AI models. The system also provides an explainability layer that highlights which astrophysical features most influenced each prediction, ensuring that results are not only accurate but also trustworthy. How we built it We collected and preprocessed light curve data from the NASA Exoplanet Archive using Lightkurve and Pandas. Key astrophysical parameters such as transit depth, duration, signal-to-noise ratio, and flux variations were extracted as input features. We trained and compared several models—Logistic Regression, Random Forest, Gradient Boosting, XGBoost, and a shallow Neural Network—on a dataset of over 8,000 confirmed and candidate exoplanets. The frontend interface was developed using React, TypeScript, and TailwindCSS, while the backend was built with FastAPI in Python to serve the trained models through an API. The system is hosted on Vercel and Hugging Face Spaces for quick, web-based inference. Challenges we ran into Handling noisy and incomplete photometric data was one of the biggest challenges. Many light curves contained false dips or irregular sampling, making preprocessing complex. We also had to ensure that the models did not rely on non-physical metadata, forcing us to design a “scientific mode” that uses only astrophysically meaningful features. Resource limits during deployment required optimization of both model size and inference time. Accomplishments that we're proud of We successfully built a working hybrid pipeline that integrates real NASA data with machine learning and explainable AI. Our visualization dashboard bridges the gap between data scientists and astronomers, offering a transparent way to interpret model outputs. We’re proud that the project goes beyond automation—it promotes responsible and interpretable use of AI in scientific research. What we learned We learned how to apply AI principles to real scientific problems, where understanding the reasoning behind a prediction is as important as achieving high accuracy. The project deepened our knowledge of astrophysical data, signal processing, and the challenges of generalizing ML models in a research setting. It also reinforced the importance of clean architecture and readable documentation in building complex technical systems. What's next for Stellar Insight Labs Next, we aim to integrate more datasets from missions like TESS and JWST and experiment with deep learning architectures such as LSTMs and CNNs for raw light curve analysis. We also plan to open-source the project, publish the dataset curation pipeline, and create a public interface where students and researchers can explore and validate exoplanet candidates interactively. Ultimately, our goal is to make planetary discovery more accessible, explainable, and scientifically reliable. <div