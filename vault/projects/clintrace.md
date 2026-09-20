---
slug: "clintrace"
url: "https://devpost.com/software/clintrace"
title: "ClinTrace"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 1103
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# ClinTrace

> ClinTrace is an AI agent that assists in emergency department triage — severity scoring, red-flag detection, specialist routing — with every reasoning step traced and auditable via Arize Phoenix.

[Devpost](https://devpost.com/software/clintrace) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[human_in_the_loop]] [[on_device_local]] [[sensor_fusion]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[geospatial]] [[medical_record]] [[sensor_telemetry]] [[structured_db]]

**stack** arize, gcp, google-bigquery, mcp, node.js, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clintrace

## Body

recalibration through phoenix feedback ( note annotations act as a feedback loop) quality assessment and why the agent made the call Audit reports Intake methods real CDC data surfaced through bigquery ClinTrace Inspiration Emergency departments operate at the intersection of chaos and consequence. A triage nurse seeing 50+ patients a shift has seconds to decide who gets seen first — and a wrong call can cost a life. AI tools for clinical settings are either black boxes that nobody trusts, or passive chatbots that just answer questions and leave the hard decisions entirely to humans. I wanted to build something in between: an agent that acts — routes patients, raises red flags, assigns acuity scores — but does so transparently, with every reasoning step on the record, and with nurses firmly in control of the final word. When I discovered that Arize Phoenix could make every agent decision inspectable and that nurse corrections could feed back into future cases through trace annotations, the idea turned into something tangible. The question I set out to answer: Can a nurse's override today make the agent smarter for the next patient with the same presentation? What it does ClinTrace is an action-taking ED triage agent. A nurse inputs symptoms, vitals, and history in natural language; the agent runs a directed clinical workflow and emits structured action cards: A routing order An ESI acuity score (1–5) Red-flag alerts for time-critical conditions (STEMI, stroke, sepsis) A human-review flag when confidence is low Every decision is logged as an OpenTelemetry span to Arize Phoenix Cloud, with a deep link from the report UI directly to the trace. Nurses can approve or override the ESI score and add a clinical note. Those overrides become Phoenix trace annotations — and on the next case with a protocol-aligned matching presentation, the agent reads that history and adjusts its confidence and ESI calibration accordingly. The loop closes without retraining the model. The intake UI ships four one-click demo cases (chest pain, stroke, sepsis, minor injury). A separate NHAMCS test lab pulls real CDC ED visit records from BigQuery (or local Stata files) for validation runs. How we built it ClinTrace runs on Google ADK 2.x ( google-adk==2.1.0 ) as a Workflow graph, deployed to Vertex AI Agent Engine in production with a FastAPI + Jinja nurse UI on Cloud Run. Default Pipeline (Production) The shipped configuration merges LLM steps and uses deterministic Python where possible to cut latency: Step Description Symptom Parser Structured extraction of chief complaint, vitals, and history. Clinical Assessor Merged ESI scoring (1–5) and red-flag screening in a single LLM call. Expand Clinical Splits merged output into severity_score and red_flags session keys. Specialist Router Determines ED destination, consults, and priority. Enforce Routing Deterministic safety guardrails (e.g., STEMI → cath lab, stroke → code stroke). Feedback Agent Queries Phoenix REST for complaint-matched prior nurse overrides and calibrates confidence and ESI (deterministic Python on the fast path; optional LLM agent when FAST_TRIAGE=false ). Deterministic Audit Builds the structured audit report and action cards from session state (no extra LLM call). Architecture & Observability Alternate Graph: An alternate configuration ( MERGE_TRIAGE_LLM_STEPS=false ) restores the original design: parallel severity_scorer + red_flag_detector synchronized by a JoinNode, followed by an LLM audit_reporter . Traceability: Every LLM step is instrumented with OpenInference and exported as OTel spans to Phoenix Cloud. The root span ( clinictrace.triage ) carries filterable attributes (complaint, keywords, ESI) powering similarity search. Nurse overrides are written as ground_truth_eval annotations via POST /api/triage/review and mirrored to the root span for the UI. Domain Reasoning: Lives in seven ADK Skills, inlined into prompts by default ( INLINE_SKILLS=true ) to avoid extra load-skill turns. Gemini 3.5 Flash on Vertex handles all pipeline reasoning. Validation: Tested against the CDC's NHAMCS public-use ED visit dataset, utilizing nurse immediacy (IMMEDR) as ground truth and critical under-triage as the primary safety metric. Challenges we ran into Feedback loop scope: Applying recent nurse overrides broadly created dangerous cross-contamination (e.g., alcohol overrides bleeding into chest-pain triage). We solved this via protocol-aligned calibration: overrides must pass complaint similarity, MTS-inspired protocol family checks, and pathway marker alignment in nurse notes. Phoenix annotation schema: The nested result structure for add_trace_annotation was unintuitive. A large portion of our integration time was spent understanding the difference between trace-level and span-level annotation endpoints to ensure UI visibility. Demo environment state: The self-improvement loop requires historical nurse annotations to work. We had to run representative override scenarios during prep so the feedback step had data to query, highlighting that feedback-loop systems are least impressive on their first run. Latency vs. auditability: The "five-step pipeline" was elegant but slow. Merging ESI/red-flag assessments, using deterministic audit tools, and inlining skills cut several LLM round-trips without sacrificing Phoenix spans. Accomplishments that we're proud of Protocol-aligned, complaint-matched calibration: Nurse overrides only influence future cases that share a presenting-complaint protocol family and pass pathway-marker checks. This keeps the feedback loop clinically safe. Full per-step traceability: Every pipeline node is a span. A user can open any triage run to see exactly why an ESI was assigned, the red flags detected, and the prior overrides that influenced it. NHAMCS validation: Evaluated against real CDC ED visit data using critical under-triage as a safety metric, explicitly excluding diagnosis codes from the prompt. Closed feedback loop without retraining: The model's behavior improves dynamically based on trace annotations and runtime calibration. Production-shaped deploy: Leverages Agent Engine, Cloud Run, Phoenix Cloud, and an optional BigQuery lab, all runnable locally via InMemoryRunner . What we learned Observability is the infrastructure for trust: In high-stakes environments, un-auditable AI cannot be deployed. Phoenix traces turned every step into a paper trail—the fundamental premise of the entire system. Workflow graphs fit clinical systems: Google ADK's Workflow forced us to be explicit about state dependencies between steps, crucial for real-world patient routing. Careless feedback loops are dangerous: A system that doesn't meticulously scope its signals is worse than one with no feedback at all. The pathway-marker work prevented the system from silently drifting into error. What's next for ClinTrace Quantitative calibration reporting: Surface override rates and ESI accuracy deltas per complaint category directly in the UI. Broader NHAMCS evaluation: Expand spot checks into full-dataset validations via the batch runner to publish complaint-category benchmarks. Shift-level feedback aggregation: Aggregate a full shift of corrections and apply updates at handoff to minimize noise from single outlier overrides. Integration with real EHR intake: Replace manual free-text input with structured HL7 FHIR feeds from existing ED systems. Formal IRB pathway: The full traceability, human-in-the-loop design, and protocol-scoped learning architectures are built specifically to support a regulated clinical validation study. <div