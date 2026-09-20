---
slug: "mdt-assemble"
url: "https://devpost.com/software/mdt-assemble"
title: "Agentic Multidisciplinary Tumor Board (AMDT)"
hackathon: "Agents Assemble - The Healthcare AI Endgame"
organization: "Prompt Opinion (Darena Health)"
winner: true
words: 731
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# Agentic Multidisciplinary Tumor Board (AMDT)

> Orchestration that uses A2A agents to synthesize unstructured FHIR pathology & radiology data into instant Tumor Board briefs. We eliminate hours of manual prep to accelerate cancer treatment.

[Devpost](https://devpost.com/software/mdt-assemble) · hackathon [[Agents Assemble - The Healthcare AI Endgame]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[provenance_signing]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[developer_tools]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[developer]] [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[genomic_bio]] [[geospatial]] [[medical_record]] [[structured_db]]

**stack** python

## How they structured the write-up

- what inspired me
- how i built it (the architecture)
- challenges i faced
- what i learned
- what's next for amdt

## Body

Problem Current Solution Architecture Diagram Architecture Design & Guardrails Final Notes Agentic Multidisciplinary Tumor Board (AMDT): The Neuro-Symbolic Tumor Board Orchestrator What Inspired Me In oncology, Time-to-Treatment Initiation (TTI) is a matter of life and death. Yet, at community cancer centers worldwide, patients wait weeks just for their cases to be reviewed at a Multidisciplinary Tumor Board (MDT). Why? Because a highly trained oncology fellow or nurse navigator must spend 45 to 90 minutes per patient digging through the EHR, manually synthesizing dense, unstructured pathology and radiology PDFs into a cohesive presentation. It is unbillable, soul-crushing data entry that artificially caps a hospital's throughput. When observing the current landscape of Healthcare AI, I noticed a fatal flaw: developers are trying to use LLMs to diagnose and calculate medical staging. In oncology, guessing an AJCC Cancer Stage via probabilistic text generation is a catastrophic liability. I was inspired to build AMDT to bridge this gap. I wanted to democratize precision medicine by creating a system that uses Generative AI purely as a high-speed reader, while delegating all medical calculations to strict, deterministic code—ultimately slashing MDT prep time from 90 minutes to 20 seconds. How I Built It (The Architecture) AMDT was built at the intersection of Prompt Opinion's A2A protocol , SHARP FHIR Context , and a custom Python FastMCP backend. 1. Multi-Agent Composability Instead of a monolithic chatbot, I deployed a specialized team of agents: The Pathology Sub-Agent: Constrained via strict JSON Schema prompting to read Base64-encoded FHIR DiagnosticReports and extract histology and biomarkers (e.g., EGFR, PD-L1). The Radiology Sub-Agent: Extracts primary tumor size ($T$), nodal involvement ($N$), and metastasis ($M$). The MDT Coordinator: The orchestrator that delegates tasks sequentially and synthesizes the final report. 2. Hybrid Neuro-Symbolic Logic (The AI Factor) To ensure FDA CDS Exemption Compliance , the AI is explicitly forbidden from calculating the cancer stage. Instead, the Coordinator agent passes the extracted variables into a deterministic FastMCP Python tool: $$ \text{Clinical Stage} = f_{\text{AJCC}}(T, N, M) $$ By mapping continuous unstructured data to discrete logic gates, we eliminate hallucination risk. The system then queries a local Retrieval-Augmented Generation (RAG) engine containing NCI PDQ guidelines to retrieve the exact standard-of-care pathway. 3. Bidirectional Interoperability (Closing the Loop) A read-only AI is just a toy. Once the Tumor Board Brief is generated, the Coordinator uses a specialized save_tumor_board_note MCP tool. It base64-encodes the Markdown and executes a POST request to the FHIR database, saving it as a DocumentReference with an explicit attestation block for human sign-off. Challenges I Faced 1. The A2A Concurrency Choke Initially, I designed the Coordinator to query the Pathology and Radiology agents in parallel. However, simultaneous LLM handoffs triggered massive rate-limiting spikes (HTTP 429s). I had to meticulously engineer the Coordinator’s System Prompt to enforce strict, sequential A2A routing—forcing the orchestrator to await an explicit JSON payload from Agent $A$ before calling Agent $B$. 2. The Pydantic/Rust Serialization Wall To achieve a Zero-Trust, Least-Privilege security model, the MCP server needed to dynamically inject Prompt Opinion's proprietary ai.promptopinion/fhir-context extensions during the initialization handshake to request specific SMART on FHIR scopes (e.g., Patient.rs , DocumentReference.write ). Because the modern MCP SDK uses Pydantic V2 (which serializes directly via a Rust core), standard Python monkey-patching failed. I had to build a custom ASGI Network Byte Interceptor in Starlette to intercept the raw outbound TCP stream, decode the JSON, inject the proprietary capabilities mid-flight, and pass the strict CSRF/Host validations to successfully establish the tunnel. What I Learned Cryptographic Provenance is King: Doctors don't trust black boxes. I learned how to build strict traceability by forcing the LLM to embed the exact source_report_id (the FHIR Document ID) inline for every clinical finding. FHIR Transaction Rules: I gained a deep understanding of FHIR R4 Transaction Bundles, specifically how to use temporary urn:uuid: schemas to link Patient , Condition , and DiagnosticReport resources perfectly in a single POST payload. What's Next for AMDT The modular A2A architecture means this system has infinite composability. The immediate next step is ecosystem integration: updating the MDT Coordinator to automatically hand off the finalized cancer stage and biomarkers to 3rd-party registry agents on the Prompt Opinion Marketplace (such as clinical trial matchers) without rewriting the core engine. By reclaiming $\approx 40$ hours of unbillable specialist time per week, AMDT doesn't just save hospital overhead—it fundamentally accelerates Time-to-Treatment Initiation, improving survival outcomes for patients worldwide. <div