---
tags:
  - "claim"
confidence: 0.9
evidence: "none"
---

# contrary to expectation, seed phrases are not always enough to recover funds: with a multisig or complex wallet you must also back up the descriptor, and that backup leaks your entire policy to whoever holds it

Asserted by [[descriptor-encrypt]] — *descriptor-encrypt*  
<sub>Bitcoin 2025 Official Hackathon</sub>

**Problem** the recovery material and the privacy-sensitive material are the same artifact

**Mechanism** encrypt the descriptor under exactly the access policy it describes  
**Beneficiary** holder of a complex wallet

**Recurs in** [[estate planning]] [[institutional custody]] [[key escrow]]