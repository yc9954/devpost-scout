---
slug: "arrhythmia-detection"
url: "https://devpost.com/software/arrhythmia-detection"
title: "Arrhythmia Detection"
hackathon: "IEEE OC Computer Society  AI Dev Hack 2025"
organization: "IEEE Orange County Computer Society"
winner: true
words: 504
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/legal_professional"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Arrhythmia Detection

> Arrhythmia is a problem with the heart rhythm affecting mainly older adults (6-20 million US adults). Our application uses machine learning to detect abnormal heart rhythms and record their metrics.

[Devpost](https://devpost.com/software/arrhythmia-detection) · hackathon [[IEEE OC Computer Society  AI Dev Hack 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[elder_child_care]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[legal_professional]] [[patient_family]] [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** cnn, git, github, google-colab, python, random-forest, wfdb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for arrhythmia detection

## Body

Inspiration We were inspired to do this project because my grandmother passed from heart complications which run in my family (Egan). Ting-Yu being a good friend wanted to help tackle this issue by using machine learning to examine and record the arrhythmia for alerting patients and doctors of the abnormalities that occur. What it does Our project detects arrhythmias in ECG signals using two complementary approaches: A baseline machine learning model (Random Forest) trained on extracted ECG features such as heart rate, HRV, QRS width, and R-wave amplitude. A deep 1D Convolutional Neural Network (CNN) trained directly on raw ECG windows. Users can upload either a feature dataset or raw ECG signals to our Streamlit demo app, which: Predicts Normal vs. Abnormal heart rhythms (AFib + PVC). Provides metrics (F1, AUROC, false alarms/hour). Shows alerts if multiple abnormal windows are detected consecutively. This allows both clinicians and researchers to screen arrhythmias faster, combining interpretability (features) with accuracy (CNN). How we built it Data: MIT-BIH Arrhythmia Database + additional annotated ECGs. Preprocessing: Band-pass filtering (0.5–40 Hz), segmentation into 10s windows, R-peak detection. Feature extraction: NeuroKit2 pipeline to compute HRV and ECG morphology features. Baseline ML: Random Forest (scikit-learn) with binary classification. Deep Learning: 1D CNN (PyTorch) for raw signal classification. Evaluation: F1, AUROC, confusion matrices, false alarms/hour. App: Streamlit + Plotly visualizations with configurable thresholds. Collaboration: Integrated partner’s Colab experimentation into the pipeline. Challenges we ran into Feature alignment: Our feature extraction produced lowercase names while scikit-learn expected original casing → fixed by standardizing all names to lowercase. Model storage/loading: Needed to bundle features + model together for reproducibility in the app. Class imbalance: Abnormal rhythms were underrepresented in some datasets so we switched to a binary model instead of a multi-weighted model. Integration: Combining baseline ML and deep CNN into one Streamlit app without breaking file upload logic. Collaboration: Merging Colab outputs with local Python/Streamlit code and handling Git conflicts. ## Accomplishments that we're proud of Built a complete end-to-end pipeline: preprocessing → feature extraction → training → evaluation → app demo. Achieved 91% accuracy (Random Forest) and strong F1 scores, with the CNN showing even better abnormal recall. Designed a real-time alert mechanism for consecutive abnormal detections. Created a user-friendly app for judges and clinicians to test with their own ECG CSV files. Successfully collaborated across environments (Colab + local Python). ## What we learned How to balance interpretability vs. accuracy in biomedical ML (features vs. deep learning). The importance of consistent data preprocessing (naming, scaling, alignment). Using Streamlit + Plotly for rapid biomedical visualization. Handling GitHub collaboration with multiple contributors and resolving conflicts. Metrics like false alarms per hour are critical for clinical usability. What's next for Arrhythmia Detection Expand from binary → multi-class arrhythmia detection (AFib, PVC, other). Train on larger datasets (AFDB, PTB-XL) for robustness. Incorporate transfer learning architectures (ResNet, LSTM, Transformer). Deploy as a cloud API or mobile app for remote monitoring. Explore integration with wearables (smartwatches, ECG patches). Collaborate with healthcare professionals for validation in clinical settings. <div