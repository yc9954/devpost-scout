---
slug: "lightningcelo"
url: "https://devpost.com/software/lightningcelo"
title: "LightningCELO"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 922
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/frontline_worker"
  - "user/small_business"
---

# LightningCELO

> Real-time money-streaming protocol for Celo Stables Enabling your $cUSD to flow like the river in real-time. Let's make money more beautiful than ever.

[Devpost](https://devpost.com/software/lightningcelo) · hackathon [[EthCC Hack 2022]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[agriculture_food]] [[developer_tools]] [[finance_payments]]
**user** [[frontline_worker]] [[small_business]]

**stack** ethers, next, react, sablier, solidity, truffle, wagmi, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lightningcelo

## Body

Inspiration Enabling your $cUSD to flow like the river in real time. Let's make money more beautiful than ever. DECK: LINK TO THE DECK Bob is a freelancer, working in Latin America, and he is using HeyMate services for getting hired and paid in Celo Dollar for his services. He starts working on day one of the month and gets compensated on the payday (usually the last day of the month). HeyMate uses its own payments SDK on Celo to transfer your income in Celo dollars to your wallet. Imagine, what if you were paid every second for your services through a novel recurring mode of payments? Imagine having half of your compensation already in your wallet by mid-month, so you do not have to wait until the month-end to get your payment. You would be able to invest and spend your salary during the month, rather than waiting for the month's end to receive it. Imagine, you do not have to pay a one-time subscription fee on Netflix to watch your favorite shows, without actually knowing the amount of time you would actually be able to watch the shows. Rather, you pay Celo Dollars at a constant flow rate (0.02cUSD/min), for every duration that you watch the show on NetFlix. In this way, you would be able to save up a lot of money, for the duration that you do not use Netflix. -Insurance DAOs could also enable memberships through recurring ERC-20 payments. Insurance premiums for farmers, do not have to be paid as a one-time payment for guaranteed protection/insurance. They can be paid by the second, thus, farmers do not have to worry about making one-time payments at the start of the month, but chose to pay continuously over the second. -In this way, they could cultivate a habit of healthy savings and spending efficiently. What it does Stream cUSD from one wallet to another in real time You can connect your wallet to the platfrom running on Celo Alfajores Network. You can view an ongoing recurring stream by referencing to the created streamID else you can create a new stream. To start the stream, you have to enter: The receipient's wallet address The token that you want to stream. For now we enable cUSD flows on Alfajores Testnetwork The amount of token you want to stream (say: 10cUSD) The time you want the stream to end. Let's say you start the stream at x seconds. You choose a time interval of x+T for the stream to end, where both x and T can be measured in seconds and can amount to minutes, hours, days, weeks, months, years, and even centuries. The token stream would be live for T duration of time The platform also displays the total number of token streamed and the amount of tokens remaining for withdrawal in real time. If y is the total number of tokens to be streamed, then you can withdraw a certain amount of token, let's say x tokens out y at a time, and then, another z amount of tokens out of the remaining y-x tokens. Tokens here refers to $cUSD on Alfajores Test Network. Once the stream ends, the entire token is to be withdrawn to the receipients wallet, and then the platform would redirect you to create a new stream. How we built it A money stream has six properties: Sender. Recipient. Fixed deposit amount. ERC-20 token used as streaming currency. Start time Stop Time A. Smart Contract Deployed to Celo Alfajores Testnet 0x671580C2d0e99Bb17690B5D4D805F1902d26f5b0 B. We use Celo Contract Kit and Truffle to deploy our contracts to Celo Alfajores testnet, web3js , wagmi.js and ethers to interact with the smart contract. C. The front end is built on React , and Chakra UI , and many third part libraries. Sender's wallet has 14 $cUSD. Sender wants to start a stream of 5 $cUSD Sender enters the details of the receipient, start and end time, and amount to be streamed, and creates a recurring stream of tokens in real time to the receiver's wallet. Stream starts initially with 0 cUSD streamed and 0 cUSD withdrawable, local time 23:30pm (IST - Indian Standard Time) Middle of the stream, we see that 1.6cUSD has been streamed already and 1.6cUSD is withdrawable. Meanwhile receiver claimed 1.63cUSD of the stream, midway, and the stream finished in two minutes ( 23:33 local time IST- Indian Standard Time ). The receiver is yet to claim 3.37 cUSD. After claiming the remaining cUSD, the streamID, expires and the user can create another stream So the protocol enables a user to stream money in real time as well as withdraw money at any instant. Look at the potential use case above. Also watch the demo video linked above. Challenges we ran into Using Wagmi JS Deploying Sablier Contracts to Celo using Truffle Working on a Next App Integrating Valora App via Wallet Connect (pending) Accomplishments that we're proud of Facilitating streams of cUSD using the ERC-1620 standard Constructing simple user interface for better understanding What we learned Use of redux for state management Use of wagmi, web3, ethers, on the user interface What's next for LightningCELO To enable multiple streams and display status of recurring multiple streams in real time. To enable streaming for other tokens on the Celo Network, like $CELO, $cEUR, $cREAL, $PACT, and many more. To expand the use cases of LightningCelo to projects building on Celo developing a mobile app in React Native, compatible with Valora, with development of integrable SDK, better UI. <div