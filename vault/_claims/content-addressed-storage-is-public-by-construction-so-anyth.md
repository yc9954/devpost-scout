---
tags:
  - "claim"
confidence: 0.7
evidence: "concrete-instance"
---

# content-addressed storage is public by construction, so anything sensitive has to be encrypted before it is pinned and there is no standard step for doing that

Asserted by [[encryption-pinner]] — *Encryption Pinner*  
<sub>Chainlink Spring 2022 Hackathon</sub>

**Problem** IPFS is used in nearly every project and encrypting before pinning is manual

**Mechanism** encrypting a file with a chosen method and pinning it in one operation  
**Beneficiary** developers storing anything non-public on IPFS

**Recurs in** [[object storage]] [[backups]] [[public datasets]]