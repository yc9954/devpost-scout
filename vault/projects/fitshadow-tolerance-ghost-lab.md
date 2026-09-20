---
slug: "fitshadow-tolerance-ghost-lab"
url: "https://devpost.com/software/fitshadow-tolerance-ghost-lab"
title: "FitShadow — Tolerance Ghost Lab"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 540
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/measured_ablation"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# FitShadow — Tolerance Ghost Lab

> See 2,000 possible fits before one tolerance becomes a jam.

[Devpost](https://devpost.com/software/fitshadow-tolerance-ghost-lab) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[measured_ablation]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[finance_payments]] [[housing_homeless]] [[scientific_research]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[web_dom]]

**stack** react, svg, typescript, vite, vitest

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments that we're proud of
- what we learned
- what's next
- technologies used
- disclosure and limitations

## Body

FitShadow’s 2,000 seeded ghost assemblies with Jam, Target, and Wobble outcomes. Inspiration A nominal dimension can look reassuring while the permitted variation around it remains hard to picture. FitShadow explores a more tangible way to learn a tolerance stack: show the possible assemblies as a population of “ghosts,” then connect their outcomes back to the dimensions that shaped them. What it does FitShadow presents one deliberately bounded bearing press-fit scenario. A learner can adjust the housing bore, shaft diameter, diametral coating build, and thermal diameter shift, then run 2,000 deterministic samples. Each sampled assembly is classified as Jam, Target, or Wobble from its calculated clearance. The workspace keeps the explanation attached to the result. It shows the sampled population, outcome rates, a tolerance-squared contribution estimate, nominal clearance, and an analytical worst-case envelope. A paired counterfactual changes only the housing-bore tolerance to ±0.04 mm and reuses the same seed, making the before-and-after comparison easier to inspect. How we built it The local prototype uses React, TypeScript, and Vite. A seeded Mulberry32 pseudo-random generator creates uniform, independent draws for the four inputs. The clearance calculation and classification logic live in a separate domain module, while a code-native SVG ghost field turns the samples into an interactive visual population. The same configuration and seed replay identically. Focused tests cover determinism, the 2,000-sample total, percentage accounting, nominal clearance, analytical worst-case bounds, classification boundaries, contribution totals, and the one-change counterfactual. Challenges The hardest design problem was keeping the visualization intuitive without pretending the simplified model knows more than it does. We made the clearance sign convention explicit, separated the analytical worst case from the sampled population, reused common random draws for the counterfactual, and kept the engineering limitations visible beside the result. Accomplishments that we're proud of The simulation is deterministic and inspectable instead of being a decorative random animation. One screen connects editable dimensions, the ghost population, outcome bands, contribution estimates, and a single-variable counterfactual. The model documents exactly how coating and thermal shift enter the clearance calculation. Boundary behavior and the default worst-case envelope are covered by automated tests. The prototype says what it excludes, so an educational result is not mistaken for an engineering release. What we learned Reproducibility improves explanation: a fixed seed lets a learner change one input without wondering whether a different random population caused the result. We also learned that an uncertainty visualization becomes more useful when its assumptions and exclusions remain close to the numbers, not hidden in fine print. What's next The next version could save and compare scenarios, explain individual ghost assemblies, and accept validated process data. Correlations, measured capability distributions, gauge error, GD&T, deformation, insertion force, and material behavior would only be added with suitable engineering data and validation. The current prototype intentionally makes none of those claims. Technologies used React TypeScript Vite SVG Vitest Disclosure and limitations FitShadow is an educational preflight for one bearing press-fit example. Its independent uniform distributions and simple outcome bands are not a bearing manufacturer specification. It must not be used for supplier acceptance, safety, warranty, fatigue, or release of a real assembly. No deployment URL, public repository URL, or demo-video URL is claimed in this draft. Those fields must remain empty unless independently created and verified. <div