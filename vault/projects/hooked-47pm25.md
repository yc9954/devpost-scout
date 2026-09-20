---
slug: "hooked-47pm25"
url: "https://devpost.com/software/hooked-47pm25"
title: "Hooked"
hackathon: "UNIHACK 2026, funded by the European Union"
organization: "UNIHACK"
winner: true
words: 1041
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Hooked

> An AI-powered FishDex that transforms fishing into conservation. Gamify your catches, get hyper local insights, and track invasive species to protect our waterways.

[Devpost](https://devpost.com/software/hooked-47pm25) · hackathon [[UNIHACK 2026- funded by the European Union]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[climate_energy]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** .net, c#, gemini, leonardo.ai, maui, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hooked

## Body

Achievements earned by the user Notifications page Profile page Fishdex - shows all fish the user has caught Shows the details on individual fish species and personal bests. Home page on the desktop web version, with all posts and options to start your fishing session. Upload image for fish for AI detection Elastic dashboard for use for the fisheries to track invasive species, endangered species and more Inspiration Hooked was born from a deep-rooted passion for Australian fishing and an urgent environmental mandate: the critical need to manage and track invasive fish species devastating our native waterways. We realised that while fishing is a beloved pastime, the barrier to entry for beginners is high, and localised, actionable data is scarce. We envisioned a solution that gamifies conservation. Inspired by the concept of a digital "FishDex," we set out to turn scattered photos, anecdotal notes, and local knowledge into a smart, AI-powered ecosystem that helps anglers catch more fish while actively protecting Australia's aquatic biodiversity. What it does Hooked is not just a fishing app; it is an intelligent, gamified conservation and angling companion. The Smart FishDex: Anglers can seamlessly log their catches with rich media and metadata. AI-Powered Identification & Insights: Using Google Gemini AI, Hooked automatically helps identify species from photos—especially crucial for distinguishing native fish from harmful invasive species—and provides real-time, personalised tips on bait and tackle. Stunning Gamification: Powered by Leonardo AI, the app generates beautiful, custom achievement badges and dynamic visual assets as users level up, earn XP, and complete localised fishing challenges. Advanced Spot Sharing & Mapping: A highly interactive map allows users to share hidden gems with friends or mark restricted/invasive hotspots. Hyper-Local Insights: An intuitive dashboard synthesises real-time data on local tides, lunar cycles, weather, and water conditions, making the learning curve disappear for beginners. Environmental & Social Impact: By tracking the spread and extraction of invasive species, anglers actively clean up waterways. We take this a step further by providing dedicated Elastic dashboards directly to local fisheries and environmental agencies . This empowers authorities to track endangered native fish, monitor the real-time spread of invasive species, and make data-driven decisions on exactly where to execute native fish stocking programmes. We are turning every recreational fishing trip into a powerful, community-driven conservation effort. How we built it We engineered Hooked using a robust, hybrid technology stack designed for scale and performance: Frontend: Developed entirely in .NET MAUI using Visual Studio 2026, leveraging C# alongside embedded HTML, CSS, and JavaScript components to deliver a flawlessly smooth, cross-platform mobile experience. Search & Analytics Engine: We integrated Elasticsearch at the core of our data architecture. Elastic handles complex geospatial queries for map features and blazingly fast full-text search for the FishDex. Crucially, it aggregates massive amounts of crowd-sourced catch data to power our dedicated fisheries dashboards, translating raw data into visual, actionable environmental intelligence. Artificial Intelligence: We wired Google Gemini into our backend pipeline for sophisticated image analysis, natural language processing, and dynamic fishing advice. Meanwhile, Leonardo AI was utilised in our design pipeline to generate breathtaking, award-worthy UI assets, avatars, and gamification rewards. Challenges we ran into Building a world-class, multi-faceted platform came with significant hurdles: Complex Data Modelling: Designing a schema that could simultaneously serve a lightning-fast personal FishDex on mobile and feed into heavy, aggregated Elastic indices for broad ecosystem trend analysis by government fisheries. AI Integration on Mobile: Ensuring that Gemini’s image recognition and insights were delivered seamlessly without lagging the mobile experience. UI/UX Harmony: Bridging the gap between native C# components and embedded web technologies (HTML/CSS/JS) to maintain a cohesive, award-winning interface. Educational Onboarding: Crafting an onboarding flow that educates beginners on the nuances of Australian fishing and the critical importance of invasive species management without feeling like a lecture. Accomplishments that we're proud of We are incredibly proud to have built an end-to-end, polished application that successfully bridges the gap between recreation and conservation. We successfully engineered a seamless Catch-to-Elastic-to-Insights pipeline, meaning the moment an angler logs an invasive fish, the global map updates, XP is awarded via our Leonardo AI-generated badge system, Gemini provides context-aware feedback, and the data is instantly available on our fisheries dashboard. We created a highly engaging social ecosystem that encourages outdoor activity, peer-to-peer learning, and spot-sharing. Most importantly, we've gamified environmental impact, creating a platform where having fun directly correlates with cleaning up Australian waterways and providing critical data to help rebuild native fish stocks. What we learned This project was a masterclass in modern application architecture: Data is Everything: We learned that robust data modelling and the raw power of Elasticsearch unlock entirely new product features—what started as a simple logbook evolved into a real-time invasive species tracking engine for environmental authorities. AI Lowers Barriers: Integrating Gemini taught us that AI is the ultimate tool for accessibility; it replaces hours of frustrating beginner research with instant, actionable guidance. UX Drives Mission: We discovered that to drive social and environmental impact, the user experience must be flawless. Gamification and beautiful design (aided by Leonardo AI) are just as important as the underlying code when it comes to user retention and community building. Tech Stack Synergy: Establishing strict, clean contracts between our C# backend, AI microservices, Elastic clusters, and mixed MAUI frontend was essential for maintaining stability. What's next for Hooked The future of Hooked is expansive and impactful: Predictive Environmental Analytics: We plan to deepen our Elastic integration to offer predictive trend analysis—forecasting invasive species movements and ideal fishing conditions based on historical data. Conservation Partnerships: We aim to expand our rollout of bespoke Elastic dashboards to more Australian environmental agencies (like the CSIRO) and local councils, aiding in national conservation efforts, pinpointing native stocking locations, and organising targeted eradication of invasive pests. Enhanced AI Capabilities: Rolling out advanced Gemini-powered conversational agents where users can literally "talk" to their FishDex to ask for real-time advice on the water. Social Expansion: Introducing competitive community leaderboards, deeper privacy controls for secret fishing spots, and local tournaments focused on invasive species removal. Global Reach: While our heart is in Australia, the architecture is infinitely scalable. We plan to adapt Hooked’s AI and Elastic models for diverse ecosystems worldwide, bringing our gamified conservation movement to a global audience. <div