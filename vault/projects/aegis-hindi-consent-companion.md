---
slug: "aegis-hindi-consent-companion"
url: "https://devpost.com/software/aegis-hindi-consent-companion"
title: "Aegis Hindi Consent Companion"
hackathon: "Agents Assemble - The Healthcare AI Endgame"
organization: "Prompt Opinion (Darena Health)"
winner: true
words: 1261
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/clinician"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/medical_record"
---

# Aegis Hindi Consent Companion

> **India's AI-generated perioperative informed consent in Hindi — patient-specific, clinically grounded, and built for the real communication gap in Indian surgical care.**

[Devpost](https://devpost.com/software/aegis-hindi-consent-companion) · hackathon [[Agents Assemble - The Healthcare AI Endgame]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[structural_withholding]]
**domain** [[agriculture_food]] [[civic_government]] [[education]] [[elder_child_care]] [[health_clinical]] [[transportation]]
**user** [[clinician]] [[educator_student]] [[frontline_worker]] [[patient_family]]
**substrate** [[medical_record]]

**stack** 3.11, a2a, apfel, asa, asra, classification, code, docker, esa, fastmcp, fhir, git, mcp, promptopinion

## How they structured the write-up

- inspiration
- what it does
- what makes this distinctly indian
- worked example (k+ 6.4 — postpone case)
- postponement notice in hindi
- how we built it
- mcp tools
- mcp server stack
- challenges we faced
- what we learned
- future scope
- built with
- links

## Body

From Complex Medical Language → Clear Hindi Explanations AI-generated perioperative consent in Hindi — designed for patients to truly understand. Consent Patients Can Actually Understand AI That Speaks the Patient’s Language Safer surgery starts with better understanding. When Patients Understand Risks, Care Becomes Safer Aegis transforms perioperative data into understandable consent. INSPIRATION India performs over 50 million surgical procedures annually. The majority of patients in government hospitals — AIIMS, PGIMER, JIPMER, district hospitals — are Hindi-speaking, with limited English literacy. Yet almost all pre-operative informed consent happens in English: the consent form, the surgeon's explanation, the anaesthesia risk discussion. This is not informed consent. It is the performance of consent. A patient who cannot read the form they are signing has not consented to their surgery. A patient who does not understand what “anaesthetic complications” means — in any language — has not been informed of the risks. Legally, the signature may hold. Ethically, it does not. I see this every week. A patient from rural Uttarakhand, a farmer or a teacher or a homemaker, who has never heard the word “hyperkalemia” — signed a form using that word without understanding it. They trusted us. We owe them better than a signature on a form they could not read. Aegis Consent Generator (Hindi) was built to close this gap. Not as a translation tool. As a clinical communication agent that understands the patient’s actual risk profile — the K+ of 5.6, the Mallampati 3, the uncontrolled HbA1c — and explains it in clear, warm, respectful Hindi that a patient can read, understand, and genuinely consent to. WHAT IT DOES Aegis Consent Generator (Hindi) is a PromptOpinion AI agent that receives a completed preoperative risk assessment via A2A handoff from the Aegis Perioperative Copilot and produces a structured, patient-specific informed consent brief in Hindi. It is the same 8-section clinical structure as the English agent — but written in simple, accessible Hindi, calibrated for a typical educated Indian family. Not literary Hindi. Not bureaucratic Hindi. The Hindi you would speak to a patient’s family in a pre-op clinic. LANGUAGE ARCHITECTURE Patient-facing sections (1, 2, 3, 6, 7) Written in clear, simple Hindi (Grade 8 level) Medical terms introduced in Hindi, with English in parentheses Example: रक्त में पोटेशियम (Serum Potassium) की मात्रा थोड़ी अधिक है (5.6 mmol/L; सामान्य 5.0 से कम होनी चाहिए)। Clinical documentation sections (4, 5 — Surgeon Checklist + Optimisation Action Table) Bilingual: Hindi label + English clinical term alongside Medicolegal records must be interpretable by English-language review; Hindi alone is insufficient Example: □ रोगी को ASA III वर्गीकरण के बारे में बताया गया / Patient informed of ASA III classification. WHAT MAKES THIS DISTINCTLY INDIAN 1. Indian Clinical References AIDAA 2024 guidelines, ISA protocols, AIIMS context wherever relevant — not just western guideline citations. 2. Indian Drug Names Glycomet instead of Metformin, Ecosprin instead of Aspirin, Warfarin as “खून पतला करने की दवा (Warfarin)” — the name the patient actually knows from their prescription. 3. Indian Cost Framing When explaining consequences of postponement, references to ₹ costs rather than $ or £ — relevant to the patient’s financial planning around surgery. 4. Family-Inclusive Language Indian patients typically make health decisions with family. The language is written to be readable aloud to a family member, not just to the literate patient alone. 5. Cultural Calibration Warm, respectful tone appropriate to Indian patient-doctor relationships. Honest about risk without being alarming. WORKED EXAMPLE (K+ 6.4 — POSTPONE CASE) English Consent “Serum potassium is critically elevated at 6.4 mmol/L. Surgery is contraindicated. Postponement required.” Aegis Consent Hindi आपके खून में पोटेशियम (Potassium) की मात्रा बहुत अधिक है (6.4 mmol/L; यह सामान्य से काफी ज़्यादा है)। इस स्थिति में बेहोशी के दौरान दिल की धड़कन पर खतरनाक असर हो सकता है। इसलिए अभी ऑपरेशन करना सुरक्षित नहीं है। आपके डॉक्टर पहले इसका इलाज करेंगे और जब यह मात्रा सामान्य हो जाए, तब ऑपरेशन की नई तारीख़ तय होगी। Translation “The amount of potassium in your blood is very high (6.4 mmol/L; this is much more than normal). In this condition, there can be a dangerous effect on heart rhythm during anaesthesia. Therefore, operating now is not safe. Your doctor will treat this first, and when the level becomes normal, a new surgery date will be set.” This is what genuine informed consent in Hindi looks like. POSTPONEMENT NOTICE IN HINDI When the Aegis recommendation is POSTPONE , the Hindi agent generates a full postponement letter in Hindi — explaining: why surgery cannot proceed, what must happen before rescheduling, and who to contact. The patient receives this in a language they can read and share with their family. HOW WE BUILT IT AGENT ARCHITECTURE Aegis Supervisor (Agent 1) ↓ assessment JSON via A2A Aegis Safety Reviewer (Agent 2) ↓ final assessment + safety addendum via A2A Aegis Consent Generator Hindi (Agent 4) ↓ 8-section bilingual consent brief SYSTEM PROMPT (IN HINDI) Written entirely in Hindi — intentionally. The system prompt establishes: the agent’s identity in Hindi, language rules, reading level ( कक्षा 8 ), Indian clinical context requirements, recommendation-gating behaviour. CONSULT PROMPT Includes: full 8-section structure, worked examples for every major flag type, bilingual formatting rules, explicit postponement letter structure. WORKED EXAMPLES IN THE PROMPT For: hyperkalemia difficult airway metformin HbA1c OSA PONV anticoagulants Each includes a calibrated Hindi paragraph to guide consistent medical output. MCP TOOLS The Consent Generator operates primarily from A2A assessment JSON, but remains connected to the Aegis Anesthesia MCP server. If additional patient context is needed, the agent can directly call: fetch_patient_from_fhir normalize_fhir This allows: re-querying live EHR data, verifying missing values, grounding consent language in verified patient data. MCP SERVER STACK Python 3.11 FastMCP 3.x Railway deployment FHIR R4 Production Tools fetch_patient_from_fhir assess_current_patient normalize_fhir compute_risk_scores fetch_guideline format_aegis_report Deterministic Risk Engine Computes: RCRI STOP-BANG Apfel ASA cancellation probability 15+ safety flags Rule-based logic only. No hallucinated scoring. CHALLENGES WE FACED Hindi Medical Language Has No Standard There is no consensus on: “मधुमेह” vs “डायबिटीज़” “रक्त” vs “खून” “शल्य चिकित्सा” vs “ऑपरेशन” For consent: understanding matters more than vocabulary purity. Bilingual Section Calibration Sections 4 and 5 must remain legally interpretable in English while readable in Hindi. Cultural Tone Calibration The correct tone is: warm, honest, respectful, family-aware, not excessively formal, not blunt. Recommendation-Gated Hindi Different recommendations require different communication structures: PROCEED OPTIMIZE ESCALATE POSTPONE The postponement letter required especially careful language design. WHAT WE LEARNED 1. Language Is a Clinical Intervention Patients ask more questions and make more informed decisions when information is delivered in their own language. 2. Hindi AI Medical Output Needs Calibration Without prompt engineering: outputs become overly literary, or literal English translations. Worked examples solved this. 3. Bilingual Documentation Is Non-Negotiable India requires: English clinical interoperability, patient-language communication. Both are essential. 4. This Is the Missing Middle in Indian Healthcare AI Most healthcare AI in India targets English-literate users. The patients needing AI-assisted communication most are often excluded. 5. Context Matters The Hindi agent works because it connects to real perioperative risk data: “आपका HbA1c 8.9% है” instead of: “आपकी शुगर ज़्यादा है” Specificity creates trust. FUTURE SCOPE Immediate Tamil Telugu Bengali Marathi Gujarati Odia voice consent output Medium Term pictographic consent Hindi patient Q&A caregiver/family briefing mode Long Term ABDM / ABHA integration rural telemedicine support national multilingual consent framework BUILT WITH PromptOpinion A2A Protocol Claude Sonnet Python 3.11 FastMCP FHIR R4 Indian clinical context calibration Companion Projects Aegis Perioperative Copilot Aegis Consent Generator English LINKS Demo Video https://youtu.be/HNkhVd1zTGc PromptOpinion Agent https://app.promptopinion.ai/marketplace/agent/019e1012-8d75-71c8-a03a-3871af7cf396 Companion Projects Aegis Perioperative Copilot https://devpost.com/software/ai-assisted-perioperative-optimization Aegis Consent Generator English https://devpost.com/software/aegis-intelligent-consent-generator <div