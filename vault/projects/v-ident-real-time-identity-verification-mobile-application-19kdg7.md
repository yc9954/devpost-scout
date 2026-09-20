---
slug: "v-ident-real-time-identity-verification-mobile-application-19kdg7"
url: "https://devpost.com/software/v-ident-real-time-identity-verification-mobile-application-19kdg7"
title: "V-Ident : Real Time Identity Verification Mobile Application"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 3059
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "user/general_public"
  - "user/government_staff"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# V-Ident : Real Time Identity Verification Mobile Application

> V-Ident: Pulse + pixels = proof. On-device heartbeat detection & frequency forensics catch deepfakes. ZK-proofs verify live humans in 8 sec — zero biometrics stored. Fakes can't bleed.

[Devpost](https://devpost.com/software/v-ident-real-time-identity-verification-mobile-application-19kdg7) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]] [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[structural_withholding]]
**domain** [[accessibility]] [[civic_government]] [[developer_tools]] [[elder_child_care]] [[finance_payments]] [[immigration_refugee]]
**user** [[general_public]] [[government_staff]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[regulation_legal_text]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** fastapi, firebase, github, mobilenetv2, node.js, numpy, pandas, python, pytorch, react-native, scikit-learn, snarkjs, tensorflow, typescript

## How they structured the write-up

- demo video
- v-ident ml model
- tech stack
- table of contents
- core design philosophy
- what makes v-ident different
- architecture: the three-axis model
- device tier classification
- signal portfolio (tass matrix)
- trust score engine
- verification zones
- accessibility system
- security & anti-spoofing
- enrollment flow
- per-transaction verification flow
- economic model
- regulatory compliance
- roadmap
- what's excluded from phase 1
- summary

## Body

Main Technical Workflow ML Model Training ML Model Training Security System Architecture V-Ident — TASS-V Tier-Adaptive, Risk-Calibrated, Accessibility-First Identity Verification Built by Team PsychoBytes · IIIT Pune · February 2026 V-Ident is a mobile app identity verification engine that detects whether a user is a live, unique human — without storing raw biometrics, without blockchain overhead, and without locking out budget-device users. It dynamically selects the optimal combination of physiological signals per device, achieving < 3% human review rate and < ₹1 cost per verification . Demo Video 🎥 Watch the Demo Video See V-Ident in action and explore how the app performs in real-time. V-Ident ML Model The machine learning model powering this project is maintained in a separate repository. 🔗 View the V-Ident ML Model Tech Stack Core : React Native & Expo (Managed Workflow) Language : TypeScript (Strict Mode) Navigation : Expo Router (File-based routing) State Management : Zustand Animations : React Native Reanimated 3 Graphics : React Native SVG & Expo Linear Gradient Sensors : Expo Camera & Expo Sensors Storage : React Native MMKV Camera and Video Processing : react-native-vision-camera Machine Learning and rPPG : react-native-fast-tflite Zero-Knowledge Proofs (ZKP) : snarkjs Table of Contents Core Design Philosophy What Makes V-Ident Different Architecture: The Three-Axis Model Device Tier Classification Signal Portfolio (TASS Matrix) Trust Score Engine Verification Zones Accessibility System Security & Anti-Spoofing Enrollment Flow Per-Transaction Verification Flow Tech Stack Economic Model Regulatory Compliance Roadmap What's Excluded from Phase 1 Core Design Philosophy The redesigned V-Ident is not a 6-layer ML monolith. It is a signal-selection engine governed by three runtime inputs: Signal Set = f(Device Tier, Transaction Risk Level, User Accessibility Profile) This single architectural shift — computing signal selection at runtime rather than statically — resolves over 60% of the flaws present in the original design, including computational overload on budget phones, biometric bias, and accessibility exclusion. What Makes V-Ident Different Three genuine innovations not found combined in any competitor product: Psychophysiological signal fusion — rPPG heartbeat detection combined with behavioral timing as the core liveness proof, running on-device with no video upload. XAI-based explainability — every rejection generates a plain-language explanation for both the user and the review officer, as required under RBI FREE-AI and the DPDP Act. Privacy-first ZK-proof output — the system attests "live unique human" without transmitting raw biometrics or creating a cross-service tracking vector. Architecture: The Three-Axis Model Every verification is governed by three axes, each independently set and tamper-resistant: Axis Determined By Values Modifiable By User? Device Tier Hardware benchmark at install T1 (Budget) / T2 (Mid) / T3 (Premium) No Transaction Risk Calling service (bank / govt) R1 (Low) / R2 (Medium) / R3 (High) No User Profile Self-declared at enrollment Standard / Motor / Visual / Neurological / Elderly Declared once, encrypted Device Tier Classification At first launch, a 3-second Device Profiler silently benchmarks actual hardware — not spec sheets — to prevent tier spoofing. Property Tier 1 — Budget (₹10K–₹20K) Tier 2 — Mid (₹20K–₹45K) Tier 3 — Premium (₹45K+) Example Devices Redmi 13C, Realme C65, Samsung A15 Realme 12, Samsung A55, Pixel 6a iPhone 15+, Pixel 8 Pro, Samsung S24 Front Camera 8 MP, no OIS, ≤ 30 FPS 16–32 MP, 30 FPS 12–48 MP, PDAF, 60 FPS ML Accelerator CPU only / basic DSP Mid-tier NPU (Helio G99 / SD 7s) Apple Neural Engine / Tensor G3 / SD 8 Gen 3 TEE Basic TrustZone TrustZone + Android Keystore StrongBox (Android) / Secure Enclave (iOS) RAM 4–6 GB 6–8 GB 8–16 GB Max On-Device Model Size ~15 MB total ~40 MB total ~80 MB total Profiler Benchmark < 500 TOPS 500–1500 TOPS > 1500 TOPS Signal Portfolio (TASS Matrix) Signals are selected automatically based on device tier. The app ships with only the Core Model (~12 MB); additional signal modules are downloaded once after device profiling. Signal Available On Compute Cost Spoof Resistance (2026) Visual Frequency Forensics (VFF) T1, T2, T3 Low — 3–5 MB model HIGH — detects GAN/diffusion artifacts at frequency domain Cognitive Response Timing (CRT) T1, T2, T3 Near-zero — rule-based MEDIUM-HIGH — AI reaction timing lacks natural human jitter Hardware Attestation (HA) T1 (basic), T2/T3 (full) Negligible VERY HIGH — cryptographic; requires physical hardware compromise Micro-tremor IMU Analysis T2, T3 only Low HIGH — natural 8–12 Hz hand tremor is physically impossible to inject rPPG Heartbeat Detection T2, T3 (with lighting gate) Medium — 8–12 MB model MEDIUM (improving) — multi-region skin tone adaptation applied Touch-Pressure Behavioral Biometrics T2, T3 only Low MEDIUM — real-time force signature is hard to replicate Micro-saccade Eye Tracking T3 only High — 15–20 MB model VERY HIGH — sub-ms latency physically impossible to deepfake in real time Minimum Signal Requirements per Risk × Tier Risk Level Tier 1 (Budget) Tier 2 (Mid) Tier 3 (Premium) R1 — Low (≤ ₹5K / routine login) VFF + CRT + HA-Basic VFF + CRT + Micro-tremor + HA VFF + CRT + Micro-tremor + HA-Full R2 — Medium (₹5K–₹50K / account changes) VFF + CRT + HA-Basic + Step-Up Challenge VFF + CRT + Micro-tremor + rPPG + HA All T2 signals + Touch Pressure R3 — High (₹50K+ / SIM swap / KYC) VFF + CRT + HA-Basic + Async Human Review VFF + CRT + Micro-tremor + rPPG + Touch + HA Full suite including Micro-saccade Note: For Tier 1 + R3, the system falls back to Async Human Review (within 4 hours) rather than blocking service entirely. Trust Score Engine V-Ident uses Bayesian Log-Odds Fusion — not a weighted geometric mean — because it handles missing signals (for accessibility profiles) gracefully and accounts for signal reliability variance across device tiers. Computation Steps 1. Prior Log-Odds (neutral): LogOdds₀ = log[0.5 / 0.5] = 0 2. Per-signal LLR: LLR_i = log[ P(human | s_i) / P(spoof | s_i) ] (LLR > 0 = evidence for human; LLR < 0 = spoof detected; LLR = 0 = signal unavailable) 3. Weighted Bayesian Fusion: LogOdds_fused = LogOdds₀ + Σ (w_i × LLR_i) [Missing/inaccessible signals contribute 0 automatically] 4. Cross-Signal Temporal Consistency Bonus (T2/T3 only): Corr = Pearson correlation between rPPG rhythm and IMU tremor rhythm Bonus_LLR = 0.5 × max(0, Corr) 5. Rooted Device Penalty (if detected): LogOdds_fused = min(LogOdds_fused, 0.70) [caps TS at ~70] 6. Sigmoid Conversion → Trust Score: P_human = 1 / (1 + exp(-LogOdds_fused)) TS = round(P_human × 100, 1) Signal Weight Matrix Signal Weight — Tier 1 Weight — Tier 2 Weight — Tier 3 Visual Frequency Forensics (VFF) 0.45 0.30 0.20 Cognitive Response Timing (CRT) 0.35 0.20 0.15 Hardware Attestation (HA) 0.20 0.15 0.10 Micro-tremor IMU 0.00 0.20 0.15 rPPG Heartbeat 0.00 0.15 0.20 Touch Pressure Biometrics 0.00 0.00 0.10 Micro-saccade Eye Tracking 0.00 0.00 0.10 SUM 1.00 1.00 1.00 Verification Zones Zone Trust Score Range Action 🟢 GREEN TS ≥ 80 (R1) / ≥ 90 (R2) / ≥ 95 (R3) Auto-Approve. ZK-proof issued immediately. No human involved. 🟡 AMBER 65 ≤ TS < threshold Secondary Challenge triggered automatically in a different modality. Target: converts 80% of Amber to Green. 🔴 RED TS < 65, OR attestation fail, OR rooted device + R3 Async Human Review queue. User is never blocked — notified within 4 hours. At scale (100K verifications/day): ~88% Green → ~9% Amber → ~3% human review , manageable by a 50-person team at 4 minutes per case. Trust Score Thresholds by Risk Level Risk Level Green (Auto-Approve) Amber (Challenge) Red (Human Review) R1 — Low TS ≥ 80 65 ≤ TS < 80 TS < 65 R2 — Medium TS ≥ 90 72 ≤ TS < 90 TS < 72 R3 — High TS ≥ 95 82 ≤ TS < 95 TS < 82 Rooted Device Never (capped at 70) R1 only (65–70) Always for R2, R3 Accessibility System At enrollment, users optionally declare an accessibility profile. It is encrypted in the Secure Enclave and never sent to any server . Any signal inaccessible to a profile is automatically excluded, and the Trust Score formula re-normalizes weights across remaining signals — no user is penalized for a disability. Accessibility Profile Alternative Signal Configuration Standard (default) Full TASS matrix per device tier Motor Disability Removes CRT gesture component; replaces with extended rPPG + voice pitch micro-tremor analysis Visual Impairment Removes all gaze-based challenges; replaces with audio-guided voice challenge + touch pressure biometrics + rPPG Neurological (Parkinson's, MS, etc.) Extended time windows (3×); IMU tremor model uses personalized baseline from enrollment; flags for human review only if deviation from personal baseline is large Elderly Users Extended challenge windows (2×); larger visual targets; voice challenge available; reduced gesture complexity Security & Anti-Spoofing Rooted / Jailbroken Device Handling Layer 1 — Android Play Integrity API / iOS Jailbreak detection at every session start. Layer 2 — Root detection does NOT deny service. Instead, Trust Score is capped at 70 , ensuring AMBER or RED zone for anything above R1. Layer 3 — Temporal consistency check: injected sensor data arrives with suspiciously uniform inter-sample timing. Real sensor data has 0.5–2 ms jitter from OS scheduling. Jitter analysis is performed inside the Secure Enclave. Layer 4 — Attestation timestamp validation: if IMU data claims to be captured before the camera started recording, it is flagged as a spoofed replay. rPPG Bias Mitigation (Skin Tone & Camera Quality) Lighting Gate — Ambient lux is measured via camera histogram. If lux < 150, rPPG is skipped and weight redistributed to other signals. Fitzpatrick Classifier — A 400 KB one-frame model classifies skin tone on the forehead ROI. Fitzpatrick I–III uses green-channel primary; Fitzpatrick IV–VI uses red-channel primary with a 4-second extended averaging window for better SNR. Multi-Region Fusion — Forehead, left cheek, and right cheek are analyzed independently. A deepfake generates consistent artificial pulse; a real human shows natural cross-region variability. The Cross-Region Consistency Score (CRCS) feeds directly into the Trust Score. Camera Quality Compensation — On Tier 1, a noise-adaptive pre-filter calibrated to the specific camera sensor (from EXIF metadata) is applied. 15 FPS is accepted instead of 60 FPS. Device Recovery (Split-Key Architecture) If a device is lost, biometric templates are recoverable: Key Part A — Derived from the user's 8-word Recovery Code shown once at enrollment. Key Part B — Stored on V-Ident's server, associated with an anonymous ID (no PII). Neither key alone decrypts the template. Full recovery on a new device takes under 3 minutes: enter Recovery Code → server sends Key B → template decrypted locally → new hardware attestation generated → old attestation invalidated. ZK-Proof Privacy (Per-Service Nullifiers) Each ZK-proof contains a service-specific nullifier : a hash of the user's identity commitment combined with the service's unique domain ID. The same user gets a different nullifier for their bank, telecom, and government portal — preventing cross-service tracking while enforcing per-service uniqueness. Enrollment Flow Enrollment is a one-time, 8-step process. No video or face images ever leave the device. Step What Happens Privacy / Security Note 1. Device Profiling 3-sec benchmark: camera FPS, NPU throughput, TEE capability, RAM, root status Stored locally; only tier classification (T1/T2/T3) sent to server 2. Accessibility Declaration User optionally selects accessibility profile Encrypted in Secure Enclave; never sent to server 3. Guided 12-Sec Capture Front camera captures physiological signals. Instruction: "Keep face in oval and follow the white dot for 12 seconds" All processing on-device. No video transmitted. 4. Template Extraction M