---
slug: "lens-me-in"
url: "https://devpost.com/software/lens-me-in"
title: "Lens me in"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 1065
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
---

# Lens me in

> Have you ever wanted to custom your comments right on your various social media posts? Lens me in is here to help!

[Devpost](https://devpost.com/software/lens-me-in) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]]

**stack** lensprotocol, polygon, proofofhumanity, react, sismo, solidity, thegraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lens me in

## Body

Set Sismo badge restriction on your post Comment function not allowed when you don't own the Sismo badge require Inspiration One of the biggest challenges of the IT world is the sybil resistance. You have probably already seen that some Twitter messages containing keywords like "metamask" or "nft" are spammed with bot comments. Web3 makes no exception! We started from this observation and came up with a solution that would allow users to define commenting rights on their Lens post. What it does Lens Me In is an Integration of multiple projects : Sismo, Proof of Humanity (Kleros) and Lens Protocol.. Sismo and Lens being deployed on Polygon, that’s the blockchain we used too. Sismo protocol lets users mint ERC-1155 badges via modulable attesters. One of the attesters already deployed uses ZK proofs and it’s amazing! It allows anyone who meets the requirement on his source address to mint a badge on his destination address. And this, thanks to ZK proofs, is done anonymously. Proof of Humanity (PoH) is a protocol that maintains a registry of address belongings to humans. Only one address per person can be registered. One drawback of PoH is that it forces you to link your identity to an active Ethereum address. First, we wrote a Sismo generator to let anyone mint a badge proving he’s a real human. That’s great because we can now register to PoH with an inactive address (i.e. only used for the PoH submission) and then mint a badge on one of our active addresses. Lens Protocol is a decentralized social network. We built a new Lens module that lets Lens users restrict who can comment or mirror (= retweet) their post. The restriction is based on ERC-1155 tokens. Sismo badges following that standart, they can be used in our module. Lens users can now prevent bots from interacting with their posts using our Sismo-Poh badges! How we built it So in order to do that, we split the work in 3 differents parts : ReferenceModule Smartcontract : This contract which works with lens protocol will allow us to set the restrictions we want on the post. The goal of this contract is to allow only the addresses who own X ERC-1155 to post comments on the publication. How does it work? You call the contract and give in arguments the address and the id of the ERC-1155 you want to use as restriction. As a user, if the poster configured that you need to have this sismo badge to reply, and you don't have it, you won’t be able to reply and a link to the Sismo minting page will be printed. Frontend We used Lenster, but what is it? Lenster is a Lens Protocol frontend, it enables people to see lens protocol posts, comments, followers… But also to write, comment, mirror, collect posts etc… on Lens. And because Lenster is open source, we forked it, and built our new functionalities in it. Sismo badge The first use case we wanted to build was to authorize only “Human” users to comment on posts (using Proof Of Humanity) without doxing the address we used for it. So we had to create a group generator, in order to get all the addresses who registered to POH and create the sismo badge. Challenges we ran into We first thought we could easily deploy our new Lens module on testnet or mainnet. But we forgot a little detail : modules must be whitelisted by Lens Protocol. This can certainly not be achieved in two days. We then had two choices : make the demo on our local development blockchain or deploy our own version of the Lens Protocol and our new module on testnet/mainnet. The Sismo-PoH badges generator we wrote is based on the PoH registry. We wanted to combine this source of information with the BrightId registry. Unfortunately, BrightId doesn’t expose its list of profiles. In order to present our work we needed a frontend. Anyone can build a frontend on top of the Lens Protocol. We chose to fork Lenster. The problem we faced is that Lenster relies on a centralized closed source api developed and maintained by Lens. It provides developers of frontend an interface between their webapp and the Polygon blockchain. Of course, this api wasn’t aware of our new module! So we had to rewrite some Lenster code to read and write post related data directly onchain. Accomplishments that we're proud of On the second day of the hackathon, the problems we ran into made us consider choosing another subject. We finally stuck to our initial plan even if we knew that this meant that the result wouldn’t be 100% production ready. We were right. The idea was worth being implemented. We read a lot of documentation to integrate all of our components (Sismo, Lens, PoH, The Graph, BrightId, React libraries, etc.). That was not always easy but we managed to find all the info we needed. We came up with an elegant solution. In the future, using Sismo in combination with PoH is something we think will be frequently seen in the Ethereum ecosystem. What we learned We learned a lot during this hackathon: First for some teammates we learn to use the wagmi library in order to create interaction between a frontend and the blockchain. It was also the first time we forked an open source project in order to add new functionalities. Moreover, Lenster is developed in React and nobody in the team has used React before, so we learned some concepts of this framework and understand it better now. We also learn to use protocols like graphQL to get some onChain infos. We also developed our capacity to understand how a protocol works, by reading the documentation, and contracts. What's next for Lens me in Our ReferenceModule contract was designed to work with ERC-1155. That’s why the permission you can set on your post comments can not only be limited to sismo badges, but to any other ERC-1155. E.g : if you want to create a giveaway for your NFT community, you could configure that only the NFT holders can respond to your post. With such use cases, our module could be proposed to the Lens Protocol. The PoH badges generator we developed might interest the Sismo Protocol. If so, a PR on its Github repository could be created. <div