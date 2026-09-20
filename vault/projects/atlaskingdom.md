---
slug: "atlaskingdom"
url: "https://devpost.com/software/atlaskingdom"
title: "AtlasKingdom"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 945
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# AtlasKingdom

> AtlasKingdom is a novel protocol that mixes gaming and work, powered by Atlassian Forge.

[Devpost](https://devpost.com/software/atlaskingdom) · hackathon [[Devs Unleashed]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** atlassian, confluence, forge, jira, storageapi, unity

## How they structured the write-up

- brief
- why ❓
- gameplay 📜
- architecture ✨
- attractions ☘️
- challenges we ran into 😏
- future updates ✔️

## Body

Brief This game is a novel protocol that mixes gaming and work . At the core it is a game which rewards users on doing certain tasks powered by the Atlassian platform. Users can enjoy and earn in a variety of ways, including but not limited to Playing Game , Completing task, Writing blogs Live streaming gameplay, staking weapons as well as selling on secondary market places. We strongly believe that a good game is an amalgamation of Scarcity, Thrill , Realtime and Sharing. We have combined various elements to bring these properties. Why ❓ It's very essential to have a friendly working environment but in the current times people have moved away from small talk and are finding it easier to interact over something entertaining whether it's playing pool in the office or playing game with there colleague so in order to accomodate this demand we came up with a unique solution in the form of AtlasKingdom. It is a game that integrates very well with a suite of atlassian products and based on certain events rewards the users. Gameplay 📜 Build the most powerful kingdom and army The core of the game lies in creating your own base and attacking other bases to earn Players can earn coins by completing the task on JIRA and whenever there blog/page/doc written on Confluence gets like/comment. This is how they passively collect coins as we have programmed our backend to listen to events from both JIRA and Confluence inorder to reward users. To give a more detail overview Miners: Miners are locked when a player adds them to there base. Once locked miners start producing coins every second and after certain amount of time the storage is filled so players have to keep collecting. On upgrading miner level the storage capacity and per block output increases Assets : This are in-game assets that include defenders and attackers. Once a player places them in there base the assets get locked and when a player removes them from there base the assets are unlocked and can be sold in the secondary market place. Currently we have 6 such assets. Cannon Xbox Tesla Archer Valkyrie RoboDriller Beside depending on secondary market place we have our own marketplace in which user can buy/sell various assets. 3D Marketplace : We have our own marketplace in which users can buy/sell there assets. The best part about the marketplace is that players can visualize the asset in 3D before buying it. This gives them the overview of how they will look in the game. Architecture ✨ We have integrated closely with Atlassian platform's various products inorder to utilize it completely and make the game as fun as possible. Confluence and JIRA : We are utilizing the events emitted by the Confluence and JIRA inorder to update the user stats and coins in game. users get rewarded based on there actions such as issues, approving and merging pull request on JIRA and writing docs and getting likes and comments on Confluence docs Atlassian Forge : We have used many features provided by atlassian forge inorder to maintain the state of backend as well as serve the frontend Storage API : In order to store data such as user stats we are using the storage API provided by Atlassian forge and is very easy to integrate on our platform. CUSTOM UI : As our game is designed and built on Unity we are using invoke bridge to calll resolver this allows us to integrate with atlassian forge securely. Product Events : We are listening to various events emitted by different Atlassian products inorder to reward users as well as unlock user assets. Web Trigger : We have utilized this web triggers inorder to store confluence related events on the jira storage api because our game integrated both Confluence and Jira Attractions ☘️ Guilds : People always like playing games together and allowing players to form guilds increases the interaction and active users. Guilds will be a core part of the game and users will be able to form team with their colleagues Mystery Boxes : Players will be able to buy and earn mystery boxes for their proof of contribution. Creating organic growth and demand. Clan War : Inorder to make thing interesting every month we can organize clan wars where colleagues form different teams and attack each others bases,complete various task to get more coins. Challenges we ran into 😏 Art Work : Beautiful Art requires time we have been working on this game for more than two months and are very proud to present our 3D assets. We currently have 8 3D assets which we plan to increase over time Merging Events : It was a bit tough to merge events coming from both Confluence and Jira, so we setup a webtrigger on jira and on every event from confluence we add the confluence event to jira state inorder to maintain a persistent state Future Updates ✔️ We truly feel that gaming can connect people. We want to take this project to it's full potential. Future updates that we have planned are : Integrate Bitbucket : Add bitbucket commits as events and also monitor them for the user Improve Datapoints : Add more datapoints to reward function so the users can be rewarded more appropriately Bringing Tournaments : Users will be able to fight in the tournaments for rare assets Forming Guild : Players will be able to form guild/clan so during an attack they can send some help to fellow guild member. Adding more Assets : We want to increase our library of assets such as defense assets and attacker assets <div