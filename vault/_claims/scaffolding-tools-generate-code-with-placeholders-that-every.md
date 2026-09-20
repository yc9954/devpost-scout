---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# scaffolding tools generate code with placeholders that every later change has to find and update, so the template's convenience becomes the project's maintenance burden

Asserted by [[ast-walking-around-starport]] — *(AST)Walking around starport*  
<sub>Cosmos HackAtom VI </sub>

**Problem** blockchain scaffolding relies on placeholder strings throughout the generated code

**Mechanism** manipulating the abstract syntax tree directly instead of substituting text  
**Beneficiary** developers maintaining generated projects

**Recurs in** [[code generation]] [[configuration management]] [[refactoring tools]]