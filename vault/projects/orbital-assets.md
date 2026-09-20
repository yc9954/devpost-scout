---
slug: "orbital-assets"
url: "https://devpost.com/software/orbital-assets"
title: "Orbital Assets"
hackathon: "Gemini 3 Hackathon"
organization: "Google"
winner: true
words: 910
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Orbital Assets

> The first Investment Bank for the solar system. Orbital Assets, powered by Gemini 3 Reasoning, turns raw NASA asteroid data into rigorous, physics-based financial valuations.

[Devpost](https://devpost.com/software/orbital-assets) · hackathon [[Gemini 3 Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
  <sub>weak: retrieval_grounding</sub>
**domain** [[developer_tools]] [[finance_payments]]
**user** [[researcher]]
**substrate** [[structured_db]] [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** firebase, gemini, google-ai-studio, next.js, resend, three.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orbital assets

## Body

System Architecture: A robust pipeline mapping NASA data through Cloudflare Edge and the Gemini 3 Reasoning Core to a real-time UI. Landing Page: The Investment Bank for the Solar System: Bridging the gap between raw astrodynamics and professional orbital asset classes. The Logic Engines: Four interlinked systems transforming complex NASA ephemeris data into high-fidelity investment intelligence in realtime Mission Trade-Space: Optimizing mission profiles by balancing hardware complexity against fuel costs for maximum orbital efficiency. Gemini 3 Flash Thinking analyzes the "Space Resource Valuation Framework" to verify physics and economics with zero hallucinations. A professional, AI-generated appraisal summarizing composition, accessibility, and NPV for institutional-grade decision making. Astrophysical Logic: Deterministic rules using spectral classification to drive material valuation and establish planetary ground truth. Astrodynamic Logic: Fueling feasibility with the Tsiolkovsky Rocket Equation to categorize targets into strict accessibility tiers. Email Export Dialog: Seamlessly transition from web analysis to institutional record-keeping with our one-click. Receive a high-fidelity, framework-grounded investment report directly in your inbox. Inspiration The commercialization of space is no longer science fiction; there are companies like AstroForge and TransAstra are targeting Near-Earth Objects (NEOs) for mining, unlocking trillions in resources. Yet most public valuations quote opportunities of quadrillion dollars, ignoring physics, economics, and market reality, leading to hype without substance. Inspired by this gap, we built Orbital Assets : the first AI-powered Investment Bank for the Solar System. We wanted to create a realistic, transparent tool that turns raw NASA asteroid data into investor-grade memorandums, including Net Present Value, Risk assessment, and grounded reasoning. Gemini 3's advanced reasoning made this idea possible: It thinks step-by-step like an analyst, avoids hallucinations through our deterministic guardrails, and streams thoughts in real-time for an engaging thinking experience. What it does OrbitalAssets is an AI-powered Investment Memorandum generator for NEOs. Users paste a NASA Eyes URL (e.g., for asteroid Psyche) and the App: Fetches orbital/physical data from NASA's Small-Body DataBase (SBDB) API Applies deterministic valuation logic (delta-v, composition inference, market damping) Feeds everything to Gemini 3 for deep analysis Streams the reasoning process and generates a full Investment Memorandum with Net Present Value (NPV), risks, and strategic insights (Earth-return vs in-space utilization) The valuation number comes from pure math functions to prevent AI invention, while Gemini 3 handles narrative and qualitative reasoning. How we built it We architected OrbitalAssets using a "Separation of Concerns" between deterministic physics and generative reasoning: The Engine: We built a custom Deterministic Valuation Library in TypeScript. This library implements the mathematical core of the project: Net Present Value calculations using space-specific discount rates of 20% to 35% to account for the unique technology and regulatory risks of deep-space ventures. It also utilizes the Shoemaker-Helin Delta-v approximation to determine orbital accessibility and a Market Damping Factor to prevent unrealistic valuations by automatically adjusting commodity prices based on global annual production thresholds. The Frontend: Developed with Next.js (App Router) and Tailwind CSS . We integrated React Three Fiber and Three.js to render interactive 3D shape models sourced from official NASA resources to give investors a tangible look at their potential assets. The Intelligence: We used Gemini 3 (gemini-3-pro-preview) to act as the "Senior Analyst." While our code handles the hard math to prevent hallucinations, Gemini 3 performs qualitative risk assessments. It analyzes spectral classifications—specifically the M, S, and C-complex groups—to determine mining priority and strategic approaches based on established mineralogical analogues. The Infrastructure: The app runs on the Edge Runtime for global low-latency performance. We utilized Firebase (Firestore) for lead capture and logging, and the Resend API to deliver the final Investment Memorandum directly to users' inboxes. Challenges we ran into Data Entropy: The NASA JPL SBDB API is powerful but often has missing values. We implemented a heuristic layer to infer diameter from Absolute Magnitude and Albedo when explicit data was unavailable. The Rocket Equation Penalty: Balancing mission cost vs. potential revenue was a major hurdle. We learned that small increases in Delta-v (velocity change) require exponential increases in fuel mass, making targets with high velocity requirements generally "uninvestable" for commercial models. Environment Parity: Debugging 3D WebGL components and complex AI streaming within a browser-based environment required careful management of dependencies and local-to-cloud synchronization. Accomplishments that we're proud of Bridging the Gap: Successfully turning theoretical orbital mechanics into an investable "Asset Class" framework. Deterministic AI: Creating a system where the AI provides the narrative but cannot hallucinate the valuation—the math is locked in TypeScript constants derived from our technical logic tables. Interactive Visualization: Successfully loading and rendering official NASA shape models for famous asteroids like Eros and Bennu in a web-native environment. What we learned The Two Markets: We realized the real "Space Gold" isn't just platinum—it's water. C-type asteroids are strategic assets because water mined in space has a "replacement value" equal to the cost of launching it from Earth, estimated at US$1,500 to US$2,500 per kilogram. Supply & Demand Damping: We learned the importance of "Market Damping." Bringing back 100% of the global annual production of a resource doesn't make a venture rich; it crashes the commodity's price to approximately 1% of its spot value. What's next for Orbital Assets Live "Launch Windows": Transitioning from static accessibility approximations to dynamic mission planning that identifies exactly when the next optimal launch window opens. Gesture-Controlled Dashboards: Implementing gesture controls so users can rotate asteroids and "drill" for resources with hand movements. Tokenization: Exploring the fractionalization of asteroid mining claims to allow smaller investors to participate in the emerging space economy. <div