---
slug: "foodbank-automation"
url: "https://devpost.com/software/foodbank-automation"
title: "AI-Powered Food Bank Management System"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 292
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/social_worker"
---

# AI-Powered Food Bank Management System

> Food banks lose time at intake. Our web app makes any phone a scanner: scan, auto-fill, add weight. Live inventory + instant CSVs for audits. Faster check-ins mean more families served, less waste.

[Devpost](https://devpost.com/software/foodbank-automation) · hackathon [[Cal Hacks 12.0]]

## Facets

**domain** [[agriculture_food]] [[finance_payments]] [[supply_logistics]]
**user** [[social_worker]]
  <sub>weak: video_visual</sub>

**stack** creao, flask, gemini, node.js, openfoodfacts, python, react, typescript, vercel

## Body

Home UI and Inventory Recipe Generation Barcode Scanning Inspiration When we talked to our local food bank, one theme kept coming up: logging donations takes forever. Every can, every label, every nutrition field has to be typed in. Meanwhile, people are waiting in line. And sometimes perfectly good food expires in storage because no one realizes it is there. We wanted to fix that. Our goal was to build a tool that gives volunteers time back and helps more food reach families while it is still fresh. How We Built It We built a web app so that all volunteers need is a phone. They scan a barcode or snap a quick photo and the system fills in product details automatically. We used React and TypeScript on the front end and connected to AI services for barcode lookup, food recognition and recipe generation. The app tracks quantities, filters by dietary rules and even suggests meals based on what is about to expire. Everything updates instantly so staff always know what they have on hand. Challenges We learned that building something simple is not simple at all. Food banks deal with low-signal environments, inconsistent donations and items without barcodes. Training the system to recognize food accurately took a lot of iteration. We also had to think carefully about accessibility and making sure anyone could use it without training. What We Learned Talking to users early changed our entire direction. We learned that the best productivity tools remove friction instead of adding more features. We also learned how to blend AI tools with real-world needs: offline support, clear instructions and fail-safes for bad scans or missing data. Most importantly, we saw how technology can directly support communities when built with care and empathy. <div