---
slug: "ustx-t-boost"
url: "https://devpost.com/software/ustx-t-boost"
title: "T-Boost by USTX Team"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 951
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/web_dom"
---

# T-Boost by USTX Team

> TRX yield generator and USTX buyback booster

[Devpost](https://devpost.com/software/ustx-t-boost) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**domain** [[agriculture_food]] [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** html, javascript, php, solidity, tronide, tronlink, tronscan

## How they structured the write-up

- inspiration
- what it does
- what are the benefit for the users
- what are the benefits for the ustx ecosystem
- what are the benefits for the tron ecosystem
- what are the conditions of use
- what are the risks of t-boost
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ustx t-boost

## Body

Inspiration In USTX Team we believe that the crypto industry should provide tools to give individuals financial freedom. These tools should be easy to use and safe. T-Boost is one additional piece of the USTX infrastructure, a step further to the goal of providing a complete solution for a risk balanced and profitable portfolio for our loyal users. What it does T-Boost is a TRX yield generating dApp that gives weekly rewards in USTX tokens. The rewards are bought back from our bespoke DEX are not locked in any way. The internal smart contract logic manages the user deposits implementing a pseudo delta-neutral strategy on TRX-USDD LP, providing and abstraction level to complex JustLend and Sun platforms. The end user faces a comfortable interface, not different from most staking platforms: deposit, withdraw, claim rewards. What are the benefit for the users Using T-Boost the users will gain access to a high rewarding staking solution for Tron network native coin: TRX. The net user APR will be above 10%, at current market conditions. All the complexity to implement the strategy is handled by the smart contract, so the user benefits from a comfortable interface. What are the benefits for the USTX ecosystem The rewards are distributed in USTX, our project native token, and are generated from weekly buyback on our bespoke DEX. This will keep a constant positive push on the token price. The users will be free to decide what to do with the rewards: keep them in USTX or exchange them in any other token using our DEX , Sunswap or JustMoney swap services. What are the benefits for the Tron ecosystem Every TRX deposited on T-Boost generates TVL on Tron ecosystem with a multiplier effect: 0.725 TVL on JustLend (TRX deposits) 0.55 TVL on SunSwap (TRX/USDD LP) 0.55 TVL on Sun farming (TRX/USDD farm) So globally 1 TRX into T-Boost generates 1.825 TRX TVL across the Tron ecosystem, or a 1.825X multiplier What are the conditions of use Interface: web app accessible via browser (pc, mac, mobile) Wallet: Tronlink (Math and Klever will be validated shortly after the release) Deposit coin: TRX Rewards token: USTX TRC20 Deposit lock: 1 full epoch (epochs duration is 1 week, changes every Saturday) Rewards lock: none Fees: app requires energy to operate, a portion of the rewards will be used for buyback and reserve (max 25%), balance withdraw is not taxed unless the equity ratio is below 100%. This can happen after significant changes in TRX price, but recovers naturally within a few days. The team will create a reserve in the contract to avoid equity ratio < 100%. Custody: the deposits are fully managed within the contract, they will NOT be moved to team wallets. The smart contract handles all the interactions with JustLend, SunSwap, Sun.io and all other contracts required to manage the strategy. Management: the team will monitor the equity level continuously and weekly will re-balance the strategy if needed, to make sure that it stays close to neutrality. APR: T-Boost yield will vary over time and will depend on Sun.io and JustLend conditions. The team will make sure the contract parameters are always optimized for the best yield and lowest risk. Anti-whale: There is a limit on how much a single user can deposit. At launch the limit will be 100,000 TRX but it will be increased after a few weeks. What are the risks of T-Boost As always, we want informed users, so here’s the risks associated with T-Boost: smart contract risk: we carefully designed and tested the contracts on Nile and mainnet, but human error can never be excluded 100%; capital risk: in case of TRX price variations, the value of the underlying assets (deposits, borrows and LP value) can go below 100%. The team will make sure that over time and adequate reserve will be created to handle these events; liquidation risk: USDD is borrowed from JustLend against TRX deposits. The strategy is balanced so that if TRX price is reduced up to 50% there is no liquidation risk. The team will monitor the margin and act to re-balance the strategy in case of significant variation from nominal; TRX price risk: the contract works with TRX, so all values are relative to TRX. If TRX price falls, the same will happen to the deposit value. This risk is NOT strictly related to T-Boost, but is present every time the user holds TRX (or any other token). This is not financial advice, DYOR. How we built it HTML, JS, PHP, Tronweb, TronIDE, Tronscan Challenges we ran into Debugging interaction with platforms that are not present in testnet. JustLend and Sun farming where tested directly on mainnet Accomplishments that we're proud of The dApp has the comfortable look and feel of the other ecosystem dApps, so we expect a good reception by our users. New users will find the interface intuitive and easy to use. What we learned TronIDE has become a very usable platform for developing complex contracts (proxy + implementation), the same goes for Tronscan. The development teams did a great job of making Tron the best platform not only for users, but also for developers. What's next for USTX T-Boost The goal is to increase USTX and Tron TVL and generate more revenue to be used for USTX buyback. The overall project goal is to be 100% sustainable and T-Boost, after WARP, is another important step in the right direction. Disclaimer: T-Boost is a completely new dApp, with new functionality, released within the USTX ecosystem in addition to many other dApps (DEX, STAKING, TELEPORT, WARP, UPFOLIO, VOTING). Considering the HackaTRON rules, the team considers T-Boost a new project, developed entirely after September 20th 2022. <div