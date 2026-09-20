---
slug: "ceres-yield-aggregator-for-the-people"
url: "https://devpost.com/software/ceres-yield-aggregator-for-the-people"
title: "Ceres: Cash In Cash out to BRL and DeFi for people in Brazil"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 998
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/video_visual"
---

# Ceres: Cash In Cash out to BRL and DeFi for people in Brazil

> Ceres aims to simplify DeFi, with a built in Cash In - Cash Out to BRL and a simpler UX so that non crypto natives can enjoy higher yields and risk exposures tailored to their profile.

[Devpost](https://devpost.com/software/ceres-yield-aggregator-for-the-people) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[agriculture_food]] [[finance_payments]]
**substrate** [[financial_record]] [[regulation_legal_text]] [[video_visual]]

**stack** digitalocean, mongodb, node.js, react-native, tecnospeed, truffle, web3.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ceres: cico and yield aggregator for the people

## Body

Home Logo Portifolio view Portifolio View Investment Details Kresko asset view Inspiration We conducted user interviews with people who are new to crypto in Brazil and we were inspired to solve a few problems that we found when introducing DeFi for the people. Such as: a) The average person thinks it is too difficult to use DeFi. They do not want to go through the trouble of learning to do it. b) The average person wants to invest (and see their returns) in their native currency, they do not care which tokens are being purchased. c) Every person has different risk tolerance levels. For some people, $200 is their life savings, and it can be devastating for them to lose 50% of the value. d) The average user wants to be able to convert BRL in their bank account for cUSD in a seamless way, through the PIX instant payment system. What it does Ceres has a built in Cash In Cash Out in Brazilian Real so that users in Brazil can move from crypto to fiat in a seamless way. Our vision is that it will take less than 20 seconds for the user to make a request, and it to arrive in the user´s bank account. Also, unlike other Yield aggregators, Ceres is focused on understandability and a simpler UX. It was designed for the user who is new to crypto to take advantage of the DeFi yields according to their risk profiles.). It will be easier to use and to understand, denominated in the native currency of the user (Brazilian Real), with a UX similar to investing through banks, with different risk tiers and it will make DeFi accessible to the average individual in developing nations, starting in Brazil (our home country). How we built it We built it by forking our Lovecrypto project to provide the infrastructure for Signup/Login and wallet management, therefore, abstracting the complexity of creating a wallet and handling private keys for the new user. In addition, we developed a Cash In - Cash Out architecture to allow people to convert BRL in their bank account to cUSD via PIX (instant payment system). In order to be fully compliant with regulations in Brazil, we manually do the KYC by analyzing their pictures, photos and proof of address. Also, all trades are reported to Receita Federal by the end of every month, according to the regulation. The connection to the PIX instant payment system is handled through an API from Tecnopay. That way, we detect when the user does the Cash In, and transfer the value when the user does the cash out Finally, we built a smart contract that automates the investment in an Ubeswap pool and farm, withdrawing and reinvesting the yields every X hours. Therefore, providing a higher yield than just leaving in the Ubeswap farm without withdrawing and reinvesting. It is also a simpler UX, because the user only has to handle cUSD. Challenges we ran into One challenge is that our Yield aggregator contract is not audited, so we advise people not to invest a large sum of money before it can be reviewed by an audit firm. Another challenge is that we suffered a Ransomware attack during the hackathon. It was just a small part of the application compromised, but it shows that we need to do a complete information security review before we go on production with Ceres. Accomplishments that we're proud of We are proud that we could dive into the problem and conduct interviews with potential users. Understanding that what the regular user need to invest in DeFi is a simpler and more familiar UX. We are proud that, part of what we developed during the hackathon will allow users from Lovecrypto App (our first product) to be able to exchange from cUSD to BRL in less than 20 seconds, thanks to an integration with the PIX instant payment system. We are proud that our team is united and motivated around the mission of creating a world of shared prosperity. What we learned We learned that different people have different risk profiles. We have to respect that and contemplate the risk appetite of people who are crypto noobs or crypto degens. We learned that people think in their native currency. We learned that people do not want to go through the trouble or learning how to invest in DeFi. They think it is too hard. We learned that the potential market for an easier DeFI experience in Brazil is huge because our country is experiencing an escalating inflation and the purchasing power of the brazilian real lost 15% of the value from 12 months before. Therefore, people want to protect their savings from inflation. The number of individuals subscribed in the Brazilian stock market is 3.4 Million people, a growth of nearly 90% in relation to just two years before. All those people are potential investors in DeFi through Ceres. What's next for Ceres: CICO and Yield Aggregator for the people To complete both the Cash In and Cash Out flow 100% automated, that we could not do it on time during the hackathon. To raise a seed round of $300,000 in investment so we can have a proper liquidity pool both in cUSD and in BRL, and to have runway for two years while we perfect our CICO into an API service that can be installed in third party apps building on Celo. To adapt the Iddle Finance ( https://idle.finance/#/ ) yield aggregator smartcontracts to the Celo blockchain, and build our innovations in UX and understandability on top of it. To make it accessible for anyone with a Celo Wallet, rather than needing to download our App. Connectable through Valora, Metamask, Ledger and others. To integrate with other projects, like Kresko. Therefore, people will not only be able to invest on Farms, but on synthetic assets on Celo. This is our Github repo for this project: https://github.com/celo-org/make-crypto-mobile-hackathon/pull/42 Link to APK: https://drive.google.com/file/d/1zA0u2V1vOxy4H85zkH0ftIoN0N2qbA7F/view?usp=sharing <div