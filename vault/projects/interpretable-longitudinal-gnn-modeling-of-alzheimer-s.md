---
slug: "interpretable-longitudinal-gnn-modeling-of-alzheimer-s"
url: "https://devpost.com/software/interpretable-longitudinal-gnn-modeling-of-alzheimer-s"
title: "Interpretable Longitudinal GNN Modeling of Alzheimer’s"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 532
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# Interpretable Longitudinal GNN Modeling of Alzheimer’s

> This is a code that longitudinally models Alzheimer's disease progression for more clinical relevance while incorporating powerful interpretability features.

[Devpost](https://devpost.com/software/interpretable-longitudinal-gnn-modeling-of-alzheimer-s) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** alzheimer's, gnn, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges + accomplishments
- what's next for interpretable longitudinal gnn modeling of alzheimer’s

## Body

Inspiration Recently, I have a growing interest in understanding the brain and how this marvelous, complex biological system can be understood through modeling. A few months ago, I started researching neurodegenerative diseases and found work that framed Alzheimer’s disease as a network-level disorder instead of just isolated issues. However, there was little work on modeling disease progression over time, especially using graph-based and continuous-time methods. This is something that would push work further than standard Euclidean representations, but most importantly, something I can contribute towards. Overall, I am motivated by my interest in machine learning and neurological disease, hoping to apply my computational skills to improve the quality of life for individuals like my close family friend and mentor, who is currently living with this disease. What it does Building upon current approaches, this project models individual brains as time-evolving graphs derived from resting-state fMRI. Brain regions are represented as nodes, which have two primary parts: A node’s edges encode dynamic functional connectivity, while its features incorporate neurophysiological descriptors of regional activity and synchrony. To capture the deteriorating connectivity across time, the model extends graph convolution with continuous-time graph neural ordinary differential equations. This enables a smooth modeling of longitudinal network evolution. Interpretability is included through attention-based edge weighting and node-level attribution, allowing identification of disease-relevant regions and subnetworks consistent with known AD pathology. The model will be evaluated using multi-site neuroimaging cohorts with cross-site validation and comparisons against non-graph baselines. This work advances graph neural networks toward mechanistic and interpretable modeling of Alzheimer’s disease progression. How we built it To model Alzheimer’s disease as a progressive network disorder, this project portrays each subject as a longitudinal sequence of functional brain networks evolving. For each clinical session, resting-state fMRI (rs-fMRI) time series are extracted from regions of interest (ROIs). Pairwise Pearson correlations between ROI signals are computed to construct functional connectivity matrices at each time point. Each time point is represented as a weighted, undirected graph, where nodes correspond to ROIs and edges encode the strength of functional connectivity. The novelty is that they are organized into subject-specific temporal trajectories that preserve the evolution of network structure across clinical visits. This formulation explicitly captures progressive connectivity disruption rather than simply static representations. To model continuous-time network evolution under irregular longitudinal sampling, the model uses graph neural ordinary differential equations (GNN-ODEs) in the learning process. This allows the latent trajectories to be modeled smoothly, accommodating missing visits and variable inter-scan intervals common in longitudinal neuroimaging. Disease-relevant predictions are produced from time-dependent graph representations without collapsing temporal information into flat vectors. The model is trained end-to-end in a supervised setting using gradient-based optimization. The architectural choices are guided by stability, interpretability, and biological plausibility. Challenges + Accomplishments Challenges: This took forever. I had to do so much debugging 😭😭😭 🥀. Accomplishments: I learned so much. This was such a great experience, and I can confidently say I now understand how to use PyTorch. What's next for Interpretable Longitudinal GNN Modeling of Alzheimer’s All planned extensions are detailed in the accompanying design document and will be completed before major research competitions (ISEF and JSHS) and the conclusion of the Hack for Health mentorship: https://docs.google.com/document/d/1cy0_JPhTfHO2ONlpRYeG0yKOuKpWstInn_SPx_0A3I0/ <div