---
slug: "bloodlink-vxj8rb"
url: "https://devpost.com/software/bloodlink-vxj8rb"
title: "BloodLink"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 615
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/structured_db"
---

# BloodLink

> A hospital blood management system that tracks inventory, predicts expiry, reduces blood wastage, and enables secure inter‑hospital sharing to save lives and improve emergency response.

[Devpost](https://devpost.com/software/bloodlink-vxj8rb) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[finance_payments]] [[health_clinical]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[structured_db]]

**stack** framer-motion, node.js, postgresql, radix-ui, react, recharts, supabase, tailwind-css, typescript, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bloodlink

## Body

Inspiration In a world where medical innovation is advancing rapidly, blood distribution inefficiency remains a silent crisis. One hospital may discard expired blood units while another nearby faces a life-threatening shortage of the same type. The issue isn’t just supply it’s fragmentation. Hospitals operate in silos without shared visibility into inventory levels. In emergencies, that delay can cost lives. We asked ourselves: What if blood management operated like a connected network instead of isolated systems? That question became BloodLink. What it does BloodLink is a conceptual hospital blood bank management platform designed to eliminate waste, reduce shortages, and modernize emergency coordination. Real-Time Inventory Simulation Tracks blood units across types and statuses (Safe, Warning, Critical, Expired) with live-updating dashboards. Inter-Hospital Sharing Workflow Simulates secure blood requests and transfers between hospitals, preventing localized shortages. Smart Alerts Visual indicators notify staff about expiring units, low stock levels, and pending transfers. Patient & Transfusion Tracking Logs transfusion records and patient blood usage within a structured system. Role-Based Interface Different dashboards simulate hospital administrators, technicians, and system-level views. Offline-First MVP Built to function without a backend, using local state and browser storage to simulate persistence. BloodLink transforms blood inventory from a static spreadsheet problem into an interactive, networked experience. How we built it BloodLink was built as a high-performance frontend MVP to demonstrate how a modern blood coordination platform could function in real hospital environments. Core Architecture Built with React 18 and Vite using a modular component-based structure. TypeScript enforces strict typing across core models such as BloodUnit, TransferRequest, and Patient. State Management & Persistence Instead of a backend database, the app uses structured mock datasets and localStorage-based persistence to simulate real-time inventory updates and state transitions. Workflow Engineering Implemented controlled state transitions for blood units: Available → Requested → In Transit → Used This models real-world logistics while preventing invalid state changes. Data Visualization Recharts powers responsive dashboards that reactively update as inventory changes. Design System Tailwind CSS and Radix UI primitives provide accessible, clean UI components, with Framer Motion for smooth animations. Deployment Deployed on Vercel for fast global access. Challenges we ran into I did not have access to a real hospital environment to test BloodLink in live conditions. Because of this limitation, I had to simulate realistic hospital workflows using structured mock data and controlled state logic. While this meant I couldn’t validate the system with actual medical staff, it pushed me to carefully design the architecture to reflect real-world blood bank operations as accurately as possible. Simulating a Multi-Hospital System Without a Backend Designing realistic inter-hospital logic without an actual database required careful structuring of mock data and state synchronization. Preventing Invalid State Transitions Ensuring blood units couldn’t skip lifecycle stages required precise frontend logic. Designing for Real-World Complexity Healthcare systems are highly structured. Modeling that complexity within a frontend-only MVP required thoughtful architecture. Accomplishments that we're proud of Built a fully interactive multi-hospital blood sharing simulation without backend infrastructure. Engineered a realistic transfer lifecycle workflow. Designed dashboards that clearly communicate supply trends and shortages. Created a scalable architecture ready for backend integration. What we learned Built a fully interactive multi-hospital blood sharing simulation without backend infrastructure. Engineered a realistic transfer lifecycle workflow. Designed dashboards that clearly communicate supply trends and shortages. Created a scalable architecture ready for backend integration. What's next for BloodLink Backend Integration Connect to a real backend (e.g., Supabase + PostgreSQL) to enable real multi-hospital collaboration. IoT Cold-Chain Monitoring Integrate smart temperature sensors in blood storage refrigerators to monitor real-time temperature and ensure compliance. Mobile Scanning App Build a mobile companion app for barcode/QR scanning of blood bags. Predictive Analytics Use historical usage data to forecast shortages before they occur. <div