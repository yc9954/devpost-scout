---
tags:
  - "claim"
confidence: 0.95
evidence: "none"
---

# detection rules go stale — an attacker changes one field, a different IP, a new region, a slight timing variation, and a rule that caught them yesterday misses them completely, and nobody knows

Asserted by [[argus-p4davt]] — *ARGUS*  
<sub>Splunk Agentic Ops Hackathon</sub>

**Problem** the decay of a defensive rule is silent and only the attacker measures it

**Mechanism** one agent invents variant attacks, another repairs the rule, and the improvement is proven live  
**Beneficiary** security team relying on rules they wrote once

**Recurs in** [[fraud rules]] [[content policy]] [[quality inspection]]