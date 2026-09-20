---
slug: "helix-checkout"
url: "https://devpost.com/software/helix-checkout"
title: "Helix Checkout"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 878
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/general_public"
  - "substrate/financial_record"
---

# Helix Checkout

> The easiest way to buy and sell NFTs on TRON!

[Devpost](https://devpost.com/software/helix-checkout) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]] [[general_public]]
**substrate** [[financial_record]]

**stack** node.js, react, solidity, tronweb, typescript

## How they structured the write-up

- ✨ inspiration
- 💳 what it does
- ⚙️ how it works
- 🏗️ how we built it
- 🤔 challenges we ran into
- 😊 accomplishments that we're proud of
- 🎓 what we learned
- 🚀 what's next for helix checkout
- ❤️ demo

## Body

GIF Pay for NFTs with a credit card! The seller dashboard makes it a breee for creators to set up a checkout Our built in wallet makes it easy for users to view their digital assets Our landing page Our demo token The problems with the current NFT sales process Our roadmap ✨ Inspiration Buying and selling NFTs is way harder than it has to be. To buy an NFT, firstly, you need to sign up to an exchange and buy the right crypto-currency. After you find all your ID and upload a selfie, it still all needs to be verified, which can take days. Once you finally have your crypto, you need to set up a wallet like TRON link with your confusing 24 word passphrase, “spaceship”, “monkey”, “dishwasher” - which you can’t lose and have to keep super safe and secure. Only after all that can you actually buy your NFT, which involves confusing things like signing transactions and using smart contracts. Let’s face it, the user experience for buying NFTs is broken - but we can fix it. 💳 What it does Helix Checkout provides NFT creators a simple, fast, safe and secure way to sell NFTs on the TRON blockchain via credit card to consumers. 🛍️ Checkout For NFT consumers, the checkout experience is simple and familiar. As part of the checkout process, the user authenticates using a magic link which also sets up a TRON wallet linked to that email address to securely store NFT purchases. Once the buyer has authenticated, all they need to do is select their payment method, enter their payment details and click pay. The buyer is then presented with a confirmation screen so that they can track the progress of their NFT transaction. After the NFT transaction is complete, the buyer can immediately see their purchase in their wallet. It’s just that simple. 📈 Seller Dashboard As an NFT creator, adding a checkout is quick and simple. After deploying a Helix compatible NFT contract, sellers can login to the dashboard and search for their contract address. The search retrieves all the token information and pre-fills the checkout details, as well as making sure the contract has successfully implemented the Helix Checkout interface. All the seller has to do now is hit ‘Add checkout’ and that’s it! The checkout has been created. The seller can now share their checkout link and sell NFTs directly to consumers using credit cards. 👛 Wallet Buyers are not required to bring their own wallets - we create one for them to make the checkout process a breeze! ⚙️ How it works Firstly, NFT creators must create their NFT contract and implement the Helix Checkout interface: contract IHelixCheckoutInterface { // Required // Used by Helix Checkout to mint and deliver the NFT to the customer function claimTo(address userAccount) public payable returns (bool); // Required // Gets the price of the NFT function price() public view returns (uint256); } It is highly recommended that NFT creators record their token details on TronScan. This is where Helix Checkout pulls the token metadata from to simplify the checkout creation process. 🏗️ How we built it We've built Helix Checkout on a modern technology stack, including React and Node.js, written in Typescript, hosted on Firebase. Our technologies and services we have used include: Tron Web Javascript SDK TronScan APIs Stripe Payments SDK CoinMarketCap API Firebase - Authentication, Firestore, Hosting, Analytics Solidity smart contract 🤔 Challenges we ran into Working with the various SDKs (Ton Web, TronScan, Stripe, CoinMarketCap) required a lot of upfront research and understanding. Some of the blockchain-specific aspects of the project (e.g. signing transactions, authentication via private keys) were also particularly tricky new flows for our team. Fortunately, we started researching solutions very early on when the hackathon was announced, so we were able to give ourselves ample time to learn all these new technologies and overcome the hurdles. 😊 Accomplishments that we're proud of We are really happy with the simple user experience and clean UI that we have developed for the checkout process. It is responsive, and makes it so easy for people to buy NFTs. We really see this as being able to drive adoption of TRON and help creators sell their digital assets with ease. 🎓 What we learned How to implement TRC-721 contracts and deploy them on TRON Tron Web SDK functionality Stripe payments and integration Best UX flows for checkouts 🚀 What's next for Helix Checkout We want to create a Javascript SDK to make it easy for developers to embed the checkout within their apps. We also have a roadmap of features we wish to develop ❤️ Demo Please head to Helix Checkout and hit the 'Demo Checkout' button to test it out. We have set up a demo token that can be purchased to test out the checkout flow. The demo is using the Shasta Testnet and test Stripe account, as we didn't want to have to actually charge users real money to demo the solution! Please use a real email address to authenticate. Once authenticated, you can use these credit card details to make a purchase: Credit card number: 4242 4242 4242 4242 Expiry: 01 / 25 CCV: 123 Code available for review on request <div