---
slug: "team-re-admit"
url: "https://devpost.com/software/team-re-admit"
title: "Team Re-Admit"
hackathon: "Predictive AI In Healthcare with FHIR®"
organization: "Darena Solutions"
winner: true
words: 477
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Team Re-Admit

> Our Re-Admit App integrates CDS Hooks → SMART on FHIR in MeldRx to identify high-risk patients, alert care teams, and reduce preventable readmissions—seamless, real-time, and EHR-integrated.

[Devpost](https://devpost.com/software/team-re-admit) · hackathon [[Predictive AI In Healthcare with FHIR-]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]] [[medical_record]] [[sensor_telemetry]] [[structured_db]]
  <sub>weak: financial_record</sub>

**stack** angular.js, fhir, meldrx, node.js, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for team re-admit
- closing statement

## Body

Patient Profile with LACE and PAM scores ML Model Feature Importance Chart Population Level Landing Page Team Re-Admit: Hackathon Submission Inspiration Hospital readmissions are a major challenge in the U.S. healthcare system, negatively impacting patient outcomes and costing hospitals billions annually. Nearly 20% of patients discharged from hospitals are readmitted within 30 days, leading to unnecessary strain on resources. With an average readmission cost exceeding $15,000 per case, our goal was to develop an AI-powered solution that helps predict and prevent readmissions, improving patient care and reducing costs. What It Does Our Readmission Predictor is an advanced clinical decision-support tool that seamlessly integrates into the MeldRx ecosystem. It helps clinicians and care managers identify high-risk patients in real-time, allowing for proactive intervention. Key features include: CDS Hooks Integration: Real-time alerts for readmission risk. SMART on FHIR App: A detailed analysis of patient demographics and risk factors. Population-Level Dashboard: Enables hospital administrators to track readmission trends across patient populations. Automated Task Assignment: Uses LLM-generated recommendations for intervention planning. How We Built It Model: We trained a weighted XGBoost model on the MIMIC-IV dataset , utilizing over 546,028 patient records with key predictive features including previous visits, ICU stays, elective admissions, lab counts, and medication counts. Performance Metrics: AUC: 0.69 Precision: 0.37 True Positive Rate: 60.6% Minimized False Negatives to ensure fewer high-risk patients are missed. Infrastructure: FHIR R4 Bundle API: Standardized data exchange. CDS Hooks: Embedded decision support. PowerBI Integration: Interactive dashboards for data-driven decisions. Challenges We Ran Into Data Balancing: Early iterations suffered from class imbalance, making predictions skewed. FHIR Integration: Mapping EHR data to FHIR resources was complex. Minimizing False Negatives: Ensuring that high-risk patients were not misclassified required significant tuning. Scaling Predictions: Optimizing inference time while handling large datasets efficiently. Accomplishments That We're Proud Of Successfully integrated real-time AI-driven alerts into MeldRx . Achieved 60.6% true positive rate , reducing undetected high-risk cases. Developed an intuitive population-level dashboard for care coordination. Enabled automated intervention planning using LLM-based recommendations . What We Learned Feature Importance Matters: ICU stays and previous visits emerged as top predictors. FHIR Adoption is Crucial: Standardizing healthcare data leads to better interoperability. Iterative Model Tuning is Key: Reducing false negatives required ongoing adjustments to hyperparameters and weighting strategies. Clinician-Friendly Design: Ensuring UI/UX aligns with hospital workflows is critical for adoption. What's Next for Team Re-Admit LLM-Driven Interventions: Automating patient-specific care plans based on risk factors. Geospatial & Temporal Analysis: Incorporating social determinants of health (SDoH) for deeper insights. EHR Vendor Expansion: Extending our integration beyond MeldRx. Deployment & Pilots: Testing in real-world hospital settings to measure impact and refine predictions. Closing Statement Thank you for reviewing our project! Team Re-Admit is committed to leveraging AI and predictive analytics to transform hospital care, reduce readmissions, and improve patient outcomes. If you'd like to learn more, visit app.meldrx.com or reach out to us. <div