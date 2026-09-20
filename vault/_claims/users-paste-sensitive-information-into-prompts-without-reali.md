---
tags:
  - "claim"
confidence: 0.9
evidence: "benchmark"
---

# users paste sensitive information into prompts without realising the data goes to a third-party API

Asserted by [[hbp100-hummingbird-privacy-firewall]] — *hbp100: Hummingbird Privacy Firewall*  
<sub>DSH Hacks V1</sub>

**Problem** the privacy decision is made unconsciously, inside a text box, at the moment of pasting

**Mechanism** a tiny fast local filter intercepting sensitive content before the request leaves  
**Beneficiary** anyone using a model at work

**Recurs in** [[email]] [[support tickets]] [[code sharing]]