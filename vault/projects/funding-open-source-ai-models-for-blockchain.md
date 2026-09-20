---
slug: "funding-open-source-ai-models-for-blockchain"
url: "https://devpost.com/software/funding-open-source-ai-models-for-blockchain"
title: "Funding Open Source AI Models for Blockchain"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 753
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Funding Open Source AI Models for Blockchain

> How can open source AI models compete with "Open"AI? With blockchain, anyone in the world can make micropayments for your AI models. Integrate any AI model on-chain and collect $ for operational costs

[Devpost](https://devpost.com/software/funding-open-source-ai-models-for-blockchain) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[finance_payments]]
**user** [[general_public]]
**substrate** [[financial_record]] [[web_dom]]

**stack** amazon-web-services, huggingface, javascript, solidity, sweat, tears

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for funding open source ai models for blockchain

## Body

Chainlink Functions Hackathon For submission by Harshil Dave June 9 2023 Project title: Funding Open Source AI Models for Blockchain Inspiration Problem statement: OPENAI and other large companies are building closed source AI models that the public has little input on. Additionally, the APIs from these models are not always available worldwide, and can be cost prohibitive when scaled. However, the open source community (see HuggingFace) has been building powerful models as well. But these are not easily available to average users, and the cost to deploy these models on the large scale is not available to the open source community. With blockchain-technology and chainlink-functions, we create a simple interface where the user can interact with any AI model on HuggingFace, and also fund the cost of running the model though micropayments using Eth/Matic. For demonstration, we use a conversational AI model, like ChatGPT, on HuggingFace. This is different from the ChatGPT API because the past conversation history can be saved on blockchain, and each user can have a unique, ongoing conversation. It is not as good as ChatGPT, but one application in the future could be that the model is trained to be a blockchain expert, and a user could interact with their smart wallet through a chat interface. What it does With this approach, the following things can be possible: Any user worldwide can connect a wallet to our website, and pay to use our ML models. Ideally, they can be integrated into their workflow/program. With this income, we can support open source development, possibly DAO-led development, of AI models. Costs could potentially be competitive with OpenAI and other services. Responses from AI models can be posted on the blockchain, so other smart contracts can also use our services to enhance their features. For example: A smart contract wallet with a chat-based interface. A user can 'talk to their wallet' to make transactions, made trades, do other DeFi things. The chat based interface can make sure the transactions are safe and valid. The costs to run this service can be paid by the user or someone delegated by the smart contract wallet. How we built it The main scripts that I have added are: promptHuggingFace.js - the HuggingFace API call ManageUserRequest - responsible for prompting the user for input, updating Functions-request-config.js with the prompt, calling functions-request. FundMe.sol - allows user to deposit and withdraw Matic. Also has a chargeMe function which is called after user request is fullfilled. It transfers funds from user to contract owner. I don't have a Front end unfortunately so my demo will be shown in CLI. The additional steps I did not complete includes saving the conversation history on-chain per user, so that it can be fed into the next request. However, the promptHuggingFace.js shows the conversation history is simply included as additional fields when prompting the AI. Challenges we ran into My experience is in science and engineering, and I made it halfway through one of the smart contract development courses before jumping into this Hackathon. I wasn't able to find teammates, so I did my best here. There are definitely problems and bad practices here, but it is a proof of concept. What we learned Breakdown of costs To see how economical it would be to run a ChatGPT like service on the blockchain, here is a quick analysis of costs. OpenAI pricing is available here: Pricing Comparison: GPT3.5: $0.002 / 1K tokens GPT4: $0.03 / 1K tokens HuggingFace API pricing is here: Hugging Face – Pricing $0.6/hour for Nvidia T4 Notice the pricing style is different. OpenAI charges per token of text. HuggingFace charges per hour. With my testing, I find the ChainLink functions service cost was about $0.0108 per 1k tokens. However, this does not include the base fee of 0.2 LINK. The base fee makes the cost much higher, but these numbers are TBD from Chainlink on Mainnet. In summary, it may be possible for blockchain costs to be on par with OpenAI costs, especially as gas costs are lowered in the future. Personal takeaway I've learned so much about smart contract development. I plan completing more coursework to continue working on this and refining the idea. Accomplishments that we're proud of This is my first Hackathon. Proud that I am able to submit something. What's next for Funding Open Source AI Models for Blockchain More coursework, and then probably tear down this code to build a better version. I hope I can find partners to work with as well. <div