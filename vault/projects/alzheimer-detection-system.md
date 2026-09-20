---
slug: "alzheimer-detection-system"
url: "https://devpost.com/software/alzheimer-detection-system"
title: "Alzheimer detection system"
hackathon: "Student Innovators Without Borders Hacks (Students; Open Ended)"
organization: "Batch 09"
winner: true
words: 315
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Alzheimer detection system

> "AI that thinks like a doctor, combining brain scans, handwriting, and clinical data to catch Alzheimer's years earlier"

[Devpost](https://devpost.com/software/alzheimer-detection-system) · hackathon [[Student Innovators Without Borders Hacks -Students- Open Ended-]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[genomic_bio]] [[geospatial]] [[structured_db]]

**stack** flet, google-colab, pandas, pillow, python, pytorch, scikit-learn, torchvision, tqm, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for alzheimer detection system

## Body

detection home Inspiration Late-stage Alzheimer's diagnosis is too late. Current single-test approaches (MRI-only or cognitive tests alone) miss the disease's multimodal complexity. Why Mixture-of-Experts? Neurologists don't average all evidence equally, they prioritise strong signals. When MRI shows severe atrophy, they weight it heavily. When handwriting reveals tremor, they trust that signal. MoE learns this adaptive reasoning: a gating network that asks "Which expert should I trust for THIS patient?" What it does Analyzes three biomarkers in <10 seconds: MRI scans - Structural brain atrophy Handwriting - 450-dim motor control features Clinical scores - MMSE, CDR, age, memory Results: 63.1% accuracy, beats single-modality by 5.3% How we built it Architecture: Sparse MoE with 3 experts (ResNet-18 for MRI, MLPs for handwriting/clinical) + gating network that learns dynamic routing Key Techniques: Temperature scaling (T=3.0) fixes overconfidence Feature normalization (handwriting was exploding to 2.7M) Top-k=2 sparse routing for efficiency Stack: PyTorch, Flet UI, 50 epochs, AdamW optimizer Challenges we ran into 1.Exploding features - Handwriting values hit 2.7M → Fixed with z-score normalization 100% overconfidence - Dangerous in healthcare → Temperature scaling Finding speech dataset that is open source ## Accomplishments that we're proud of 63.1% accuracy with interpretable expert routing 27% clinical threshold validated on real patients Safety-first: calibrated confidence, no dangerous overconfidence Real-time: <10 seconds on CPU ## What we learned MoE models really do better than simple ensembles: letting the system route information dynamically gave us about 1.9% better performance than just averaging everything. Good normalization beats adding more layers: fixing the way features are scaled made a much bigger difference (about 10×) than stacking extra layers. Calibration matters a lot: it’s far more useful to have a model that’s 60% confident and actually right than one that claims to be 100% confident but is wrong. What's next for Alzheimer detection system Validate on 1,000+ patients, mobile app deployment and biomarker expansion (CSF, genetics), <div