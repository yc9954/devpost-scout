---
tags:
  - "claim"
confidence: 0.85
evidence: "benchmark"
---

# we routinely pack contexts with retrieval chunks, massive chat histories and few-shot examples, and you pay for every input token regardless of whether it mattered

Asserted by [[distill-fnk4as]] — *Distill*  
<sub>NexHacks</sub>

**Problem** the cost is charged per token supplied and the value is in a small unidentified subset of them

**Mechanism** small models removing noise from long contexts before inference  
**Beneficiary** anyone paying for long contexts

**Recurs in** [[search]] [[summarisation]] [[archival]]