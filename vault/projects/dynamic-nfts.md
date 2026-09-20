---
slug: "dynamic-nfts"
url: "https://devpost.com/software/dynamic-nfts"
title: "Dynamic Metadata"
hackathon: "Theta Network 2023 Hackathon"
organization: "Theta Labs"
winner: true
words: 475
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Dynamic Metadata

> In-game actions are reflected in the metadata of assets through the 0xygen plugin for Unreal Engine, thereby creating truly dynamic NFT assets to make your gameplay experience unforgettable.

[Devpost](https://devpost.com/software/dynamic-nfts) · hackathon [[Theta Network 2023 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** amazon-web-services, c++, google-cloud, javascript, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dynamic nfts

## Body

Inspiration We're inspired by developers making awesome games and our mission is to help them achieve their creative vision through our flexible and simple API toolbox. We aim for a seamless user story, with our servers doing the heavy lifting so the developer can focus on their game, and the gamer can focus on enjoying their experience. What it does In game actions are reflected in the metadata of assets through the 0xygen plugin for Unreal Engine, thereby creating truly dynamic NFT assets to make your gameplay experience unforgettable. In this demonstration, a playable NFT character from our partners at FuseWars kills another character, triggering an armor upgrade and the gamer's kill count to be updated in the metadata. The armor is reflected in a visual update to the NFT, name update, and kill count attribute. These NFTs are fully playable, tradable, and most importantly, dynamic . How we built it The Dynamic Metadata feature is a natural extension of our original feature set, which involves wallet validation and syncing of NFT metadata in-game. In basic terms, the plugin sends and receives information to our backend server through a RESTful API. The backend server validates and processes these requests, including metadata updates. We developed the dynamic metadata functionality specifically at the request of our partner, Ivory Jones, for the FuseWars game, but we do plan to provide this technology to other projects in the future as part of our business model. Challenges we ran into We were one of, if not the first team to develop a link between Unreal Engine and MetaMask. The challenges were immense, and the original solution spanned multiple servers and endpoints using Java, Python, Firebase, and C++. The funny thing was, we never set out to build a plugin. Our original purpose was to make our own game. Then a couple developers joined our Discord asking if they could use our tech, and we thought, "That's weird, because people definitely mainly want to buy our NFTs!" Then it happened about a dozen more times before we finally recognized that the market really needed this technology. Accomplishments that we're proud of We are proud to work with some truly amazing people. Not just our team, but the broader community has really increased in quality during the market downturn. The people who are left are passionate about what they do, and purpose driven. We are proud to be able to provide the tools to help game developers like Ivory Jones achieve their vision. What we learned It's just as much about who you're working with, as it is about what you're building. Listen to the market, it might just tell you what you need to hear. What's next for Dynamic NFTs Our next feature set will be in-game minting, expanding upon our existing User Validation, Sync NFT, and Dynamic Metadata functionality. <div