---
slug: "just-dao-it"
url: "https://devpost.com/software/just-dao-it"
title: "Just DAO It!"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 927
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# Just DAO It!

> A decentralized crypto mutual fund, by the people, for the people.

[Devpost](https://devpost.com/software/just-dao-it) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** axelar, figma, framer-motion, javascript, next.js, smart-contracts, solidity, tailwindcss, typescript

## How they structured the write-up

- 💡 inspiration
- 🔍 what it does
- ⚙️ tech stack
- 🚧 challenges we ran into
- ✔️ accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for just dao it!

## Body

Home page Browse mutual funds and Fund dashboard Proposal view, with voting options Our entire backend diagram! Diagram of proxy contract Diagram of DAO contract 💡 Inspiration Just DAO It! was heavily inspired by the Collective Intelligence Theory, which proposes that one person can easily make an unwise decision, but it is much more unlikely for a whole group of people to make that same unwise decision. We wanted to apply this theory to blockchain technology whilst avoiding the expensive managing fees of mutual funds. This is when we stumbled upon Axelar and the Decentralized Autonomous Organization (DAO) model which was perfect for applying the Collective Intelligence Theory across different chains. Using Axelar, our decentralized mutual fund can have token assets from varying chains, whether it’s MATIC on the Polygon network, or AVAX on Avalanche. Hence… Enter a decentralized, democratic, mutual fund! 🔍 What it does Just DAO It! Provides a framework for people to easily implement decentralized mutual funds. This allows for people to create their own mutual funds, without having to pay a management fee to the bank. We used smart contracts to act as mutual funds, with customers buying governance tokens with USDC. These governance tokens are both bought and sold, acting as shares to the mutual fund. This also dictates the amount of voting power they get. Every month, people can propose an investment in an asset via DAO proposals and the shareholders will decide as a group whether or not to approve or disapprove the request. The proposals are then sent via call contracts with tokens, which perform buy/sell operations on their chain. Proxy contracts swap USDC to native token to perform buy operation, or convert native token to USDC to transfer back to the DAO smart contract USDC from tokens sold is fed back into the DAO Fund Pool, to be exercised at a later point. To combat whales, we have implemented a quadratic voting system where the voting power corresponds to the transformed radical function of the governance tokens, meaning that it is near impossible to hold a share of over 50%. This allows the voting system to be truly democratic, and allows everyone to play their role in deciding how their money is invested. Finally, when a customer wishes to withdraw their money from the DAO, they do so by having their tokens burnt and the corresponding amount of USDC returned to them. ⚙️ Tech Stack • The UI/UX was designed with Figma • The front end was built on Next.js, the CSS was implemented with TailwindCSS, while the animations were done with framer-motion. We also used various dependencies such as TradingViewWidget to display the graphs • The Web3 backend was coded in Solidity, Javascript, and Typescript • The mutual funds were built with smart contracts, while proposals are made via DAO proposals • Blood, sweat, heart, and tears. Mostly tears tho. 🚧 Challenges we ran into Throughout this hackathon, we ran into a plethora of challenges. For starters, none of us were familiar with Web3 technologies, meaning we had to learn everything from scratch. It was a huge struggle brainstorming an idea and architecturing a working structure that had no loopholes.This was an especially difficult challenge because Axelar was built for people who’ve had prior experience with Ethereum, which we did not. Hence, we had to read up on both Axelar and Ethereum! Finally, as these technologies are so new, there is still very limited documentation. In fact, most of the documentation we used was only 2-3 months old! This meant that we had very little to go off of, and required us to really rack our brains to figure out how to implement certain features. With guidance from Axelar mentors, we were able to surmount this gargantuan challenge. Overall, it was a huge challenge learning and implementing so many new concepts in such a short time frame! ✔️ Accomplishments that we're proud of We are extremely proud of overcoming the seemingly endless stream of difficulties that come with using new, cutting edge technologies. We take pride in successfully navigating such a new technology, often having to come up with innovative ways to tackle certain problems because of the limited documentation. Additionally, this was all of our first times navigating such a foreign technology, and we take pride in the fact that we were able to understand, plan, and implement everything in such a short time frame. All in all, we are proud to be innovators, exploring the uncharted territories of Web3! 📚 What we learned We can wholeheartedly say that we have come out with significantly more knowledge on Web3 compared to when we came in! For starters, before we even began architecting our project, we read multiple articles on DAO and Axelar. Whether it's engineering decentralized systems, architecting cross chain transaction systems, or working with smart contracts and solidity. Last but not least, we learned many core skills, imperative to a software developer. Whether it’s learning to navigate extremely new documentation, or implementing completely new algorithms within a short time span, or to invent innovative ways to bypass problems. We can confidently say that we have inarguably become a better developer throughout Hack the North! 🚀 What's next for Just DAO It! We have a few things in mind to bring Just DAO It! to the next level: Allow for members to propose token-to-token trading (ex. direct MATIC -> AVAX) Deploy our DAO and Proxy contracts to the mainnet Support even more chains Use 0xsquid to convert tokens due to its direct compatibility with Axelar <div