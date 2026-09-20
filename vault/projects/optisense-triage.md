---
slug: "optisense-triage"
url: "https://devpost.com/software/optisense-triage"
title: "OptiSense Triage"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 725
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# OptiSense Triage

> Transforming Emergency Care with AI — delivering faster, more accurate triage decisions, better patient outcomes, and smarter resource allocation.

[Devpost](https://devpost.com/software/optisense-triage) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[structural_withholding]]
**domain** [[health_clinical]] [[transportation]]
**user** [[clinician]] [[frontline_worker]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]]

**stack** fastapi, gemini, javascript, mimic-iii, numpy, pandas, python, react, scikit-learn, tailwind-css, vite, xgboost

## How they structured the write-up

- our inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for optisense triage

## Body

Patient Assessment Form Real-time triage scoring with explainable clinical signals Live patient prioritization and resource visibility across the ER Our Inspiration Emergency departments are among the most time-critical environments in healthcare, yet triage - the decision of who needs urgent care - is still performed entirely manually. Studies show misclassification rates of 30–40% in busy ERs. Every under-triage is a life at risk; every over-triage wastes scarce resources. We were struck by a simple question: if a nurse has to simultaneously assess dozens of patients under extreme cognitive load, why isn't there an AI second opinion? That question became OptiSense Triage . What it does OptiSense Triage is a real-time AI decision support tool for ER nurses. When a patient arrives, the nurse inputs five vitals (heart rate, blood pressure, SpO₂, temperature, respiratory rate), a short plain-text chief complaint, and basic history. Within a few seconds, the system returns an ESI Level 1–5 severity score along with a plain-English explanation of the top three clinical risk drivers and ordered next steps. The system also displays a live bed allocation map and a severity-sorted patient queue on the dashboard, giving the entire care team a real-time risk profile of the department at a glance. It does not replace the nurse's judgment - it gives them a reliable, data-grounded second opinion. How we built it We built OptiSense Triage in two layers. The predictive layer is a gradient boosting classifier (XGBoost) trained on the MIMIC-III clinical database — a publicly available dataset of de-identified records from over 40,000 real ICU admissions at Beth Israel Deaconess Medical Center. We engineered features from raw vitals and mapped historical outcomes to ESI severity labels to produce a model served via a FastAPI Python backend. The explainability layer uses the Google Gemini API to translate the model's feature importances into plain-English clinical reasoning that a nurse can act on immediately. The frontend is a React + Tailwind dashboard. Challenges we ran into The hardest challenge was bridging the gap between model accuracy and clinical trust. A high AUC score means little if a nurse can't understand or verify the model's reasoning — so designing the Gemini explainability pipeline to produce concise, jargon-free output that felt natural to a clinical audience required significant prompt engineering and iteration. A second challenge was was the limited size of the dataset which made training a little difficult and structure of the labeled dataset we could construct from MIMIC-III. MIMIC-III doesn't ship with pre-assigned ESI scores, so we had to derive severity labels from clinical outcome proxies (ICU admission urgency, length of stay, intervention codes), which involved careful validation to avoid introducing labeling bias. Accomplishments that we're proud of We're most proud of the explainability layer. Clinical AI tools routinely produce black-box predictions that clinicians can't audit or trust. Getting Gemini to reliably surface the top three risk drivers in plain clinical language - consistently was a genuine technical and UX achievement. We're also proud of the end-to-end architecture: from raw MIMIC-III data ingestion through feature engineering, model training, API serving, and a real-time dashboard - all built during the hackathon. The stateless, HIPAA-ready design means OptiSense Triage isn't just a demo; it's a system that could enter a real clinical pilot with minimal rework. What we learned We learned that in clinical AI, explainability is not a nice-to-have - it is the product. Without it, accuracy is irrelevant because the clinician has no basis for trusting or overriding the model. This shaped every architectural decision we made. We also learned that real-world medical datasets require far more domain knowledge to use correctly than their documentation suggests. Deriving meaningful triage labels from MIMIC-III outcome data forced us to think carefully about the difference between model performance on a benchmark and actual clinical utility. That gap is where most AI healthcare projects fail, and navigating it was the most valuable thing we did. What's next for OptiSense Triage The immediate next steps are to expand and clean the training dataset to improve model reliability across all ESI levels, refine the Gemini explainability prompts based on feedback from actual nurses, and build a more robust frontend with proper authentication. From there, we'd look to validate the model's predictions against real triage decisions and, if the results hold up, explore a small pilot with a willing clinical partner. <div