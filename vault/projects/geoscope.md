---
slug: "geoscope"
url: "https://devpost.com/software/geoscope"
title: "GeoScope"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 427
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# GeoScope

> GeoScope is a Business Hotspot Scoring web app that empowers micro-retailers by converting Google Maps data into transparent, location-based business scores.

[Devpost](https://devpost.com/software/geoscope) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[developer_tools]] [[finance_payments]] [[transportation]]
**user** [[small_business]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** chart.js, framer, google-directions, google-geocoding, google-maps, google-places, next.js, puppeter, tailwind, three.js, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for geoscope

## Body

Inspiration Across regions like Latin America, Africa, and South Asia, many small businesses struggle to access financing, even when their locations have great potential. GeoScope was created to help business owners showcase the value of their location using real data. What it does GeoScope calculates a Business Hotspot Score (0–100) for any shop address. Users select a business type, and instantly receive scores for: Foot Traffic Index Safety Score Transit Accessibility Competition Density No sign-in, no paperwork. Just data + location = score. How I built it Frontend : Built with Next.js 14 (App Router) , Tailwind CSS for styling, and Framer Motion for animations. Edge Functions : Everything runs serverlessly through Vercel Edge Middleware , so no traditional backend is needed. APIs Used : Google Maps JavaScript API Google Geocoding API Google Places API (using Places Aggregate for business insights) Google Directions API (Transit mode) Scoring Engine : Written in TypeScript inside /lib/location-store.ts . All scores are calculated using custom heuristics—no ML yet, just logic that's easy to explain and tweak. Challenges I ran into Google API rate limits were tighter than expected. Had to optimize requests with field masking and filter logic to stay within free limits. Foot-Traffic AI is still in beta, and getting accurate, normalized data from it was kind of a guessing game. Scoring fairly across regions (rural vs urban) is tough. A quiet area in a small town shouldn’t get punished unfairly just for being less dense. Edge Middleware debugging got confusing sometimes, especially during hydration or local development. Accomplishments that I'm proud of Deployed a fully working credit scoring engine on the edge, with ~2 ms response time Designed a clean UI that works great on desktop and mobile Made the scoring system 100% transparent—users can actually understand how the score was calculated Learned a ton about API optimization, edge computing, and real-world geospatial logic And honestly? Built something that could actually make a difference for someone. What i learned Google Maps Platform is super powerful if you know how to chain the APIs properly You don’t always need machine learning—sometimes clear, explainable logic is more valuable, especially in fintech Optimization matters: reducing payloads, masking fields, bundling only what’s needed = fast apps Edge + Next.js 14 is such a solid combo for building real-world tools fast What's next for GeoScope Here’s what I plan to add next: Use kernel density estimation to improve competition fairness in dense city areas Later: build a GNN (Graph Neural Network) to learn non-linear place patterns Let users save or compare multiple locations <div