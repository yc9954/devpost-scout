---
slug: "multiverse-fighters"
url: "https://devpost.com/software/multiverse-fighters"
title: "Multiverse Fighters"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 902
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Multiverse Fighters

> Play-to-earn turn-based MMORPG with a card combat system and deep social involvement.

[Devpost](https://devpost.com/software/multiverse-fighters) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[structured_db]] [[web_dom]]

**stack** digitalocean, graphql, nextjs, node.js, react, redis, rust, typescript

## How they structured the write-up

- introduction
- trading system:
- problems we faced
- what is done:
- what's next for multiverse fighters

## Body

Introduction Hello, dear colleagues! We are pleased to present to you our project "Multiverse Fighters" - MMORPG in the setting of the battle of Magic and Technology with a turn-based card combat system and deep social engagement. The player is represented in the game as an eternal Avatar (account), and in search of “Power”, he will need NFT cards. Defeating opponents, the Player receives Trophies and Parts from which he creates Equipment for his Avatar. Collecting your unique NFT collections. The incredible progress of blockchain technology and the possibilities of Near have inspired us to rethink the vision of classic browser games. Based on the DAO philosophy, we offer players various ways to make money in the game while helping our community. Our task is to make the combat system of the game, which not only makes you want to return again and again, but is also pleasant just to watch or stream. Trading system: As part of creating an economy and mechanics based on NFT and in-game tokens, we needed original solutions for our own marketplace. Players will be able to trade NFTs - in-game items such as weapons, armor, avatars, and consumables. Players will be able to buy and sell items through direct sales, private sales, or scheduled public auctions on our in-game marketplace. Item ownership and a player-driven economy are paramount in the latest blockchain games, and as such, we give players complete freedom of action. Providing a loan. Players will be able to lend their NFTs, such as in-game weapons and items, to other players for a fee. Simply select the NFTs you want to borrow, the loan term, and the type of loan fee. Loan options: the owner of the NFT collects an advance payment from the recipient; the NFT holder charges a percentage of the tokens earned during the loan term. (coming soon) Problems we faced Ecosystem problems: lack of comprehensive solutions for browser game developers who want to integrate their project into the Near ecosystem. Developing problems: 1) Smart contract migration - the documentation does not describe how to do it correctly. 2) Gas - there were some problems when changing the smart contract, after which his methods required more gas. And on the front end, less gas was used and calls to contract methods fell. 3) TheGraph is a good technology, you can quickly publish a subgraph and interact with it through GraphQl (which is what we need). Because we store part of the data in our database and it would not be convenient to build large sql queries in 2 databases at once. But another projects can find it yousifull What is done: 1) Synchronization with the blockchain, recording the necessary logs in our database. Further, based on the logs, the database is filled with data (Nft, Account, Rent, Sale), so that you can make a selection for ui using complex filters. 2) Rental smart contract, any nft can be listed on the stock exchange, indicating the price per hour of rent and the time range (from how many to how many hours nft can be rented). The buyer chooses the required rental time from the range specified by the seller, and after the purchase can use this NFT in the game. 3) Fraction - works as an extension of the NFT smart contract. When a new "faction" is added, an NFT is created (which the user will receive) and the desired items to create are specified. When the user collects all the necessary details, he can burn them, after which he will receive a new NFT in his collection. 4) TheGraph - created a subgraph for smart contracts (NFT, market, rent, FT). What's next for Multiverse Fighters Within three months, our team was able to make a full-fledged product for users - an NFT store based on ready-made solutions provided by the Near community and our own original solutions. During the work on the store, many technical problems were solved, which gave us a more complete understanding of the possibilities of blockchain technologies. This allowed us to form a workable core gameplay design for our players and start developing the game itself. Unlike the pyramidal economic model, our task is to create a self-replenishing living economic system for the entire period of the game's existence. This directly affects the formation of the price of our NFTs and, of course, the most valuable thing - the trust of our players. Although we have done a lot of preliminary work on the project, there is still a lot to be done. We are sure that the Near community needs a complex game project that will demonstrate all the advantages of the technologies used, and the players - an exciting game with an exciting combat system that their friends want to watch online stream. Our global goal for the Near community is to provide affordable browser game development tools through our API package: advanced in-game store with DEX function and auctions of your choice NFT features: fractionation, rent, royalty, gacha game connect aurora bridge bridges to large NFT trading markets token smart contract system: liquid staking, game mechanics and discounts system Dear colleagues, thank you for your interest in our project! We are proud to invite you to visit our website Mfight.io where you can test our store (hackathon project), find the latest news and immerse yourself in the game lore of our game. <div