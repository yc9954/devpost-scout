---
slug: "zenohosp-hospital-s-operating-system"
url: "https://devpost.com/software/zenohosp-hospital-s-operating-system"
title: "ZenoHosp - Hospital's Operating System"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 524
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ZenoHosp - Hospital's Operating System

> One Hospital. One OS. Every Workflow Connected.

[Devpost](https://devpost.com/software/zenohosp-hospital-s-operating-system) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[finance_payments]] [[health_clinical]] [[scientific_research]] [[supply_logistics]] [[transportation]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]]

**stack** react, springboot

## How they structured the write-up

- inspiration
- what it does

## Body

Inspiration Hospitals run on a patchwork of disconnected systems — separate tools (or no tools at all) for finance, inventory, staff management, pharmacy, lab work, and patient scheduling. Front-desk staff, doctors, admins, and patients all lose time to coordination overhead that a unified software suite should have solved years ago. We wanted to build one platform that handles the entire operational backbone of a hospital, with each concern cleanly separated into its own module but sharing a consistent design language and data layer. What it does Zenohosp is a modular healthcare operations suite consisting of 8 core modules, each addressing a distinct operational concern: HMS (Hospital Management System) — The core module handling patient appointment booking and doctor scheduling. Built on a production-grade database design that manages recurring doctor availability, day-specific exceptions, break windows, and slot-type reservations — engineered to prevent double-bookings under high-concurrency load. Also includes room allocation and infrastructure mapping via a clinical-first React admin interface, and a tiered categorization system for routing medical investigation requests. Lab — Manages diagnostic test orders and results, working in tandem with HMS's investigation-routing tool to classify and direct tests to the correct department (radiology vs. pathology/laboratory). Pharmacy — Handles medication inventory, prescription fulfillment, and dispensing workflows tied to patient records. OT (Operation Theatre) — Manages surgical scheduling, theatre allocation, and resource coordination for procedures. Inventory — Tracks hospital supplies, consumables, and stock levels across departments, with reordering and usage visibility. Assets — Manages hospital equipment and infrastructure assets — tracking, maintenance, and lifecycle status of physical hospital resources. People — Staff and HR-oriented module covering hospital personnel management, shift/role assignment, and department staffing. Finance — Handles billing, payments, and financial operations tied to patient care and hospital administration. How we built it Frontend: React across all modules, with custom, clinically-styled components (e.g., a redesigned room allocation interface) built for clarity in fast-paced hospital environments rather than generic admin-template aesthetics Backend/Database: A normalized relational schema, with particular care taken in HMS's scheduling engine — recurring availability modeled separately from exceptions, and slot computation weighed between dynamic (real-time) generation vs. materialized (precomputed) slots to handle concurrent booking load , deployed on Architecture: Modular by design — each of the 8 modules (Finance, Assets, HMS, Inventory, People, Pharmacy, OT, Lab) is built to function as an independent service while sharing a common data and design foundation, so hospitals can adopt the full suite or individual modules Challenges we ran into Cleanly separating 8 distinct operational domains without duplicating shared data (patients, staff, rooms) across modules Designing HMS's scheduling schema to gracefully handle recurring schedules and one-off exceptions (holidays, leave, extended breaks) without conflicting states Deciding between on-the-fly slot computation vs. precomputed slots — balancing database load against real-time accuracy during high-traffic booking windows Migrating away from a legacy pattern of storing schedule days as comma-separated strings to a properly normalized structure Accomplishments we're proud of A genuinely modular suite architecture spanning the full operational surface of a hospital — not just a single-feature demo A booking system built for real concurrency, not toy-scale A cohesive design language across all 8 modules that feels like one integrated product <div