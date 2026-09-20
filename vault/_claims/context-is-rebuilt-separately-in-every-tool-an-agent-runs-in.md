---
tags:
  - "claim"
confidence: 0.8
evidence: "none"
---

# context is rebuilt separately in every tool an agent runs in, so the expensive part of agentic work is reconstruction rather than inference

Asserted by [[monolith-z10684]] — *Monolith*  
<sub>TreeHacks 2026</sub>

**Problem** coding agents each maintain their own context and cannot share it

**Mechanism** shared context usable across agents and runtimes  
**Beneficiary** teams running agents in several environments

**Recurs in** [[clinical handover]] [[customer records]] [[research collaboration]]