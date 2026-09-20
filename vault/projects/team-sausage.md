---
slug: "team-sausage"
url: "https://devpost.com/software/team-sausage"
title: "Team Sausage"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 448
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
---

# Team Sausage

> An explainable AI system that predicts Alzheimer’s disease by combining clinical data (XGBoost + SHAP) with CNN-based MRI analysis for accurate and trustworthy risk assessment.

[Devpost](https://devpost.com/software/team-sausage) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**domain** [[elder_child_care]] [[health_clinical]] [[supply_logistics]]
**user** [[clinician]] [[patient_family]]
**substrate** [[genomic_bio]] [[sensor_telemetry]]

**stack** cnn, ml, python, shap, tensorflow, xgboost

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for team sausage

## Body

Inspiration Alzheimer’s disease affects millions worldwide, yet early diagnosis remains challenging due to subtle symptoms and limited access to specialist assessments. We were inspired by the potential of artificial intelligence to assist clinicians by extracting meaningful patterns from both clinical data and brain imaging. Our goal was to build a system that is not only accurate, but also interpretable and trustworthy, aligning with the needs of real-world medical decision-making. What it does Our project predicts Alzheimer’s disease risk by combining two complementary data modalities. Using structured clinical and demographic data, we estimate disease risk with explainable machine learning models. In parallel, we analyze brain MRI scans using a convolutional neural network to capture imaging biomarkers associated with neurodegeneration. Together, these models provide both quantitative risk estimates and insights into the factors driving each prediction. How we built it We processed clinical data using standard preprocessing techniques and trained a logistic regression model as an interpretable baseline. We then applied XGBoost to capture non-linear relationships and feature interactions, using SHAP to explain both global and individual predictions. For imaging data, we decoded and normalized grayscale MRI scans and trained a CNN to automatically learn spatial features relevant to Alzheimer’s disease. We evaluated models using stratified validation and emphasized clinically meaningful metrics. The entire pipeline was developed collaboratively using Python-based machine learning frameworks. Challenges we ran into One major challenge was working with heterogeneous data types, requiring different preprocessing and modeling strategies for clinical and imaging data. Ensuring interpretability while maintaining strong predictive performance was another key challenge, particularly for complex models. We also had to carefully manage data imbalance and avoid overfitting given the limited size of medical datasets. Accomplishments that we're proud of We successfully built an end-to-end multimodal pipeline that integrates explainable clinical models with deep learning–based MRI analysis. We are particularly proud of incorporating interpretability techniques such as SHAP, which allowed us to connect model predictions to clinically meaningful features. Despite time constraints, we delivered a robust and extensible system suitable for real-world medical applications. What we learned Through this project, we gained hands-on experience working with medical data and learned the importance of transparency and validation in healthcare AI. We deepened our understanding of explainable AI techniques and their role in building trust with clinicians. Additionally, we learned how combining traditional machine learning with deep learning can yield complementary insights. What's next for Team Sausage Next, we aim to further integrate clinical and MRI modalities into a unified multimodal model, incorporate longitudinal patient data, and expand interpretability using techniques such as Grad-CAM for MRI visualization. We also plan to explore external validation on independent datasets and refine the system for potential clinical decision-support use. <div