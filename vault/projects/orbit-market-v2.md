---
slug: "orbit-market-v2"
url: "https://devpost.com/software/orbit-market-v2"
title: "Orbit Market V2"
hackathon: "Evmos Momentum Hackathon led by Web3Scholarships (Deployment required for prize)"
organization: "Huobi"
winner: true
words: 1180
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
---

# Orbit Market V2

> After creating Evmos' largest NFT marketplace, we deployed V2 with improved efficiency, new features and a greater focus on community. Orbit is now the default NFT Market in the Chain.

[Devpost](https://devpost.com/software/orbit-market-v2) · hackathon [[Evmos Momentum Hackathon led by Web3Scholarships -Deployment required for prize-]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** amazon-web-services, docker, graph, javascript, mongodb, react, redis, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orbit market v2

## Body

Inspiration As the creators of Orbital Apes NFTs, we wanted to provide our users with the best utility and functionality for our collection in the chain. As we all know, an NFT can't really thrive without a vibrant marketplace where people can trade and interact with the community, and that's where Orbit Market came from. We needed to provide the infrastructure for our users to engage with their NFTs, and we took this a step further to provide a platform that would serve all Evmos NFTs and users. We were the first to move in, and our offering was captivating enough to allow us to capture the full space, so Orbit Market V2 was our way to provide people with even more functionality and utility as a reward for the loyalty they've given us, the feedback they provide and the high user engagement we got in the platform. What it does Orbit Market is a public NFT marketplace run by the Orbital Apes. It provides Evmos users with free infrastructure to create and trade NFT's. For NFT buyers, it allows them to trade in different ways, such as direct listings, holding an auction, making collection offers and offering a bunch of NFT's as a bundle. For project creators, it provides them with the infrastructure for their users to trade the NFT, and also gives them access to the largest NFT community and potential buyers for their collections. The highlights in Orbit Market V2 are: Auctions Bundles NFT Categories Notifications Multi Currency Support e.g. Atom and Osmo (ERC-20 IBC Representations) Significant decrease in loading times With all of these features, we sought out to be pioneers in what is offered in the chain. The most important of these would be the Multi Currency Support, as we are one of the first dApps in Evmos to meaningfully implement the IBC module in a practical scenario. With our platform, users can have a taste of one of the most promising features in Evmos, which is the ability to use tokens from the entire Cosmos ecosystem. Overall, we were extremely excited to see that users in Evmos chose Orbit as the default platform, and their usage and support has helped us build an even better version and create a future roadmap that will continue to enhance their experience. How we built it Orbit uses solidity smart contracts on Evmos to handle the sales, offers, auctions, and transfers of NFTs as well as royalty payments to creators completely on chain in a fully decentralized manner. We host our own graph protocol to index the events of our smart contract and sync the database to the current state of our marketplace. The frontend queries our graph to allow users to view NFT collections available on evmos and participate in buy/selling, creating offers, creating bundles, and creating auctions with NFTs. Challenges we ran into On the tech side No native support for Graph Protocol services on Evmos: This was solved by hosting our own version of graph protocol to evmos with custom configurations to work with Evmos Slow loading times of NFT data: Originally we queried NFT metadata using the evmos RPC, this caused slow load times across the site. To solve this we hosted a redis cache that syncs and stores NFT metadata for collections on Orbit which greatly increased load times. On the marketing and support side: Once the platform was built, we had to get it across to our potential users. We knew we had built something reliable and useful for the community, but now it was time to onboard users. We approached multiple strategies that ranged from partnerships with other major projects from the ecosystem to engaging with informative and popular influencers in the space that could help spread the word about our offering. Coordinating such a large approach was complex at times, as we dealt with dozens of people that helped us spread the word and we had to coordinate multiple marketing events that would cause an effect on people. However, as time passed and we got to know our partners better, our workflow improved greatly and we got to become a recognized name in Evmos. Once we onboarded users however, another major challenge came to us. We are now serving thousands of users and hundreds of daily active users, so we commonly get questions about how the platform works, we have to troubleshoot any problems that the community faces and at times this becomes a time consuming process. For this, we have designed guides and trained our community mods to help address questions, so these challenges have faded for the most part but we do understand that this will be a constant in anything new we launch, so we'll be prepared for it. Accomplishments that we're proud of Some of our greatest achievements are: Reached 200,000+ Evmos traded volume Listed 30+ different collections We have 30,000+ Unique NFT’s Listed 5000+ Individual Sales Captured 99%+ market share These numbers describe a bigger picture, which is widespread adoption of our platform in the evmos ecosystem. We have enthusiastic users that continue to trade in Orbit and suggest new features so we have an ongoing feedback loop that helps us further improve the marketplace. We appreciate the community we've built, as they are the most important part of our platform so we're proud to deliver the best for them. What we learned One of the most important things we learned is that even though Evmos is still a new chain and the community may not be as big as others, it is a community full of life and excitement for what's next to come to the chain. Our users have always provided us with their full support, and we realized that having this connection with the community where they become part of the marketing and they are promoting the platform themselves is one of the most important assets to have. Once people get into the ecosystem, they want the ecosystem to thrive so they act as agents that share all the recent developments in the chain and on our projects and help us expand our reach way more than what we could do by ourselves. Another valuable insight we got is just how powerful Evmos is, and the potential it has for the future. As solidity developers with a background on EVM, we were surprised with the simplicity of how we can implement what we know on this new chain, and just how further we can go if we consider the Cosmos SDK connection. We can't wait for more features to come live in Evmos and are perplexed about what we'll be able to build as the chain grows. What's next for Orbit Market V2 As with every other project we have, we will continue to listen to the community and implement their feedback to serve them better. Our path to growth is one of constant development, so we continue to add features by the day, and we constantly evaluate what our next path should be in order to cause the greatest effect. <div