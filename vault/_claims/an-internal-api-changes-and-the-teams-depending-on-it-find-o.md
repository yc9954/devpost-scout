---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# an internal API changes and the teams depending on it find out when something breaks, so the coordination failure is announcement rather than versioning

Asserted by [[syncup-dmi15k]] — *SyncUp*  
<sub>Codegeist 2022</sub>

**Problem** developers have no reliable way to learn about internal API changes

**Mechanism** change notification to the teams that consume the API  
**Beneficiary** teams whose integrations break silently

**Recurs in** [[database schemas]] [[configuration]] [[regulatory changes]]