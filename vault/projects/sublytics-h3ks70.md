---
slug: "sublytics-h3ks70"
url: "https://devpost.com/software/sublytics-h3ks70"
title: "Sublytics"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 772
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Sublytics

> Rescue failed clinical trials by discovering hidden responder subgroups using AI-powered analytics!

[Devpost](https://devpost.com/software/sublytics-h3ks70) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[genomic_bio]] [[geospatial]] [[structured_db]]

**stack** matplotlib, numpy, pandas, python, scikit, seaborn, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sublytics

## Body

Inspiration Clinical trials fail at an alarming rate—only 12% of drugs make it through Phase III. When a trial fails, pharmaceutical companies lose an average of $2.6 billion and years of research. But here's the hidden opportunity: these "failed" trials often contain hidden responder subgroups —specific patient populations that actually benefit from the treatment, but get lost in the overall negative results. We were inspired by real cases like Trastuzumab (Herceptin) , which initially failed in breast cancer trials until researchers discovered it worked brilliantly for patients with HER2+ tumors. That discovery turned a failed drug into a $7B blockbuster that saved millions of lives. Sublytics was born from a simple question: What if we could systematically find these hidden responders in every failed trial? What it does Sublytics is an AI-powered clinical trial analytics platform that discovers patient subgroups who respond to treatments in "failed" trials. Instead of abandoning a drug after negative results, researchers can: Upload trial data (demographics, biomarkers, outcomes) Train ML models to predict treatment response with explainable AI (SHAP) Discover subgroups using multi-feature combination analysis Identify responders through demographic + biomarker patterns Get AI-generated insights via Claude API explaining the clinical significance Key Features: Multi-feature subgroup discovery (2-way and 3-way combinations) SHAP-based explainability for feature importance Claude AI integration for natural language clinical insights Interactive visualizations (ROC curves, demographic breakdowns) Statistical rigor with Bonferroni correction and confidence intervals Synthetic dataset generator with ground-truth subgroups for validation How we built it Tech Stack: Frontend : Streamlit (interactive web app with modern UI) ML Pipeline : scikit-learn (Random Forest), SHAP (explainability) Data Processing : pandas, NumPy, scipy (statistical tests) Real-world Data : NHANES dataset (3,996 patients with biomarkers) AI Integration : Anthropic Claude API for clinical interpretation Visualization : matplotlib, seaborn Architecture: Data Layer : NHANES XPT file processing → cleaned trial dataset ML Layer : Hyperparameter-tuned Random Forest with class balancing Subgroup Discovery : Novel algorithm testing single features + 2-way/3-way combinations Statistical Validation : Chi-square tests, Wilson confidence intervals, multiple testing correction Explainability : SHAP TreeExplainer for feature importance + beeswarm plots AI Layer : Claude Sonnet integration for narrative insights Key Innovation : Most subgroup analysis tools only look at single features (e.g., "females" OR "age 60+"). We built a combination discovery engine that finds patterns like "Females aged 60-80 with HDL > 60"—the kind of multi-feature subgroups that exist in real biology. Challenges we ran into Sparse Subgroups : Finding statistically significant combinations with adequate sample sizes was hard. We had to balance between finding granular subgroups (high specificity) and maintaining statistical power (N ≥ 30). Multiple Testing Correction : Testing dozens of subgroups inflates false positive rates. Implementing Bonferroni correction was necessary but made significance harder to achieve—we had to add "promising subgroups" reporting to show clinically meaningful patterns even without strict significance. NHANES Data Complexity : Raw NHANES comes in SAS XPT format with cryptic variable names, missing values, and complex merge logic. Converting it into a clean clinical trial dataset required careful column mapping and imputation strategies. Explainability vs Accuracy Trade-off : We initially used XGBoost (higher AUC) but switched to Random Forest for better SHAP interpretability—clinicians need to understand why a subgroup responds, not just that it does. Real-time AI Integration : Streaming Claude API responses in Streamlit required careful state management to avoid re-running expensive computations on every interaction. Accomplishments that we're proud of End-to-end Pipeline : From raw XPT files → cleaned data → trained model → SHAP explanations → subgroup discovery → AI insights—all in an intuitive Streamlit interface. Explainable AI : SHAP visualizations show exactly which biomarkers drive predictions, making the black box transparent for clinicians. What we learned Technical: SHAP TreeExplainer is powerful but computationally expensive—sampling background data is crucial for speed Bonferroni correction is extremely conservative; FDR (False Discovery Rate) might be more appropriate for exploratory analysis Class imbalance (responders are rare) requires careful handling: balanced class weights + stratified splitting Clinical: Subgroup discovery is a double-edged sword: it can save drugs OR lead to dangerous false positives that harm patients The "file drawer problem" is real—companies bury negative trials, losing valuable subgroup signals Regulatory bodies (FDA) are increasingly open to post-hoc subgroup analyses if done rigorously Product: Researchers want transparency: showing warnings about multiple testing and overfitting builds trust AI explanations need to be specific and actionable, not generic Interactive visualizations (expandable sections, hover tooltips) are essential for complex medical data What's next for Sublytics Long-term (1-2 years): Phase IV Surveillance : Monitor post-approval drugs for safety signals in subpopulations Regulatory Pathway : Work with FDA to establish guidelines for AI-driven subgroup discoveries <div