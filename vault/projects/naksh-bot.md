---
slug: "naksh-bot"
url: "https://devpost.com/software/naksh-bot"
title: "NakshaBot"
hackathon: "ML Empowerment Build Challenge 2.0"
organization: "ML Empowerment Foundation"
winner: true
words: 1316
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# NakshaBot

> Turns hours of hand-drawn Census field maps into accurate, ready-to-use HLB layouts in minutes built solo by a Class 12 student, already used by 5000+ enumerators.

[Devpost](https://devpost.com/software/naksh-bot) · hackathon [[ML Empowerment Build Challenge 2.0]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]
**domain** [[civic_government]] [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** cashfree, dbscan, deno, docker, fastapi, google-earth-engine, leaflet.js, opencv, openstreetmap, overpass-api, postgresql, pymupdf, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nakshabot

## Body

Layout Created By NakshaBot Satellite HLB Boundary SEO Performance Reviews And Feedbacks Inspiration I'm Kratagya Singh, a Class 12 student in India. While looking into how India's Census 2027 field enumerators actually work, I kept seeing the same problem: enumerators roaming their assigned area for hours, hand-sketching the layout of their HLB (House Listing Block) every road, every building, every landmark — on paper, from scratch, before they could even begin the actual survey. It's slow, error-prone, and entirely dependent on the enumerator's own sense of direction and memory. I decided to build something that could hand them an accurate base map instead of a blank page, and that could run at close to zero operating cost, since this needed to be usable at the scale India's census actually operates at — not a paid enterprise tool. What it does NakshaBot gives a field enumerator an accurate, ready-to-annotate map of their HLB in minutes instead of hours. There are four modes, and I'll be upfront about where each one stands: Canvas mode — freeform manual map building: draw roads, place buildings and landmarks, and lay out the block by hand with full control. This is one of the two most polished modes. Desk mode — the standard workspace: upload an existing Census GeoPDF (the app extracts the exact HLB boundary straight from it, no manual retracing) or point it at a location, and it pulls real road and building data automatically. Also one of the two most polished modes. Sat-Extractor (Satellite Mode) — the newest and most powerful mode: generates the map directly from satellite imagery. it's already the most capable mode and the one I'm iterating on most. Live Survey Mode — walk the area with GPS on and the app builds the map from your live movement. I'll be honest: this is currently the weakest mode. Real-world GPS noise and rural connectivity make it a genuinely harder problem than the other three, and it's the one I'm actively working to bring up to the same standard. For dense urban blocks, roads and buildings render directly. For rural blocks where OpenStreetMap data is often sparse or the settlement pattern is scattered hamlets rather than a grid NakshaBot runs a clustering step over building centroids to auto-detect and label hamlet groups, which is normally the hardest part to draw by hand .(I wasn't able to use Google Maps API as it was paid and that was unaffordable , but still this works well at 0 cost) The finished map can be edited (rename, move, delete points; draw roads by hand), then exported to PDF or Excel for the official submission — and it works offline-first, since a lot of field survey happens with unreliable connectivity. (HLB MAPS FOR TESTING :- https://drive.google.com/drive/folders/1UyFMVvKTUxwFsZI7br-nX-dEruab3FqJ?usp=sharing ) How we built it Frontend: React + TypeScript + Vite, Tailwind CSS, Leaflet for the interactive map layer, Turf.js for geospatial math, simplify-js to clean up raw GPS tracks, IndexedDB ( idb ) for offline-first storage in the field. Boundary extraction service: a Python microservice (FastAPI, Dockerized, deployed on Render) using PyMuPDF and OpenCV to parse the geo-referenced Census PDF directly and pull out the HLB boundary and printed labels, with Tesseract OCR and Shapely as supporting tools. Map enrichment: the Overpass API against OpenStreetMap for real road and building geometry, and Google Earth Engine for building footprints and land-cover context in areas where OSM coverage is thin. Rural mode: DBSCAN clustering over building centroids to detect and group scattered hamlets automatically instead of leaving them as an unreadable scatter of dots. Live Survey Mode: Kalman-filtered GPS smoothing so the walked path doesn't jump around from raw GPS noise, plus automatic serpentine numbering of buildings as the enumerator moves through the block. Backend: Supabase — Postgres with row-level security scoped per user, Auth, and Deno edge functions for the geodata fetch calls and payment handling (Cashfree, currently sandboxed). Export: jsPDF and SheetJS ( xlsx ) to produce the final submission-ready map. The whole stack was chosen to keep marginal cost near zero at scale OpenStreetMap and Earth Engine data are free, Supabase's free tier covers the current usage. Challenges we ran into Getting an accurate boundary out of a real government GeoPDF is messy — text layers, scan artifacts, and inconsistent label placement meant the extraction pipeline went through several rewrites (I recently replaced a slower OCR-first approach with direct PDF text-layer extraction once I realized the census maps are always centered on the target HLB, which let me eliminate OCR from the common path entirely and cut processing time significantly). Rural India's settlement patterns don't fit a grid, and OSM coverage varies wildly by district — the DBSCAN hamlet-clustering approach took real trial and error to get right. Live GPS in the field is noisy, especially in areas with tree cover or dense construction, so the Kalman filtering step needed real tuning rather than defaults — and honestly, Live Survey Mode is still the roughest edge of the app because of this; Canvas mode, Desk mode, and Sat-Extractor are all further ahead. Sat-Extractor, the newest mode, was built in just 4 days to get it in front of enumerators quickly which meant shipping it before every feature was fully polished, and then iterating on what mattered most based on how people actually used it. Doing all of this solo, on a 0 budget, while preparing for JEE Main and Advanced at the same time — the near-zero-cost constraint wasn't optional, it was the only way this could actually reach the people who needed it. Accomplishments that we're proud of The thing I'm most proud of is that this isn't a demo — people are actually using it: 13000+ registered users and 17k+projects (HLB maps) created on the platform. 120+ pieces of direct feedback from real enumerators, which has directly shaped features like the offline export and rural clustering mode. 9 live survey sessions actively in progress, and early signs of return usage — enumerators coming back on a different day to update or continue a map rather than starting over. Early, small-scale validation that people are willing to pay for it (a handful of paid projects so far), while the core mapping tool stays free. Ranked #1 on Google organically for target search terms like "HLB map," with zero ad spend and zero prior SEO experience — I learned SEO from scratch specifically to get this in front of enumerators. Google Search Console shows last 45 days alone brought 15K clicks (+538%) and 100K impressions (+321%). NakshaBot is now surfaced directly inside Google's AI Mode as a recommended tool for generating HLB layout maps — which means people are finding and using it without me spending anything on marketing. What we learned Building for real users surfaced problems no textbook or tutorial would have — messy real-world government PDFs, patchy rural connectivity, GPS noise, and enumerators who are focused on finishing their block, not learning a new app. Shipping something people actually rely on, then fixing it based on their feedback, taught me far more about product engineering than any solo side project would have. I also had to learn SEO completely from zero, since there was no budget for ads. Getting NakshaBot to rank organically for the searches enumerators actually type turned out to matter as much as the engineering — it's the main reason the user numbers above exist at all. What's next for NakshaBot Bringing Live Survey Mode up to the same standard as Canvas, Desk mode, and Sat-Extractor is the top priority — better GPS smoothing and offline resilience for genuinely poor-connectivity areas. Beyond that: expanding district coverage ahead of Census 2027, continuing to iterate on Sat-Extractor now that the core is in place, and exploring a formal pilot with local census administration so the tool can move from grassroots adoption to an officially supported option for enumerators. <div