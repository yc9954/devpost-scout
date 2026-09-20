---
slug: "social-defi-vrd1js"
url: "https://devpost.com/software/social-defi-vrd1js"
title: "Social DeFi"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1333
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Social DeFi

> Use web3 social network in a cooler way interacting with DeFi protocolos without realizing it

[Devpost](https://devpost.com/software/social-defi-vrd1js) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]]
  <sub>weak: general_public</sub>
**substrate** [[financial_record]]

**stack** aave, chainlink, etherjs, hardhat, javascript, lens, mumbai, polygon, react, remix, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for social defi

## Body

1. Launch App 2. Connect wallet 3. Sign in with Lens 4. Set your profile 5. Select create profile 6. Create profile 7. Set default profile 8. Click on Set default profile 9. Select default profile 10. Click on Set follow module 11. Select FlowmiFollowModule 12. Search for a profile with DeFi follow mode 13. Now you can DeFi follow 14. If you are the last follower of this round 15. Reload to see if you won 16. In the main dashboard, claim your prize 17. Now you earned WMatics! 18. You got new NFTs of your friends 19. And also your profile NFT! 20. Now Txs and infra 21. Quiknode Mumbai Testnet NODE 22. Tx of fees to the AAVE pool 23. ATokens waiting to be raffled 24. Redeeming of ATokens 25. VRF consumers 26. VRF activated Inspiration With the emergence of Web3, we have seen how new technologies such as DeFi, NFT, and tokens have gradually entered common use. Defi provides compelling advantages over traditional finance along the verticals of decentralization, access, efficiency, interoperability, and transparency. However, even with these advantages and the advancement of Web3, the common user misses the great opportunity that exists in DeFi due to the difficulty in the user experience, complexity, and the number of things to do and information on DeFi. The web3 adoption started with DeFi, but to get to the next 1 billion users, we need something more. For many, the next big revolution comes from social web3. Social web3 wants to give users back control over their data on social networks. There are several new protocols focused on this. One of these protocols is Lens-protocol . Lens allows us to build social networks through NFT. The Profile NFT is the main object in the Lens Protocol. It is ownership over this NFT that gives you control of your content. The Profile NFT contains the history of all of the posts, mirrors, comments, and other content you generate. Something interesting about Lens is that it allows us to program and interact with contracts when, for example, following another profile. The Profile NFT is the main object in the Lens Protocol. It is ownership over this NFT that gives you control of your content. For us, a social network is the next killer app for web3. Now, imagine combining the power of a social network with existing DeFi protocols. Social DeFi was built to demonstrate that it is possible to use DeFi protocols in an entertaining and different way without the user noticing the complexity of what is going on. What it does Social DeFi allows a user to interact with other users with actions like following, creating content, etc, and at the same time using DeFi protocols. We created a fun way to combine the act of following a profile on Lens with using an Aave pool to lend tokens. We call that contract Flowmi. Flowmi is a 🌿 Lens-protocol follow module, which is like following someone in a decentralized social network, but in a cooler way. What is special about Flowmi is that by following a profile with the FlowmiModule, you enter a raffle associated with that profile! 🎲 Flowmi will ask you for a $1 dollar contribution to the pool, and when a number of followers are gathered the raffle is activated and one of the followers gets the prize!🏅🏅🏅 But not only that! while the fees are in the contract, they earn interest by depositing the tokens in a liquidity pool provided by the 👻 Aave protocol, and if you win the Flowmi Raffle, you get a prize in Aave Wrapped Matic Token , which you can redeem for Matics anytime you want! it will earn interest while you don't redeem it!! 😎. To be able to perform this task, Flowmi uses two Chainlink technologies, the 🐸 "Datafeed" to calculate how many Matics are equal to the $1 dollar fee by the time you use the FlowmiModule, and the 🐸 "VRF" to calculate verifiable random numbers for the raffle. Have fun flowmin with your friends!🥳 How we built it Frontend: Webapp built in Remix with TypeScript language. Remix is a framework focused on building web apps with a better user experience. For the UI we used the Chakra UI library . Etherjs the make the transactions with the Blockchain. Blockchain: 🌿 Lens-Protocol : Lens Protocol is a composable and decentralized social graph, ready for you to build on so you can focus on creating a great experience, not scaling your users. Social Defi uses Lens so you can access Flowmi functions and play with your Lens frens with your Lens profile! 🐸 Chainlink Datafeed : Chainlink Data Feeds provide a secure, reliable, and decentralized source of off-chain data to power unique smart contract use cases for DeFi and beyond. Flowmi uses this tool to always charge a $1 dollar equivalent of WMatics. 🐸 Chainlink VRF Chainlink VRF provides cryptographically secure randomness for your blockchain-based applications. Flowmi uses Chainlink VRF to select the winner between the followers in the current raffle in a verified way! 👻 Aave : Aave is a fully decentralized, community-governed liquidity protocol to earn interest, borrow assets, and build applications. Every fee transfer to a user is deposited in a liquidity pool to earn interest. And they will keep on earning interest until the winner redeems them! Network: The platform uses Polygon network as Lens protocol is deployed on Polygon. Polygon's eco-friendly blockchain allows each publication on Lens Protocol to have a low carbon footprint while on a low-cost, secure blockchain. As developers, one of the best features of Polygon is Mumbai tesnet. It's amazing how well it works 🙌. Thanks to that we were able to deploy quickly and test faster. All these pieces work together in the Mumbai Testnet of Polygon through a Quicknode Polygon Mumbai Testnet node, as shown in the diagram below. Challenges we ran into Compatibility of contracts in Mumbai Testnet. Integration of Raffle logic, Chainlink Datafeed, Chainlink VRF, and Aave into a Lens Module. We had to create a couple of views to create Lens profiles and set them up Accomplishments that we're proud of It all started as an idea. How to make one profile follow another and at the same time use DeFi. We knew it was theoretically possible but putting all the pieces together makes us really proud. On the other hand, for us, improve the UI/UX in web3 is too much important. In web3, we usually sign transactions without knowing how much we are going to pay in fees and shares. We also do not know how much is left before the transaction is indexed. We wanted to show the approval cycle of each transaction in a clear and beautiful way. Each transaction shows each fee that is going to pay the user and what is going to be done with their funds. What we learned We learned a lot about social web3 and the use of NFT in social networks. The most important lesson was the development of this MVP. Being able to connect Lens with Aave when doing a follow is the first step towards infinite possibilities. What's next for Social DeFi Create more and more different follow logics with more DeFi protocols Create contracts for other different actions like doing a post or collecting. Integration with some push notification protocol (PUSH or XMTP) to send a notification to the winner. Podium of top Social DeFi users. Control of parameters of the raffle to the user. Data indexation to improve user experience and add the possibility to show more information. Proof of reserve of the amount gathered to be raffled by every user. Make this kind of raffles obsolete: With little modifications, you could do this kind of raffles in social DeF with your followers without needing any extra tool or fintech, just set your flowmi module, set the rules to raffle your funds, your followers funds or a mix of both and go! <div