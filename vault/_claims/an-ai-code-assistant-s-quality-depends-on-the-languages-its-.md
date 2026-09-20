---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# an AI code assistant's quality depends on the languages its indexer can parse, so a missing language parser silently excludes entire codebases from assistance

Asserted by [[gitlab-orbit-kotlin-ast-indexing-devex-5-contributions]] — *GitLab Orbit: Kotlin AST Indexing & DevEx (4 Merged)*  
<sub>GitLab Transcend Hackathon</sub>

**Problem** a code knowledge graph lacked Kotlin parsing and associated tooling

**Mechanism** contributing Kotlin AST parsing, storage tooling and pipeline fixes upstream  
**Beneficiary** teams whose code is in an unindexed language

**Recurs in** [[search indexing]] [[static analysis]] [[documentation generation]]