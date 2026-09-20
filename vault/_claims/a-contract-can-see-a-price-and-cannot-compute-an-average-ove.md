---
tags:
  - "claim"
confidence: 0.7
evidence: "concrete-instance"
---

# a contract can see a price and cannot compute an average over it, so strategies that depend on history are impossible on chain without an external computation step

Asserted by [[chainlink-technical-indicators]] — *Chainlink Technical Indicators*  
<sub>Chainlink Fall 2022 Hackathon</sub>

**Problem** technical indicators cannot be calculated by contracts directly

**Mechanism** an external adapter and keepers computing indicators for on-chain consumption  
**Beneficiary** developers building history-dependent strategies

**Recurs in** [[insurance triggers]] [[supply chain thresholds]] [[energy pricing]]