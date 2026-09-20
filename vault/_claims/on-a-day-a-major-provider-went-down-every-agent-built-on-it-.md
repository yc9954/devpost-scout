---
tags:
  - "claim"
confidence: 0.95
evidence: "concrete-instance"
---

# on a day a major provider went down, every agent built on it stopped — and the specific failure nobody handles is credit_balance_too_low, an HTTP 400 that every gateway passes through as a normal error

Asserted by [[aegis-a-resilient-ai-agent-runtime]] — *Aegis — A Resilient AI Agent Runtime*  
<sub>DevNetwork [AI + ML] Hackathon 2026</sub>

**Problem** agent runtimes treat provider failure as an exception when it is a certainty, and one of the certainties looks like a client error

**Mechanism** hedged parallel requests with fallback, verified continuously by chaos injection  
**Beneficiary** anyone whose product depends on a model provider

**Recurs in** [[payment processors]] [[identity providers]] [[mapping services]]