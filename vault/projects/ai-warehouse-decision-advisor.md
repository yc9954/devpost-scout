---
slug: "ai-warehouse-decision-advisor"
url: "https://devpost.com/software/ai-warehouse-decision-advisor"
title: "FlowMind"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 568
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "substrate/sensor_telemetry"
---

# FlowMind

> An operational reasoning and stabilization co-pilot for warehouse systems.

[Devpost](https://devpost.com/software/ai-warehouse-decision-advisor) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[health_clinical]] [[supply_logistics]]
**substrate** [[sensor_telemetry]]

**stack** amazon-nova, amazon-web-services, boto3, huggingface, novalite, pandas, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for ai warehouse decision advisor

## Body

Architecture diagram Inspiration Modern warehouse systems generate thousands of operational signals — lift utilization, zone starvation, Scratch rate, pick latency, demand deltas. But during new software rollouts or demand shifts, teams struggle not because of missing data, but because of slow interpretation. I am inspired by a simple problem: How can I help operations teams reason about multi-metric system behavior faster — without handing control to AI? Instead of building an autonomous optimizer, I built a reasoning co-pilot that explains risk, detects instability patterns, and suggests software-level corrective actions — especially during post-go-live stabilization. What it does AI Warehouse Decision Advisor is an operational reasoning layer for warehouse systems. It: Calculates deterministic risk scores in the backend Ingests structured operational metrics Interprets cross-metric causality Identifies instability patterns Recommends corrective actions limited to software and scheduling changes Avoids suggesting unrealistic hardware interventions Designed specifically for below scenarios: Post-go-live stabilization Demand surge diagnostics Control logic bias detection Capacity stress interpretation Importantly, it does not make decisions or change system configurations. It acts as a reasoning accelerator for human operators. How I built it The architecture separates control from interpretation: Deterministic Backend Layer I compute: $$R = \sum_{i=1}^{n} w_i \cdot \frac{|x_i - x_{\text{ideal}}|}{|x_{\text{critical}} - x_{\text{ideal}}|}$$ Where: $R$ = composite risk score $w_i$ = weight of metric $i$ $x_i$ = current metric value $x_{\text{ideal}}$ = ideal SLA target $x_{\text{critical}}$ = critical SLA threshold This ensures: ✅ Transparency — every score is traceable ✅ Repeatability — same inputs always produce same outputs ✅ No hallucinated math ✅ Enterprise-safe outputs AI Interpretation Layer I pass structured metrics and calculated risk into a constrained LLM prompt that: Explains why the risk is high or low Identifies causal relationships between metrics Recommends corrective strategies Is restricted from suggesting hardware expansion Is restricted from inventing thresholds or new data This separation ensures the AI reasons over validated data without becoming the control system. Challenges I ran into Preventing generic AI responses like "add more lifts" Constraining the solution space to realistic operational levers Designing prompts that avoid hallucinated metrics or thresholds Ensuring the AI interprets, rather than recalculates, risk Framing the system clearly as a reasoning layer, not an optimizer We realized early that without strict constraints, AI defaults to textbook capacity advice instead of real warehouse logic. Accomplishments that I am proud of Designed a deterministic + AI hybrid architecture Prevented AI from making operational control decisions Built a structured risk scoring framework: $R = \sum w_i \cdot r_i$ Created a prompt design that avoids hardware fantasy solutions Reframed AI from "optimizer" to "stabilization co-pilot" Most importantly, we built something that feels realistic for enterprise deployment — not just a demo. What I learned AI is powerful at cross-metric reasoning, not deterministic control Clear architectural boundaries are critical in operational environments Constrained prompts dramatically improve solution quality During system transitions (go-live, demand surge), interpretation speed is more valuable than raw data We also learned that AI is most useful when it accelerates human engineering judgment — not when it replaces it. What's next for AI Warehouse Decision advisor Integrating real-time metric streaming Adding anomaly detection over time-series data Building a feedback loop where operator decisions improve reasoning quality Expanding to additional warehouse automation systems Developing a dashboard for visual risk decomposition Incorporating scenario simulation ("What if demand increases 20%?") Long term, we envision this becoming a commissioning and stabilization intelligence layer for warehouse automation systems. <div