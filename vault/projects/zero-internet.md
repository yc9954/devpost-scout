---
slug: "zero-internet"
url: "https://devpost.com/software/zero-internet"
title: "Zero Internet"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 604
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Zero Internet

> Bridging internet barriers to AI and blockchain spread

[Devpost](https://devpost.com/software/zero-internet) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** chainlink, langchain, nextjs, openai, solidity, stability, twilio, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zero internet

## Body

data marketplace AI agent creation AI agent templates Decrypting and Consuming data Publishing new data NFT Address Inspiration There's a significant digital divide in my country and many other regions that ranks low in terms of stable and widespread internet access. This lack of connectivity leaves millions unable to leverage emerging technologies, further exacerbating socio-economic disparities. With many individuals also being unbanked, the potential benefits of AI and blockchain technology remain out of reach. Zero Internet aims to bridge this gap by enabling offline access to AI capabilities and data profitability, ensuring that powerful tools are available to everyone, regardless of internet connectivity. What it does Zero Internet allows users to interact with AI agents and blockchain offline. The core is a data marketplace where users can publish or purchase datasets. AI agents consume these specialized datasets to increase their knowledge base. On-chain, the smart contract controls metadata and keys for the vectors stored off-chain in a custom decentralized database, Most importantly, Chainlink Functions and Chainlink Automation are used to track and manage offline sessions/conversations with an AI agent. By enabling AI agents to respond to user queries sent via SMS, Zero Internet is breaking down connectivity barriers and making advanced AI tools accessible to millions of underserved individuals. How we built it Tool Description Lit Protocol Each content piece indexed on Zero is associated with an NFT contract deployed by the creator and is listed for a price in ETH, allowing only NFT holders to decrypt and access the data. The LIT Protocol handles encryption and signing. IPNS IPNS is used to upsert additional vectors into the AI-agents knowledge base as it grows (buys more NFT 🤭). Additionally, we store sessions of conversations into IPNS pointers which are created by API requests sent from on-chain via Chainlink Functions . Twilio Users interact with AI agents via SMS, with Twilio forwarding these queries to our backend via a webhook. Chainlink Automation Automation is used to watch upkeeps if there's a need to create a new session of conversation. Chainlink Functions Functions are used to make requests onto Lighthouse.storage API to create a new session represented by an IPNS(InterPlanetary Naming System) pointer. The Graph Indexes events emitted when a new NFT contract is deployed from the factory, enabling efficient querying and populating of Zero Data Marketplace. Smart Contracts Contract Description Session.sol Manages sessions using Chainlink automation and Chainlink functions to track offline conversations between the AI agent and a phone number. AgentFactory.sol Deploys a new AI agent by cloning the AgentTemplate.sol . AgentTemplate.sol The base contract for creating AI agents. NFTFactory.sol Deploys new NFTs used to token-gate datasets. AI agents can consume these datasets after minting/paying for the NFTs. PayableNFT.sol NFT Contract representing a published data. It is used as an access condition while encrypting documents with Lit Protocol. So users can get access to an AI by paying and minting an NFT from the contract. Challenges we ran into Most SMS providers (our implementation inclusive) have restrictions in sending SMS to some regions. An alternative setup was to use a local SMS provider in the regions to re-route the messages. Nonetheless, we can also read simulated responses from the Console for demonstration purposes. Accomplishments that we're proud of The payment router idea is something we think other marketplaces can leverage Chainlink to achieve. We also created a decentralized vector database within the timeframe by embedding and upserting vectors into IPNS pointers What we learned Gas fees aren't so much of a huge blocker to decentralization anymore. What's next for Zero Internet We plan to explore more use cases and applications for our technology. <div