---
slug: "dao-ambassador"
url: "https://devpost.com/software/dao-ambassador"
title: "DAO Ambassador"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 679
team_size: 7
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# DAO Ambassador

> We are planning to create a service for DAO representation. DAOs will be able to issue a DAO representation token (soulbound token) and delegate certain rights to a DAO ambassador.

[Devpost](https://devpost.com/software/dao-ambassador) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** apollo-client, apollo-server, docker, eslint, eslint-2.-web-app:-next.js/litefront, graphql, graphql-code-generator, prisma, solidity, typescript, web3, web3-react

## How they structured the write-up

- inspiration## about the project
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for dao ambassador
- links

## Body

DAO Usease Ambassador Usecase Verifier Usecase Inspiration## About the project DAO Ambassador is a solution for the digital representation of DAOs. It allows DAOs to issue digital proxies to their members in the form of soulbound tokens and present them to third parties to prove their roles, powers granted, and contributions. A DAO often needs to interact with other DAOs and organizations. We experienced this firsthand when we tried to enter into B2B communications on behalf of our HowToDAO project . Our team members had to prove who they are and where they are from before anyone starts just talking to them. It seems that for many Web3 projects that are represented and managed by DAOs, this problem of digital trust is also relevant. At the same time, it is clear that the paper and electronic proxies used by conventional organizations are overhead and extra bureaucratic for such cases. Digital proxies can be one of the application use cases for soulbound tokens because the latter provide: trustworthy and verifiable fixation of assertions; timestamping mechanism; machine-readable data. What it does Our solution is a set of smart contracts and applications: 1) universal SBT contracts on Polygon; 2) DAO representation tools based on that infrastructure. SBT contracts Soul contract - identity representation contract on Polygon. Used for anchoring of all SBTs issued to a specific entity. Collection contract as soul-bound tokens storage. Web application DAO Ambassador is a web application that interacts with our general-purpose SBT infrastructure contracts but is designed specifically for the DAO representation case. Thus, it has two authentication methods for different purposes: Metamask authentication is preferred for individual delegators or representatives on behalf of a DAO if they are authorized to issue proxies independently. Gnosis Safe authentication allows DAO to sign all transactions with a multisig. So that it also provides a voting mechanism. Preferred for DAOs who use Gnosis for decision making. Each authenticated agent has to create a Soul contract controlled by the owner’s pubkey. Tying proxies with the Soul contract instead of ordinary address allows to lay down mechanisms for restoring Identity in the future (e.g. social recovery). An authenticated agent may perform 3 roles in DAO Ambassador Solution: Proxy Issuer . Proxy Issuer creates Proxy Group (SBT collection in essence) and issues an SBT token on behalf of the Representative’s Soul address. Representative . A Representative can explore his proxies issued by different DAOs and share them with Verifiers via a web link. Proxy Verifier . Proxy Verifier is either a living entity or automated agent which can: 1) Ensure that Proxy SBT exists; 2) Ensure that Proxy is not expired and still valid; 3) Ensure that Proxy is tied to the specified ambassador’s Soul address; 4) View the Proxy content (the information about the role and powers of the representative) and make the decision. Backend We made the backend to improve the UX and make it easier to showcase the technology. We cache data (collection addresses and SBT ids) to avoid unnecessary input from the user. How we built it Technical stack: API Server: Node.js + Typescript, Apollo server, GraphQL, Prisma, Web3, Docker, ESLint Web app: Next.js/LiteFront, Web3, Typescript, Docker, ESLint, Apollo client, graphql-code-generator, web3-react Smart contracts: Solidity Challenges we ran into We encountered certain difficulties while working with Gnosis Safe because it is a new technology for us. We had stuck with collection smart contract deployment via Gnosis. Accomplishments that we’re proud of We are proud of the well-coordinated work of developers and designers in a limited time. We noticed the hackathon recently and managed to cooperate and deliver a solution. What we learned Here are some points that were new to us and which we struggled to dive in when joining the hackathon: Understanding of SBT philosophy and possible use cases; Polygon blockchain specifics; Working with Gnosis Safe tools. What’s next for DAO Ambassador Possible future directions: Deeper product-market fit research; Soul social recovery feature; Data schemas for automated SBT verification. Links Web app : https://sbt.identix.space/ Web app source : https://github.com/identix-space/dao-ambassador-frontend Backend source : https://github.com/identix-space/dao-ambassador-backend Contracts source : https://github.com/identix-space/dao-ambassador-contracts <div