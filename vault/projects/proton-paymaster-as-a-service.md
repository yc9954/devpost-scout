---
slug: "proton-paymaster-as-a-service"
url: "https://devpost.com/software/proton-paymaster-as-a-service"
title: "Proton - Paymaster as a Service"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 702
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# Proton - Paymaster as a Service

> Platform for dApps to sponsor gas for their users to increase user acquisition and retention. Using account abstraction, dApps can conditionally sponsor gas with no change in their smart contracts.

[Devpost](https://devpost.com/software/proton-paymaster-as-a-service) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** html, javascript, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- why is this needed?
- our solution
- why this? and why now?
- challenges we ran into
- what's next for proton - paymaster as a service

## Body

Inspiration Users currently have to purchase multiple tokens to interact with DApps across different chains. It sometimes restricts users from trying out new applications and games built on chains for which they don’t have the native coin. We discovered innovative work being done by amazing devs in the field of Account Abstraction, which for us is the default evolution for web3 wallets. Following this, Garvit, one of the co-founders submitted the proposal for 'Paymaster as a Service' for Polygon Fellowship and got selected. This led us further to work on the problem statement and build a better future for web3. What it does We provide a way for a dApp to sponsor gas for users who are transacting via smart contract wallets. The dApp can deploy its own paymaster contract through our platform, which helps them conditionally manage and sponsor the gas fees for their users. Why is this needed? Onboarding users on web3 is difficult due to the requirement of native tokens for gas, and complicated wallet experiences. Smart Contract Wallets using Account abstraction (EIP 4337) are simplifying that. With the increased adoption of such wallets, dApps will be able to selectively sponsor gas for their users and make their user’s experience better. Our product will help the dApps sponsor gas and manage the user onboarding. It will be done via deploying a “Paymaster” contract for each dApp that can be used for sponsoring gas. Why DApps can’t create their own Paymasters? In the future of smart contract wallets, there would be multiple wallets through which users would be interacting with dApps. Each wallet has to be audited by the paymaster before sponsoring the GAS fee to make sure the transaction sent is authentic and there is no malicious code in the smart contract wallet that would dry up the paymaster account balance. For DApps to verify each smart contract wallet is going to be a big challenge and would sink a lot of valuable dev hours. Hence it would make much more sense for dApps to integrate with a trusted Paymaster service which takes the risk and responsibility of vetting each wallet and transaction before sponsoring the GAS fee. Our Solution A platform for DApps that helps them manage their user onboarding by sponsoring gas. DApps will have the ability to sponsor gas for selected transactions for their users, which can drive certain behaviour like better conversion rate, retention, or referral. The three integrals part of the product will be: SDK for front-end integration Paymaster Contract which will sponsor and manage the gas. Dashboard and notifications for the dApp to manage the total gas spent, and leftover gas in the gas station. Why this? and Why now? In near future, EOA wallets will be replaced by Smart contract wallets because of the advantages they have to offer over EOA wallets. EIP 4337 which proposes Account abstraction on Ethereum has brought the concept of smart contract wallets closer to reality and already some big players in smart contract wallets like Argent and Gnosis safe are seeing exponential growth in their user base. Also, with the L2s adoption increasing and low gas fees, it is feasible for dapps to sponsor gas fees now. Challenges we ran into Since the whole development in the space is new, we ran into multiple technical challenges due to poor documentations. Although support from the community was insane, a lot needs to be still figured out. What's next for Proton - Paymaster as a Service Our milestones for the next 6 months are: August 2022 - Launch paymaster where if dApp signs the transaction, the paymaster sponsors it September 2022 - Ship SDK which allows dApp to send userOperations Add support for DAPPs to pay gas in any token October 2022 - Launch on multiple EVM-compatible L2s Onboard 2 dApps December 2022 Launch graph integration to add the ability to sponsor selective wallets in realtime SDK support to tell users how much gas will be sponsored February 2023 Launch Dashboard for marketers to specify various conditions with drag & drop tool to define conditions for gas sponsoring Integrate with multiple wallets like Gnosis, Argent, etc Onboard 10 dApps Link to smart contract: link Spheron Link: https://paas-i1ro6m.spheron.app/ <div