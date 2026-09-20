---
slug: "edflowai"
url: "https://devpost.com/software/edflowai"
title: "EDFlow AI"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1195
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# EDFlow AI

> EDFlow AI: A Mixture of Expert AI Agents auto-coordinate ER emergencies in <30s. Each specialist agent—beds, labs, pharmacy—works in parallel to save lives.

[Devpost](https://devpost.com/software/edflowai) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
**domain** [[health_clinical]] [[supply_logistics]]
**user** [[clinician]] [[frontline_worker]] [[patient_family]]
**substrate** [[geospatial]] [[medical_record]] [[sensor_telemetry]] [[structured_db]]

**stack** claude, langchain, langgraph, python, uagent

## How they structured the write-up

- the problem that inspired us
- what it does
- how we built it
- challenges we faced
- what's next for edflow ai
- built with
- try it out

## Body

EDFlow AI: Autonomous Emergency Department Coordination The Problem That Inspired Us At 3:15 AM, a 69-year-old male arrives by ambulance with severe chest pain radiating to his left arm. His ECG shows ST elevation—a STEMI heart attack. For every minute of delay, 1.2 million cardiac cells die. In traditional emergency departments, coordinating the response requires multiple phone calls: checking ICU beds, paging cardiology, ordering STAT labs, preparing medications, alerting staff. This manual coordination takes 3-5 minutes of precious time. The bottleneck isn't medical expertise—it's coordination. What if autonomous AI agents could handle all this coordination simultaneously, reducing response time from minutes to seconds? EDFlow AI makes this reality. What It Does EDFlow AI is an autonomous multi-agent system that coordinates emergency department preparation in under 10 seconds using Fetch.ai's uAgents framework and Claude AI. Traditional Coordination (Sequential): Nurse calls lab → calls pharmacy → pages doctor → reserves bed → 180+ seconds EDFlow AI (Parallel): Seven autonomous agents work simultaneously → <10 seconds The Agent Team: ED Coordinator (Claude Sonnet 4): Receives ambulance reports, analyzes patient condition, detects protocols (STEMI/Stroke/Trauma), orchestrates all agents Resource Manager : Allocates trauma bays, assigns nursing staff, stages emergency equipment Bed Management : Reserves appropriate ICU/cardiac beds, verifies equipment functionality Lab Service : Orders protocol-specific STAT tests (troponin, CBC, coags), alerts lab technicians Pharmacy : Prepares time-critical medication kits (antiplatelet, anticoagulation protocols) Specialist Coordinator : Pages relevant specialists (cardiologist, neurologist), activates cath lab teams WhatsApp Notification : Sends real-time alerts to medical staff phones with patient details and ETA Real-World Scenario: Ambulance sends: "69yo male, severe chest pain, ST elevation on ECG, HR 110, BP 160/95, SpO2 94%, ETA 5 minutes" Within 10 seconds: Claude AI identifies STEMI protocol, urgency level 1 Trauma Bay 1 cleared and staffed Cardiac ICU Bed 3 reserved STAT troponin and cardiac panel ordered Aspirin, heparin, and nitroglycerin staged at bedside Cardiologist paged (ETA 15 min), cath lab team mobilizing WhatsApp alert sent: "🚨 STEMI ALERT - Patient arriving in 5 min, cath lab activation required" Impact: For STEMI patients, reducing door-to-balloon time by 3 minutes saves ~3.6 million cardiac cells per patient. For a hospital handling 200 STEMI cases annually, that's 720 million cells saved—translating to improved survival rates and reduced long-term cardiac damage. How We Built It Agent Framework: Built on Fetch.ai's uAgents framework for native agent-to-agent communication, deployed all 7 agents on Agentverse with Chat Protocol enabled, integrated with ASI:One for discoverability, and registered agents on Almanac Contract. Intelligence Layer: Claude Sonnet 4 powers the ED Coordinator's decision-making: Analyzes unstructured ambulance reports with medical context Accesses real-time hospital status (current capacity, staff availability, protocol performance) Determines protocol type and urgency level Generates clinical recommendations (door-to-balloon targets, resource allocation) Provides sub-5-second response times Architecture: Hub-and-spoke coordination model where ED Coordinator broadcasts emergencies to all 6 specialized agents simultaneously, each agent independently fetches data from shared JSONBin database, agents respond with detailed preparation reports, and ED Coordinator aggregates responses with 10-second timeout. Data Layer: JSONBin serves as shared hospital database storing real-time ED status (patient count, capacity, wait times), bed availability (ICU, regular, equipment status), medication inventory, specialist rosters, and protocol performance metrics. Communication: Twilio WhatsApp API integration for instant medical staff notifications with rich context (patient vitals, protocol type, ETA, required actions), delivery confirmation tracking, and protocol-specific message templates. Deployment: All agents deployed on Agentverse with unique addresses, health checks every 2 minutes, persistent agent mailboxes, and environment-based configuration (API keys, database credentials). Challenges We Faced Agent Coordination Reliability: Problem: How to ensure all 6 agents respond reliably? What if one agent fails? Solution: Implemented polling mechanism with 10-second timeout. ED Coordinator checks every 3 seconds if all responses collected. System proceeds with partial responses if timeout reached. Result: 95%+ agent response rate. Database Race Conditions: Problem: Multiple agents reading/writing simultaneously could cause conflicts (e.g., two agents reserving same bed). Solution: Used JSONBin's versioning system for optimistic locking. Critical operations (bed reservations) include version checks. Failed updates trigger automatic retry with fresh data. Real-Time WhatsApp Delivery: Problem: Twilio requires phone number verification, has rate limits, and delivery isn't guaranteed. Solution: Pre-verified all medical staff numbers, implemented exponential backoff for rate limits, added delivery status tracking, and created fallback notification queue. Claude AI Context Management: Problem: How to provide Claude with enough context without exceeding token limits? Solution: Structured prompts with hierarchical information (critical vitals first, then hospital status, then protocol history). Used Claude's 200K context window efficiently. Result: Consistent high-quality analysis. Agentverse Deployment: Problem: Managing secrets (API keys, phone numbers) across 7 agents securely. Solution: Created standardized deployment scripts, used environment variables for sensitive data, implemented secret rotation mechanism, and added deployment validation checks. Performance Optimization: Problem: Initial coordination took 15-20 seconds due to sequential database calls. Solution: Implemented async/await patterns throughout, used connection pooling for database access, parallelized agent broadcasts, and optimized Claude API calls. Result: Consistent <10-second performance. What's Next for EDFlow AI Immediate (Next 3 Months): Expand protocol coverage: Sepsis, Cardiac Arrest, Massive Transfusion, Pediatric Emergencies Add predictive analytics: 4-hour ED capacity forecasting using historical patterns Multi-language support: Spanish, Mandarin for diverse patient populations Enhanced metrics: Real-time dashboard showing protocol performance trends Medium-Term (6-12 Months): Multi-hospital coordination: Regional networks for capacity sharing and patient transfers EHR integration: Automatic patient history retrieval and documentation Advanced AI features: 100K+ token patient history analysis, drug interaction checking Mobile app: Direct ambulance crew interface for report submission Long-Term (1-2 Years): AI-human collaboration: Suggested decision support with human override Clinical validation: Multi-center trials to measure mortality impact FDA clearance: Pursue approval as clinical decision support system Global deployment: Scale to 5,000+ emergency departments worldwide Vision: Transform emergency departments into precision coordination systems where AI agents handle routine logistics, allowing medical staff to focus entirely on patient care. Every emergency department operating with Formula 1 pit crew efficiency—fast, coordinated, error-free. Built With Fetch.ai Ecosystem: uAgents Framework (v1.0.5) - Multi-agent orchestration Agentverse - Cloud deployment platform Chat Protocol - Agent-to-agent messaging ASI:One - Agent discoverability Almanac Contract - Agent registration Anthropic: Claude Sonnet 4 - Medical reasoning and protocol detection Claude API - Real-time patient analysis Infrastructure: Python 3.10+ with AsyncIO for concurrent operations HTTPx for async HTTP requests Pydantic for data validation JSONBin.io for shared hospital database Twilio WhatsApp API for staff notifications Try It Out Live Demo on ASI:One: Visit app.fetch.ai Search for "ED Coordinator Agent" Send this ambulance report: ``` 🚑 AMBULANCE REPORT Patient: 69yo male Chief Complaint: Severe chest pain radiating to left arm Vitals: HR 110, BP 160/95, SpO2 94% EMS Report: ST elevation on ECG, suspected STEMI ETA: 5 minutes 4. Watch autonomous coordination happen in real-time (<10 seconds) 5. See detailed responses from all 6 specialized agents 6. View WhatsApp notification sent to cardiologist **Live Agents on Agentverse:** @ed-coordinator-agent @bed-management-agent @pharmacy-agent @lab-service-agent @resource-manager-agent @whatsapp-notification-agent @specialist-coordinator-agent **Performance Metrics:** - STEMI Protocol: <10 seconds (Target: <10s) ✅ - Stroke Protocol: <10 seconds (Target: <10s) ✅ - Trauma Protocol: <10 seconds (Target: <10s) ✅ - Agent Response Rate: 95%+ - System Uptime: 99.2% - WhatsApp Delivery: 98%+ --- **EDFlow AI: Where autonomous agents meet emergency medicine. Coordinating care at the speed of thought.** *Built with ❤️ using Fetch.ai uAgents & Claude AI* <div