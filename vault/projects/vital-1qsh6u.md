---
slug: "vital-1qsh6u"
url: "https://devpost.com/software/vital-1qsh6u"
title: "Vital"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 495
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# Vital

> Agentic workflow platform that links new guidelines, drug approvals, and policy changes into actionable insights on current patients, empowering providers to act faster with confidence.

[Devpost](https://devpost.com/software/vital-1qsh6u) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]

**stack** cedaros, openai, react, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vital

## Body

Standard Page Radial Wheel Prompting AI helper for organization Zoomed out patient canvas Match feature in action Match feature with treatment plan generated Group of patients with note Inspiration While researching pain points in the healthcare industry, we repeatedly saw physicians voicing the same struggle: the constant influx of new medical literature, drug approvals, and policy updates. Many doctors spend hours reading and parsing through this information, but just as many struggle to keep up, risking outdated care for their patients. To help alleviate this stress, we wanted to build a platform that ingests the latest medical evidence and instantly shows a provider which of their own patients are affected. What it does Vital is an agentic workflow platform for clinicians. The real-time Research Stream is integrated with Impiricus' own data feed and continuously uses AI to analyze new guidelines, policy changes, etc and matches the relevant insights to the provider's own patient panel. It highlights impacted patients in an interactive dashboard, provides quick AI-generated explainers, and drafts patient education material. Vital even has a promptable group sorting feature that allows providers to quickly sort different patients into separate groups. How we built it We built Vital with a Next.js frontend, Tailwind/shadcn UI components, and Cedar-OS for the agentic workflow layer. Supabase serves as our database, organizing our information. OpenAI powers the natural-language extraction of criteria from new literature. Cedar-OS "spells" enable right-click context menus so clinicians can trigger actions (like matching patients or generating explainers) directly inside the dashboard. Challenges we ran into Some challenges we ran into include setting up the promptable AI 'helper' agent that can sort the different patient cards. Initially, we struggled to get the patient cards to act as a group to be able to move freely. We also struggled with integrating the OpenAI with CedarOS and getting the full workflow setup. Accomplishments that we're proud of We managed to build a working demo in under 36 hours that combines live patient data, guideline updates, and AI analysis. We also created an interface that doctors can actually use with a drag and drop canvas. And we integrated Cedar-OS "spells" to trigger AI workflows contextually, rather than relying on clunky buttons or forms. What we learned We learned how to orchestrate multiple cutting-edge tools like Cedar-OS, Supabase, and OpenAI into a cohesive agentic workflow. Additionally, we gained valuable insight into how clinicians think about information overload and how to present AI outputs in a way that focuses on building trust rather than overwhelming. What's next for Vital We plan to expand Vital from a single-provider dashboard into a collaborative and cross-team platform. Beyond surfacing literature and policy changes for one clinician, Vital will allow care teams to share notes and flag at-risk patients together. We're also exploring integrating anonymized outcomes data so the system can not only match guidelines to patients but also track downstream results and continuously improve its recommendations, turning Vital into a LLM for evidence-based care. <div