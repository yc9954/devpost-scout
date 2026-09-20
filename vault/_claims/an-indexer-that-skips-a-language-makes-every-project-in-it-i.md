---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# an indexer that skips a language makes every project in it invisible to the assistance built on top, so the exclusion is total rather than partial

Asserted by [[merged-mr-feat-code-graph-add-elixir-language-support]] — *Merged MR: feat(code-graph): add Elixir language support*  
<sub>GitLab Transcend Hackathon</sub>

**Problem** Elixir files were skipped entirely by the code indexer

**Mechanism** adding language support to the indexer upstream  
**Beneficiary** teams whose codebase was excluded

**Recurs in** [[search coverage]] [[static analysis]] [[documentation tooling]]