---
slug: "posterity-y6bedz"
url: "https://devpost.com/software/posterity-y6bedz"
title: "Posterity"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1095
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Posterity

> A thoughtful way to secure your on-chain resources for access by those you care about.

[Devpost](https://devpost.com/software/posterity-y6bedz) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[general_public]]
**substrate** [[financial_record]] [[structured_db]]

**stack** chainlink, goerli, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for posterity

## Body

Inspiration The Posterity project was developed as a way to enable crypto asset holders to ensure access to these resources for those who are important to them, their heirs. There is an old pain in the Web3 ecosystem related to the eventuality of loss of these assets by their holders, in the event of their death, if someone other than the wallet holder does not have access to the private key or even the seed phrase. In order to solve this problem, some solutions have appeared in the market. However, these solutions imply the need for custody or semi-custody of access to crypto-assets of a given user, to ensure that other people have access, in the event of the death of the owner of the wallet. In addition, other existing "off-chain" solutions do not solve this problem, they just "displace" it to cold wallets and other devices such as physical artifacts, causing points of vulnerability to emerge in the physical world. We created the Posterity project to get around all these problems. Now, it is possible for users to ensure access to their crypto assets to their heirs, in an on-chain, decentralized, permissionless, and secure way! Posterity is "a thoughtful way to show love to those who matter to you". What it does The Posterity project consists of creating a dApp that allows users who have a cryptocurrency wallet to deploy a smart wallet, which we call Posterity Wallet, after providing their personal ID number, in order to confirm their identity. However, we do not have any access to this information. For the purpose of this Hackathon, we enabled the dApp to recognize only the personal ID number of Brazilian citizens. Thus, the functionality of the smart wallet was created for the purpose of a succession of crypto assets to heirs. Once the Posterity Wallet has been created, the next step consists of indicating the public addresses of the wallet owner's heirs, in addition to adjusting the percentage of crypto assets that will be allocated to each heir, when the Posterity Wallet owner dies. Currently, the wallet we developed only supports fungible tokens. Thus, it is important for the user to keep this in mind. Having completed these steps, the creator of the Posterity Wallet must deposit the funds he intends to make available in this wallet. As for the purpose of use, it is possible for the owner of the Posterity Wallet to use it in his day-to-day life, as his main wallet, bearing in mind that he will be able to carry out transactions through this new wallet. The occurrence of the wallet owner's death will be an identifiable event through the any API function of the oracle provided by Chainlink, which will consult the database of the "Receita Federal do Brasil", the public entity responsible for managing the information related to the identification number personal data of Brazilian citizens, in this case, the CPF number. In this way, a trigger will be activated to release access to the assets left by the deceased to the heirs indicated by the owner of the Posterity Wallet, according to the percentages assigned to each of them still alive. Each of the heirs will be able to access these crypto assets left by the deceased through access to Posterity's dApp dashboard, connecting their wallets, from the sending request by clicking on the "start a succession" button. When using the any API function, we caught a possible request error for the API we use. Our API successfully responds to the request made with the information, however, no API follows the fulfillment function contained in the smart contract. Thus, when performing the request through the any API function, our API receives the request and responds with status 200 (success), but our oracle does not invoke the fulfillment function to continue the logic of inheritance succession. However, the application is functional, achieving a concrete use case. How we built it The Posterity project was built on the Goerli testnet. We use the any API function of Chainlink's oracle to make requests to an endpoint of the API we use, which makes requests to rapidapi and receives the situation of the consulted CPF of the Brazilian citizen, which can be a “canceled” or “regular” situation. The Posterity Wallet is a smart wallet, that is, a smart contract, which receives, sends and "releases" ethers when the succession event occurs. Each Posterity Wallet has heirs configured by the wallet owner. Once an heir requests the succession of a wallet, the CPF associated with it is consulted through Chainlink's any API and, if the situation is canceled, the ethers balance of the Posterity Wallet is transferred to the heirs' wallets according to the configured percentage. Challenges we ran into Overall, we had three major challenges: Difficulty debugging error when using Chainlink's any API function. Participate in an online hackathon, without face-to-face contact, which can help resolve specific details, which generate greater value exchanges and learning for all. Asynchronous work on the project, which made doing synchronous tasks a bit more challenging. Accomplishments that we're proud of We are proud to have completed the integration of the "on-chain" world with real-world "off-chain" data from the "Receita Federal do Brasil", enabling a real use case, for a real problem, making tangible the high-value solution for an old pain of the Web3 ecosystem, according to the Web3 ethos, emphasizing decentralization, permissionless and security. What we learned We learned that, despite the challenges, the effort put into developing a real solution to a real problem, as is the case with the Posterity project, is not only worthwhile, but rewarding. In addition, we learned that the integration of “off-chain” data within “on-chain” dynamics can be really challenging, especially when it comes to the use of open data, that is, those data that originate from entities and public bodies. This is our case, through the use of the any function of the API of the Chainlink oracle, to bring data of deceased persons existing in the "Receita Federal do Brasil" database to verify the situation that authorizes the heirs to redeem the crypto assets left by the deceased. What's next for Posterity For the future of the Posterity project, we intend to: Implement Zero-Knowledge Proof, aiming to guarantee greater privacy and scalability in the process of creating and using the Posterity Wallet. Add compatibility with NFTs, enabling the inclusion and support of these assets in the Posterity Wallet. Include the ERC-4337 standard related to Account Abstraction, to increase the user experience and the possibilities of using the application. <div