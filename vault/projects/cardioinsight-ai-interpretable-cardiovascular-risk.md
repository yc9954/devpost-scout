---
slug: "cardioinsight-ai-interpretable-cardiovascular-risk"
url: "https://devpost.com/software/cardioinsight-ai-interpretable-cardiovascular-risk"
title: "CardioInsight AI – Interpretable Cardiovascular Risk"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 475
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
---

# CardioInsight AI – Interpretable Cardiovascular Risk

> An AI-powered cardiovascular risk prediction system that estimates 10-year CVD risk, explains key contributing factors, and shows how lifestyle or clinical improvements can reduce future risk.

[Devpost](https://devpost.com/software/cardioinsight-ai-interpretable-cardiovascular-risk) · hackathon [[Frostbyte Hackathon]]

## Facets

  <sub>weak: sensor_fusion</sub>
**domain** [[health_clinical]]
  <sub>weak: scientific_research</sub>
  <sub>weak: patient_family, researcher</sub>
  <sub>weak: structured_db</sub>

**stack** github., google-colab, jupyter, numpy, pandas, python, scikit-learn, shap, streamlit, xgboost

## Body

Inspiration Cardiovascular Disease (CVD) remains the leading cause of death worldwide, yet many people do not understand why they are at risk or what changes could actually reduce that risk. Most existing prediction tools provide only a risk score without explanation. This project was inspired by the need for an accessible, transparent, and actionable AI system that not only predicts cardiovascular risk but also helps users understand the driving factors behind it and how they can improve their health outcomes. What it does CardioInsight AI predicts a person’s 10-year cardiovascular disease risk and goes beyond traditional models by: Explaining which health factors contribute most to the predicted risk Showing how much the risk could reduce if certain factors (like blood pressure, BMI, cholesterol, or smoking) are improved Providing actionable insights instead of just a numerical score Supporting both full clinical data and limited feature inputs, making it usable in real-world scenarios The system also evaluates population-level risk using a real cardiovascular dataset and supports interactive individual risk analysis. How we built it We built CardioInsight AI using a two-model architecture: Model A (Clinical Model): Uses a comprehensive set of medical features for high-accuracy risk estimation in clinical or research settings. Model B (Lightweight Model): Uses a smaller, commonly available feature set to ensure usability when full medical data is unavailable. Both models are trained using XGBoost, optimized for class imbalance, and calibrated using probability calibration to ensure reliable risk estimates. To improve transparency and trust: We used SHAP (Explainable AI) to identify which features increase or decrease risk Implemented what-if simulations to estimate risk reduction if a modifiable factor improves Deployed the system as an interactive Streamlit web application Challenges we ran into Handling class imbalance in real medical datasets without sacrificing recall for high-risk patients Ensuring probability outputs are well-calibrated, not just accurate Making complex ML explanations understandable to non-technical users Designing medically safe what-if simulations without unrealistic assumptions Aligning different datasets (training vs evaluation) while maintaining consistency Accomplishments that we're proud of Built an explainable CVD risk prediction system, not just a black-box model Successfully implemented actionable risk-reduction insights Designed a dual-model approach for both clinical and real-world usability Deployed a fully working interactive web application Maintained reproducibility with clean notebooks and saved model artifacts What we learned In healthcare AI, interpretability is as important as accuracy Calibrated probabilities matter more than raw predictions in medical decision support Small, well-chosen features can still produce meaningful predictions Explainable AI greatly improves user trust and adoption Building for real-world constraints is just as important as model performance What's next for CardioInsight AI – Interpretable Cardiovascular Risk Clinical validation using larger and more diverse datasets Personalized lifestyle recommendations based on demographic profiles Integration with wearable or routine health data Improving fairness and bias analysis across population groups Exploring collaboration with healthcare researchers for real-world impact <div