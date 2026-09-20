---
slug: "cipher-shield"
url: "https://devpost.com/software/cipher-shield"
title: "Cipher Shield"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 787
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/web_dom"
---

# Cipher Shield

> Making discrimination mathematically impossible via the blockchain & homomorphic encryption

[Devpost](https://devpost.com/software/cipher-shield) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[on_device_local]] [[privacy_tech]] [[provenance_signing]] [[retrieval_grounding]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[finance_payments]] [[health_clinical]] [[labor_employment]]
**user** [[educator_student]] [[general_public]]
**substrate** [[web_dom]]

**stack** c++, node.js, openfhe, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cipher shield

## Body

Title System Architecture Blockchain Social Impact B2B Model Inspiration The inspiration for our project came from a problem based approach to ideation. We as students fill out countless job applications, and each one asks for demographic data. Most simply opt out as there seems to be no tangible benefit. In fact, there seems to only exist a potential downside: that it may be illegally misused to negatively affect your application. And yet, demographic collection does serve a large social purpose for society, specifically for detecting trends that may expose discrimination. In numerous cases, including employment, healthcare, loans, and credit cards, collecting demographic data is actually mandated by the federal government. We figured that in the era of decentralization and advanced encryption schemes, there is no reason for misuse of this information to even be mathematically possible . What it does Cipher Shield acts as a trusted third party, providing completely secure data aggregation services via the blockchain. We empower companies to extract aggregate statistical insights from homomorphically encrypted data, thus making it impossible to profile individuals based on their protected data. How we built it Blockchain: The chain is a critical component of our architecture and business model since it accelerates trust in our services. Every aggregation request is stored on the chain, creating an immutable, public record. Before any homomorphic computation is initiated, our smart contract performs critical on-chain validation - a transparent verification that ensures enough records exist to make reverse engineering mathematically impossible. If there aren't enough data points to maintain statistical anonymity, the contract automatically rejects the request. Once the request is validated and the computation is complete, the final aggregated result is also stored on chain, creating an audit trail of our services that companies can trust - we can't nullify data because every step is permanently and publicly verifiable on the blockchain. Dealing with advanced encryption schemes and blockchain operations, our business logic was written entirely in C++ and solidity. We leveraged OpenFHE homomorphic encryption operations and key generation. As a B2B product, our demo needed to include an entire demo business to use our product, which required a whole other backend+frontend pair. Challenges we ran into We ran into a number of challenges while building the product: Implementing our design of the homomorphic encryption in OpenFHE library, specifically with the dual private key setup which did not come as a out of the box solution. Writing the implementation for the backend responsible for the data aggregation in C++ and facilitating the key exchange with correct serialization, deserialization. Managing the large payloads of ciphertext in the communications between company and server and storing ciphertext. Accomplishments that we're proud of We started off as 4 complete strangers with incredibly varying interests and skillsets and we were able to collaborate seamlessly. Together, we created the first ever implementation of a split key homomorphic encryption scheme that’s also verified through blockchain technology. We learned a lot about homorphic encryption as well as blockchain. We were able to intergrate the full stack of the application together and make all of the parts of the system working locally, with all of the Customer Data, Company/Organization, and Authority. What we learned We learned about how to implement Homomorphic Encryption libraries and packages and alter their fundamentals to be able to work with split keys. We learned about the different ways that data security and insurance is important in B2B SaaS solutions, as well as potential business market ideas that could benefit both business and consumer at the same time. We also learned about the integration of Web-2 with Web-3 technology as well as integrating visualizations on the full-stack end despite coming in with very limited knowledge about blockchain. Moreover, we also learned about creating front-end web applications as well as a balance of creativity, inspiration, and feasibility when implementing a large scale and ambitious project. We also learned about the importance of Web-3 in web-application security. What's next for Cipher Shield We believe Cipher Shield should mediate the demographic collection and protected data collection processes of every company in America, and we believe this will have transformative societal outcomes in mitigating discrimination. The data aggregation capabilities of our scheme extend far beyond single company aggregation, but can even be used to securely combine hospital datasets. To encourage companies to adopt our tech, we would also want to create an easy to use SDK for organizations, companies, and industries less knowledgeable on the prospect and understanding of Blockchain and encryption. Furthermore, the ability to directly create a form or application directly on Cipher Shield and embed it into any company or organizations’ website directly through a Web Embedding that CipherShield uses would be essential to seamless adoption. <div