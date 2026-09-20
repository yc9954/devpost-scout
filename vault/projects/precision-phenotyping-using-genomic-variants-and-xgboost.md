---
slug: "precision-phenotyping-using-genomic-variants-and-xgboost"
url: "https://devpost.com/software/precision-phenotyping-using-genomic-variants-and-xgboost"
title: "Precision Phenotyping using Genomic Variants and XGBoost"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 496
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Precision Phenotyping using Genomic Variants and XGBoost

> We built an Explainable AI model (98.9% accuracy) that uses simple genetic variants to predict 9 distinct Alzheimer's phenotypes, replacing expensive brain scans with accessible genomic screening.

[Devpost](https://devpost.com/software/precision-phenotyping-using-genomic-variants-and-xgboost) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**mechanism** [[benchmark_measured]] [[vision_ocr]]
**domain** [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[genomic_bio]] [[geospatial]] [[structured_db]]

**stack** google-collab, python, shap, xgboost

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for precision phenotyping using genomic variants and xgboost

## Body

Google Collab Inspiration Alzheimer's is not a single disease—it’s a complex spectrum. Currently, patients undergo expensive PET scans or painful spinal taps just to know which type of cognitive risk they face. We asked: What if a simple blood test could tell you the same thing? Inspired by the concept of "Precision Medicine," we wanted to build an AI that doesn't just say "You have Alzheimer's," but explains exactly which biological pathway is at risk, democratizing access to early diagnosis. What it does Our project is a Genomic Risk Classifier. It takes a patient's genetic profile (specifically Single Nucleotide Polymorphisms, or SNPs) and predicts their specific Alzheimer's phenotype. Instead of a vague "High Risk" label, our AI categorizes patients into 9 actionable groups, including: Pure AD (Alzheimer's Disease) Vascular/ADRD (Related Dementias) Cognitive Decline (Early stage risk) Neuropathological Risk (Brain tissue damage) This allows doctors to tailor treatments to the specific cause of the disease rather than just the symptoms. How we built it We utilized the Alzheimer’s Disease Variant Portal (ADVP) dataset (advp.hg38), a high-confidence catalog of genetic associations. Data Engineering: We rigorously cleaned the data to prevent leakage (removing P-values) and used One-Hot Encoding to translate biological sequences into machine-readable vectors. Modeling: We trained an XGBoost Classifier, chosen for its superior performance on structured biological data. Explainability: We integrated SHAP (SHapley Additive exPlanations) to visualize exactly which genes drove the predictions, ensuring our "Black Box" AI is transparent and clinically trustworthy. Challenges we ran into The "Data Leakage" Trap: Our initial model achieved 100% accuracy, which seemed too good to be true. We discovered the dataset included statistical columns (like P-values) that gave away the answer. We had to rebuild our pipeline to strip these out and train on only the biological variants. Class Imbalance: Some phenotypes (like "Neuropathology") were rare compared to "AD." We used stratified splitting and F1-score evaluation to ensure the model didn't ignore these critical minority cases. Accomplishments that we're proud of Achieving 98.90% Accuracy on a 9-class classification problem. Successfully mapping specific genetic loci (like APOE variants) to their correct phenotypes, proving our model learned real biology. Building a fully reproducible pipeline in Google Colab that any researcher can run in seconds. What we learned We learned that "More Data" isn't always better; "Clean Data" is. Understanding the biological context of our features (genes vs. statistical artifacts) was more important than the complexity of the model itself. We also learned how to use SHAP to bridge the gap between computer science and medicine, making complex AI decisions understandable to doctors. What's next for Precision Phenotyping using Genomic Variants and XGBoost Validation: Testing our model on raw, whole-genome sequencing data (e.g., from the UK Biobank) to prove its robustnes in the real world. Expansion: Adding more demographic data to ensure the tool is accurate for non-European populations. App Integration: Building a simple web interface where a user can upload their "23andMe" raw data file and get a personalized risk report. <div