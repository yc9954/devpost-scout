---
slug: "social-maven"
url: "https://devpost.com/software/social-maven"
title: "Maven"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 589
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Maven

> Enabling social media agencies to trustlessly manage Lens profiles on behalf of individuals, companies, or DAOs.

[Devpost](https://devpost.com/software/social-maven) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets


**stack** amazon-web-services, chainlink, eks, javascript, next.js, solidity, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for social maven

## Body

Inspiration Social media management is huge in web2, but we have not seen anything emerge for it yet in web3. Despite Lens Protocol's continued growth, today there isn't a way to safely allow a social media agency to manage your profile on your behalf. We are building Maven to fill the gap. What it does Maven is a platform designed to allow agencies to manage Lens profiles on behalf of their clients trustlessly. With advances in account abstraction, it is now possible to allow an agency to post with your Lens profile without giving them the ability to steal your profile away from you forever. How we built it By combining Thirdweb smart accounts, a smart contract, our frontend, our Chainlink node, and a Chainlink External Adapter, Maven can allow users to keep control of their profile, while granting an agency the ability to post on their behalf. Challenges we ran into This was our first time creating a Chainlink External Adapter, and we ran into a few hiccups along the way. The piece that held us up the most was getting the job to execute once it had been deployed to our Operator node. Thanks to some help from the Chainlink Discord, we realized what we were missing and got it to work! Integrating Lens profile and Thirdweb to allow agencies to post on behalf of users in a smart wallet proved difficult, and we did not finish the integration before the hackathon ended. However, we have a good path forward, and are planning on having our POC built within the next few weeks that will include this functionality. This was also our first time hosting Chainlink nodes on AWS EKS. Coming from the world of ECS Fargate, this was a big lift, but one that enabled us to better scale and operate our Chainlink node, and make it far more ready for an eventual production deployment that could eventually include many other services. Accomplishments that we're proud of As far as we are aware, we built the first External Adapter that gathers data about Lens profiles. While it only gathers the total number of posts on a profile today, we believe this could be greatly extended to allow data about Lens profiles to make its way into smart contracts for an unlimited number of use cases. We are looking forward to extending the EA, and trying it out as a Chainlink Function at some point in the near future. We are also not aware of many use cases yet with Lens profiles and account abstraction. We believe we are doing something new and exciting in the AA space, and are very excited to launch our POC in the next few weeks after the hackathon. What we learned We learned a ton about AWS EKS through this hackathon, as we were determined to host our Chainlink node and external adapter on it. We also learned a lot about gathering data from the Lens API to enable our external adapter. What's next for Social Maven We are very passionate about this project, and intend to continue to build it out. We want to spend more time on making the user experience as smooth as easy as possible, including automatically spinning up a smart account on behalf of the user, paying any gas fees for them, and making agency management of profiles easier. We also want to spend more time making our backend infrastructure more stable for production usage, and continue to build out our frontend with extra functionality. <div