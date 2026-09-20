---
slug: "solanafloor"
url: "https://devpost.com/software/solanafloor"
title: "SolanaFloor"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 555
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# SolanaFloor

> Solana NFT data analysis platform with on-chain information about token distribution, price development and NFT data. This project provides valuable information for NFT holders and those interested.

[Devpost](https://devpost.com/software/solanafloor) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**substrate** [[financial_record]] [[structured_db]]

**stack** express.js, javascript, mongodb, netlify, nuxtjs, solana, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for solanafloor

## Body

Main dashboard per project List of projects/collections Floor insights (floor analysis per attribute) NFT Portfolio tracker Listed NFT's for sale overview All tokens and their attrributes NFT holders overview NFT rarities/attributes More dashboard data Daily unique users growth Daily page views growth and duration on site Inspiration Got into crypto in 2017. Heard about NFT's in 2020, but bought my first NFT a couple of weeks ago. Which was a SMB NFT on Solana during the initial mint. Got really invested in the whole scene and joined the MonkeDAO discord soon after. The whole NFT scene is still so young and more so on Solana. I missed some valuable data to have better insights into NFTs on Solana, so I built SolanaFloor. I started building it early-mid September next to my day job. Most people were enthusiastic about it, so I'm slowly adding features and improving performance. What it does SolanaFloor shows information about the tokens itself, the listing prices, current owners, rarities and rankings. How the distribution is and price development. The web app is pretty interactive, so visitors can sort and filter data for themselves. How I built it I made the frontend in NuxtJS (VueJS) using TypeScript. The backend is built in JavaScript. The app is statically hosted on Netlify. The backend uses the @solana/web3.js package to fetch on-chain data about the tokens and transactions. I also scrape several markets to find all the listings and put them into a MongoDB database. The API is built on ExpressJS. Challenges I ran into I didn't know much about Solana and blockchain development. So it was a lot of trial and error to get the correct data without using too many requests. I had help from people in the community and @MonkeDAO specifically that pointed me to possible solutions to my problems, but pretty much built everything on my own. I also spent some time on the decoding part, since there isn't much documentation on @solana/web3.js. And as SolanaFloor gained more publicity there were more visitors. And with so much data it was difficult to have proper performance. Some pages were taking almost a minute to load or would just crash. So I migrated the whole API and DB in a couple of days from cloud db and lambda to a dedicated app + db. Load times are blazing fast now. Accomplishments that I'm proud of Successfully querying the blockchain for the correct data and processing them into useful visualisations. The overall acceptance of the project in the community has been amazing and all the projects that want to get listed on my site. Even Anatoly talked about it, which I'm exceptionally proud of: https://twitter.com/aeyakovenko/status/1446883293194903552 And obviously how SolanaFloor is used. I went from 0 to 30k page views per day and 3k unique visitors per day in just 4 weeks time. The average time visitors spend on my site is 2:50 min, which I think is pretty good. What I learned How awesome it is to build using Solana. It's fast and cheap. What's next for SolanaFloor Keep adding features and other NFT projects. Features like improved portfolio tracking, realtime data, APIs, more filter/search possibilities, add volume and transactional data. But since I'm doing this by myself in my free time, it might not go as fast as I'd like it to. <div