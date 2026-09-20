---
slug: "proteognn"
url: "https://devpost.com/software/proteognn"
title: "ProteoGNN"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 344
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "substrate/genomic_bio"
---

# ProteoGNN

> A. Graph Neural Network Modeling of Tau Protein Misfolding in Alzheimer’s Disease and Related Tauopathies

[Devpost](https://devpost.com/software/proteognn) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[elder_child_care]] [[health_clinical]] [[scientific_research]]
  <sub>weak: finance_payments</sub>
**substrate** [[genomic_bio]]
  <sub>weak: sensor_telemetry, web_dom</sub>

**stack** alpha-fold, biopython, claude, geometric, github, jupyter, matplotlib, mdtraj, notebook, numpy, pandas, python, pytorch, rcsb-protein-data-bank

## Body

GNN Layers Architecture Diagram Bar chart + pie chart Combined ROC, PR curve, and confusion matrix Bar chart comparing ProteoGNN vs TANGO/PASTA/WALTZ General outlining of objectives The Alzheimer's series of diseases has a worldwide population of 55 million+. Irreversible damage to the brain from the Alzheimer's disease series occurs before the onset of symptoms. Thus, we set about creating a tool for identifying the regions of proteins that are at the highest probability of misfolding and aggregation (misfolded proteins lead to neurodegeneration) so that they can be identified prior to clinical decline, allowing for intervention prior to that time. Description of ProteoGNN Using the 3-D structure of the protein, ProteoGNN (a graph neural network) predicts the propensity to misfold at the residue level (aggregation risk) of amyloidogenic proteins by outputting a probability score for each amino acid indicating its propensity to aggregate. The model generates a 95.5% ROC-AUC and identifies known hotspot motifs (example: PHF6 from tau). How We Built ProteoGNN Using 80 cryo-EM fibril structures (from both Alzheimer's and other tauopathies), we created the foundation to develop ProteoGNN. The protein's structure can be depicted as a graph, whereby each residue is represented as a node and the spatial contacts between residues are represented as edges. Each of the residues includes up to 33 biophysical features to develop a cumulative understanding of each protein. The model consists of four graph convolutional layers and uses focal loss to compensate for class imbalance. ProteoGNN successfully outperforms the sequence-based molecular aggregation prediction methods at 92% sensitivity for identifying experimental validated aggregation regions. What We Learned and What Lies Ahead Structural characteristics of proteins (3-D structure) are critical to understanding and predicting the propensity of misfolding. Future iterations of ProteoGNN will be extended to additional receptors associated with other neurodegenerative disorders. Eventually we will expand the capability of ProteoGNN through the building of a web page that offers aggregation predictions for a variety of protein classes to be used by the broader community. The Video includes my reproducible notebook and the research paper is in additional info <div