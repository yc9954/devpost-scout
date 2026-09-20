---
slug: "axiom-orthogonal-modeling"
url: "https://devpost.com/software/axiom-orthogonal-modeling"
title: "AXIOM AI — Dual-Engine Combinatoria"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 818
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/geospatial"
---

# AXIOM AI — Dual-Engine Combinatoria

> Most AI tutors guess their way through math and science. AXIOM computes first with a deterministic combinatorial engine (exact Punnett squares, permutations, electron configurations, harmonic analysis

[Devpost](https://devpost.com/software/axiom-orthogonal-modeling) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[geospatial]]
  <sub>weak: sensor_telemetry</sub>

**stack** chat-gpt, cloudflare, codex, css, d1, firebase, framer, meru-prastara, motion, next.js, pages, pi?gala, radhikachain, sol

## Body

Inspiration Most AI tutors guess. They produce confident-sounding explanations of Punnett squares, combinations, electron configurations or harmonic series that are subtly (or completely) wrong. Students absorb the error and build fragile mental models. AXIOM was born from a simple but radical inversion: compute first, explain second. We looked back to the 2nd–3rd century BCE, to Piṅgala’s Chandaḥśāstra and the method of prastāra (systematic enumeration of metrical patterns). Long before modern combinatorics, Sanskrit prosodists decomposed complex structures into atomic units (gaṇa), marked boundaries (yati), and enumerated every valid possibility with absolute rigor. We asked: what if a modern STEM tutor did exactly the same? The result is a dual-engine system that never approximates probabilities, never hallucinates electron configurations, and never invents combinatorial steps. It calculates the exact structure first, then hands a perfect JSON to a narrative layer that turns it into vivid, Socratic, age-appropriate explanations for students 13+. Built in a high-pressure 5-hour sprint for DSH Hacks V1 under the theme AI × STEM Education, AXIOM is our answer to the trust crisis in educational AI. What it does AXIOM is a dual-engine STEM tutor: Layer 1 — Combinatorial Decomposer (pure TypeScript, zero network calls, instant) Decomposes problems into atomic combinatorial units inspired by Chandas prosody and produces exact, machine-readable JSON. Supported domains today: Genetics → full Punnett grid enumeration + genotype/phenotype percentages Mathematics → permutations and combinations with complete step-by-step expansion Chemistry → electron configurations via the Aufbau principle (full + noble-gas notation) Physics → harmonic series (frequencies + wavelengths from a fundamental) Layer 2 — Narrative Adapter (OpenAi/GPT 5.6 sol) Takes the exact JSON and generates engaging, Socratic, story-driven explanations tailored for ages 13–18. The student first sees the structure, then receives the meaning. Additional features: Gamification (XP, badges, streaks) aligned with White Hat Octalysis Google sign-in via Firebase + progress persistence in Cloudflare D1 Optional Bhakti karma tier overlay from the RadhikaChain wallet Full observability (events shipped to Splunk) Demo mode that works even without API keys Live demo: https://axiom-stem.pages.dev How we built it Frontend: Next.js 15 (App Router) + TypeScript + Tailwind CSS + Framer Motion Layer 1 engine: Pure TypeScript combinatorial core (no external dependencies for the critical path) Layer 2: SuperGrok (xAI API) as primary narrative engine, with agent-core / Workers AI fallback Backend & persistence: Cloudflare Workers + D1 (axiom_progress table) Auth: Firebase Authentication (Google) with token verification against the RadhikaChain API Observability: Splunk HEC Deployment: Cloudflare Pages (primary) Time constraint: Entire functional product built and deployed in a single 5-hour hackathon sprint The architecture deliberately separates deterministic computation from probabilistic language generation so that the mathematical truth is never compromised by the LLM. Challenges we ran into Time pressure of a true 5-hour sprint while still delivering four working domains + auth + gamification + deployment. Designing a single combinatorial abstraction flexible enough for Punnett squares, C(n,r), Aufbau, and harmonic series without becoming a mess of special cases. Keeping Layer 1 completely deterministic and offline-capable while still producing rich enough JSON for the narrative layer to sound natural. Making the demo mode (no API keys) feel as polished as the full SuperGrok experience. Balancing the philosophical depth of the Chandas inspiration with a clean, modern UX that students actually want to use. Accomplishments that we're proud of A working dual-engine system that never hallucinates the math — the core differentiator. Full end-to-end product (decompose → narrate → gamify → persist → observe) shipped in five hours. Clean mapping from ancient Sanskrit prosody (prastāra, gaṇa, yati) to modern STEM problems that feels both rigorous and poetic. Live production deployment on Cloudflare Pages with real Firebase auth and D1 persistence. Comprehensive documentation, demo video script, one-pager, and submission package ready on day one. Seamless integration path into the larger RadhikaChain / A.L.I.C.E. sovereign education layer. What we learned Deterministic “compute-first” architecture is dramatically more trustworthy for STEM than pure LLM approaches. Ancient combinatorial methods (especially Piṅgala’s recursive enumeration) map surprisingly cleanly onto modern educational domains. Constrained time forces ruthless prioritization: the dual-engine separation was the single highest-leverage decision. Students respond more strongly when they first see the exact structure and then receive the narrative — it builds genuine understanding instead of passive consumption. Having a high-quality demo mode is non-negotiable for reliability during judging. What's next for AXIOM AI — Dual-Engine Combinatoria Expand domain coverage (advanced genetics, stoichiometry, wave mechanics, discrete math, basic linear algebra). Deeper RadhikaChain integration: learning actions can generate verifiable Proof-of-Impact / Bhakti signals. Classroom mode + teacher dashboard. Multilingual narrative layer (starting with Spanish and English). Mobile-responsive progressive web app + offline Layer 1 capability. Open-source the combinatorial core as a standalone library so other educators can build on exact engines. Pilot programs with schools and STEM clubs. Long-term vision: AXIOM becomes the education nervous system of the RadhikaChain / A.L.I.C.E. sovereign stack — a living, non-hallucinating tutor that respects both mathematical truth and the student’s dignity. <div