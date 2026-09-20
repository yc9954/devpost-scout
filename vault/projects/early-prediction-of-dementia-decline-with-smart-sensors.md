---
slug: "early-prediction-of-dementia-decline-with-smart-sensors"
url: "https://devpost.com/software/early-prediction-of-dementia-decline-with-smart-sensors"
title: "Early Prediction of Dementia Decline with Smart Sensors"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 457
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Early Prediction of Dementia Decline with Smart Sensors

> 92% accurate machine-learning early-warning system that detects patterns in sleep, mobility, and vitals from passive smart-home sensors to predict adverse health events in dementia 14 days in advance.

[Devpost](https://devpost.com/software/early-prediction-of-dementia-decline-with-smart-sensors) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[elder_child_care]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[developer]] [[patient_family]] [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]]
  <sub>weak: document_pdf</sub>

**stack** colaboratory, matplotlib, numpy, pandas, python, scikit-learn, shap, xgboost

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what is next for early prediction of dementia decline with smart sensors

## Body

Note: The research paper PDF is in the "Try It Out" section, because Devpost is broken for me Inspiration Dementia often deteriorates rapidly between clinic visits, and caregivers may not notice early warning signs until a crisis occurs. We wanted to explore whether passive smart home sensors could detect behavioral changes associated with health decline, enabling caregivers and clinicians to intervene sooner. Our goal is to support safer independent living and a better quality of life for people living with dementia. What it does Our system uses AI to predict whether a person with dementia is at high risk of an adverse health event in the next 14 days. It analyzes activity, sleep, and physiological data collected from smart home devices and provides an early warning when rising risk is detected. Care teams could use this information to check in, review vital signs, or schedule earlier follow-ups. How we built it We used the TIHM open dataset, which contains real-world passive monitoring data from people living with dementia. We aggregated sensor streams into daily behavior profiles and created temporal features that capture temporal changes. We trained an XGBoost classifier with grouped evaluation by patient to avoid data leakage. Performance was evaluated using ROC and precision-recall metrics. SHAP explainability tools provided insight into which behavior changes drive rising risk. Challenges we ran into The dataset is complex with multiple sensors and different sampling rates. We had to engineer features that combine activity, sleep, and physiology into something a model could learn from. Class imbalance made high precision difficult, so we focused on high recall to avoid missing warning signs. Formatting the results into a research paper that still fit strict page limits was another challenge. Accomplishments that we are proud of We built an early warning system that predicts most high-risk days up to 2 weeks in advance. We achieved 92% recall at the optimal threshold while keeping false positives at an acceptable level. We also generated clear, interpretable visualizations to explain why the model makes each decision. What we learned We learned how trends in mobility, sleep, and physiology can reveal upcoming deterioration. We gained hands-on experience in working with real-world health data and understood the importance of an evaluation design that reflects clinical priorities. We also learned a lot about academic writing and scientific communication. What is next for Early Prediction of Dementia Decline with Smart Sensors Next, we want to test additional models and add calibration methods to reduce false alarms. We also plan to expand the evaluation to include per-patient analysis and multiple risk categories. Ultimately, we hope to collaborate with clinicians to explore how this type of system could fit into a genuine care pathway and help people remain safely at home. <div