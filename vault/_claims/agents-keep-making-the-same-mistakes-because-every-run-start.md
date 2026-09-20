---
tags:
  - "claim"
confidence: 0.9
evidence: "none"
---

# agents keep making the same mistakes because every run starts from a clean slate: no memory of the last failure, no feedback loop, no learning, and you watch it repeat the exact error you rejected yesterday

Asserted by [[autopsy-zq5d84]] — *Autopsy*  
<sub>LA Hacks 2026</sub>

**Problem** the corrective information exists in the previous session and is discarded at its boundary

**Mechanism** record every action, diagnose the failures into a graph and inject that into the next attempt  
**Beneficiary** developer supervising an agent

**Recurs in** [[clinical handover]] [[manufacturing defects]] [[incident response]]