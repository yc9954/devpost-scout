---
slug: "casting"
url: "https://devpost.com/software/casting"
title: "CASTING"
hackathon: "YouCam API Skin AI & Apparel VTO Hackathon "
organization: "Perfect Corp"
winner: true
words: 929
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# CASTING

> Show your customers someone who looks like them. One product photo, eight measured skin tones, one coverage score: CASTING tells a brand who its catalogue never shows. Built on four YouCam APIs.

[Devpost](https://devpost.com/software/casting) · hackathon [[YouCam API Skin AI - Apparel VTO Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]]
**domain** [[finance_payments]] [[health_clinical]] [[scientific_research]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** ai-clothes-virtual-try-on, ai-facial-color-tones-analyzer, ai-fitzpatrick-skin-type-analysis, ai-skin-analysis, cielab-color-math, next.js, node.js, react, typescript, vercel, youcam-api

## How they structured the write-up

- inspiration
- what it does
- how we built it — four youcam apis, all load-bearing
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for casting
- honesty — what is measured, what is curated

## Body

The coverage board: one product on eight people, measured — Fitzpatrick I, III, IV and VI. Red markers: low contrast at Fitzpatrick VI. What the product page shows today vs. what CASTING shows. MERIDIAN GOODS is fictional; its campaign images are AI-generated and labeled. The one-page coverage report: measured bands, ΔL* and ΔE2000 per person, and a plain-text diagnosis. Inspiration A brand photographs its product on two models. Its customers are everyone else. And nobody in the company can answer a simple question: who does our catalogue never show? Almost every tool built on try-on technology asks "does this suit me ?" — a consumer question. We inverted it: CASTING's user is the brand , and it measures a cohort instead of a face. It is a tool for the person who runs the catalogue — a merchandiser, not a consumer. What it does CASTING takes one product photo, runs Perfect Corp's Apparel Virtual Try-On across a reference panel of eight measured skin types, and returns a coverage board — the same garment on eight people — plus a measured answer no catalogue has today. One upload, under thirty seconds: The product image is tried on all eight panel members in parallel — a real API fan-out with visible per-person progress. The coverage board shows the same garment on eight measured skin tones, Fitzpatrick band labeled per tile. A coverage score reports which Fitzpatrick bands this catalogue serves, and on which measured skin tones the product's colorway loses contrast (ΔL* primary, ΔE2000 secondary — deterministic color math over measured values, no model). Export: a PDP-ready image set (ZIP) and a one-page coverage report. A merchandiser runs this before the product goes live — not after the return arrives. And a store manager can ask a local question: does this colorway serve my customers, not the brand's average. How we built it — four YouCam APIs, all load-bearing AI Clothes Virtual Try-On (Fashion): the core fan-out — puts the uploaded garment on each of the 8 panel members, 8 parallel calls per run. AI Skin Analysis (Skin): one-time measurement of each panel member's skin profile when the panel was built. AI Fitzpatrick Skin Type Analysis (Skin): one-time measured Fitzpatrick band per member — the bands on the board are measured, not assigned. AI Facial Color Tones Analyzer (Skin): one-time measured skin tone values per member — the basis for the ΔL*/ΔE2000 contrast diagnosis. The three Skin API measurements were run once and frozen as JSON in the repo, so a live run spends exactly 8 Virtual Try-On calls and nothing else. The stack: Next.js (App Router) + TypeScript on Vercel; all YouCam calls go through server routes, so the API key never reaches the client. The fan-out endpoint streams results as NDJSON — one failed panel member never aborts the run; the UI reports "7 of 8 measured" instead of silently claiming success. A credit circuit-breaker checks the real account balance via the YouCam credit API before every live run and visibly falls back to the labeled, precomputed demo run when the budget cap is reached. No database, no accounts, no LLM anywhere in the product. Challenges we ran into Latency × 8: a single try-on takes 16.5–28.0s (measured). Running the panel in parallel brings a full run to ~28s — and the board's staggered tile reveal follows those real measured latencies, so the loading state is honest dramaturgy, not decoration. The panel refused to be tidy: our generated candidates for Fitzpatrick II and V measured as neighboring bands. So the panel is eight people, measured — Fitzpatrick I, III, IV and VI. The app reports II and V as "not measurable with this panel" and never counts them as covered. A capped unit budget: one live run costs 16 API units. The circuit-breaker plus a clearly labeled precomputed seed run keep the app alive for cold visitors without burning the judging reserve. Accomplishments that we're proud of A real 8-person parallel try-on fan-out, live on production, with honest partial-failure states. Measurement language throughout: every claim about a skin tone is an API measurement with visible provenance, down to the hex values labeled on the tiles. Honesty as a feature: the product states its own limits — sample size, panel gaps, curated content — before anyone asks. The Methods panel ("How we measure") documents endpoints, sample size, image provenance, and thresholds. What we learned "The backend works" and "the product is demoable" are two different claims — our adversarial review caught exactly that gap. And: file names are intentions, measurements are results. We had named panel candidates by their target Fitzpatrick band; once the measurements disagreed, the names had to go. What's next for CASTING A second colorway in the same run for direct contrast comparison; permalinks to finished runs; and the same coverage measurement across other VTO categories (shoes, bags, accessories). Deliberately out of scope: sizing and fit — CASTING stays on the skin-tone axis, where its measurements live. Honesty — what is measured, what is curated The panel is a curated reference panel of AI-generated people , not real customers — chosen deliberately (no personality-rights issues, reproducible) and disclosed in the app. Measured coverage is Fitzpatrick I, III, IV and VI. Eight people are a sample, not a population; the product says so itself. "MERIDIAN GOODS" in the comparison view is a fictional brand; its campaign images are AI-generated and labeled as such directly in the UI. Every tile presented as a result is a genuine YouCam try-on result — precomputed runs are always labeled as precomputed. <div