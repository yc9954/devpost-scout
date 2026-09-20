---
slug: "neurocast-ai-autonomous-stroke-intervention-system"
url: "https://devpost.com/software/neurocast-ai-autonomous-stroke-intervention-system"
title: "Neurocast AI (Autonomous Stroke Intervention System)"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 1159
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Neurocast AI (Autonomous Stroke Intervention System)

> NeuroCast: Autonomous stroke intervention—safe, fast, anywhere.

[Devpost](https://devpost.com/software/neurocast-ai-autonomous-stroke-intervention-system) · hackathon [[NexHacks]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]]
  <sub>weak: on_device_local, simulation_digital_twin, vision_ocr</sub>
**domain** [[developer_tools]] [[health_clinical]]
  <sub>weak: elder_child_care</sub>
**user** [[patient_family]]
  <sub>weak: clinician, developer, legal_professional</sub>
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: medical_record, web_dom</sub>

**stack** ed25519), figma, google-gemini-api, kairo-api-(smart-contract-security-analysis), leanmcp-(mcp-server), next.js-(app-router), node.js, npm, overshoot.ai-sdk/api, radix-ui, react, server-sent-events-(sse), tailwind-css, the-token-company-(tokenco)-api

## Body

# NeuroCast AI — Agentic Stroke Coordination + Verified Transfer Packets > **One-line summary:** NeuroCast AI is an agentic, real-time stroke coordination layer that turns messy clinical inputs + remote video telemetry into **interpretable triage decisions** and a **NeuroCast Verified Transfer Packet (VTP)** that is verifiable, tamper-evident, and easy to share across care teams. --- ## Why I built this Stroke care is brutally time-sensitive. Minutes lost before a specialist even sees the patient translate into worse outcomes and higher cost. What bothered me most wasn’t “lack of AI”—it was **lack of coordination**: - The *same* information exists (notes, meds, timeline, vitals), but it’s scattered. - Early triage is inconsistent outside major centers. - Handoffs are often non-standard and hard to trust. I wanted to build something that feels like the future of healthcare operations: an **agent** that can watch real-time signals, summarize the truth, show its work, and produce a transfer artifact others can rely on. --- ## What it does (in human terms) NeuroCast AI is **not a diagnosis system**. It’s a **coordination + triage acceleration tool** that helps clinicians, coordinators, and caregivers answer: 1. **What happened?** 2. **Why does it matter?** 3. **What should happen next?** It provides: - **Agentic pipeline visibility** (every step emits events live so you see the “agent thinking”) - **Remote Home Check-In telemetry** via real-time video understanding (camera or uploaded video) - **Numeric decision workflow** for structured reasoning you can trust - **NeuroCast Verified Transfer Packet (VTP)**: a signed, hash-verifiable packet designed to be immutable/auditable over time --- ## How the system works ### 1) Inputs NeuroCast accepts two major input streams: - **Clinical inputs**: past surgeries, medication lists, EHR snippets, EMS notes, vitals, timeline events, imaging notes (messy text + structured data). - **Home Check-In telemetry**: real-time camera feed or uploaded video to capture symptoms and motion patterns remotely. ### 2) The agentic pipeline (visible end-to-end) The pipeline is built as discrete steps that emit a **live event stream**: - **INGEST**: normalize structured fields and attach case metadata - **REDACT**: remove PHI before any downstream processing - **COMPRESS**: TokenCo compresses messy text to reduce cost and focus on critical context - **EXTRACT**: derive evidence-backed risk flags (interpretable) - **NUMERIC**: Wood Wide AI performs numeric reasoning on structured/time-series features - **ROUTE**: deterministic gating into actionable next steps (e.g., HOLD / ESCALATE / PROCEED) - **PACKET**: generate the transfer packet - **VTP**: cryptographic verification + optional immutable commitment The event stream is delivered using **Server-Sent Events (SSE)** so the UI can render “agent actions” in real time. --- ## Sponsor tracks & how they’re used ### Overshoot.ai — Home Check-In (Real-time vision telemetry) I built **NeuroCast AI Home Check-In** to support remote monitoring: - A user can run a **live camera stream** or upload a **video file** - Overshoot runs a vision model over time windows and returns **text or JSON** - These detections can be interpreted into a triage signal and an alert payload This gives NeuroCast a “real-world perception layer” rather than only text inputs. ### Wood Wide AI — Numeric Trust Layer Wood Wide is used as the numeric reasoning engine for structured data: - Converts time-series and event features into stable numeric outputs - Enables consistent, interpretable numeric intelligence (prediction + clustering) - Helps produce a decision workflow that can be tested and monitored Instead of relying on an LLM to “do math,” numeric reasoning is handled by a dedicated layer designed for reliability. ### Kairo — Smart Contract Security Gate + Verifiability Architecture The **NeuroCast VTP** is designed to be committed into an immutable audit trail (on-chain or similar). Kairo is integrated as the security gate: - Before deploying or committing contract logic, Kairo runs **analysis** and returns a decision: - `ALLOW`, `WARN`, `BLOCK`, `ESCALATE` - This creates a “trust boundary” so we don’t ship unsafe contract code Even when commitment is simulated locally, the architecture is set up so Kairo can be placed in CI and deploy gates. ### Token Company (TokenCo) — Prompt compression for cost + speed Clinical text is often long and redundant. Compression helps: - Reduce token usage and latency - Retain the high-signal medical details - Keep downstream agent logic faster and cheaper ### TRAE AI IDE — How it was built TRAE was central to the workflow: - Iteration speed for full-stack changes - Rapid refactors across the UI + API routes - Tight feedback loop to keep the prototype functional I treated the IDE as an “AI development engineer” to keep momentum across multiple sponsor integrations. --- ## What I learned (the biggest takeaways) 1. **“Agentic” has to be visible to be believable.** Users trust a system more when they can see actions happening step-by-step. 2. **Numeric reasoning should not be done by text models.** LLMs are great for language, but decision-grade quantitative work needs deterministic outputs. 3. **Trust is a product feature, not just a security feature.** The Verified Transfer Packet is not “extra”; it’s what makes cross-org sharing realistic. 4. **Medical-adjacent demos require a safety posture.** Clear redaction rules + synthetic-only messaging matters for credibility. --- ## Challenges & how I overcame them ### 1) Port conflicts and multi-app structure The repo evolved with a prototype UI and a Next.js app router backend. Ensuring the frontend hit the right API routes required careful dev setup and consistent base URLs. ### 2) Real-time streaming reliability SSE is simple and reliable, but reconnect logic and event replay needed to be designed so demos wouldn’t break mid-stream. ### 3) Making sponsor integrations demoable Integrations only “count” if judges can see them. I had to push outputs into the UI: - TokenCo compression metrics - Wood Wide numeric outputs - VTP verification steps - Security-gate architecture for Kairo - Live telemetry feed for Overshoot ### 4) Safety constraints (PHI) I implemented an explicit REDACT step and a policy that raw packet text never becomes UI evidence or logging material. --- ## A tiny bit of math (why minutes matter) If the cost of delay scales roughly linearly, then: \[ \text{Cost Increase} \approx \$10{,}000 \times \left(\frac{t}{10\ \text{minutes}}\right) \] So a 20-minute reduction in “decision + reporting delay” is roughly: \[ \$10{,}000 \times 2 = \$20{,}000 \] This isn’t claiming exact savings per patient in all contexts—it's an intuition for why workflow acceleration has real economic impact. --- ## What’s next (post-hackathon) - Expand Home Check-In prompts + schemas to cover more symptom patterns (e.g., fall detection, confusion, speech difficulty). - Add alert routing integrations (care team paging, SMS, facility workflows). - Make VTP commitment real on a testnet and enforce Kairo gates in CI/CD. - Improve model calibration and interpretability of the numeric outputs with richer feature attribution. --- ## Closing NeuroCast AI is built around a simple idea: > Make the **right decision** easier to reach, faster to communicate, and easier to trust. That’s what the agentic pipeline + numeric trust layer + verified transfer packet is designed to deliver. <div