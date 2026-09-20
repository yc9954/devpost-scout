---
tags:
  - "claim"
confidence: 0.9
evidence: "benchmark"
---

# tests check the contract you wrote down, not the one you actually had, so a replacement can pass everything and still break what depended on the original

Asserted by [[karma-the-reincarnation-agent-for-deprecated-services]] — *Karma — The Reincarnation Agent for Deprecated Services*  
<sub>Google Cloud Rapid Agent Hackathon</sub>

**Problem** undocumented dependencies are invisible to every gate designed to catch regressions

**Mechanism** learn the retired service's observed behaviour and assert it against the replacement  
**Beneficiary** migration team

**Recurs in** [[regulatory transitions]] [[supplier substitution]] [[staff handover]]