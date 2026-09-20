---
slug: "workbench-107jf2"
url: "https://devpost.com/software/workbench-107jf2"
title: "Workbench"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 642
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/legal_professional"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Workbench

> Cancer-state workbench for scientists. Cell biology LIVES on context - combos of genes mutated with different levels of variations respond differently. We built a causal model around your data.

[Devpost](https://devpost.com/software/workbench-107jf2) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[simulation_digital_twin]]
**domain** [[health_clinical]]
**user** [[clinician]] [[legal_professional]] [[patient_family]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** claude, codex, graphrag, neo4j, python, react, render, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for workbench

## Body

Inspiration As researchers ourselves, we know that cell biology has a context problem that affects researchers. The same gene, mutated two different ways, needs two completely different drugs. Yet, matching a tumor's actual mutation profile to the right drug is still mostly manual. A researcher cross-referencing pathway diagrams, drug labels, and papers by hand, with no curated answer for most real mutation combinations. We wanted a workbench that builds a live, causal model around your specific mutation data, not a static reference table. What it does Upload a tumor's mutation profile and the system builds it into a live pathway graph, then lets you ask natural-language questions about it. Behind the scenes, a deterministic lookup checks the graph first for a variant-specific drug match. Where the graph has no answer, a classifier trained on real DepMap LUAD CRISPR and mutation data predicts which pathway is still worth targeting. The output allows the user to clearly see what the most optimized pathway to continue with is, and why. How we built it We built a multi-agent pipeline on top of a Neo4j pathway graph: ingestion (CSV → LLM-hydrated mutations → KEGG pathways, streamed live via SSE), an agentic chat layer (natural language → Cypher → cited subgraph retrieval), and a drug-routing core (agent_pipeline/) — graph lookup → gap detection → ML fallback → synthesis. The classifier was trained on hundreds of real examples, built by filtering 440MB of DepMap CRISPR data and 580MB of mutation calls down to specific lung cancer cell lines. We evaluated it honestly with GroupKFold by gene, not random row splits, so reported performance reflects real generalization to an unseen mutation, not memorized gene identity. Challenges we ran into Our biggest challenge wasn't building the pipeline, it was trusting our own results enough to stop building and start questioning them. One of our refactors silently broke our gap-detection logic partway through, and it only surfaced because we ran the full pipeline end-to-end instead of assuming no errors meant it was working. We also hit a real data wall: with under 200 real training examples, building something that generalizes honestly, rather than just looks good on paper, took far more iteration than writing the original model did. Accomplishments that we're proud of Catching a dangerous correctness bug before it ever reached a demo: our system initially matched KRAS G12D patients with G12C-only drugs, which would have been a real wrong recommendation if shown to a clinician or judge unchecked. We're equally proud of how we handled uncertainty, rather than letting the system guess silently, every output is explicitly tagged as either a confirmed database match or a model prediction, so everything is laid out clearly and accurately for the user. What we learned That trustworthy software in biology isn't about the model being right the first time, it's about building in enough friction to catch yourself when it's wrong. The bug that taught us this most clearly wasn't even in our code: a teammate's refactor silently broke our gap-detection logic, and only running the full pipeline end-to-end, instead of trusting that it ran without errors, surfaced it. We learned that "no error thrown" and "correct" are two completely different claims, and biology is exactly the domain where conflating them has real consequences. What's next for Workbench More real training data since drug-screen data would let us build direct mutation-to-drug predictions instead of the current per-pathway fallback. Beyond that, our actual goal is explicit causal inference and dynamic state-transition simulation of resistance evolution over time instead of a single-shot retrieval technique. Today's system reasons over a fixed snapshot of a tumor's pathway state; the version we want to build in the future simulates how that state changes as you intervene. This would allow researchers to accurately screen pathways before running them in the wet-lab, helping solve a billion dollar bottleneck. <div