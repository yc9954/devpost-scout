---
tags:
  - "claim"
confidence: 0.95
evidence: "none"
---

# deterministic software has unit tests, but for agents 'the code did not error' stops being a definition of success: an agent can complete a run, exit clean, and have done exactly the wrong thing confidently

Asserted by [[pact-q8nvkb]] — *Pact*  
<sub>Splunk Agentic Ops Hackathon</sub>

**Problem** observability records that an action happened and never whether it was permitted

**Mechanism** declare a behavioural contract and evaluate every agent run against it in the existing telemetry pipeline  
**Beneficiary** team operating agents in production

**Recurs in** [[financial controls]] [[clinical protocols]] [[industrial safety interlocks]]