---
slug: "google-admodconsumer-chainlink-charity-app"
url: "https://devpost.com/software/google-admodconsumer-chainlink-charity-app"
title: "Google AdmodConsumer & Chainlink Charity App"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 810
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# Google AdmodConsumer & Chainlink Charity App

> This project aims to make donation from Google Admod and mobile game application. By utilizing Chainlink, the earning from Google could be proven to be eligible and transparent throughout.

[Devpost](https://devpost.com/software/google-admodconsumer-chainlink-charity-app) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** 0xsplit, chainlink, dart, flutter, googleadmod, safe, solidity, toml, transak

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for google admodconsumer & chainlink charity app

## Body

Inspiration Since we were little kids, my friend and I always talked about how we wish to help the environment, the people and the ability to support animals. We were very young and had few money, we didn't dare to ask our parents to help us with the charity call. In our country, the higher chance we will be scolded, especially with low-income family like us. What we can do are very few, but we did make some efforts: we try Ecosia - a platform where promises to give 80% their revenue to plant trees. We're making donations when we're mature enough However, all that leads me to realize one thing: I'm not using Ecosia much because Google is really handful, familiar; and mostly I wouldn't donate to the same organization/person twice! I think, that is because sympathy won't last long, people will tend to think that's they've done enough. That's why I think of this project: where we could earn donation by Google Admod! What's exciting thing go with it? A Mobile Game App to keep people enthusiasm. With the huge amount of people's having phone, we can approach more users, and with Chainlink, we can prove that the App is transparent and trustworthy. What it does The Game Mobile App will attract users' attention, by giving game reward we can instruct users to watch Video Ad. Afterwards, we always calculate the current earning with Google Admod API and display the data to users. Every week, we will buy LINK to the beneficiary address - a Split contract contains the list of charity organizations. The Chainlink contract - AdmodConsumer: the important layer to check the Admod earning of the App; check the correctness of transactions buying LINK for the beneficiary address. How we built it A ChainlinkClient contract which is called AdmodConsumer which acts an important role: Track Google's Admod Earning with Google Admod API Record that Earning to the Contract Pass the Earning to Transak API to check the LINK token amount would be bought with that Earning money Compare the LINK token amount of the beneficiary address with the LINK token amount to update the eligible status of the Contract 0xSplit contract 0xSplits is a set of composable, open-source and audited smart contracts that make it easy to split onchain payments. With 0xSplits, we can divide the Earning easily between multi charity organizations: After transferring LINK to the contract, we just need to call distributeERC20 with LINK token Chainlink Automation Every week, there's 1 Time-based Upkeep that will distribute the Earning of the contract: Every Sunday 22pm CRON: 0 22 * * 6 After 10 minutes, there's 1 Time-based Upkeep that runs after it to call AdmodConsumer's requestWeekEarning to request for Google Admod Earning this week. This function will also call an internal request called requestTransakValidation to get the amount of LINK buy-able from the Earning amount Every Sunday 22pm10 CRON: 10 22 * * 6 The requestWeekEarning function is only callable by Upkeep to prevent spamming Note: the 10 minutes delay will buy us some time to buy LINK to the destinated Split contract via Transak Administration For AdmodConsumer contract, 0xSplit contract, the Owner/Admin will be a multisig contract Gnosis Safe which the owner are Chainlink, Google if possible, me, other charity organizations so that: 0xSplit contract: the Safe has the ability to add more charity organization to the Split list; remove; modify split percentages AdmodConsumer contract: the Safe has the ability to withdraw contract's LINK to the 0xSplit contract - this is defined in the contract Who would be in charge of supplying LINK to the AdmodConsumer Request contract? The contract would be a recipient in the Split contract, perhaps with 1% share percentages so that it can have the fund needed to send request to Oracle 2 Chainlink Automation Upkeep would be the recipient in the Split contract also Challenges we ran into Unfortunately, I'm unable to create a real game to demo for it. However, I've got idea for it so it'll be comfortable for users to enjoy the Ads while playing the game too Accomplishments that we're proud of AdmodConsumer contract will deliver the secure information powered by Chainlink, Google API, Transak API. I'm proud that I handled the logic to my best Note: I tracked Transak rate, it's stable kind of long for the exchange rate between fiat and crypto so it would be fine. What we learned Chainlink architecture Google Admod for Flutter, and API Transak What's next for Google AdmodConsumer & Chainlink Charity App If my project would ever be noticed and get funded, I will put all of my efforts to build it. I, myself won't profit anything from it. I won't be in the 0xSplit list, but it would be great to have a slot for developer team so that they can maintain the project well. <div