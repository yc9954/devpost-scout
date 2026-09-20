---
tags:
  - "claim"
confidence: 0.8
evidence: "concrete-instance"
---

# an AI context system is trusted only if its ontology, documentation and indexer are verified, so the value of the whole depends on tests nobody writes for infrastructure

Asserted by [[hardening-gitlab-orbit-schema-docs-code-graph-tests]] — *Hardening GitLab Orbit: schema, docs & code-graph tests*  
<sub>GitLab Transcend Hackathon</sub>

**Problem** a knowledge graph's promise fails silently if its schema or indexing is wrong

**Mechanism** schema guardrails, documentation and code graph test coverage, finding a real data-loss bug  
**Beneficiary** everyone relying on the system's context being truthful

**Recurs in** [[search indexes]] [[data pipelines]] [[clinical registries]]