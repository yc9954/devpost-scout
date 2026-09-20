---
slug: "zkretsanta"
url: "https://devpost.com/software/zkretsanta"
title: "ZKretSanta"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 423
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
---

# ZKretSanta

> A truly secret, Secret Santa protocol

[Devpost](https://devpost.com/software/zkretsanta) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[finance_payments]]

**stack** arkworks, avalanche, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for zkretsanta

## Body

Inspiration Secret Santa is a fun Christmas tradition. The traditional game of drawing names from a hat or a bowl works well for secretly deciding who gives gifts to whom. But it doesn't work for remote/online communities who can't meet in person to draw the names. Such communities inevitably end up relying on a trusted party - someone who makes the "master list" or an online centralized (Web2) Secret Santa generator - for making the assignments. So, I challenged myself to come up with a scheme that does not rely on a trusted party by using blockchain and zero-knowledge proofs. What it does ZKretSanta allows for the trustless generation of Secret Santa assignments. At the end of the protocol, each person only ends up knowing who they need to give their present to and nothing else. How we built it I desinged this protocol by taking inspiration from the ZCash protocol. It is basically a very stripped down version of ZCash that works well for this purpose. I wrote the zero-knowledge circuits needed for the protocols using the awesome Arkworks library. To realize the protocol, I used the Avalanche platform and developed a custom VM for it. Challenges we ran into I faced most of the challenges in writing my custom zero-knowledge circuits for the protocol. Arkworks does not have any documentation, so you have to rely on internal tests and examples. But it feels very natural once you get over the learning curve. Accomplishments that we're proud of Just seeing this project to completion is a very big accomplishment for me. I can't believe how I got from just thinking about an abstract protocol to an actual real implementation in the limited time that I had. Giving it my all in the last few days is definitely something I am proud of. What's next for ZKretSanta I originally imagined ZKretSanta for remote/online communities. Avalanche allows for custom subnets and this can really work well for an organization-level deployment. But it can be extended to a global protocol where you give (receive) gifts to (from) random people on the internet for Christmas! For this, the process of giving and receiving gifts would also need to be done online over the blockchain while maintaing secrecy. This can be achieved by implementing a custom Avalanche VM that supports ZCash like anonymous payments. The presents can then effectively be exchanged over any other blockchain in the form of NFTs/tokens by using a bridge (for eg, Chainlink!) while still maintaining the anononymity of the parties involved. <div