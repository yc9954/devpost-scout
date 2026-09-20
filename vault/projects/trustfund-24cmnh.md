---
slug: "trustfund-24cmnh"
url: "https://devpost.com/software/trustfund-24cmnh"
title: "TraceFund"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 401
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# TraceFund

> Rebuilding donation trust through transparent giving.

[Devpost](https://devpost.com/software/trustfund-24cmnh) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[provenance_signing]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[finance_payments]]
  <sub>weak: housing_homeless</sub>
**substrate** [[financial_record]]
  <sub>weak: code_repository, document_pdf</sub>

**stack** base, claude, erc-20, ethereum, ethers.js, express.js, hardhat, next.js, node.js, open-zeppelin, react, solidity, tailwind.css, typescript

## Body

What it is We built TraceFund, an AI-gated donation platform on blockchain. Donors send USDC directly into an on-chain vault. A recipient can request a payout for a specific need (“$280 for urgent stitches, here’s the invoice”). Our AI verifier reviews that request, and if it’s legit and aligned with the campaign’s mission (housing, medical, survival needs), it authorizes the spend. The smart contract will only release funds if it sees a valid signature from that AI verifier key. So money only moves if policy passes, and every payout is publicly auditable. Why we built it Traditional aid is slow and opaque. You donate, but you rarely see where dollars actually go. People in crisis, meanwhile, can’t wait weeks for committee approval. We asked: can we replace “trust us” with math? How it works The recipient submits a spend request on-chain: [ R = (\text{amount}, \text{to}, \text{description}, \text{evidenceHash}) ] The backend pulls that request and asks Claude: “Does this match the stated mission and look reasonable?” If approved, the backend signs a hash of ( R ) using a dedicated verifier wallet. Anyone can then call executeSpend(id, sig) on-chain. The contract: Verifies the signature via ECDSA. Transfers USDC. Emits an event logging what was paid and why. No signature, no money. No human override. Mathematically, the approval flow looks like this: Compute [ h = \mathrm{keccak256}(\text{vault_address} \,|\, \text{spendId} \,|\, \text{amount} \,|\, \text{to} \,|\, \text{description} \,|\, \text{evidenceHash}) ] Claude decides if the request is aligned with the campaign’s stated purpose and reasonable in size. If yes, the verifier wallet signs ( h ) to produce a signature ( \sigma ). On-chain, the contract checks that [ \mathrm{ecrecover}(h, \sigma) = \text{aiVerifier} ] and only then releases funds. What we learned AI can act as a compliance gatekeeper, not just a chatbot. We can enforce “aid must match mission” cryptographically: the vault literally refuses to pay unless the model-approved signature is present. Donor transparency doesn’t have to expose private documents: we store a human explanation and an evidenceHash on-chain, not the full invoice. Challenges Fiat on/off ramp partners (MoonPay / Bridge / Coinbase Offramp) require real KYC/KYB and money-transmitter onboarding. That’s not possible in a weekend without being an incorporated financial entity, so we simulated that honestly instead of faking ACH. Private key hygiene in a hackathon: the verifier key never touches Claude. Claude only returns JSON like ```json { "approve": true/false } <div