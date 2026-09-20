---
slug: "dealforge-ub8mjf"
url: "https://devpost.com/software/dealforge-ub8mjf"
title: "DealForge"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 981
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/social_worker"
  - "substrate/document_pdf"
---

# DealForge

> DealForge turns messy commercial handoffs into trusted, signed agreements by separating AI interpretation from commercial authority, human approval, and Doctavian execution.

[Devpost](https://devpost.com/software/dealforge-ub8mjf) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[retail_commerce]] [[supply_logistics]]
**user** [[social_worker]]
**substrate** [[document_pdf]]

**stack** doctavian-api, gemini, google-vertex-ai, next.js, node.js, react, tailwind-css, typescript, vitest, zod

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what makes dealforge different
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next
- where doctavian did the real work

## Body

Deterministic commercial truth: DealForge computes the authoritative €104,332.80 contract value. AI evidence stays separate from authority, with confidence, provenance, and ambiguity visible. Draft does not mean Send: EMAIL SENT is NO until explicit human authorization. Doctavian reports Envelope Completed and Signer Completed before signed-contract retrieval. Trusted Execution Trace records signing, reconciliation, and signed PDF retrieval as observable events. Inspiration Commercial agreements rarely begin as clean structured data. They begin as sales notes, pricing fragments, customer requirements, discounts, payment terms, compliance requests, localization instructions, and incomplete handoffs between people and systems. AI can extract plausible facts from that information, but plausible is not the same as authoritative. That became the central question behind DealForge: How can AI help understand a messy deal without quietly becoming the source of truth for the agreement itself? What it does DealForge turns messy commercial evidence into a trusted, generated, digitally signed agreement. A user submits an unstructured sales handoff. Gemini through Vertex AI extracts candidate deal facts together with confidence and provenance. Those results are treated as evidence — not authoritative business state. DealForge then resolves application-owned product identities, validates a canonical DealManifest, computes the commercial values deterministically, and evaluates whether the agreement is READY, requires REVIEW, or must be BLOCKED. Only a READY agreement can be generated. In the demo, DealForge processes an enterprise agreement for 120 seats at EUR 79 per seat per month, EUR 4,800 annual support, a 12-month term, and a 12% discount. DealForge — not the language model — computes: Subtotal: EUR 118,560.00 Discount: EUR 14,227.20 Final agreement value: EUR 104,332.80 Once the deal is trusted, DealForge calls Doctavian to generate the real contract PDF. But generation is deliberately not the same as sending. DealForge first creates the signature envelope as a Draft and explicitly shows: EMAIL SENT: NO Sending the signature request is treated as a consequential external action and requires explicit human authorization. Only after that approval does DealForge send the request through Doctavian. The signer completes the real Doctavian signing workflow, DealForge reconciles the external envelope and signer state back to COMPLETED, and only then allows retrieval of the signed PDF. How I built it DealForge is built with Next.js, React, TypeScript, Gemini through Google Vertex AI, Zod, and the Doctavian APIs. The system deliberately separates three different kinds of information: AI Evidence — candidate facts, confidence, provenance, and ambiguity. Authoritative Deal State — application-owned product identities, canonical deal data, readiness policy, and deterministic financial calculations. External Execution — document generation and signature operations performed through Doctavian. Authoritative money is calculated using integer minor units rather than model-generated totals. Trusted workflow state is carried across mutations through a tamper-evident HMAC-sealed workflow token. Before generation, Draft creation, sending, and signed-document retrieval, DealForge re-opens and verifies the trusted state rather than accepting authoritative commercial data back from the browser. The Trusted Execution Trace records observable application and provider events such as extraction, provenance anchoring, money computation, generation, human authorization, signing, reconciliation, and signed-artifact retrieval. It deliberately represents operational evidence rather than hidden model reasoning. What makes DealForge different The core idea is not simply to generate a contract with AI. It is to make authority explicit. AI interprets. DealForge establishes commercial truth. Humans authorize consequential actions. Doctavian generates and signs. That separation is the product. An AI model is useful without being allowed to invent internal product identities, calculate authoritative totals, decide readiness, send external signature requests, or declare provider completion. Challenges we ran into One challenge was modelling recurring commercial pricing correctly. The agreement combines monthly seat pricing with annual support, so DealForge had to model price cadence explicitly and compute the contract value deterministically without allowing implicit or model-invented proration. Another challenge was Doctavian's document-storage lifecycle. During integration testing I learned that temporary uploaded template and data references must be treated as ephemeral, so DealForge uploads fresh generation inputs immediately before generating the document. The signature workflow introduced another important boundary: creating an envelope and sending an external email are not the same operation. I modelled Draft creation and Send as separate application actions and placed explicit human authority between them. I also had to reconcile distributed state because the signing provider can advance while the browser still holds an older workflow state. DealForge therefore observes Doctavian's state and reconciles it back into its trusted workflow. Accomplishments that we're proud of The strongest result is the complete trusted path rather than an isolated API call. DealForge successfully goes from: messy commercial intake → AI extraction → provenance → deterministic commercial truth → READY → real Doctavian generation → signature Draft → explicit human authorization → real Doctavian signing → automatic reconciliation → COMPLETED → digitally signed PDF. The final demo reaches a real signed artifact rather than ending with a simulated success screen. What we learned The biggest lesson was that responsible AI workflows are often less about making the model smarter and more about designing authority correctly. A model can interpret information without being allowed to make it authoritative. A provider can execute an external action without owning commercial truth. A human can authorize the consequential boundary without manually performing the entire workflow. Making those roles explicit produced a much stronger system than a simple prompt-to-document pipeline. What's next The hackathon build intentionally focuses on one complete trusted execution path. The next version would add durable deal and workflow persistence, distributed idempotency, larger controlled product catalogs, multi-signer and sequential approval policies, organization and role boundaries, CRM ingestion, exception-review queues, contract version comparison, and long-term agreement lifecycle management. The principle would remain unchanged: AI may interpret the deal. It does not get to silently become the deal. Where Doctavian did the real work Doctavian did the real document execution — generating the contract from DealForge's trusted commercial state, carrying it through digital signing, reporting completion, and returning the signed PDF instead of DealForge simulating those external steps. <div