---
slug: "flowagent"
url: "https://devpost.com/software/flowagent"
title: "FlowAgent"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 541
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# FlowAgent

> Flow Agent uses AI, IoT, and simple SMS to turn any rural water point into an autonomous, transparent, and cashless utility that works even without internet.

[Devpost](https://devpost.com/software/flowagent) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[finance_payments]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** arduino, c++, esp32, node.js, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flowagent

## Body

Inspiration Access to clean water is still a major challenge across many African communities, where most people only have basic phones and limited or unreliable internet. We wanted to prove that advanced AI can deliver real impact in these environments — not by replacing what exists, but by augmenting it with an intelligent, autonomous layer. The inspiration behind FlowAgent is simple: use AI + SMS + IoT to make clean water available anywhere, even where technology is scarce. What it does FlowAgent allows anyone to buy clean water using a simple SMS, no apps or internet needed. When the user pays, FlowAgent uses a Nullshot AI Agent to verify the transaction on-chain and securely trigger a real IoT water pump via an ESP32 T-Call. Everything is logged, monitored, and visualized in a Nullshot-powered web dashboard. FlowAgent transforms any water kiosk into: an autonomous AI-operated utility, transparent and tamper-proof, cashless, reliable even with 2G coverage, and accessible to all, including communities without smartphones. How we built it We built FlowAgent by combining Nullshot, Web3, and IoT hardware: Nullshot AI Agent Responsible for reasoning, validation, and decision-making Triggers hardware actions via MCP tools Interfaces with blockchain for payment confirmation Custom MCP Tool Communicates directly with the ESP32 (LilyGO T-Call SIM800L) Sends ultra-light (1–5 byte) commands Handles pump activation and status reporting Python Listener Receives SMS payment confirmations Forwards data to the Nullshot Agent Logs events and handles fallback logic ESP32 Water Controller Activates pump based on commands Tracks volume, timing, and errors Sends back telemetry Nullshot Web App Dashboard for operators Real-time logs, pump states, payment records Manual override + sensor visibility Blockchain Layer (Base L2 / or any EVM) Payment verification Tamper-proof transaction logs Everything works together to build an AI-native autonomous water system. Challenges we ran into Designing a reliable pipeline with zero internet for the end user Making SMS payments compatible with real-time blockchain verification Building an MCP tool that can communicate with hardware in extremely lightweight packets Ensuring pump activation is safe, repeatable, and tamper-resistant Syncing hardware state with Nullshot’s web dashboard Optimizing the AI agent to make deterministic decisions in a low-connectivity context Accomplishments that we're proud of Built a fully autonomous water-control system powered by Nullshot AI Demonstrated real hardware control using MCP tools Created a fully functional low-connectivity payment → AI → IoT → pump pipeline Achieved end-to-end verification from a simple SMS all the way to a real water pump Developed a clean, instantly deployable web dashboard powered by Nullshot Proved that AI can operate in environments with 2G-only connectivity What we learned How to integrate traditional telecom (SMS) with modern Web3 systems How powerful Nullshot is for creating AI-native autonomous agents How to architect reliable IoT systems under extreme constraints The importance of deterministic AI reasoning in real-world infrastructures That simplicity (SMS + AI + IoT) can actually produce the most robust solutions What's next for FlowAgent Deploy pilot units in Burundi and East Africa Add prepaid NFC card support for offline villages Integrate solar-powered sensors for water-level monitoring Expand the dashboard with predictive analytics for maintenance Add community-level DAO governance for pricing and transparency Partner with NGOs, water operators, and humanitarian organizations Scale FlowAgent to support agriculture, irrigation, and remote utility management <div