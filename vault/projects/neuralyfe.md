---
slug: "neuralyfe"
url: "https://devpost.com/software/neuralyfe"
title: "NeuraLyfe"
hackathon: "FigBuild 2026"
organization: "Figma"
winner: true
words: 658
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "user/clinician"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# NeuraLyfe

> NeuraLyfe makes hidden brain damage visible, helping medical staff detect risk earlier and protect players before symptoms appear.

[Devpost](https://devpost.com/software/neuralyfe) · hackathon [[FigBuild 2026]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[health_clinical]]
**user** [[clinician]]
**substrate** [[genomic_bio]] [[geospatial]] [[sensor_telemetry]]

**stack** figma, figmamake

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned

## Body

Inspiration Football players take thousands of hits over the course of their careers. Most of the damage is invisible. Chronic Traumatic Encephalopathy (CTE) has become one of the most alarming consequences of repeated head impacts. Many players only discover the damage after they die , when their brains are examined during autopsy. Studies have found CTE in 91% of examined NFL players . On the sideline, medical decisions are still largely based on visible symptoms and quick evaluations. But brain damage often accumulates silently, long before those symptoms appear. So we asked a simple question: What if coaches and medical staff could see the hidden impact on the brain as it happens? NeuraLyfe was created to make the invisible visible. What it does NeuraLyfe turns football helmet impact data into actionable medical insights for sideline decision-making . The system presents three interactive views designed for medical staff: Roster View Flags players at risk before symptoms appear. Athletes are ranked by medical urgency based on cumulative impacts and brain health indicators. Brain View A 3D brain visualization mapping neurological stress by region, revealing early degeneration and cumulative brain impact. Impact Replay Traces every detected hit back to the play, showing severity, timing, and affected brain regions. Together, these views allow medical teams to detect risk earlier, understand neurological impact, and make safer decisions during games and practices. How we built it We approached NeuraLyfe as an end-to-end interactive system that turns complex neurological data into intuitive medical decisions. First, we designed the core interaction model around three key views used by sideline medical staff: Roster , Brain , and Impact Replay . These views translate helmet impact data into actionable insights that can be understood instantly during high-pressure game situations. We prototyped the interface using Figma and Figma Make , allowing us to build interactive visualizations that simulate real-time medical monitoring. The system aggregates simulated helmet sensor data and maps it into player risk scores, brain health visualizations, and impact replay analysis. To demonstrate the workflow, we designed a full sideline scenario where medical staff can: identify at-risk players from the roster view inspect brain health changes in the 3D brain view trace dangerous hits back to the exact play through impact replay This approach allowed us to quickly prototype a future-facing system that combines wearable sensing, data visualization, and real-time decision support for safer football. Challenges we ran into Translating complex brain data into intuitive signals. Neurological indicators like brain activity, biomarkers, and cumulative impacts are difficult to interpret quickly. Designing visualizations that communicate risk instantly for sideline medical staff was a major challenge. Balancing real-time decisions with long-term brain health. Doctors on the sideline need immediate insights during a game, while players and teams also need to understand cumulative damage over an entire career. Designing interfaces that support both time scales required careful interaction design. Making invisible damage understandable. CTE develops gradually and cannot be directly observed during a game. We had to explore ways to visualize hidden neurological risk and connect individual impacts back to real plays. Designing for high-pressure environments. Medical teams have only seconds to make decisions. We focused on clarity, visual hierarchy, and interaction speed to ensure the system communicates risk at a glance. What we learned Invisible problems require visible systems. Brain injuries often accumulate silently, making them difficult to detect through symptoms alone. Designing systems that surface hidden risk can fundamentally change how medical decisions are made. Clarity is critical in high-pressure environments. Medical staff only have seconds to evaluate players. We learned that medical interfaces must prioritize clear signals and visual hierarchy over complex data. Interaction design can bridge complex science and real-world action. By translating neurological signals into intuitive visualizations, design can help transform raw sensor data into meaningful decisions. Proactive health monitoring is the future of sports medicine. Instead of reacting to visible injuries, systems like NeuraLyfe could enable earlier detection and prevention of long-term brain damage. <div