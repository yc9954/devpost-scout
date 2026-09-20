---
slug: "take-it-right"
url: "https://devpost.com/software/take-it-right"
title: "Take It Right"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 851
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/general_public"
  - "substrate/structured_db"
---

# Take It Right

> A safety-first medication risk analyzer that uses deterministic medical logic to detect overdoses, interactions, and organ stress—then explains the results with AI.

[Devpost](https://devpost.com/software/take-it-right) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[general_public]]
**substrate** [[structured_db]]
  <sub>weak: financial_record</sub>

**stack** custom-deterministic-rule-based-engine, flask, plotly.js, python, react, vite

## How they structured the write-up

- inspiration
- what it does
- key innovation
- system architecture
- challenges
- impact & usefulness
- what we learned
- what’s next
- final statement

## Body

Clinically structured rule engine. Risk scoring is deterministic; AI only generates explanations, never alters risk. Dose, timing, and organ load validated. No conflicts detected. System returns SAFE classification. Repeated dosing triggers accumulation logic and organ load scoring, resulting in a CAUTION risk classification. Duplicate paracetamol detected across brands. Deterministic engine escalates to HIGH RISK with structured guidance. Weight-based mg/kg validation flags unsafe pediatric dosing and deterministically escalates to HIGH RISK. Alcohol interaction rule increases liver toxicity risk and triggers automatic HIGH RISK escalation. Take It Right — Deterministic Medication Safety Before Harm Compounds Inspiration At 8:00 AM, someone takes a headache tablet. At 1:00 PM, they take a cold medicine. At 9:00 PM, another dose before bed. There’s alcohol at dinner. Every decision follows the label. Every dose feels safe. By midnight, they’ve unknowingly crossed the safe daily limit for a liver-toxic ingredient. No alarms. No warning. No obvious mistake. This is how most preventable medication harm happens. Not from reckless misuse. From normal decisions made across time : Two brands with the same hidden ingredient A “safe” repeat dose taken too soon Cold medicine + pain reliever stacking Pediatric dosing guesswork Alcohol mixed with common OTC drugs NSAIDs combined without realizing it Individually safe. Together, sometimes dangerous. Medication safety is not a guessing problem. It is a rules problem across time . Take It Right was built to detect preventable medication risk before it compounds into harm. Instead of asking AI to estimate risk probabilistically, this project asks: Can everyday medication safety be evaluated using transparent, deterministic medical logic — with AI used only to explain results? What It Does Take It Right is a deterministic medication safety engine that evaluates real-world dosing decisions across time before risk escalates. It models everyday scenarios: Repeating doses Combining medications Mixing with alcohol Pediatric dosing NSAID stacking Hidden duplicate ingredients The system analyzes a dose timeline , detects cumulative risk patterns, and surfaces conflicts before harm occurs. The engine evaluates 15+ structured safety rules: Weight-based dosing validation (mg/kg) Daily cumulative dose limits Single-dose maximum limits Time-spacing violations Alcohol interaction escalation NSAID stacking detection Hidden duplicate ingredient expansion Age and pregnancy contraindications Organ stress scoring (liver, kidney, stomach) Output includes: Quantitative risk score (0–100) Risk category: SAFE / CAUTION / HIGH RISK Deterministic HIGH-RISK overrides Structured conflict detection Clear, actionable guidance Visual dose timeline Organ load indicators This tool does not replace clinicians. It prevents avoidable mistakes before they stack into harm. Key Innovation Most health tools rely on probabilistic AI predictions. Medication safety should not depend on probabilistic guesses. Take It Right separates safety decisions from AI entirely. All risk classification is computed using deterministic medical logic: Transparent rules Reproducible outcomes Auditable decisions Deterministic HIGH-RISK overrides AI is used only after the decision is made — to translate structured results into clear language. AI can explain risk. It cannot change it. This separation ensures: Reliability Accountability Auditability Reduced hallucination risk Safety-first behavior In safety-critical contexts, that boundary matters. System Architecture Deterministic Safety Engine (Python + Flask) The core engine evaluates: Dose thresholds mg/kg pediatric validation Time-spacing logic Ingredient duplication Contraindications Interaction escalation Critical violations trigger deterministic HIGH-RISK overrides that cannot be downgraded by AI. All scoring and classification occur here. This ensures: Interpretability Reproducibility Auditable outcomes AI Explanation Layer After structured evaluation, an AI module converts results into plain-language guidance. The AI: Summarizes conflicts Explains risks clearly Provides understandable next steps The AI does not : Change scores Downgrade risk Modify decisions Safety decisions remain deterministic. Frontend Built with React, Vite, and Plotly.js to visualize: Risk gauge Organ load indicators Conflict cards Dose timeline Escalation triggers Actionable guidance The interface makes cumulative risk visible before harm occurs. Challenges Designing a safety-first system required balancing precision and usability. Key challenges: Designing an interpretable scoring model Preventing duplicate conflict inflation Implementing HIGH-RISK overrides correctly Modeling cumulative dosing across time Enforcing strict AI boundaries In safety systems, clarity is as important as correctness. Impact & Usefulness Many medication errors involve common over-the-counter drugs taken exactly as people believe is safe. These mistakes are: Preventable Common Often invisible until damage accumulates Take It Right helps detect: Cumulative overdosing Hidden duplicate ingredients Alcohol interactions Unsafe pediatric dosing NSAID stacking Dangerous time-spacing violations The system demonstrates how AI can support understanding without replacing structured safeguards. Goal: detect risk before it compounds. What We Learned Building for safety-critical scenarios changes system design: Determinism builds trust Clear boundaries improve accountability Interpretability matters more than novelty Responsible AI often means limiting AI Constraint is a design decision. What’s Next Expand medication database coverage Add deeper interaction modeling Strengthen pediatric and geriatric rules Refine organ load scoring Validate against clinical dosing guidelines Explore consumer and clinical integrations Long-term vision: A scalable, safety-first medication decision support system. Final Statement Medication mistakes rarely look dangerous in the moment. They accumulate quietly across hours and days. Take It Right demonstrates a safety-first model for AI-assisted healthcare: Deterministic logic for decisions. AI for explanation. By making cumulative risk visible and auditable, this system helps people recognize danger early — before routine decisions compound into preventable harm. <div