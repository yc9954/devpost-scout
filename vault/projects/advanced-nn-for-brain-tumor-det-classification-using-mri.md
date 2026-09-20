---
slug: "advanced-nn-for-brain-tumor-det-classification-using-mri"
url: "https://devpost.com/software/advanced-nn-for-brain-tumor-det-classification-using-mri"
title: "Advanced NN for Brain Tumor Det. & Classification Using MRI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 218
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Advanced NN for Brain Tumor Det. & Classification Using MRI

> AI-powered system for automatic brain tumor detection, segmentation, and classification from MRI scans with explainable results.

[Devpost](https://devpost.com/software/advanced-nn-for-brain-tumor-det-classification-using-mri) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]]
**substrate** [[geospatial]] [[web_dom]]

**stack** albumentations, cbam, css, efficientnet-b3, flask, grad-cam, html, matplotlib, numpy, opencv, python, pytorch, u-net

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- results
- future scope

## Body

Inspiration Brain tumor diagnosis using MRI is time-consuming and depends heavily on radiologists. We wanted to build an AI system that can assist doctors by providing fast, accurate, and explainable results. What it does Our system automatically: Detects brain tumors from MRI scans Segments tumor regions at pixel level Classifies tumors into glioma, meningioma, pituitary, or no tumor Generates Grad-CAM heatmaps for explainability Produces a structured diagnostic report How we built it We developed a multi-task deep learning model based on: U-Net architecture for segmentation EfficientNet-B3 encoder with transfer learning CBAM attention module to focus on relevant regions Preprocessing includes: CLAHE for contrast enhancement Data augmentation for robustness The system is deployed using: Flask backend HTML/CSS frontend Automated HTML report generation Challenges we ran into Limited and imbalanced medical datasets Accurate segmentation of small tumor regions Making the model interpretable (black-box problem) Integrating classification + segmentation in one pipeline What we learned Multi-task learning improves efficiency and performance Attention mechanisms significantly improve accuracy Explainability (Grad-CAM) is critical for medical AI trust End-to-end system integration is harder than model building Results Classification Accuracy: 93.2% Dice Score: 0.81 IoU: 0.72 The system successfully generates: Tumor segmentation maps Explainable heatmaps Diagnostic reports Future Scope Use larger medical datasets Improve real-time performance Add multi-modal MRI support Deploy as a clinical tool <div