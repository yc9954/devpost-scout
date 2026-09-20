---
slug: "altiverse"
url: "https://devpost.com/software/altiverse"
title: "AltiVerse"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1454
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# AltiVerse

> AltiVerse: AI-powered simulations that let students fork decisions into living alternate realities with 1,000 of personalities to explore second-order effects and complex systems in STEM and education

[Devpost](https://devpost.com/software/altiverse) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[multi_agent]] [[simulation_digital_twin]]
**domain** [[climate_energy]] [[education]] [[health_clinical]] [[mental_health]] [[scientific_research]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** css, javascript, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i faced
- what i learned

## Body

Inspiration STEM education is great at teaching facts and terrible at teaching systems . Students learn Newton's laws, then meet the real world — classrooms, ecosystems, economies, epidemics — where nothing has a single clean answer and everything has second-order effects . Ban phones to raise focus, and conflict moves to the hallway. Change one variable in a complex system and three others you weren't watching shift too. That intuition — that systems push back — is the heart of biology, economics, climate science, and engineering, and almost no classroom tool lets you feel it. The other gap is the scientific method as a verb . Textbooks describe controlled experiments; students rarely get to run one. What does it actually mean to "hold variables constant," "change one thing," and "measure the difference"? You need a reproducible world to even ask. AltiVerse was built to make both tangible. The metaphor is simple enough for a 13-year-old: fork a decision the way you fork a git branch , and watch the alternate worlds drift apart. Underneath, the student is doing real computational science — running a controlled experiment on an agent-based model and interpreting the data it produces. And it had to be accessible to anyone : free, no account, no install friction, and runnable fully offline on a low-end laptop — because the students who most need ambitious tools are the least likely to have a paid API key or a fast connection. What it does A student takes one decision — a school phone ban, 8- vs 12-hour shifts, a 4-day week — and forks it into 2–4 alternate realities . Each becomes a small living world of up to ~1,000 simulated people with personalities, moods, friendships, and rivalries, who move through rooms and react to the policy. The student then does science on it : Hypothesize — "I think banning phones raises focus but increases conflict." Run a controlled experiment — the same seed produces a byte-identical world, so the only difference between two realities is the policy. That's a textbook controlled variable, made real. Observe & measure — live metrics (0–100), trend sparklines, a divergence tree showing the exact day the worlds split, a wellbeing histogram (distribution, not just the average), and per-reality causal chains ( rule → consequence → second-order effect ). Interrogate — click any single person to see how that individual fares across every timeline, then ask them questions in character. Conclude — export a report with a recommendation, and Reseed to test whether the result was robust or just one lucky world. The pedagogical core: every number is deterministic; only the prose is AI. The simulation is a seeded engine (same seed → identical world, every time), which is what makes it a legitimate experimental instrument. An optional LLM layer — any OpenAI-compatible endpoint, local (Ollama, LM Studio, llama.cpp) or online (OpenAI, Groq, …) — only narrates : in-character thoughts, interviews, headlines, the final report. Turn the model off and the science still works. Why this fits AI × STEM Education: the AI lowers the barrier to expressing an idea (type "a hospital choosing between 8- and 12-hour nursing shifts" and it builds the cast, metrics, and environment), while the deterministic engine teaches the discipline of experimentation. AI for accessibility, real math for rigor. How I built it Stack: Vite + React + TypeScript, no backend, no build step required to run ( npx github:LeoTheAIDev/Altiverse boots it). State lives in localStorage . The heart is a tiny deterministic engine. Every world is driven by a Mulberry32 PRNG , and each branch runs on a derived seed ($\text{seed} + i \cdot 1013$) so realities stay independent yet reproducible — the formal basis of the "controlled experiment." Each metric (Focus, Stress, Trust, … on a 0–100 scale) evolves by exponential relaxation toward a per-reality attractor , plus noise — a first-order linear dynamical system students can actually reason about. For metric $k$ on day $t$: $$ m_k(t+1) = \mathrm{clamp}_{[0,100]}!\Big( m_k(t) + \alpha\,\big(a_k - m_k(t)\big) + \xi_t \Big), \qquad \alpha = 0.09 $$ where $a_k$ is the reality's attractor and $\xi_t$ is roughly-normal noise (a sum of three uniforms, centered, scaled by $1.3$). A policy's causal chain injects discrete "kicks" on scripted days — the same pull with a larger coefficient $\kappa$: $$ m_k \leftarrow \mathrm{clamp}!\big( m_k + \kappa\,(a_k - m_k) \big), \qquad \kappa \in {0.16,\,0.22,\,0.28} $$ so "policy enacted" lands a hard shove and its ripples land softer ones. Divergence — the headline lesson, when do the worlds split? — is the average spread across branches, normalized to $[0,1]$: $$ D(t) = \frac{1}{100\,|K|} \sum_{k \in K} \Big( \max_b\, m_k^{b}(t) \;-\; \min_b\, m_k^{b}(t) \Big) $$ The worlds are declared to have "split" on the first day $D(t) \ge 0.16$, and the top drivers are the metrics with the largest final gap — teaching students to attribute an effect to its causes. People are the other half — a hands-on intro to agent-based modeling . A persona has fixed traits in $[0,1]$ ( stressProne , ruleProne , burnoutProne ) and the same persona exists in every reality . Whether they're visibly stressed on a day is a threshold against a metric-derived pressure score $s$, direction-aware via a "badness" function $\beta(m, v) = v/100$ if lower-is-better else $1 - v/100$: $$ \text{stressed} \iff \text{stressProne} \le s, \qquad s = \beta(m_{\text{stress}}, v) $$ That's why the anxious overachiever cracks under a policy the weary veteran shrugs off — identical world, different individual. The social layer is a bounded random walk on pairwise affinity, seeded from an FNV-1a hash of each id-pair, drifting in $[-1,1]$ as people bond, clash, or pass rumours that spread through co-located agents and decay once everyone's heard them. Popularity emerges as $\mathrm{clamp}(50 + 14\,(\text{pos}-\text{neg}))$, summarized in $O(\text{interactions})$ — not $O(n^2)$ — so it stays smooth at ~1,000 agents. The LLM client is deliberately dependency-light: plain fetch against /chat/completions , a timeout, and jsonrepair to salvage the malformed JSON small local models love to emit. The engine never depends on it — so a student with no key, no internet, and a slow laptop gets the full experience. Challenges I faced Determinism vs. life. A reproducible engine (needed for controlled experiments) and a world that feels alive (needed to engage a 13-year-old) pull in opposite directions. The fix was to push all randomness through seeded PRNGs derived from one master seed — so "Reseed" explores a genuinely new world while a shared seed is bit-for-bit identical. Trusting a small model with structure. Local 3B models cheerfully return broken JSON. Instead of threatening the prompt, I made the parser forgiving: slice to the matching brace, jsonrepair , retry once. Robustness at the boundary beat strictness in the prompt — essential when the target user is running whatever tiny model fits on their machine. 1,000 agents at 60fps in a browser. Per-frame React re-renders die at that scale. Agent motion is spring-physics written straight to the DOM , outside React's render loop — so it runs on a Chromebook, not just a gaming laptop. The zero-backend, accessibility-first constraint. No server meant the browser talks directly to the model (hence CORS and the OLLAMA_ORIGINS=* note) and the API key lives only in localStorage , sent only to the provider the student picked. Every "make it private and free" decision had a real engineering cost to pay. Teaching, not predicting. The honest framing — this models second-order dynamics, it does not predict the future — had to be enforced by the architecture (deterministic mechanics, AI only narrates), not just claimed in the copy. A STEM tool that pretends to be an oracle teaches the wrong lesson. What I learned Separating mechanism from narration was the whole game. Numbers from a deterministic engine, language from the LLM: more honest, more debuggable, and pedagogically correct — the model can never silently invent a statistic, so students learn to trust the data, not the prose. Simple math, well-composed, reads as emergence. There's no agent "AI" here — just relaxation toward attractors, threshold flags, and a bounded affinity walk. Layered together they produce rivalries and rumours that feel authored. That is the lesson of complex systems, and it's cheaper to build than it looks. Accessibility is an architecture decision, not a feature. "Runs offline on any laptop with no account" isn't a checkbox you add later — it's what forced local-first, determinism, and a dependency-light client, which turned out to be the best parts of the project. Lowering the barrier and raising the rigor aren't opposites. AI handles the messy part (turn a sentence into a full scenario); the engine enforces the disciplined part (controlled, reproducible, measurable). That balance is exactly what AI × STEM education should be. <div