---
slug: "fortunity"
url: "https://devpost.com/software/fortunity"
title: "Fortunity"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1137
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/researcher"
---

# Fortunity

> Forecast Markets – the future of prediction markets

[Devpost](https://devpost.com/software/fortunity) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[researcher]]

**stack** css, github, hardhat, javascript, npm, polygon, python, scaffold-eth, solidity, truflation, typescript, uniswapv3vamm

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fortunity

## Body

Some interesting code Clearing house Liquidity Liquidity Long Position Long Position Inspiration We live in an uncertain world. Our governments, businesses and families struggle to foresee the future of our economy. We outsource the task of understanding the future to a handful of "experts" who have no good reason to be right about their predictions. Worst of all, unless you're a researcher at the central bank, your understanding is ignored by the current system. To solve this problem, we invented Fortunity: a new system that lets anyone trade economic variables directly. From indicators like inflation to GDP growth, we are empowering you to turn your wisdom into wealth – your predictions into profit. And, in the process, your unique insight shapes a clearer vision of our economy for everyone. The inspiration for this project came to us in the economic turmoil we’re witnessing in 2022. Currently, Truflation is measuring UK inflation to be 17%, far above its ‘target’ of 2%. It is clear that our world has gotten too complex to be understood by a handful of elites alone: we need to unlock the insight of everyone to forecast the future of our economies. What it does Fortunity is a decentralised exchange that allows users to trade derivatives that are directly linked to economic variables. We call this new class of derivatives 'Forecast Markets'. These are a new type of prediction markets that allow for continuous trading of variables. Unlike prediction markets, which typically offer bets on a 'yes or no' outcome, Forecast Markets let you trade variables the same way you can trade any asset. Fortunity uses a novel 'Growth Variable vAMM' to bring together traders and liquidity providers to make markets for derivatives on economic variables. This technology is used in current Decentralised Exchanges (DEXs). For the first time, our adaptation allows the smart contract to transform any economic variable, even non-positive indicators such as GDP growth rate, into a positive equivalent Forecast derivative, allowing them to be traded as assets. For example, CPI can be shown as 1 + CPI/100. This is then used as an Index Price for us to track with our Forecast Derivative. For a deeper dive into our financial and technical architecture, see https://fortunity.gitbook.io/fortunity-docs/ To ensure that our derivatives track the value of the underlying variable, we use another technology from DEXs, the Funding Rate’ that uses the aforementioned Index Price calculated from on-chain data feeds. For CPI we use the Truflation Node through Chainlink on the Polygon network. Due to their highly convenient and reliable data feeds, we began by making Forecast Markets on YoY Inflation figures provided by Truflation. We connect to the Truflation node on Polygon as provided through the Chainlink network (deployment to Polygon testnet has unfortunately been delayed 😅and development is currently locally run). As Truflation adds to their platform, we look forward to incorporating more countries, inflation sectors, and support for more variables to offer more advanced options for users. We chose Polygon thanks to their low network fee, fast-growing DeFi ecosystem & community, and brilliant development support. How we built it To achieve our ambitious goal, we had to define priorities, learn fast, and collaborate like never before. We had many meetings – and sleepless nights – to deliver the best product possible within this short time. But most importantly, we are grateful to have been supported by the Chainlink, Truflation, and Polygon communities both in person and on their active support discords. Ultimately, we compiled a demo of our new class of DEX that will serve as the foundation in future development in Forecast Markets whilst we perfect functionality and ensure security. Challenges we ran into When we set out to solve the problem of making variables tradeable, we had to delve deep into core financial mathematics. We compared many orderbook and AMM exchanges, as well as various ways of bootstrapping liquidity on new DEXes. We explored the origins and evolution of prediction markets and tried dozens of ways of adapting them to suit variable trading. However, no prediction market solution really could provide what we needed. We had to get creative and work out what else was available that hasn’t yet been put together. We eventually realised DEXs were the answer. After countless nights of drawing graphs and working with zero-arbitrage mathematical arguments, we managed to come up with an elegant solution that we’re proud to present in this hackathon. Pavel On the technical side, writing the equivalent of a fully functional DEX in a month is certainly a challenge. We of course forked code from previous DEXs, perpetual protocol in particular due to its impressive documentation, but even then understanding the internal functionality of over 100,000 lines of code was by all means not an easy mission. For quicker development purposes we worked on locally created blockchains, after recently facing a few technical challenges with deployment we have unfortunately had to make the decision to submit our local copy. We will be deploying to the Polygon Testnet soon. I do believe we have achieved a lot, the implementation has simply faced a lot of debugging issues (2 whole weeks in fact). It will simply require time and effort, nothing we can’t manage ;). Greg Accomplishments that we're proud of Our most important accomplishment is that we stayed true to our vision, and to each other. Despite forming our team only a month ago, we worked tirelessly together to design and implement this revolutionary solution – on paper and on chain. Although we have so much ahead of us, we are pleased to have compiled a demo of our new type of DEX as well as the accompanying documentation and theory behind it. What we learned In the process of designing the financial architecture for Forecast Markets, we learnt LOTS about AMMs, LP mechanics, perpetual futures and prediction markets. We took a truly deep dive into DeFi. Additionally, we gained practical understanding of Chainlink’s Oracle APIs and, in particular, Truflation’s Inflation data feeds. Just in terms of development, we’ve learned buckets. We know now so much more about deployment, upgradeable contracts, scaffold-ETH, dApps, ethers, hardhat locals, Truflation, the Chainlink starter kit, and of course perpetual protocol (we can read really complex code now, finally worked out what the X96 means and it’s honestly funny). Most importantly, we learnt the art of building a DeFi project together across the world – despite being 3 time zones apart. Being part of the Chainlink ecosystem is truly a unifying experience. What's next for Fortunity The journey is just beginning for Fortunity. Our mission remains: we aim to make a universal exchange for trading the variables that matter to humanity. To achieve this, we laid out a roadmap [ https://fortunity.gitbook.io/fortunity-docs/fortunity/roadmap ] to summarise our future goals. Let’s unlock the next chapter of finance together. <div