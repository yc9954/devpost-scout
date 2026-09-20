---
slug: "nest-newborn-maternal-safe-transition"
url: "https://devpost.com/software/nest-newborn-maternal-safe-transition"
title: "NEST: Newborn & Maternal Safe Transition"
hackathon: "Agents Assemble - The Healthcare AI Endgame"
organization: "Prompt Opinion (Darena Health)"
winner: true
words: 1484
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/video_visual"
---

# NEST: Newborn & Maternal Safe Transition

> Fragmented charts cost lives. NEST saves mothers and newborns by orchestrating 5 AI agents that synthesize complex FHIR data into a unified, evidence-backed discharge control panel.

[Devpost](https://devpost.com/software/nest-newborn-maternal-safe-transition) · hackathon [[Agents Assemble - The Healthcare AI Endgame]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[structural_withholding]]
**domain** [[elder_child_care]] [[health_clinical]] [[labor_employment]] [[mental_health]]
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[code_repository]] [[geospatial]] [[medical_record]] [[video_visual]]

**stack** a2a-protocol, fhir, gemini, google-adk, httpx, litellm, multi-agent, ngrok, prompt-opinion, python, uvicorn

## How they structured the write-up

- 💔 inspiration
- 🪺 what nest does
- 🧬 meet sarah chen
- 🏗️ how we built it
- 🧠 what we learned
- 🪨 challenges we faced
- 🌅 what's next
- 🤍 why this matters

## Body

