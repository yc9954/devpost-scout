---
slug: "chikara-protocol"
url: "https://devpost.com/software/chikara-protocol"
title: "Epoch Protocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 692
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Epoch Protocol

> We are putting smart contracts on autopilot, helping users automate tasks.

[Devpost](https://devpost.com/software/chikara-protocol) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[agriculture_food]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** biconomy, ethereum, javascript, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for epoch protocol

## Body

Inspiration While doing mundane tasks in web3 we realize some things need to be simplified and some normal functionalities are missing. One such thing is smart contract automation or automation of time-based or recurring tasks. While regularly claiming prizes from poolTogether(they clawback prizes if we don't claim them), we noticed there is nothing available for the end user to put their recurring tasks or some time-bound tasks on auto-pilot, thus we took it upon ourselves to build one such product that will solve various problems like Crypto SIPs, auto restaking in yield farms, Uniswap v2 conditional liquidity providing and a lot more cool stuff. Eventually, we will also be moving to provide more robust solutions to various other businesses and protocols. What it does We are enabling individuals to automate some functions on their smart contracts and protocols that they regularly use. Pitch deck - https://www.canva.com/design/DAFGatAjV78/PF9N6KnJWC2N_I700Kqn8A/view?utm_content=DAFGatAjV78&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton We provide following features as a protocol as of now: v1 (Submitted for hackathon) Users can setup their recurring task to be executed automatically. All the tasks that needs to be executed get listed on Dapp, anyone can come and execute them without even having to pay gas fee. Executors have fixed rewards so they don't have to calculate if a transaction is profitable for them or not. Real people ( Executors ) will invoke transactions for you. How we built it There are three components to the whole project Smart Contract Wallet Handles users funds, permissions and allowances Makes it very easy for user to manage his jobs and automation tasks Job Registry Creates a job marketplace for the protocol Executors can come and run any job with gasless Biconomy integration and earn rewards While users can add their Arbritary Jobs as well as Dapps(AAVE, Uniswap etc.) Specific Jobs Protocol / Destination Execution Contracts Challenges we ran into It was difficult to design an architecture for the dapp and smart contracts since the job creation part has to be arbitrary and it is pretty hard to create do bytes manipulation to create smart contracts calls data. We also had to find out a way to make the off-chain execution part as little as possible - which would’ve required a protocol specific network(blockchain) to be up and running. Smart Contract wallet was also a difficult part since the users fund management and giving compatibility for other contracts along with good security is hard to achieve. Accomplishments that we're proud of We were selected to Polkadot relayers (Accelerator program) first cohort to build the project We were successfull in creating contracts for Job Registry, Epoch Smart Contract User Wallet and other supporting contracts We were able to execute Arbitrary Jobs as well as jobs that connect to Protocols like AAVE and Uniswap (for certain tasks like automatic SIPs etc, deposit, withdraws etc.) on behalf of the user. We were able to integrate Biconomy to make the job execution part completely gasless. What we learned On the product Side We learned that UX is one of most important aspects of this project - since Automation is complex and thus we need to design the app in such a way that it is easy for both normal users as well as devs to use our dapp. On the Tech Side We learned about the nuances of creating a Smart Contract Wallet that will handle user funds and data, another thing we learned was making arbitrary smart contract calls to support our feature of delegated transaction. What's next for Epoch Protocol v2 (After the launch of V1) Along with v1 we will add our own network, that will execute tasks that has strict deadline. This network will be essential to cater B2B needs. We also intend to have a user-centric product that will be built along with the protocol, it will have the following features : Automating recurring tasks for users of certain protocols. Decentralised crypto-based SIPs. Migrating loans from one protocol to another for better APR %. Uniswap v3 like liquidity management for uniswap v2 fork ( Providing liquidity for a specific price range to cut down impermanent losses ). Providing users to create limit orders on DEXs. <div