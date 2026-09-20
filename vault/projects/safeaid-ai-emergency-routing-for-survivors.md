---
slug: "safeaid-ai-emergency-routing-for-survivors"
url: "https://devpost.com/software/safeaid-ai-emergency-routing-for-survivors"
title: "SafeAid - AI Emergency Routing for Survivors"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 1171
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/education"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# SafeAid - AI Emergency Routing for Survivors

> AI-powered platform that routes trafficking survivors and vulnerable people to the nearest shelter, NGO, or emergency contact via SMS or the Web app (no smartphone needed).

[Devpost](https://devpost.com/software/safeaid-ai-emergency-routing-for-survivors) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[realtime_stream]] [[structural_withholding]]
**domain** [[education]] [[housing_homeless]] [[labor_employment]] [[legal_justice]] [[security_privacy]]
**user** [[patient_family]] [[social_worker]]
**substrate** [[geospatial]] [[structured_db]]

**stack** express.js, google-gemini, next.js, node.js, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next
- built with

## Body

Safeaid Dashboard Safeaid Dashboard Inspiration In December 2024, Nigeria's National Bureau of Statistics released a report that stopped us cold. Between May 2023 and April 2024, over 2.2 million Nigerians were kidnapped . In a single year. That same period saw 614,937 people killed and ₦2.23 trillion paid in ransom to abductors. In November 2025, gunmen abducted 10 women and children from a farming village in Kwara State. More than 300 children were seized from a Catholic school in Niger State — over 265 remain missing. These are not distant statistics. They are people. And the terrifying reality is that when someone is in danger in Nigeria — held against their will, trafficked, exploited — the traditional response is to call for help. But what if you cannot call? What if your phone is confiscated? What if speaking out loud means your abuser will hear you? What if you simply do not know who to call? Nigeria ranks first among nationalities of trafficking victims identified in the European Union . NAPTIP has rescued over 25,000 victims since its founding — yet for every person rescued, countless others never find a way to reach help at all. We built SafeAid because no cry for help should go unheard because of fear, lack of internet, or the inability to speak. What It Does SafeAid is an AI-powered emergency routing platform built for vulnerable people in Nigeria — trafficking survivors, abuse victims, people in danger — who need to reach help quickly, discreetly, and safely. For survivors on basic phones (no smartphone, no internet needed): A survivor sends a silent SMS — even just the word "HELP" — to the SafeAid number. The system responds with a simple menu. The survivor replies with what kind of help they need (shelter, food, legal aid, medical, emergency) and their state. SafeAid instantly routes them to the nearest verified NGO, shelter, or NAPTIP contact — by name, address, and phone number — in a single SMS reply. For caseworkers and NGO staff: A real-time emergency dashboard shows every incoming alert, the AI-generated risk assessment, what resource was matched, and the full conversation thread. Caseworkers can monitor cases, review AI suggestions, and mark cases resolved — all from one place. The core principle: reach anyone, on any phone, anywhere in Nigeria. How We Built It Backend: Node.js, Express, TypeScript deployed on Render. We built a multi-step SMS state machine that tracks each conversation across messages — receiving the type of help needed, the survivor's state, then routing to the nearest verified center from our database of 15+ real Nigerian NGOs and shelters including Pathfinders Justice Initiative, WOTCLEF, NAPTIP zonal commands, FIDA Nigeria, LSETF, and NDE state offices. AI Layer: Google Gemini 1.5 Flash analyses every incoming message for risk level (HIGH, MEDIUM, LOW) and generates a one-sentence caseworker summary. Critically, Gemini handles insight — the routing itself is deterministic, rule-based, and fast. We deliberately separated AI reasoning from routing logic so a Gemini failure never leaves a survivor without a response. SMS Gateway: Africa's Talking — the leading SMS provider across Africa — handles all inbound and outbound messaging. Works on every basic phone with zero internet required. Database: Supabase (PostgreSQL) stores anonymous case records. Phone numbers are SHA-256 hashed before touching the database — the raw number is never stored. Frontend: Next.js 15 with TypeScript and Tailwind CSS. The emergency dashboard polls the API every 5 seconds, showing incoming alerts sorted by risk level with the recommended help center visible on every case card. Challenges We Ran Into The data problem. Nigeria does not have a centralised, structured directory of verified support organisations. We manually researched, verified, and seeded 15+ real organisations — Pathfinders in Benin City, WOTCLEF in Abuja, NAPTIP zonal commands across five states, legal aid through FIDA Nigeria, vocational programs through LSETF and NDE. Building this directory was unglamorous and essential. SMS is not stateless. A single survivor reaching SafeAid may send three or four messages: "HELP", then "1" for shelter, then "EDO" for their state. Routing requires remembering where they are in that conversation across separate webhook calls. We built a session state machine backed by Supabase to track each conversation step without ever linking it to an identity. Responsible AI under real stakes. This is not a productivity tool. The people using it are in danger. We had to draw a hard line: the AI suggests, humans decide. Every AI output is labelled. The routing itself — the most critical output — is rule-based, not AI-generated, so it cannot hallucinate a shelter address. The cold start problem. Render's free tier spins down after inactivity. A survivor cannot wait 45 seconds for a server to wake up. We implemented a cron job to keep the server warm at all times. Accomplishments That We're Proud Of A complete, working SMS flow: a message sent to our Africa's Talking number is analysed, risk-scored, routed to a real verified Nigerian organisation, and replied to — end to end — in under 3 seconds. A seeded directory of 15 real Nigerian support organisations across Edo, Lagos, FCT, Rivers, and Kano states. Zero PII in our database. Phone numbers are hashed before storage. We cannot identify a survivor even if the database were compromised. A caseworker dashboard that surfaces HIGH-risk cases at the top and shows the recommended help center on every card — so the most urgent cases are never buried. Responsible AI built into the architecture, not bolted on as an afterthought: AI labels on every generated output, human review required before action, deterministic routing so the AI cannot hallucinate a response that endangers someone. What We Learned Building for a vulnerable population forces a level of design discipline that most software never requires. Every decision carries a safety implication. The "AI suggestion" label on our dashboard is not a legal disclaimer — it is a life-safety feature. The decision to use rule-based routing instead of AI routing was not a technical limitation — it was a deliberate ethical choice. We also learned that the hardest infrastructure problem in this space is not the technology. It is the data. You cannot route someone to help that has not been verified, mapped, and maintained. The directory of organisations is as important as the AI. What's Next WhatsApp integration — 95% of Nigerian smartphone users are on WhatsApp. Adding a WhatsApp channel would reach survivors who have data access but cannot safely make calls. Multilingual SMS responses — Nigeria has over 500 languages. Yoruba, Igbo, and Hausa responses would dramatically expand reach. Pilot with Pathfinders Justice Initiative, Benin City — they already run manual case matching in Edo State, the epicenter of Nigeria's external trafficking pipeline. SafeAid is designed to reduce that manual burden. NDPA compliance audit — full alignment with Nigeria's Data Protection Act before any production deployment. Offline-first mobile app — for caseworkers in low-connectivity areas. Built With Node.js Express TypeScript Next.js 15 Tailwind CSS Supabase PostgreSQL Google Gemini 1.5 Flash Africa's Talking Render Vercel <div