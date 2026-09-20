---
slug: "auraguard"
url: "https://devpost.com/software/auraguard"
title: "AuraGuard"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 587
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/agriculture_food"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# AuraGuard

> An AI-powered brand protection platform

[Devpost](https://devpost.com/software/auraguard) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[cross_origin_web]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[agriculture_food]] [[labor_employment]] [[retail_commerce]] [[transportation]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** fastapi, google-gemini, mutagen, next.js, piexif, pillow, postgresql, python, react, supabasevercel, tailwind-css, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for auraguard

## Body

Inspiration With the explosive rise of web scraping, automated bots, and unauthorized data harvesting, digital creators and e-commerce brands are completely losing control over their original imagery. Traditional visible watermarks ruin the user experience and are easily cropped out or scrubbed by AI tools. We were inspired to build AuraGuard to create a stealthy, modern line of defense—giving creators a way to securely tag, track, and prove ownership of their digital assets across the web without altering their visual beauty. What it does AuraGuard is a complete brand protection and asset tracking platform. When a creator uploads an asset to their dashboard, AuraGuard automatically embeds a unique, invisible tracking signature deep into the file's metadata. The platform then deploys an automated web-crawling engine that inspects target web domains and online marketplaces. The crawler systematically pulls images, decodes their underlying payloads, and checks them against our secure registry. If a match is flagged, AuraGuard uses advanced AI models to synthesize raw tracking data into clear, human-readable threat impact summaries, alerting the owner exactly where and how their work is being misused. How we built it We engineered AuraGuard as a decoupled, multi-service monorepo built using an advanced tech stack: The Control Center: A polished frontend dashboard built with Next.js 16 , React 19 , and Tailwind CSS 4 , deployed globally on Vercel for instant, static speed. The Forge Engine: A dedicated backend Python daemon utilizing Pillow , Mutagen , and piexif that handles the heavy lifting of processing queues and stamping secret tracking tokens ( AG-XXXXXXXX ). The Sandbox Storefront: A standalone mock e-commerce site engineered with FastAPI specifically to act as a target destination for end-to-end scanner pipeline testing. Database & Cloud Layer: Backed by Supabase (PostgreSQL) with strict Row Level Security (RLS) tracking files, automated scan results, and service heartbeats. The backend services are hosted concurrently using Railway . Challenges we ran into Our biggest challenge was shifting our multi-service setup from a cozy local development network onto live cloud infrastructure. Initially, trying to push a complex monorepo caused our background processing worker and our mock storefront to conflict over container roots and ports on a single service block. We overcame this by diving deep into infrastructure-as-code principles, breaking our single cloud repository link into independent micro-services on Railway's canvas dashboard, mapping distinct root directory paths, and orchestrating cross-origin communication between Vercel, Supabase, and our API endpoints. Accomplishments that we're proud of We are incredibly proud of building a fully functional, end-to-end simulation environment. Instead of just coding a simple "concept" page, we built an actual live mock shop to actively test our backend crawler against. Watching our system crawl an independent cloud URL, extract a hidden metadata tag, and instantly push a real-time alert back to our dashboard was an amazing milestone. What we learned We gained a massive amount of experience regarding microservice orchestration, handling environment isolation across modern cloud providers, and managing complex multi-language repositories (TypeScript + Python). We also learned how to effectively leverage large language models like Google Gemini to instantly parse chaotic database rows into clean, actionable intelligence for end users. What's next for AuraGuard We want to take AuraGuard's tracking signatures to the next level by implementing robust steganography—hiding the unique identifier strings dynamically inside the pixel values themselves so that the tracking ID remains intact even if a bad actor strips the image's EXIF metadata or recompresses the file. We also plan to build automated DMCA takedown notice generators fueled directly by our AI impact summaries. <div