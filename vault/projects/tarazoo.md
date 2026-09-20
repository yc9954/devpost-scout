---
slug: "tarazoo"
url: "https://devpost.com/software/tarazoo"
title: "Tarazoo"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 384
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/small_business"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Tarazoo

> An e-commerce platform with two faces: customers checkout by camera no barcode, just the item’s look while businesses get catalog, inventory, sales, forecasting & intelligent procurement.

[Devpost](https://devpost.com/software/tarazoo) · hackathon [[Hack the North 2025]]

## Facets

**domain** [[retail_commerce]] [[supply_logistics]]
**user** [[general_public]] [[small_business]]
**substrate** [[geospatial]] [[video_visual]]

**stack** claude, cohere, cplex, minlp, next.js, pyomo, python, pytorch, scip, shopify, superbase, vercel

## How they structured the write-up

- inspiration ✨
- what it does 🛒
- how we built it 🛠️
- challenges we ran into 🚧
- accomplishments that we're proud of 🎉
- what we learned 📚
- what's next for tarazoo 🚀

## Body

App Logo Homepage Tarazoo Inspiration ✨ We wanted to make trading in e-commerce quick, natural, and effortless . Seeing experimental checkout systems in Paris and Amsterdam inspired us to go further: why shouldn’t checkout be as easy as just pointing your camera at an item, no barcode required? On the merchant side, we aimed to remove the pain of managing catalogs, inventory, forecasting, and procurement by giving businesses a smart, automated system. What It Does 🛒 Customer Face: Shoppers can open their camera, point at an item, and add it instantly to their cart—no barcode needed. Merchant Face: A full management suite for catalog editing, inventory overrides, sales tracking, demand forecasting, and procurement optimization powered by MINLP. Together, Tarazoo delivers frictionless shopping for consumers and intelligent operations for merchants . How We Built It 🛠️ Frontend: Next.js App Router (TypeScript), Tailwind CSS. Backend: Local JSON data ( backend/data ) + Supabase client ( lib/supabase.ts ). Data Management: Editable catalog, inventory, and forecasts in app/merchent/* and components/dashboard/* . Optimization: MINLP solver models purchase orders, balancing MOQ, case packs, and demand requirements. UI/UX: Optimistic saves on blur/Enter, minimal visual noise, consistent Tailwind styling. Challenges We Ran Into 🚧 Validating exactly 52 weekly demand values and 12-week forecast arrays. Keeping inline editing responsive while persisting changes reliably. Preserving legacy forecast/PO flows while introducing new editors and routes. Redirecting optimization processes seamlessly without disrupting the user flow. Accomplishments That We're Proud Of 🎉 Achieved everything we set out to build within the timeframe. Delivered a barcode-free checkout experience that feels futuristic. Integrated procurement optimization with real data, making merchant decisions smarter. Built a system that bridges the gap between customer convenience and merchant intelligence . What We Learned 📚 Designing intuitive UIs while enforcing strict backend validation. The value of optimistic UI updates with proper error handling. How to model procurement as a Mixed-Integer Non-Linear Program with real-world constraints. Inspiration matters—seeing innovative systems abroad sparked ideas we could apply globally. What's Next for Tarazoo 🚀 We want to abstract the procurement software even more , making it accessible as a standalone service that merchants can plug into any e-commerce platform. By decoupling the optimization layer, Tarazoo could evolve into a universal procurement intelligence API , powering not just our system but the entire ecosystem of online commerce. <div