---
slug: "unpredictable-dao"
url: "https://devpost.com/software/unpredictable-dao"
title: "Unpredictable DAO"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 981
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
---

# Unpredictable DAO

> A DAO of unbiased, unpredictable, on-chain randomness

[Devpost](https://devpost.com/software/unpredictable-dao) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]]

**stack** chai, hardhat, javascript, node.js, solidity

## How they structured the write-up

- inspiration
- problems with randomness and our solution
- what does unpredictable dao do?
- how we built unpredictable dao
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- how our project utilizes polkadot & impacts on polkadot
- what's next for unpredictable dao

## Body

Unpredictable DAO logo Homepage Test out submission Inspiration Before participating in this hackathon, the Unpredictable DAO team was working on the core infrastructure for a proof-of-stake blockchain network. We have realized the importance of randomness for not only just the security of the validator picking process for a PoS chain, but also in the blockchain industry and some dapps in general. So we started researching and building a system to create randomness that is unbiased, unpredictable and accessible on-chain. We believe the best platform for such a system is Polkadot - a platform with an innovative multi-chain architecture, along with a strong parachains ecosystem and big community. Finally, the team settled on to build Unpredictable DAO. Problems with randomness and our solution In traditional centralized applications, services where many people are present don't provide enough clarity and fairness. The centralized provider can definitely lie about randomness, cheat, and adjust results based on his bias, so we have come to a conclusion that we need a workable, unbiased, decentralized random number generator. Environments like blockchains are decentralized but completely deterministic and isolated, thus making randomness fairly difficult to achieve. Some solutions were carried out for this problem. The common naive decision would normally be to use pseudorandom functions combined with changing properties on the blockchain to generate somewhat random numbers. This is often not a good idea because pseudorandom numbers often "look random" but are predictable or/and easily manipulated by block producers through censorship or block data modifications. So pseudorandom functions are definitely not the way to go, another solution is to use oracles. However, there are caveats in using oracles, with the main one being the lack of decentralization. Many existing oracles are either centralized or controlled by a limited group of node operators, which leads to centralization. Blockchains and many applications running on them currently can not safely implement randomness in their smart contracts. Unpredictable DAO solves the randomness problem by creating a system where everyone can participate in the process of generating random numbers. The smart contracts using Unpredictable DAO service pay an amount of tokens, which will be distributed to all participants. For a technical explanation, check out our pitch video right above where we talked about the technology behind Unpredictable DAO. What does Unpredictable DAO do? Unpredictable DAO works primarily as a random number generator that is unbiased, unpredictable, and usable by any smart contracts on-chain. It is a DAO in that the system works by having multiple participants join in to generate a random number, and many properties of the random number generator can be changed through voting by members of the DAO. It also acts as a service where participants can get rewarded for contributing to the DAO through fees from smart contracts or applications using the random number generator. We have built a random number generator that can create secure randomness in a deterministic environment like a blockchain, which couldn't be achievable before in a censorship-resistant, unbiased and unpredictable style without severe security tradeoffs. How we built Unpredictable DAO Conceptually, we first spent a lot of time doing research, thinking of the possibilities, and then finally ended up with a polished idea for an implementation of Unpredictable DAO that should be workable. Technologically, with Polkadot being "the internet of blockchains" and Substrate - the framework for production-ready blockchains, they have paved ways for ecosystems which support the EVM runtime environment like Acala, Astar and ICE. Thanks to those parachains, Unpredictable DAO was built through Solidity - a language that our team is very familiar with. Challenges we ran into Secure randomness is already hard to implement, but secure randomness on blockchains is much, much more difficult to achieve. The Unpredictable DAO team has run into numerous impractical ideas and failed implementations, only then to bring out the current Unpredictable DAO that we are happy with throughout all of our hard work. Accomplishments that we're proud of Again, randomness on a deterministic environment like blockchains is not easy to create, and it is almost impossible to implement such a system that is secure, decentralized, fully accessible on-chain, unpredictable and non manipulatable. We are really proud that Unpredictable DAO can solve the problem, and from that, we also wish it can bring much more possibilities to applications and smart contracts from Polkadot, Kusama and the blockchain industry in general. What we learned Aside from time management, teamwork and innovative problem solving, which are valuable skills from competing in the hackathon, we have also had a chance to expand our knowledge about the core technologies behind Polkadot, Kusama and some of their parachains, which I believe is the best thing we had received from this hackathon to further improve Unpredictable DAO. How our project utilizes Polkadot & impacts on Polkadot Thanks to Substrate and the Polkadot’s multi-chain network, parachains are highly customizable, thus making fast, decentralized EVM hubs like Acala, Astar, ICE, etc available, which are the suitable platforms that power Unpredictable DAO. Unpredictable DAO brings truly unbiased and unpredictable randomness to the Polkadot and Kusama ecosystem, which helps further expand a ton of possibilities from them without losing any security like existing on-chain random number generators. It is usable by every smart contract for decentralized applications, and through Polkadot’s multi-chain architecture, it can also be used by any parachains to further strengthen the network. What's next for Unpredictable DAO Our main goal is to gather participants from the Polkadot community to make the DAO even more secure and decentralized, as well as having the adoptions from developers to integrate our random number generator into their applications and smart contracts, expanding the possibilities of blockchains. We are working to extend the use case of Unpredictable DAO. In addition, we also hope that with the strong community and top-notch technology of Polkadot, developers can figure out a way to use our randomness to enhance their product’s security. <div