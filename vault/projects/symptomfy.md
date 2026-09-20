---
slug: "symptomfy"
url: "https://devpost.com/software/symptomfy"
title: "Symptomfy"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 253
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
---

# Symptomfy

> Symptomfy is an AI-driven health companion that turns a few simple questions into clear, personalized care advice—in minutes.

[Devpost](https://devpost.com/software/symptomfy) · hackathon [[SpurHacks]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]]

**stack** flask, python, react, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for symptomfy

## Body

One-pager explaining Symtomfy's Startup Proposal Inspiration Your spark for Symptomfy came from watching how easily people—yourself included—get anxious and confused by online searches or generic symptom checkers, only to end up waiting hours in an ER (or worse, delaying care when it really mattered). You wanted a fast, question-driven flow that delivers clear, personalized next steps—in minutes—so users can decide whether to treat at home, book a doctor, or head to urgent care, all while cutting down unnecessary costs and easing the strain on health systems. What it does Personalized Care Advice Uses a medical-grade decision tree (with room to plug in ML models later) to recommend one of three paths: Home care resources Book a nearby provider Seek urgent/emergency care How we built it rontend React + TypeScript with Tailwind CSS for rapid, responsive layouts Headless UI & Framer Motion for accessible, animated dialogs and transitions Recharts for nice-looking wait-time and cost comparison charts Backend Python Flask hosted in a Docker container Decision‐tree logic encoded in a service layer, with clear interfaces to swap in ML models later Infrastructure Containerized on Google Cloud Run for auto-scaling and zero-maintenance operations Appointment-booking integration via secure RESTful APIs (OAuth2) Logging & monitoring with Cloud Logging and Cloud Monitoring Challenges we ran into SO MANY CORS ISSUES. SO MANY BUGS. Accomplishments that we're proud of That we finally connected it all together at 4am. What we learned It’s better to ask one well-phrased question than three overlapping ones. What's next for Symptomfy Better ML models. <div