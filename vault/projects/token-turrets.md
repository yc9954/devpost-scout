---
slug: "token-turrets"
url: "https://devpost.com/software/token-turrets"
title: "Token Turrets"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 433
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
---

# Token Turrets

> Play, Pay, Pulverize - on chain! ⛓️‍💥

[Devpost](https://devpost.com/software/token-turrets) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
  <sub>weak: financial_record</sub>

**stack** escrow, express.js, ipfs, javascript, mongodb, nft, nfts), node.js, tcp, three.js, typescript, webgl, websockets, xrpl

## How they structured the write-up

- 🚀 inspiration
- 💡 what it does
- 🛠️ how we built it
- ⚔️ challenges we ran into
- 🏆 accomplishments that we’re proud of
- 🔮 what’s next for token turrets

## Body

Landing page Escrow 1st Place Ripple: Best in Ledger 🚀 Inspiration We wanted to make online competition feel real. The game is skill, tanks, and action - but the stakes are on-chain. By weaving XRPL features like RLUSD (a USD-pegged token), escrow, and tokenization directly into the match flow, we created a trustless tournament model : stake → battle → payout. No middleman, no organizer - just players competing, with XRPL guaranteeing the rewards. Live in production here! https://tokenturrets.vercel.app 💡 What it does Token Turrets is a real-time multiplayer tank battle where anyone can create a room, start a tournament pot, and let the players fight it out. Each participant stakes RLUSD to enter, the pool is locked in escrow, and when the battle ends, XRPL automatically pays the winner. On top of that, players can personalize their tanks in our skin store , where every skin purchased with RLUSD is minted as a unique NFT and stored on-chain. This turns cosmetic purchases into verifiable, tradable assets - bridging gameplay, payments, and tokenization. 🛠️ How we built it Networking & gameplay : Real-time tank arena using WebSockets, TCP protocol, and Three.js for smooth multiplayer action. Tournament flow : Any player can spin up a room → others stake RLUSD to join → our backend secures the pot in XRPL escrow → the winner is determined by in-game results → escrow automatically releases payouts. Skin store : A full in-game shop where skins are purchased with RLUSD. Each skin is minted as an NFT on XRPL, giving players unique, ownable assets tied to their tanks. Trustless by design : Because both payments and assets live on-chain, players don’t have to trust an organizer. The system itself guarantees fairness and ownership. ⚔️ Challenges we ran into Synchronizing real-time gameplay with on-chain financial flows without slowing things down. Designing escrow and NFT minting flows that feel seamless in-game. Balancing scope: building multiplayer networking + escrow + NFT skin store all under hackathon time constraints. 🏆 Accomplishments that we’re proud of Built a real-time multiplayer tank game from scratch and fully integrated XRPL. Created a trustless tournament model with RLUSD staking and escrow. Launched an on-chain skin store where every purchase mints an NFT, giving players verifiable ownership. Showcased XRPL’s power across payments, escrow, and tokenization in one cohesive MVP. 🔮 What’s next for Token Turrets Building a secondary marketplace for NFT skins, enabling trading and rarity-driven economies. Introducing seasonal rewards and governance features to make Token Turrets a community-run esport. Positioning the game as a showcase for how XRPL can power trustless, on-chain esports ecosystems. <div