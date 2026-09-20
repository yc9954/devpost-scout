---
tags:
  - "claim"
confidence: 0.8
evidence: "concrete-instance"
---

# a pretrained model is unusable when the architecture differs in trivial ways, so capability is lost to naming and wrapping rather than to incompatibility

Asserted by [[torchliberator-partial-weight-loading]] — *TorchLiberator - Partial Weight Loading*  
<sub>PyTorch Annual Hackathon 2021</sub>

**Problem** loading a state dict fails when a model was saved with or without a wrapper or with small structural differences

**Mechanism** finding the maximum correspondence between two networks' weights automatically  
**Beneficiary** researchers reusing pretrained weights

**Recurs in** [[schema migration]] [[API versioning]] [[config compatibility]]