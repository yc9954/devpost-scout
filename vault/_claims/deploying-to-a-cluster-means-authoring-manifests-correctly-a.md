---
tags:
  - "claim"
confidence: 0.65
evidence: "none"
---

# deploying to a cluster means authoring manifests correctly and the errors are found in production, so the operational risk is concentrated in a configuration format

Asserted by [[devtool-api]] — *DevTool API*  
<sub>Cloud Native Hackathon</sub>

**Problem** writing Kubernetes manifests for production is error-prone and painful

**Mechanism** an API service handling the manifest generation  
**Beneficiary** developers deploying without platform expertise

**Recurs in** [[cloud templates]] [[CI configuration]] [[network policy]]