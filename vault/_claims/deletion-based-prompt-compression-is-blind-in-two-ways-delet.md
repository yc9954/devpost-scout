---
tags:
  - "claim"
confidence: 0.9
evidence: "ablation"
---

# deletion-based prompt compression is blind in two ways deletion structurally cannot fix: it cannot read your question and it cannot rewrite

Asserted by [[re-compress]] — *Re:Compress*  
<sub>UC Berkeley AI Hackathon 2026</sub>

**Problem** the compressor does not know what the compressed text is going to be asked

**Mechanism** query-aware rewriting distilled into a small model and carried across turns  
**Beneficiary** anyone running long multi-turn contexts

**Recurs in** [[summarisation]] [[retrieval]] [[transcript archives]]