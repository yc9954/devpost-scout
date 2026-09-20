---
slug: "trustecg"
url: "https://devpost.com/software/trustecg"
title: "TrustECG"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 549
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# TrustECG

> Explainable AI for 12-lead ECG classification

[Devpost](https://devpost.com/software/trustecg) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[patient_family]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** matplotlib, numpy, pandas, plotly, python, pytorch, pytorch-lightning, scikit-learn, scipy, seaborn, streamlit, wfdb-physionet

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trustecg
- team information

## Body

Detail ExplainableECGNet Architecture for Multi-label ECG Classification High-Level ExplainableECGNet Architecture Class Distribution Sample 12-Lead ECG Sample 12-Lead ECG Co-Occurrence Training Curves Roc Curves AUROC Per Class Confusion Matrices Lead Importance Inspiration Every year, millions of ECGs are recorded in hospitals worldwide. Many are read by overworked doctors who might miss subtle patterns, especially during night shifts or when juggling dozens of patients. We wanted to build an AI assistant that acts as a second pair of eyes, but here's the catch: doctors won't trust a black box. They need to see why the AI made its decision. That's what drove us to build TrustECG, an explainable system that doesn't just predict, it shows its reasoning. What it does TrustECG analyzes 12-lead ECG recordings and detects 5 cardiac conditions simultaneously: Normal rhythm, Myocardial Infarction (heart attack), ST/T Changes, Conduction Disturbances, and Hypertrophy. What sets it apart is the built-in explainability. Through attention visualization, doctors can see exactly which ECG leads and time segments the model focused on. How we built it We used the PTB-XL dataset , the largest publicly available ECG dataset with 21,801 clinical recordings verified by cardiologists. Our model, ExplainableECGNet, processes each of the 12 leads through residual CNN blocks, then applies temporal attention (which time points matter?) and lead attention (which leads matter?). We trained using PyTorch Lightning with sqrt-scaled class weights to handle imbalanced data. The preprocessing pipeline applies bandpass filtering (0.5-40 Hz) and z-score normalization. Challenges we ran into Class imbalance was a big one. Hypertrophy appears in only 10% of recordings, while Normal ECGs make up 43%. Full inverse frequency weighting made the model overfit to rare classes. We solved this with square-root scaling. Another challenge was multi-label evaluation. Patients often have multiple conditions, so we couldn't use simple accuracy metrics. We switched to per-class AUROC and macro-averaged F1. Accomplishments that we're proud of We achieved 92.1% validation AUROC and 91.2% test AUROC across 5 cardiac conditions. More importantly, the attention mechanisms provide genuine explainability, not post-hoc explanations bolted on afterwards. The lead attention patterns actually make clinical sense: for MI detection, the model focuses on leads II, III, aVF (inferior leads) and V1-V4 (anterior leads), exactly where cardiologists look. What we learned Building explainability into the architecture from the start is better than adding it later. The attention weights give us interpretable features without any additional computation at inference time. We also learned that class weighting requires careful tuning, more weight isn't always better. On the engineering side, we learned the importance of matching preprocessing between training and inference. A 5-line preprocessing bug caused hours of debugging because predictions were completely wrong despite the model being correctly trained. What's next for TrustECG We want to optimize per-class thresholds instead of using 0.5 for everything. HYP detection (84.9% AUROC) could be improved with threshold tuning or additional features specific to hypertrophy patterns. We're also planning external validation on other ECG datasets like CPSC 2018 to test generalization. Longer term, we'd like to add more explainability methods (SHAP, Grad-CAM), deploy on edge devices for resource-limited clinics, and integrate clinician feedback to improve the model over time through active learning. Team Information Kaleemullah Younas Role: Full-Stack AI Engineer - GITHUB Muhammad Umer Role: Web Developer & Devops - GITHUB Contact Primary Contact Email: EMAIL <div