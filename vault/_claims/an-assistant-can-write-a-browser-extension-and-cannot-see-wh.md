---
tags:
  - "claim"
confidence: 0.85
evidence: "none"
---

# an assistant can write a browser extension and cannot see whether the popup renders or the worker initialises, so it is producing code it has no way to evaluate

Asserted by [[caps-chromium-ai-plugin-skeletton]] — *CAPS Chromium AI Plugin Skeleton*  
<sub>Kiroween</sub>

**Problem** the generation loop is missing the feedback signal that would make it converge

**Mechanism** scaffolding that lets the assistant verify, test and explore the extension it is writing  
**Beneficiary** developer using AI on plugin code

**Recurs in** [[embedded firmware]] [[mobile apps]] [[hardware drivers]]