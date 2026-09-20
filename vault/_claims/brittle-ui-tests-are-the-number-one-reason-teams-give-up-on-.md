---
tags:
  - "claim"
confidence: 0.95
evidence: "none"
---

# brittle UI tests are the number one reason teams give up on automation — someone renames a button, the suite goes red overnight, and an engineer loses a morning working out whether anything is actually broken; self-healing was supposed to fix that and heals real bugs too

Asserted by [[selfheal-qa]] — *SelfHeal QA*  
<sub>UiPath AgentHack</sub>

**Problem** the repair mechanism cannot distinguish an incidental change from a genuine regression, so it hides the failures it was meant to surface

**Mechanism** heal the brittle case and refuse the real defect, filing it instead  
**Beneficiary** team that abandoned test automation

**Recurs in** [[monitoring alerts]] [[data validation]] [[compliance checks]]