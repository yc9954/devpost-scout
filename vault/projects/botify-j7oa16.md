---
slug: "botify-j7oa16"
url: "https://devpost.com/software/botify-j7oa16"
title: "Botify"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 636
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Botify

> A p2p marketplace for bots that will rival the GPT store.

[Devpost](https://devpost.com/software/botify-j7oa16) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]] [[video_visual]]

**stack** chainlink, nextjs, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for botify

## Body

Landing page, users can shop by category or view all bots Bots are embeddable, so third parties can also use these bots. Possible use cases are Discord bots and Telegram bots Bot view Store view Inspiration I wanted to create decentralized alternative to the GPT store recently released by OpenAI. As an industry I think we really want to avoid the pitfalls we saw with the centralized app stores on mobile devices. Botify is however more than a store just for GPTs you can buy any bots you can imagine here! Botify also gives developers API access, making it possible to integrate Botify bots into Discord, telegram or any third party app. What it does Botify is a bot marketplace that connects SaaS developers with users. It uses the new ERC6551 NFT Bound accounts that allows the creation NFTs that can own assets. We combine this feature with Chainlink functions to create NFT tokens that can execute some piece of software in exchange for tokens. Currently users can create pay-as-you-go bots , where users pay for each request made (kind of like Lambda functions in the AWS ecosystem), and AI bots which let's devs define system prompts that will then be used by LLMs to create AI agents which help users with any problems they might have. Botify has an API that allows third-party applications to interact with any bot on the platform. Using this developers can access blockchain functions in their own application without having to learn about smart contract development, an easy and fast way to onboard new users into web3! How we built it Chainlink functions and ERC6771 are used to represent bots. The Chainlink functions are created in separate contracts which are called by the ERC6771 account when a user wants to execute the bot. The execution only occurs when the value of the transaction exceeds the pre-defined price of the bot defined at initialization. In short each bot is represented by a single NFT which has an address that users pay to which will in turn execute the CL function. The frontend is built using Typescript+Nextjs together with the https://wagmi.sh/ library which is used to create a nice dApp UX. Challenges we ran into Chainlink functions can return a maximum of 256 bytes, this really limits the capabilities of certain use cases we had in mind. To get around this we created the concept of "pay-as-you-go" bots and "pay-per-session" bots. Had trouble deploying project to vercel last second. Accomplishments that we're proud of Implementing a ERC6551 account correctly. The first two weeks I had a completely different idea that I wanted to implement, but it turned out to be unpractical and unusable. I proud that I managed to create this in only half the time. What we learned Everything about Web3 development. This is the first ever dApp i've created! :D More specifically I got some hands on experience writing solidity smart contracts and I got a much better understanding about how the Ethereum EVM works. Maybe more importantly I got to see some of the many things that don't yet work very well in blockchain (mostly execution/transaction speed). What's next for Botify Some debugging is still needed. We need to iron out some security issues. At the moment anyone can call a Bot without payment, we need to add some functionality so that a bot can only be called by it's owner (it's NFT). This obviously should already be added but when I added it the whole platform stopped working. This project should be very easy to market on tiktok since it's quite easy to understand (some input returns some cool output). I wanted to make some better AI products by adding generative AI and image upscaling capabilities to the bots as well, visual apps are easier to market... <div