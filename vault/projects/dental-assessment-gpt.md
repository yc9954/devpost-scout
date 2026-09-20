---
slug: "dental-assessment-gpt"
url: "https://devpost.com/software/dental-assessment-gpt"
title: "Dental Assessment GPT"
hackathon: "OpenAI Open Model Hackathon"
organization: "OpenAI"
winner: true
words: 976
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Dental Assessment GPT

> Dental GPT that generates evidence-based dental assessments and treatment plans from case data. Treatment planning is critical for patient care provided + revenue generation for dental clinics.

[Devpost](https://devpost.com/software/dental-assessment-gpt) · hackathon [[OpenAI Open Model Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[retrieval_grounding]]
**domain** [[finance_payments]] [[health_clinical]] [[mental_health]]
**user** [[legal_professional]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** python, shell

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dental assessment gpt

## Body

How it all works? Data Distribution and Output Inspiration Several dentists in lower-socio economic areas administer care with limited knowledge and understanding. Thirdly, dentists are facing significant burn out and dental practices are just getting busier. We hope this GPT helps them diagnose and provide essential care to their communities. What it does The Dental Assessment GPT generates an evidence-based dental assessment & plan from a structured case, and qualitatively grade the assistant’s output against clinical principles. The GPT takes inputs such as Patient data, oral problems, patient medical history, clinical findings, radiographs, current medications and habits. How we built it We built this using a mix of data collected from dentists via surveys + publicly available data and specialised problem/treatment dental documentation. 1. Dataset Processing Pipeline ⁠ Initial Data Audit Found 2494 total cases in dataset ⁠ Placeholder patterns (e.g., “Patient reports symptoms began approximately 2 weeks ago”) dominated content Clinical Enhancement Enriched cases with demographics (age 18–75, gender balance, diverse occupations) Inserted condition-specific findings : Caries vs. periodontal disease vs. cysts vs. mucosal lesions Matching radiographic findings (periapical radiolucency, bone loss patterns, cystic expansion, etc.) Urgency levels (0 = elective, 1 = moderate, 2 = urgent) ⁠ Full Pipeline Application Applied continous refinements and enhancements to get the final 2494 cases . Have gone through expert feedback and llm as a judge fine tuning to get robust causal links ⁠ Quality Control Gates JSON schema validation (ensured ⁠ diagnosis ⁠, ⁠ etiology ⁠, ⁠ urgency ⁠, ⁠ management ⁠, ⁠ abx ⁠, ⁠ follow_up ⁠, ⁠ counseling ⁠, ⁠ guideline ⁠) Internal checks for: missing values, duplicate patient profiles, inconsistent urgency assignments 2. Expert Validation Process Dentist Grading via Typeform Practicing dentists graded sample cases for clinical plausibility and completeness Scores used to refine enhancement logic Typeform: https://form.typeform.com/to/RFEHs2Xy Agent Mode Research Ran 40+ structured Agent Mode queries (e.g., “How would a periodontist classify this?”) Extracted literature-backed treatment pathways. AI Cross-Comparison Benchmarked random cases against ChatGPT-5 “thinking” mode outputs Flagged inconsistencies between enhanced cases vs. gold-standard reasoning Structured Input–Output Linking Built causal mapping: Demographics + findings → Risk assessment Risk assessment + urgency → Management plan Management plan + systemic signs → Antibiotic indication Challenges we ran into Data Issues ⁠ Duplication Noise – 95% of data was placeholders ⁠ Template Lock-In – Generic time markers ("2 weeks ago") everywhere ⁠ Missing Clinical Context – No age, gender, or systemic history initially ⁠ Radiographic Gaps – No condition-specific images described Flat Urgency Levels – Every case looked the same complexity-wise Dentist buy in – Typeform required about 45mins of dentists time which was hard to get in this short window. Over-Representation of Healthy Cases – Dataset skewed toward low-complexity “routine” or “checkup” visits, underrepresenting challenging pathologies. Ambiguity in Diagnoses – Some cases were vague or combined multiple possible conditions, creating fuzzy labels for model training. Technical Problems Python Failures – Syntax errors during JSONL transformation ⁠ Scope Creep – Accidentally generated “healthy check-up” patients instead of pathology-driven cases ⁠ Expert Coordination – Dentists flagged inconsistencies requiring multiple feedback loops ⁠ AI Variability – ChatGPT-5 outputs differed across sessions even with structured prompts Accomplishments that we're proud of We have learnt a lot about the dental space over the last 2 weeks and the long term impacts poor dental treatments can have on people. We are most pleased that dentists feel heard when we talk to them and are able to create something that can alleviate some of the pressures they face. Alongside this holistic accomplishment we also are proud of: Data & Clinical Deduplication First – prevents amplifying noise ⁠- Schema Discipline – enforce required fields early ⁠ Scope Boundaries – healthy cases ≠ pathology training data Urgency Calibration – cases must span elective to urgent for realism Causal Pathways – clinical data must logically connect to management Technical ⁠ JSONL Handling – strict error checks & rollback points ⁠ Template Detection – auto-flag placeholder cases pre-enhancement ⁠ Version Control – multiple checkpoints during processing ⁠ Iterative Sampling – small test batches before scaling full dataset Expert Validation ⁠ Typeform Feedback Loop – dentist ranked scores provided measurable quality signal. We had to make the typeform ourselves and let dentist to rank out of 4 answers. Here is the form: https://form.typeform.com/to/RFEHs2Xy ⁠ Agent Mode Testing – revealed weak spots where AI diverged from expert consensus. good for rapid dataset production. ⁠ Cross-AI Comparison – Over the span of several days we continuously sampled, compared and refined the training data and graded each sample out of 100. ChatGPT-5 thinking mode was vastly more superior in understanding input output pairs than ChatGPT normal mode (which seems to give a relatively higher score on training data when using it to compare samples). What we learned Despite enhancements, the final dataset skewed heavily toward “healthy” patient cases , limiting its usefulness for training pathology-focused dental AI. This underlined the need for domain-specific expert tuned validation criteria : Minimum pathology density Balanced representation of caries, periodontal, mucosal, and radiographic conditions ⁠- Urgency distribution reflecting real-world triage ability to capture nuances is only possible with scale. Instead of 2494 high quality gold outputs, more samples curated and reviewed by experts helps understand nuance a lot better. What's next for Dental Assessment GPT We have a strong feeling that this GPT can become the spine/brains for several Dental AI agents if further refinement can be provided. We plan on getting dentist buy in and refining this model further with RLHF on the fine tuned outputs. At inference we hope to implement RAG in context and longer token sequences to make model fully context aware. In line with recent breakthroughs in model hallucinations, we also plan to improve its ability to reject prompts and not solely aim for the best answer, instead improve its "i dont know" quotient for multivariate dental cases. <div