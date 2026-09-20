---
slug: "sigmora-sigmora-org"
url: "https://devpost.com/software/sigmora-sigmora-org"
title: "SIGMORA(sigmora.org)"
hackathon: "Backblaze Generative Media Hackathon: Build with Genblaze on B2"
organization: "Backblaze"
winner: true
words: 1275
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SIGMORA(sigmora.org)

> Generative media at production scale, for a fraction of the cost. Genblaze orchestrates every model; Backblaze B2 stores and serves it at zero egress. Every asset ships with a verifiable receipt.

[Devpost](https://devpost.com/software/sigmora-sigmora-org) · hackathon [[Backblaze Generative Media Hackathon- Build with Genblaze on B2]]

## Facets

**mechanism** [[on_device_local]] [[provenance_signing]] [[structural_withholding]]
**domain** [[finance_payments]] [[housing_homeless]] [[supply_logistics]]
  <sub>weak: labor_employment</sub>
**user** [[general_public]] [[legal_professional]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** backblaze-b2, blender, cloudflare-d1, cloudflare-workers, docker, elevenlabs, fastapi, ffmpeg, firebase, genblaze, gmi-cloud, google-veo, hls, manim

## How they structured the write-up

- inspiration
- what it does
- ai providers and models used
- use of genblaze
- how we use b2
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next
- disclosure

## Body

Bytes go direct to B2; the B2 to Cloudflare hop is zero egress under the Bandwidth Alliance. Green edges cost no bandwidth. Inspiration The hard part of generative media at volume was never quality. It's two unglamorous things: cost , and not knowing what made your asset . We learned both the expensive way. Sigmora is a live product — real tenants, real invoices, real generative spend across roughly 50 distinct metered operations. Running it taught us that the model bill is only half the problem. The other half is egress : on a typical object store, serving the video you just generated costs more over its lifetime than generating it did. And when a customer asks "which model made this, from what prompt, and what did it cost me?" — most pipelines simply cannot answer. Backblaze B2 solves the first problem structurally. Genblaze solves the second. What it does Sigmora turns a brief into finished media through a multi-provider Genblaze pipeline, stores it on B2, and serves it through Cloudflare under the Bandwidth Alliance — so delivery costs $0 in egress . Every asset carries a receipt. Each run emits a canonical, SHA-256-bound manifest — provider, model, prompt, per-step cost, retries, lineage — embedded directly into the delivered file. Download anything Sigmora produced, drop it into our public verifier at https://www.sigmora.org/verify , and see exactly what made it. No account required. The file never leaves your browser: it is parsed locally and only the few-kB record is sent for the hash check, so a 4 GB master and a thumbnail cost the same to verify. The cost on that receipt is the cost we bill. Rates are exported from the same TypeScript cost model that charges customers, drift-guarded in CI, and registered onto forked Genblaze registries. estimated_cost() quotes the run before a provider is called. AI providers and models used Step Modality Provider Model Fallbacks 0 Image OpenAI gpt-image-2 gpt-image-1.5 1 Video GMI Cloud seedance-2-0-260128 seedance-1-0-pro-fast-251015 , wan2.6-r2v 1 Video Google veo-3.1-generate-preview veo-3.1-fast , veo-3.1-lite 2 Audio Speechify simba-3.2 simba-english 2 Audio ElevenLabs eleven_v3 eleven_multilingual_v2 Two steps carry a vendor switch rather than a single vendor, because both failed in production for reasons that were not bugs: narration on an exhausted character quota, video on a credential we did not hold. Use of Genblaze brief → video is one Pipeline across three modalities, running natively in our Python service (FastAPI, Python 3.12): Pipeline("brief-to-video", chain=False) .step(DalleProvider(models=priced_registry(DalleProvider)), model="gpt-image-2", modality=Modality.IMAGE) .step(video_provider_cls(models=priced_registry(video_provider_cls)), model="seedance-2-0-260128", modality=Modality.VIDEO, input_from=0) # animate the key frame, not text .step(narration_provider_cls(models=priced_registry(narration_provider_cls)), model="simba-3.2", modality=Modality.AUDIO) ModelRegistry.register_pricing() fed from our production cost model , so every manifest carries the price we actually charge. Registries are forked, never mutated — the default is process-wide, and mutating it would price every other consumer with our numbers. chain=False with explicit input_from . Chaining feeds every output forward, which is right for image→video and wrong for narration — that is generated from the script and must not take the video as input. Two providers written against BaseProvider / SyncProvider . SpeechifyTTSProvider and VeoVideoProvider wrap engines this service already ships rather than replacing them. VeoVideoProvider implements submit / poll / fetch_output natively, because that is Veo's shape — so it inherits the retry policy across all three phases, resumable runs and automatic costing. Manifest , verification_report() and the media handlers power the public verifier. How we use B2 Serve — Cloudflare in front of B2 under the Bandwidth Alliance: $0 egress . This is the lane today's verified run went out over. Store — direct-to-bucket presigned multipart. The app server mints a presigned URL and the browser PUTs straight to B2 in 5 parallel parts with per-part retry, so no generated byte transits our compute. Index — Cloudflare D1 + KV in front of the bucket, so we query an index and never LIST B2. Provenance — manifests are written under Object Lock ( GOVERNANCE rather than COMPLIANCE , deliberately: tamper-evident without making a deletion request impossible to honour). Being straight about status: that sink is implemented and tested, but the dedicated provenance bucket is not yet provisioned on our account — B2 only enables Object Lock at bucket creation, and we would not retrofit the live one. Today's verified run therefore carried its manifest inline in the delivered file . Challenges we ran into Genblaze is seven weeks old, and its launch example does not run. Integrating it proved four lines wrong against 0.4.4: GeminiChatProvider does not exist, step_type="classify" is not in StepType , and seedream-5.0-lite is not in GMICloudImageProvider 's registry. genblaze-google pins google-genai<2 , which silently downgrades any consumer on 2.x — our own Gemini voice path. So VeoVideoProvider wraps the google-genai 2.12.1 we already had rather than installing the adapter. The delivered file carried no receipt. ObjectStorageSink writes the manifest as a separate object — it never puts it inside the asset's bytes. A judge downloading our output would have been told there is no provenance record. Fixed by muxing picture over voice and then calling save(path, embed=True) , with the run reporting embedded / embed_method rather than assuming. And then the CDN nearly undid it. Our storage service transcodes video to HLS and its public route redirects a processed video to the playlist. Those segments are a re-encode — the manifest does not survive. The obvious link would have handed a judge a file with no record, one hop past the bug we had just fixed. Stale model pins are invisible. The pipeline was still on Kling-Image2Video-V2.1-Master and gpt-image-1.5 long after both were beaten. Nothing fails — a superseded slug still resolves and still returns a worse frame. We deleted them rather than demoting them to fallbacks, and added a CI test that fails if a retired id reappears. The Veo registry is pattern-keyed on ^veo- , so the next generation resolves without a code change. Accomplishments we're proud of A run that is checkable rather than asserted. gpt-image-2 → veo-3.1-generate-preview → simba-3.2 , all three steps succeeded, $0.675 quoted before the run and $0.675 charged , manifest embedded inline, published to B2 behind Cloudflare, downloaded from the public URL, extracted, and verified — hashOk: true , canonical hash 0cd3f935… , with per-step provider, model, prompt and cost. What we learned Provenance and cost accounting are the same data structure. We had built a billing ledger and Genblaze had built a provenance manifest, and they wanted the same fields. Once we fed our pricing into ModelRegistry , every manifest became an invoice line. The other lesson was about silence. Every serious bug here was invisible: a stale model that still resolves, a manifest written beside the file instead of inside it, a CDN that re-encodes the receipt away, a deploy that leaves a container healthy but unreachable, and two narration selectors on the same box picking different vendors with nothing saying so. None of them raised. We ended up adding the reporting — embed_method , videoKeyPresent , narrationDivergence — as much as the fixes. What's next Provenance-aware search: query the ledger in B2 for "every asset made with model X" and re-render on a newer model with lineage intact C2PA alignment for the embedded manifests Opening the verifier to any Genblaze-produced asset, not just ours Disclosure Sigmora is a pre-existing product; we did not build a platform in nine days. Built for this hackathon: the Genblaze pipeline service and its HTTP surface, the two BaseProvider implementations, the B2 provenance layer, and the public verifier. Reused: the cockpit, the provider integrations, the billing and margin model, and the B2 storage service. Everything reused predates the hackathon and is what made those days buy something real instead of a prototype. <div