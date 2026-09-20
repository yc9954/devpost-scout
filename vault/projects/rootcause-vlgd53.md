---
slug: "rootcause-vlgd53"
url: "https://devpost.com/software/rootcause-vlgd53"
title: "RootCause"
hackathon: "Agents Assemble - The Healthcare AI Endgame"
organization: "Prompt Opinion (Darena Health)"
winner: true
words: 1188
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# RootCause

> A FHIR-native multi-agent AI system that detects why dental patients stop coming in and automatically generates personalized re-engagement plans, orchestrated across five specialized A2A agents.

[Devpost](https://devpost.com/software/rootcause-vlgd53) · hackathon [[Agents Assemble - The Healthcare AI Endgame]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[finance_payments]] [[health_clinical]] [[mental_health]] [[transportation]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** a2a, fhir, gemini-3.1, json, mcp, promptopinion

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rootcause

## Body

Inspiration Dentistry has a retention problem that nobody talks about. One in three Americans skips recommended dental care every year — not because they don't care about their health, but because something specific gets in the way. After speaking with dental professionals, the same two culprits kept surfacing: dental anxiety and financial fear. What struck us wasn't just how common these barriers are, but how invisible they are to the practice. A patient cancels with a vague excuse. The front desk sends a generic recall reminder. The patient never comes back. Nobody ever found out why. We wanted to build a system that could get to the root of it. What it does RootCause is a FHIR-native multi-agent AI system that detects why dental patients stop coming in and automatically generates personalized re-engagement plans — no manual staff intervention required. When a patient misses or cancels an appointment, the pipeline activates automatically. The RootCause Orchestrator coordinates five specialized agents in sequence: Pattern Scout analyzes the patient's FHIR record, activity log, clinical notes, and financial history to detect anxiety signals, financial red flags, and avoidance patterns. Empathy Bridge then conducts a warm, adaptive four-phase conversation with the patient to surface the real barrier — without ever revealing that their data was analyzed. Based on what the patient shares, the Orchestrator routes to Financial Navigator, which pulls live insurance coverage via FHIR context, assesses prior authorization risk through ClaimShield AI, and generates three payment plan options alongside a personalized patient message that mirrors the patient's own words. Everything is synthesized into a single Staff Summary Brief — delivered to the front desk with zero manual effort. How we built it RootCause was built entirely on the Prompt Opinion platform using a no-code agent configuration approach. Each of the five agents was configured with a carefully engineered system prompt, a structured JSON output schema, defined A2A skills, and explicit guardrails. The agents communicate through Prompt Opinion's native A2A protocol, with FHIR R4 patient context propagated across every agent call via the SHARP extension. The FHIR MCP Server provided live patient data connectivity. ClaimShield AI was integrated as an external A2A agent for denial risk assessment and prior authorization flagging. Patient documents — including clinical history, activity logs, and financial records — were uploaded to a Prompt Opinion knowledge base collection to ground agent reasoning in real-world data. The demo was built around a synthetic patient, Lincoln Bednar, with realistic mock documents designed to trigger both the anxiety and financial re-engagement pathways simultaneously — demonstrating the system's ability to run parallel agent workflows and synthesize their outputs into a single coherent deliverable. Challenges we ran into The most significant technical challenge was prompt engineering for Gemini Flash Lite. As a smaller, speed-optimized model, it required far more explicit, step-by-step instructions than larger frontier models to produce consistent structured JSON output. Any ambiguity in the system prompt produced incomplete schemas or agents that skipped reasoning steps entirely. Every prompt went through multiple iterations before producing reliable, clinically appropriate output. The A2A handoff between Pattern Scout and Empathy Bridge was the most fragile point in the pipeline — ensuring the pattern brief JSON was correctly passed into Empathy Bridge's context required careful orchestrator routing logic and fallback handling for cases where the handoff produced no usable output. Working across a split team — one deeply technical, one deeply clinical but non-technical — also required building a workflow where both contributors could work in parallel without blocking each other. The clinical domain expert owned knowledge base curation, synthetic patient design, output review, and the demo narrative, while the technical lead owned all platform configuration and prompt engineering. This division turned out to be a strength: the clinical review caught several instances where the agents produced technically valid but clinically unrealistic output that would have undermined the submission's credibility. Accomplishments that we're proud of We are proud of building a system that genuinely could not be replicated with rule-based software. The barrier identification logic — detecting anxiety signals in unstructured clinical note language, correlating them with appointment avoidance patterns, and routing to the right response — requires the kind of reasoning across ambiguous, heterogeneous data that only generative AI can do at scale. We are also proud of Empathy Bridge. Getting a language model to conduct a warm, human, four-phase patient conversation — one question at a time, never clinical, never revealing its data sources, adaptive to what the patient actually says — required significant prompt design effort and produced something that genuinely feels like it belongs in a real patient experience workflow. Finally, we are proud of the Staff Summary Brief as a concept. The goal was never to build impressive AI outputs for their own sake — it was to collapse a 15-to-20 minute manual re-engagement process into a single document a front desk coordinator can act on in under 60 seconds. That focus on the last mile of clinical utility guided every design decision we made. What we learned We learned that prompt engineering is product design. The difference between an agent that produces useful clinical output and one that produces plausible-sounding nonsense comes down entirely to how precisely you define its role, its reasoning steps, its output format, and its guardrails. This is especially true on a smaller model like Gemini Flash Lite, where the system prompt has to do work that a larger model would handle implicitly. We also learned that the no-code path is genuinely powerful for healthcare AI use cases — not as a shortcut, but as the right tool when the core value lies in clinical reasoning design rather than software engineering. The Prompt Opinion platform handled the infrastructure complexity of A2A communication, FHIR context propagation, and multi-agent orchestration, freeing us to focus entirely on the quality of the clinical logic. And we learned that the most important person in an AI healthcare project is the one who can tell you when the output is wrong. Clinical domain knowledge is not a nice-to-have — it is the quality gate that determines whether an AI system is safe to put in front of a clinician. What's next for RootCause The immediate next step is adding Comfort Planner — the anxiety resolution agent that generates specific care team protocols for managing anxious patients, including scheduling recommendations, environment preparation, and communication approach guidance. This was scoped out of the hackathon build due to time constraints but is fully designed and ready to configure. Beyond that, RootCause has a natural expansion path into broader dental practice intelligence. The same pattern detection and conversational barrier assessment framework could be applied to treatment plan acceptance (why did the patient decline the crown?), post-treatment follow-up (is the patient recovering as expected?), and preventive care gap closure (which patients are overdue for which screenings?). The longer-term vision is a practice-wide patient intelligence layer that runs continuously in the background — surfacing the right intervention for the right patient at the right moment, without requiring a single staff member to manually identify who needs attention or why. RootCause is the proof of concept for that vision. <div