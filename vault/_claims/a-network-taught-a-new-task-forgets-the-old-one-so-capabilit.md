---
tags:
  - "claim"
confidence: 0.8
evidence: "ablation"
---

# a network taught a new task forgets the old one, so capability is traded rather than accumulated and every deployment is frozen at its training moment

Asserted by [[variable-neural-networks]] — *Variable Neural Networks*  
<sub>AWS Deep Learning Challenge</sub>

**Problem** continual learning fails because training on a new task overwrites prior weights

**Mechanism** swapping parameter sets rather than retraining a single network  
**Beneficiary** anyone deploying a model that must keep learning

**Recurs in** [[personalization]] [[robotics]] [[fraud models]]