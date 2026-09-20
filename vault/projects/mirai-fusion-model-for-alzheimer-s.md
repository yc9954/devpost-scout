---
slug: "mirai-fusion-model-for-alzheimer-s"
url: "https://devpost.com/software/mirai-fusion-model-for-alzheimer-s"
title: "MirAI 未来: Protecting Futures with Intelligence"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 556
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# MirAI 未来: Protecting Futures with Intelligence

> MirAI (未来): A Dual-Expert AI System for Early Alzheimer’s Detection through 3D Neuroimaging and Cognitive Analysis.

[Devpost](https://devpost.com/software/mirai-fusion-model-for-alzheimer-s) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**domain** [[elder_child_care]] [[health_clinical]]
  <sub>weak: scientific_research</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[genomic_bio]] [[sensor_telemetry]] [[structured_db]]

**stack** gradio, markdown, monai, nibabel, numpy, nvidia, oasis-3, pandas, pytorch, scikit-learn, tensorflow

## Body

Gradio powered ML Demo Integrated Diagnosis (MRI + clinical assessment) About~ Model card MirAI (未来): Protecting the Future of Brain Health 🌟 Inspiration Alzheimer’s Disease is a progressive journey that often remains hidden until significant damage is done. The inspiration for MirAI (Japanese for Future ) came from a critical gap in current diagnostic workflows: the disconnect between structural neuroimaging and cognitive behavioral testing. We wanted to build a system that doesn't just provide a diagnosis, but offers a consensus —combining what the brain looks like (MRI) with how the brain performs (Clinical scores). Our mission is to "Protect the Future" of patients by enabling earlier, more transparent AI-assisted detection. 🧠 How We Built MirAI We engineered a Parallel Dual-Expert System using the extensive OASIS-3 longitudinal dataset . The Structural Expert (3D MRI): We implemented a 3D DenseNet-121 architecture to process volumetric T1-weighted MRI scans (128*128*128). Unlike 2D models, this captures the spatial relationships of brain atrophy across the hippocampus and ventricles. The Functional Expert (Clinical MLP): A Multi-Layer Perceptron (MLP) was trained on UDS (Uniform Data Set) clinical records. It analyzes high-impact cognitive biomarkers including MMSE (Mini-Mental State Exam) scores and Clinical Dementia Rating (CDR) values. Data Alignment Pipeline: We developed a custom time-alignment algorithm to synchronize MRI scans with the closest clinical visit data, ensuring that the "structural" and "functional" snapshots of the patient matched in time. Clinician Dashboard: The interface was built using Gradio with a premium, scrollable UI/UX, designed to provide physicians with a side-by-side comparison of structural and cognitive findings. 🚀 Challenges We Faced Computational Complexity: Processing 3D volumes is resource-intensive. We had to optimize our pipeline for an Nvidia DGX-1 , utilizing mixed-precision training and efficient data loading to handle 128^3 voxels without memory overflows. Data Disparity: With over 8,000 clinical records but only 4,000 MRI scans, aligning the data without introducing "leakage" or bias required rigorous subject-level splitting. Architecture Pivot: Initially, we explored feature-level fusion, but since the access the GPU server was limited , a Parallel Architecture was superior. It allows doctors to see where the discrepancy lies if the models disagree, rather than being forced to trust a single "black box" score. 📚 What We Learned Medical Context Matters: We learned that high accuracy isn't enough; medical AI must be interpretable. By presenting two separate "expert reports," we provide a more robust decision-support tool. Data Engineering is 80% of the Work: Building the time-alignment scripts was just as important as the neural network architecture itself. 3D Volumetric Insight: We discovered how 3D convolutions can identify subtle atrophy patterns that are often missed in traditional 2D slice analysis. 📊 Performance Summary We achieved a balanced performance that leverages the strengths of both modalities: Clinical Accuracy: 87% MRI Structural Accuracy: 84% System Consensus Accuracy: ~90% 🔮 Future Enhancements: The MirAI Fusion Roadmap Our current parallel architecture is only the beginning. We are moving toward a Unified Multi-Modal Fusion Engine that will integrate: Metabolic Imaging (PET Scans): Incorporating Amyloid/FDG-PET data to detect metabolic changes before structural atrophy occurs. Fluid Biomarkers: Integrating CSF (Cerebrospinal Fluid) and blood-based protein markers (Tau/Amyloid-beta) for biochemical validation. Triple-Modality Fusion: Developing a late-fusion transformer architecture where MRI + PET + Biomarkers + Clinical Scores are weighted mathematically to provide a singular, high-confidence "Neuro-Health Index." MirAI (未来) — Utilizing AI to preserve the memories of tomorrow. <div