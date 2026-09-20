---
tags:
  - "claim"
confidence: 0.9
evidence: "concrete-instance"
---

# a change that passes every test can still be catastrophic because the test environment differs from production in the one dimension that matters, which is scale

Asserted by [[time-traveler-w3cxp0]] — *Time-Traveler*  
<sub>GitLab AI Hackathon</sub>

**Problem** validation runs against data that does not resemble the data it will meet

**Mechanism** preview migrations against isolated clones of real production data before merge  
**Beneficiary** engineer shipping a schema change

**Recurs in** [[clinical protocol rollout]] [[policy changes]] [[structural load testing]]