---
tags:
  - "claim"
confidence: 0.75
evidence: "concrete-instance"
---

# content-addressed storage produces a different identifier for the same file uploaded twice, so duplication is invisible and the network stores the same content repeatedly

Asserted by [[chainlink-hash]] — *Wiki IPFS*  
<sub>Chainlink Fall 2022 Hackathon</sub>

**Problem** two people uploading the same files got different identifiers and did not know

**Mechanism** indexing files on chain so a content hash resolves to an existing identifier  
**Beneficiary** users and networks storing duplicate content

**Recurs in** [[backup systems]] [[media libraries]] [[scientific data]]