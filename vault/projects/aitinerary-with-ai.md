---
slug: "aitinerary-with-ai"
url: "https://devpost.com/software/aitinerary-with-ai"
title: "Aitinerary with AI"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 636
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/immigration_refugee"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Aitinerary with AI

> AITINERARY is a smart, AI-powered travel planner that creates immersive, personalized itineraries using Google Maps 3D and Gemini AI—turning exploration into a visual storytelling experience.

[Devpost](https://devpost.com/software/aitinerary-with-ai) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[immigration_refugee]]
**substrate** [[document_pdf]] [[geospatial]] [[web_dom]]

**stack** css, gemini, google-maps-javascript-api, html, javascript, tailwind, vite

## How they structured the write-up

- about the project: aitinerary – immersive 3d ai-powered travel planner

## Body

AiTinerary About the Project: AITINERARY – Immersive 3D AI-Powered Travel Planner QUICK LINKS Demo (Protected): https://codersbeyondborders.co.in/projects/aitinerary/ Username: googledevpost Password: G00gl3EDM@p5 GitHub: https://github.com/codersbeyondborders/AITINERARY/tree/dev Video: https://www.youtube.com/watch?v=8W2W2WxaGK4 Categories: AI , Travel , Immersive Note: This project is an enhanced and evolved version of a previously submitted entry for the Google Photorealistic 3D Maps Challenge 2024 . Building on the original concept, this version integrates Google Gemini AI, improves UX, and expands itinerary intelligence with a live deployment. Inspiration AITINERARY was born out of a simple yet powerful idea: make travel planning exciting, intelligent, and immersive . Too often, travelers are overwhelmed by scattered blogs, rigid tour packages, and static lists. We imagined a future where generative AI could create smart itineraries , and Google Maps’ 3D capabilities could let users explore them visually — all from a single-page app. The spark came during the Google Photorealistic 3D Maps Challenge, where I realized the potential of blending the rich 3D map layers with conversational AI to reimagine the way people explore destinations. How It Was Built AITINERARY is a lightweight, single-page app built with: Vite (Vanilla JS + HTML + CSS) for fast build and deploy Google Maps JavaScript API to render a photorealistic 3D globe experience Google Gemini AI (via @google/generative-ai) to generate structured, city-based itineraries in JSON cPanel-based hosting deployed under a subdirectory on a real domain: https://www.codersbeyondborders.co.in/projects/aitinerary The app dynamically takes a city and number of days as input, sends a prompt to Gemini, and displays the returned structured itinerary over an immersive 3D Map canvas. It’s designed to be visual-first, simple to use, and easily expandable with markers, routes, and user interactivity. What I Learned Prompt engineering is everything : To generate usable, structured output from Gemini AI, the prompt had to be precise and instructive. 3D Maps unlock user delight : Seeing itinerary points on a spinning, tilted, zoomable Earth adds a “wow” factor. Minimal UI can still deliver big value : Even without heavy frameworks, combining Maps + AI can offer a high-impact experience. Deploying to subdirectories requires special handling : Setting correct Vite base paths and using .htaccess for routing taught us practical lessons in static site deployment. Challenges I Faced API limits and costs during prototyping with Gemini and Maps Balancing design with deployment constraints (e.g., subdirectory routing and browser compatibility) Parsing structured JSON responses reliably from Gemini in real-time Mapping AI-generated places to real-world POIs for visualization and interactivity What Makes It Special AITINERARY stands out because it’s not just a planner — it’s an experience. It brings together AI-driven personalization and Google’s immersive 3D technology to help travelers visualize their journey before it even begins. It’s fast, live, and built with simplicity and accessibility in mind. What's Next for AITINERARY with AI AITINERARY is just the beginning of a smarter, more immersive travel experience. With the foundations of Google Maps Platform and Gemini AI in place, I am exploring the next wave of innovations: Maps + AI + AR Using Google Maps’ photorealistic 3D and augmented reality capabilities, I plan to: Let users “fly through” their itinerary Preview routes, views, and locations using AI-narrated story mode Accessibility & Sustainable Travel I aim to embed inclusive and eco-conscious options by: Highlighting wheelchair-friendly routes Prioritizing local and green tourism Giving carbon-conscious travel suggestions using AI heuristics Mobile Experience & Shareable Exports I am developing a mobile-first interface where users can: Edit and customize AI-generated plans Save and export itineraries as PDFs , Google Maps links , or interactive trip cards Open Data + User Contributions Future versions will allow: Users to vote or submit improvements to AI-generated plans Integration with travel APIs and user reviews for better recommendations AITINERARY's future lies at the intersection of intelligence, immersion, and impact — redefining how we explore the world, one itinerary at a time. <div