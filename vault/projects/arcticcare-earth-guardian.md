---
slug: "arcticcare-earth-guardian"
url: "https://devpost.com/software/arcticcare-earth-guardian"
title: "ArcticCare - Earth Guardian"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 466
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/general_public"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ArcticCare - Earth Guardian

> Every report counts. Every action protects and cares.

[Devpost](https://devpost.com/software/arcticcare-earth-guardian) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[civic_government]] [[climate_energy]] [[disaster_emergency]] [[security_privacy]] [[transportation]]
**user** [[general_public]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** contexts, custom, databases:, hooks, javascript-frameworks:-next.js, languages:-typescript, next.js-api-routes-other:-tailwind-css, node.js-(express)-platforms:-node.js-(desenvolvimento), orm, postcss, prisma, prisma-(orm), procfile-(gerenciamento-de-processos), railway-(deploy/hosting)-cloud-services:-railway-databases:-prisma-orm-(provavelmente-com-postgresql-ou-outro-banco-sql)-apis:-rest-(endpoints)

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for arcticcare – earth guardian
- instructions for testing

## Body

ArcticCare – Earth Guardian Inspiration ArcticCare was born from the urgent need to protect vulnerable ecosystems in a world increasingly affected by climate change. Environmental damage often goes unnoticed or is reported too late. We wanted to transform citizens, researchers, and institutions into active guardians of the planet through real-time, shared intelligence. What it does ArcticCare is a collaborative environmental monitoring platform that combines live data, citizen reports, and AI-driven analysis to detect risks early and coordinate action. Users can: Visualize climate indicators in real time Report incidents from the field Validate community alerts Track resolution progress Receive intelligent prioritization of threats To turn raw data into decision-ready information, the platform computes indicators such as: Temperature anomaly: $$A = T_{\text{current}} - T_{\text{baseline}}$$ Ice loss rate: $$R = \frac{\Delta V}{\Delta t}$$ Community engagement index: $$S = \frac{\text{reports} + \text{actions} + \text{validations}}{3}$$ This allows ArcticCare to highlight where attention is needed now. How I built it ArcticCare was developed with a modern, scalable architecture: Frontend: Built with Next.js, React, and Tailwind CSS. Design System: Evolved to a professional, high-contrast aesthetic — removing emojis and using Lucide icons and neutral tones (gray, graphite, white) for a clean, corporate environment. API Bridge: A robust integration layer in api.ts that connects the UI to real backend services and AI models for risk analysis and decision-making. Authentication: Feature-complete flow (Login / Signup / Logout) integrated with a centralized AuthProvider and JWT persistence via arctic_care_token . Challenges I ran into Presenting complex environmental data without overwhelming users. Maintaining clarity across multiple analytical dashboards. Implementing real-time synchronization between report submissions and map updates. Creating trustworthy and explainable AI suggestions. Standardizing the design system to be professional and scalable. Accomplishments that I'm proud of Delivering a clean and intuitive dashboard experience, removing visual clutter. Turning community participation into measurable intelligence. Making AI outputs understandable and actionable for immediate environmental response. Building a modular architecture ready for real-world adoption. What I learned Simplicity is critical: Removing flashy colors and emojis actually increased clarity and trust in the data. Rapid prototyping: Using a centralized API bridge allowed for faster integration of backend logic. Accessibility: A consistent design language is the first step toward a global community of users. What's next for ArcticCare – Earth Guardian We aim to evolve ArcticCare from monitoring to prediction and prevention . Future models may include: Environmental risk probability: $$P(E) = \frac{\text{critical alerts}}{\text{total observations}}$$ Weighted impact estimation: $$I = \sum w_i \cdot x_i$$ Next steps: Expand predictive AI capabilities for disaster forecasting. Introduce deeper gamification mechanics (Impact Trees and CO₂ counters). Integrate satellite and governmental data feeds. Grow an international network of Earth Guardians. Instructions for Testing When testing the platform, please use the search bar and side menus as the primary navigation tools to explore the integrated routes and features. <div