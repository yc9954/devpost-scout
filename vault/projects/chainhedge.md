---
slug: "chainhedge"
url: "https://devpost.com/software/chainhedge"
title: "ChainHedge"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 930
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# ChainHedge

> ChainHedge is a marketplace of insurance writers and buyers where anyone can issue a custom inflation-target insurance contract.

[Devpost](https://devpost.com/software/chainhedge) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[vision_ocr]]
**domain** [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]] [[web_dom]]

**stack** chainlink, covalent, react, solidity, spaceandtime, truflation

## How they structured the write-up

- chainhedge

## Body

Home page Creating a contract (issuer view) Creation completed Chainlink/Truflation contract call making a state change of the last inflation Contract sample Viewing history using space and time or covalent queries Example contract with creation and purchase Example policy with several events Viewing a created contract (buyer view) Confirming purchase (buyer view) Contract expired (buyer view) ChainHedge Logo Completing purchase of policy (buyer view) ChainHedge ChainHedge is a marketplace of insurance writers and buyers where anyone can issue a custom inflation-target insurance contract. If the inflation exceeds a given amount before a set expiration, the policy buyer can redeem a payout from the writer. ChainHedge is validated by an internal Chainlink/Truflation contract API call saving the last reported inflation value and comparing against a policy's set target inflation payout value. Try it out here: https://chainhedge.surge.sh (note must be connected to polygon testnet). Demo video: https://youtu.be/VUzjFkqY_Sc How it works Insurance writers can deploy smart contracts with the following terms: * Inflation target: Threshold monthly reported inflation percentage for payout. * Expiration: Date the policy expires. * Payout: Amount to payout if percentage is greater than or equal to inflation target above. Premium: Cost for buyer to participate in the insurance contract When the policy is created, a url can be shared with a potential buyer to participate in the policy! The buyer must call the contract while the reported inflation is higher than the target. Once recorded, the buyer can withdraw the payout at any time. Note ChainHedge is currently a hackathon prototype and would require additional work to be mainnet/production-ready Get Mumbai link/matic here: https://faucets.chain.link/mumbai Motivation The motivation behind ChainHedge stems from the recognition of the limitations and inefficiencies prevalent in traditional insurance markets and contract execution processes. In many existing contracts, there is a heavy reliance on intermediaries and paid exchanges, leading to high transaction costs, delays, and a lack of transparency. In particular, you often have: Centralized parties with middle man fees Slow claims process for insurance policies Not always able to create the exact policy or terms you want KYC policy that might restrict some global participants Cost Reduction: By eliminating the need for intermediaries, ChainHedge significantly reduces transaction costs associated with insurance contracts. Traditional insurance policies often involve various middlemen, such as brokers and underwriters, who add their fees to the overall premium. With ChainHedge, the platform directly connects insurance writers and buyers, cutting out unnecessary expenses and making insurance more affordable for everyone. Transparency and Trust: Transparency is a crucial aspect of any insurance contract. However, the current system lacks transparency, making it difficult for buyers to understand the underlying terms and conditions. ChainHedge utilizes the inherent transparency of blockchain technology, allowing all parties to view and verify the terms of an insurance contract. This transparency fosters trust between writers and buyers, as both parties can rely on the integrity of the blockchain and a chainlink truflation API call for accurate and immutable record-keeping. Customization and Flexibility: ChainHedge empowers individuals and businesses to create highly tailored insurance contracts. Traditional insurance policies often come with rigid terms and standardized coverage, which may not adequately address specific risks or individual needs. With ChainHedge, anyone can create an inflation-based insurance contract and set parameters such as the threshold for inflation, expiration time, and payout structure. This flexibility enables buyers to design insurance solutions that precisely align with their unique requirements. Accessibility and Inclusion: ChainHedge democratizes the insurance market by providing a platform that is accessible to everyone. In many cases, individuals and small businesses face difficulties obtaining insurance coverage due to high entry barriers or limited options. ChainHedge opens up the market to a broader range of participants, enabling individuals and businesses of all sizes to engage in insurance transactions and protect themselves against inflation risks. Efficiency and Speed: Traditional insurance processes can be time-consuming and prone to delays. Claims processing, in particular, can be slow and cumbersome, leading to frustrations for policyholders. ChainHedge leverages smart contracts, which are self-executing and automatically trigger the payout process when predetermined conditions are met. Global Reach: With its decentralized nature, ChainHedge transcends geographical boundaries, allowing insurance writers and buyers from around the world to connect and transact seamlessly. https://www.statista.com/statistics/1312060/us-inflation-rate-federal-reserve-interest-rate-monthly/ Example Example policy: chainhedge.surge.sh/policy/0xa9A430749e40DC808E50201a1B2aA9ed91f8b443 Technologies used Truflation: Truflation provides a reliable and accurate measure of inflation, which is essential for creating an inflation-based insurance contract. With Truflation, insurance buyers and sellers can have confidence in the accuracy of the inflation data used in the contract, which helps to reduce the risk of disputes and increases trust in the overall insurance marketplace. Flow Blockchain: Flow is used for user verification. The Flow blockchain also offers strong security features, including its unique multi-role architecture, which helps to prevent attacks and protect user data. Flow enforces that only the user that bought the policy can be the one that redeems for a payout. Chainlink: Chainlink provides a reliable and secure way to connect smart contracts with external data sources, such as Truflation. With Chainlink, insurance buyers and sellers can be confident that the data used in their contracts is accurate and tamper-proof, reducing the risk of fraud and disputes. Space and Time: Space and Time ensures the data of the buyers and sellers is stored in a secure and tamper-proof manner, reducing the risk of data loss or manipulation. Users of the ChainHedge app can query Space and Time tabled history for any contract directly from the history tab in-app. A covalent history key can also be used. Every completed truflation check emits a CheckInflationEvent that gets indexed and appended to the insurance contract. <div