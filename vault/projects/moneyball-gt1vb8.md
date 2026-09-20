---
slug: "moneyball-gt1vb8"
url: "https://devpost.com/software/moneyball-gt1vb8"
title: "Moneyball"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 381
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Moneyball

> Play basketball, earn crypto.

[Devpost](https://devpost.com/software/moneyball-gt1vb8) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[financial_record]] [[structured_db]]

**stack** bttc, go, mongodb, react-native, solidity, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moneyball

## Body

Note: Apple Testflight build will be emailed to Devpost for judging. Inspiration Basketball players can shoot hundreds of shots everyday. So why not get paid for it? Moneyball was inspired by classic basketball arcade games and the NBA 3-point contest. What it does Moneyball is the first ever app that pays you to play basketball. Using GameFi pay to earn mechanics and AI computer vision algorithms, Moneyball tracks your shots and rewards you for successful shooting. How we built it I built this app using React Native with a Go backend and Solidity smart contracts. A MongoDB database is also used. The smart contracts are mostly hosted on the BTTC testnet, but a few are also on the ETH Goerli testnet (using the mapped BTT asset) for easy access, as testers don't need to add a custom network in Metamask. Challenges we ran into The biggest challenge was integrating Web3 technology into a mobile application. The vast majority of Web3 and blockchain tooling today is designed for the web, so building out a mobile solution was a challenge. I decided to use React Native because of its easy interoperability with some Web3 libraries. Another big challenge was integrating alongside the BTTC blockchain. I repeatedly ran into problems when I attempted to use custom networks in Metamask mobile, so I had to settle for the ETH Goerli network for client-side transactions, while leaving the main game contracts running on the BTTC Donau Testnet. Additionally, designing and developing the core computer vision algorithms that make the app work was a big hurdle to overcome. It was the first thing I tackled at the beginning of the hackathon in May, and took several weeks to perfect. Accomplishments that we're proud of Developing the algorithm to accurately track basketball scoring was a huge accomplishment for me. I don't have a lot of experience with computer vision or machine learning, so figuring it out and making it work after lots of trial and error was exciting for me. Actually getting mobile transactions figured out was also something I was proud of. What we learned I learned a lot about the Web3 ecosystem as well as computer vision and mobile app development. What's next for Moneyball Improving the algorithm Public beta NFT release More robust contracts <div