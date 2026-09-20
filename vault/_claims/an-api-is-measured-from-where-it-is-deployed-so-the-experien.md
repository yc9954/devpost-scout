---
tags:
  - "claim"
confidence: 0.75
evidence: "self-measurement"
---

# an API is measured from where it is deployed, so the experience of distant users is invisible to exactly the people responsible for it

Asserted by [[global-api-network-test]] — *Global API Network Information*  
<sub>The Postman API Hack</sub>

**Problem** front-end logs did not reveal how latency and DNS behaved for customers far from the data centres

**Mechanism** measuring latency, DNS and connectivity to the API from many global locations  
**Beneficiary** teams serving users outside their deployment regions

**Recurs in** [[CDN configuration]] [[video delivery]] [[game servers]]