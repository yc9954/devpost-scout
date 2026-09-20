---
slug: "space-wars-ntrwxj"
url: "https://devpost.com/software/space-wars-ntrwxj"
title: "Space Wars: Diplomacy"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 705
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Space Wars: Diplomacy

> Win prizes in a strategic space Battle Royale, completely on the blockchain.

[Devpost](https://devpost.com/software/space-wars-ntrwxj) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** chainlink, hardhat, javascript, react, redux, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for space wars

## Body

Main Game Map View Ship Information Display Movement Panel Transferring Dark Matter to other players Movement and Range indicator zones Inspiration Although we hadn't met before the event, our team members shared a common goal: to build an application using modern technology, on the blockchain, that fulfills the promises of decentralization and uses the emergent behavior of NFT purchasers as a core game element. Although the technology is new, the concept is classic: vehicular combat across the vast reaches of deep space. Our pitch - and the source of our working title - was Spacewar! meets Diplomacy, mediated by the blockchain. The spacecraft themselves, while simple, are unique and randomly located. The real game is what happens when people group up to win - what promises are made, and will they be kept? Who will be the final spacecraft standing? What it does Space Wars: Diplomacy is a real-time strategy game designed to take place over several days. Each minted Spacer NFT has a unique colorway, a randomized location on the cöordinate plane, and an initial supply of three ERC-20 tokens representing energy, à lá mana or AP in other games. How we built it We were serious about building a decentralized application. We wanted to store all the data on chain, and launch on the main network to maximize robustness and minimize complexity. With this, we tried out several different frameworks while following along the Chainlink webinars (thank you for these!) Challenges we ran into As a randomly assembled team from all over the world, working together every day with minimal structure, we had some great opportunities to learn and become better dApp developers. We spent several days pair programming to facilitate knowledge transfer between each other, explaining terms and getting to know one another. Once we had specific roles, things flowed smoothly - we should especially celebrate the accomplishments of Nok, who may have humbly presented himself as a new developer but was able to deliver dozens of completed features without assistance. The biggest challenge is the expense of blockchain data itself - even with a 3.5kb SVG file, we looked at techniques to marshal and compress it further - allowing us to store the SVG image itself on the blockchain. Accomplishments that we're proud of Our app meets our original design goals: it does not require an active traditional web host and stores all of its data on the blockchain. Despite these very stiff constraints, the game is playable, immutable, and extensible - not only can we not prevent someone from building a different frontend, we can't interfere with the game at all. This allows players to form alliances, strategize, and connive without worrying that a game change will interfere with their plans... We are proud of both our frontend and our smart contract. For the entire length of the hackathon, we checked in daily for a standup and to architect and develop the software. We practiced modern development, with feature branches and code reviews, and used the latest deployment we had - the first time for some members on our team. We're also proud of the efficiency of our contract, which has extremely minimal external dependencies (besides the crucial addition of the Chainlink VRF) and is highly optimized for gas use. We think the marriage of solid game design principles with the absolute latest technology offers a compelling experience for players, and with our open source design, they can launch their own seasons instead of waiting for developers to modify the game. What we learned With learning being a core goal of our team's philosophy, we experienced tremendously high throughput of skill transfer throughout our development experience. While making the team, we activiely tried to find complementary skillsets, so we would be able to help each other grow. With a marketer, front end, and back end developer, it ended up working out great. What's next for Space Wars Our goal has always been to build a project that would be viable on mainnet. While we know our project is clearly going to dominate the Chainlink Hackathon, more work will be done to hit the chart-topping numbers we know Space Wars: Diplomacy can attain. Look our for our mainnet contract address! <div