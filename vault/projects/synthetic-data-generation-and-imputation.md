---
slug: "synthetic-data-generation-and-imputation"
url: "https://devpost.com/software/synthetic-data-generation-and-imputation"
title: "Synthetic Data Generation and Imputation"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 410
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
---

# Synthetic Data Generation and Imputation

> We generate realistic virtual patients and impute missing data to simulate, optimize, and de-risk clinical trials, accelerating drug discovery while ensuring data integrity.

[Devpost](https://devpost.com/software/synthetic-data-generation-and-imputation) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[patient_family]] [[researcher]]
**substrate** [[genomic_bio]] [[sensor_telemetry]]

**stack** numpy, pandas, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for synthetic data generation and imputation

## Body

Inspiration Clinical trials often fail or get delayed due to incomplete data, small sample sizes, and biased analyses. We wanted to build a system that could fill in missing information and generate realistic virtual patients, helping researchers design, simulate, and analyze trials more effectively before they even begin. What it does Our architecture is based off of deep generative models such as GAIN and conditional GANs to impute missing clinical data while preserving correlation and variance. It also generates synthetic patient cohorts for pre-trial simulation and power analysis and enables privacy-safe data sharing for multi-site collaboration. The result is complete, realistic datasets ready for modeling, analysis, and regulatory submission. How we built it We built the system by training our architecture de-identified trial data to learn complex feature distributions. We integrated a synthetic data generation module that samples new patient profiles conditioned on biomarkers, demographics, and treatment arms. To ensure data quality, we developed validation metrics including Wasserstein distance, correlation preservation, and RMSE to compare imputed versus real distributions. We analyzed our design in 3 different environments, including MCAR, MAR, and MNAR missingness patterns. Challenges we ran into One of the main challenges we faced was handling high-dimensional data. Balancing statistical fidelity with privacy when generating synthetic cohorts required careful design. We also needed to calibrate uncertainty in imputations so results remained biologically plausible and ensure model interpretability for regulatory transparency. Accomplishments that we're proud of We are proud of achieving high correlation preservation and low deviation in key variable distributions. Our synthetic distributions accurately align to our generated data, showing the feasibility of synthetic data for pre-trial simulation. In addition, we're proud of designing and implementing our own ML architecture in a research backed environment. What we learned We learned how to merge statistical imputation and deep generative modeling for clinical reliability. We also learned the importance of uncertainty quantification and model explainability in healthcare AI. Most importantly, we realized that synthetic data is not just a replacement for real data but a simulation tool for smarter, faster trial design. What's next for Synthetic Data Generation and Imputation Next, we plan to integrate multi-modal data, including electronic health records, imaging, and genomics, for richer synthetic cohorts. We aim to add reinforcement learning modules to dynamically optimize trial designs and develop open-source APIs and datasets under an MIT license for the research community. We also hope to collaborate with biotech and pharmaceutical teams to pilot real-world pre-trial simulation workflows. <div