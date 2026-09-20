---
slug: "toyotron"
url: "https://devpost.com/software/toyotron"
title: "Toyotron"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 572
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Toyotron

> Toyotron is a solution that allows users to easily find their dream Toyota through agentic AI powered by NVIDIA's intelligent open source foundational model, Nemotron.

[Devpost](https://devpost.com/software/toyotron) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[finance_payments]] [[retail_commerce]] [[supply_logistics]] [[transportation]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** ai, css, nemotron, next.js, openrouter, resend, retell, supabase, tailwind, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for toyotron

## Body

Home page Recommendations based on user preferences Trade in analysis Emailing confirmation of appointment Emailing recommendation to user Talk to the Ai via phone # call System Diagram Inspiration We drew inspiration from last year’s HackUTD winner “talktauhbank,” which showed how natural AI conversations can unlock new user experiences. That sparked the idea of a phone-call-style agent for car shopping. The name comes from combining Toyo (from Toyota) and tron (from Nemotron), as a nod to the two sponsor tracks we built this project for hence, Toyotron! From there, we focused on a simple question: what keeps people from buying a car? We kept coming back to lack of confidence too little time, not enough knowledge, and no easy way to take the first step. That led us to combine Nemotron’s reasoning with a suite of productivity tools. The result is a personal automotive concierge that can onboard shoppers, answer questions, send promotional follow-ups, and schedule test drives like a proactive sales assistant. What it does Toyotron is an AI-powered auto-buying assistant. It conducts an onboarding survey to understand a shopper’s budget, lifestyle, and preferences, then recommends vehicles that truly fit. It can hop on a phone-style interaction, answer detailed questions about each option, trigger follow-up tasks like booking appointments or emailing quotes, and keep the conversation moving until the shopper is ready to visit a dealership. How we built it We orchestrated agents using Nemotron as the reasoning core, wrapped in a Next.js frontend that delivers both chat and simulated phone-call experiences. The backend exposes API routes for agent orchestration, connects to external tooling for scheduling and messaging, and captures all interactions in a shared session. We used prompt engineering for consistent assistant tone, and a modular tool layer so the agent can invoke capabilities like email, google calendar, trade in estimation and without leaving the conversation. Challenges we ran into Stitching multimodal interactions chat, call, and onboarding forms into a single coherent flow without losing context. Prompt balancing to keep Nemotron both helpful and safe while still making confident recommendations. Integrating third-party services (email, scheduling APIs) in a way that remained reliable during rapid prototyping sprint cycles. Handling edge cases where users changed preferences midstream and ensuring our agent gracefully recovered. Accomplishments that we're proud of Delivering an end-to-end experience that feels like a dedicated sales assistant rather than a static chatbot. Achieving high-quality car recommendations by aligning onboarding data, vehicle metadata, and agent reasoning. Building a modular tool framework so new capabilities—finance pre-qualification, insurance quotes—can be added quickly. Shipping a polished demo in a hackathon timeline while still writing maintainable code and clean documentation. What we learned Users respond better when the assistant takes initiative suggesting next steps, confirming times, or offering test-drive slots rather than waiting for instructions. Combining voice-like interactions with text-based confirmations helps bridge comfort levels across different users. Careful prompt design is as important as the model itself when you want consistent behaviors in a complex workflow. Rapid iteration with tight feedback loops (pairing with teammates, testing with mock users) is crucial for conversational UX. What's next for Toyotron Expand the toolset: integrate financing calculators, insurance comparisons, and dealership inventory feeds. Launch a real phone-call interface using Twilio so shoppers can talk to Toyotron hands-free. Personalize outbound campaigns that follow up with tailored offers based on conversation history. Partner with dealerships to sync CRM data and close the loop from conversation to signed paperwork. <div