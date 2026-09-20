---
tags:
  - "claim"
confidence: 0.8
evidence: "none"
---

# semantic code search returns an isolated snippet, so the assistant answers with a fragment while the developer needs the call graph around it

Asserted by [[washedmcp]] — *WashedMCP*  
<sub>NexHacks</sub>

**Problem** search returns one snippet and requires several follow-up searches to find callers and callees

**Mechanism** returning the function with its callers and callees in one token-efficient result  
**Beneficiary** developers and agents working on real repositories

**Recurs in** [[legal citation]] [[scientific literature]] [[dependency analysis]]