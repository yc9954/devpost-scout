---
tags:
  - "claim"
confidence: 0.75
evidence: "none"
---

# deploying a contract requires exposing a private key on the deploying machine, so the most privileged operation in the lifecycle has the weakest handling

Asserted by [[nairobi]] — *Nairobi*  
<sub>EthCC Hack 2022</sub>

**Problem** multi-contract deployment is complex and requires exposing keys

**Mechanism** a deployment tool that executes without exposing private keys  
**Beneficiary** teams deploying production contracts

**Recurs in** [[cloud credentials]] [[signing keys]] [[CI secrets]]