---
slug: "medunity"
url: "https://devpost.com/software/medunity"
title: "medunity"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 952
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# medunity

> Longitudinal healthcare platform to empower and inform Canadians personally and systemically.

[Devpost](https://devpost.com/software/medunity) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[runtime_tool_creation]] [[simulation_digital_twin]]
**domain** [[accessibility]] [[civic_government]] [[education]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[educator_student]] [[patient_family]]
  <sub>weak: social_worker</sub>
**substrate** [[code_repository]] [[geospatial]]

**stack** fastapi, gemini-2.5-flash, google-cloud, google-cloud-vertex-ai, mapbox, next.js, overpass-api, python, railtracks, react, supabase, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how it was built
- challenges ran into
- what was learned

## Body

Landing page (1) Landing page (2) Landing page (3) Health Dashboard (Patient Triages) Agent Pipeline Visualization (Patient Triage) Facility Matching (Patient Triage specific) Triage/Intake form Provider Dashboard Simulation (1) Provider Dashboard Simulation (2) All Locations (Patient's view) Community resources reporting Hospital/clinic reporting Inspiration Like many university students and young people, I move around all the time - always changing my walk-in clinic, my pharmacy, my context. Often when something feels off, options are Google, a very tempting general-use chatbot that misleads, an 8-hour ER wait only to miss more suitable resources nearby, or even worse - to ignore something that actually needs attention. And that's with having a family doctor - around 6 million Canadians don't. Most hospitals in Canada are also over 100% capacity, with frontline workers overworked, and overcrowding mismanaged. In 2024, roughly 500,000 Canadians left ERs before seeing a doctor. MedUnity exists to empower not only individuals in making the best decisions with their health data, but allowing every user action to inform and benefit the community at large. It's built on 3 areas: acuity, continuity, and community. What it does MedUnity is a longitudinal health platform that creates a shared layer of medical intelligence across multiple audiences: For patients: an AI-powered preliminary triage system. Describe symptoms in plain language Answer a dynamically generated short triage form Receive a structured clinical assessment with a CTAS score and recommendations, all based on CTAS 2025 (the Canadian Triage and Acuity Scale, the same framework used in every Canadian ER) Entries build a 30-day health timeline, where the agent detects patterns and links related entries When you're ready to seek care, routes you to the right facility that matches your condition and optimizes your time Send your triage report and ETA ahead so the facility knows you're coming For healthcare providers: real-time demand projections. Incoming patient signals along with their CTAS score and reports appear on the map, with ETA and location updated live The system detects clusters ("4 respiratory patients inthe last hour, consider isolation protocol"), projects capacity ("full in 45 minutes at current rate"), suggests ward assignments, generates prep checklists, and recommends diversions to less-loaded facilities. Simulate different scenarios to stress-test readiness. For communities: Features under each facility to communicate live updates, wait times, strain and resource shortage. e.g. health centres with live resource inventories, where staff can report shortages (naloxone kits running low, menstrual products out of stock) and the community can see what's available where. Hospital staff can report alerts and capacities to advocate for government attention and funding under this network of shared health visibility. How it was built Gemini & Vertex AI - CTAS Fine-Tuning: Using 1,000 synthetic training examples covering all five CTAS levels, 80% written in casual language, I fine-tuned Gemini 2.5 Flash on Vertex AI and achieved 77% validation accuracy on a 5-class task where most errors are clinically reasonable off-by-one boundary decisions (CTAS 3 vs 2). The model outputs structured assessments: CTAS level, CEDIS complaint, modifiers applied, and clinical rationale – parsed into a structured triage report that both the patient and provider can access. About CTAS 2025: has 169 CEDIS complaint categories, Primary Modifiers (airway, breathing, circulation, disability, pain, mechanism of injury, frailty), Complaint-Specific Modifiers, and a 2025 update that reclassified sexual assault into trauma, added frailty as a universal modifier, and introduced new modifiers for diplopia, sensory loss, and pruritus. Agentic Framework - Railtracks: The provider side dashboard uses Railtracks to power ER demand intelligence. Five deterministic tool nodes run the analytics – ward routing, prep checklists, cluster detection, capacity projection, diversion recommendations, while a Railtracks agent with Gemini 2.5 Flash synthesizes them into actionable summaries for charge nurses. The tools are fast and deterministic (no LLM latency for critical decisions); the agent adds the narrative layer on top for more accessible insights. Features: Triage : Gemini extracts symptoms and generates triage questions → user answers → fine-tuned CTAS model classifies → Gemini generates the structured report. Facility discovery : Overpass API (OpenStreetMap) for real-time hospital/clinic queries, merged with sample data for community health centres that carry resource inventories. Simulation engine : Four demand scenarios (normal day, flu season, mass casualty, heat wave) with curated Toronto patient profiles, realistic ETAs, deterministic routing table for wards suggestions, time-acceleration controls. Challenges ran into CTAS boundary ambiguity was the hardest problem. Solution was to craft training examples where the rationale section explicitly reasons about why a level was chosen, teaching the model to weigh modifiers rather than keyword-match symptoms. Facility matching noise: querying for nearby facilities returns every eye clinic, chiropractor, and vet office. We built a multi-layer filter: specialist keyword exclusion, AI-recommended facility types from the triage report, with exclusion keywords. What was learned The biggest lesson was that the value isn't limited in the triage for an individual when the problem is systemic. A CTAS level by itself is just a number. But when that number routes you to the right facility, generates a prep checklist for the receiving nurse, feeds into a cluster detection algorithm that triggers an isolation protocol, and shows up on a community resource dashboard – that's when a single patient interaction benefits others in the community I learned that simulation wasn't just a demo feature. Running a mass casualty scenario and watching 10 patients converge on Toronto General, triggering cluster alerts and diversion recommendations, revealed bottlenecks in the demand analysis pipeline that I wouldn't have found testing one signal at a time. Sources: Hall JN, McCarron J, Toarta C, McLeod SL; CTAS National Advisory Committee and NENA Triage Committee. Canadian Emergency Department Triage and Acuity Scale (CTAS) Guidelines 2025. CJEM. 2025 Oct;27(10):774-777. doi: 10.1007/s43678-025-00996-1. Epub 2025 Sep 12. PMID: 40938532. ( https://link.springer.com/article/10.1007/s43678-025-00996-1 ) https://www.cbc.ca/news/marketplace/hospital-wait-times-9.6983849 https://www.cbc.ca/news/health/primary-care-ourcare-family-doctors-9.7007471 <div