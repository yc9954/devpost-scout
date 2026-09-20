---
slug: "yo-zfqlao"
url: "https://devpost.com/software/yo-zfqlao"
title: "CERBERUS: An Adaptive Digital Immune System"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1146
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# CERBERUS: An Adaptive Digital Immune System

> CERBERUS learns normal system behavior and detects ransomware instantly when abnormal entropy patterns emerge, helping protect vulnerable community infrastructure.

[Devpost](https://devpost.com/software/yo-zfqlao) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[civic_government]] [[education]] [[health_clinical]] [[security_privacy]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** ai, css, next.js, node.js, postgresql, pusher, react, sql, tailwind, typescript, vercel

## How they structured the write-up

- p.s.
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for cerberus

## Body

ENTROPY SPIKE : RANSOMWARE ATTACK CERBERUS RANSOMWARE PROTECTION AND DETECTION MAIN SCREEN PS IGNORE THIS HACKATHON SUBMISSION , MY TEAM HAS SUBMITTED ANOTHER PROJECT "SENTINEL PROTOCOL" , THAT ONE IS OUR FINAL SUBMISSION , THIS IS AN OLD EXTRA SUBMISSION BY MISTAKE P.S. If u want a quick skim over this project's technical details ,then it is better to refer to README file of the Github repo i have attached rather than the documentation file whose link i have attached in this devpost project page. The other documentation file is better for a longer and deeper read coz the document is large. Also in the demo video , you might have missed the change in entropy signature plot changing over every click of "TRAIN NORMAL" button on left hand side of the screen , if you click that button a few times while keeping an eye from the beginning on the ENTROPY SIGNATURE plot on the right hand side then you will be able to see the changes being added to the ENTROPY SIGNATURE, "TRAIN NORMAL" triggers the unsupervised learning phase , it scans the current file system to establish a mathematical baseline for every file's entropy Inspiration • Shannon’s Entropy & Behavioral Learning for Real-World Protection The core technical driver is Shannon Entropy used as a dynamic feature for behavioral AI. Our insight was that every digital environment — from a school lab to a clinic server — develops a unique statistical rhythm. When that rhythm is disrupted, it often signals malicious interference. By learning entropy history over time, CERBERUS distinguishes harmless updates from the chaotic high-entropy signature of ransomware. This enables early detection in environments that cannot afford enterprise-grade cybersecurity. • Biomimicry: The Autonomous Digital Immune System The visual design and reactive architecture are inspired by the human immune system. Just as white blood cells autonomously detect infection, CERBERUS acts as a lightweight digital immune layer for vulnerable infrastructure such as NGOs, schools, and municipal systems. Instead of waiting for logs to be reviewed, the system reacts immediately, visually “inflaming” the dashboard to bridge the gap between AI detection and human reaction while reducing alert fatigue. • Tactical Cognitive Load & Augmented Intelligence for Non-Experts Security teams are often absent in smaller institutions. CERBERUS shortens the OODA Loop (Observe–Orient–Decide–Act) by filtering statistical noise into clear, actionable signals. Inspired by AI-augmented HUD systems, the platform presents only the most critical intelligence, enabling administrators with limited cybersecurity training to trust the system’s mathematical reasoning and respond quickly. What it does • AI-Driven Deterministic Behavioral Detection CERBERUS uses Shannon Entropy as a dynamic feature for unsupervised anomaly detection. Unlike signature-based defenses or opaque neural models, CERBERUS relies on deterministic statistical inference. It learns entropy baselines and tracks Z-score deviations to mathematically profile the shift from normal operations to chaotic encryption. Through sliding-window temporal modeling, the system continuously stores entropy history, calculates variance, and identifies the precise moment a file’s behavior deviates from its learned trajectory. Result: Predictive zero-day detection that flags ransomware at the earliest measurable deviation, often before full payload execution. • Neuro-Symbiotic Visualization (Explainable AI Interface) CERBERUS translates inference outputs into a “Digital Nervous System” designed for interpretability. Bio-Grid: Visual neural map showing system health through vitality-to-infection transitions Seismograph: Displays volatility drift in incoming data streams Confidence Mapping: Color intensity corresponds directly to statistical deviation magnitude This ensures the AI’s reasoning is transparent and understandable even for non-technical operators. • Real-Time Inference Stream Built on Next.js and WebSockets, CERBERUS pushes inference signals instantly without page refresh. When deviations occur, alerts propagate in sub-second time, creating a zero-latency decision support environment where forensic replays and shockwave alerts allow responses at machine speed. • Adversarial Simulation Engine CERBERUS includes a built-in simulation layer to validate detection thresholds. Organizations can trigger simulated attacks to test system resilience, train staff, and evaluate response readiness without requiring expensive penetration testing services. How we built it We structured CERBERUS around two pillars: the Behavioral Inference Engine and the Reactive Visualization Fabric. • Real-Time Inference Pipeline Next.js Server Actions serve as lightweight inference APIs, while WebSockets broadcast alerts instantly. This architecture ensures low-resource environments can still receive near-instant intelligence. • Entropy Learning Engine We built a custom entropy calculator and persistence layer storing entropy trajectories over time. This allows CERBERUS to mathematically distinguish between legitimate compression patterns and malicious encryption signatures. • Explainable Visualization Layer The Bio-Grid maps model confidence directly to visual neural states, allowing operators to interpret AI decisions intuitively without reading technical logs. • Modular AI Operations As a two-person team, we designed strict modular boundaries so the system could scale across institutions without heavy infrastructure. Challenges we ran into • Temporal Learning Overhead Tracking entropy trajectories across thousands of files required heavy optimization. We implemented asynchronous entropy extraction and delta comparison to maintain responsiveness. • Real-Time Signal Congestion Simulated attacks produced hundreds of signals per second. We solved this with batching logic and heartbeat updates, preserving interface stability while retaining statistical accuracy. • Bridging the Explainability Gap Raw mathematical deltas were unintuitive. We mapped deviation magnitude directly to visual states so operators could understand the AI’s reasoning instantly. • Ground-Truth Validation We synchronized entropy logs with simulation timestamps to ensure alerts corresponded to real behavioral shifts rather than noise. Accomplishments that we're proud of • Deterministic Behavioral Engine We implemented an entropy-driven statistical learner that detects threats based on deviation from learned normalcy rather than known signatures. • Real-Time Explainable Dashboard Our interface translates complex inference into intuitive signals, making advanced AI-driven defense accessible to non-experts. • Forensic Replay System The “Kill-Cam” feature reconstructs attack timelines from entropy logs, helping institutions understand not just what happened, but how. • Democratizing AI Security Our greatest achievement is building a system that brings advanced behavioral defense to institutions that lack dedicated cybersecurity teams. What we learned Entropy is a powerful behavioral feature for defining normalcy Real-time AI requires efficient distribution, not just fast inference Trust depends on explainability and transparency Modular AI design enables deployment across diverse environments What’s next for CERBERUS • Predictive Temporal Forecasting We plan to train time-series models on entropy history to detect precursor drift before attacks begin. • Federated Learning Across Institutions Future versions will allow organizations to share anonymized learning signals, forming a collaborative defense network while preserving privacy. • Autonomous Response Layer We aim to integrate automated containment protocols that isolate suspicious processes instantly. • Kernel-Level Entropy Extraction Moving feature extraction into the OS layer will allow CERBERUS to scale to enterprise data volumes with minimal overhead. • Explainable Causal Forensics Future iterations will allow operators to trace attack origins through entropy drift timelines, improving transparency and institutional learning. CERBERUS is designed to become a deployable AI-powered digital immune layer that protects the infrastructure communities rely on — bringing deterministic, explainable, real-time defense to environments that historically lacked access to advanced cybersecurity. <div