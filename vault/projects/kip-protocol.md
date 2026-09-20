---
slug: "kip-protocol"
url: "https://devpost.com/software/kip-protocol"
title: "KIP Protocol"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1411
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/scientific_research"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# KIP Protocol

> KIP Protocol is the decentralised base layer that AI models, apps & data owners build on, to safely transact & monetise in Web3.

[Devpost](https://devpost.com/software/kip-protocol) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
  <sub>weak: provenance_signing</sub>
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[labor_employment]] [[scientific_research]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[financial_record]] [[web_dom]]

**stack** alchemyapi, ccip, chainlink, evm, javascript, langchain, nest, node.js, openai, polygon, postgresql, react, s3, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kip protocol
- official links

## Body

Homepage KIP Protocol MVP Base Tech GIF Your Knowledge is Power, Property and Provenance Inspiration We are a group of AI researchers & web3 natives who have been working on natural language processing, computational linguistics and large language models, from the time before AI was cool (and indeed before the space was called AI). We have deep expertise in traditional off-chain retrieval augmented generation (RAG). And while we have always been hugely excited about what AI could potentially do for humanity, we are also extremely disturbed about the corporate monopolies forming in AI. There is a great knowledge heist underway, with everything we’ve ever published on the Internet being taken without permission to train the AI models of Big Tech companies. Such is the arrogance of Big Tech that one of them has offered to pay for copyright claims of their customers if their customers steal copyrighted data. AI is an enabling tech, and monopolies in AI are much more dangerous than monopolies in any other tech area. But one thing they do need for now, is our data. Since our knowledge and data are extremely valuable to AI development, they deserve to be treated as the valuable assets they are. We call these assets Knowledge Assets, and we’re calling this movement: #KnowledgeFi We’re building KIP Protocol, an open Web3 framework to build a vibrant ecosystem where everyone creating value to AI can be treated and compensated fairly, and not have the fruits of their labour appropriated by big tech. What it does KIP Protocol is a decentralised AI framework for the creation, ownership and monetisation of knowledge assets. Creation and ownership of knowledge & data is achieved via what we’re naming “Knowledge Assets”, which are represented on the blockchain as Ethereum NFTs. (for this hackathon we have used ERC 1155, but we are also developing using the new Semi-Fungible Token standard ERC 3525) Monetization is achieved with a rev-share and accounting framework, where AI dApps (eg decentralized chatbots) interact directly with the stored data and implements a Pay-per-query business model that is distributed to the creator and all other owners of the Knowledge. We must remember that the base revenue model of AI is pay-per-query, because every user query costs GPU computing resources, which means every query costs money. Given the dynamic nature of AI, we designed our system to be extremely gas efficient. We do this by splitting ownership and transactions on two different chains, and using CCIP as an essential component to sync transactions and value changes between chains. For this hackathon, we have developed for demonstration: 2 components, namely Creation of On-chain Knowledge Asset and Monetization of Knowledge Asset Creation of On-chain Knowledge Asset: For the first step of creating an on-chain Knowledge Asset, we allow individuals to upload data files for vectorisation to make it AI-readable They can set their metadata information such as description, quantity, price per query etc. Upon creating the Knowledge Asset NFT, Chainlink CCIP is used to deploy the NFT on Ethereum mainnet and sync on Polygon. This Knowledge Asset can be traded in NFT marketplaces and can also directly interact with the AI dApps. Monetization of Knowledge Asset: A user opens up the Knowledge NFT page. There is a chatbot for users to query the knowledge base and send the question over with a payment and by making use of Chainlink’s CCIP, this is done on the Polygon blockchain for faster and cheaper transactions. Once payment is made, only the purchaser can use his wallet to sign and view the AI’s replies. There is then an option to mint the query so that the user can resell the answers either to other individuals or institutions looking to train data, or store them on-chain for perpetuity. This Query & Answer NFT is also minted on the Polygon blockchain and is accessible to trade on NFT marketplaces. Use case of Query & Answer NFT: Take for instance in an AI-powered future, a student working on a thesis took some material off a professor’s Knowledge Asset via an AI chatbot and needs to make proper referencing. That is not possible especially when all the data is encrypted and vectorised. With this concept he can mint the answer so that this source is recorded on the blockchain. In the event that he needs to provide verification, he can delegate access or transfer the token to the checker to access the encrypted source. Another use case would be community building around common research interests. Users who query from certain Knowledge Assets have a common interest. They can mint the answer which represents that shared interest and also acts as a membership of a particular community and gain gated access to a shared space. How we built it There are a number of components to build this framework for the hackathon. In total we used 4 different smart contracts and Chainlink’s CCIP function. ERC-1155 Knowledge Asset NFT contract on Ethereum - This is for the creation of Knowledge Assets. Query & Answer contract on Polygon - This is for users to interact with the Knowledge Asset, execute payment and query functions. KIP token contract on Polygon - This is the token that we created for the use of paying the transactions. Although the front end lists the cost in USD for simplification, in reality we are using KIP tokens. ERC-721 Query & Answer NFT on Polygon - If the user wishes to mint the answer as an NFT, this is the smart contract that allows it. CCIP function enables us to sync the Ethereum and Polygon contracts (1) when Knowledge Assets are created, (2) when pay-per-query transactions occur and (3) when revenue has to be accounted for and shared to the rightful NFT owners on Ethereum. When all these parts are working in tandem with each other, the sum of the parts is greater than the whole. Whereby Knowledge Assets are birthed and the concept of KnowledgeFi takes root. Challenges we ran into We found out that the CCIP waiting time for finality was rather long at about 20min. This resulted in longer test times for us. When the cross-chain transaction is successful we are also not able to know about it. If there was a webhook to notify developers, it would be very helpful indeed. Accomplishments that we're proud of We are proud to be able to successfully create a framework for any individuals to create on-chain Knowledge Assets and monetise them with a decentralized pay-per-query model. We have hopefully developed a way for us to wrest control of our economic rights over our knowledge and data back from Big Tech. Without solutions for this, ordinary people and companies will be subservient to the super models of the future, which was trained on all our data, and excluded from the economic benefits of that future. We also managed to breathe new life into AI used data, in this case the Query & Answer NFTs, which have real-life use cases especially when academics in future will transfer from being centred around research papers and books to more usage of AI applications. Lastly we feel a sense of achievement by being able to find a way to execute a multi-chain framework, using the appropriate chains for NFT ownership and trading, and interactions with AI. What we learned We understood Chainlink on a deeper level and were glad to find a perfect fit with CCIP and our AI project. We were able to have assets remain on the Ethereum blockchain and have the interactions carried out on L2s to enjoy greater speeds and lower cost. This will also allow us to be a true and open Web3 Cross-chain platform by allowing individuals in future to choose the chains they want to store their Knowledge Assets without worrying about practical matters like transaction fees. What's next for KIP Protocol KIP Protocol will build a community to shape the direction of KnowledgeFi. We will be building an ecosystem for individuals to thrive in the age of AI. We will make Knowledge into financial assets with true digital property rights and cultivate the growth of a Knowledge Marketplace where demand for Knowledge increases from AI applications and training datasets. Most importantly we allow individuals to maintain and exert control over their knowledge and not be exploited by Big Tech any longer. Official Links KIP Protocol: Decentralised AI Base Layer Website: https://kip.pro/ X: https://x.com/KIPprotocol Discord: https://discord.gg/Hma2Y6RgND Galxe: https://galxe.com/KIPProtocol Documentation: https://kipprotocol.gitbook.io/wp/ Github: https://github.com/kip-protocol <div