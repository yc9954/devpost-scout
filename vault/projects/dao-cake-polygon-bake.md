---
slug: "dao-cake-polygon-bake"
url: "https://devpost.com/software/dao-cake-polygon-bake"
title: "DAO Cake (Polygon Bake)"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1183
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# DAO Cake (Polygon Bake)

> No code. No token. DAO tooling for web3 communities & startups.

[Devpost](https://devpost.com/software/dao-cake-polygon-bake) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[civic_government]] [[finance_payments]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** filecoin, hardhat, ipfs, nextjs, polygon, react, solidity, spheron

## How they structured the write-up

- inspiration
- what it does
- architecture
- accomplishments that we're proud of
- what's next for dao cake (polygon bake)
- business model
- why dao cake on polygon?

## Body

Our vision Market No Code. No Setup. Inspiration We've been working with DAOs over the last 10 months to better understand their needs. The inspiration for DAO Cake came from those discovery interviews with founders of DAOs and new members. What we found is that for every tokenised DAO there were at least 10 more that were not! We learned that web3 communities with tokenisation in their roadmap still needed the tools of DAOs: proposals, voting, payments, equity share tracking on chain ....yet without their own token; More so, as many of these projects were early with many decisions still to be made; they needed the tools to be easy to use, easy to simply get started; without complex configuration or dev resources. From our interviews; consistently we heard that the founding process was full of excitement and energy, everyone involved wanted the same things. However, if there was one thing that caused fiction it was the arguments over contributions which impacted that founding energy. DAO Cake sets out to solve that issue. For the BUIDL IT hackathon we’ve focused on the requirements prior to the token generation event. This is often the most troublesome; in the absence of a DAO’s own token there needs to be a mechanism for trust. What it does DAO Cake solves the problem every multi founder team experiences: measuring and rewarding contributions. The typical (imperfect) approach for startups is to split equity equally between each member of the founding team, with the expectation each is bringing equal value. This is not a solution for DAOs as the entire founding community are the ‘founders’. Even if still at the infancy this could be ten or more people committing time and effort in varying degrees to form the DAO. Polygon provides an on-chain ledger and runs the most widely used and readable industry standard smart contract language (Solidity). DAO Cake achieves reliability and security benefits by writing transactions via the Polygon chain at a fraction of the transaction cost of Ethereum. The contributions are transactions which claim an amount similar to IOUs (I Owe yoU). In our case, there is no ‘I’ so we term these DOU (DAO Owes You) or ‘Dough’. This makes the dApp easy to use and suitable for startups and communities that do not know if they are going to ultimately generate a token, they may simply have a founding event where all the contributions (DOUs) are tallied and the equity share split accordingly to each contributor. We call this event ‘Baking’. Beyond the hackathon we’ll continue to add features that will allow various forms of Token generation methods for the Bake: Airdrops, NFT Badges etc for contributors. Polygon offers the ability for DAO Cake to 'Bake' ERC20 and ERC1155 tokens through to Ethereum should the DAO wish to tokenise. DAO Cake brings to Polygon a powerful tool to serve the thousands of new web3 communities and startups. Beyond DAO Cake, our team at amaDAO.io have been working on a suite of products to serve DAOs in facets relating to the future-of-work. Architecture We’ve kept the model simple yet sufficiently complex and considered for this application. You could say we did not want to “over cook it” (Cake pun intended). We believe the best smart contracts are simple and easy to read so that anyone (technical or not) can understand what is happening. We also wanted to keep this DApp open for anyone to use. With more time we can assess market needs and adjust the implementation where needed (see: our roadmap) Smart Contracts Solidity (EVM Compatible) - Secure, type-safe and readable Event emitting - For integration with GraphQL (tracing / audit capable) Simple extensible model based on: Proposal -> transaction lifecycle through voting which can be easily adapted to various types of work associated with an organisation. Inbuilt consensus rules and the ability to update though a proposal and voting. External ID fields to assist integration with external databases. On-chain data maintained to only the critical elements and references necessary for on chain actions. Blob link (immutable IPFS storage) to encode references to large data PDF for invoices, proposal docs etc Hardhat test cases, deployment to Mumbai network Bake of ERC20 Tokens or ERC1155 NFT to members (manually load recipients) Front end MVP NextJS / TailwindCSS / React IPFS NFT.Storage for uploading of Proposal / Claims documents Light use of Supabase DB for managing public vs private DAO listings Services approach to encapsulate Smart Contract layer Deployed decentralised front-end using Spheron with Filecoin storage. A fully decentralised web3 dApp DAO Cake's backend is decentralised on Polygon; File storage on Filecoin, served over IPFS. The front-end is decentralised through Spheron deploying to Filecoin. This architecture achieves a true decentralised dApp. Accomplishments that we're proud of The DAO Cake Smart contracts are complex yet easily read. Hitchens CRUD & Open Zeppelin libraries abstract deeper operations; combined with the repository approach with shared entities the high level the contract DAO Cake.sol provides an easy to read & implement interface. The BUIDL IT designathon encouraged us to complete our next milestone toward 'Cakery - DAO Operating System' our full featured Native App version of DAO Cake. We're particularly proud of high-fidelity prototype and it's already proving a valuable tool for feedback as we commence development. What's next for DAO Cake (Polygon Bake) Implement Smart Contracts on Polygon (DONE) dApp services layer connected to contract on Mumbai Testnet (DONE) Complete front-end of dApp MVP (90% DONE) UX Design for Native App (DONE) Implement ‘Bake’ Smart Contracts for Token pay out or NFT Badge awards to members (DONE) User interface for Baking actions - Options for filtering based on DOU etc. Customer testing of dApp & feedback Generate Internal $DOU token with tokenomics to incentivise participation in voting/proposals Launch dApp on Polygon Mainnet Build iOS and Android 'Cakery' native apps Launch dApp with chosen business model (Token, SaaS, Service fee?) Assess other applications: eg: measuring open source GitHub contributions. Business model DAO Cakes’ target audience is both web3 startup and DAO founders. We’ll publish the product to Product Hunt, Indie hackers, Reddit and through founder niche campaigns. We’ll generate users through campaigns we’ve planned for amaDAO which include a web3 jobs marketplace and an on-chain CV; the target audience is the same. Revenue will mostly come through amaDAO products and add ons. We’ve had little time for gauging reaction, however potential business models for DAO Cake include the following: Monthly SaaS fee per seat or per organization (includes support) A small percent eg: 5% of $DOU on a TGE Percentage fee per each block signing event. Why DAO Cake on Polygon? There are currently approx 4,800 indexed and tokenized DAOs. We’re targeting the 40k+ DAOs who are essentially startups or web3 communities that have not yet tokenized or formalised their structure. These organisations want the benefits of an Ethereum native token without delays and high gas fees. We’re excited by the potential to simplifying fledgling ‘DAO’ operations and payments. But also excited by the potential to bring thousands more daily transactions to the Polygon network and its' ecosystem partners. <div