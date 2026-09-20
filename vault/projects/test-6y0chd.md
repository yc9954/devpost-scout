---
slug: "test-6y0chd"
url: "https://devpost.com/software/test-6y0chd"
title: "YardMaster"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 548
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# YardMaster

> A tech ecosystem for a non-tech world: Transforming physical logistics into a digital lifecycle

[Devpost](https://devpost.com/software/test-6y0chd) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** confluence, forge, html, javascript, jira, node.js, react, rovo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for yardmaster

## Body

slide1 slide2 slide3 slide4 slide5 slide6 slide7 slide8 slide9 slide10 slide11 slide12 slide13 slide14 mindmap YardMaster Inspiration YardMaster was inspired by the idea of building a tech ecosystem for a non-tech world . Yard and warehouse operations still rely heavily on manual paperwork, fragmented communication, and human judgment, leading to poor visibility and inefficient use of critical resources such as docks and parking areas. The goal was to digitize the physical movement of vehicles—gate entry, parking, docking, and exit—into a structured, traceable lifecycle and demonstrate that enterprise workflow tools can manage real-world logistics as effectively as they manage software development. What it does YardMaster converts physical yard operations into a real-time digital workflow : Tracks vehicles from gate-in to gate-out Provides live visibility into vehicle locations and dock availability Automatically assigns optimal parking lots or docks based on availability Digitally captures vehicle details, photos, and operational logs Manages real-world exceptions such as blocked docks or vehicle breakdowns Enables conversational querying of yard data for non-technical staff How we built it YardMaster is built entirely on the Atlassian ecosystem by modeling the physical yard as a digital board. Jira acts as the central engine. Each vehicle is created as an issue with custom fields for vehicle number, gross weight, and driver details, along with photo attachments captured at the gate. Physical movement is mapped to workflow transitions: $$ \text{At Gate} \rightarrow \text{Parked / Docked} \rightarrow \text{Gate Out} $$ A Forge App bridges on-ground staff and the digital system. It generates QR codes encoding the Jira issue key, allowing quick identification and updates via mobile scanning. The Forge layer also implements smart dock and parking allotment logic , ensuring assets are assigned only when available. Confluence is used to store unstructured operational data. Shift reports and digital manifests are automatically generated when vehicles enter docking stages. Jira Service Management handles operational exceptions by allowing incidents to be raised directly from the Forge interface. Rovo Agent acts as a virtual yard assistant, enabling natural-language queries across structured Jira data and unstructured Confluence logs. Challenges we ran into Resource allocation conflicts: Preventing double-booking of docks required real-time availability checks and strict assignment logic. Unstructured data management: Operational logs varied widely in format, making traditional search and analysis difficult. Handling failures gracefully: Real-world logistics frequently deviate from the happy path, requiring workflows that could absorb interruptions without breaking. Accomplishments that we're proud of Digitized an end-to-end physical logistics workflow using enterprise software tools Achieved real-time yard visibility without relying on a traditional database Automated dock and parking allocation to eliminate manual coordination Enabled non-technical staff to retrieve operational insights using natural language Designed a resilient system that handles exceptions without disrupting core workflows What we learned This project demonstrated that enterprise workflow platforms can be effectively adapted for non-IT domains. Structured workflows combined with AI-driven intelligence can transform chaotic physical operations into transparent, optimized systems. Jira functioned as an operational control layer, Confluence as institutional memory, and AI as an accessibility layer for frontline users. What's next for YardMaster Integrating real-time GPS or IoT signals for automatic vehicle state updates Introducing analytics on yard efficiency, dwell time, and bottlenecks Predictive dock allocation using historical movement data Role-based dashboards for security, operations, and management teams Scaling YardMaster across multiple yards with centralized visibility <div