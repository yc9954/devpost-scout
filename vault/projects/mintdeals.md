---
slug: "mintdeals"
url: "https://devpost.com/software/mintdeals"
title: "MintDeals"
hackathon: "TRON Grand Hackathon - HackaTRON Season 7"
organization: "TRON DAO"
winner: true
words: 766
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# MintDeals

> Transforming Club Memberships and Deals with DeFi-Driven Credit Access

[Devpost](https://devpost.com/software/mintdeals) · hackathon [[TRON Grand Hackathon - HackaTRON Season 7]]

## Facets

**domain** [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** ipfs, justlenddao, mongodb, nextjs, pinata, solidity, tronweb, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mintdeals

## Body

Landing Page Explore Clubs View My Minted Deals Club Details Club Dashboard Manage Deals Approve Redemptions Access Credit Inspiration The inspiration behind MintDeals stems from observing the challenges small businesses face in accessing credit and maintaining customer loyalty. Traditional financial systems often fail to support these businesses adequately, especially in regions where credit infrastructure is underdeveloped. By leveraging blockchain technology, we saw an opportunity to create a decentralized, transparent and efficient credit system that not only addresses these issues but also provides businesses with a powerful tool to enhance cash flow, build customer loyalty, and create an onchain credit score that could open doors to further financial opportunities. What it does MintDeals enables businesses to create blockchain-based clubs where they can offer exclusive and tokenizable deals to their members. Users pay a fee in stablecoin to join these clubs in order to mint and enjoy the deals. Behind the scenes, a DeFi-powered credit facility provides businesses with access to credit loans they need to grow and thrive. The credit facility funds are accumulated through the various membership payments made or earned through the platform and integrates with JustLendDAO for collateralized borrowing and liquidity management. Business' onchain activities help them build a credit score which is used as a metric to increase their borrowing capacity within the credit facility. MintDeals accepts USDT,USDD as payments. At the core of the shared credit facility is a BTC accumulation strategy with a portion of incoming revenue. This ensures that over time, as BTC's value increases, so too does the amount of available credit businesses or club owners can access/borrow. How we built it MintDeals was built on the Tron blockchain, leveraging smart contracts to automate credit management and deal creation. We integrated with JustLendDAO to enable the shared credit facility and used Wink price oracle for fetching the value of BTC. The core contract components include: MintDealsNFT: For minting and redemption of deals. Integrates with the ClubDealRegistry. ClubDealRegistry: For creating and managing clubs, deals and splitting of received payments to Credit Facility and Credit Manager. CreditManager: A contract account integrated with the CreditFacility, managing BTC, shared credit access, handles repayments and manages credit scoring that affects club owners' borrowing capacity. CreditFacility: Manages individual credit access and collective funds as sub accounts and integrates directly into JustLendDAO for accessing supplying, lending, borrowing, repayment and yield claiming capabilities. Challenges we ran into One of the main challenges was ensuring that the system remained user-friendly for businesses unfamiliar with blockchain technology. Due to the nature of the MintDeals and its integrations, we could not use wallet abstraction tools. So we will need to educate potential businesses on using TronLink and onboard them. We also had to tackle the complexity of creating the best combination of mechanics for the credit facility, along with combing through JustLendDAO's docs for integration of the required functions. Then, achieving an essential credit scoring system that's cost effective enough onchain, while maintaining the security, transparency and room for addon mechanics in the future. Lastly, optimizing the smart contracts to manage transaction costs effectively was a significant technical hurdle. Accomplishments that we're proud of We're proud to have developed and delivered a fully functioning MVP that bridges the gap between traditional business needs and modern DeFi solutions. Successfully integrating a shared credit facility, supporting credit scoring, creating a seamless user experience, and implementing club and NFT-based deal management are significant milestones for us. Additionally, we’ve created a system that not only benefits businesses but also offers value to end-users, hopefully encouraging broader adoption and new use cases of blockchain technology. What we learned Throughout the development of MintDeals, we learned the importance of simplifying complex blockchain concepts for end-users. We also gained deeper insights into the integration of DeFi solutions with real-world applications, particularly in how decentralized credit can be structured and managed. This project reinforced the value of iterative development, user feedback, and the need for constant optimization in both the technical and user-experience aspects. What's next for MintDeals The next steps for MintDeals include expanding our platform to onboard and support more businesses and users, establishing some small case studies from early adopters. Once we have some growth in users, then we can plan to enhance our credit scoring algorithms and explore new avenues to expand available shared capital capacity for instance, this could done be via staking and earning mechanics. We’re also looking at developing partnerships with local businesses to broaden the impact of our platform. Finally, we’ll focus on refining the UI to make MintDeals more accessible to non-technical users, ensuring widespread adoption and success. <div