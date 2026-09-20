---
slug: "cartify-c7dmlr"
url: "https://devpost.com/software/cartify-c7dmlr"
title: "Cartifyy"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 630
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/geospatial"
---

# Cartifyy

> AI agent that solves shopping confusion, time waste, forgetfulness & budget stress.

[Devpost](https://devpost.com/software/cartify-c7dmlr) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[geospatial]]
  <sub>weak: structured_db</sub>

**stack** groq, javascript, json-based-cart-schema, llm-powered-ai-agent, react.js, rest-apis, supabase-(auth-&-database), supabase-edge-functions, tailwind-css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for cartify
- final impact

## Body

Title: Cartify - The AI-Powered Task-to-Cart Agent for Every Shopper Inspiration We've all been there. You open your shopping app, just trying to cook biryani or prep for a house party. But then - 23 ingredients, 10 YouTube videos, and 14 tabs later - you're frustrated, confused, and still forget the milk. Shoppers don't want filters and categories. They want help. They want something that understands the task behind the purchase. Ecommerce stores are struggling too - carts are abandoned, budgets blown, essentials forgotten. Shoppers waste time. Merchants lose revenue. We weren't just building a feature. We were solving a human emotion - the gap between "I want to..." and "I bought it." That's why we created Cartify - your shopping copilot. What it does Cartify transforms a user's task - like "Make biryani under $500" , into a complete, ready-to-checkout cart on any ecommerce site. With one line of input, Cartify: Understands what you need (ingredients, items, quantities) Understands how you feel (lazy Sunday? busy Monday? festive mood?) Stays within your budget Saves your habits into reusable smart bundles Lets you reorder anything - in one tap It works across any ecommerce store. It's fast, smart, and deeply personalized. From forgetful shoppers to merchants struggling with low cart size - Cartify solves both. How we built it Frontend SDK : React + Tailwind CSS A lightweight SDK embeddable in any ecommerce store (Cartify's core experience) Cartify Agent : Groq API + Llama 3.5 Converts user goals like "Snacks for $300" into structured JSON cart formats Backend : Supabase (auth, DB, bundles) Handles user sessions, cart memory, API requests, and analytics events Edge Functions : Performs smart budget logic, seasonal detection, mood analysis, cart generation triggers Analytics Engine : Real-time dashboards in the Merchant Portal Tracks bundle popularity, average cart value, top-selling SKUs, etc. Memory Layer (Cartify Memory) : Stores smart bundles, reorder patterns, nudge triggers, seasonal restock logic Challenges we ran into API Rate Limits : The ecommerce API we used had a limited number of search requests. Once we exceeded it, we had to constantly re-authenticate with alternate accounts , slowing our build cycle. Agent ↔ App Integration : The Cartify Agent generated cart data in JSON, but aligning that with the frontend SDK and product schema was tricky. Schema mismatches caused bugs until we stabilized the format. Cart Memory System : Saving and retrieving bundles based on user, season, and context was more complex than expected. We had to carefully design Supabase tables and edge logic for privacy and speed. Accomplishments we're proud of Built a complete shopping agent , fully AI-powered, context-aware, and store-ready Cart generation happens in under 2 seconds via Groq's blazing speed Created reusable Smart Bundles that remember and re-trigger weekly Developed a real-time dashboard with trend and conversion analytics Embedded intent + emotion + budget understanding into shopping Did it all inside Bolt.new , without switching tools What we learned Users don't want to browse , they want outcomes. Task-first shopping is the future. Connecting agents to real actions (cart, reorder, checkout) is 90% of the work Memory is not a luxury , it's the bridge to loyalty Bolt.new is powerful , from idea to execution, it enabled full-stack development and deployment What's next for Cartify Voice-to-Cart: Add voice input for hands-free, natural shopping One-click Shopify & Flipkart plugins Bundle Marketplace for influencers and creators Visual Drag-and-Drop Field Mapping (Zapier-style) More Agent Skills (meal planning, checklist mode, etc.) Final Impact Cartify doesn't just speed up shopping. It removes mental friction, adapts to emotions, and turns scattered intent into smart execution. For shoppers , it's a 2-minute solution to a 30-minute problem For stores , it's bigger carts, smarter bundles, and repeat revenue Let's redefine ecommerce , one cart at a time. <div