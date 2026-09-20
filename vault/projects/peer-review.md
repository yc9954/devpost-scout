---
slug: "peer-review"
url: "https://devpost.com/software/peer-review"
title: "Peer Review"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1360
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "domain/scientific_research"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# Peer Review

> Restoring integrity to academic publishing

[Devpost](https://devpost.com/software/peer-review) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]]
**domain** [[scientific_research]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** chainlink, ethers.js, express.js, hardhat, metamask, mongodb, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for peer review

## Body

Login using Metamask and Google Scholar Profile Browse through papers already on the blockchain View your profile Upload a paper Add the abstract Submit your paper Paper status Inspiration A rising issue observed in the world of academia and research is Predatory Publishing . This refers to journals charging “publication fees” from researchers to publish papers, often those lacking the quality to have any real academic relevance. Journals don’t check the article's legitimacy, and most papers published in these journals are just derivatives of other works (plagiarism). No transparent peer-review process, even if the journal claims to do one. How do we trust if the first reviews were conducted, and second, were they conducted by qualified peers? Central authorities control journals with financial motives, there is a lot of corruption. Preference is given to people willing to pay a higher sum of money. The problem of predatory publishing would be resolved if we decentralize the system so that nobody and everybody is in power and have a system that is transparent with peers that are loyal. What it does PeerReview is a project which aims to decentralize the process of peer-reviewing research papers with the help of Ethereum, Smart Contracts, and Blockchain. Some features of PeerReview include: Completely anonymous users, we don't store any data to identify users on our blockchain Upload papers with ease, and in less than 2 minutes! Reviews are transparent and honest. We integrate with Google Scholar to generate a "trust rating" for users, and then use this to evaluate a user's action on our network. Get feedback from reviewers, and accommodate changes to your paper. Reviewers are rewarded for their work in the form of Ether. Completely compatible with Metamask! Let’s say a researcher wants to publish a paper on our network. They sign up on our platform using their Metamask Wallet and Google Scholar profile and pay a nominal fee. Through Google Scholar, we scrape information like their h-index, citations, etc to establish how valuable the user's reviews are. Chainlink helps us in the user signup process, to properly vet a user's profile on google scholar (off-chain data). We built an external adapter to access google scholar data, and tested it by running it on our own self hosted Chainlink node. Now, the user can upload a paper to our system by paying a negligible fee. Each research paper is represented by a smart contract on our blockchain. Initially, the smart contract sets the status of the paper as “Under Review”, and other researchers in the community can review the paper. Each time a review has been completed, the smart contract records the same. When the paper has reviews from peers whose h-index on our system is > 150 , it is automatically published on our network by the contract, and the status is set as “Published”. The smart contract also automatically divides the fees and a bonus to all the reviews of the paper, as a reward for their work. How we built it The diagram below gives a basic high level view of Peer Review's architecture: Peer Review Contract The central component in the whole system is the "PeerReview" smart contract running on the blockchain. The smart contract is implemented using Ethereum. I chose Ethereum because it’s one of the biggest blockchain networks and the leader behind the upcoming Web3.0 technology. Each contract consists of the following data: A unique UUID. The author’s UUID. The state of the paper. (under review/published/rejected) The actual research paper. This is stored on the IPFS network, and the hash of the IPFS document is embedded in this contract. A list of papers which this paper cites. (Paper UUIDs) A list of peers (other researchers) who have reviewed this paper. (Author UUIDs) The quality index of this paper. The contract also has methods to create "User" contracts on the blockchain. These contracts are created by verifying off-chain data using a Chainlink external adapter, which is covered below: Chainlink External Adapter To allow the PeerReview contract to verify if the user's google scholar profile is accurate, I executed a chainlink request which runs a job linked to an external adapter . I wrote logic in this adapter to communicate with the PeerReview Backend to validate the user's profile, and also return a "trust rating" for the user computed by analyzing the user's profile on google scholar. This data is sent back to the Peer Review contract using a "Fullfill oracle" response. Frontend/Backend Furthermore, I built a NodeJS + ExpressJS backend, and a React frontend to help users: Register and join our public blockchain. Publish papers onto the network, and track the status/citations of your paper. View and search other research papers. View the profiles of other researchers. I chose NodeJS/React due to its simplicity, and believe it will help us implement a prototype in a short amount of time. Challenges we ran into One of the biggest challenges we ran into was deciphering how can we trust users and papers on the network as fake reviewers could falsely verify papers on the network. To solve this challenge, we implemented something called trust rating : Each researcher on our network has a “trust rating”. When a paper reviewed by a researcher gets cited by other papers, the smart contract automatically increases the trust rating of people who reviewed the paper. Thus, the more the papers reviewed by a person get cited, the higher the trust rating of the person. We use these “trust ratings” to evaluate the quality of every paper, i.e., the quality index of a paper is now proportional to the ratings of its authors and peers. Since our network will initially have no users, each user has an initial trust rating derived from their existing academic profile. The system uses the h-index of a researcher from Google Scholar for this, but this only serves as an initial metric. We use this formula to check whether we can publish a paper after a peer has reviewed it. The h-index variable here signifies the h-index we scraped from the researcher's Google Scholar profile. Accomplishments that we're proud of This was my first time working on such a big project completely by myself. I had to juggle around building the frontend, backend, and also smart contracts for the blockchain. I learned a lot about React, Javascript, NodeJS, and Solidity by working on this project. Successfully built a complete end to end, decentralized solution to solve the academic peer review process. This solution is completely public and can be trusted by all users part of the network. No more fake "publication fees" or bribes, all research content is legitimate and vetted publicly by users on the network. I learned about Chainlink and integrated it into a project for the first time. I am proud of being able to pick it up in a short amount of time, and use it in the project to solve for a valid use case. Without chainlink, the solution would not have been completely decentralised. What we learned I learned how to use Chainlink to retrieve off-chain data on a on-chain Solidity smart contract. I hope to use this new technology in even more applications in the future! I am not a UI/UX person, but I single-handedly built wireframes and the interface for the project. This was an interesting experience, and helped me pick up a new skill, design thinking. I also learned how to properly divide my time to different components of a project. My workflow involved first getting a minimum prototype working, then polishing the user interface, and then finally integrating with chainlink to authenticate users correctly. What's next for Peer Review There is a lot of future scope for new ideas that can be incorporated into Peer Review. Some of these are: Automated plagiarism checks using AI algorithms by the smart contract. Automatically detecting citations of a paper from other websites, to increase your trust rating. Distribute rewards to authors and reviewers of papers with a high number of citations. Even more chainlink integrations using automation to update trust rating for users on our blockchain networks with off-chain research user profiles. <div