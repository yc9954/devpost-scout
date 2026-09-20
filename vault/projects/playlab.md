---
slug: "playlab"
url: "https://devpost.com/software/playlab"
title: "PlayLab"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 756
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/education"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# PlayLab

> A tower defense where the weapon is a math function you write and a deterministic engine proves every AI generated wave is beatable before you play it.

[Devpost](https://devpost.com/software/playlab) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[education]]
  <sub>weak: educator_student</sub>
**substrate** [[financial_record]] [[geospatial]]

**stack** canvas, es-modules, featherless-ai, html5, javascript, node.js, qwen2.5, render, vercel

## Body

Inspiration Two things that didn't fit together kept bothering me. First: 272 million children are out of school (UNESCO). Even in classrooms, math is taught as symbol-pushing, a student can solve ( a\sin(bx) ) on paper but cannot tell you what it looks like in the world. Second: everyone is rushing to generate education with LLMs, and nobody talks about the obvious failure mode. A hallucinated level is an unbeatable level. A kid who loses to a broken level doesn't learn math — they learn to quit. I wanted the AI's creativity, but I never wanted to hand it the truth. Archimedes defended Syracuse with mathematics. That felt like the right hero. What it does It's a tower defense where the cannon has no aim button. You write the function, and the shell flies along your graph. Shape a curve with sliders or type a formula like ( 0.5 - 0.05(x-6)^2 ), and the trajectory is the function. One parabola can solve three enemies at once. Enemies move along curves drawn from real phenomena. To hit a flock of geese pinned to a sine wave, you have to understand a sine wave. Understanding is the win condition. Type any topic and an LLM themes the next wave around it. But before a wave reaches you, a deterministic verifier, the same engine that runs in your browser, simulates thousands of shots and proves at least one function beats it. Failed generations are rejected and retried; non-phenomena like my homework deadline get an honest refusal. Every verify and reject is written to a public Proof Ledger you can watch live. How we built it Solo, in vanilla JavaScript with HTML5 Canvas — ES modules, no framework, no build step. The key decision was one shared engine. The same curve-sampling, physics, and collision code runs the game in the browser and the verifier on a Node backend. There is exactly one definition of "this shot hits", so the proof on the server is a proof about the real game, not about a model of it. Math input goes through my own safe expression compiler : tokenizer → recursive-descent parser → closure tree, no eval. It doubles as the gate for LLM output: anything the parser rejects never reaches a player. Frontend on Vercel, verifier backend on Render. Works on a phone, no sign-up. Challenges we ran into The biggest one became the thesis of the whole project. I started by asking the LLM to generate full levels: coordinates, parameters, win conditions. It failed almost every time. Small models are confident and wrong about geometry, and nearly every generated level was unbeatable or degenerate. Instead of reaching for a bigger model and hoping, I inverted the architecture. The LLM only proposes the theme and the law a phenomenon follows; my deterministic code computes everything that must be correct; the verifier has the final word. The flaw stopped being a bug and became the design. A smaller but real one: a free-tier backend that falls asleep. I had to make generation so a cold start never blocks the gameplay loop, if the server is slow or down, the client falls back to offline generation running the same proof. Accomplishments that we're proud of No unbeatable level can ever reach a player, by construction, not by hope. The Proof Ledger shows this publicly, including the rejections. The same prompt box that makes geese also says, honestly, "this is not a phenomenon I can model", and I think the refusal demos better than the success. One engine, two jobs, zero drift between what is verified and what is played. It's live, it runs on a phone, and a stranger can play it in ten seconds with no account. What we learned The right question for AI in education is not "how good is the model" — it's "what is the model allowed to decide". The moment I limited the LLM to creative choices and gave deterministic code authority over correctness, a 7B model became reliable enough to ship. Also: building the verifier first made every other feature cheaper. I could let the AI be wild because the gate was strict. What's next for PlayLab Hyperbolas and damped sines as weapons. Intercept missions where you solve ( f(x) = g(x) ). Shielded enemies keyed to slope is a quiet way into derivatives. And a classroom mode where one topic builds the same verified wave for a whole class, turning the understanding map into a live picture of what the room is confused about. <div