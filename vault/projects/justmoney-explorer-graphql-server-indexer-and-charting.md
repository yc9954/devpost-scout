---
slug: "justmoney-explorer-graphql-server-indexer-and-charting"
url: "https://devpost.com/software/justmoney-explorer-graphql-server-indexer-and-charting"
title: "JustMoney Explorer: GraphQL Server, Indexer, and Charting"
hackathon: "TRON Grand Hackathon - HackaTRON Season 7"
organization: "TRON DAO"
winner: true
words: 1158
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# JustMoney Explorer: GraphQL Server, Indexer, and Charting

> JM Explorer integrates GraphQL-based indexing to provide detailed blockchain data insights, featuring dynamic charts and analytics, streamlining the process of tracking and understanding transactions

[Devpost](https://devpost.com/software/justmoney-explorer-graphql-server-indexer-and-charting) · hackathon [[TRON Grand Hackathon - HackaTRON Season 7]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[sensor_telemetry]]

**stack** credshields, emberjs, google-cloud, jm, kubernetes, mysql, node.js, solidityscan.com, sunswap, tronrpc, tronscan, typescript, vercel

## How they structured the write-up

- justmoney explorer: graphql server, indexer, and charting
- introduction
- inspiration
- what it does
- how we built it
- challenges we faced
- accomplishments we are proud of
- what we learned
- what's next for justmoney explorer: graphql server, indexer, and charting

## Body

JustMoney Explorer JustMoney Explorer - https://just.money GraphQL Data Access Token Page - Markets Tab Token Page Enhancements Real-Time transfers scan recognizing each transaction type Pairs Page (New addition) How We Built The GraphQL Server And Blockchain Indexer Charting On JustMoney Explorer Advertising Spaces - Twiskers Banner Favorites List & Labels JustMoney Explorer: GraphQL Server, Indexer, and Charting Introduction We are thrilled to introduce the next evolution of JustMoney Explorer—taking blockchain exploration to new heights with comprehensive, chain-wide data. Our latest addition is a custom GraphQL server and a powerful blockchain indexer that scans every transaction in real time, constructing chart data and trading history for every pair on the TRON blockchain (including Sunswap V3 pools). This enhancement also opens the door to exciting new features such as listing the latest pairs and viewing all pairs ranked by volume, delivering an unparalleled level of insight to our users. Inspiration As we advanced from the beta stage, our primary focus was on fixing bugs, refining the user experience, and adding new features. However, we recognized a major gap in our offering—something our competitors, like Dextools, already provided: comprehensive chain-wide charting data for every token. It wasn't enough for us to only cover a limited scope. We needed to expand to include charting for Sunswap pools and other DEXes to provide complete data coverage across the TRON blockchain. Unlike other platforms, such as Dexscreener, which only scan Sunswap pools and often provide incomplete data, we sought to bring accuracy and integrity to every metric—from total volumes to token pairs and liquidity. This realization was a turning point for us. We knew it was time to take data aggregation into our own hands to provide users with the complete and correct information they deserve. What It Does GraphQL Server and User Interface: Our new GraphQL server and blockchain indexer bring powerful new capabilities: Scanning and Indexing: Transfers: We monitor all token transfers and categorize each one, whether it’s adding liquidity, removing liquidity, a swap (buy/sell), or even an arbitrage trade. Swaps: Our indexer captures every swap transaction, allowing us to build comprehensive swap histories. New Pairs: We track newly created trading pairs, ensuring all new market opportunities are reflected promptly. Charting Data (OHLC Candles): We generate OHLC (Open, High, Low, Close) candles for various timeframes—5M, 15M, 30M, 1H, 4H, 1D, and 1W—providing complete visualization of trading activity for all tokens. Token Page - Markets Tab Querying: GraphQL Data Access: Users can query indexed data using the GraphQL query language, either through an API or the user interface, enabling highly customizable access to exactly the information they need. GraphQL Data Access Explorer (New Functionality): Token Page Enhancements Token Page Enhancements: All Pairs Displayed: Now, all trading pairs from all DEXes are displayed on the token page, complete with DEX logos. Charts for Every Pair: Users can view trading charts for any pair linked to the selected token. Comprehensive Market Tab: The market tab includes all trading pairs of the token, total 24-hour volume across all pairs, and total liquidity. It also displays how much of the liquidity is burned for each pair. Circulating Supply Accuracy: We calculate circulating market cap and total tokens in circulation by determining the number of tokens in blackhole addresses, instead of relying on data from Tronscan. This results in a more accurate representation of supply. Detailed Transfer Information: For each transaction, we display the logos of the DEXes involved, providing clarity for multi-route swaps. Pairs Page (New Addition): Pairs Page Menu Integration: A new "Pairs" page has been added to the menu for easy navigation. Latest Pairs: Users can see the latest pairs deployed on the blockchain. Volume Ranking: Pairs can be viewed and sorted based on their 24-hour trading volume, offering users a deeper market analysis. Favorites List Import/Export & Labels (New addition): Favorites List Import/Export & Labels Now, users can not only add any token or contract address to their favorites list but also import and export that list as a JSON file. This feature allows users to easily back up their favorites or share them across multiple devices. Also the favourites list works now as labels. You can label any address with custom name, making transaction tracking clearer and more intuitive. Instead of seeing a long, complex address in your transaction history, you’ll see the label you’ve assigned. For example, if you label your own wallet as "Me", any transaction involving your wallet will display “[Me]” instead of the raw address. This feature allows for quicker and easier identification of important addresses, simplifying your navigation through transaction lists and providing a more personalized experience. How We Built It Our GraphQL server and blockchain indexer were developed using NodeJS, along with the Apollo GraphQL library to manage efficient data querying and aggregation. This robust backend solution supports real-time indexing and provides users with accurate and immediate blockchain insights. Challenges We Faced One of our biggest challenges emerged during the launch of Sunpump, which caused an immense surge in transaction volume across the network. The high volume led to issues for several explorers, including Tronscan. To overcome this, we focused heavily on optimizing our indexer, allowing it to scan transactions faster than they were being generated. We reached an indexing speed of 40-50 blocks per minute—well above TRON’s block generation rate of 20 blocks per minute—ensuring that JustMoney Explorer remains accurate and up-to-date, regardless of network congestion. Accomplishments We Are Proud Of We are incredibly proud of our optimization achievements. Despite the immense transaction surge during the Sunpump launch, our indexer managed to stay ahead, providing real-time data without falling behind. This accomplishment highlights our team's innovation and our commitment to delivering a high-quality, dependable product, even under challenging conditions. What We Learned Throughout this journey, we deepened our understanding of the GraphQL protocol, as well as the intricacies of blockchain data scanning and aggregation. This knowledge allowed us to create a solution that not only provides fast data access but also offers more efficient and accurate queries for our users. What's next for JustMoney Explorer: GraphQL Server, Indexer, and Charting Charting on JustMoney Explorer For now, our GraphQL server and indexer serve as internal powerhouses driving data for JustMoney Explorer, JM Swap, and other products within the JustMoney Ecosystem. However, we see immense potential to expand this into a commercial service—offering third parties access to our data and charting tools in the future.This commercial opportunity would enhance our current business model, which primarily focuses on the sale of advertising spaces, such as banners. Advertising Spaces - Twiskers Banner We also plan to add more data points to the indexer, which will further enhance the functionalities of our ecosystem’s products, especially JustMoney Explorer. Our vision is to keep pushing the boundaries of what is possible in blockchain data access and to continue serving our community with the most comprehensive, real-time insights available. Smart contract addresses The ones that already deployed earlier https://explorer.just.money/contract/TKf3q4QLWavrhJYMb1TighJ65URWHFU6Gs additionally: https://explorer.just.money/contract/TCoevKLm2jtnChxefbBYysbcMZeAPhWGSf , https://explorer.just.money/contract/TPvyi8d6HnkYbwdstRDjAMYaZ88GYHi57Q <div