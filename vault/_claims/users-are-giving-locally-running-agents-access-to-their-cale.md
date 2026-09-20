---
tags:
  - "claim"
confidence: 0.9
evidence: "none"
---

# users are giving locally running agents access to their calendar, repositories and chat — their entire digital life — and handing off raw OAuth tokens to do it

Asserted by [[1-sec-open-source-security-nq9gmk]] — *1-SEC Open Source Security*  
<sub>Authorized to Act: Auth0 for AI Agents</sub>

**Problem** delegation to an agent is implemented as a full unrevocable credential because no narrower instrument exists

**Mechanism** scoped revocable tokens plus containment of what the agent can reach  
**Beneficiary** anyone running an agent with account access

**Recurs in** [[third-party integrations]] [[contractors]] [[device provisioning]]