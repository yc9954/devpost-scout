---
slug: "aloud-lxqr70"
url: "https://devpost.com/software/aloud-lxqr70"
title: "Aloud"
hackathon: "YouCam API Skin AI & Apparel VTO Hackathon "
organization: "Perfect Corp"
winner: true
words: 901
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Aloud

> Beauty, aloud. The first beauty AI a blind shopper can use alone, screen off. Built on the YouCam Skin Analysis API.

[Devpost](https://devpost.com/software/aloud-lxqr70) · hackathon [[YouCam API Skin AI - Apparel VTO Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[accessibility]] [[developer_tools]] [[legal_justice]] [[retail_commerce]] [[supply_logistics]]
**user** [[general_public]] [[legal_professional]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[regulation_legal_text]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** capacitor, deepgram, elevenlabs, eu-cosing, html5-qrcode, mediapipe, next.js, open-beauty-facts, openai-realtime-api, typescript, vercel, vercel-ai-sdk, webrtc, youcam-mcp-server

## How they structured the write-up

- the problem, in retail terms
- what it does (four flows, all operable with the screen off)
- how we used the youcam api (technological implementation)
- why it is safe (and why that matters for retail)
- impact
- try it

## Body

Scan: the back camera finds the barcode by sound, so a blind shopper never has to aim at a target they cannot see. Typing it also works. One product, four flows, all operable with the screen off. The footer names what grounds them: YouCam Skin Analysis and EU CosIng. Consent before the camera opens, in plain words: one photo, this session only, nothing saved, nothing about identity inferred. Talk: a live WebRTC voice session. Ask about any ingredient or allergen and the assistant calls real tools, then speaks a grounded answer. Verify: after makeup, the same guided capture compares against this session's bare-skin YouCam scores and speaks what changed. The spoken read of Nivea Creme: seven EU-flagged fragrance allergens named first, then what each marquee ingredient is listed to do. The problem, in retail terms Skincare commerce is built on pictures. Product images, ingredient panels, and shade swatches are frequently unavailable to a screen reader, so a blind shopper cannot independently learn what a product is, what is in it, or whether it suits them. This is not a niche annoyance. It is litigated: beauty retailers have been sued specifically over inaccessible e-commerce (Sephora 2017, Fenty Beauty 2019, Ulta 2019), 5,114 ADA digital-accessibility suits were filed in 2025 with retail the top-targeted industry, and the European Accessibility Act became enforceable in June 2025 with e-commerce in scope. 8.5 million Americans are blind or have serious difficulty seeing (2024 ACS), and iOS is 70.6 percent of screen-reader users, so this belongs in a mobile browser. Perfect Corp reports its beauty AI powers 800-plus brands, serves 300 million API calls a day, and lifts sales conversion 2.5x through try-before-you-buy. None of that value was reachable without sight. Perfect Corp's own site carries no accessibility statement, VPAT, or screen-reader documentation. Aloud closes that gap. What it does (four flows, all operable with the screen off) Talk: a live voice conversation over WebRTC. Ask about any ingredient, allergen, or barcode; the assistant calls real tools and speaks a grounded answer. Every reply is mirrored as text. Scan: beep-guided barcode finding, then a layered spoken read: product identity, EU-flagged fragrance-allergen status in what-the-label-lists language, marquee-ingredient functions, the full list on request. Know your skin: a selfie framed by sound alone (tonal guidance, a lighting gate, auto-capture on steadiness), then a spoken read grounded only in the YouCam Skin Analysis structured scores, with honest uncertainty. Verify your look: after makeup, the same capture compares against the session's bare-skin scores and speaks what changed. How we used the YouCam API (Technological Implementation) Aloud is built on the Perfect Corp YouCam AI Skin Analysis API, wired end-to-end, not wrapped. A server-side route registers the image ( POST /s2s/v2.0/file/skin-analysis ), uploads the bytes to the presigned URL, creates the task ( POST /s2s/v2.0/task/skin-analysis , seven cosmetic SD concerns at the 12-unit tier, format: json ), and the client polls the result through a thin proxy. The Bearer key never leaves the server. Response shapes and the stringified error tuples are pinned by fixtures captured from real API runs. Every spoken skin statement traces to a ui_score ; the face image is never sent to a general vision model to freely describe it. Around that core runs an agentic tool loop (Vercel AI SDK) whose tools reach the full EU CosIng inventory of 33,116 active ingredients, the EU fragrance-allergen list from Regulation 2023/1545, and Open Beauty Facts, plus a WebRTC voice layer over the OpenAI Realtime API. The same tools compose the products a shopper has scanned in a session into a plain, ordered morning-and-evening routine, flagging any listed allergens as it goes. Aloud also speaks Perfect Corp's own language: the skin analysis can be routed through Perfect Corp's native YouCam MCP server, the sponsor's 2026 agentic surface, and returns the same real scores. On a real iPhone the non-visual capture passed its kill experiment: 10 of 10 attempts accepted by the analysis, every one under 30 seconds. Why it is safe (and why that matters for retail) A blind user cannot catch a confident wrong answer, so honesty is engineered, not hoped for. A claim linter runs in CI and blocks any medical or treatment language from ever being spoken; the app uses cosmetic and appearance language only, states uncertainty in plain words, communicates input quality without blaming the user, and stores nothing. That discipline is exactly what a beauty retailer needs to deploy skin AI without regulatory exposure. It goes one step further, and this is the part we are proudest of. Published dermatology documents that readings like redness are measured less reliably on deeper skin tones and in low light. So Aloud runs Perfect Corp's Skin Tone Analysis, converts the returned skin color to a neutral color metric (ITA, not identity, never race), reads the API's own lighting quality, and on exactly those inputs it lowers its confidence and says so, out loud. It is, as far as we can find, the first consumer skin tool that discloses its own accuracy bias to the person it affects most, at the moment it affects them. Impact A documented, underserved population; a documented, litigated retail barrier; and a solution that turns a compliance liability into a new customer segment. For the shopper, it is independence: completing the decision alone. Try it Live web app (primary judge URL): https://aloudbeauty.vercel.app iOS native shell on TestFlight: https://testflight.apple.com/join/AKWHYekX Android APK: https://github.com/StephenSook/aloud/releases/latest Code: https://github.com/StephenSook/aloud <div