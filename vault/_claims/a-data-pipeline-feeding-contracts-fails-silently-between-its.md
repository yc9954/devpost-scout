---
tags:
  - "claim"
confidence: 0.75
evidence: "none"
---

# a data pipeline feeding contracts fails silently between its stages, so the developer debugging it has no view of where the value was lost

Asserted by [[chainwiz]] — *Oriviz*  
<sub>Chainlink Fall 2022 Hackathon</sub>

**Problem** contract developers cannot trace a failure across the off-chain to on-chain pipeline

**Mechanism** an end-to-end debugger for the oracle pipeline  
**Beneficiary** developers building data-dependent contracts

**Recurs in** [[ETL pipelines]] [[IoT ingestion]] [[microservice traces]]