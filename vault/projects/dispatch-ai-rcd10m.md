---
slug: "dispatch-ai-rcd10m"
url: "https://devpost.com/software/dispatch-ai-rcd10m"
title: "Dispatch AI"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 574
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Dispatch AI

> Dispatch AI powers precise, real-time delivery routing with AI and Google Maps—turning every address into a smart, adaptive promise kept.

[Devpost](https://devpost.com/software/dispatch-ai-rcd10m) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[retail_commerce]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** google-directions, google-maps, langgraph, next.js, node.js, postgresql, python, react-native, redis, typescript, websockets

## How they structured the write-up

- dispatchai

## Body

Dispatch Console Create route screen Dispatch Console Route screen Dispatch Console Live route screen Dispatch Console scheduled route screen Dispatch AI (warehouse manager conversation) Dispatch AI (driver conversation) Dispatch AI (driver conversation 2) Dispatch AI (customer conversation 2) Dispatch AI (customer conversation) Dispatch App Login screen Dispatch App delivery screen Dispatch App Journey/order details screen Dispatch App driver route in google maps DispatchAI DispatchAI bridges the gap between human unpredictability and logistical precision—powered by AI and Maps. Inspiration In delivery logistics, drivers constantly face unpredictable real-world challenges—traffic delays, customer unavailability, mechanical issues. These disruptions often require back-and-forth communication with dispatch teams, delaying operations and overwhelming human managers. Meanwhile, customers frequently want to update their delivery preferences, but legacy systems make such changes cumbersome. We were inspired to build an AI assistant that understands delivery-related problems in natural language, classifies them intelligently, and seamlessly triggers backend workflows. Our goal was to create a frictionless bridge between drivers, customers, and warehouse teams—empowering each group to resolve issues quickly and intelligently. What It Does DispatchAI is an AI-powered assistant that streamlines last-mile delivery operations by integrating natural language interfaces with smart backend automation. It: Understands and classifies driver, customer, and manager inputs using LangGraph-powered stateful LLM agents Triggers backend API workflows based on prompts (e.g., "Stuck in traffic", "Change my delivery address") Supports drivers via mobile (DispatchGO), managers via a dashboard (Dispatch Console), and all roles via an AI chatbot Uses Google Maps APIs for live route tracking, reoptimization, and delivery visibility Maintains conversation context throughout user sessions, securely isolated per role Allows manual and AI-suggested route creation, with driver assignment and real-time status monitoring How We Built It Frontend: React + Tailwind for responsive UIs (web dashboard, mobile app) Chatbot interface embedded across all platforms Backend: FastAPI for secure API routing Firebase for real-time notifications Google Maps Platform for geocoding, map rendering, and route optimization (Directions API, Routes API, Maps JS) AI Layer: LangGraph for orchestrating multi-role, memory-aware agent workflows Groq LLaMA3 and Claude for prompt understanding and tool invocation Role-specific tool routing based on JWT-authenticated sessions Challenges We Ran Into Translating free-form natural language into accurate, structured backend actions Keeping delivery routes in sync across stakeholders when reoptimizations occurred Managing AI tool routing securely while maintaining session-level memory without persisting post logout Handling reoptimization latency and UI feedback during fluctuating network states Accomplishments That We're Proud Of Built a fully working AI assistant that classifies logistics-related issues and invokes real-time backend actions Seamlessly integrated Google Maps APIs for accurate live routing and ETA tracking Enabled secure, session-aware interactions across three distinct roles with tailored tools Delivered a demo-ready platform with pre-populated, realistic delivery data and end-to-end UX What We Learned LangGraph is a powerful orchestration framework for modular, multi-role AI agents Even simple language prompts like "Customer not home" can hide complex backend workflows—AI makes these accessible Mapping APIs become truly impactful when paired with AI agents who understand when and how to use them Role-based memory and secure context awareness significantly enhance the reliability and trust of conversational systems What's Next for DispatchAI Live route modification: Enable drivers or managers to re-route deliveries mid-route with map updates Voice input for drivers: Hands-free reporting of issues via mobile Analytics dashboard: Delivery success rates, reoptimization frequency, and AI performance metrics External API integrations: Connect DispatchAI with ecommerce or ERP systems for end-to-end automation Advanced scheduling engine: Consider time windows, driver preferences, and warehouse hours dynamically <div