---
slug: "applauds-dhlt5p"
url: "https://devpost.com/software/applauds-dhlt5p"
title: "Applauds"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 733
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Applauds

> Take ownership of your skills.

[Devpost](https://devpost.com/software/applauds-dhlt5p) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[education]] [[finance_payments]] [[labor_employment]]
**user** [[developer]] [[educator_student]] [[general_public]]
**substrate** [[financial_record]] [[structured_db]]

**stack** alicloud, chainlink, django, javascript, postgresql, python, solidity, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for applauds

## Body

Inspiration Currently, developers face difficulties in showcasing their skills effectively, as all their data is tied to a centralized platform. If platform shutdown, users risk losing all their data. Additionally, because data is controlled by centralized platforms, they restricts users from searching for and socializing with others based on skills, leading to an influx of irrelevant advertisement messages and a significant waste of time. Our project, Applauds, aims to empower developers to truly "own" their skills by publishing their achievements on the blockchain. This approach makes the developers' skills searchable and more easily discoverable by others. Beyond this, by integrating payment and chat functionalities, we introduce a minor cost for sending messages, which the sender has to bear. This measure is designed to reduce meaningless advertisements and spam, thereby enabling users to engage in high-quality social interactions. In essence, Applauds aims to liberate skills from the confines of centralized platforms and foster meaningful connections among users in a decentralized environment. What it does With Applauds, any organization (such as learning platforms like Coursera or Alchemy Academy) can publish learning tasks on Applauds. Subsequently, developers can complete courses on these platforms and earn a non-transferable NFT (Non-Fungible Token) as a certificate. This allows developers to showcase their skills on the blockchain in the form of these NFTs, making them discoverable by any one. If the individual is a job seeker, this facilitates their discoverability by HR through skill-based filters, effectively becoming a candidate for companies. On the other hand, if the individual is an entrepreneur, they can leverage their blockchain-verified skills and achievements to make a more compelling case when pitching to VCs or other fundraising institutes. How we built it In the user achievement verification process, one of the most crucial aspects for us is enabling smart contracts on the blockchain to access users' off-chain learning outcomes, as these constitute their "achievements". To facilitate this, we use Chainlink Functions to relay data from learning platforms to blockchain contracts. Furthermore, in the social features, to ensure message authenticity, we created a distributed message protocol allowing users to sign their messages and bind tips with their messages. This adds an additional layer of trust and integrity to the communications. We store large volumes of social data off-chain, while utilizing smart contracts for storing signature information and handling asset transfers. In terms of Web2 backend technology, we leverage Alibaba Cloud for hosting and utilize a Postgres database to store all the data coming from the backend. Challenges we ran into We lacked experience in balancing on-chain contracts with off-chain business logic, so we were uncertain whether to store chat messages entirely on-chain or only partially. Ultimately, we opted to store signature information and asset transfers transactions on-chain, while keeping the actual messages in an off-chain database. Additionally, we were not familiar with the various functionalities of oracles, so we spent some time researching to learn about Chainlink Functions. Eventually, we integrated them into our user contracts to facilitate access to data from learning platforms. Accomplishments that we're proud of Our team comprises front-end, back-end, smart contract engineers, and designers. This was our first endeavor in collectively implementing features we were passionate about and genuinely aiding every developer through our project. Additionally, we successfully integrated Chainlink Functions into Applauds seamlessly, enabling secure access to off-chain data. What we learned We conducted numerous experiments concerning the integration of user data in on-chain contracts with data from off-chain learning platforms. Many approaches struggled to ensure data security. We dedicated some time to exploring how Chainlink Functions can securely access off-chain data in a decentralized manner, significantly enhancing the usability of smart contracts and extending them into "hybrid smart contracts". For the variety of tasks that we plan to implement behind Applauds, Chainlink Functions can be leveraged to interact with a variety of Web2 APIs. What's next for Applauds At present in our project, we only support users in publishing learning-related tasks to encourage learners to engage and complete them. In the future, we plan to expand the types of tasks, allowing the publication of bug bounties, GitHub PRs, hackathon awards, and any achievements related to developers. Chainlink Functions will be heavily leveraged in this regard to interface with all forms of "achievements." Additionally, we will support integration with a broader range of Web2 platforms, to create a more comprehensive developer profile that is discoverable and showcases their achievements. <div