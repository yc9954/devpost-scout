---
slug: "stark-protocol"
url: "https://devpost.com/software/stark-protocol"
title: "Stark Protocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1013
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Stark Protocol

> A defi protocol that enables everyone to borrow with no collateral.

[Devpost](https://devpost.com/software/stark-protocol) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** alchemyapi, chainlink, ethers, filecoin, hardhat, javascript, moralis, nextjs, polygon, solidity, spheron

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for stark protocol

## Body

Inspiration Undercollaterised lending is still needed to be solved in this Defi space. Some protocols try to provide it but they are unable to do it to their best extent as they only provide one solution to users. But Stark Protocol enables no collateral credit by combining multiple things like credit score and loans backed by your friend. What it does Stark Protocol enables everyone to borrow without any collateral. Stark protocol is like any other defi lending protocol but it implements additional features like guaranty request, p2p request, credit score sbt, and real-time chat system to talk to enable borrowing without any collateral. Like in Traditional Banking, in some situations a borrower needs someone(securer) to back the deal between the borrower and the bank, where if the borrower is unable to repay the credit to the bank, then the securer will have to pay the remaining about to the bank. With this situation we have created a system where when a user(borrower) wants to borrow the assets from the protocol but is not able to due to insufficient balance then he may request his friend to secure the loan. And if the securer accepts it, then his balance of the same amount as the Loan Amount will be locked in the protocol, and his friend will be able to borrow the assets from the protocol. Here are the following benefits of a Guaranty Backed Loan:- The Borrower will get the amount he needed with collateralizing. The Securer will earn greater interest by locking his amount in the protocol and can even get interest from the borrower if wanted. The protocol will earn the assets by implementing interest on the deal. Can pay this loan in installments for a specific period. In the traditional market, where P2P loans also exist, we have made a functionality, P2P Lending, where the user can ask for a loan from the other user (with some interest on it if the lender implements it). Here are the following benefits of a P2P Loan:- The transaction will be P2P or between friends, so it will have some personal trust. The interest will be implemented only by the Lender, not the platform (at first). The platform will earn assets if the borrower extends the duration of the loan. Can pay this loan in installments for a specific period. Both types of loans will maintain functionality to modify the Credit Score of the borrower so that in the future the lenders or friends can check out the risk factor by analyzing their Credit Score. The credit score will be modified after considering various factors like the number of installments used, the time period required in total, the previous history of the loans, etc. And all the chat will happen on the platform only using the decentralized chat application where the user only needs to enter the address of their friend or the person from whom they want to request their guaranty or a loan. How we built it Stark Protocol is a decentralized protocol. We have gone to every extent possible in this time frame to make this whole protocol decentralized. Decentralization was achieved by using different technologies. These are the following Technologies we have used in the Stark Protocol:- Polygon: Polygon Mumbai Testnet helped us to deploy smart contracts and to make transactions very quick and cheap. Chainlink (Sponsor): Chainlink keepers help in maintaining the modifying Credit Score Token (SBT) and its metadata. Alchemy (Sponsor) : Alchemy provided us with powerful nodes to built our dapp on top of. Filecoin/IPFS (Sponsor): To make our project fully decentralized we deployed our project on filecoin. Spheron (Sponsor): Spheron help us to deploy our project on filecoin efficiently. Moralis: Moralis helped to make frontend with hooks Hardhat: Hardhat helped us in compiling, testing, and deploying the contracts. Next.js: It helps us build the UI of the Stark Protocol. XMTP: XMTP SDK helped us in building a decentralized application where users can chat and make a deal. We developed all the Smart Contracts with Solidity, using the Open Zeppelin Contracts. These contracts are thoroughly tested by building different tests using Hardhat and later deployed on the Polygon Testnet using the same. The Chainlink implemented in the contracts helps us in making the dynamic SBT tokens, which change as the Credit Score of the user changes. On the client side, Next.js help us in building a serverless client side, and with help of Moralis hooks, we were helping to maintain the state of the UI. Not to mention, XMTP helped us exceptionally to build a decentralized chat application that works as we want. The extraordinary thing we consider in this project is the Credit Score Token. They are built on the concept of the Soul Bound Tokens, which have the non-transferring property. Credit Score Token will be minted only once by a user in his lifetime, i.e. when he enters the protocol for the very first time. It will maintain the Credit Score of the users, which will help other users to check the risk of lending or backing someone their assets. Challenges we ran into While building this we ran into many challenges we try to use tableland for sbt but in the end, chainlink helped us to make our credit score sbt dynamic and we also try to use real-time notification with epns in guaranty request but it didn't work properly, we also tried to contact their team but we got no response. But still, after all the challenges, we are succeeded to build our dapp What we learned We learned many things from building credit score sbt tp building a real-time chat system but the main thing we learned was what is teamwork and how we can work effectively as a team. What's next for Stark Protocol Our mission is to allow everyone to borrow without any restrictions because most people borrow because they don't have collateral to give e.g. education loans, personal loans, etc. If we could get some help we want to launch it and work on our mission. <div