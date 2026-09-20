---
slug: "poc-proof-of-consent"
url: "https://devpost.com/software/poc-proof-of-consent"
title: "PoC² - Proof of Consent"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 827
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# PoC² - Proof of Consent

> AI-powered, blockchain-anchored medical consent system that verifies patient understanding before signing and creates tamper-proof legal proof for doctors and hospitals.

[Devpost](https://devpost.com/software/poc-proof-of-consent) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]]
**domain** [[accessibility]] [[health_clinical]] [[legal_justice]] [[security_privacy]]
**user** [[clinician]] [[patient_family]]
**substrate** [[medical_record]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** ai, blockchain, css, ethers.js, express.js, hardhat, html, metamask, node.js, react, sha-256, solidity, tailwind, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for poc² - proof of consent
- final thought

## Body

Doctor Dashboard Digital Content Signature AI Explanation Landing Page Architecture Proof of Consent (PoC²) Inspiration One simple question inspired this project: "Did the patient truly understand the consent form before signing?" In hospitals today, consent often becomes a rushed signature on a complex form filled with medical jargon. Patients may feel pressure. Doctors remain legally vulnerable. And when disputes arise, courts ask: Was the patient truly informed? We realized that the real problem is not documentation — it is proof of understanding . That is how Proof of Consent (PoC²) was born. We wanted to transform consent from a paper event into a verifiable process . What it does PoC² is an AI-assisted, blockchain-anchored medico-legal consent system that ensures consent is clearly explained, actively understood, authenticated, digitally signed, and tamper-proof. Instead of assuming understanding, we measure it. The patient must answer key procedure-related questions. We calculate comprehension using: \( \text{Understanding Score} = \frac{\text{Correct Answers}}{\text{Total Questions}} \times 100 \) The system only proceeds if: $$ \text{Understanding} \geq 80\% $$ If the score is lower, the AI re-explains misunderstood sections in simpler language and the patient retakes the quiz. This creates measurable proof that the patient actively engaged with the information. How we built it Step 1: Doctor Creates Consent The doctor logs in, enters patient details and procedure information, and the system generates a unique Consent ID with a secure link. Step 2: Patient Identity Verification The patient opens the link and verifies their identity via OTP to prevent impersonation. Step 3: AI Explanation Instead of medical jargon, AI explains what the procedure is, why it's needed, the risks and benefits, and alternatives. AI assists understanding — it does not replace human responsibility. Step 4: Understanding Assessment The patient answers critical questions. If below the threshold, AI re-explains and the patient retries until comprehension is demonstrated. Consent becomes a learning-confirmed process , not a blind signature. Step 5: Digital Signature + Blockchain Integrity Once signed, the formatted consent packet is hashed: $$ H = \text{SHA256}(\text{Consent Packet}) $$ Only the cryptographic hash is stored on blockchain — no medical data is placed on-chain. If anyone modifies the consent later: $$ \text{SHA256}(\text{Modified Packet}) \neq H $$ This instantly proves tampering. Blockchain ensures timestamp integrity, non-repudiation, and immutable proof. Tech Stack: Frontend: React, Tailwind CSS Backend: Node.js, Express Database: MongoDB Blockchain: Solidity, Hardhat Web3: Ethers.js, MetaMask Cryptography: SHA-256 Challenges we ran into Legal Responsibility AI cannot legally certify understanding. We redesigned the system so human responses prove comprehension, while AI only assists. Privacy vs Blockchain Healthcare data cannot live on a public chain. We solved this by anchoring only cryptographic hashes, keeping all medical information off-chain. Identity & Coercion Risks We added OTP verification and structured flow to reduce proxy consent risks and ensure the actual patient is giving consent. Technical Determinism Ensuring identical hashes required strict JSON normalization and timestamp formatting: const hash = sha256(JSON.stringify(sortedConsentObject)); Even small changes in key order can produce different hashes. Precision matters in cryptographic systems. Accomplishments that we're proud of ✔ Measurable understanding — We created a quantified, verifiable method to prove patient comprehension, not just documentation ✔ Ethical AI integration — AI assists without replacing human judgment or legal responsibility ✔ Privacy-preserving blockchain — Only hashes on-chain, full medical privacy maintained off-chain ✔ Tamper-proof integrity — Immutable cryptographic proof that protects both patients and healthcare providers ✔ Legal defensibility — Structured evidence trail that can withstand medico-legal scrutiny This is not just a digital consent form. It is Medico-Legal Consent Assurance Infrastructure . What we learned Building PoC² taught us that: Technology must respect law and ethics — Healthcare innovation requires careful consideration of legal frameworks and ethical boundaries AI should assist, not replace — The best use of AI in healthcare is augmenting human decision-making, not substituting it Blockchain is for integrity, not storage — The power of blockchain lies in verification and immutability, not as a database for sensitive information Legal defensibility requires structure — Code alone isn't enough; the entire process must be designed with legal standards in mind Deterministic systems are crucial — In cryptographic applications, even minor inconsistencies in data formatting can break the entire verification chain What's next for PoC² - Proof of Consent Multi-language support to serve diverse patient populations and ensure understanding across language barriers EHR system integration for seamless adoption in existing clinical workflows Advanced analytics dashboard to help hospitals identify common comprehension gaps and improve patient education Witness and family member verification for complex or high-risk procedures Regulatory compliance certifications across different healthcare jurisdictions (HIPAA, GDPR, etc.) Mobile app development for easier patient access and improved user experience Telemedicine integration to support remote consent processes Final Thought Consent should not be a checkbox. It should be a transparent, ethical, and verifiable process. With AI assisting understanding and blockchain protecting integrity, Proof of Consent ensures that when someone asks: "Was the patient truly informed?" There will not be doubt. There will be proof . <div