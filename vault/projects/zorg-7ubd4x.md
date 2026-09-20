---
slug: "zorg-7ubd4x"
url: "https://devpost.com/software/zorg-7ubd4x"
title: "Zorg - Health Records Reimagined"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 645
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/retrieval_grounding"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/medical_record"
---

# Zorg - Health Records Reimagined

> Automated healthcare with Zorg: secure, decentralized storage and instant access to encrypted patient records, ensuring life-saving info is available in emergencies.

[Devpost](https://devpost.com/software/zorg-7ubd4x) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[privacy_tech]] [[retrieval_grounding]] [[revocation_withdrawal]]
**domain** [[civic_government]] [[disaster_emergency]] [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[frontline_worker]] [[general_public]] [[patient_family]]
**substrate** [[code_repository]] [[medical_record]]
  <sub>weak: financial_record</sub>

**stack** blockchain, bun, data, docker, express.js, flask, hardhat, intersystems, javascript, machine-learning, next, python, react, shad-cn

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- what's next for zorg

## Body

System Design Chain Transaction IPFS System Frontend Patient Facing Frontend Provider Facing Inspiration Last week, one of our team members was admitted to the hospital with brain trauma. Doctors hesitated to treat them because of their lack of insight into the patient’s medical history. This prompted us to store EVERYONE’s health records on a single, decentralized chain. The catch? The process is end-to-end encrypted, ensuring only yourself and your designated providers can access your data. How we built it Zorg was built across 3 verticals: a frontend client, a backend server, and the chain. The frontend client… We poured our hearts and ingenuity into crafting a seamless user interface, a harmonious blend of aesthetics and functionality designed to resonate across the spectrum of users. Our aim? To simplify the process for patients to effortlessly navigate and control their medical records while enabling doctors and healthcare providers to seamlessly access and request patient information. Leveraging the synergy of Bun, React, Next, and Shadcn, we crafted a performant portal. To safeguard privacy, we fortified client-side interactions with encryption, ensuring sensitive data remains inaccessible to central servers. This fusion of technology and design principles heralds a new era of secure, user-centric digital healthcare record keeping. The backend server… The backend server of Zorg is the crux of our mission to revolutionize healthcare records management, ensuring secure, fast, and reliable access to encrypted patient data. Utilizing Zig for its performance and security advantages, our backend encrypts health records using a doctor's public key and stores them on IPFS for decentralized access. These records are then indexed on the blockchain via unique identifiers (CIDs), ensuring both privacy and immutability. Upon request, the system retrieves and decrypts the data for authorized users, transforming it into a vectorized format suitable for semantic search. This process not only safeguards patient information but also enables healthcare providers to efficiently parse through detailed medical histories. Our use of Zig ensures that these operations are executed swiftly, maintaining our commitment to providing immediate access to critical medical information while prioritizing patient privacy and data integrity. The chain… The chain stores the encrypted key and the CID, allowing seemless access to a patient’s file stored on decentralized storage (IPFS). The cool part? The complex protocols and keys governing this system is completely abstracted away and wrapped up modern UI/UX, giving easy access to senior citizens and care providers. Challenges we ran into Our biggest challenges were during integration, near the end of the hackathon. We had divided the project, with each person focusing on a different area—machine learning and queries, blockchain and key sharing, encryption and IPFS, and the frontend design. However, when we began to put things together, we quickly realized that we had failed to communicate with each other the specific details of how each of our systems worked. As a result we had to spend a few hours just tweaking each of our systems so that they could work with each other. Another smaller (but enjoyable!) challenge we faced was learning to use a new language (Zig!). We ended up building our entire encryption and decryption system in Zig (as it needed to be incredibly fast due to the potentially vast amounts of data it would be processing) and had to piece together both how to build these systems in Zig, and how to integrate the resulting Zig binaries into the rest of our project. What's next for Zorg In the future, we hope to devise a cryptographically sound way to revoke access to records after they have been granted. Additionally, our system would best benefit the population if we were able to partner with the government to include patient private keys in something everyone carries with them like their phone or ID so that in an emergency situation, first responders can access the patient data and identify things like allergies to medications. <div