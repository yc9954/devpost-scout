---
slug: "anemochain"
url: "https://devpost.com/software/anemochain"
title: "AnemoChain"
hackathon: "ML Empowerment Build Challenge 2.0"
organization: "ML Empowerment Foundation"
winner: true
words: 1107
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/financial_record"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AnemoChain

> Non-invasive anemia screening from a single eye photo — powered by AI and secured with blockchain tamper-detection. No blood draw. No lab. Deployable anywhere.

[Devpost](https://devpost.com/software/anemochain) · hackathon [[ML Empowerment Build Challenge 2.0]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[accessibility]] [[health_clinical]] [[scientific_research]] [[security_privacy]]
**user** [[clinician]] [[patient_family]]
**substrate** [[financial_record]] [[medical_record]] [[structured_db]] [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** dart, fastapi, flask, flutter, hyperledger-fabric-(style), jinja, onnx-runtime, python, scikit-learn, sqlite, tailwind-css, xgboost

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for anemochain

## Body

Landing Page — Main home screen of the AnemoChain mobile app Screening Result (Status & Image Preview) — Displays the conjunctiva photo preview Screening Result (Clinical Detail) — Extended result view showing advanced optical color metrics & AI Interpretation — Intuitive error message displayed when the submitted photo cannot be identified as a human eye by the AI validation system Record Verified (No Tampering) — The Hospital Dashboard when a clinician verifies a patient record Tampering Detected — The system's protective response when it detects unauthorized modification of a local database record Block View — The Hyperledger Blockchain Explorer displaying the list of transaction blocks in the network Research Flow & System Architecture Two-Layer Image Validation Inspiration 1.92 billion people live with anemia, yet most cannot access a simple blood test. In low-resource settings like community health posts and rural clinics, laboratory infrastructure for routine blood draws simply does not exist. Prior research has explored non-invasive anemia detection from conjunctiva images using deep CNN ensembles, achieving AUC scores as high as 0.97. But none of these systems were ever integrated into a mobile application, meaning they remained confined to laboratory environments and never reached the communities that need them most. As I explored these existing solutions more deeply, I found two additional critical blind spots. First, every existing pipeline accepts any image as valid input — a photo of a wall or a floor would still produce a clinical label. Second, not a single system included any mechanism to detect whether a stored medical record had been altered after the fact. In an era where healthcare data breaches rose 239% and ransomware attacks rose 278% between 2018 and 2023, this is not a minor gap. If a screening result can be silently modified in a database, the entire diagnostic chain becomes untrustworthy. These three gaps — no mobile integration, unsafe inputs, and unverifiable outputs — were the starting point for AnemoChain. What it does Non-invasive anemia screening from a single photo. The user captures or uploads a conjunctiva (inner eyelid) photo through the mobile app. No blood draw, no lab equipment, no trained phlebotomist required. Two-layer image validation gate. Before any AI inference runs, the system checks whether the submitted image is actually a valid conjunctiva photo using pixel quality and colorspace constraints. Non-ocular or low-quality images are rejected immediately. 171-feature multi-colorspace ML inference. Valid images are processed across RGB, CIE LAB, HSV, and YCbCr colorspaces plus clinical pallor indices, returning a confidence score, optical-clinical details, and health recommendations. Blockchain-sealed records. Every screening result is hashed (SHA-256) and sealed into a Hyperledger Fabric-style blockchain ledger before being written to the database, ensuring the blockchain always holds the ground truth. Hospital dashboard with tamper detection. Clinicians can verify any patient record against the blockchain in one click. If the database record has been modified after the fact, the system immediately raises a DATA TAMPERED alert. How we built it Machine Learning Pipeline. Five classifiers were benchmarked across a 171-feature matrix from the Eyes-Defy-Anemia dataset across three stratified splits. HistGradientBoosting was selected as the production model and exported to ONNX for lightweight edge inference. FastAPI Backend. Handles the full inference chain in strict order: image validation, feature extraction, ONNX inference, SHA-256 hashing, blockchain sealing, and finally database persistence. The blockchain seal always precedes the database write. Hyperledger Fabric-style Ledger Node. A custom blockchain node where every screening hash is chained into an immutable block, creating a permanent and verifiable audit trail. Flask Hospital Dashboard. A clinician-facing web interface supporting patient record lookup and one-click hash verification against the blockchain ledger. Flutter Mobile App. A cross-platform mobile app supporting camera capture, gallery upload, real-time screening results, screening history, and data sync to the hospital database. Challenges we ran into Building the validation gate without labeled rejection data. No public dataset of invalid conjunctiva images exists. The two-layer gate was designed entirely from first principles using colorspace constraints derived from known conjunctiva tissue properties, then tuned iteratively against real-world test photos. Keeping the model edge-deployable. Prior research relied on computationally heavy CNN ensembles not feasible for mobile deployment. The challenge was finding a classical ML approach that remained competitive in AUC while lightweight enough to export to ONNX and run on low-resource devices. Enforcing strict transaction ordering across services. Ensuring the blockchain seal always precedes the database write, and that a failed blockchain call never produces a dangling database record, required careful sequencing and rollback logic across two separate services. Small dataset with high variance. The Eyes-Defy-Anemia dataset contains only n ≈ 218 samples. Achieving stable results required careful stratification and honest reporting across three different train/test splits. Accomplishments that we're proud of First input validation gate in any non-invasive anemia pipeline. No prior published system rejects non-ocular images before inference. AnemoChain is the first to do so explicitly. First blockchain tamper-detection layer in any non-invasive anemia system. Any post-hoc modification to a database record is immediately detectable by cross-checking against the immutable on-chain hash. Competitive model performance with a lightweight approach. An AUC of 0.9153 with a balanced sensitivity/specificity trade-off (0.80 / 0.83), achieved without heavy CNN ensembles. Full system integration as a solo submission. All five components were designed, built, and integrated independently across five different technology stacks. What we learned Input validation is non-negotiable in medical AI. A model that silently accepts any image and produces a clinical label is not production-ready, regardless of benchmark accuracy. Validation must be treated as a first-class component, not an afterthought. Blockchain integrity does not require enterprise infrastructure. A well-architected Fabric-style ledger node can provide a genuine tamper-evident audit trail without the full complexity of a production Hyperledger Fabric deployment. Classical ML can stay competitive when constraints are real. Careful feature engineering across multiple colorspaces can approach the AUC of deep CNN ensembles at a fraction of the computational cost when edge deployability is a hard requirement. What's next for AnemoChain Expand the dataset to Southeast Asian populations. Field data collection from Indonesia, Philippines, and Vietnam is the highest-priority next step for improving real-world generalizability. Add hemoglobin regression. Future versions will estimate an actual hemoglobin value in g/dL, giving clinicians a quantitative severity estimate rather than a binary risk flag. Enable fully on-device ONNX inference. Moving inference entirely onto the Flutter app would allow offline screening with zero backend dependency, critical for the most remote deployment scenarios. Pursue a clinical validation study. A formal partnership with community health facilities (posyandu/puskesmas) to validate real-world diagnostic performance before any responsible clinical deployment. Upgrade to a production Hyperledger Fabric deployment. Replace the current simulation with a full enterprise-grade network for production-level auditability and decentralization. <div