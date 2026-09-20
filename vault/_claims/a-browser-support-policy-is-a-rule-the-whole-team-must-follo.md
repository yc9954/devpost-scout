---
tags:
  - "claim"
confidence: 0.8
evidence: "concrete-instance"
---

# a browser support policy is a rule the whole team must follow and no tool enforces it, so compliance depends on individual memory and fails silently

Asserted by [[eslint-plugin-baseline-js]] — *eslint-plugin-baseline-js*  
<sub>Baseline Tooling Hackathon</sub>

**Problem** static analysis tools cannot reliably enforce JavaScript baseline browser support

**Mechanism** a lint rule enforcing availability by year with type-aware API checks  
**Beneficiary** teams with a stated support policy nobody can check

**Recurs in** [[accessibility standards]] [[security policy]] [[API deprecation]]