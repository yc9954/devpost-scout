---
slug: "lan-pfkngy"
url: "https://devpost.com/software/lan-pfkngy"
title: "LAN - Literally Any NFT"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 501
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
---

# LAN - Literally Any NFT

> A mark to market solution for illiquid assets

[Devpost](https://devpost.com/software/lan-pfkngy) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[education]] [[finance_payments]] [[labor_employment]]

**stack** moralis, next.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lan

## Body

Inspiration One of the key issues is that there is no manner for pricing NFTs in an efficient manner. This is particularly important for term loans on P2P platforms since as a lender, the risk of loss can be unclear as there's no way to determine what kind of liquidation price you'd be able to liquidate the collateral at. What it does It's an English auction with locked bids which are released if there's a higher bid. Bids are incentivized via pool rewards, which can be increased as time progresses in order to provide a higher APY to prospective bidders. This incentivizes speculators to provide more liquidity in order to receive the reward yields associated with the pool, or acquire the asset outright in a pure bid – or a mix of both. As the auction reaches maturity, the NFT converges onto the market price, and the owner has a choice of buying or selling. These are the deployments: Gnosis: 0x0E1C6348A0e80112fE98fc4422673126582C7318 Polygon: 0x5784a2d78Cf14DE66F37Bdf988391AE69e854942 Celo: 0x7ECcf1C51Bcf013dBED04bFd76f5eB26510e581F Cronos: 0x7ECcf1C51Bcf013dBED04bFd76f5eB26510e581F How we built it The contracts were written in Solidity and we used Github for collaboration. I used Remix while the others used VScode as their IDE. For testing, we used Ganache. I used Figma to create the UI design. The webapp was created using Next.js, React, and Moralis. Challenges we ran into The process of learning while doing likely made the process more complicated than it should've been. We had to refactor all of the solidity code for example, since the initial version that I wrote up was messy. Since solidity was a dependency for the UI, it left us with not as much time as we hoped to finish it up. You can still unlock all the functionality via Etherscan. Accomplishments that we're proud of As a team, we are proud of the mechanism that we were able to come up with, and figuring out some of the intricacies and implementing them into code. Although the UI has it's rough edges, it looks very clean. Personally speaking, this was my first contract I deployed on chain, so very happy about that. What we learned This was the first hackathon for us, outside of a much smaller school hackathon, so it was very interesting for us to see the processes, watch the workshops, and meet all the cool hackers here. I myself learned a lot about development, finally putting some of my solidity learnings to an actual project. What's next for LAN There are a lot of interesting ideas in here to push it forward: allowing bidders who are locked to free up a portion of collateral by allowing a contract to vouch on Union( https://github.com/Wyxuan1/ethcchackathon22/blob/integration/src/unionIntegration.sol ) figuring out undercollateralized gasless bids a la Opensea for undercollateralized bids, leveraging Sismo and Privy to identify skilled appraisers expanded use cases– allow a DeFi protocol to borrow against unissued tokens if they haven't released yet. tranched party bids, which would allow for groups to come together and bid rehypothecation with DeFi protocols like Paladin <div