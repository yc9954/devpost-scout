---
slug: "4sight-neoslb"
url: "https://devpost.com/software/4sight-neoslb"
title: "4sight"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1052
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# 4sight

> AI-powered biometric and visual monitoring that predicts when you’re prone to bad decisions. With autonomously triggered interventions, 4sight helps you make better decisions for a better you.

[Devpost](https://devpost.com/software/4sight-neoslb) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]] [[labor_employment]] [[security_privacy]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]]

**stack** bangle.js, cloudflare-containers, cloudflare-d1, cloudflare-durable-objects, cloudflare-workers, expo.io, fastapi, gemma-3-4b(vlm), github-actions, gpt-4o-mini, meta-ray-ban-smart-glasses, modal, poke, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for 4sight

## Body

4sight Logo Inspiration We’re surrounded by tools that track our health, but none that meaningfully protect our decision-making or help us make decisions. Research shows that stress, health, and our environment significantly alter how we evaluate ideas, often leading to impulsive or suboptimal choices (Starcke & Brand, 2012). If our physiology influences decisions so much, we wondered: What if wearables could predict when you’re vulnerable to making bad decisions and intervene before you act? 4sight was built around that idea. Not just tracking health, but a real-time decision-support system that combines internal biometric signals with external environmental context. What it does 4sight is an autonomous decision-support system that predicts when you’re prone to making bad decisions based on biometric and contextual data. Drawing on findings that stress and physiological load directly impact decision-making processes, 4sight continuously monitors biosignals such as heart rate and heart rate variability (HRV), motion and exertion metrics, sleep-related indicators, and cognitive and physiological stress signals. In addition, Meta smart glasses provide lightweight environmental context such as visual surroundings and situational cues that help interpret biometric spikes more intelligently. This allows the system to distinguish between healthy exertion and stressful overload, or between calm focus and cognitive fatigue in overstimulating settings. These signals are used to generate five domain-specific risk scores of stress, sleep, health, cognitive exhaustion, and physical exertion. A weighted aggregate produces a general decision-risk score, identifying windows of time where impaired judgment is more likely. When risk crosses a threshold, 4sight autonomously intervenes through various channels: Activating Screen Time APIs to curb doomscrolling during stress spikes Sending nudges via iMessage using Poke AI, which can use MCPs to trigger real-world interventions, like ordering from Amazon Triggering automated actions such as Amazon ordering stress-mitigation products such as magnesium supplements to aid in sleep quality Instead of passively reporting metrics, 4sight acts by using both internal physiological state and external context to make more holistic decisions about when intervention is truly necessary. How we built it 4sight pairs a Bangle.js 2 smartwatch with Meta Ray-Ban smart glasses to continuously capture two streams of data: biometric signals and environmental context via CV. The watch's custom-built firmware records 60-second windows of raw PPG (25 Hz) and accelerometer (12.5 Hz) data in a compact binary format, syncing over BLE via the Nordic UART Service to our Expo/React Native app. On-device, a pure TypeScript XGBoost engine extracts 36 biosignal features from each window, including HRV time-domain metrics (SDNN, RMSSD, pNN50), Poincare non-linear measures, and motion energy, then runs nine trained models (five 4-class risk classifiers spanning stress, health, sleep fatigue, cognitive fatigue, and physical exertion, plus four regressors for overall susceptibility and time-to-risk) to produce real-time vulnerability scores with no network dependency and fast inference. These models were trained on over 70,000 instances drawn from multimodal physiological datasets including WESAD and PPG-DaLiA (Schmidt et al., 2018; Reiss et al., 2019), with a weighted risk aggregation layer that transforms domain-specific predictions into a single generalized vulnerability score. On the backend, the Ray-Bans stream live video frames over a WebSocket to a FastAPI server on Cloudflare Containers, which chunks them into 1-second windows and dispatches them to a Gemma 3 4B vision-language model (VLM) running on Modal (L40S GPU) for low-latency food and activity captioning. Both biometric features and vision captions land in a Cloudflare D1 database via idempotent uploads. A Cloudflare Worker cron fires every 60 seconds, pulling the latest biometric and caption windows and feeding them to GPT-4o-mini with structured JSON outputs to make an intervention decision. If the model says "yes," a contextual nudge is sent as an iMessage through the Interaction Company Poke API. We also integrated Screen Time APIs for device-level behavior control and programmatic purchasing workflows for proactive mitigation. The whole pipeline, from biometric capture to environmental scan to autonomous intervention, runs in real time with no user interaction required. Challenges we ran into Real-Time Environmental and System Integration: Connecting wearable biometric streams and environmental context from Meta glasses to a live ML inference engine and intervention system without latency or cascading errors required careful architectural design. Training a Niche Prediction Model: There is no labeled dataset for impaired decision-making windows. We had to develop vulnerability detection using stress and physiological markers while preventing overfitting due to limited ground-truth signals in this niche field. Coordinating Autonomous Interventions: Designing a system that does not just notify but acts on its own required building safe thresholds and ensuring interventions were context-aware rather than disruptive. Accomplishments that we're proud of Building a fully autonomous monitoring to prediction to intervention pipeline Successfully integrating real-time biometric data from a hackable smartwatch Designing a weighted multi-domain risk model rather than relying on a single metric Creating a system that can actively modify digital behavior instead of passively displaying data Most importantly, we transformed wearable biometrics into real decision-support infrastructure that works with you, not for you. What we learned Most of us had never worked with biometric monitoring, hackable smartwatches, or autonomous intervention systems before. We learned how to handle noisy physiological data, build sliding-window ML models, and architect real-time systems that connect hardware to actionable outcomes. We also saw firsthand how powerful multidisciplinary collaboration can be. 4sight sits at the intersection of machine learning, systems engineering, behavioral science, and product design. All of this only worked because we brought those perspectives together. What's next for 4sight We plan to expand contextual intelligence to detect overstimulating or high-risk environments where cognitive clarity is critical. We’re also exploring medical integrations, including Continuous Glucose Monitoring (CGM) systems for diabetic patients. By combining glucose trend data with physiological stress modeling, 4sight could help predict and manage hypo- and hyperglycemic swings proactively. Long term, we envision 4sight as a generalized autonomous safety layer, one that connects biometric monitoring, environmental awareness, and real-world intervention pathways, including rapid connection to healthcare providers when risk escalates. References Starcke, K., & Brand, M. (2012). Decision making under stress: A selective review. Neuroscience & Biobehavioral Reviews, 36(4), 1228–1248. https://doi.org/10.1016/j.neubiorev.2012.02.003 Schmidt, P., Reiss, A., Dürichen, R., Marberger, C., & Van Laerhoven, K. (2018). Introducing WESAD, a Multimodal Dataset for Wearable Stress and Affect Detection. Proceedings of the 20th ACM International Conference on Multimodal Interaction (ICMI ’18), 400–408. https://doi.org/10.1145/3242969.3242985 Reiss, A., Indlekofer, I., & Schmidt, P. (2019). PPG-DaLiA [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C53890 <div