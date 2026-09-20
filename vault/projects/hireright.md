---
slug: "hireright"
url: "https://devpost.com/software/hireright"
title: "HireUp"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 661
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# HireUp

> Match with the best applicants, powered by AI agents and TikTok's recommendation algorithm.

[Devpost](https://devpost.com/software/hireright) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** fastapi, html, numpy, openai, python, react, sqlite, typescript

## How they structured the write-up

- motivation
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hireup

## Body

Motivation Imagine you’re a recruiter at a startup trying to hire a great engineer. You open applications expecting ~100 relevant candidates, but instead you see over 2,000. How do you pick out who to interview, and how can you be sure you didn't miss the best candidates? The modern job application pipeline is a lose-lose for everyone involved. Job seekers have to constantly spam apply just to have a shot, while recruiting teams have to sift through thousands of applications, when most are jut noise. In an ideal world, candidates only apply for exactly what they're qualified and a good match for, and recruiters always have high signal results. While hiring for some student led clubs, we realized how dire the situation has become, and wanted to set out and change the status quo has become. After speaking to many experienced recruiters, we realized we had just the right combination of experience and insight to change things for the better. What it does HireUp turns hiring from a volume game into a quality and fit game. We do this in three steps: Scarcity + targeting: candidates see a limited number of highly curated roles per day and can only apply to a small number. This reduces spam, increases intent, and improves signal for both sides. Two-tower matching + feedback loops: we use a two-tower model that learns from outcomes on both sides (interest, interviews, feedback, etc.) to recommend jobs candidates want and jobs that are likely to want them back. AI recruiting assistant lets teams interactively search and shortlist candidates based on a more intimate understanding of each applicant's profile, bringing more confidence and efficiency in your results. How we built it Candidate user flow: sign up → upload resume + interests → receive a daily set of matched roles → apply → get offers Company user flow: create a posting → receive a smaller, higher-signal candidate set → use the recruiter assistant to query and compare → select interviews → submit feedback Under the hood: We represent jobs and candidates as embeddings in a two-tower setup. We update embeddings from real interactions (apply, interview, offer, feedback), and use those signals to improve future matching. We built multimodal AI agents to help recruiting teams analyze applicants, compare strengths, all to ensure the best matches based on any relevant criteria. Challenges we ran into Two-sided objectives: optimizing for “what candidates want” alone isn’t enough; the model also needs to learn “what companies will say yes to.” Keeping recommendations stable: making sure updates don’t drift or collapse required careful normalization and conservative update steps. Signal quality: recruiter feedback can be messy or inconsistent, so we designed the system to learn from multiple signals rather than a single label. Accomplishments that we're proud of We were able to build an end-to-end demo of a scarcity-based applications portal that incorporates the two-tower model for the highest quality matches Implemented a dynamic two-way learning system that collects feedback from candidate and company actions. Built a power interactive recruiting assistant that can summarize, evaluate, and index on any criteria of your choosing, all with great visual tools to help recruiters. Grounded the product in real workflows by speaking with recruiters early and iterating from their feedback. What we learned The biggest lever in hiring is incentives : when applying is free, spam is rational; scarcity changes behavior and improves signal. Hiring matching is inherently two-sided , and systems work better when they learn from both sides’ outcomes. AI assistants are most valuable when the funnel is already high-signal —reducing noise first makes everything downstream faster and more reliable. What's next for HireUp Improve our resume and job encoders with models that train on more real world interactions and context. Improve and iterate the interactive recruiting assistant by working closely with recruiters. Add in better offline evaluation metrics to verify user integrity. Ship product to the real world, starting with smaller startups, and slowly growing from there! <div