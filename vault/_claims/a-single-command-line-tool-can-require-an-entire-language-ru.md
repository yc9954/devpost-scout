---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# a single command-line tool can require an entire language runtime, so a heavy dependency is installed permanently for an occasional need

Asserted by [[box-81khm9]] — *box*  
<sub>Go Hack</sub>

**Problem** running a Java-based CLI tool meant introducing a Java runtime into the development environment

**Mechanism** a container-first command runner  
**Beneficiary** developers avoiding permanent dependencies

**Recurs in** [[build toolchains]] [[CI images]] [[scientific software]]