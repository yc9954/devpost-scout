---
slug: "seed-web3-career-hub-dhrazk"
url: "https://devpost.com/software/seed-web3-career-hub-dhrazk"
title: "SEED Web3 Career Hub"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 988
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
---

# SEED Web3 Career Hub

> Hire efficiently, with on-chain profile

[Devpost](https://devpost.com/software/seed-web3-career-hub-dhrazk) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]]

**stack** amazon-web-services, assembly, digitalocean, java, jwt, near, near-sdk, node.js, react, rest, rust, springboot, typescript, web3j

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for seed web3 career hub

## Body

Inspiration As Marieke mentioned recently that we need to go back to real utility, especially in the current turmoil. Our goal is to solve a long-lasting pain: Recruitment, that exists in all companies, with web3 technology. As a recruiter: We are always unsure about the authenticity of the candidate’s profile We take extra effort doing due diligence We sometimes fire the candidate after the probation ends As a job seeker: We always get so many questions and doubts from the recruiters We are writing too many copies of resumes and profiles We realise this problem even before we graduate from universities. And it becomes more dire as we run our APAC Web3 Community. We’ve been helping to mitigate the problem manually by connecting and we decided to transform it digitally, more efficiently. What it does We aim to make hiring more efficient, with on-chain profile. We are solving 3 key problems in the Recruitment Industry: Cost of Resume due diligence a. The candidate only needs to be certified once. Unlike the conventional way where each businesses’ recruiters conduct their own due diligence repeatedly on the same candidate when they switch jobs. b. We allow users to both retrieve & mint NFT credentials c. In order to encourage transition from using web2 feature to web3, for those without a wallet address, they are still able to create profile, just without NFT credentials. Cost of Network Limitation a. By introducing the simple bounty feature, recruiters are able to allocate an affordable budget that incentives all users to recommend talents within their social network. b. A cost & time efficient way for recruiters and/or headhunter to gather a large pool of talents; While users will be rewarded for successful referrals Cost of Trust a. By depositing the bounty into a smart contract escrow account with public governance, it eliminates referrer’s worry on not being able to receive the bounty. How we built it SEED is built using an on-chain and off-chain technology. The on-chain part is using NEAR smart contracts which is build using Rust and also Assembly Script. The smart contracts - 2 NFTs contract (achievement and testimonial) and 1 Job contract. The off-chain is only use to store and run expensive on chain computation such as Job filtration, Job category and so on. The tech stack we are using is Spring Boot Web Framework (Java). For the frontend we consume both logic from smart contracts and backend using ReactJS. Summary: Backend tech Java, Spring Boot (JPA, Web, Security, Mail), Web3j and salty-coffee (cryptographic libraries), Rest API, JWT Cloud services: DigitalOcean App (autobuilt by GitHub change, docker build on any change, run as docker container) DigitalOcean Droplet (VM) for hosting Frontend DB: AWS RDS MariaDB Smart contract: Assembly script, rust Front end: React Challenges we ran into Testnet failure NEAR SDK only supports the older version of Reactjs, so we had to revert back Limited third-party APIs Limited functionality provided by near-api Nothing is available to query or index all NFTs available for a near wallet The biggest challenge was to implemnt MVP in short amount of time. We had a lot of communication at the beggining, what should be on-chain, we wanted to use backend as little as possible. Found very good tools to store and serve backend tasks in a web3 way (Using decentralized DB: OrbiDB and services: FLuence), but the learning curve could have been more than we had for finishing the hakcathlon. In implementation the authentication part was the most diffucult, we asked some help on Discord: how to verify on backend side that User successfully logged into MyNearWallet on client side. There are plenty of examples in JavaScript, but finding samples for backen (in Java) was challenging. Java libraries Web3j and salty-coffee solved our issues. Accomplishments that we're proud of One question that we received from Illia at the NEARCON stage was how do we incentivise users. Despite that the product is built on demand and we have an active APAC Builders Community with around 5,000 members, we constantly come back to this question to build a product that the market really needs. Hence, we introduce the new feature - Decentralised Headhunting Network, this time around at Metabuild. With this, recruiters are able to allocate an affordable budget to incentivise all platform users to recommend suitable talents within their social network. Being able to go back to the real utility and bring solid benefit to the recruitment industry using web3 technology without the need of massive education. What we learned In order to have a sustainable tech product, it has to fit into the economy of scale. As an example, people think of airbnb when they are looking for accommodation, grab when they are commuting. These platforms attract and match the demand & supply, providing a very efficient solution for all parties. We are trying to do the same thing for the job market. The value added is that we use web3 technology to provide more control to the users. What's next for SEED Web3 Career Hub Jan 2023 Focus group - After Metabuild, we are planning to form a focus group with 3 students from National University of Singapore, 3 recruiters in both web2 and web3 space and 3 project founders and CEO to conduct an in-depth study and improve the beta version. Mar 2023 Backendless - One of the key elements we wish to implement during iteration is to be backendless. We hope to open it up to the whole NEAR ecosystem and web3 space. Each job listing is a smart contract, which is fully transparent and immutable and can be retrieved by all other platforms and recruiters. June 2023 3rd Party Validator - In order to reach to mass users and help web2 users validate their credentials using on-chain technology, we will work with validating company to help validate web2 credentials and issue NFT badges. It works similar to twitter blue-tick. <div