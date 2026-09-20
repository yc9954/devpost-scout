---
slug: "prompt-defi"
url: "https://devpost.com/software/prompt-defi"
title: "Prompt DeFi"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 616
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Prompt DeFi

> Redesign DeFi experience with AI

[Devpost](https://devpost.com/software/prompt-defi) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** chainlink, openai, react, solidity, web3auth

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for prompt defi

## Body

Review strategy with trigger Home screen Login with web3auth View account & use prompt Use templates Switch themes Inspiration Let's imagine for a moment that we have forgotten everything we know about DeFi and are opening Uniswap or installing MetaMask for the first time. Consider how many steps we would need to take to provide liquidity to pools or to borrow funds from a lending protocol. On average, it involves 10-15 actions, greatly complicating the new users' onboarding. Furthermore, any mistaken button can result in a total loss of funds. Now, let's compare this onboarding process to a centralized exchange. How much more straightforward and more intuitive is it? Our goal is to streamline this process to a simple voice command. Now, you can interact with DeFi by simply speaking a command or typing it into a text field. Such an approach can attract even more newcomers to the world of DeFi. Drawing inspiration from ChainLink's groundbreaking approach that played a vital role in the inception of the DeFi landscape, our mission is to propel decentralized finance to new heights by captivating a broader audience. Additionally, it's important to note that this concept can be particularly beneficial for people with limited abilities, such as the visually impaired. What it does Introducing Prompt DeFi - a platform designed specifically for newcomers to the DeFi world. Now users can perform desired actions by simply expressing them in a single sentence, whether through text input or voice commands. The platform is built on an account abstraction standard, allowing users to avoid paying gas fees. To execute transactions from text-based prompts, we are using a trained ChatGPT AI model. The account creation process is streamlined through Social Auth, enabling new users to onboard the platform quickly. Currently, Prompt DeFi integrates popular DeFi projects such as Uniswap, Lido, and Aave. Users can effortlessly send and exchange tokens through Uniswap, deposit into Lido and borrow and repay loans in Aave. Meantime, additional portfolio triggers based on Chainlink Automations enhance the user experience. How we built it The project comprises multiple components that interact with each other. We use the web3auth library to enable the creation of secure accounts based on MPC or make interactions with web3 as easy as Google auth. Integrating the @account-abstraction SDK on the front end enables working with Account Abstraction. The Bundler actively handles transaction processing while working with Account abstraction. UI development is based on the Mui library. AI Parser API uses Open AI API to translate user prompts to JSON. The solutions supports execution both of immediate actions with other protocols and strategies with triggers. Currently there is only one take profit/stop loss strategy for the portfolio of few assets. We deployed Trigger Factory and Trigger implementation. Once the creation of trigger is initiated, the corresponding Trigger Proxy is deployed and new Upkeeper is registered on Chainlink Automation Registry and the initial deposit in LINK is sent. Challenges we ran into Account Abstractions infrastructure is poorly developed yet. What we learned We have significantly improved our skills in working with Chainlink Automations. Additionally, we continue to be amazed by the capabilities of ChatGPT and its potential. What's next for Prompt DeFi We need to validate the idea at the hackathon, after which we can decide how to proceed with this product. Prompt DeFi was developed as part of mad.fish R&D, our goal is a market research and hypothesis validation for the next bull market. If Prompt DeFi passes the hackathon with good traction, we plan to integrate other DeFi projects and refine the concept into an MLP* version. We foresee creating all sorts of automated strategies using ChainLink Automation. *MLP - minimum loveable product ❤️ <div