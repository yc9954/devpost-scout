---
slug: "d3cision"
url: "https://devpost.com/software/d3cision"
title: "D3CISION"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 1201
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/measured_ablation"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# D3CISION

> Solving the triage challenge by transforming raw security logs into explainable, gravity-sorted attack stories, allowing analysts to spot real threats instantly.

[Devpost](https://devpost.com/software/d3cision) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[benchmark_measured]] [[measured_ablation]] [[privacy_tech]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]] [[security_privacy]] [[transportation]]
**user** [[educator_student]] [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** gemini, mongodb, networkx, nextjs, python, react, scikit-learn, tailwind, typescript, xgboost

## How they structured the write-up

- 🎯 inspiration
- 🚀 what it does
- 🛠 how we built it
- 🏆 accomplishments that we're proud of
- 🚀 what's next for d3cision
- 🏗 built with
- 📊 performance metrics
- challenges we ran into

## Body

D3CISION 🎯 Inspiration "10,000 alerts. 8 hours. 1 analyst. Which 100 do you investigate?" Security Operations Centers face an impossible choice: every alert could be the one that leads to a breach, but investigating them all is physically impossible. We watched analysts drown in alert fatigue, making split-second decisions with incomplete context, knowing that one mistake could cost millions. We built D3CISION to solve the fundamental problem: it's not a lack of data, it's a lack of contextual clarity . Our mission: transform the noisy "Alert Hell" into an explainable, prioritized, and actionable Gravity Stack where the most critical threats naturally rise to the top. 🚀 What it does D3CISION is a next-generation SOC triage platform that fundamentally reimagines security operations: Core Capabilities 🔗 Intelligent Story Correlation : Uses entity-affinity algorithms and temporal analysis to connect isolated security events into coherent "Attack Stories." A single malicious campaign spanning 20 events across 3 hosts becomes one story, not 20 separate alerts. 🧠 Neural Threat Scoring (98.9% AUC) : An XGBoost ensemble model analyzes 50+ features per event, including burst patterns, external sources, temporal clustering, and historical indicators, to calculate precision threat scores. Outperforms baseline rules by 142%. 💡 Explainable AI (SHAP) : Every score comes with a reason. Using SHAP (SHapley Additive exPlanations), we show analysts exactly which features drove each decision: "High priority due to: External Source IP [Yes] + Story Max Severity [Critical] + Burst Activity [5 events/hour]." No black boxes. 🛡️ Autonomous Response Platform : Axiom_Sentinel has shifted from analysis to action. Analysts can now Isolate Hosts and Block Traffic directly from the Mission Control interface. 🤖 AI Tactical Autonomy : The Gemini agent can execute tactical actions autonomously. You can ask: "Block traffic for all stories with risk over 95%" or "Isolate host for S042," and the system will perform the remediation and log it in the database. 🤖 AI Tactical Advisor : Powered by Google Gemini 3 Flash, our AI assistant provides: Contextual remediation plans specific to each story Plain-English explanations of complex attack patterns Voice-narrated briefings via ElevenLabs for hands-free operation Interactive Q&A about any security event ⚖️ Uncertainty Quantification : We don't just score threats, we score our own confidence. Stories with low signal volume, missing user context, or conflicting indicators are explicitly flagged for manual review, preventing false confidence. 🛠 How we built it Frontend (The Mission Control) Next.js 15 + TypeScript : Server-side rendering for instant load times Framer Motion : Physics-based animations for the 3D Gravity Stack Tailwind CSS 4.0 : Custom design system with glassmorphic UI elements 💪 Challenges we ran into 1. Correlating the "Invisible" Security events often lack explicit relationships, an EDR alert might not reference the Azure AD login that triggered it. We built a multi-dimensional correlation engine using: 🏆 Accomplishments that we're proud of 98.9% AUC-ROC , Our model achieves near-perfect threat detection accuracy, validated on real-world SOC data with ground-truth labels. 142% Improvement Over Baseline , We didn't just build a model; we proved it works. Against the official D3 Security rule-based logic (severity + confidence + external IP), our ML approach delivers 2.4x better F1-score. Explainable AI That Analysts Trust , Most "AI security tools" are black boxes that analysts ignore. We use SHAP to expose every decision: "This is high-priority because: External Source [Yes], Story Max Severity [Critical], Burst Activity [5 events/hour]." Trust through transparency. Sub-Second Performance at Scale , The entire pipeline: correlation, scoring, SHAP explanation, story aggregation, processes hundreds of events in under 1 second. Production-ready. Voice-Activated Security , Using ElevenLabs, analysts can listen to threat briefings hands-free while triaging incidents. "Alexa for SOC analysts." Uncertainty as a Feature , We don't hide when the model is uncertain. Stories with low confidence get amber warnings: "Manual Review Required." Honesty prevents false confidence and reduces risk. Getting this right without creating false positives was our hardest technical challenge. 2. The Explainability Paradox SHAP values are mathematically rigorous but cryptic. We spent hours translating raw SHAP outputs into actionable analyst guidance: "High Severity [3.0]" became "Story contains Critical-severity events requiring immediate investigation." 3. Balancing Performance with Richness Run🎓 What we learned Explainability > Accuracy , A 95% accurate model that analysts don't trust is useless. A 90% accurate model with clear explanations gets adopted. SHAP isn't just a technique—it's the bridge between AI and human decision-making. "Actionable Intelligence" > "Raw Detection" , Security teams don't need more alerts; they need fewer, better, more contextualized ones. Story correlation reduces 100 alerts to 5 actionable campaigns. Uncertainty is Data , When the model isn't confident, that's valuable information. We learned to quantify and communicate uncertainty explicitly rather than hiding behind a single confidence score. Voice Changes Everything , Adding ElevenLabs voice narration transformed the UX. Analysts can now "listen" to briefings while investigating on other screens. Multimodal interfaces aren't just cool, they're practical. Hackathons Accelerate Learning , We learned more about production ML deployment, security workflows, and real-time AI in 24 hours than we could in a month of tutorials. 🚀 What's next for D3CISION Real-Time Streaming , Integrate with Kafka/Kinesis for live alert ingestion. No more batch processing, threats surface in real-time. Automated Response , Connect to SentinelOne/CrowdStrike APIs for autonomous threat containment. The AI doesn't just recommend, it acts. Federated Learning , Allow multiple SOCs to train collaboratively without sharing sensitive data. Global threat intelligence, local privacy. VR Mission Control , Full 3D immersive triage environment using WebXR. Walk through your threat landscape in virtual reality. Multi-Model Ensemble , Add transformer-based models for log parsing and anomaly detection. XGBoost for structured data, LLMs for unstructured. SOC Workflow Integration , Native plugins for Splunk, Sentinel, QRadar. Make Axiom_Sentinel the AI layer for existing SIEM platforms. 🏗 Built With google-gemini-api - AI reasoning and contextual analysis elevenlabs - Voice-narrated tactical briefings mongodb-atlas - Persistent storage for AI plans python - ML pipeline and data engineering xgboost - Neural threat scoring engine shap - Explainable AI framework next-js - Frontend framework framer-motion - Kinetic UI animations tailwindcss - Design system typescript - Type-safe development networkx - Graph-based story correlation 📊 Performance Metrics AUC-ROC : 0.9886 (98.9%) F1-Score : 0.9627 (96.3%) Precision : 0.9722 (97.2%) Recall : 0.9533 (95.3%) Baseline Improvement : +142.5% Built with 🔥 at ConUHacks X 2026 "From Signal to Decision in Seconds, Not Hours" story clustering Scikit-learn : Feature engineering, preprocessing, and baseline comparisons AI Integration (The Voice) Google Gemini 3 Flash : Context-aware reasoning over correlated security logs, generates remediation plans, answers analyst questions in real-time ElevenLabs API : Voice-narrated tactical briefings for eyes-on-glass monitoring and hands-free triage MongoDB Atlas : Persistent storage for AI-generated plans and analyst feedback Data Engineering 5-Stage Pipeline : Clean → Train → Score → Correlate → Finalize Dual-Dataset Strategy : Differentiated handling for high-throughput noisy telemetry (Dataset 1) vs. low-noise high-fidelity alerts (Dataset 2) Feature Enrichment : Burst detection, external IP flagging, temporal clustering, story-aware aggregations Challenges we ran into Correlating the "Invisible" : Building the logic to connect a source-less EDR alert to an Azure AD login based on temporal and entity proximity was tough. The "Clipped" Problem : UI-wise, fitting high-density charts into a sidebar while keeping them legible required aggressive SVG coordinate optimization. <div