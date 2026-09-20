---
slug: "risklens-ad"
url: "https://devpost.com/software/risklens-ad"
title: "RiskLens-AD"
hackathon: "AI 4 Alzheimer's"
organization: "Hack4Health"
winner: true
words: 981
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# RiskLens-AD

> An interpretable Alzheimer’s risk stratification system that combines cognitive scores and age-adjusted brain atrophy to explicitly surface uncertainty and support safer early screening.

[Devpost](https://devpost.com/software/risklens-ad) · hackathon [[AI 4 Alzheimer-s]]

## Facets

**domain** [[elder_child_care]] [[health_clinical]] [[immigration_refugee]] [[scientific_research]] [[security_privacy]] [[supply_logistics]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]

**stack** colab, matplotlib, numpy, pandas, python, scikit-learn, seaborn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for risklens-ad

## Body

Patient-Level Risk Landscape Clinical Safety Filter via Risk Stratification Inspiration Alzheimer’s disease develops silently over many years, with biological and cognitive changes appearing long before a definitive diagnosis is possible. While recent AI systems report impressive accuracy for Alzheimer’s detection, most of them treat the problem as a hard classification task—forcing a binary decision even when the evidence is ambiguous. In real clinical practice, uncertainty is not a failure; it is expected. Physicians routinely distinguish between patients who are clearly healthy, clearly high risk, and those who require monitoring rather than immediate intervention. However, many existing AI models do not communicate this uncertainty explicitly, which can lead to overconfident errors or false reassurance. RiskLens-AD was inspired by this gap between how AI systems make predictions and how clinicians reason about risk. Instead of asking only “Is this patient demented?”, we asked a different question: how can AI support early Alzheimer’s screening in a way that is transparent, uncertainty-aware, and clinically responsible? What It Does RiskLens-AD is an interpretable machine learning system for early Alzheimer’s risk assessment. Rather than producing a single diagnostic label, the system stratifies patients into three clinically meaningful risk bands: confident low risk, confident high risk, and uncertain cases requiring monitoring. The model integrates cognitive performance, demographic context, and age-adjusted brain structure to estimate risk probabilities. These probabilities are then translated into risk bands that explicitly acknowledge ambiguity in early-stage cases, aligning model behavior with real-world clinical workflows. In addition to individual risk estimates, RiskLens-AD provides patient-level visualizations that place individuals in a cognition–brain atrophy space, allowing clinicians to see how cognitive decline and structural changes jointly influence risk. How we built it RiskLens-AD was built as a fully reproducible machine learning pipeline using the OASIS clinical dataset. We focused on clinically meaningful variables that are commonly available in real-world settings, including cognitive scores (MMSE, CDR), demographic information (age and education), and normalized whole brain volume (nWBV). To isolate pathological neurodegeneration from normal aging effects, we engineered an age-adjusted brain atrophy score by modeling expected brain volume as a function of age and measuring deviations from this baseline. We also incorporated cognitive reserve by including education level, enabling the model to reason about mismatches between cognition and structural brain health. We intentionally selected logistic regression as the core model to prioritize transparency and auditability. All features were standardized prior to training, and predictions were generated as calibrated probabilities rather than hard labels. These probabilities were then mapped into three clinically interpretable risk bands: confident low risk, uncertain / needs monitoring, and confident high risk. The entire workflow is implemented in a single Google Colab notebook to ensure reproducibility and ease of review. Challenges we ran into One of the primary challenges was handling uncertainty in early-stage Alzheimer’s cases. Cognitive decline and brain atrophy do not always progress in a synchronized manner, which makes borderline cases difficult to classify confidently using standard binary models. Another challenge was separating pathological brain atrophy from normal age-related changes. Raw brain volume decreases naturally with age, and without proper adjustment this can lead to misleading risk estimates. Designing an age-adjusted atrophy measure that preserved clinical meaning while remaining simple and interpretable required careful feature engineering. Finally, balancing model simplicity with clinical usefulness was a key challenge. While more complex models could potentially achieve higher accuracy, they often sacrifice transparency and auditability. Ensuring that the system remained interpretable, reproducible, and suitable for clinical reasoning—rather than becoming a black-box predictor—guided many design decisions. Accomplishments that we're proud of We successfully built a transparent and reproducible Alzheimer’s risk assessment system that explicitly communicates uncertainty rather than hiding it behind binary predictions. By reframing early detection as a risk stratification problem, RiskLens-AD provides clinically meaningful outputs that align more closely with real-world decision-making. A key accomplishment is the integration of age-adjusted brain atrophy and cognitive reserve into an interpretable modeling framework. This allowed the system to identify cognitively vulnerable patients whose risk may not be explained by normal aging alone. We are also proud of the patient-level visualizations that place individuals in a cognition–brain atrophy space and clearly distinguish confident low-risk, uncertain, and high-risk cases. Together with population-level risk band analysis, this demonstrates a safety-aware approach to early Alzheimer’s screening that prioritizes responsible use over raw accuracy. What we learned Building RiskLens-AD highlighted that in healthcare AI, interpretability and caution are as important as predictive performance. A model that produces a single confident label can be misleading in early-stage Alzheimer’s, where clinical signals are often subtle and ambiguous. We learned that explicitly modeling uncertainty improves the usefulness of AI systems in medical contexts. By allowing the model to express uncertainty through risk bands, rather than forcing a binary decision, the system better reflects real clinical reasoning and supports safer downstream decisions. This project also reinforced the value of simple, well-justified models. Interpretable approaches such as logistic regression, combined with domain-informed feature engineering, can provide meaningful clinical insight without relying on opaque architectures. Clear reasoning, transparent assumptions, and reproducibility proved more impactful than incremental gains in accuracy. What's next for RiskLens-AD Future work can extend RiskLens-AD in several meaningful directions. Incorporating longitudinal patient data would allow the system to model changes in cognition and brain structure over time, supporting progression monitoring rather than single-visit assessment. External validation on independent cohorts would further strengthen confidence in the system’s generalizability. Additional uncertainty-aware techniques, such as probabilistic calibration or Bayesian extensions, could refine risk band thresholds and improve reliability in borderline cases. The framework can also be expanded to include other routinely available clinical variables, enabling richer risk context without sacrificing interpretability. While RiskLens-AD is not intended as a diagnostic tool, it demonstrates how transparent, uncertainty-aware machine learning can support early Alzheimer’s screening in a clinically responsible manner. The core insight remains that trustworthy AI in healthcare must prioritize clear reasoning, explicit uncertainty, and patient-level understanding over raw predictive performance. <div