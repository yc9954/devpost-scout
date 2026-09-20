---
slug: "map-of-crypto-picm5g"
url: "https://devpost.com/software/map-of-crypto-picm5g"
title: "Map of Crypto"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 577
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Map of Crypto

> Buying and selling things online, has never been easier! With Map of Crypto, you can buy various products from all around the world without any extra fees, and pay for everything with Crypto assets.

[Devpost](https://devpost.com/software/map-of-crypto-picm5g) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[retail_commerce]]
  <sub>weak: finance_payments</sub>
**substrate** [[geospatial]] [[structured_db]]

**stack** chainlink, cloud, flask, google-maps, ipfs, javascript, metamask, netlify, polygon, postgresql, python, react, rest, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for map of crypto

## Body

Logo Sell Buy Payments Security How it Works Sing up Map Inspiration Web3, Decentralisation, and Crypto are great ideas, and one of the best use is of course barter and finance. Even though we have a lot of web2 marketplace apps, still we have to deal with high subscription fees, currency exchange rates, and mosty importantly trust. With Map of Crypto, we have addressed all of those issues, used the power of web3 technologies to solve those issues, and eventually made the online shopping easier, cheaper, and safer. What it does It helps you find/ sell different types of products, all around the world. The only thing you need is your Crypto Wallet (for now we support just MetaMask), and you can start buying and selling things online. First of all we need a seller, the seller puts the item on sell, so that we can see the item and it's location on the map. Then interested buyers, can give put their offers. Moreover, there is also a decentralised Chat Room where buyers and sellers can chat. Once the seller accepts the offer, the money gets staked inside of the smart contract, and it can be realised only under certain conditions, such as delivery of the product (fetched from the data provided by Chainlink APIs), or the cancellation of the purchase. In this way our users do not have to trust anyone, as everything is in the code, the whole system is decentralised and works on the Blockchain. How we built it The whole power of the app lies in our smart contract, which we built with the use of Solidity, and Chainlink Oracles. Later on we have built a simple Backend service in Python, and external adapter for the Chainlink Oracle. On the frontend part, we have used React with JavaScript as a fundamental technologies. WalletConnect helps us connecting the users via Metamask, which also works as a connector with the RPC nodes and our smart contract. Additionally, we have implemented web3 storage library for storing assets on the IPFS, and also a decentralised Chat Room powered by Waku connect. Challenges we ran into Switching between different chains - first of all we have started from Kovan testnet, but then we have decided to move our contract to the Polygon Mumbai testnet as it is faster, and it's easier to find faucet test tokens. We also had some issues with the Chainlink Oracles configuration, and how to connect them with different networks, as we thought that we can have Chainlink node for multiple networks but apparently currently it's not possible. Additionally, integrating Postgres database was a bit of challenge for us. Accomplishments that we're proud of Most importantly delivering the working product, even thought it can be improved we have definitely created a new paradigm and solved a lot of the problems on the way. What we learned One of the most important lessons where topics related to Chainlink nodes, adapters, configuration of the Chainlink Keepers, Data Feeds and many other related topics. What's next for Map of Crypto We really do hope to start a new movement in the web3 dapps, as with our application we let users exchange different types of goods, no matter where they live, and eventually let them pay with a single currency. Our biggest dream related to this project, is making it a full-scale working products, for masses, which would start a completely new trend in the crypto world. <div