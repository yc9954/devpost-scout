---
slug: "universal-adapter-protocol"
url: "https://devpost.com/software/universal-adapter-protocol"
title: "Universal Adapter Protocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 492
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Universal Adapter Protocol

> Make trustless agreements using only JavaScript. Access data from any Web 2 resource to calculate how much value to transfer from the agreement creator to the redeemer.

[Devpost](https://devpost.com/software/universal-adapter-protocol) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** chainlink, ethers, foundary, google-cloud, hardhat, ipfs, javascript, next.js, react, solidity, typescript, vercel, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for universal adapter protocol
- information

## Body

Home Page Create agreement Manage deployed agreements Redeem agreement View redeemed agreements Try it out at uApp.link! View example agreement scripts to see how to write your own. Watch the video here! Inspiration The goal of this project was to enable developers with zero blockchain experience to deploy trustless agreements that depend on Web 2 data. What it does First, an agreement creator writes JavaScript which returns a number indicating the amount of MATIC to transfer to the redeemer. Then, the script is uploaded to IPFS and is used to mint an NFT agreement contract, locking funds deposited by the creator. Prior to the expiration date, the agreement can be redeemed, triggering a Chainlink oracle request. All oracle nodes independently execute the script and aggregate their responses on-chain. The median return value is then sent back to the agreement contract, paying the redeemer what they are owed and sending the remaining balance back to the creator. How we built it This project utilizes the Universal Adapter, which is an open source tool developed during a previous hackathon that allows a Chainlink decentralized oracle network to execute arbitrary JavaScript code and return the aggregated response on-chain. Check this out for more information on the project. The agreement registry contract allows for creation of individual NFT agreement contracts which are minted to the redeemer's address. Upon redemption, the redeemer provides all required input variables. Then, the agreement contract sends a request to the Universal Adapter with the input variables and the IPFS content ID of the script that was used to make the agreement. Finally, the response is sent back to the agreement contract via a callback, distributing the funds. The smart contracts were created by two developers, one using Foundry and the other using Hardhat. The frontend was made with Next.js and uses Ethers and Wagmi hooks for interacting with the blockchain; it is hosted on Vercel. The Chainlink nodes, databases and function-as-a-service containers are hosted on Google Cloud Platform. Challenges we ran into In addition to writing multiple smart contracts, deploying a sophisticated frontend and creating example use cases, it also required setting up infrastructure and paying to host three separate Chainlink nodes, databases and Function-as-a-Service containers. Accomplishments that we're proud of Despite the time zone differences between the UK and United States, the team was able to coordinate and develop a fully functional prototype that can be used by anyone on the Mumbai network. Our smart contracts offer both security and gas-efficiency, while our frontend delivers a seamless user experience across desktop and mobile devices. What we learned Prior to this project, the team had almost no experience with React. However, in just three weeks, we all learned how to create performant Web 3 frontends using Next.js and Wagmi hooks. What's next for Universal Adapter Protocol We've got plans, but you will have to wait and see! 🤐 Information Agreement Registry Contract Address: 0xC1753660cC46dfabf9ea4328D10a79dAa2D661EB Universal Adapter Smart Contract Github Repository: <div