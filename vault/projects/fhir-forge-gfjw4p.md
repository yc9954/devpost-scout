---
slug: "fhir-forge-gfjw4p"
url: "https://devpost.com/software/fhir-forge-gfjw4p"
title: "FHIR Forge"
hackathon: "Agents Assemble - The Healthcare AI Endgame"
organization: "Prompt Opinion (Darena Health)"
winner: true
words: 1219
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/medical_record"
---

# FHIR Forge

> Transforms clinical notes, discharge summaries, and referrals into validated FHIR R4 resources with RxNorm, ICD-10, and LOINC grounding, clinician review, interactive edits, and approval-before-write.

[Devpost](https://devpost.com/software/fhir-forge-gfjw4p) · hackathon [[Agents Assemble - The Healthcare AI Endgame]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[structural_withholding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[medical_record]]

**stack** claude-agent-sdk, fhir, hapi, mcp, node.js, prompt-opinion, typescript, vite

## How they structured the write-up

- why this matters
- the ai factor
- what it does
- real clinical reasoning
- built for real healthcare systems
- architecture
- challenges we solved
- potential impact
- what we learned
- built with

## Body

Simply drop unstructured clinical data into the PO chat The agent extracts clinical entities and maps them to grounded medical codes automatically Review, refine, and apply AI or custom suggestions After review, seamlessly write validated entities back to your EHR system FHIR Forge Transforming Clinical Documents into Safe, Structured FHIR Records Healthcare runs on unstructured documents. Every day, hospitals generate discharge summaries, referral letters, scanned PDFs, and free-text notes containing critical patient information: new diagnoses, medication changes, allergy updates, lab findings, and follow-up plans. But most of that information never reaches the structured patient chart. Instead, clinicians manually re-enter data into the EHR, a slow, expensive workflow that creates incomplete records, safety gaps, and downstream failures for both humans and AI systems. FHIR Forge fixes that. FHIR Forge uses grounded generative AI agents to convert unstructured clinical documents into validated FHIR R4 resources, with full provenance, terminology grounding, chart-aware merging, and clinician review before anything is written to the EHR. Why This Matters Healthcare AI does not primarily have a model problem. It has a data problem. Modern AI systems can reason well, but they are often connected to incomplete patient charts because the majority of clinical information still lives inside narrative documents that computers cannot reliably structure. A severe penicillin allergy buried inside a discharge summary is invisible to downstream clinical systems until someone manually updates the chart. FHIR Forge closes that gap. Rather than replacing clinicians, the system is designed to make high-trust clinical review possible: AI handles extraction, terminology grounding, and FHIR structuring. Clinicians retain final judgment and approval authority. The AI Factor This problem cannot be solved reliably with traditional rule-based software. Clinical notes are highly variable: abbreviations differ between hospitals, diagnoses are implied rather than explicitly stated, medication changes depend on context, and terminology mapping is inherently ambiguous. For example, an HbA1c lab can map to multiple valid LOINC codes depending on methodology and wording. FHIR Forge uses specialized generative AI agents to interpret clinical meaning from messy narrative text, reason about terminology candidates, reconcile findings against the existing chart, detect superseding clinical states, and generate standards-compliant FHIR resources. But the AI is constrained at every critical step: Constraint Detail Terminology codes Must come from authoritative APIs Resource validation All resources pass HAPI FHIR validation Provenance Every extracted value links back to source text Write access Nothing is written without clinician approval The model can choose between real clinical candidates. It cannot invent unsupported medical codes. What It Does FHIR Forge processes clinical documents through a six-stage AI pipeline: 1. Extract Clinical entities are identified from the source document: conditions, medications, and allergies lab observations and referrals follow-up plans Every entity preserves the exact source text that produced it. 2. Ground Each extracted entity is matched against real terminology systems: RxNorm , SNOMED CT , ICD-10-CM , and LOINC . The system retrieves valid candidates from terminology APIs and asks the model to select the best fit, with reasoning preserved for auditability. 3. Build Grounded entities are transformed into typed FHIR R4 resources and assembled into a transaction Bundle. 4. Validate HAPI FHIR $validate runs against the generated resources before anything reaches the chart. 5. Review Clinicians review: the generated FHIR resource and grounded terminology, provenance text and merge/update decisions, and AI-flagged refinements. 6. Approve The final transaction Bundle is written atomically into the EHR. Real Clinical Reasoning FHIR Forge does more than simple extraction. The system performs chart-aware reconciliation against existing patient data. Examples include: recognizing that a severe penicillin allergy supersedes an existing moderate allergy record, detecting that losartan replaces lisinopril instead of creating duplicate medications, separating uncertain diagnoses from valid referrals, and surfacing clinically relevant missing documentation for human review rather than fabricating it automatically. FHIR resource history preserves previous states automatically, maintaining a full audit trail over time. Built for Real Healthcare Systems FHIR Forge is designed around real interoperability and healthcare standards from day one: FHIR R4 transaction Bundles SMART-on-FHIR scopes HAPI validation Terminology-grounded coding Provenance tracking Atomic chart writes The architecture is stateless : no patient data is persisted on the MCP server, only the minimum de-identified clinical context required for processing is handled, and authorization flows directly from the host clinical platform. FHIR Forge runs as an MCP server integrated into the Prompt Opinion platform, using MCP (Model Context Protocol), SMART-on-FHIR scope semantics, and scoped FHIR access delegated from the host platform. ⚡ Processes a real discharge summary in under one minute at a cost of approximately $0.05 per document . This is not a mock architecture or speculative workflow. The demo runs against a real FHIR backend using real healthcare standards end-to-end. Architecture FHIR Forge uses a small multi-agent architecture built on the Claude Agent SDK . The orchestrator delegates work across three specialist agents: Orchestrator ├── Extractor Agent → identifies structured clinical entities from unstructured text ├── Grounder Agent → resolves entities against authoritative terminology systems └── Builder Agent → generates validated FHIR R4 resources and transaction Bundles The orchestrator itself never performs clinical reasoning directly. Each agent has a tightly constrained role, minimal tool surface, and strict output contract. The clinician review experience is built using MCP Apps , allowing the same MCP tool that executes the pipeline to render a fully interactive review UI directly inside the host platform. Challenges We Solved Terminology Ambiguity Clinical terminology mapping is rarely one-to-one. HbA1c, for example, has multiple valid LOINC representations depending on methodology and reporting standard. FHIR Forge retrieves real candidates from terminology APIs and constrains the model to selecting among valid options while recording reasoning into provenance. Chart-Aware Updates Healthcare data changes over time. A severe allergy update should modify an existing clinical record rather than create duplicates. FHIR Forge reads the patient chart before writing, allowing the system to detect superseding states, preserve longitudinal history, and generate proper update semantics within FHIR transaction Bundles. Embedded Clinical Review The review surface is not a mockup. Using MCP Apps, clinicians can inspect provenance, accept or reject findings, review merges, remove out-of-scope extractions, and approve atomic chart writes directly inside the host workflow. Potential Impact The United States produces 1.2 billion clinical documents every year and approximately 60% of them contain critical patient information trapped in unstructured form, invisible to clinical systems, quality measurement, and downstream AI. FHIR Forge enables healthcare systems to: reduce manual charting workload, improve completeness of structured patient data, strengthen downstream clinical AI systems, reduce medication and allergy safety gaps, and accelerate interoperability across fragmented systems. The system is especially valuable because it improves both human clinical workflows and the quality of data powering future healthcare AI . What We Learned Tool grounding is a structural safety mechanism , not a prompt-engineering trick. Provenance matters more to clinicians than raw AI output. Clinician review is not a fallback : it is the product. MCP is an excellent interoperability layer for clinical AI tooling. Real healthcare AI systems need standards-first architecture from day one. Built With Category Technologies Language TypeScript AI / Agents Anthropic Claude Haiku 4.5, Claude Agent SDK, Model Context Protocol (MCP), MCP Apps Server Node.js, Express, Zod Frontend React 19, Vite Healthcare Standards FHIR R4, SMART-on-FHIR, RxNorm, ICD-10-CM, LOINC, SNOMED CT Validation HAPI FHIR $validate Terminology APIs RxNav, NLM Clinical Tables, LOINC Search, SNOMED CT Browser Platform Prompt Opinion <div