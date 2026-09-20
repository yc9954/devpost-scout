---
slug: "neuroxplain-alzheimer-s-detection-via-spatial-radiomics"
url: "https://devpost.com/software/neuroxplain-alzheimer-s-detection-via-spatial-radiomics"
title: "NeuroXplain: Alzheimer’s Detection via Spatial Radiomics"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 757
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# NeuroXplain: Alzheimer’s Detection via Spatial Radiomics

> Fuses Genetics & MRI Radiomics to detect Alzheimer’s. Unlike CNNs, our XGBoost engine provides clinical rationale via SHAP, achieving 97.53% accuracy on blind external data.

[Devpost](https://devpost.com/software/neuroxplain-alzheimer-s-detection-via-spatial-radiomics) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**mechanism** [[deterministic_policy]]
  <sub>weak: benchmark_measured</sub>
**domain** [[accessibility]] [[elder_child_care]] [[health_clinical]]
  <sub>weak: scientific_research</sub>
**user** [[patient_family]]
  <sub>weak: clinician</sub>
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]
  <sub>weak: genomic_bio, sensor_telemetry</sub>

**stack** gradio, numpy, pandas, pillow, python, scikit-learn, shap, xgboost

## Body

Alzheimer’s Disease is one of the most pervasive medical challenges of our time, yet early diagnosis remains difficult. While modern AI, specifically Deep Learning (CNNs), has shown promise in analyzing MRI scans, it suffers from a critical flaw: The "Black Box" Problem. In a clinical setting, a doctor cannot simply trust an algorithm that outputs "Demented" without knowing why. A neural network hides its logic inside millions of opaque weights. This project was born from a desire to solve this Trust Gap. The goal was to build a diagnostic system that not only predicts risk with high accuracy but provides a transparent, mathematical rationale for every decision, fusing the biological certainty of Genetics with the anatomical evidence of MRI scans. What it does NeuroXplain is a Multi-Modal Clinical Decision Support System. It ingests two distinct data streams for a patient: Genomic Data: Analysis of 130 specific genetic markers (SNPs). MRI Imaging: Analysis of brain scans using Spatial Radiomics. The system processes this data to classify the patient into one of four diagnostic stages (Non-Demented, Very Mild, Mild, Moderate). It outputs a Weighted Confidence Score and generates SHAP (Shapley Additive Explanations) plots, visualizing exactly which genes and which specific brain regions (pixels) drove the diagnosis. How I built it Explainability was prioritized over raw complexity. Instead of using a standard Convolutional Neural Network (CNN), a Gradient Boosting (XGBoost) solution was architected. The Spatial Radiomics Pipeline To make MRI images interpretable by a decision tree model, a spatial feature extraction pipeline was engineered. Raw MRI scans were converted into grayscale, resized to a standardized grid, and flattened into feature vectors. Transformation Logic: Image (32x32) ➔ Vector (1,024 spatial features) This allows the model to analyze the pixel intensity distribution at specific anatomical coordinates (e.g., ventricular enlargement) rather than treating the image as a black box. Class-Weighted Training Medical data is inherently imbalanced (far more healthy patients than sick ones). To prevent the model from ignoring rare cases, an algorithmic sample weighting strategy was implemented during training. This calculates a penalty weight based on the total samples relative to the class count. This forced the model to prioritize minority classes, boosting precision from 0% to >90% for "Moderate Demented" cases. Multi-Modal Fusion The modalities were combined using a weighted probabilistic ensemble: Fusion Formula: Final Risk = (0.9 * Genetics Probability) + (0.1 * MRI Probability) A higher weight was assigned to genetics based on its deterministic nature in the validation set, using MRI as a spatial corroboration tool. Challenges I ran into The "Accuracy Trap": Initially, the MRI model achieved only 47% accuracy because it couldn't distinguish between "Very Mild" and "Non-Demented" patients. It was simply guessing the majority class. This was resolved by implementing the compute_sample_weight strategy described above, which penalized the model heavily for missing rare cases. Data Leakage Risks: In medical AI, if a patient appears in both the training and testing set, the results are invalid. A custom Audit Script (using np.intersect1d) was written to mathematically verify that the train/test splits were completely disjoint. External Validation Failure: Upon first testing the model on an external Kaggle dataset (6,400 images), accuracy plummeted. A Label Alignment Paradox was discovered—the numeric encodings in the training data didn't match the folder structure of the external data. Reverse-engineering this mapping restored accuracy to 97.53%. Accomplishments that I'm proud of 97.53% External Accuracy: The model was not just overfitted to training data. It was validated against 6,400 completely unseen MRI scans from an external source, proving real-world robustness. 100% Genetic Precision: The genetic classifier identified deterministic risk markers with perfect precision and recall. Visual Proof: Seeing the SHAP plots highlight the ventricles (center of the brain) as high-importance regions was a breakthrough moment—it proved the AI was looking at the right anatomy, not background noise. What I learned A key takeaway is that bigger isn't always better. While Deep Learning is popular, it is data-hungry and opaque. For this specific challenge, Spatial Radiomics with XGBoost proved to be statistically more robust, training faster, and generalizing better than many standard CNN approaches on similar dataset sizes. Data Hygiene (auditing for leakage) was found to be just as important as the model architecture itself. What's next for NeuroXplain 3D Volumetric Analysis: Moving from 2D slices to 3D voxel analysis to capture brain volume loss more accurately. Longitudinal Tracking: Adapting the model to track patient changes over time, predicting when a patient might transition from "Very Mild" to "Mild" dementia. Clinical API: Deploying the Gradio interface as a secure REST API for hospital integration. <div