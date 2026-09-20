---
slug: "inheritokens"
url: "https://devpost.com/software/inheritokens"
title: "Inheritokens"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 721
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Inheritokens

> Inheritokens lets you inherit the tokens and NFTs from a digital wallet when chosen as a nominee. You can also nominate someone as your heir to your assets.

[Devpost](https://devpost.com/software/inheritokens) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**substrate** [[financial_record]] [[web_dom]]

**stack** bttc-api, css3, html5, python, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for inheritokens

## Body

Profile_Page Signup-page Landing-page Multiple Nominee Flow Backend flow Front end flow Priority Nominee Flow Inspiration We already know the value and the fame cryptocurrency is gaining with the current global scenario. With cryptocurrency, tokens, and NFTs being valuable assets, it's not right for them to be locked away in an account that fails to dissolve after the account holder's demise. What it does This platform is to ensure that valuable tokenized assets and NFTs do not get stuck within one's account after their demise. So, the tokens are transferred/ handed over to the nominee chosen by the user account. Our smart contract monitors the account activity and if it has been inactive for more than 6 months, an email is sent for confirmation. If the user doesn't respond, the nominee gets an email to claim the assets nominated for them. Inheritokens allows adding multiple nominees and also have a level of nominees. Thus, if the first level of nominees fail to claim the assets, the second level of nominees become the rightful claimant. We also provide an option of donating some/all portion of assets to Non-profit organizations. The TRON Community can play an important role in suggesting and collaborating with good nonprofits. How we built it React.js was used to build the front end. We developed a Flask API for signup so that the user would get an email with a magic link in it. After our platform has verified the user's email, it will take them to their profile page. On the TRON network, we deployed a smart contract that we created. When a user nominates an asset for the nominee, we employ the TRC20 and TRC721 capabilities to get their prior consent. The user's assets won't be held by our contract. To automatically check if the user's wallet has been idle for six months, we developed a Python schedule. We are using the user's wallet's transaction history for that. Our Python application automatically emails the user if their wallet has not been used for six months. The script will automatically send an email to the nominee that the user has nominated, if the user doesn't respond within a month. To use our site and claim the assets for which they were nominated, the nominee must click on a link they received in the mail. Challenges we ran into Determining the appropriate time to declare the user deceased and transfer their assets to the nominee was a hurdle. You can accomplish that in a number of ways. Thus, it became difficult to determine the optimum approach. Regarding the technical aspect, it was difficult for us to host the Flask API on a server because it was throwing issues. Accomplishments that we're proud of Our first goal was to figure out how to make it simple for users to nominate assets for a nominee on our platform. Looking at our platform, we are proud that the user only needs to follow a few steps, as we intended, and that our UI/UX is better than we expected. The entire backend and front end have been integrated. We're very happy that we were able to finish the project on schedule and that our platform is now live. We also feel satisfied that our entire website is functional. What we learned While building this project, we learned about TRON, and how to deploy smart contracts on the TRON network. We also learned about TRON tools such as the TRON IDE and the integration of contracts using TRON Web. What's next for Inheritokens Upcoming Plans: 1) To enhance the platform's functionality for smart wallet backup and recovery - in case of lost private keys. We'll finish this functionality shortly because it's simple and only requires a few minor adjustments. 2) For the BTTC chain, we can only display native token balances because APIs for NFTs and erc20 tokens are not yet available. We will bring other assets onto our platform in version 2. 3) Our next version will also provide a list of charities that users can select. In the event of the user's death, as well as the nominee's death, we can transfer the user's assets to the charity that he or she has designated. 4) Making the platform compatible with multiple blockchains to increase the accessibility for a wide range of users. <div