---
slug: "bitcoin-agent"
url: "https://devpost.com/software/bitcoin-agent"
title: "Bitcoin Agent"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 410
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "substrate/financial_record"
---

# Bitcoin Agent

> An AI agent that uses NEAR chain signatures to interact with Bitcoin L1

[Devpost](https://devpost.com/software/bitcoin-agent) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**substrate** [[financial_record]]

**stack** bitcoin, near, near-chain-signatures

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bitcoin agent

## Body

Agent Landing Page Deployed Agent AI Agent running on bitte.ai Bitcoin Agent High Level Architecture Inspiration Bitcoin lacks programmability, making cross-chain interactions complex. We aimed to bridge this gap by enabling Bitcoin transactions via NEAR accounts using AI agents and NEAR chain signatures. What it does This agent can create and send Bitcoin transactions using just your NEAR account. It can also provide information about your NEAR account and the associated BTC testnet address, including their balances. How we built it We used Bitte.ai for AI agent capabilities, NEAR mainnet and chain signatures to sign multi-chain transaction using MPC signer contract (v1.signer) on mainnet. Further we used libraries like signet.js to interact with bitcoin testnet and relay the signatures received from NEAR MPC contract. Challenges we ran into Ensuring seamless NEAR-to-Bitcoin interoperability was tricky, especially in getting signature payload from receipts_outcome of the txnHash response (it was due to a delegate call through bitte interface, due to this near-api-js function available in providers called getTransactionLastResult() couldn't extract the desired RSV signature payload ). So, we had to rewrite some helper function to extract that data manually inside our agent. Also there were some issues specific to BTC testnet4 psbt maxFee settings in bitcoin library used in this project. Due to lack of support, we had to find a workaround and set a high maxFee threshold. Although, this can easily be improved in later versions on mainnet. Accomplishments that we're proud of Despite of all the challenges, we are very proud as a team that we were able to sign BTC txns using NEAR account on mainnet with our AI Agent. We successfully built a working prototype that enables AI-powered Bitcoin transactions using NEAR accounts, making cross-chain interactions easier. What we learned We gained insights into Bitcoin transaction structure and NEAR chain signatures which is a really amazing technology for Chain Abstracted future. Also we explored the potential application of AI agents in NEAR ecosystem. What's next for Bitcoin Agent Next step is to add much more sophisticated txns on BTC L1 and move the agent to mainnet. The agent is under development and will be soon be available for users to send bitcoin directly from a chatbot interface or simply using any authentication method like X, Google account etc. The ultimate goal is to make an agent that can literally do anything and everything on Bitcoin network in seamless manner without the complexity and UX that blockchain currently faces. <div