---
tags:
  - "claim"
confidence: 0.7
evidence: "none"
---

# an AI context system's value depends on its extraction being correct and untested extraction regresses silently, so the reliability is a test-coverage problem

Asserted by [[gitlab-orbit-code-graph-test-fixtures]] — *GitLab Orbit code-graph test fixtures*  
<sub>GitLab Transcend Hackathon</sub>

**Problem** code-graph extraction can regress without being caught

**Mechanism** integration fixtures locking in the extraction so regressions fail CI  
**Beneficiary** everyone relying on the context being correct

**Recurs in** [[search indexing]] [[parsers]] [[data pipelines]]