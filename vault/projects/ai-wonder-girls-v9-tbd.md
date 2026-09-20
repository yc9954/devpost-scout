---
slug: "ai-wonder-girls-v9-tbd"
url: "https://devpost.com/software/ai-wonder-girls-v9-tbd"
title: "Multimodality Cancer disease link prediction"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 529
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/structured_db"
---

# Multimodality Cancer disease link prediction

> Through the power of graphs and machine learning, we aim to uncover new disease links and help researchers better prepare for future pandemics or emerging diseases.

[Devpost](https://devpost.com/software/ai-wonder-girls-v9-tbd) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[elder_child_care]] [[health_clinical]] [[scientific_research]]
**user** [[patient_family]] [[researcher]]
**substrate** [[genomic_bio]] [[structured_db]]
  <sub>weak: financial_record</sub>

**stack** dgl, dglke, python, pytigergraph, pytorch, tigergraph, torchdrug

## How they structured the write-up

- problem statement
- impactfulness
- innovativeness
- ambitiousness
- applicability

## Body

Intro Team presentation Pipeline Multimodal Cancer Network TigerGraph Schema Lymphoma disease relationships About the project Title: Multimodality Cancer Graph Cancer disease link prediction. Problem Statement Many diseases are related to each other, and complications from a certain disease could cause another. Inspired by the Drug Repurposing Knowledge Graph (DRKG) example, we attempt to uncover new Disease-Disease interactions. We choose to focus on the Disease-Disease to leverage the power of graphs and discover complications or developments of diseases based on others. For example, COVID-19 has rapidly developed and generated several variations. Through the power of graphs and machine learning, we aim to uncover new disease links -- with the extension of this dataset with compounds and even more diseases-- and help researchers better prepare for future pandemics or emerging diseases. Impactfulness The project will have a direct impact on people's health. In fact, the combination of multiple chronic conditions (commonly termed multimorbidity and defined as the coexistence of two or more chronic health conditions), which is commonly found among aging and aged people, significantly increases the complexity of therapeutic management and treatment regimens for both patients and health professionals. Numerous diseases, such as coronary heart disease, diabetes, and chronic liver disease, are extremely common in the elderly and impose major modifications in their treatment. Our solution is actually helping health professionals to handle the combination of diseases and thus have a direct impact on the treatment of patients. Innovativeness The project is inspired by the Drug Repurposing Knowledge Graph (DRKG). We used the concept of Multi-modal Graph Learning for Disease Prediction on cancer data. The idea of using multiple modes (genes, protein, disease,...) helps refine, in a more detailed way, each element in a network. We believe that our project is only a small use case related to Cancer. It can go beyond that and become a healthcare component in the TigerGraph platform that supports different modes for healthcare data [genes, disease, side-effects, MRI, Clinical Data, Patient...]. Ambitiousness In our project, the multimodal cancer network has 5 vertexes: Chemical, Disease, Function, Gene, and Protein. We believe we can go beyond and add more modes (side-effects, clinical data...) It has 10 link types: Chemical-Chemical, Chemical-Protein, Disease-Chemical, Disease-Disease, Disease-Function, Disease-Gene, Function-Function, Gene-Protein, Protein-Function, and Protein-Protein. Our networks contain 13 476 nodes (357 Chemical Vertex, 1364 Protein Vertex, 8773 Disease Vertex, 500 Gene Vertex, and 2482 Function Vertex) and 537 685 edges. Applicability Each individual is unique thus providing personalized treatment for the patient is key! We believe that our project can be a Changemaker in the Digital Healthcare Ecosystem especially in our continent Africa. We also believe that our project can be generalized into a multimodal healthcare network and not only for Cancer. Challenges The main challenges were related to getting the right data and fitting it into the model. It would be interesting to have the Graph Machine Learning (GNN, GCN,...) component added to the TigerGraph platform. About the team Part of AI Wonder Girls, winner of 5 challenges; an all-women team with a broad tech background empowering ladies into AI careers one project at a time. Sara and Sofia participated in the TigerGraph challenge as AI Wonder Girls V9. <div