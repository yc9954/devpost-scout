---
slug: "hospital-readmission-prediction-with-federated-learning"
url: "https://devpost.com/software/hospital-readmission-prediction-with-federated-learning"
title: "Sammy - a privacy protected federated readmission predictor"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 1004
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Sammy - a privacy protected federated readmission predictor

> HIPAA blocks pooling patient data. Sammy predicts readmission risk with federated learning, running an XGBoost model inside the database—so data never leaves the hospital. Privacy-first, live now.

[Devpost](https://devpost.com/software/hospital-readmission-prediction-with-federated-learning) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[on_device_local]] [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[health_clinical]] [[transportation]]
**user** [[clinician]] [[frontline_worker]] [[general_public]] [[legal_professional]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** amazon-aurora-postgresql, amazon-ec2, amazon-ses, amazon-vpc, aws-amplify, aws-cloudshell, aws-cognito, aws-iam, caddy, duckdns, elasticip, fastapi, flower, framer-motion

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

Mascot Authentication Secure and Confidential Authentication Homepage Authentication Live Patient Cohort View Live Patient Cohort View SHAP - powered explanation SHAP - powered explanation Aurora " THE UNSUNG HERO " System Flow Degisn Architectural Diagram Inspiration Medicare penalizes hospitals over $500M a year for preventable 30-day readmissions. The fix should be simple: pool patient data across hospitals, train a strong model, predict who's at risk. But that's illegal — HIPAA prohibits centralizing patient records across institutions. So the hospitals that most need to share knowledge are the ones legally barred from sharing data. We wanted to know: can a model learn from three hospitals' worth of patients without ever seeing a single patient record leave the building? And once we had that working, a second question followed — if the model can't live in a separate "ML service" without recreating the same data-movement problem, what if the model lived inside the database itself, instead of behind it? That's Sammy. What it does Sammy predicts 30-day hospital readmission risk for patients, trained using federated learning across three simulated hospitals that never share raw patient data — only the trained models are exchanged and aggregated. The live app, deployed on Vercel , gives clinicians a real-time risk dashboard: Three-step gated login through real AWS Cognito (hospital access code → credentials → one-time passcode) A cohort view of 200 patients, each scored live by the trained model — not hardcoded, not cached Search and High/Low risk filtering Per-patient SHAP explainability — clicking into any patient shows the exact factors (age, prior admissions, comorbidities, vitals) that drove their risk score, so a clinician understands why , not just what Credential-based data switching, so demo credentials show demo data and real hospital credentials pull live predictions from Aurora — same deployment, two data realities How we built it Frontend — Vercel + Next.js The entire UI is Next.js 15 (App Router) + React 19 + TypeScript + Tailwind + shadcn/ui, deployed on Vercel. We chose Vercel specifically so the app could ship as a real, public, zero-ops product rather than a localhost demo — judges can open the live URL and click through it themselves, with animated risk gauges, a diverging SHAP bar chart, and framer-motion transitions that make a clinical tool feel usable rather than just functional. Database — Amazon Aurora as the secure core, not a passive store This is the part we think matters most. In a typical ML system, the trained model sits in a bucket (S3, a model registry) and the server ships patient data out to it for inference. We inverted that. The trained model is stored as bytes directly inside Aurora, in a model_store table — sitting next to the patients it scores. A small EC2 instance lives in the same private VPC as Aurora. It reads the model and the patient row over the internal network only, runs the prediction and the SHAP explanation, and writes the result straight back into Aurora. Nothing — not the model, not a patient record, not a prediction — ever leaves that private network boundary to do its job. The result is one secure unit: patient data, the model itself, every prediction, and an immutable audit log all live inside Aurora. There's no separate model server to secure, no data egress to worry about, and Aurora's managed scaling means it grows with patient volume without us managing capacity. We chose Aurora specifically because we needed relational integrity between patients, predictions, and audit history — readmission risk isn't a flat key-value lookup, it's a joined, queryable, auditable clinical record, and Aurora was the right architectural fit for that, not just a default choice. Federated learning — the privacy layer Three simulated hospitals each train locally on their own patient cohort. Each hospital trains a local XGBoost model on its own cohort. Only the trained models — never patient data — are sent to a central aggregator on EC2, which combines them by bagging: it merges the decision trees from each hospital's model into one global ensemble (you can't average tree-based models the way FedAvg averages neural-net weights, so bagging is the correct aggregation here). The improved global model is then redistributed to each hospital's store inside Aurora. No hospital ever sees another hospital's patients. Explainability — SHAP Every prediction ships with SHAP values computed at inference time on the same EC2 node, so clinicians get a transparent, per-feature breakdown of risk drivers without the explanation process ever touching raw data outside the VPC. Challenges we ran into Couldn't use raw MIMIC-IV in a public demo. MIMIC-IV is credentialed, highly sensitive patient data — even with PhysioNet access granted, it can't be exposed in a live, public app without violating its data use agreement. So we generated a synthetic dataset that mirrors MIMIC-IV's structure and statistical patterns, and used that for the public-facing demo instead. Designing around Aurora's constraints, not against them. Storing a serialized model as bytes inside a relational table and keeping read/write latency low enough for live demo use took real tuning — this isn't how Aurora is "supposed" to be used, and we had to validate it could hold up under repeated inference calls during a live cohort scan. Keeping the federated aggregation real, not simulated for show. It was tempting to fake the multi-hospital split for the demo; instead we built three genuinely separate local training sets and a real federated bagging aggregation step, so the privacy claim in our pitch is actually true of the running system. Making three-factor auth and live Aurora inference feel instant on Vercel. Gating real Cognito auth behind three steps while keeping the cohort screen feeling snappy meant careful handling of loading states and credential-based routing between demo and live data, on the same deployed instance. SHAP without data leakage. Computing explainability values close to the model — on the same EC2 node, inside the same VPC as Aurora — so the "why" behind a prediction never required exporting patient features to a third location. <div