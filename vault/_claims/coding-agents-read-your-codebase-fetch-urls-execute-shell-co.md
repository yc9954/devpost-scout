---
tags:
  - "claim"
confidence: 0.9
evidence: "none"
---

# coding agents read your codebase, fetch URLs, execute shell commands, call external APIs and install packages — every one of those is an injection surface, and the powerful part and the dangerous part are the same part

Asserted by [[mighty-security]] — *Mighty Security*  
<sub>DeveloperWeek 2026 Hackathon</sub>

**Problem** the capability that makes an agent useful is the capability an attacker wants

**Mechanism** hook-level interception of multimodal prompt injection inside the agent  
**Beneficiary** developer running an agent with shell access

**Recurs in** [[CI pipelines]] [[browser agents]] [[email automation]]