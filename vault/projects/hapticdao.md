---
slug: "hapticdao"
url: "https://devpost.com/software/hapticdao"
title: "HapticDAO"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 795
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# HapticDAO

> Haptics enabled Dapp that has DeFi accessibility features for those with disabilities. The focus group is for those who are visually impaired or blind, however we hope to serve everyone.

[Devpost](https://devpost.com/software/hapticdao) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[voice_speech]]
**domain** [[accessibility]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]]

**stack** chainlink, javascript, moralis, oneinch, react, solidity, spline, truflation, uniswap

## How they structured the write-up

- inspiration
- what it does
- how we built it
- technical stack
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hapticdao

## Body

Home Entering Application Dashboard DAO Truflation DEX Haptic 3D hands Inspiration Sergey Nasarov opened this hackathon with a powerful statement. He stated that we as a space will "redefine the relationship between users and services”. There are millions of individuals globally who are unable to access and benefit from DeFi and the web3 space due to lack of accessibility. There is no single solution. We will need everyone on board to help start initiatives to foster a greater level of inclusivity. We have some of the brightest minds and the best innovation in this space. Let us not port existing problems from Web 2 to Web 3 Therefore, one such initiative we would like to humbly present to the Web 3 and blockchain community is : HAPTIC DAO What it does Haptic DAO is more than a DAO. Our project is designed to be a one-stop-shop for anyone with a disability or for any average user. We designed the UI as a relatively simple, straightforward experience. Pages are consistent and individuals do not need to adjust their mental model to navigate them. At the top of every page is an audio instruction to provide guidance on how to use that page. For the mvp we have 4 major features: Dashboard: -Users may retrieve their wallet balance via voice command -Users may request token prices fetched from chainlink data feeds via voice command -Non-visually impaired users may fetch chainlink price feed data through text input DAO -Users may upvote or downvote on feature proposals -> persisted on chain -Users may add feature proposals ->persisted on chain -Visually impaired users may select feature cards to hear dynamic audio playback Truflation -Leveraging Chainlink data provider Truflation -Users can sync latest inflation data and select each category to hear audio playback -Currently yoyInflation is supported; Truflation team indicated that the endpoints for other categories are not yet available. Placeholder function calls were deemed suitable in the interim DEX -Integrates Moralis oneInch plugin -Allows for quotes and token swaps via voice command -For non-visually impaired users, we have integrated uniswap dex on the ui as well How we built it We built Haptic DAO using React JS for the frontend and Solidity for the backend. Our repository includes Django python. For this hackathon we have not built the python use cases. Use cases and data features that would require python will be built at a future time. One example will be to add voice commands to an IoT device using python libraries. This would help expand into a wider range of use cases. In the future we would like to also create a separate mobile application using react-native. Technical Stack We have used the following technologies/tools to build our solution: -Moralis -OneInch -Uniswap -Chainlink -Truflation -React JS -Solidity -Django Python (for future development, less so currently) -Spline Challenges we ran into Timing and availability were among the most pertinent challenges. We had some library dependency challenges within react, however through thorough troubleshooting we were able to resolve them :) It was our team’s first time using keepers, we learned that setting a higher gas limit and funding the registry with more link is a MUST! Accomplishments that we're proud of One of the most notable accomplishment is that users can enact Token swaps via voice command on polygon. We were quite proud of this milestone and it is a step towards true inclusivity for everyone in this space 😎 Some other milestones that made us very proud and excited included: -Users being able to request their Metamask balances to be read aloud via voice command -Strong haptic vibrations for swaps to insure user is aware that the transaction is occurring -DAO governance model that reads choices aloud and allows our users to have a say in the development direction of this initiative -Truflation rates, which allow for up-to-date inflation data for our users to bear in mind as consumers and investors What we learned We had not heard of Truflation prior to this hackathon. This became a source of strong interest for us as this information is rather vital in our current times. Through a combination of truflation and chainlink we expanded our knowledge into priceFeeds and data providers. From a solidity standpoint we learned how to properly flatten files so that etherscan does not complain 😁 We also expanded our knowledge of keepers and greatly enjoyed it more than traditional cron jobs in web 2. What's next for HapticDAO The blockchain space has some of the brightest minds and the rapid pace of innovation is unparalleled. We would like to expand this initiative and build out more and more use cases. For individuals who feel they would like to contribute, feel free to reach out to us. hapticdao@gmail.com <div