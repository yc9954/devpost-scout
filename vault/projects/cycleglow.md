---
slug: "cycleglow"
url: "https://devpost.com/software/cycleglow"
title: "cycleglow"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 445
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# cycleglow

> AI Period & Skin Intelligence - cycle-synced skincare, nutrition, and hormone tracking

[Devpost](https://devpost.com/software/cycleglow) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[agriculture_food]] [[health_clinical]] [[retail_commerce]] [[transportation]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css, dockerfile, html, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for cycleglow

## Body

Inspiration Every month, millions of women deal with hormonal skin changes — breakouts during their luteal phase, dryness during menstruation, and sensitivity fluctuations throughout their cycle. Yet no app connects period tracking with skincare product intelligence . Women are left guessing which products to use and when. CycleGlow bridges this gap by combining cycle-aware AI with skincare product scanning. What it does CycleGlow is an AI-powered period tracker that connects your menstrual cycle phases to personalized skincare and nutrition recommendations. Product Scanner: Scan skincare product barcodes or take photos — AI identifies ingredients and rates them for your current cycle phase (green/yellow/red traffic light system) Cycle-Phase Skincare: Get ingredient recommendations based on hormonal changes (e.g., niacinamide + salicylic acid during luteal phase when progesterone causes breakouts) Hormone Dashboard: Beautiful interactive charts showing estrogen, progesterone, LH, and FSH curves throughout your cycle, with your logged symptoms overlaid Nutrition per Phase: Science-backed food recommendations for each phase — iron-rich foods during menstruation, fermented foods during follicular, antioxidants during ovulation, magnesium during luteal Mood + Skin Logger: Track daily mood, skin condition, and energy levels. AI finds patterns over multiple cycles. Privacy-First: All data stored locally. No account required. How we built it Backend: Python FastAPI with dedicated modules for cycle phase calculations, hormone modeling, skincare recommendation engine, and product scanning Frontend: Vanilla HTML/JS with Chart.js for hormone visualization, camera API for barcode/product scanning AI: Google Gemini vision API for product label analysis and ingredient identification Data: Open Beauty Facts API for cosmetics ingredient database, curated ingredient-phase compatibility matrix based on dermatological research Design: Soft feminine aesthetic (lavender, rose gold palette) — approachable, not clinical Challenges we ran into Building a scientifically accurate ingredient-phase compatibility matrix required extensive dermatological research Balancing product scanning accuracy between barcode lookup and AI vision analysis Creating smooth hormone curve visualizations that are both accurate and beautiful Accomplishments we're proud of Nobody else combines period tracking with skincare product scanning — this is a genuine market gap 50+ skincare ingredients mapped to all 4 cycle phases with compatibility scores Real-time product analysis with traffic-light ingredient warnings Science-backed nutrition recommendations per phase What we learned The connection between hormones and skin health is well-documented but underserved in consumer apps Progesterone's effect on sebum production during the luteal phase is the primary driver of cyclical breakouts Open Beauty Facts provides excellent free cosmetics data for ingredient analysis What's next for CycleGlow iOS native app with HealthKit integration. (I will have time eventually) ML-based cycle prediction (beyond simple day counting) Community feature for sharing skincare routines per cycle phase Integration with skincare e-commerce for personalized product recommendations Multi-cycle pattern recognition for long-term skin health insights <div