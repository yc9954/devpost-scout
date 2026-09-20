---
slug: "rescuerx"
url: "https://devpost.com/software/rescuerx"
title: "RescueRX"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 671
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/legal_professional"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# RescueRX

> How many drugs have been shelved that could save lives for diseases they were never tested on? We use AI to find drugs abandoned for business reasons & pinpoint diseases they're best suited to fight.

[Devpost](https://devpost.com/software/rescuerx) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[human_in_the_loop]] [[multi_agent]] [[retrieval_grounding]]
**domain** [[finance_payments]] [[health_clinical]] [[legal_justice]] [[scientific_research]]
**user** [[clinician]] [[legal_professional]] [[patient_family]] [[researcher]]
**substrate** [[genomic_bio]] [[geospatial]] [[structured_db]]

**stack** knowledge-graph, machine-learning, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rescuerx

## Body

Inspiration Baricitinib. It's an arthritis pill. Costs about $70 a month. In 2020, an AI system figured out (in 48 hours) that this drug could treat COVID-19. It went through an emergency trial. It reduced deaths by 38%. The FDA fully approved it. But here's the thing: Baricitinib had been sitting in pharmacies for YEARS before anyone made that connection. How many other drugs are sitting on shelves right now that could save lives for diseases they were never tested on? We built the system that finds them. What it does RescueRX is a multi-agent AI system that uncovers pre-existing drugs that could treat new diseases. Given a disease, we mine “unsuccessful” late-stage clinical trials to surface promising drugs that were shelved for non-scientific reasons, then produce a ranked set of repurposing opportunities with evidence. How we built it RescueRX runs a parallel team of 9 specialized agents across 3 layers, where each agent works together to solve the drug repurposing question. Agent 1: Knowledge Graph Discovery Performs graph-based biological plausibility modeling using a large-scale heterogeneous biomedical knowledge graph: 97,000+ entities 5.87M typed relationships 107 interaction categories Uses custom neural relational embeddings (trained on GPU infrastructure) to estimate drug–disease association likelihoods via rotations in 200 dimensional embedding space. Enables latent pathway inference across complex multi-hop biological interactions and produces the initial candidate pool. Once a high-confidence candidate pool is established, the remaining agents execute concurrently as independent validation modules. Agent 2: Trial Scanner Ingests and classifies 500,000+ ClinicalTrials.gov trials, focusing on Phase 2 / Phase 3 terminations caused by non-scientific reasons (e.g., sponsor bankruptcy, enrollment failure, epidemic-related disruption). Implements a hybrid classification pipeline: Deterministic rule-based filtering Contextual intent inference Produces three labels: Rescuable Non-Rescuable Ambiguous Agent 3: FAERS Inverse Signal Performs pharmacoepidemiological signal analysis over the FDA’s FAERS database. Computes inverse reporting odds ratios (ROR < 1) to identify statistically significant protective signals (reverse-signal mining), leveraging real-world patient safety data to uncover population-scale therapeutic correlations. Agent 4: Literature Review While the Knowledge Graph Agent can explain that there is a correlation, the Literature Review Agent is used to determine WHY the correlation exists. Executes retrieval-augmented literature synthesis via the Perplexity Sonar Research Agent, querying 2.3M PubMed-indexed publications Extracts evidence across four dimensions: Mechanistic rationale Prior clinical validation Regulatory trajectory Recent translational developments All outputs are citation-linked to prevent hallucination and ensure traceability. Agent 5: Molecular Similarity Performs cheminformatics validation using: 2048-bit Morgan fingerprints Tanimoto similarity scoring Quantifies structural similarity between candidate compounds and FDA-approved therapeutics, leveraging the similarity-property principle to estimate shared target engagement potential. Runs via high-throughput, vectorized computation for molecular-level plausibility assessment. Agent 6: Orchestrator + Safety Arbitration Aggregates outputs across agents and enforces a strict safety override protocol. Cross-validates: Contraindications Adverse event frequencies Black-box warnings Automatically excludes any candidate with historical safety concerns or positive risk signals in FAERS, ensuring safety constraints supersede predictive optimism. Agents 7–9: Adversarial Court Agent 7 (Advocate): constructs the strongest possible case for repurposing viability. Agent 8 (Skeptic): performs systematic critique: identifying statistical weaknesses, cross-agent inconsistencies, and evidence gaps. Agent 9 (Judge): synthesizes both arguments into a calibrated final verdict with a transparent reasoning chain. This adversarial architecture reduces confirmation bias, improves calibration, and transforms predictive scoring into defensible scientific argumentation. Challenges we ran into Orchestrator complexity! Stitching outputs from multiple agents into a cohesive, readable final verdict required robust output contracts and formatting logic. Scale + heterogeneity of bioclinical data! Normalizing, cleaning, selecting meaningful biological features, and deciding what signals to trust vs. ignore. Accomplishments that we're proud of Built an end-to-end multi-agent system that turns messy biomedical data into actionable ranked hypotheses. What we learned We learned a lot about making multiple agents work together, and even more about how the whole process of drug repurposing worked! What's next for RescueRX Adding more data to the knowledge graph to incorporate more drugs and diseases Expand RescueRX to model drug combinations instead of only mapping single-drug impact. Add human-in-the-loop feedback so clinicians/researchers can correct mappings and teach the system over time. <div