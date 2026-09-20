---
slug: "ai-4-alzheimers"
url: "https://devpost.com/software/ai-4-alzheimers"
title: "EarlyBird"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 374
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "substrate/genomic_bio"
  - "substrate/structured_db"
---

# EarlyBird

> We achieved 71% accuracy detecting Alzheimer's using blood biomarkers and cognitive tests from the Bio-Hermes dataset, proving that cheap, accessible screening can replace expensive brain imaging.

[Devpost](https://devpost.com/software/ai-4-alzheimers) · hackathon [[AI 4 Alzheimer-s]]

## Facets

  <sub>weak: benchmark_measured, vision_ocr</sub>
**domain** [[elder_child_care]] [[health_clinical]] [[scientific_research]]
  <sub>weak: patient_family</sub>
**substrate** [[genomic_bio]] [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** ad-workbench-platform, gradient-boosting, jupyter-notebooks, numpy, pandas, pickle, python, random-forest, scikit-learn, xgboost

## Body

EarlyBird: Multimodal Alzheimer's Detection Achieving 71% Accuracy Using Novel Bio-Hermes-001 Dataset Background: While most Alzheimer's disease (AD) detection approaches rely on expensive MRI or PET imaging, we developed a multimodal machine learning pipeline using the novel Bio-Hermes-001 dataset, combining accessible biomarkers for democratized screening. Methods: We successfully integrated and processed seven data modalities from 1,005 patients in the GAP Bio-Hermes study on AD Workbench: blood-based biomarkers (151 features including Tau-217, Tau-181, GFAP, NFL, Amyloid-beta ratios), digital cognitive assessments, PET neuroimaging (325,787 files including 57,209 DICOM images), clinical records in SDTM format, proteomics, genomics, and demographics. Our pipeline handles complex clinical trial structures, performs SDTM-to-ML transformations, and extracts real diagnoses from medical history records (62.4% CN, 20.6% MCI, 17.0% AD). Results: Using Gradient Boosting with class balancing to address MCI under-representation, we achieved: 71.1% overall accuracy (3-class: CN/MCI/AD) 66.4% weighted F1 score Consistent performance across all disease stages, crucial for early MCI detection Successfully processed all 325,787 PET imaging files and integrated multimodal features Key Innovations: First implementation using Bio-Hermes-001 multimodal dataset instead of standard MRI Novel approach combining blood biomarkers with digital cognitive tests Balanced class sampling improving minority MCI detection (critical intervention window) Efficient handling of 57,209 DICOM files and complex SDTM clinical trial format Technical Implementation: XGBoost and Gradient Boosting models with hyperparameter optimization Manual oversampling with noise injection for class balance Stratified train-test splits maintaining class distributions Comprehensive validation framework with cross-validation Clinical Impact: Our 71% accuracy using primarily non-invasive tests (blood biomarkers, cognitive assessments) demonstrates that accessible, multimodal screening could replace expensive imaging for initial AD detection. Blood-based Tau-217 and digital cognitive scores proved highly predictive, offering a scalable screening approach. Model Deployment: Three serialized model files enable immediate deployment: alzheimer_finetuned_model.pkl (main Gradient Boosting model) alzheimer_imputer.pkl (missing value handling) alzheimer_feature_scaler.pkl (feature normalization) Future Directions: With additional optimization, ensemble methods and deep learning integration could push accuracy to 75-80%. The multimodal approach shows particular promise for early MCI detection, the critical window for intervention. Keywords: Alzheimer's disease, multimodal machine learning, Bio-Hermes-001, blood biomarkers, early detection, gradient boosting EarlyBird achieved 71% accuracy with novel multimodal approach - demonstrating viable alternative to expensive imaging-based detection for early Alzheimer's detection. Project Name: EarlyBird - "The early bird catches the diagnosis" Hack4Health 2025 Submission <div