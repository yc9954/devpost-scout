---
slug: "parallax-edge"
url: "https://devpost.com/software/parallax-edge"
title: "Parallax Edge"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 710
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/geospatial"
---

# Parallax Edge

> The "Absolute Zero" for price. Parallax Edge scans every delivery and e-commerce app to find the mathematical minimum price. No hidden fees, just pure savings across your entire shopping list.

[Devpost](https://devpost.com/software/parallax-edge) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[retail_commerce]] [[supply_logistics]]
  <sub>weak: education, transportation</sub>
  <sub>weak: educator_student</sub>
**substrate** [[geospatial]]

**stack** beautifulsoup4, docker, fastapi, git, httpx, leaflet.js, lucide-react, next.js, node.js, pydantic, python, render, tailwind-css, thefuzz

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for parallax edge

## Body

Home Dashboard: A real-time aggregator comparing 12+ apps to find the "Total Landed Cost" using live pincode verification. find the best deals, lowest fees, and fastest delivery in real-time. Search Results: Interactive product cards highlighting "Best Price" vs "Fastest Delivery" with one-click platform visits. Local Supply Map: Geospatial heatmap tracking dark store latency, traffic jitter, and hub-load for precise delivery timing. Quantum Split Optimization—automatically dividing a 5-item cart across 3 different platforms to minimize total delivery fees Review Sentinel: NLP sentiment heatmap analyzing build quality and authenticity across 20+ platforms to filter fake feedback. Green Edge Score: Sustainability tracker visualizing $CO_2$ impact and carbon radii for eco-friendly delivery choices. Campus Deals: Hyper-local P2P flash-pools for VIT students to unlock community discounts and local vendor bundles. AI Price Oracle: ML engine providing "Buy vs Wait" signals and projecting potential savings through dynamic price forecasting. Smart Cart Drawer: Multi-platform sidebar for real-time item management and immediate cost optimization. Cart Optimizer: Advanced algorithm solving the "Knapsack Problem" to split baskets for the absolute lowest total bundle cost. Personalization Tabs: Features "Search History" and "AI Personas" to pre-fetch data for "Emergency" or "Bargain" shoppers. Inspiration The modern Indian shopping landscape is a battlefield of hidden costs. Between giants like Amazon and disruption-heavy Q-commerce like Blinkit and Zepto, finding the absolute "best deal" has become impossible. We found ourselves manually switching between four apps to save ₹30 on groceries, only to lose those savings to an invisible "surge fee" at checkout. We built Parallax Edge to be the "Truth Layer" for commerce—an unbeatable engine that exposes the real math behind every purchase. What it does Parallax Edge is a hyper-local price intelligence engine that bridges the gap between national logistics and lightning-fast dark stores. Ultimate Delivery Comparison : We scan the entire ecosystem (Amazon, Flipkart, Blinkit, Zepto, and more) simultaneously to hunt down the absolute minimum price for any single item. Total Landed Cost (TLC) : Our engine goes beyond the price tag. We calculate the real final cost—Base Price + Delivery + Platform Fees + Surge—showing you the winner in one view. AI Cart Orchestrator : For multi-item shopping lists, our "Splitting Algorithm" automatically finds the cheapest combination (e.g., "Heavy essentials from Amazon, perishables from Zepto" ). Location-Aware Scanning : Automatically detects pincode-level inventory and delivery speed to show real product availability in your specific neighborhood. Community Flash Pools : A social intelligence layer where neighbors can join order-pools in real-time to trigger bulk-discounts. How we built it The Brain (FastAPI/Python) : Built an asynchronous engine using httpx for high-speed concurrent scraping. We implemented thefuzz for complex string-reconciliation to group identical products that have different titles on different apps. The Command Center (Next.js 15) : A visual-first terminal interface built with TypeScript and a custom glassmorphism design system to provide a premium "Cyberpunk Bloomberg" experience. DevOps : Fully containerized with Docker , orchestrated via Docker Compose , and deployed using Render (Backend) and Vercel (Frontend). Challenges we ran into "Reconciling the Chaos." Every app names products differently. Matching "Organic Milk 1L" to "Full Cream Amul 1000ml" required us to build a custom logic layer using fuzzy math and category weights. We also had to optimize our async pipeline to ensure that looking up 10 apps at once didn't hit rate limits or slow down the user's experience. Accomplishments that we're proud of We successfully built a working prototype that can fetch and reconcile live data from across the Indian commerce landscape in under 5 seconds. Seeing our AI Cart Optimizer correctly suggest a "split order" that saved a test user ₹140 on a 10-item grocery list was our proudest "Aha!" moment. What we learned We mastered the intricacies of Asynchronous Python Orchestration and Fuzzy Data Reconciliation . More importantly, we learned that in the modern economy, "Time is Money"—and that a product's price is meaningless without knowing its ETA and platform fee. What's next for Parallax Edge The "Edge" Chrome Extension : A real-time popup while you shop on Amazon that says: "Stop! This is ₹50 cheaper at a dark store 2km away." One-Click Checkout : Direct deep-linking that fills your carts across multiple optimized apps instantly. Dynamic Price Prediction : AI-powered "Buy Now vs. Wait" advice based on historical surge pricing patterns. <div