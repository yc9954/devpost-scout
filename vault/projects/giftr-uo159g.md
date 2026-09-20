---
slug: "giftr-uo159g"
url: "https://devpost.com/software/giftr-uo159g"
title: "GifTr"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 985
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# GifTr

> The Decentralized Gift Card Marketplace

[Devpost](https://devpost.com/software/giftr-uo159g) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]] [[web_dom]]

**stack** express.js, node.js, react, sui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for giftr

## Body

Landing Page Sui Wallet Connection Gift Card Wallet Gift Card Marketplace Inspiration As college students who recently graduated high school in the last year or two, we know first-hand the sinking feeling that you experience when you open an envelope after your graduation, and see a gift card to a clothing store you'll never set foot into in your life. Instead, you can't stop thinking about the latest generation of AirPods that you wanted to buy. Well, imagine a platform where you could trade your unwanted gift card for something you would actually use... you would actually be able to get those AirPods, without spending money out of your own pocket. That's where the idea of GifTr began. What it does Our website serves as a decentralized gift card trading marketplace . A user who wants to trade their own gift card for a different one can log in and connect to their Sui wallet . Following that, they will be prompted to select their gift card company and cash value. Once they have confirmed that they would like to trade the gift card, they can browse through options of other gift cards "on the market", and if they find one they like, send a request to swap. If the other person accepts the request, a trustless swap is initiated without the use of a intermediary escrow, and the swap is completed. How we built it In simple terms, the first party locks the card they want to trade, at which point a lock and a key are created for the card. They can request a card held by a second party, and if the second party accepts the offers, both parties swap gift cards and corresponding keys to complete the swap. If a party wants to tamper with their object, they must use their key to do so. The single-use key would then be consumed by the smart contract, and the trade would not be possible. Our website was built in three stages: the smart contract, the backend, and the frontend. The smart contract hosts all the code responsible for automating a trustless swap between the sender and the recipient. It specifies conditions under which the trade will occur, such as the assets being exchanged and their values. It also has escrow functionality , responsible for holding the cards deposited by both parties until swap conditions have been satisfied. Once both parties have undergone verification , the swap will occur if all conditions are met, and if not, the process will terminate. The backend* acts as a bridge between the smart contract and the front end, allowing for **communication between the code and the user interface. The main way it does this is by managing all data , which includes all the user accounts, their gift card inventories, and more. Anything that the user does on the website is communicated to the Sui blockchain. This blockchain integration is crucial so that users can initiate trades without having to deal with the complexities of blockchain. The frontend is essentially everything the user sees and does, or the UI. It begins with user authentication such as the login process and connection to Sui wallet. It allows the user to manage transactions by initiating trades, entering in attributes of the asset they want to trade, and viewing trade offers. This is all done through React to ensure real-time interaction so that new offers are seen and updated without refreshing the page. Challenges we ran into This was our first step into the field of Sui blockchain and web 3 entirely, so we found it to be really informative, but also really challenging. The first step we had to take to address this challenge was to begin learning Move through some basic tutorials and set up a development environment. Another challenge was the many aspects of escrow functionality , which we addressed through embedding many tests within our code. For instance, we had to test that that once an object was created, it would actually lock and unlock, and also that if the second shared party stopped responding or an object was tampered with, the trade would be terminated. Accomplishments that we're proud of We're most proud of the look and functionality of our user interface , as user experience is one of our most important focuses. We wanted to create a platform that was clean, easy to use and navigate, which we did by maintaining a sense of consistency throughout our website and keep basic visual hierarchy elements in mind when designing the website. Beyond this, we are also proud of pulling off a project that relies so heavily on Sui blockchain , when we entered this hackathon with absolutely no knowledge about it. What we learned Though we've designed a very simple trading project implementing Sui blockchain, we've learnt a lot about the implications of blockchain and the role it can play in daily life and cryptocurrency. The two most important aspects to us are decentralization and user empowerment. On such a simple level, we're able to now understand how a dApp can reduce reliance on third party escrows and automate these processes through a smart contract, increasing transparency and security. Through this, the user also gains more ownership over their own financial activities and decisions. We're interested in further exploring DeFi principles and web 3 in our future as software engineers, and perhaps even implementing it in our own life when we day trade. What's next for GifTr Currently, GifTr only facilitates the exchange of gift cards, but we are intent on expanding this to allow users to trade their gift cards for Sui tokens in particular. This would encourage our users to shift from traditional banking systems to a decentralized system, and give them access to programmable money that can be stored more securely, integrated into smart contracts, and used in instant transactions. <div