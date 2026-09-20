---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# a secure cross-chain protocol is bounded by the slowest chain's finality, so security and speed are traded against each other unless someone fronts the capital

Asserted by [[ccip-fast-bridge]] — *Chronomancer*  
<sub>Block Magic: A Chainlink Hackathon</sub>

**Problem** CCIP transfers are slow because source chains take long to reach settlement

**Mechanism** an order-filling bot fronting the transfer against a contract endpoint  
**Beneficiary** users needing fast settlement without weaker security

**Recurs in** [[payment settlement]] [[clearing houses]] [[cross-border transfer]]