---
slug: "geodrive-ai"
url: "https://devpost.com/software/geodrive-ai"
title: "GeoDrive AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 645
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# GeoDrive AI

> GeoDrive AI – Turning Real‑Time Automotive Sentiment into Actionable Intelligence.

[Devpost](https://devpost.com/software/geodrive-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]
  <sub>weak: financial_record</sub>

**stack** axios, charts.js, css3, fastapi, github, html5, javascript, natural-language-processing, postgresql, python, python-dot, react, react-leaflet, render

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for geodrive ai

## Body

Home page layout with 3d model car for better ui Dashboard part 1 where user can input text which will be processed and will properly inserted in the database Dashboard part 2 where user input a specific company name or model and gets insight of that, it contains ai generated summary. Dashboard part 3 where we see whether the company improving or not also it show positive review last 30 days and the change made by company Dashboard part 4 where we compare models and get the best based on review Dashboard part 5 where we show from where our user give the review on the map, also shows the recent review on which company at the top . Dashboard part 6 shows radical graph for specific company and bar chart of all the reviews of all company Competitive intelligence which helps company to do deep analysis on there and other models Last is our team info Hello everyone, we are team Axionminds, and below is our problem statement description GeoDrive AI GeoDrive AI - Turning Real‑Time Automotive Sentiment into Actionable Intelligence. Inspiration Automotive companies release new models every year, yet product decisions often rely on delayed surveys, dealership feedback, or limited focus groups. We asked ourselves: What if R&D teams could see real-time customer sentiment, feature-level pain points, and competitive gaps-instantly? The inspiration came from the growing gap between raw customer feedback and actionable product intelligence. Social media, reviews, and public sentiment contain massive insight — but it is unstructured and hard to interpret at scale. GeoDrive AI was built to bridge that gap. What it does GeoDrive AI is an AI-powered automotive intelligence platform that: Analyzes customer reviews using NLP Breaks down sentiment by feature (mileage, performance, comfort, etc.) Compares competing models Detects brand trends over time Maps sentiment geographically Generates AI-driven product insights Exports executive-ready PDF reports For R&D teams, this means: Identify weak features early Detect competitive advantages Monitor market perception shifts Make data-backed product improvements How we built it Backend FastAPI for high-performance APIs PostgreSQL (Supabase) for structured storage SQLAlchemy ORM Trend algorithms comparing rolling 30-day windows Feature-level sentiment aggregation logic AI Layer NLP-based sentiment classification Topic fingerprint scoring AI-generated executive insights Confidence scoring system We structured sentiment scoring as: //SentimentScore = (positive - negative)/totalReviews Trend detection compares: //Trend=S(recent) −S(previous)​ Where: S(recent) = Sentiment score (last 30 days) S(previous) = Sentiment score (previous 30 days) Frontend React.js Chart.js (Radar, Bar, Pie visualizations) Leaflet for geo sentiment mapping Dynamic dashboards PDF report export functionality DevOps GitHub version control Automated deployment via Vercel (frontend) Backend deployment with API integration Challenges we ran into Database connection issues We faced multiple DNS and Supabase connection problems during deployment. Merge conflicts Simultaneous frontend/backend development caused conflicts that required careful rebasing and resolution. UI scaling issues When rendering large model lists, layout overflow caused inconsistent dashboard heights. We solved this by implementing controlled scroll containers. Deployment entrypoint errors FastAPI entrypoint configuration required restructuring to match deployment platform expectations. Accomplishments that we're proud of Built a full-stack AI intelligence system from scratch Implemented real trend detection logic Created feature-level sentiment radar visualization Integrated geo-mapping of automotive sentiment Delivered export-ready executive reports Built competitive intelligence comparison engine Most importantly: We transformed unstructured feedback into structured R&D intelligence. What we learned Real-time sentiment analytics can significantly improve product iteration cycles. Clean backend architecture prevents scaling bottlenecks. Deployment planning is as important as development. Cross-team collaboration requires version control discipline. UI consistency dramatically affects perceived product quality. We also learned how to handle: Production-grade database connections Environment variable configuration API route management Data normalization strategies What's next for GeoDrive AI Advanced roadmap: Real-time streaming ingestion (Kafka integration) Predictive defect forecasting Automated feature recommendation engine Competitive market share estimation Dealer-level insight dashboards Multi-language sentiment support Enterprise R&D SaaS version Long term vision: Become the intelligence layer powering automotive product innovation. <div