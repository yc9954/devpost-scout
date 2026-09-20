---
slug: "solarzu-dapp"
url: "https://devpost.com/software/solarzu-dapp"
title: "Solarzu Dapp"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 558
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Solarzu Dapp

> NFT Buy now pay later finance protocol

[Devpost](https://devpost.com/software/solarzu-dapp) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
  <sub>weak: retail_commerce</sub>
**user** [[general_public]]
**substrate** [[financial_record]] [[web_dom]]

**stack** alchemyapi, hardhat, ipfs, next, sequence, solidity, spheron, tailwind, truffle

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for solarzu dapp

## Body

Dev_Img2 Dev_Img3 Dev_Img1 Wallet connect option NFT Payment details Checkout Page Solarzu Home page Inspiration Our inspiration is humbly to provide access to NFT and the option of short term credit which solves 2 key issues in Web3 which are accessibility and usability. We have ourselves been unable to buy some NFTs due to lack of funds and high gas fee. This made us realize that the vast majority of Web2 consumers would face this hurdle, hence this became our inspiration to build this product on Polygon. Also, we believe Polygon community is the fastest growing community which helps the platform scale faster and allows matic users to participate in Ethereum NFT network. What it does The Solarzu Dapp enables users to connect with the platform and buy their chosen NFT for a fraction of the actual cost and repay the pending amount in any crypto over 3 months with interest. -Users can buy NFT on Solarzu by simply copying and pasting the URL of that NFT They can find the BNPL details after selecting the NFT Solarzu allows users to make a downpayment and place a bid for their NFT on Opensea testnet Polygon chain helps users to buy NFTs using Matic which makes the transactions cheaper and faster How we built it We built Solarzu using Next and Tailwind CSS for frontend Solidity for smart contracts and hardhat for testing and deploying the smart contracts to Mumbai testnet. The Dapp uses the Opensea API for interaction with opensea and ethers for interaction of smart contract with frontend It uses web3.storage for storing data in IPFS . The Dapp is hosted on Spheron Users can connect with Solarzu with their Sequence wallet The way it works on POLYGON is -> When the user enters amount to place a bid for the NFT in the form of ETH we fetch the price and converts it into matic using coingecko-api and the user can view that price in the form of USD. But the transaction is taking place on the polygon chain using matic and the bid on the NFT will be made in the form of WETH on the marketplace as the NFT is minted on ETH blockchain. So we are enabling polygon matic users to buy NFTs on Ethereum without the hassle of converting their crypto. Challenges we ran into Automatically placing the NFT bid in Opensea from solarzu wallet was the major challenge we faced. We were able to make it work by using Truffle Hd Wallet Providers. Remaining issues were minor challenges that we made it through easily. Accomplishments that we're proud of Creating offers on Opensea testnet from the Solarzu wallet by default is the biggest and most meaningful accomplishment so far. We're proud that all the BNPL transactions are carried out on Polygon Mumbai testnet and we believe this will enable Polygon community and users to purchase NFT on Ethereum using Matic. What we learned -> We understood how Polygon blockchain interacts with Ethereum and how transactions work ->Hosting the Dapp in Decentralised cloud -> Opensea SDK and API's -> Storing the data in ipfs using Web3.storage What's next for Solarzu Dapp We will be integrating a custom yield generating product which would offer fixed return on deposited amount and also act as collateral for higher limit on NFT purchase using BNPL <div