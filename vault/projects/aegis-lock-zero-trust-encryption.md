---
slug: "aegis-lock-zero-trust-encryption"
url: "https://devpost.com/software/aegis-lock-zero-trust-encryption"
title: "Aegis-Lock: Zero-Trust Encryption"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 764
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Aegis-Lock: Zero-Trust Encryption

> Database-agnostic field-level encryption. Keep your data searchable, and leave hackers with nothing.

[Devpost](https://devpost.com/software/aegis-lock-zero-trust-encryption) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** javascript, node.js, npm, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- the future of aegis-lock: zero-trust encryption

## Body

Aegis Dashboard Aegis Proof Aegis Playground Aegis Playground Decryption Inspiration Once again, another huge data breach in terms of passwords, emails, and SSNs is happening every week with millions of users revealed. The current standard for the industry is to use encryption at rest, i.e., to encrypt the entire hard drive. However, as soon as a hacker gets into the database server or the API itself, he/she simply gets all the data in plaintext. We realized that it is no longer safe to trust the backend. The idea is to create a true zero-trust model wherein the data is encrypted as soon as it is moved from the device, i.e., there is no chance that, as soon as the database is completely compromised, the attackers will be able to receive nothing whatsoever. What it does Aegis-Lock is a two-component ecosystem: The Core Engine It is a database-agnostic npm package that supports client-side AES-256-GCM encryption. Cryptographically binding a ciphertext to a particular row in the database to protect against tampering (Contextual Binding), as well as generating memory-aligned HMAC hashes to enable the ability to use the database to search for exact matches (e.g., an email) without reading the plaintext (Blind Indexing), are natively supported. The Interactive Portal A real-time frontend dashboard that is graphical and intuitive. The user is able to input the data as well as observe how it is converted to an unbreakable iv:ciphertext composite before it is sent to the database. How we built it We divided our work to address the heavy cryptography as well as the complicated UI simultaneously. At the cryptography level, we developed the aegis-lock npm module. We leveraged the native Web Crypto API (crypto.subtle) instead of relying on cumbersome third-party libraries to ensure that it is not only fast but also secure. We designed the automated IV generation, Contextual Binding (AAD), and the deterministic HMAC SHA-256 hashing of the Blind Indexes and assembled them into a publishable ORM-style client. The interactive portal was implemented on the frontend using React 18, Vite, Tailwind CSS, and Radix UI. We integrated the aegis-lock package directly into the browser, avoiding backend development altogether. We integrated the application into a Supabase PostgreSQL database through our modified adapter, allowing it to easily process the encrypted CRUD operations and display the live side-by-side "Aegis Proof" UI. Challenges we ran into The Searchability Paradox: AES-256-GCM is non-deterministic in that if you were to take the encrypted version of the same word, you would get a completely different string each time you try to encrypt it. This means that you cannot search for an encrypted email in a database. To allow the frontend to search through the database without allowing frequency analysis attacks, we had to securely implement Blind Indexing using HMAC. Secure Updates: Anyone can create an insert. Creating a good CRUD wrapper is hard. To avoid keystream reuse attacks, we had to create algorithms that instantly generated mathematically random IVs and obscure the hashes of the Blind Indexes. Illustrating Cryptography: Cryptography is by nature invisible. Our UX challenge was to take such complex and intricate ideas as AAD and IVs and create a highly visual playground that one can easily follow. Accomplishments that we're proud of Successfully publishing a real, production-worthy npm package (aegis-lock) at the hackathon. Achieving 100% client-side encryption. We mathematically proved that the plaintext and the encryption keys do not touch our backend server or our database. Building our own dashboard, the Aegis Proof, which has a beautiful display of a three-column live comparison: plaintext input, raw database ciphertext, and decrypted output. Working perfectly as a team, bridging the gap between low-level security engineering and high-level React frontend engineering. What we learned Applied Cryptography: We came to know the ugly truth about key management, the perils of reusing keystreams, the importance of Contextual Binding, and how to thwart malicious attacks on the integrity of data that can be committed by reusing the same key. Web Crypto API: We went through the highs and lows of using native browser APIs securely. Developer Experience (DX): We learned how to create a complex security tool with a clean and intuitive API to give developers an opportunity to use military-grade encryption with simple database queries. The future of Aegis-Lock: Zero-Trust Encryption Currently, the package is shipped with Supabase and MongoDB adapters. Next, we plan to add adapters for Prisma, Drizzle, and Firebase. We also plan to create an in-built Key Management Service (KMS) companion app that will allow developers to safely manage and inject their master encryption keys without strictly relying on environment variables. <div