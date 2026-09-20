---
slug: "deshitrip"
url: "https://devpost.com/software/deshitrip"
title: "DeshiTrip"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1308
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# DeshiTrip

> Offline-first AI travel companion for low-connectivity regions—bilingual assistance, synced squad expenses, adaptive itineraries, and SOS safety for remote travel.

[Devpost](https://devpost.com/software/deshitrip) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
  <sub>weak: cross_origin_web</sub>
**domain** [[supply_logistics]]
**user** [[developer]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** argon2, axios, cloudinary, cloudinary-storage, cors, express.js, framer-motion, geolocation-api, google-gemini, html-to-image, indexeddb, jwt, leaflet.js, lucide-react

## How they structured the write-up

- inspiration
- what deshitrip does(solution)
- how we built it
- challenges we faced
- accomplishments that we're proud of
- what we learned
- what's next for deshitrip

## Body

This is the homepage, featuring a niche background image inspired by the cultural essence of Bangladesh. Sign-up and Login page This overview dashboard shows all your created tour squads and recommends trending destinations to help you plan your next journey. The Groups page allows travelers to create squads or join existing ones seamlessly via a secure invite code Create a group by adding a tour name, destination, description, and even include non-registered members in your squad. On the Explore page, users can search destinations, apply filters, view routes on the map and generate AI-powered travel plans for any spot. In the AI Planner, enter from, to, trip duration, and group size ,AI instantly generates a personalized travel plan. It generates a day-wise itinerary with detailed activities and estimated budget for each day. It also suggests must-try local foods, essential travel tips, and a smart packing checklist for your trip. On the Expense page, add costs and memories, scan receipts via OCR, and track total spending with all group members and logged entries. View ledger history with auto-split costs, track who owes what, and settle balances seamlessly with your group members. Hold the SOS button for 3s to record 10s of audio, sent to all group members and the nearest police station automatically. Group members receive the SOS alert with a beep, voice message, and live location instantly. Community is a tour-focused hub where travelers share guides and experiences, which others can like and comment on. After a tour, generate a shareable ‘Tour Wrapped’ card with trip summary, descriptions, and any badges earned for social media. In Profile, view earned badges, upload a picture, add a bio, and customize your traveler identity Inspiration Exploring Bangladesh is a journey of discovery—but offline zones, fragmented apps, and manual expense logs turn adventure into chaos. Problems: Planning friction across fragmented platforms with massive language barriers "Bazaar Ledger" mentality forcing messy paper memos for expense logging Zero-connectivity "dead zones" in remote spots (Hill Tracts, Sundarbans) render traditional apps useless Traveler safety anxieties on isolated trails with no reliable emergency system No dedicated community platform to find trustworthy guides or discover hidden gems Our Approach: Built a localized, bilingual AI engine that understands Bangladesh's domestic economy Multimodal OCR to instantly transform paper memos into seamless digital flow Offline-First architecture ensuring critical data and budgeting tools work in zero-connectivity zones Fail-safe SOS system routing GPS and voice alerts to squads and local authorities via Twilio Unified explorer hub with Community Feed for authentic stories and viral "Tour Wrapped" cards. What DeshiTrip does(Solution) DeshiTrip is a unified platform for the modern Bangladeshi traveler: Offline Resilience : Essential data works perfectly in zero-connectivity zones, syncing the moment you return to a network. AI-Powered Itineraries : Custom plans across all 64 districts, intelligently localized by Google Gemini. Squad Expenses : Log costs, split bills, and track "who owes whom" with a robust offline-first architecture. AI Smart Scanning (OCR) : Snap a photo of any receipt. Our Gemini vision engine auto-populates expense details, even converting Bengali handwriting to digital entries. SOS Safety : A high-stakes emergency system that broadcasts live location and voice recordings to your squad. DeshiTrip goes further by automatically sending an emergency SMS (via Twilio) to the nearest police station or authority hub , ensuring help is dispatched with your exact GPS coordinates in seconds. Community Hub : A dedicated social feed where explorers share stories and tips about specific spots across Bangladesh, creating a living guide for future travelers. Gamified Discovery : Earn unique achievement badges (like Beach King for Cox's Bazar or Cloud Chaser for Sajhek) and XP as you explore. Rise from a "Rising Traveler" to a "National Legend" as you conquer all 8 divisions. Tour Wrapped : Generate beautiful, shareable cards summarizing your squad's stats and badges—ready for social media. How we built it We utilized a TurboRepo Monorepo for seamless full-stack synchronization between our Next.js frontend and Express backend. Frontend : Next.js 14, Tailwind CSS, and Framer Motion for a premium, responsive UI. Backend : Node.js/Express and MongoDB for robust data modeling and high performance. Intelligence : Google Gemini 2.5 Flash (Text & Vision) powers our AI Planning and multimodal Receipt OCR. Mapping & Routing : Integrated Leaflet and OpenStreetMap for interactive spot exploration and route visualization across Bangladesh. Offline-First Resilience : Built with Workbox and IndexedDB to ensure expense logging and safety features remain functional in zero-connectivity zones. (Flow: User Action (Offline) ➔ IndexedDB (Local Stores) ➔ Workbox Background Sync ➔ Network Detected ➔ MongoDB Cloud Sync) Real-Time Engine : Used Socket.io to enable instant, bi-directional SOS alerts between squad members. Real-World Alerts : Integrated Twilio SMS API to bridge the gap between digital safety and physical notifications for emergency contacts. Social & Media : Leveraged Cloudinary for optimized image hosting and html-to-image for generating our viral "Tour Wrapped" cards. More Details Challenges we faced SOS Reliability in 2G Zones : Guaranteeing emergency alerts in remote spots like the Hill Tracts was our biggest hurdle. We implemented a Heartbeat-Monitor & Chunked Buffer system for Socket.io. This ensures that voice recordings and GPS coordinates are buffered locally and re-attempted the second a flicker of signal returns, backed by a Twilio SMS fallback for critical delivery. Bilingual AI & Contextual Intelligence : Handling "Code-Switching" (mixing Bengali and English) in our AI Planner was complex. We had to engineer specialized system prompts to ensure the AI understands local transport logic—like the significant price delta between a local AC bus and a Green Line Scania—and provides accurate BDT estimations in both languages. Sync Conflict Management : In a squad environment where multiple users might log expenses in "dead zones" simultaneously, we built an Optimistic UI with Last-Write-Wins (LWW) versioning . This keeps balance calculations accurate across devices even after hours of offline use. Client-Side Synthesis : Generating "Tour Wrapped" cards required converting complex React components into high-quality JPEGs using html-to-image entirely in the browser to avoid server-side overhead and maintain user privacy. Accomplishments that we're proud of End-to-End Synergy : We built a complete lifecycle—moving from a paper receipt ( OCR ) to a social story ( Community Hub ) and finally a viral summary ( Tour Wrapped ). Mission-Critical Safety : Our SOS system is fail-safe, using Socket.io heartbeats and Twilio SMS fallbacks to ensure alerts reach both squad members and local authorities in 2G zones. Robust Sync Engine : Perfecting an Offline-First architecture that keeps squads in sync even after hours in zero-connectivity tea gardens or forest trails. Local Context : Creating an AI that truly understands Bangladesh—from BDT estimations to bilingual "Code-Switching" and regional transport logic. Full-Stack Monorepo : Scaling a professional TurboRepo architecture that synchronizes all features seamlessly across the entire ecosystem. What we learned Resilient Architectures : Implementing PWA background sync and Socket.io heartbeats to maintain connectivity in 2G zones. Critical Integrations : Leveraging the Twilio API for real-world SMS alerts and the Web Share API for native social memory sharing. Performance Engineering : Using Web Audio API and TurboRepo to build a fast, enterprise-grade monorepo that works even in low-bandwidth environments. What's next for DeshiTrip Scaling for Global Tourism : While we began with a deep focus on Bangladesh, our architecture—from the bilingual AI to the offline-sync engine—is built to scale. We plan to integrate multi-currency support and global travel APIs (like Amadeus or Skyscanner) to make DeshiTrip the preferred companion for international travelers exploring emerging markets worldwide. Ticketing & Logistics : Full real-time integration with Shohoz and GoZayaan for direct bus, launch, and train bookings within the squad hub. AR Heritage Guide : Using Augmented Reality to bring history to life—scan landmarks like Mahasthangarh or the Pyramids to see 3D reconstructions and historical facts. Sustainable Marketplace : Enabling verified local guides and home-stays to list services directly, creating a community-driven ecosystem that empowers local economies globally. <div