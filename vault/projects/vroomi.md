---
slug: "vroomi"
url: "https://devpost.com/software/vroomi"
title: "Vroomi"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 945
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/government_staff"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Vroomi

> Vroomi is a student-first carpooling app that makes commuting safer, cheaper, and greener. Verified users share rides, split gas, and get matched through smart routing.

[Devpost](https://devpost.com/software/vroomi) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[finance_payments]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]] [[government_staff]]
**substrate** [[financial_record]] [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** leaflet.js, react, stripe, supabase, tailwind, typescript

## How they structured the write-up

- inspiration ✨
- what it does 🔥
- how we built it 🛠️
- challenges we ran into 💥
- accomplishments that we’re proud of 🎉
- what we learned 🧠
- what’s next ⏭️

## Body

Cover Image Problem Statement Issues we're tackling Introducing VROOMI Comparison Against Competitors Adding Vehicles Driver's Dashboard Driver's Ride history Driver's Ride history (2) Updating Vehicle information Selecting the most optimized path route Inspiration ✨ Getting around as a student isn't always easy. Between unpredictable public transit, the rising cost of fuel, and the need to feel safe—especially at night—commuting can feel like just another daily stressor. While today’s mobility apps promise convenience, they rarely serve the unique realities of student life, where tight budgets, shared schedules, and trust matter most. What if getting to class, work, or back home didn’t mean sacrificing your wallet, your safety, or the planet? Now introducing Vroomi—a campus-first ride-sharing platform built specifically for students. Whether you're heading to a 9 a.m. lecture or a late-night study session, Vroomi connects you with trusted peers traveling your way. With intelligent ride matching, real-time routing, and built-in safety features, we’re making commuting simpler, cheaper, and greener—without compromise. What it does 🔥 As a project focused on sustainable and student-centered transportation, Vroomi bridges digital convenience with real-world commuting through a seamless ride-sharing experience. Users log in with their verified university email, gaining access to a trusted network of students traveling to and from campus. Our platform intelligently matches riders based on departure time and location, and uses custom-built algorithms to generate the most efficient multi-passenger routes. Once matched, passengers pay drivers through our in-app payment system, which calculates fair pricing using vehicle-specific mileage estimates—automatically splitting gas costs with zero hassle. Payments are processed securely, with a low 2% platform fee ensuring long-term sustainability. On top of that, our rating system and verification safeguards ensure accountability and safety for both drivers and passengers. By focusing on the unique commuting needs of university students, Vroomi provides a cost-effective, safe, and eco-conscious alternative to solo driving or expensive ride-hailing apps. Long-term, Vroomi’s network-based model and scalable infrastructure make it well-positioned to expand into inter-campus travel, university partnerships, and broader smart-mobility applications. How we built it 🛠️ Vroomi was built using a modern full-stack web development stack tailored for speed, scalability, and geolocation accuracy. The front-end is developed in React with Tailwind CSS for a responsive and intuitive UI. We used Leaflet.js with OpenStreetMap for real-time map rendering and location services, replacing expensive APIs while maintaining performance and cutting costs. On the back-end, we leveraged Supabase for authentication, data storage, and real-time syncing of ride and user data. Our intelligent route-matching algorithm, written in TypeScript, calculates optimal multi-passenger paths using variations of the Traveling Salesman Problem (TSP) combined with geo-distance heuristics. To handle payments, we integrated Stripe at the back-end to enable secure ride transactions. Our custom cost-splitting engine dynamically calculates fair gas-sharing based on distance and vehicle type, with a small enough platform fee applied while ensuring that it wouldn’t detract any customers away from using our services. For authentication and community trust, we implemented Clerk to ensure only students with verified university emails can access the platform. Later we plan on expanding to the corporate world for better, faster and safer commutes. We deployed the entire application on Vercel for fast and reliable hosting, and registered a custom domain through GoDaddy, giving Vroomi a professional and accessible online presence. Challenges we ran into 💥 Dynamic Route Optimization: Building an efficient, scalable routing system that supports multiple passengers with different locations was more complex than anticipated. Balancing performance and accuracy required us to explore multiple algorithmic approaches before settling on a hybrid permutation-based model. Geocoding Limitations: We initially ran into usage limits and licensing constraints with major map APIs. Switching to OpenStreetMap required rebuilding components for marker rendering and coordinate accuracy from scratch. State Management: Coordinating live ride data, user profiles, and real-time feedback posed challenges in ensuring UI consistency across sessions. Safety Assurance Logic: Designing a lightweight but trustworthy safety protocol—especially with verification, driver ratings, and user reporting—was challenging to balance with ease of onboarding. Another funny but yet challenging task was finding the missing “_’ in our Environment variables file for 45 mins straight which would not let the server side connect with the client side as it was not allowing any API responses to transmit further. Accomplishments that we’re proud of 🎉 Built a full prototype of Vroomi that successfully simulates multi-passenger ride-sharing for 4+ users with real-time routing and cost-splitting. Integrated secure authentication using university emails to foster trust and safety in a campus-specific environment. Implemented custom route matching that considers both efficiency and fairness, a feature that distinguishes Vroomi from traditional ride-hailing tools. Kept everything open-source and map-based, using Leaflet and OpenStreetMap to reduce costs and increase control. Tested modular algorithms for route planning, allowing flexibility to plug in advanced optimization models like k-opt or A* in future versions. What we learned 🧠 Building Vroomi gave us firsthand insight into the unique mobility challenges students face—particularly the tradeoffs between affordability, trust, and convenience. We learned that safety and verification are non-negotiable for users, and that successful adoption depends on simplicity and transparency in both design and pricing. Technical challenges around multi-passenger routing and payment splitting reinforced the importance of modular, testable architecture. Most importantly, we realized that peer-to-peer systems thrive when community trust is built into the core. What’s next ⏭️ Our next step is to launch a pilot across two commuter-heavy campuses, refine our matching and routing algorithms in a live environment, and collect usage feedback to validate the user experience. From there, we plan to scale to 5+ universities, introduce a premium ride-prioritization feature, and explore institutional partnerships for broader rollout. We’ll continue strengthening safety protocols and begin preparing for formal seed-stage fundraising by the end of Year 1. <div