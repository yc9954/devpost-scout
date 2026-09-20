---
slug: "cinemory"
url: "https://devpost.com/software/cinemory"
title: "Cinemory"
hackathon: "Backblaze Generative Media Hackathon: Build with Genblaze on B2"
organization: "Backblaze"
winner: true
words: 1234
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Cinemory

> Turn a set of photos into a scored, cinematic video reel. Generated with Genblaze, stored on Backblaze B2, sealed with verifiable SHA-256 provenance.

[Devpost](https://devpost.com/software/cinemory) · hackathon [[Backblaze Generative Media Hackathon- Build with Genblaze on B2]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]] [[supply_logistics]]
**user** [[general_public]]
**substrate** [[code_repository]] [[video_visual]]

**stack** backblaze-b2, fastapi, ffmpeg, firebase, genblaze, gmi-cloud, google-cloud-run, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- how it uses backblaze b2 (storage and data orchestration)
- how it uses genblaze
- ai providers and models used
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cinemory

## Body

How it works: photos in, image-to-video clips, chapter bridges, music-driven cuts, a stitched reel, every artifact sealed on B2. Live on Cloud Run and its Firebase mirror. GET /health reports the exact commit the running image was built from. Every artifact lands on Backblaze B2 under a content-addressed key, catalogued in an append-only index you can query. The sealed manifest: provider, model, prompt and a SHA-256 for every asset. Recompute it in your own browser. One core, three ports. Live Genblaze and B2 adapters swap for offline fakes, so the pipeline runs in CI with no credentials. Inspiration Cinemory began as a personal anniversary gift: photos from years together, turned into a scored short film. Making it by hand took days. The interesting part came after. Generative media is easy to make and hard to trust. When a reel is assembled by several AI models, whoever receives it should be able to ask what made this, from which inputs, and whether it was tampered with. Consumers care. Brand and comms teams care even more. So we generalised the gift into a production-shaped app where provenance is a first-class output, not an afterthought. Genblaze and Backblaze B2 make that cheap to do right. What it does Cinemory turns a set of photos, organised into chapters, into one short cinematic film: Photo to clip. Each photo is animated into a short video via an image-to-video model (a Genblaze pipeline step). Chapter bridges. First/last-frame transitions connect scenes smoothly. Music-driven cuts. Scene changes are planned onto musical beats. Stitch. Clips assemble into one reel, with an ffmpeg cinematic colour grade. Store on B2. Every input, clip, bridge, the final reel and the run manifest land on Backblaze B2 under content-addressed keys. Provenance. A SHA-256-sealed manifest records provider, model, prompt, params, timestamps and every asset hash, and cites each generated clip back to its source photo's SHA-256, so every output traces to the exact input it came from. It is persisted to B2, embedded into the reel container, and re-verifiable in your own browser at any time. The public repo and demo run on model-generated photos only, so no real person appears anywhere. The original personal content stays private. How we built it Ports and adapters, offline-first. The orchestrator depends on three protocols: MediaProvider, StorageBackend, Stitcher. The live adapters wrap a real Genblaze Pipeline (with Genblaze's ObjectStorageSink writing to B2) and a boto3 B2 client. The offline fakes implement the same protocols deterministically, so the same pipeline code, including the real SHA-256 provenance, runs in CI with zero credentials. A FastAPI app exposes it; a React + TypeScript frontend ships in the same container on Cloud Run, mirrored on Firebase Hosting. In live mode each backend is used only when its credentials are present; otherwise the API degrades transparently to the offline path and says so on screen, so the core action never 500s. Generation runs concurrently. Measured in production, a three-photo reel finished in 352 seconds of wall clock containing 871 seconds of provider work. Every push to main deploys itself once CI is green, authenticated with keyless Workload Identity Federation so no service-account key is stored in this public repo, and the deploy fails unless the live /health reports the very commit it just built. How it uses Backblaze B2 (storage and data orchestration) Every artifact is persisted to B2: input photos, each generated clip, chapter bridges, the final reel, the provenance-embedded reel, and manifest.json. Content-addressed layout (reel/kind/shard/sha256/name): identical bytes deduplicate by hash. A queryable JSONL run index catalogues every object with size and content type, the analogue of Genblaze's Parquet index sink: a catalogue across your whole media library. Two real write paths: Genblaze's own ObjectStorageSink persists every generated asset and its sealed manifest to B2, and Cinemory's boto3 adapter persists the composed reel and reel-level manifest. Per-job usage accounting reports what a run actually consumed: provider calls by model, provider seconds, objects written and bytes written. How it uses Genblaze Generation is a real Genblaze Pipeline step behind the MediaProvider port. Genblaze owns per-asset storage and provenance: the adapter attaches ObjectStorageSink, so Genblaze content-addresses each output, persists it to B2, and seals a SHA-256 manifest for the run. Cinemory reads the durable bytes back, verifies them against Genblaze's sealed SHA-256, and folds that hash into its own reel-level manifest. Genblaze owns per-asset provenance; Cinemory owns composed-reel provenance. Every Genblaze call is contract-tested in CI against the actual published SDK, so API drift fails the build instead of the demo. AI providers and models used Role Model Provider (via Genblaze) Photo to video (I2V) Kling-Image2Video-V2.1-Master GMI Cloud Chapter bridge (FLF2V) seedance-2-0-260128 GMI Cloud Still generation (optional) seedream-5.0-lite GMI Cloud Live generation runs through GMI Cloud today. Other Genblaze providers are scaffolded behind the same port and on the roadmap. Challenges we ran into The first fully live run taught us the exact lesson we designed for. Our CI contract-tests the Genblaze adapter against the real published SDK, but the SDK's mock provider performs no server-side validation. The very first live generation revealed that the adapter never forwarded the photo bytes into the pipeline step, so the GMI API rejected every submit with "image: required parameter is missing". The offline path, the storage path and the provenance path had been genuinely exercised for weeks; the one seam only reachable with live credentials hid the bug. We fixed the adapter to attach the inputs as external assets, added regression tests that assert the inputs actually reach the SDK, and hardened the API so a provider failure degrades that single request honestly instead of erroring. The second was the cost of truth in wall clock. Image-to-video takes minutes per photo, and the calls ran one after another, so a five-photo reel needed about 26 minutes and the browser gave up first. The fix was not a longer timeout. The calls were always independent, so they now run concurrently and a five-photo reel finishes while you watch it. Accomplishments that we're proud of Provenance as a product feature: every reel ships with a sealed, re-verifiable SHA-256 manifest, embedded in the video container itself, and you can recompute it in your own browser. 300+ backend tests plus frontend tests, real-browser end-to-end specs, a pen-test suite, CodeQL, gitleaks and pip-audit in CI, all runnable with zero credentials. A machine-checkable readiness gate that scores the repo against this hackathon's judging criteria with real-evidence checks. An honest live/offline degrade model, proven in production on Cloud Run with real B2 writes: when a live provider fails, the app says which kind of failure it was instead of looking slow. What we learned Mocks validate shapes, not truth: only a live call proves a required payload slot is filled. Content-addressing makes storage self-deduplicating and provenance natural. And a generative model cannot be trusted with anything that has to be correct, so anything that must be right is computed by us and the model is trusted with visual style. What's next for Cinemory The B2B wedge. Conferences, award ceremonies and sales kick-offs produce piles of photos that a comms team must turn into a branded highlight reel fast, with clear rights and provenance. Occasion themes, LinkedIn-ready share targets and per-brand style presets are next, plus more Genblaze providers behind the same port. Longer term, expressing the manifest as a signed C2PA Content Credential, so provenance is interoperable with the wider ecosystem rather than a bespoke format. <div