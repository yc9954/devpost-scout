---
slug: "nftickets-lsog6h"
url: "https://devpost.com/software/nftickets-lsog6h"
title: "NFTickets"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 867
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# NFTickets

> NFTickets aims to make NFTs useful in the real world. Allowing anyone to host events, and all others to buy tickets and attend. With ticket verification, no scalping, and penalties for bad actors.

[Devpost](https://devpost.com/software/nftickets-lsog6h) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[civic_government]] [[finance_payments]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** chainlink, chainlink-pricefeeds, moralis, react-native, solidity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for nftickets

## Body

NFTickets - login screen NFTickets - my tickets screen NFTickets - ticket for an even screen NFTickets - QR proof of ticket screen NFTickets - marketplace screen NFTickets - create event screen NFTickets - my events screen NFTickets - my event listing screen NFTickets - scanning a ticket screen Inspiration This project was inspired by a desire to showcase a real world utility for NFTs, and to allow for a fair pricing model for ticketing distribution, whilst allowing for codified trust via staking/slashing mechanics. In simple terms, I wanted to create a way for anyone to create event tickets and upload them to a marketplace where all others can buy them, whilst delivering a simple user experience that is available on mobile devices. What it does At present, NFTickets operates on the Avalanche testnet and allows users to mint ERC1155 tokens for their tickets, place those tickets on the marketplace at a fee (this fee is set at an arbitrary 20% at present, in future it is meant to be a deposit that will be refunded to good actors, and slashed for bad actors based on a complaint resolution mechanism that will use a DAO). Once a user places tickets on the market, they will be able to access their events and trigger a scanner that will scan QR codes. Buyers of tickets will be able to display QR codes representing their privately signed messages confirming their ownership of tickets for each event. All transactions on the market are tied to current USD pricing as reported by a Chainlink price feed, and are charged in the chain's native currency (AVAX). How I built it I utilised the ERC1155 standard to create two contracts - a token contract, and a marketplace contract. The Marketplace contract utilises the chainlink price feed, and uses a predefined USD price set at time of token creation to charge event hosts a fee, and the ticket buyers a the full ticket price. The marketplace contract also contain mechanics for privately signed message verification, and allows hosts to ensure the ticket holders have purchased a ticket to their event. For user experience I utilised the ethereum-react-native-boilerplate provided by Moralis, which is configured to interact with the contract and IPFS to allow for the necessary metadata to be hosted off chain in a secure manner. This is packaged and exported into an android app (apk) and is demonstrated in the video. Challenges I ran into The biggest challenges I ran into was time, and android app packaging. I imagined a highly complex app that would utilise keepers and a DAO for delayed payment to event organisers and an ability to punish bad actors, reward good actors, and encourage active participation in the DAO. But as I chose to pursue this on my own to ensure I learn as much as possible, I ended up spending more time trying to fix issues caused by different versions of JS engines in the debug and release versions of the apk then actually writing code. As a result, I'm attaching a signed debug apk which allows tickets buyers to buy tickets and display their QR codes (but refuses to show the app's logo and images) and doesn't allow minting new tickets unlike the version created by calling 'yarn android' from an IDE. I chose not to publish a release version of the apk, as it crashes upon authenticating via Metamask. Accomplishments that I'm proud of I'm proud to say I was able to create a good starting smart contract for the token and marketplace, and integrate chainlink pricefeeds that ensure end users will only ever need to think of the pricing in dollar terms. I'm also proud I was able to create simple yet easy to use UX for a mobile app - as this is my first mobile app development. I'm proud of the fact that the app worked as expected during testing and I was able to create events, sell and buy tickets, and then authenticate those tickets via the app. I'm proud that I was able to export what is very much an alpha / proof of concept version of my app that achieves real world use of blockchain technology for what is presently a heavily monopolised industry. What I learned I learned that my idea was far larger than my capacity to develop in the time allotted for the hackathon, and that I cannot rely on untested boilerplate code to export flawlessly using android studio. In future, I will test that the boilerplate code can actually generate working debug and release apks, before I code the app. What's next for NFTickets I plan on building out the Chainlink Keepers integration and creating a DAO with an ERC20 voting mechanism to finalise the smart contract, and then re-writing the app to determine which library is causing issues upon packaging. I may even start from scratch with a plain react-native project and slowly add in web3 and an IPFS integration to eliminate the apk packaging problems. I will also build a website front end in react for the event hosting mechanism, to ensure event organisers get a better experience and aren't limited by a mobile screen. <div