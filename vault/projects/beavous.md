---
slug: "beavous"
url: "https://devpost.com/software/beavous"
title: "Beavous"
hackathon: "Backblaze Generative Media Hackathon: Build with Genblaze on B2"
organization: "Backblaze"
winner: true
words: 1007
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Beavous

> Turn one approved product into a complete, product-true campaign—four concepts, 16 ratios, claim-safe copy, a reel, and verifiable Genblaze/B2 lineage.

[Devpost](https://devpost.com/software/beavous) · hackathon [[Backblaze Generative Media Hackathon- Build with Genblaze on B2]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[labor_employment]] [[retail_commerce]] [[supply_logistics]]
**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** backblaze-b2, fastapi, ffmpeg, genblaze, github, google-artifact-registry, google-cloud-build, google-cloud-run, google-cloud-tasks, google-gemini-api, google-gen-ai-sdk, google-secret-manager, next.js, pgtap

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for beavous

## Body

Inspiration Most generative media tools optimize for volume. Ecommerce teams, however, pay for mistakes: a changed cap, incorrect material, missing component, altered label, or unsupported claim can make an entire campaign unusable. We built Beavous around a different idea: product truth should be an approved, versioned input—not a hopeful sentence buried inside a prompt. The name comes from the beaver: a deliberate builder that turns raw material into something structured and durable. Beavous does the same for product references, turning them into complete campaigns with traceable evidence. What it does Beavous is a product-truth-first creative workshop for ecommerce campaigns. A user can import an owned product URL or upload one to four reference images. Beavous extracts a structured Product Truth Lock covering identity, colors, materials, visible components, packaging text, dimensions, approved claims, forbidden claims, and details that must not change. The user reviews, corrects, versions, and approves that truth before generation can begin. They can also create a Brand Kit and approve a campaign plan. From one approved product, Beavous produces: four purposeful concepts: studio hero, lifestyle, detail/benefit, and bold social; four delivery ratios for each concept: 1:1, 4:5, 9:16, and 16:9; clean and optional text-overlay variants; claim-safe captions, headlines, CTAs, and alt text; a portrait product reel; QA results for product fidelity, brand fit, and unsupported claims; a downloadable campaign package with provenance and integrity evidence. Every output shows its status, approval state, model, provider, QA result, download controls, and lineage. Failed work remains visible and is never presented as approved. How we built it The public site and responsive application use Next.js 16, React 19, and TypeScript , deployed on Vercel at beavous.com . Supabase provides email/password authentication, PostgreSQL, row-level security, organization isolation, and private Realtime Broadcast updates. The browser never receives service credentials, and organization membership is revalidated by the backend. A public FastAPI service runs on Google Cloud Run . Expensive or long-running operations are divided into durable, idempotent units and dispatched through Google Cloud Tasks to a separate OIDC-protected worker. Genblaze is the execution and provenance boundary for every generative and deterministic media operation. We built project-local providers for Gemini image generation, Gemini Omni image-to-video, Veo image-to-video, and deterministic media transforms using Google's current google-genai SDK. Backblaze B2 is the authoritative media store. It contains product sources, normalized references, intermediate work, retained failures, corrected outputs, final media, evaluations, private prompt sidecars, thumbnails, manifests, verification records, videos, and campaign ZIPs. For every final asset, Beavous: verifies the canonical Genblaze manifest; fetches the stored bytes back from private B2; recalculates SHA-256 and byte size; compares them with the manifest and database record; records the result as integrity-verified. Signed delivery URLs are short-lived and are never persisted in the database or logs. Challenges we ran into Making long-running media generation durable Video submission, polling, and download cannot safely live inside one web request. Cloud Tasks may also redeliver work. We split provider operations into resumable stages, persisted external operation identities, generated deterministic task names, and made every expensive transition idempotent. Refreshing or closing the browser does not cancel a campaign. Completed work is recovered without regenerating already successful paid assets. Integrating current Gemini capabilities through Genblaze The available Genblaze Google connector did not support all of the current multimodal image and video routing we needed. Instead of bypassing Genblaze, we implemented small project-local provider adapters that satisfy its contracts while using the current Google SDK. This allowed real Gemini image and Omni video operations to retain Genblaze run IDs, manifests, B2 storage, and parent lineage. Treating product fidelity honestly Product fidelity evaluation is probabilistic. We did not present model scores as certainty. Human approval remains authoritative, failed QA stays visible, retries are bounded, and integrity verification is described as integrity—not proof of authorship. Securing imports and private media Owned-page import required SSRF protection, redirect revalidation, public-IP enforcement, DNS and peer-IP checks, response limits, and HTML sanitization. Uploads required magic-byte validation, MIME checks, hashing, deduplication, and safe SVG handling. Private B2 media also required tenant-authorized, short-lived delivery without leaking signed URLs. Accomplishments that we're proud of We completed a real paid production campaign for our owned fictional Field Bottle product: 43 of 43 durable pipeline steps completed; four real Gemini Flash Image master concepts; sixteen final delivery ratios; sixteen deterministic text variants; Gemini planning, approved-claim copy, and multimodal QA; one real 10.005-second Gemini Omni portrait reel with audio; 38 Genblaze manifests passing canonical verification; 38 corresponding B2 media objects passing independent fetched-byte verification; one fetched-byte-verified 40-file campaign ZIP; $1.8551 total recorded generation cost, with the budget reservation reconciled to zero. The campaign also retains a failed ratio attempt and its passing successor instead of hiding the failure. Separate, clearly labelled recovery evidence demonstrates a genuine Genblaze from_result parent link without pretending the paid masters required correction. Beyond the media proof, Beavous includes real authentication, tenant isolation, row-level security, durable jobs, bounded retries, cancellation, recovery, cost limits, responsive mobile workflows, accessibility checks, security scans, and production deployment. What we learned The strongest provenance system is both durable and modest about what it proves. A canonical manifest plus a second hash of bytes fetched from B2 demonstrates that the stored asset matches its recorded lineage. It does not prove authorship, so Beavous deliberately says integrity verified . We also learned that reliable generative media is an orchestration problem as much as a model problem. Idempotency, retries, recovery, cost controls, failure visibility, storage identity, and human approval are what turn an impressive generation into a usable product workflow. Finally, product truth works best as structured, approved data shared by planning, generation, evaluation, copy, and export—not as repeated prompt text. What's next for Beavous After judging, we would add: collaborative review roles and approval workflows; richer brand-rule and packaging-text evaluation; more provider adapters and model-routing options; comparison and approval tools for campaign teams; physical iPhone and Android device validation; a public Backblaze showcase bucket once the account satisfies Backblaze's payment-history requirement. The long-term goal is to make Beavous a trustworthy creative production layer: more campaign range, less product drift. <div