---
slug: "keepme"
url: "https://devpost.com/software/keepme"
title: "KeepMe"
hackathon: "YouCam API Skin AI & Apparel VTO Hackathon "
organization: "Perfect Corp"
winner: true
words: 914
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/government_staff"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# KeepMe

> KeepMe makes AI virtual try-on trustworthy. Shoppers control what can change, detect unwanted changes to their appearance, repair visual drift, and receive proof before approving the result.

[Devpost](https://devpost.com/software/keepme) · hackathon [[YouCam API Skin AI - Apparel VTO Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[security_privacy]]
**user** [[government_staff]] [[legal_professional]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[video_visual]]

**stack** ai-clothes-v3, axe-core, clamav, clerk, fastapi, jose, mediapipe, next.js, node.js, opencv, opentelemetry, playwright, postgresql, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for keepme

## Body

KeepMe adds consent and visual-integrity checks to AI apparel try-on. Live mode pairs a shopper photo with a selected or uploaded garment for YouCam AI Clothes v3. The shopper defines what AI may change and protects glasses, face, hair, skin, body, and custom zones. KeepMe catches the disclosed glasses-removal drift before the shopper can approve the result. Supported drift is restored from the source image and independently reverified. A signed receipt records the contract, evidence, generator, repair status, and retention choice. The shopper can immediately delete every image, mask, heatmap, and repair artifact from the session. Inspiration Virtual try-on should answer one simple question: “How does this garment look on me?” But a generative model can also change a shopper’s glasses, face, hair, skin appearance, body outline, or background. Those changes may be subtle, deeply personal, and difficult to notice before an image is accepted. We built KeepMe around a different premise: consent should be specific enough for software to enforce. A shopper should be able to say what AI may change, protect everything else, and see evidence before approving a result. What it does KeepMe adds a consent and visual-integrity layer around apparel virtual try-on. The shopper selects a photo and garment, or opens the disclosed guided scenario. They create an Identity Contract : the garment area may change, while glasses, face, hair, skin, body shape, background, and optional hand-drawn zones can be protected. In live mode, KeepMe sends the approved inputs to YouCam AI Clothes v3 and follows the asynchronous generation task to completion. KeepMe measures the source and result with garment-aware pixel, geometry, face-landmark, silhouette, protected-zone, and skin-consistency signals. The result is classified as passed, needs review, failed, inconclusive, or passed after repair. A hard finding cannot be hidden behind an average score. Supported drift can be restored from the source and independently reverified. The shopper can approve a signed integrity receipt or delete all session images immediately. The guided demo intentionally removes the shopper’s glasses so judges can repeat the full detect → restore → reverify flow without presenting the fixture as a fresh YouCam failure. Live mode runs the same contract and verification workflow on a real YouCam-generated result. How we built it The product UI and orchestration layer use Next.js 16, React 19, and TypeScript . Live apparel generation is integrated server-to-server with the YouCam AI Clothes v3 API through its file-upload and asynchronous task endpoints. Eligible sessions can also use the YouCam Skin Analysis API v2.1 as an additional skin-appearance consistency signal; KeepMe does not expose diagnostic labels or use the signal for medical conclusions. A private FastAPI integrity service uses OpenCV and MediaPipe for alignment, face landmarks, silhouette measurements, protected-region comparisons, and repair. Uploads are decoded, normalized, stripped of metadata, and scanned with ClamAV before provider use. Session state lives in PostgreSQL , images use private Vercel Blob storage, and production services communicate through private Vercel Services bindings. Clerk protects retailer views. Integrity receipts are signed with JOSE/JWS and bind the approved contract and result evidence with cryptographic digests. We instrumented the system with OpenTelemetry and tested it with Vitest, Playwright, and axe-core . Challenges we ran into The hardest problem was separating intended garment change from unwanted identity drift. A jacket should cover part of the torso, but it should not silently move a face boundary or erase glasses. We addressed this with explicit allowed regions, component-level evidence, conservative hard rules, and an inconclusive state when evidence is insufficient. We also had to make an asynchronous external API feel safe and understandable. That meant private result proxying, bounded polling, credit-aware retries, structured error responses, and clear progress states. Production safety created another challenge: image processing must fail closed when malware scanning, private storage, signing, authentication, or the integrity service is unavailable. We fixed scanner cold-start behavior without weakening that boundary. Finally, we wanted a compelling demo without making an unfair claim about the generator. The guided glasses-removal scenario is therefore prominently labeled as a controlled synthetic fixture, while live mode is explicitly labeled as a YouCam result. Accomplishments that we're proud of A real end-to-end YouCam flow from approved inputs to generated apparel preview. A shopper-readable Identity Contract instead of a vague consent checkbox. Multi-signal verification with explainable findings and conservative decision states. Source-zone repair followed by a fresh verification pass. Signed, downloadable receipts tied to contract and result digests. Immediate, verified deletion of source, garment, result, mask, heatmap, and repair artifacts. Privacy-filtered retailer insights that exclude shopper photos and suppress small cohorts. Automated unit, integration, browser, accessibility, and live production smoke tests. What we learned Generative UX needs an explicit scope. “Create a try-on” is not enough; the system also needs a machine-readable definition of what must remain unchanged. We learned to separate measurement confidence from the final decision. Missing evidence should produce “inconclusive,” not a reassuring score. We also learned that privacy is a lifecycle property: private upload, server-only provider access, safe observability, retention limits, and verified deletion all matter. Most importantly, trust comes from showing limitations. A controlled failure is useful when it is disclosed, repeatable, and connected to the same workflow used in production. What's next for KeepMe Next we want to calibrate thresholds on a larger, consented evaluation set; expand repair to handle more occlusion boundaries; add provider webhooks where available; and pilot the workflow with retailers. We also plan to publish a public-key receipt format, add independent integrity evaluations, and continue usability and accessibility testing with real shoppers. <div