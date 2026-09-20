---
tags:
  - "claim"
confidence: 0.9
evidence: "none"
---

# teams now ship in hours and nobody fully understands what they built, so a reviewer sees changed lines and not that this change ripples through three subsystems they did not know were connected

Asserted by [[graphdev]] — *GraphDev*  
<sub>GitLab AI Hackathon</sub>

**Problem** review operates on a diff while risk lives in the dependency structure the diff does not show

**Mechanism** semantic graph of the codebase giving each change an impact analysis  
**Beneficiary** reviewer on a fast-moving codebase

**Recurs in** [[regulatory change]] [[supply chain]] [[clinical protocol updates]]