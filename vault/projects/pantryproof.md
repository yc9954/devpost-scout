---
slug: "pantryproof"
url: "https://devpost.com/software/pantryproof"
title: "PantryProof"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 906
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# PantryProof

> PantryProof uses Nutrient and SerpApi to turn fragmented recall evidence into cited, human-reviewed actions and a replayable closure packet for every partner pantry.

[Devpost](https://devpost.com/software/pantryproof) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]]
**domain** [[agriculture_food]] [[finance_payments]] [[housing_homeless]] [[security_privacy]] [[supply_logistics]] [[transportation]]
**user** [[legal_professional]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[web_dom]]

**stack** actions, ai, api, css3, data, document, dws, extraction, food, generation, github, google, html5, javascript

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges
- accomplishments
- what was learned
- what's next

## Body

Audit log of PantryProof Live APIs: SerpApi, Nutrient Data Extractor and Nutrient Processor Recall case of PantryProof Responses and Evidence of PantryProof Inspiration Food banks and partner pantries form the “true last mile” of a food recall. Products may arrive through central distribution, retail rescue, local purchasing, food drives, and other paths. Partner agencies may operate intermittently or rely on volunteers, so sending an alert does not prove that the affected product was found, contained, or communicated downstream. PantryProof was built around a simple question: How can a food bank prove that every partner completed the correct recall response without letting an uncertain AI prediction make the final safety decision? What it does PantryProof converts fragmented recall notices, pantry inventories, donation records, and response actions into one evidence-first closure workflow. Discover: SerpApi retrieves current, structured recall evidence from Google News. An official-focused mode limits results to FDA and USDA domains. Extract: Nutrient Data Extraction converts recall notices and partner inventory documents into schema-shaped fields with citation metadata. Review: Extracted information remains a preview until a coordinator explicitly approves it. Reconcile: A deterministic engine compares normalized UPC/GTIN and lot identifiers across partner inventory. Respond: Ambiguous records require a human decision. Affected inventory requires a recorded quarantine, disposal, or return action, and distributed units require downstream-notification confirmation. Close: Closure remains locked until every identity decision and response action is complete. Prove: Nutrient Processor generates a PDF containing agency reconciliation, the audit trail, policy version, and a SHA-256 evidence-manifest digest. The application includes a visibly fictional demo case, so judges can evaluate the complete workflow without credentials or real pantry data. When sponsor credentials are configured, each live capability activates independently, and failures are shown instead of silently substituting demo output. How it was built The browser experience is built with TypeScript, JavaScript, semantic HTML, and responsive CSS. A deterministic TypeScript domain engine owns identifier normalization, matching policy, agency aggregation, human review state, response completeness, and closure readiness. Vercel serverless functions provide four hardened API boundaries: /api/search integrates SerpApi for current recall discovery. /api/extract sends validated PDF, PNG, or JPEG documents to Nutrient Data Extraction. /api/build-packet independently revalidates closure and calls Nutrient Processor to generate the final PDF. /api/health reports whether each sponsor capability is configured without exposing credentials. Uploads are bounded and checked for extension, MIME agreement, canonical base64, size, and file-signature bytes. Search URLs reject embedded credentials. Generated PDFs must have a PDF content type, remain under the configured limit, and begin with a valid %PDF- signature. Where Nutrient DWS does the heavy lifting Nutrient DWS extracts schema-shaped, source-cited fields from messy recall and inventory documents, then generates the final PDF only after PantryProof’s deterministic and human-controlled closure gates succeed. Nutrient extraction uses fixed recall and inventory schemas, understand parsing mode, and citation output. PantryProof preserves page and source-region metadata while keeping the result outside the active safety workflow until a person approves it. How SerpApi is used SerpApi supplies structured, current Google News recall results ordered newest first. PantryProof validates every returned URL, determines evidence tier from the actual hostname rather than an untrusted label, and allows a coordinator to attach a reviewed result as canonical evidence. This makes web search part of a traceable evidence workflow instead of treating the first search result as truth. Challenges The hardest challenge was separating probabilistic document understanding from deterministic safety policy. AI extraction is useful for finding fields in inconsistent documents, but confidence is not permission to declare a product affected or safe. PantryProof therefore introduces an explicit human promotion boundary and requires exact normalized UPC/GTIN and lot matches for automatic affected status. Brand and description similarity can only send a record to review. Another challenge was preserving citations beyond the extraction screen. PantryProof carries document, page, and source-region metadata into agency reconciliation so operators can inspect the evidence behind each decision. The final challenge was making sponsor integrations honest and failure-aware. Nutrient extraction, Nutrient PDF generation, and SerpApi discovery have separate server-only credentials and capability states. The application never hides an unavailable integration behind fabricated live output. Accomplishments Built a complete discovery-to-closure workflow rather than an isolated API demonstration. Integrated two Nutrient DWS capabilities: cited data extraction and PDF generation. Integrated SerpApi as current, structured evidence discovery. Kept uncertain AI output behind explicit human approval. Implemented exact identifier policy, identity-review gates, containment requirements, and downstream-notification requirements. Added independent server-side closure validation and a SHA-256 manifest digest. Created a safe fictional case that demonstrates the product without exposing real pantry or recipient information. Passed strict TypeScript checking, syntax validation, repository hygiene checks, all 26 automated tests, and the dependency audit. What was learned Trustworthy AI is not created by presenting a confidence score. It comes from architecture: preserve the source, expose uncertainty, constrain automation, require human authority at consequential boundaries, and validate the final output independently. The project also reinforced that recall closure is not a single status. It is a chain of evidence connecting discovery, document fields, identifiers, partner decisions, physical containment, recipient communication, and a replayable record. What's next A production version would add authenticated organizations, tenant isolation, durable role-based authorization, append-only audit events, delivery receipts, encrypted object storage, malware scanning, rate limiting, configurable retention, background processing, monitoring, backup recovery, and managed-key signatures. PantryProof supports recall operations; it does not certify regulatory compliance or independently declare food safe. Human operators retain final authority. An alert says a recall was sent. PantryProof proves the network responded. <div