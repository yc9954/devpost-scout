---
slug: "hextopus"
url: "https://devpost.com/software/hextopus"
title: "Hextopus"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 1053
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/revocation_withdrawal"
  - "substrate/financial_record"
---

# Hextopus

> On-Chain Referral Marketing(Share-to-Earn) Platform

[Devpost](https://devpost.com/software/hextopus) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[cross_origin_web]] [[revocation_withdrawal]]
**substrate** [[financial_record]]

**stack** javascript, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hextopus

## Body

Inspiration In the traditional market, there are various marketing agencies and methodologies for efficient use of a limited marketing budget. However, unlike the traditional market, the web3 market operates based on a wallet, making it difficult to apply the traditional marketing-efficiency analysis. In addition, in order for the existing marketing agencies to implement DApp/DAO’s CPA(Cost-Per-Action) marketing, additional understanding and development ability of smart contracts are required. For these reasons, marketing means in web3 are limited to influencer marketing or community marketing. Hextopus aims to solve this problem by developing an on-chain referral marketing platform. All DApps/DAOs in the TRON ecosystem who want to do marketing can leverage HEXTOPUS by creating Hextopus campaigns and charging marketing budget to the campaign reward pool. We believe that TRON's strong community is best suited to be a solid starting point and support for the block-chain marketing ecosystem that Hextopus is trying to build. What it does HEXTOPUS is a ShareFi on-chain marketing platform. DApp/DAO can start marketing by creating a campaign, and the generated campaign will goes viral through a referral link from the participants. Campaign Customization : Campaign creators can set all smart contract-based actions as target action conditions and allow rewards to be distributed only when target actions are performed by users - CPA marketing. In addition, campaign creators can create an event-type campaign aimed at a specific holder group by setting only qualification condition without a target action. Referral Marketing : Hextopus campaign is basically based on referral marketing. With Hextopus, DApp/DAO can maximize marketing reach through viral effects. Abuse Prevention Mechanism : Hextopus minimizes the number of cherry pickers through its own optimal participation deposit scheme. Minimum Participation : When creating a campaign, if DApp/DAO enter the amount of rewards to charge in the reward pool and the minimum number of participating wallets, Hextopus campaign contract automatically sets the reward schema to ensure the minimum participation. This makes it easier for DApp/DAO to quantify the correlation between marketing cost and efficiency. Withdrawal : DApp/DAO can withdraw its marketing budget from the reward pool after a certain period of time. Consecutive Referral Chain Hextopus is a protocol that allows users to earn rewards through both ‘participation’ and ‘share’. When users participate in a campaign, they can receive participation rewards and their unique referral links are generated. Once generated, these links can be shared among their community and if their referrals also participate in the campaign, the user is rewarded again for the successful referral. Participants are eligible for ‘1st level referral rewards’ arising from direct participation for each of their referees, and ‘2nd level referral rewards’ for their referees’ successful referrals. For example, a campaign with a participation reward scheme [50 (DApp's reward token), 10 (HXTO)] , a direct referral reward scheme [25 (reward token), 5 (esHXTO)] , and an indirect referral reward scheme [10 (reward token), 1 (esHXTO)] will result in the reward structure described below. Analyzing Participant A's total rewards, Participant A receives 50 reward tokens and 10 HXTO for his/her direct participation . Through Participant A's link, he/she has also shared the campaign to Participants B, C, and D, who all have participated in the campaign. Then Participant A is eligible for an additional 25 reward tokens and 5 esHXTO arising from direct participation for each of his referees. If Participants E, F, G participate indirectly through either Participant B, C, or D's referral link, then Participant A will be eligible for another 10 reward tokens and 1 esHXTO for each. Thus the total rewards received by Participant A is 155 reward tokens, 10 HXTO, and 18 esHXTO . Note that this consecutive scheme is currently restricted to only three layers, so any participation by users further down in the tree will not be considered when calculating Participant A's rewards. Calculating from Participant B's viewpoint, 50 reward tokens and 10 HXTO** for his/her direct participation . Through Participant A's link, he/she has also shared the campaign to Participants E and F, who all have participated in the campaign. Then Participant B is eligible for an additional 25 reward tokens and 5 esHXTO arising from direct participation for each of his referees. If Participant H participates through either Participant F's referral link, then Participant B will be eligible for another 10 reward tokens and 1 esHXTO . Thus the total rewards received by Participant B is 110 reward tokens, 10 HXTO, and 11 esHXTO . How we built it HEXTOPUS’s marketing campaign is fully on-chain. Challenges we ran into It would be a problem for HEXTOPUS to ensure that the effects of marketing spread to mass public. Hextopus attracts existing crypto people with participation rewards, and with referral rewards, Hextopus marketing goes viral even to the normies. However, there are many hurdles for normies to participate in the campaign, such as transaction fees, participation deposit and etc. Hextopus wants to overcome these hurdles by developing functions such as transaction fee delegation and participation deposit delegation by other HXTO holders. Accomplishments that we're proud of Build a first on-chain marketing platform on Tron Ecosystem. Overcome technical challenges to accomplish goals. What we learned Throughout the journey, we have learned to Build a complete dApp on TRON. Deploy a Smart Contract and the concept of it on TRON Blockchain. Use the TronWeb library to interact with Wallets and Smart Contracts. What's next for Hextopus Project Milestones : Designing the UI/UX (O) Writing Lite Paper (O) Developing Frontend (O) Building Backend smart contracts (O) Developing Campaign creator admin page (X) Project Roadmap Hextopus Lock (2023 Q1) Hextopus Lock makes the ecosystem safer by ensuring the reliability and safety of DApps. It making DApp’s community trust-building process clear and easy. DApps will be given a certification mark and benefit from the campaign creation process. Premium Pass NFT (2023 Q1) Premium Pass NFT offers exclusive opportunities for multiple Hextopus events such as campaigns or airdrops only for Premium Pass NFT holders. Boost NFT (2023 Q2) Boost NFT is used for boosting referral rewards for a certain period of time. It accelerates campaign participation and increases the value of HXTO. Hextopus Community Platform (2023 Q2) To further accelerate Hextopus’s growth, Hextopus will launch its own community platform to write and share articles about crypto. The more high-quality content is shared, the more rewards the user will receive. <div