---
tags:
  - "claim"
confidence: 0.7
evidence: "none"
---

# secrets are stored in a file that lives beside the code and is excluded by convention, so a single mistake exposes everything and the protection is a habit rather than a mechanism

Asserted by [[pronoobs]] — *DotCloud*  
<sub>The Postman API Hack</sub>

**Problem** every project creates an environment file and worries about accidentally committing it

**Mechanism** storing the environment securely outside the repository  
**Beneficiary** developers relying on convention to protect credentials

**Recurs in** [[configuration management]] [[key rotation]] [[backups]]