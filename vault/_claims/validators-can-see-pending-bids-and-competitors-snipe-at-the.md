---
tags:
  - "claim"
confidence: 0.9
evidence: "concrete-instance"
---

# validators can see pending bids and competitors snipe at the last second — commit-reveal helps and adds complexity while still leaking during the reveal

Asserted by [[shadowbid-r9f26v]] — *ShadowBid*  
<sub>Frostbyte Hackathon</sub>

**Problem** the auction mechanism depends on bids being secret and the infrastructure makes them visible

**Mechanism** confidential computing primitives implementing a genuinely sealed-bid auction  
**Beneficiary** bidder whose bid is being read

**Recurs in** [[procurement]] [[spectrum auctions]] [[sealed tenders]]