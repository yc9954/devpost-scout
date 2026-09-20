---
slug: "fetch-health"
url: "https://devpost.com/software/fetch-health"
title: "Fetch Health"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1227
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/educator_student"
  - "user/general_public"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Fetch Health

> AI assistant for organ transplant

[Devpost](https://devpost.com/software/fetch-health) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[provenance_signing]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[education]] [[health_clinical]] [[supply_logistics]]
**user** [[clinician]] [[educator_student]] [[general_public]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** anthropic, claude, deepgram, fetchai, midjourney, react, redis, sentry

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fetch health

## Body

Inspiration Organ matching is one of the highest-stakes workflows in healthcare, but the process is hard to understand, hard to simulate, and difficult to explain clearly to non-specialists. Hospital staff often deal with fragmented medical documents, imaging files, reports, and patient history while trying to make sense of compatibility, urgency, logistics, and risk. We wanted to build something that makes this workflow more transparent, educational, and easier to reason about. Fetch Health was inspired by the idea of combining agentic AI, medical document understanding, imaging analysis, and explainable scoring into one simple hospital-facing workflow. Our goal was not to replace doctors or clinical systems. Our goal was to create a safe educational and simulation platform that shows how donor-recipient matching could be analyzed, explained, and visualized with modern AI infrastructure to save lives . What it does Fetch Health is a hospital-staff-facing donor and recipient intake and matching simulator. The interface is intentionally simple. Staff choose whether they are uploading information for a patient/recipient or a donor , upload medical files, and let the system process the case. For a patient/recipient case, Fetch Health analyzes uploaded documents, imaging, videos, and structured records, then returns the top three donor candidates with: compatibility percentage organ type estimated transport time transportation and medical risk missing information warnings collapsible candidate reports agent-generated reasoning summaries For a donor case, Fetch Health evaluates whether the donor profile can be added to the donor database. If accepted, the system confirms the donor profile was added and shows a respectful donor-status message. If not eligible, it explains that the donor is not currently eligible based on the available information. Behind the scenes, the system uses local agents for document analysis, image/video processing, chunking, profile creation, Redis-backed memory, candidate retrieval, compatibility scoring, ranking, transport risk, benchmarking, reporting, and voice debrief generation. Fetch.ai agents act as the public agent layer, while the heavy processing runs on our local backend infrastructure. How we built it We built Fetch Health as a modular agentic healthcare simulation system. The frontend is a simple hospital-staff interface with three screens: intake upload screen loading/processing screen result screen The backend is built around a local HPC-first architecture. Uploaded files are processed by a Master Orchestrator Agent, which coordinates local agents for documents, images, videos, profile building, compatibility scoring, ranking, benchmarking, and reporting. We used Redis as the core state and memory layer. Redis stores profile state, run status, agentic memory, stream events, rankings, document chunks, embeddings, and traceable agent outputs. Every agent writes a structured memory record so the system can explain what happened during a run. We designed a context-compacting layer for agent-to-agent handoff. Instead of passing huge raw context between agents, each agent emits a compact “context capsule” containing hard facts, findings, risks, missing fields, and references. Long narrative context can be compressed before report generation, while critical facts like IDs, scores, rankings, organ type, and risk values are preserved exactly. We used Fetch.ai as the public capability layer. The Fetch agents are lightweight routers that expose capabilities like intake, document intelligence, image intelligence, candidate retrieval, compatibility scoring, ranking, reports, and health checks. These agents route requests to the local backend instead of trying to run heavy medical processing themselves. We also integrated sponsor tools into the workflow: Fetch.ai for public agent orchestration and mailbox-style routing Redis for state, memory, rankings, traces, and retrieval Anthropic for final reasoning and report generation The Token Company conceptually for context compacting and token efficiency Sentry for monitoring backend, agent, and tool failures Deepgram for final voice debriefs MidJourney for UI/UX visual direction and design inspiration The system is designed as an educational and simulation workflow, not a clinical decision engine. Challenges we ran into One major challenge was balancing ambition with usability. Organ matching is complex, but hospital staff need a simple interface. We kept the frontend minimal and moved complexity into the backend agents. Another challenge was data structure. We needed profiles that could support documents, images, videos, reports, segmentation outputs, and matching metadata without pretending composite data represented a real patient. We solved this by separating public profile summaries, private artifacts, provenance, and agent memory. Agent orchestration was also difficult. If every agent receives every file and every trace, the system becomes noisy and inefficient. We solved this with Redis-backed context capsules and structured handoffs, so each agent receives only the information it needs. We also had to handle missing or incomplete medical information responsibly. Instead of fabricating data, the system tracks missing fields, lowers confidence, and surfaces warnings in the final report. Finally, coordinating Fetch.ai agents with local HPC processing required a clean separation: Fetch agents are public routers, while local agents do the heavy processing. Accomplishments that we're proud of We are proud that Fetch Health turns a complex healthcare workflow into a simple three-screen hospital-facing experience. We built a system where every step is traceable. Each agent writes memory, each run has events, and each result can be explained through structured reports. We are also proud of the context-compacting design. Instead of blindly dumping large documents and traces into an LLM, we separate hard facts from compressible context. This makes the agent pipeline more efficient, more reliable, and easier to debug. Another accomplishment is the modular architecture. Document analysis, imaging, video, retrieval, scoring, ranking, reporting, monitoring, and voice output are all separated into agents that can improve independently. Most importantly, we kept the system safe. Fetch Health is framed as an educational simulation and decision-support prototype, not a replacement for doctors or transplant allocation systems. What we learned We learned that good agent systems are not just about having many agents. They are about having the right boundaries between agents. We learned that Redis is extremely useful as an agent memory and state layer because it can store run status, events, rankings, vectors, chunks, traces, and summaries in one fast system. We also learned that healthcare AI needs transparency. A compatibility score alone is not enough. Users need to know why a profile ranked highly, what information was missing, and where the system had uncertainty. We learned that frontend simplicity matters. A powerful backend means nothing if hospital staff cannot use the product quickly and confidently. Finally, we learned that context management is one of the hardest parts of agentic AI. Passing less context, but better context, leads to better outputs. What's next for Fetch Health Next, we want to expand Fetch Health in several directions. First, we want to improve the profile database with more real open-source medical imaging, reports, and benchmark cases across brain, lung, heart, kidney, and liver workflows. Second, we want to strengthen the compatibility scoring system with better baselines, better evaluation, and clearer confidence scoring. Third, we want to improve the Fetch.ai agent layer so hospital staff and educators can interact with the system through ASI:One-style agent workflows, not only the web interface. Fourth, we want to expand the voice debrief system so doctors, educators, and trainees can ask follow-up questions about a report. Finally, we want to make Fetch Health a stronger educational simulator for medical students and transplant teams, where users can explore “what-if” cases, compare candidate rankings, and understand how different compatibility factors affect the final result. Fetch Health is not trying to replace clinical judgment. It is trying to make complex medical matching workflows more understandable, traceable, and teachable. <div