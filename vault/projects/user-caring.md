---
slug: "user-caring"
url: "https://devpost.com/software/user-caring"
title: "Mistransfer"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 534
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Mistransfer

> Did you send tokens to the wrong address? Recover automatedly.

[Devpost](https://devpost.com/software/user-caring) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]] [[web_dom]]

**stack** chainlink-functions, ethereum-boilerplate, hardhat, heroku, moralis, sepolia, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mistransfer

## Body

BNB smartcontract has about 5 million dollars worth tokens locked forever Mistransfer Mistransfer Architecture NPM package to support mistransfer Ideal solution Crypto.com sent 400 million dollars worth tokens to a wrong address USDT smartcontract has about 2 million dollars worth tokens locked forever Inspiration Whenever I was building games, some players were reporting that they mistakenly sent their assets to our smartcontracts. We didn't make the recovery mechanism as a support as it happens rarely but requires a lot of effort from us. However, I always cared about the users and wanted a mechanism that enabled users to recover their assets. What it does Mistransfer is a verifiable, automated token recovery from the smartcontracts. Mistransfer verifies the mis-transferred transactions within the smartcontract and doesn't require manual withdrawal from the project owners. How we built it Smartcontracts The Mistransfer core technology is composed of two smartcontracts. The first smartcontract adds token withdrawal functionality. This smartcontract is available as an NPMJS package: mistransfer . A developer who wants to add the mis-transfer mechanism extends the UserCaring. * The UserCaring sets the owner of smartcontract to receive a fee for recovering the tokens.* The second smartcontract interface connects to all UserCaring smartcontracts. The smartcontract has the javascript code. This javascript code verifies the transaction parameters, such as sender, token, and amount. Then, using Chainlink Functions , the smartcontract executes the mentioned javascript code. Once the mis-transfer is verified, the tokens are transferred back to the user. Website To simplify, we provide a dashboard for a UserInterface. This dashboard is implemented using Moralis SDK. The Moralis has an API to fetch the token transfers and NFTs transfers. We use them to detect all recoverable cases automatically. The website itself uses Wagmi and RainbowKit to interact with the smartcontracts. Challenges we ran into Debugging chainlink functions was quite challenging. For two weeks, functions were not accepting POST methods, and then suddenly, it started to work even though I didn't change the code. Sometimes, Debugging messages were generic, so I had to debug them by deploying them line by line. For example, history stopped working, so I manually checked the function interaction result. SubId: 1705 has 65 requests, but history shows only 30. Accomplishments that we're proud of Now, I will deploy all my smartcontracts with Mistransfer and know that users who accidentally sent the tokens can return them themselves. Helping people to recover locked tokens makes me proud of Mistransfer. What we learned Etherscan submits the strings in the HTML Encoded format. It strips all the quotes and double quotes. Wagmi is the trend number one to work with blockchain on the front. What's next for Mistransfer Goal: All projects to implement mistransfer . To accomplish this goal, we need to work on the following: Strategic partnerships with network projects that could create awareness Work on a standard and push it as EIP. Marketing and community building Auditing for a production release Support of ERC1155 Deploy on multiple chains. Verify the transactions by multiple, independent RPC providers. Right now, it uses public nodes or Infura . LINK payment mechanism using price feeds and paid by the users. Right now, it has to be managed by the Mistransfer admin. <div