---
tags:
  - "claim"
confidence: 0.8
evidence: "none"
---

# an authentication system designed for browsers cannot be used by an agent that has none, so the capability exists and is unreachable for exactly the client type it was needed for

Asserted by [[mcs-auth-bridge-enabling-token-vault-for-headless-ai-agents]] — *MCS Auth Bridge. Enabling Token Vault for Headless AI Agents*  
<sub>Authorized to Act: Auth0 for AI Agents</sub>

**Problem** the auth flow assumes a human at a redirect and agents have no redirect

**Mechanism** bridge letting device flow obtain vaulted tokens without a browser callback  
**Beneficiary** developer building a headless agent

**Recurs in** [[embedded devices]] [[CI systems]] [[kiosk terminals]]