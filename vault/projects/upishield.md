---
slug: "upishield"
url: "https://devpost.com/software/upishield"
title: "UPIShield"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 514
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/transportation"
  - "substrate/sensor_telemetry"
---

# UPIShield

> A real-time UPI fraud intelligence system that combines graph analytics and machine learning to identify mule networks, detect anomalies, and trigger adaptive security actions.

[Devpost](https://devpost.com/software/upishield) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[security_privacy]] [[transportation]]
**substrate** [[sensor_telemetry]]
  <sub>weak: structured_db</sub>

**stack** csv, json, numpy, pandas, python, scikit-learn

## How they structured the write-up

- inspiration
- project overview
- mathematical framework
- system architecture
- technology stack
- challenges faced
- key learnings
- future scope
- conclusion

## Body

UPISheild Inspiration Cyber attacks today are automated, polymorphic, and increasingly AI-assisted. However, many defensive systems still depend heavily on static signatures and predefined rules. This reactive model creates a structural gap: attackers evolve faster than defenses. We asked a forward-looking question: What if a cybersecurity system could continuously learn system behavior and detect threats based on deviation rather than known signatures? This project was built to design a lightweight, AI-driven behavioral anomaly detection engine capable of predicting malicious activity in real time. Project Overview We developed an adaptive cyber defense system that: Monitors real-time system and network activity Learns baseline behavioral patterns Detects anomalous deviations Computes dynamic risk scores Triggers intelligent alerts Each system state is represented as a feature vector: $$ X = {x_1, x_2, x_3, ..., x_n} $$ Where features include: Network request frequency Port access distribution File access entropy CPU usage variance Authentication attempt patterns Mathematical Framework We model threat probability using Bayesian inference: $$ P(\text{Threat} \mid X) = \frac{P(X \mid \text{Threat}) \, P(\text{Threat})}{P(X)} $$ If: $$ P(\text{Threat} \mid X) > \tau $$ where \(\tau\) is a dynamic threshold, the system flags the activity as suspicious. We combine multiple anomaly metrics into a unified risk score: $$ \text{Risk Score} = \alpha \cdot IF(X) + \beta \cdot B(X) $$ Where: \(IF(X)\) = Isolation Forest anomaly score \(B(X)\) = Bayesian threat probability \(\alpha, \beta\) = adaptive weighting coefficients Long-term trust modeling is expressed as: $$ Trust(t) = e^{-\lambda \cdot Risk(t)} $$ Where trust decays exponentially as cumulative risk increases. System Architecture Data Collection Layer Real-time log ingestion Network traffic metadata parsing Feature normalization Feature Engineering We extracted: Statistical deviation metrics Temporal frequency shifts Shannon entropy of file access: $$ H = -\sum_{i=1}^{n} p_i \log p_i $$ Behavioral drift scores Model Layer Isolation Forest (unsupervised anomaly detection) Bayesian probabilistic modeling Adaptive threshold optimization Response Engine When risk exceeds threshold: Event is logged Alert is generated Mitigation suggestions are provided Optional IP auto-blocking is triggered Technology Stack Python Scikit-learn NumPy Pandas Real-time socket monitoring Modular logging engine The system is: Lightweight Modular Deployable locally Extensible for enterprise-scale deployment Challenges Faced 1. Limited Labeled Attack Data High-quality labeled cybersecurity datasets are scarce. We addressed this using: Simulated attack injection Synthetic anomaly generation Unsupervised learning models 2. False Positives Anomaly detection systems are sensitive by nature. To reduce false alarms, we implemented: Rolling behavioral baselines Context-aware detection windows Adaptive threshold tuning 3. Real-Time Constraints Live threat detection requires computational efficiency. Optimizations included: Vectorized numerical operations Batch inference windows Lightweight model selection Key Learnings Behavioral modeling is more scalable than signature-based detection. Risk scoring is superior to binary classification in real-world security. Adaptive thresholds significantly reduce false positives. AI in cybersecurity must balance detection sensitivity and operational practicality. Future Scope This system can evolve into: Federated learning across endpoints Zero-trust architecture integration Cloud-native deployment Autonomous response agents SIEM platform integration Conclusion This project shifts cybersecurity from reactive detection to predictive defense. Instead of asking: Is this a known attack? We evaluate: Does this behavior statistically deviate from trusted patterns? That shift enables next-generation adaptive cyber defense systems. <div