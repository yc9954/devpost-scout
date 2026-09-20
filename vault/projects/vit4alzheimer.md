---
slug: "vit4alzheimer"
url: "https://devpost.com/software/vit4alzheimer"
title: "ViT4Alzheimers"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 656
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/privacy_tech"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ViT4Alzheimers

> Using Vision Transformers to achieve 94.5% accuracy in Alzheimer's detection from brain MRI scans, our solution handles class imbalance, trains in 50 mins, and provides reproducible coding environment

[Devpost](https://devpost.com/software/vit4alzheimer) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**mechanism** [[benchmark_measured]] [[privacy_tech]] [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]]
**substrate** [[structured_db]] [[video_visual]]

**stack** huggingface, python, pytorch, vision-transformers

## How they structured the write-up

- why this approach is unique and revolutionary
- how to use
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i’m proud of
- what i learned
- what’s next for vit4alzheimer

## Body

HuggingFace Model Card Training and Validation Graphs Training Logs Confusion Matrix for Predictions Why this approach is Unique and Revolutionary Vision Transformers are revolutionary because their global self-attention captures whole-brain structural patterns simultaneously, unlike CNNs’ local receptive fields, enabling superior modeling of diffuse neurodegeneration and robustness under extreme class imbalance in medical imaging. How to Use Upload the train.parquet and test.parquet files (provided by the hackathon organizing team) to Google Colab . Then, run the notebook cells sequentially , so no additional configuration required. Inspiration Alzheimer’s disease affects over 55 million people globally , yet early detection remains a major challenge due to subjective clinical assessments and limited access to expert neuroimaging interpretation. I was inspired to leverage Vision Transformers (ViTs) , which have demonstrated state-of-the-art performance in natural image recognition to automate brain MRI analysis . The most critical challenge was handling an extreme 26:1 class imbalance , where traditional CNN-based approaches tend to fail, making this an ideal opportunity to showcase ViT’s superiority in medical imaging . What It Does ViT4Alzheimer is an automated Alzheimer’s disease detection system that analyzes brain MRI scans and classifies disease stages with 94.53% accuracy . Key highlights: Handles extreme class imbalance (26:1 ratio) using weighted cross-entropy loss Achieves a perfect F1-score of 1.0 on the minority class , despite it representing only ~1% of the data Provides fast inference along with confidence scores for clinical decision support Designed to be deployment-ready for real-world hospital integration How I Built It I fine-tuned Google’s ViT-Large (304M parameters) by selectively unfreezing the last 6 transformer layers to enable medical domain adaptation. Core technical components: Weighted loss function with a 26.12× weight for the minority class Mixed-precision FP16 training combined with gradient accumulation to fit GPU memory constraints Cosine annealing learning rate scheduler for stable convergence The model was trained on 5,120 brain MRI scans using PyTorch . Challenges I Ran Into The severe 26:1 class imbalance initially caused the model to collapse into majority-class predictions Minority-class accuracy and F1-score were poor until applying 26.12× weighted loss , which ultimately achieved F1 = 1.0 T4 GPU memory limitations required careful optimization using FP16 mixed-precision and gradient accumulation Finding the right balance between model capacity and training time required systematic experimentation across three configurations , with the 6-layer unfreezing strategy proving optimal I experimented with data augmentation , but performance degraded, likely because medical MRI scans are highly sensitive to artificial transformations ➜ As a result, no data augmentation was used in the final submission Accomplishments I’m Proud Of Achieving perfect F1 = 1.0 on the minority class , with only 49 training samples (~1%) , which is rare in medical AI under extreme imbalance Outperforming ensemble CNN models using a single Vision Transformer Conducting a systematic 3-configuration study , producing actionable insights for real-world deployment Releasing the model as a fully open-source solution on HuggingFace , enabling adoption by resource-constrained hospitals worldwide What I Learned Vision Transformers’ global self-attention is fundamentally superior to CNNs’ local receptive fields for capturing whole-brain atrophy patterns Weighted loss functions are essential for extreme class-imbalance scenarios in medical datasets Transfer learning from 14M+ natural images significantly reduces overfitting, even with relatively small medical datasets ( ~5,000 samples ) Architectural decisions (e.g., how many layers to unfreeze) have a larger impact than brute-force scaling What’s Next for ViT4Alzheimer Immediate goals Revisit carefully designed medical data augmentation strategies to further boost performance Deploy a pilot study at a partner hospital for prospective clinical validation Mid-term scaling Expand the dataset via multi-center collaborations Target: 50,000+ MRI scans from 10+ institutions Technical roadmap Multimodal fusion (T1/T2 MRI + PET + clinical metadata) Attention visualization for clinician interpretability Federated learning for privacy-preserving collaboration (GDPR/HIPAA compliant) Long-term vision Longitudinal disease progression modeling (1 to 5 year predictions) Experiment with ViT-Huge (632M parameters) for potential +1 to 2% accuracy gains Expand the framework to other neurodegenerative diseases such as Parkinson’s and Huntington’s disease <div