---
slug: "dao-gigs"
url: "https://devpost.com/software/dao-gigs"
title: "AMADAO Gig Pay"
hackathon: "Ripple CBDC Innovate "
organization: "Ripple"
winner: true
words: 505
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "user/small_business"
  - "substrate/financial_record"
---

# AMADAO Gig Pay

> Secure P2P escrow cross border payment for knowledge workers.

[Devpost](https://devpost.com/software/dao-gigs) · hackathon [[Ripple CBDC Innovate]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[immigration_refugee]] [[labor_employment]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** nextjs, ripple, supabase

## How they structured the write-up

- inspiration
- vision
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Confirming Escrow Dashboard Xumm Escrow transaction Inspiration For knowledge workers, centralised platforms like Expert360, Upwork, Fiverr etc have popularised the opportunity to work remotely and ad-hoc for multiple clients. Such platforms solve the problem of obtaining new work and managing payments. Both of these problems are no longer significant; many freelance workers have their own regular clients and the decentralised blockchain can provide payment and security. In many cases work can be performed between the Client and the Worker peer-to-peer (P2P) with no recognisable benefit provided by the centralised work platform. Specifically, Ripples' decentralised ledger makes it possible to lock a payment for automated release based on a set of conditions via their built in Escow facility. Vision We've previously developed solutions in this market and implemented CBDCs (APIX Singapore Sandbox) and have a strong vision of how bank backed digital currencies can transform this space. Workers in all corners of the globe could receive funds in their regular bank accounts in an instant without a third party intermediary. In Phase I, we've developed a simple dApp for inclusion in the Xumm xApps library that solves the required workflow of a P2P interaction between a contractor and their client. Our goal has been to help the Ripple team see the potential in this market segment and consider supporting our collaborative implementation of CBDCs for this application in Phase II. What it does With AMADAO Gig Pay: The contractor can create a job, set the licensing, terms and attribution all in a few simple steps. The client receives the quote, and should they accept, proceeds to fund the escrow on XRPL. The escrow contract resides on the blockchain and ensures both parties fulfil their obligations without risk. Iterations of the works continue through convenient messaging and progress updates stored in the contract. On final acceptance, the contractor is paid out automatically, work and rights transferred. This all sounds complex, but it's all done through a clean, familiar UX and tidy dApp that guides users through the process. How we built it We're experienced in developing escrow smart contracts and P2P payment solutions. In the case of Ripple there was no need for a Smart Contract. Calls are made over secure websockets and integration with Xumm wallet to sign the transactions and secure the funds on the ledger. Accomplishments that we're proud of The simplicity of the implementation. Demonstrate to the Ripple team the benefits of including the Escrow capability in the CBDC roadmap. What we learned XRPL offers a relatively simple 'out of the box' escrow capability. The implementation was more akin to implementing an API than a the usual work effort required on the blockchain. What's next We'd really like the Ripple team to consider a CBDC implementation for their escrow capability. This would be the cleanest and simplest way forward. Alternatively, we'd like to investigate our own escrow Smart Contract approach within the supported capabilities of trustlines or another payment channel that receives CBDC support. Application and acceptance in the Xumm xApp list. <div