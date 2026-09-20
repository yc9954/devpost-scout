---
slug: "harbs"
url: "https://devpost.com/software/harbs"
title: "Harbs"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 655
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Harbs

> Through a Harberger Tax NFTs standard we create, we make a Proof of Concept to administer ads as real estate, providing a crypto native and more ethical way to do advertisements.

[Devpost](https://devpost.com/software/harbs) · hackathon [[EthCC Hack 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** ethersjs, graph, hardhat, hardhat-deploy, ipfs, parcel, polygon, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for harbs
- links

## Body

Screenshot of the ad manager website An ad on a web3 website Inspiration We have been passionate about Harberger Taxes for a while, and in ETH Barcelona decided to join the next Hackathon so that we can have an excuse to build it. Harberger Taxes allow for efficient resource management, and taxes can be used for hard-to-fund purposes such as public goods. Making a solution for real estate management, either IRL or digital assets, or ads, or providing governance experiments (like "seats" that are Harberger NFTs) is exciting. What it does Open the frontend, and you can see a marketplace of ads real-estate . You can buy them and display any image you like for as long as you remain the owner of the real-estate and pay due taxes. The taxes can be collected and sent to the tax collector designated during the NFT collection creation. The payments are made in wMATIC in our example (can be changed during NFT creation). The frontend is self-service , anyone can come in and create a collection (without permission) representing advertising real-estate which they are putting for sale. Apart from that, we built a draft ERC-5320 standard that can be used for the general purpose of Harberger Taxes. It's here: https://github.com/ethereum/EIPs/pull/5320 How we built it First day at the venue internet didn't work very well so progress was slow and mostly brainstorming, and figuring out frontrunning issues with the standard. Second day we just worked at the hotel to avoid gambling on the internet working or not. We used: Hardhat to build the smart contract and the interfaces, The Graph to make an indexer for fast queries (and allow web2-like pages to fetch the ads), Polygon Mumbai to deploy the NFT and factory smart contracts, accepting wMATIC (and any ERC20) as a currency. Parcel, React, Typescript to make a marketplace and ads management front-end, and to interact with the contract. Also to make additional demo front-ends showcasing the advertisement display on a popular website. IPFS to store images uploaded by the front-end. Challenges we ran into Venue internet halted progress Polygonscan getting down often (especially Saturday evening) Mumbai RPCs getting down often (settled for Ankr and AlchemyAPI). Scope creep and figuring out deal-breaking edge cases (frontrun related) during the first day, that had to be solved at the interface level. Many "fix later" ugly hacks. Accomplishments that we're proud of Hacking together a PoC ad injection React component in like 10 minutes Built a little ecosystem pretty fast: ERC-5320, HarbergerAds implementation, HarbergerAds frontend, a subgraph, a little hook + component that can be injected into React apps. What we learned So hard, we had many dumb mistakes we swiftly fixed along the way, but we were too focused to pay attention, maybe: Streaming ERC-20s generates a lot of issues. It's easier to just use OpenZeppelin ERC721, explorers are often non-compliant with the minimal implementation and it creates headaches. Planning around food and coffee is vital for a hackathon (especially if you stop attending the venue). Organization is pretty difficult, especially for large scope projects like this one. Often the team members will work in "surprising" ways and you need to be able to go with the flow. What's next for Harbs This app could be way more refined, attractive and usable: Remove the hacks in the frontend, and some hardcoded things. Pass URL in the ad. It doesn't make sense to have an ad that's just an image! The change is not difficult, but since we're a big team, we couldn't coordinate around it on time. Make a proper ad library, it should be an NPM style utility function. Make the ads a bit prettier. They should provide a link the owner passes, and a link to the frontend so that a potential buyer can access it and acquire it. Links App website Repository Draft EIP for Haberger Tax NFTs Ad Display React Component Ad Display Website <div