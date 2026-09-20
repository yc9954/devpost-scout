---
tags:
  - "claim"
confidence: 0.85
evidence: "benchmark"
---

# large models are outgrowing conventional infrastructure — hundreds of gigabytes, far past what a single GPU container can hold

Asserted by [[commissure]] — *Commissure*  
<sub>Cloud Run Hackathon</sub>

**Problem** the serving unit is a container and the model no longer fits in one

**Mechanism** slice the model into GPU microservices and stream activations between them  
**Beneficiary** anyone serving a model too large for one machine

**Recurs in** [[scientific simulation]] [[video processing]] [[genomics]]