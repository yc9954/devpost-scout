---
slug: "towerguard-xcpi7u"
url: "https://devpost.com/software/towerguard-xcpi7u"
title: "Towerguard"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 883
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "domain/transportation"
  - "substrate/financial_record"
---

# Towerguard

> TowerGuard quantifies the Cost of Doing Nothing in America's air-traffic-controller staffing crisis.

[Devpost](https://devpost.com/software/towerguard-xcpi7u) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[developer_tools]] [[disaster_emergency]] [[labor_employment]] [[mental_health]] [[transportation]]
**substrate** [[financial_record]]

**stack** anthropic, claude, cloudflare, fastapi, httpx, leaflet.js, lovable, opensky-api, pypdf, pytest, python, react, redis, request

## How they structured the write-up

- inspiration
- what it does
- how we built it
- validation — how we know it isn't just a pretty chart
- responsible ai
- challenges we ran into
- what we learned
- what's next for towerguard

## Body

Inspiration In 2023 a string of near-miss runway incursions put a number most travelers never think about on the front page: the United States is thousands of air- traffic controllers short , and has been for years. The FAA, the GAO (GAO-26-107320), and the National Academies keep issuing the same warning — yet "hire more controllers" never seems to translate into urgency. We wanted to understand why doing nothing feels free when it clearly isn't. That became TowerGuard : a tool that puts a dollar figure and a safety number on every year we wait. What it does TowerGuard is a "Cost of Doing Nothing" simulator for the controller staffing crisis. It projects the Certified Professional Controller (CPC) workforce across five policy scenarios through FY2036 and answers the three questions a policymaker actually asks: How bad does it get? On the do-nothing path, CPCs collapse from ~11,000 to ~2,412 ( −78% ) and staffing stays below the 85% safety floor for the whole horizon. What does waiting cost? On the order of \$365B in controller- attributable delay and overtime versus the current plan — and it is front- loaded and largely irreversible , because the certification pipeline takes 2–3 years. What about safety? Relative fatigue-error risk climbs to ~3.6× the rested baseline — the cost money can't buy back. A second, live pipeline then validates the model against real traffic. How we built it TowerGuard is two decoupled halves that close a loop : a simulator that projects the future, and a live system that checks whether reality is unfolding the way the model assumed. The core is a discrete-time system-dynamics stock-flow model . The crux is the certification lag : hiring grows developmentals $D$, but CPCs only grow after a delay $\tau$: $$\mathrm{CPC} {t+1} = \mathrm{CPC}_t + p\,D {t-\tau} - a_t\,\mathrm{CPC}_t$$ where $\tau \approx 2\text{–}3$ years, $p$ is the OJT pass rate, and $a_t$ is attrition. The do-nothing collapse is driven by a reinforcing burnout loop — understaffing forces overtime, overtime raises attrition, attrition deepens the gap: $$a_t = a_0\left(1 + \beta\,\max!\bigl(0,\;1 - s_t\bigr)\right), \qquad s_t = \frac{\mathrm{CPC}_t}{\mathrm{CPC}^{\text{target}}}$$ A Monte Carlo wrapper samples uncertain parameters to produce $P_{10}\text{–}P_{90}$ confidence bands instead of false-precision points. The cost of delay compares starting a plan in year $y$ against starting in 2026: $$\Delta C(y) = \sum_{t}\left(C_t^{\,\text{start }y} - C_t^{\,\text{start }2026}\right)$$ The live half streams ADS-B traffic into three deterministic risk modules (traffic density, conflict geometry, workload index) over Redis . When risk escalates, Claude ( claude-opus-4-8 ) phrases the advisory and the shift briefing — but never decides escalation (we call this Option B). The deterministic engine owns every decision; the LLM only turns structured evidence into readable text, with a template fallback. A human controller confirms every alert. Stack: Python (pure-stdlib SD model), FastAPI + SSE, Redis, the Anthropic SDK, OpenSky, pypdf; a React / Vite / Tailwind / shadcn dashboard built with Lovable; 304 tests guard two frozen contracts that keep the halves decoupled. Validation — how we know it isn't just a pretty chart Out-of-sample backtest (FY2020–2025): the model under-predicts CPC with a MAPE of 7.91% , breaching our own 5% threshold. We show this honestly — the drift monitor is catching the COVID structural break, and a model that flags its own failure mode is more credible than a fake-perfect one. Extreme-condition tests: a one-year hiring flood does not raise next- year CPC — the model respects the certification lag. Reproduction with honesty tiers: every check is labeled IN-SAMPLE vs. INDEPENDENT, so a tight fit is never dressed up as predictive skill. Responsible AI The AI phrases; it never decides. Escalation is deterministic and auditable; a human confirms every advisory. Fail-safe: missing data shows DEGRADED, never a fake "LOW". Honest about its limits: confidence bands, an assumption ledger with per-parameter confidence, explicit "model-void" conditions, and a drift monitor that self-flags when the model is stale. Challenges we ran into Keeping the two halves decoupled. We froze a JSON contract and a Redis contract so each half could be built independently — guarded by 304 tests. Calibrating with thin public data. Controller counts mix CPCs, developmentals, and trainees under inconsistent definitions; we solved hiring to historical endpoints and pinned the CPC split with OJT washout. The burnout-loop coefficients remain illustrative, so we report collapse depth and cost as order-of-magnitude, not point predictions . Wiring a live LLM without letting it "drive." Choosing augmentation over automation took several iterations plus a full template-fallback path. Streaming a local engine to a cloud dashboard. Free tunnels buffer SSE, so the always-on dashboard replays a real captured session (real Claude output, re-sequenced for timing) while the live engine runs in our demo video as proof the agent is real. What we learned The crisis isn't "knowing what to do" — it's that the fix takes years to land, so delay compounds before it can be reversed. That reframing is the whole project. Honest uncertainty (bands, a self-breaching backtest, confidence tiers) persuades decision-makers more than confident point estimates. The right division of labor for safety-critical AI: let deterministic logic decide, let the language model communicate. What's next for TowerGuard Calibrate the burnout-loop coefficients against facility-level attrition data. Run live OpenSky end-to-end (currently demo / replay). Per-facility scenarios so a region can model its own staffing path. <div