---
tags:
  - "claim"
confidence: 0.6
evidence: "none"
---

# model inference reuses computed prefill state and recomputing it wastes GPUs, so the cost is redundant computation rather than the model size

Asserted by [[pliops-challenge-1-lower-the-infrastructure-costs]] — *Pliops Challenge #1 - Lower the infrastructure Costs*  
<sub>DeveloperWeek 2025 Hackathon</sub>

**Problem** inference recomputes prefill or decode state, using more GPUs than necessary

**Mechanism** reducing GPUs used by reusing computed state  
**Beneficiary** teams running inference at scale

**Recurs in** [[caching]] [[batch processing]] [[distributed compute]]