---
slug: "trialflow"
url: "https://devpost.com/software/trialflow"
title: "TrialFlow"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 562
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/code_repository"
---

# TrialFlow

> The Smart Clinical Trial Coordinator

[Devpost](https://devpost.com/software/trialflow) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[scientific_research]] [[supply_logistics]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[code_repository]]

**stack** creao, google-calendar-api, google-gmail-oauth, react, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what does it do
- how we built it
- challenges we ran into
- what's next for trialflow

## Body

Inspiration 40% of patients drop out of clinical trials before completion, and scheduling friction drives a large share of attrition. Clinicians spend hours coordinating windows, patients miss reminders, and research teams lose momentum. Phase 1 of most clinical trials lasts only a few weeks, and each delay weakens patient engagement and undermines trial consistency. We are also keenly aware that clinicians’ expertise is best applied to interpreting trial results, not managing logistics. Yet studies show that clinical staff spend up to 25–30% of their time on administrative logistics like scheduling and follow-up management, time that could otherwise advance research and patient care. Enter TrialFlow, an intelligent scheduling platform that streamlines clinical trial coordination for both clinicians and patients. Clinicians set availability windows with real-time booking limits, and the app takes care of the rest. Patients can self-schedule visits based on clinician availability and receive 24-hour reminders with logistics and clear instructions on how to prepare for the upcoming appointment. A built-in burden score estimator measures participant load, helping researchers anticipate fatigue and enhance follow-up planning. What does it do Clinicians log into the dashboard, select a date range on the calendar, and specify procedures (Blood Draw, ECG, MRI, etc.) and per-slot booking limits. Patients are then notified via email that appointment times have opened up, and are sent a link that redirects them to their patient dashboard. From here, they are able to book their appointment time, add the event to their Google Calendar, and download an ics file if they wish to utilize any other calendar application. Finally, an email reminder is sent to each patient 24 hours before their upcoming appointment covering procedures, logistics, and if necessary, special instructions on how to prepare for the appointment. How we built it We built TrialFlow using Creao as the foundation for managing data models and workflow logic, which helped us quickly structure our backend and integrate custom functionality. On top of that, we used Creao to develop a custom Burden Score API to estimate participant workload based on visit frequency, procedure complexity, and total time commitment. For the frontend, we used TypeScript, React, and Tailwind CSS to create a clean and intuitive interface for both clinicians and patients. We implemented Google OAuth for secure sign-in and integrated the Google Calendar API so users can easily add upcoming appointments to their calendars and receive automatic reminders on their devices. This stack let us build a cohesive, production-ready scheduling platform that bridges the gap between clinical coordination and patient accessibility. Challenges we ran into One of the main challenges we faced was working with Creao for the first time. While it provided a great starting point for structuring our backend and workflows, understanding its abstractions and figuring out how to extend it with our custom Burden Score API took time and experimentation. Integrating the Google Calendar API also came with hurdles, especially around OAuth permissions, refresh tokens, and syncing events across multiple accounts to ensure a smooth user experience for both clinicians and patients. What's next for TrialFlow Given a time frame of 36 hours, our team had many more features planned than we were able to execute. Primarily, we'd love to integrate TrialFlow with existing Clinical Trial Management Systems, or CTSM for short. This way, clinicians have an all-in-one stop for them to manage their logistics and aggregate data from their trials. <div