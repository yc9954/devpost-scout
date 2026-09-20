---
slug: "certifi-lgbd3z"
url: "https://devpost.com/software/certifi-lgbd3z"
title: "CertiFi - Academic Credentials Powered by Blockchain"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 793
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
---

# CertiFi - Academic Credentials Powered by Blockchain

> Blockchain based Credential Platform that lets institutions issue credentials and learners store, verify and share their credentials. Transcript Issuing cost for CertiFi ($0.56) << Conventional ($5+).

[Devpost](https://devpost.com/software/certifi-lgbd3z) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[education]] [[labor_employment]]
**user** [[educator_student]] [[general_public]] [[researcher]]
**substrate** [[financial_record]] [[transcript_audio]]

**stack** amazon-web-services, javascript, mongodb, node.js, react, tailwind, tron, tronlink

## How they structured the write-up

- inspiration
- what it does
- certifi features
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for certifi

## Body

CertiFi Features of CertiFi Use cases of CertiFi CertiFi Diagram Inspiration Credential Verification is a $10+ Billion business. National Student Clearinghouse & Parchment are some legacy companies that earn huge amounts because of an outdated and slow to adapt education industry. We all have dealt with credentials at some point. Whether it is transcripts and degree certificates from universities or verification letters from past employers, this is a tedious process involving lot of bookkeeping. What if there was a better, cheaper and faster solution that we could use? A few universities (mentioned below) are already doing it and we have helped them do it. Now, we want to push for a mainstream adoption of the blockchain technology for credential verification with our platform, CertiFi. CertiFi is a natural fit - a blockchain based solution wins over the conventional system which requires a trusted intermediary who charges expensive fees. Colleges charge $2-$15 for issuing a transcript once where the middleman has a take rate of 20-30%. We are able to issue and certify transcripts and other credentials for <$1 due to TRON's low gas fees and sustain a lower take rate. We store the uploaded credentials on IPFS as of now. The certification is immutable once granted. This is a blockchain business with strong unit economics!! These credentials can be used for admission to courses, background verification for employees, new kinds of job portals where degrees and other qualifications automatically make job seekers eligible for certain jobs, etc. The possibilities are endless once we have moved out the 'proving' part of credentials and made verification a trust-less process. What it does We enable 3 things: Institutions like Universities can issue credentials like transcripts or degree certificates to students. The contents of the transcript are hashed and stored on IPFS. We certify that the transcript has been issued by institution to the student. We secure this information on the TRON ledger by storing the hashed issuer, recipient and credential file relation. Learners can then view all their credentials in one place if the data is stored on the school's servers. They can export their credentials and keep it with them. They can verify the credentials whenever they'd like. Verifiers can verify the credentials with a valid link OR a downloaded credential file. This validates the issuer, recipient and the credential relationship and enforces trust when recruiting students to a course or a job. **Currently the institution and individual view are both accessible to any address. We intend to integrate DID to verify which addresses are institutions in the future. **A verifier does not need a Tron Address to verify credentials! Only the issuer and the recipient need an address. We can even do away with the need for an address for a recipient by using downloaded credentials. CertiFi Features How we built it We used the TronWeb library and lots of documentation resources to build our product. Our experience with implementing the technology in a real world case helped us a lot. You need the Tron Extension and to be on the Shasta Testnet to use the demo. Challenges we ran into The storage of files is a big challenge. We need to determine a location to store the credential file and make it accessible securely and in a decentralized manner. The files per say do not need to be stored in a decentralized fashion because they can be downloaded by the recipient. What matters is the validation of the credential which can be done with an offline copy of the file as well. Onboarding institutions from legacy systems involves writing lot of backwards compatible systems. The legacy CRM softwares used by institutions can be a pain to work with and the few universities we worked with required us to rewrite a lot of our software to support the use case. We have then gone ahead and pulled out the the common features and made the existing code extensible to enable these custom mods for each institution resulting in this platform, CertiFi. The platform can be extended easily because it has all the core functionalities and can offer APIs easily. Accomplishments that we're proud of We have implemented similar systems at Maryville University and Oral Roberts University and have reduced costs for transcript issuance. We intend to make this platform open and let more institutions use the public blockchain for issuing credentials. What we learned Cryptography + Web3 opens a huge potential for innovations and solves a lot of web2 problems. TronWeb Implementation and Usage IPFS Implementation and Usage What's next for CertiFi 2022 Q3 Build bulk credential issuance. Integrate with PeopleSoft & Ellucian for pulling student records from legacy systems. 2022 Q4 Build a robust data hosting solution with ability to pin credentials. <div