NEST — Newborn and Maternal Safety Agent "Severe BP, a baby above the phototherapy threshold, two breastfeeding-incompatible medications, no transportation home — and the current discharge plan would have caught none of it." 💔 Inspiration The United States has the worst maternal mortality rate of any developed nation. Roughly 700 mothers die each year , and the CDC estimates that 80% of those deaths are preventable . The most dangerous window isn't labor. It isn't surgery. It's the silence after discharge — the days when a new mother is home alone, exhausted, and trying to read her own warning signs through a fog of hormones and sleep deprivation. A typical postpartum patient in the US is handed a single instruction: "Follow up in 6 weeks." Six weeks. For the most physiologically volatile period of her life. For a person whose blood pressure can spike into stroke territory days after she leaves the hospital. For a baby whose bilirubin can climb past the phototherapy threshold while everyone smiles and says she's just a sleepy newborn . And here is the cruelest part of the system: the mother's chart and the baby's chart live in two different worlds. The OB never sees the pediatrician's notes. The pediatrician doesn't know the mother is on tramadol. The social worker who could have arranged transportation was never paged. Five specialists who should have been a team are instead five strangers leaving five separate notes in five separate EMRs. We built NEST — Newborn & Maternal Safe Transition — because no family should fall through the cracks between two charts. 🪺 What NEST Does NEST is a multi-specialist A2A agent that converts a chaotic postpartum discharge into a single, structured, evidence-backed transition plan for the mother-infant dyad . In ~90 seconds, it convenes the team that should have been at every bedside: Specialist Domain Knowledge Base 🩺 Maternal-OB Postpartum hypertension, preeclampsia, hemorrhage ACOG PB 222, ACOG CO 736, CDC "Hear Her" 👶 Pediatric Newborn jaundice, feeding, well-baby schedule AAP Bright Futures, AAP Hyperbilirubinemia 2022 🤱 Lactation Breastfeeding medication safety (Hale L1–L5) NIH LactMed, ABM protocols, FDA boxed warnings 🧠 Mental Health EPDS / PHQ-9 with explicit suicide-risk handling ACOG CO 757, USPSTF 2023 🏠 Social Work SDOH barriers → owned, time-bounded interventions CMS AHC HRSN, USPSTF IPV Each specialist returns a verdict matrix where every single row carries a Source column . The orchestrator joins them into a unified report — a Transition Score , a 7-day dual timeline, dual red-flag cards, a care-team task board with owners and due dates, and a plain-language summary the family can actually read. Nothing appears in the report without a citation. No source, no recommendation. 🧬 Meet Sarah Chen To make this real, we built a synthetic dyad that mirrors the cases that haunt every L&D nurse we've ever met: Sarah, 32. Postpartum day 2 after a Cesarean for severe preeclampsia. BP this morning: 162/108 . On tramadol for pain. EPDS score of 14. Lives alone, food insecure, no reliable transportation home. Baby Boy Chen, day of life 2. Weight loss now 9.86% . Total serum bilirubin 16 — above the AAP phototherapy threshold. Current discharge plan: "Follow up in 6 weeks." NEST scores this transition. Out of a hundred, it returns: $$ \text{Transition Score} = 5 / 100 \;\; \text{(Critical Hold)} $$ It fires an EMERGENCY box with a 60-minute action window. It flags tramadol against LactMed's FDA boxed warning. It writes a mental-health referral with a 7-day deadline. It pages Social Work for transport, food, and Medicaid coverage extension before she walks out the door. And every one of those calls links back to a rule ID — ACOG-PB-222-SEV , AAP-HYPERBILI-2022-PHOTO , LactMed-tramadol-FDA-2017 — so a clinician can trust it. 🏗️ How We Built It NEST is composed of three layers that we deliberately kept boring so the clinical work could stay sharp. 1. The Orchestrator and Council ( nest_agent/agent.py ) A Google ADK agent that fans out to five LlmAgent specialists in parallel. The wall-clock win is real: $$ T_{\text{NEST}} = \max_{i \in \text{specialists}} T_i \;\ll\; \sum_{i} T_i = T_{\text{serial}} $$ What would take a human care team a full day of paging and chart review collapses into a single coordinated turn. 2. The Dyad Context Layer ( nest_agent/tools/dyad.py ) The single most novel piece of work in NEST. We extended Prompt Opinion's inline-context pattern from one patient to two linked patients . The orchestrator calls set_inline_dyad_context once with the full dyad payload, and every specialist reads with get_dyad_*(subject="mother") or get_dyad_*(subject="infant") . The same shape will translate cleanly to a future FHIR-backed implementation: subject becomes a patient ID, and the tool fans out parallel reads against an EMR. 3. The Knowledge Bases ( nest_agent/data/ ) We refused to let the LLM make up clinical thresholds. So we curated: ACOG Committee Opinion 736, Practice Bulletins 222 and 183, Committee Opinion 757 AAP Bright Futures, Hyperbilirubinemia 2022, Breastfeeding Medicine 2022 NIH LactMed for the ~80 most-prescribed postpartum medications, encoded with Hale categories L1–L5 CMS Accountable Health Communities HRSN tool USPSTF Perinatal Depression 2023 and IPV 2018 CDC "Hear Her" maternal warning signs Every threshold, every red flag, every screening cutoff is a constant in a Python module — not a hallucination waiting to happen. 4. The A2A Surface ( nest_agent/app.py + shared/ ) NEST is exposed as a standard A2A agent on port 8005 , registered with a Prompt Opinion BYO Coordinator over an ngrok tunnel. The PO coordinator handles the human conversation, the FHIR context routing, and the TUI rendering. NEST handles the clinical reasoning. They speak via the A2A protocol, with the agent card published at /.well-known/agent-card.json . 🧠 What We Learned Multi-agent systems live or die on context plumbing. The clinical reasoning was almost the easy part. The hard part was making sure all five specialists were reading the same patient at the same time. Audit trails are not a feature — they are the product. Clinicians cannot, and will not, act on findings they cannot trace. The day we made Source a required column was the day NEST started feeling real. Latency is a UX problem with clinical consequences. Five LLMs in parallel still take 60–90 seconds. We had to teach Prompt Opinion to narrate the wait — explaining what NEST is doing under the hood — so the silence didn't read as a hang. The dyad is not a join. It is a relationship. Mother and baby are not two patients; they are a single physiological unit. Modeling that explicitly changed every downstream design decision. 🪨 Challenges We Faced A2A taskId reuse. Prompt Opinion's SendA2AMessage would forward the previous taskId , and our server would correctly refuse: Task is in terminal state: completed. We documented the fix (start a new consult per request) and codified it in our README. FHIR's single-patient assumption. Every off-the-shelf FHIR helper assumes one patientId . The whole point of NEST is two . We built set_inline_dyad_context as a dyad-shaped escape hatch — and as the blueprint for a true dual-FHIR future. Cognitive load in the output. The first version of NEST returned a wall of text. Clinicians glazed over. We rebuilt the renderer around an ASCII "control panel" with ANSI-styled badges, a Transition Score above the fold, and dual red-flag cards designed to be photographed on a phone. Hallucination guardrails. Early specialists would confidently invent BP thresholds. We hardcoded every clinical constant into data/ modules, and we made the LLM cite the rule ID it used. If it can't cite a rule, it can't include the finding. 🌅 What's Next Replace inline mode with live FHIR queries scoped per subject ( mother_patient_id , infant_patient_id ). Write back the care-team task board to the FHIR server, so NEST's recommendations become real assignments in the real EMR. SMS and patient-portal delivery of the caregiver summary and red-flag cards, so the safety net reaches home with the family. Nightly sync of knowledge bases from authoritative sources. Generalize the dyad scaffolding to other linked-patient workflows: pediatric asthma + caregiver , oncology patient + family caregiver , transplant donor + recipient . 🤍 Why This Matters We are not building NEST to win a hackathon. We are building it because somewhere in America tonight, a new mother is going home with a blood pressure of 162 over 108 and a six-week follow-up appointment, and her baby is sleeping a little too deeply in the car seat next to her. A whole team should have looked at them. A whole team should have told her what to watch for. A whole team should have made sure she had a ride to her postpartum visit and food in her fridge when she got home. NEST is that team. In ninety seconds. With every recommendation linked to a guideline. For every dyad. Every time. No mother should die because her chart and her baby's chart were in different systems. <div