---
slug: "a2a-mediflow-ai-healthcontext-ai"
url: "https://devpost.com/software/a2a-mediflow-ai-healthcontext-ai"
title: "A2A-MediFlow"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 585
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
---

# A2A-MediFlow

> Agent to Agent Flow

[Devpost](https://devpost.com/software/a2a-mediflow-ai-healthcontext-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]]
**domain** [[health_clinical]]
  <sub>weak: developer_tools</sub>
**user** [[patient_family]]
**substrate** [[geospatial]] [[medical_record]] [[sensor_telemetry]]

**stack** agent, agent-to-agent, apis, backend, configuration, core, customagent, data, deployment, design, deterministic, devops, external, fhir

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- inspiration:
- context handling

## Body

A2A-MediFlow AI: Intelligent Prescription & Risk Orchestration: Inspiration Healthcare workflows often involve fragmented systems—clinical notes, lab reports, prescriptions, and compliance policies exist in silos. This project was inspired by the need to: unify clinical decision support automate prescription generation integrate risk detection with real-time patient data ensure compliance with healthcare policies like HIPAA What it does Generates structured prescriptions based on clinical conditions Calculates risk factors (e.g., hypertension, cholesterol risks) Uses FHIR APIs to retrieve patient context securely Applies policy-aware logic for safer outputs Demonstrates Agent-to-Agent orchestration for modular AI systems How we built it Architecture A2A (Agent-to-Agent) flow: GeneralChatAgent → External Agent → Tools → LLM Components PrescriptionServiceAgent generate_prescription_tool calculate_risk_factors_tool LLM gemini-2.5-flash for reasoning + formatting FHIR Integration Secure API-based patient data retrieval Middleware Handles authentication (API key) Injects FHIR context App Layer app.py, app_factory.py ngrok for external access Challenges we ran into FHIR data inconsistency: Multiple observations with conflicting values (e.g., triglycerides) Sorting issues: FHIR _sort not reliable across servers Agent orchestration complexity: Managing tool outputs + LLM reasoning cleanly Balancing determinism vs LLM: Avoiding hallucination in prescriptions Security concerns: Handling PHI safely with API-based context Accomplishments that we're proud of Built a modular A2A healthcare agent system Integrated FHIR with AI agents Achieved deterministic + LLM hybrid design Added risk-aware prescription generation Created a scalable multi-agent architecture pattern What we learned FHIR data requires client-side validation + sorting LLMs should format, not decide critical medical data Tools provide ground truth, LLM provides presentation Agent orchestration improves scalability + separation of concerns Healthcare AI must prioritize: accuracy compliance explainability ## What's next for A2A MediFlow AI Add Drug Interaction Checker Agent Expand to multi-patient workflows Add clinical guideline validation Implement FHIR write-back (MedicationRequest resource) Deploy on OpenShift / Kubernetes with AI Orchestrator ------------------------------------------------------------------------------------------------------------------ Project 2-MCPHealthContextOctopus AI: MCP-Powered Patient Insight Engine: Inspiration: Healthcare data is often scattered across multiple systems—lab results, vitals, and clinical records are not unified. This project was inspired by the need to: create a single source of truth for patient health context enable dynamic tool discovery via MCP integrate FHIR-compliant healthcare data with AI agents reduce manual effort in interpreting patient data What it does Retrieves patient data using FHIR APIs Exposes clinical tools via MCP server Aggregates: Blood Pressure Cholesterol Triglycerides Builds a structured patient health context Enables A2A + MCP hybrid architecture Uses LLM (Grok / Gemini) for reasoning and summarization How we built it Core Architecture Custom Agent → MCP Server → Tools → FHIR API pipeline Pipeline Components Agent Layer PatientHealthContextAgent System prompt-driven context builder MCP Server (mcp-health-context-server) Tool mapping layer Exposes: GetPatientBloodPressure GetPatientCholesterol GetPatientTriglycerides FHIR Layer fhir_client.py API-based retrieval using secure token Utilities mcp_utilities.py → response formatting mcp_instance.py → MCP server initialization API Layer FastAPI ngrok for external exposure Context Handling FHIR context injected via middleware / environment Challenges we ran into Unable to fetch latest data uploaded FHIR returned older observations instead of latest _sort was unreliable across server implementations Required manual sorting using effectiveDateTime MCP Tool Mapping Complexity Mapping tools dynamically to MCP server required careful design Ensuring consistent input/output contracts Data Consistency Issues Multiple records for same metric (e.g., triglycerides) Needed validation and filtering (final vs preliminary) Context Propagation Passing FHIR context correctly across agent → MCP → tools Accomplishments that we're proud of Built a custom MCP server for healthcare tools Successfully integrated FHIR APIs with AI agents Enabled dynamic tool usage via MCP skills layer Created a scalable multi-agent + MCP architecture Solved real-world issue of clinical data inconsistency <div