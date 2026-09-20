---
tags:
  - "claim"
confidence: 0.9
evidence: "none"
---

# agent integrations ship provider keys with no user-level consent, long-lived tokens that cannot be inspected or revoked, and no distinction between reading and writing, so the highest-risk actions are the least visible

Asserted by [[phantom-auth0]] — *Phantom Auth0: Secure Delegated Actions for AI Agents*  
<sub>Authorized to Act: Auth0 for AI Agents</sub>

**Problem** delegation was implemented as credential sharing rather than as scoped, revocable authority

**Mechanism** vaulted per-user tokens with explicit permission boundaries and approval for writes  
**Beneficiary** person delegating to an agent

**Recurs in** [[financial automation]] [[clinical systems]] [[industrial control]]