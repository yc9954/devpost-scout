---
slug: "midatopay-jeksiy"
url: "https://devpost.com/software/midatopay-jeksiy"
title: "MidatoPay"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 898
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# MidatoPay

> Ofrecemos a los comercios la libertad de elegir. Una billetera virtual intuitiva para comercios que acepta dinero fiat y convierte automáticamente a criptomonedas.

[Devpost](https://devpost.com/software/midatopay-jeksiy) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]] [[supply_logistics]]
**user** [[small_business]]
**substrate** [[financial_record]] [[structured_db]]

**stack** alchemyapi, cairo, javascript, next.js, node.js, openzeppelin, postgresql, prisma, qrcode, react, scarb, starkli, starknet, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for midatopay

## Body

Inspiration Our inspiration comes from a reality we live every day in Argentina: inflation. As a team, we’ve seen friends and family who own businesses constantly struggle against devaluation. The problem is simple yet painful — the money they earn today is worth less tomorrow, making it nearly impossible to restock goods and maintain profitability. We noticed a huge gap between the advanced financial technology that already exists (crypto, DeFi) and the people who need it the most. The inspiration behind MidatoPay was simple: to use the best available technology to build a bridge and solve this real problem for real people. What it does MidatoPay is the payment solution that protects businesses from inflation. It allows any business to accept payments in their local currency (Argentine pesos) through a simple QR code and instantly receive the value of that sale in stable crypto assets (such as digital dollars). For both merchants and customers, the experience is identical to that of a modern payment app, completely removing the complexity of blockchain technology. In short: you get paid in pesos, protect your capital in digital dollars — automatically and seamlessly. How we built it MidatoPay was built on a robust and decentralized architecture: Frontend (React/Next.js): We developed an intuitive and responsive user interface for merchants and customers, including QR generation and scanning, wallet management, and transaction visualization. Backend (Node.js/Express.js): We implemented the business logic, database integration (PostgreSQL with Prisma ORM) for user and wallet management, and orchestration of interactions with Starknet. Starknet Integration: Oracle Contract: We use an Oracle contract on Starknet to obtain real-time ARS to USDT conversion rates. Payment Gateway Contract (Cairo): We developed a custom Cairo contract (PausableERC20) to handle payment logic, including the pay function that enables token transfers and transaction recording. starkli CLI: We integrated the starkli command-line tool into the backend to directly interact with Starknet contracts (invoke functions, perform dry-runs, etc.). Cavos Aegis SDK: Integrated to enhance contract interaction and security handling. Persistent Wallets: We implemented a system to generate, store, and manage Starknet wallets for each merchant, ensuring their private keys are protected and wallet addresses remain persistent. Interoperable QR (EMVCo TLV): We developed a QR code generator and parser following the EMVCo TLV standard to ensure compatibility and proper transmission of payment data. Challenges we ran into Here’s something about market education — our barrier is the same as all competitors’. "Our biggest challenge is communicating a crypto solution to a non-native audience. We had to refine our message many times, moving away from talking about 'crypto' and instead focusing on 'value protection' and 'digital dollar,' which is what merchants truly understand and need." BigInt and decimal handling in Starknet: Precise conversion of amounts between JavaScript (BigInt) and Cairo’s u128/u256 types, along with managing decimal scales (6, 18, or 0) in the Oracle and contracts, was a constant challenge. Accurate data extraction: Extracting precise data (merchant address, amount, payment ID) from the QR chain, which often contained variations, required robust regex patterns. Accomplishments that we're proud of The biggest lesson we learned is that the best technology is the one you don’t see. At first, we were excited about Web3 features, but we quickly realized that our users (the merchants) don’t care about the underlying technology; they care that their problem is solved in the simplest and most familiar way possible. This forced us to obsess over the user experience and make architectural decisions, such as using Cavos Aegis, that prioritize simplicity above all else. We learned to sell the benefit, not the feature. We are proud to have achieved: A fully functional end-to-end payment flow: From QR generation to executing the transaction on Starknet and displaying detailed results. Successful integration with Starknet Oracle: Obtaining real-time ARS to USDT conversion rates and applying them correctly from the contract. Persistent wallet system for merchants: A robust solution for merchants to securely manage their crypto assets. Error handling and resilience: Implementing mechanisms to debug and resolve complex issues related to blockchain and external tool integration. What we learned This project provided us with valuable lessons: Deepening our knowledge of Starknet: We gained a thorough understanding of the Starknet ecosystem, including Cairo, starkli, and contract interactions. The importance of decimal precision: We learned how critical it is to handle decimal scales correctly in crypto transactions to avoid financial errors. Complex full-stack development: Integrating frontend, backend, database, and blockchain requires meticulous coordination and a holistic understanding of the system. Problem-solving in decentralized environments: Debugging errors on the blockchain and interacting with CLI tools presents unique challenges that demand patience and creativity. Security in key management: The importance of protecting private keys and sensitive wallet information. What's next for MidatoPay The future of MidatoPay is promising. Our next steps include: Expansion to other cryptocurrencies: Integrating support for more stablecoins and cryptocurrencies. Advanced features for merchants: Implementing dashboards with detailed analytics, financial reports, inventory management tools, and more — since our main focus is on businesses and stores, we aim to provide them with as many tools as possible to stand out. Cairo contract optimization: Improving efficiency and reducing gas costs in our smart contracts. Production deployment: Preparing the platform for a large-scale launch, ensuring scalability and security. Education and adoption: Continuing to educate merchants on the benefits of cryptocurrencies and protection against inflation. With MidatoPay, we are building the “Payments of Today and Tomorrow.” <div