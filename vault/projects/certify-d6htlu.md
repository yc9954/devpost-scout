---
slug: "certify-d6htlu"
url: "https://devpost.com/software/certify-d6htlu"
title: "Certify"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 605
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Certify

> Certify - A Decentralised Certification System with Immutability, Privacy and Certificate Statuses for Complex Applications!

[Devpost](https://devpost.com/software/certify-d6htlu) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[civic_government]] [[finance_payments]] [[labor_employment]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** celo, ipfs, metamask, react, solidity, walletconnect

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for certify

## Body

Demo Explanation Inspiration Certificates are very important in our lives. They allow us to prove our identity, our skills and a whole host of other things. But the current centralised systems are bogged down by fake certificates, corruption and difficulty in verifying the certificates. When we are dealing with such private information security and privacy is also a very big concern. Because they are so valuable, people often lie about their academic qualifications by producing fake certificates. In the United States there are currently 2 million fake degree certificates in circulation and 300 unauthorised universities operating. A study indicated that the United Sates has the highest number of fake institutions in the world followed by the United Kingdom which has about 270 fake institutes. It was also found that up to 35% of candidates in Australia falsified their academic credentials for the sake of employment. Most candidates lie at least about some part of their educational credentials and experience. Academic certificate fraud costs employers about $600 billion every year. We propose a system for creating and managing certificates which is decentralised thus giving maximum security. All the data is on public block-chain therefore it can be easily verified by anyone. The stored data would be encrypted too. Our application consists of a User Interface for institutes to create certificates and revoke certificates. There is also provision for a central authority which verifies institutes for authenticity. The institutes signs each certificate with their private key which ensures no forgery can be done, once the certificate is issued. What it does The project needs to store highly confidential data in an easily accessible and verifiable way. Therefore AES(Advanced Encryption Standard) encryption is used to encrypt data before uploading to IPFS(Inter Planetary File System). Then the IPFS hash of the data is stored on blockchain where it cannot be tampered with. Anyone can verify the certificate if they have the IPFS hash and the password used for encryption. How we built it The frontend is built with react using various hooks and web3context to optimise the performance. Parts of certificate data are fetched from IPFS and the blockchain and displayed on a predefined certificate format. IPFS API is used to submit and retrieve encrypted certificate data. The certificate data is encrypted using AES and a randomly generated password before uploading to IPFS. The IPFS hash is stored on blockchain. A verifier can see the details in the certificate if the owner of the certificate gives the verifier permission by sharing the private key. Certificates are stored as mapping with a certificate id as key and a certificate struct as object, which contains fields like certificate issuer, IPFS hash etc. Accomplishments that we're proud of These certificates can also be used for on-chain governance and Decentralised Finance (DeFi) for proving once identity. Governments can also use a similar system to issue driving licences, voter Id card, passport etc. increasing the security of our nation as these documents cannot be forged. In these kinds of system the identity of the individual is only visible to authorities and people who has access to encryption keys, Thus this system tends to be very secure and resistant to hacking. What's next for Certify The proposed project provides features like privacy because of AES encryption, Fast online verification by scanning QR code, ability to revoke certificate by institute at a later date. Various customisations will be added for user convenience in the future, using which issuers will be able to add certificates in batches. Protocols like Superfluid can be used to create certificates that allow streaming of tokens to create a wages system. <div