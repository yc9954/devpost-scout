---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# generated code is edited by text substitution into placeholders, so every later change is string manipulation on a structured artifact and breaks unpredictably

Asserted by [[code-scaffolding-in-starport-with-ast-analysis-and-mutation]] — *Code Scaffolding in Starport with AST Analysis and Mutation*  
<sub>Cosmos HackAtom VI </sub>

**Problem** scaffolding relies on placeholder markers throughout the generated code

**Mechanism** parsing, querying and mutating the syntax tree to insert new definitions  
**Beneficiary** developers maintaining scaffolded projects

**Recurs in** [[refactoring tools]] [[migrations]] [[configuration management]]