---
slug: "chaincrunch"
url: "https://devpost.com/software/chaincrunch"
title: "ChainCrunch"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 914
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/legal_justice"
  - "user/developer"
  - "user/educator_student"
  - "user/government_staff"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# ChainCrunch

> "The" go-to place for on-chain data for Solana.

[Devpost](https://devpost.com/software/chaincrunch) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[legal_justice]]
**user** [[developer]] [[educator_student]] [[government_staff]] [[legal_professional]] [[researcher]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, docker, grafana, javascript, parquet, postgresql, python, rust, s3, sqlite, tsdb

## How they structured the write-up

- motivation
- so far
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chaincrunch

## Body

Motivation Our goal is to be "the" go-to place for on-chain data on the Solana blockchain. We are a team of 3 full-stack engineers with strong big data and data analysis backgrounds thanks to our industry experience in handling projects with millions of users. We believe an infrastructure for indexing historical data and streaming live data can be useful to most Solana users, including investors, developers, traders, government agencies (regulators), and data analysts. Therefore, we set out to crunch this data and expose it to the end-users in the forms of APIs, dashboards, live metrics, and even notebooks to query in SQL/Python arbitrarily. Please feel free to follow us on Twitter or visit chaincrunch.cc to stay up to date with our progress and announcements. So far We have managed to: Provide a historical token balance dashboard and API for all wallets 📈 Balance dashboard We are building our APIs to be extremely performant and we will continue doing so. Through our APIs, teams will be able to access data that is too expensive or simply impossible to obtain through Solana RPC nodes, while not having to worry about the performance of a certain node. Capture live data from 🥭 Mango markets including deposit-borrow APYs, per-token deposits/withdrawals, and balance tracking over time for every single Mango user . All these are directly from on-chain data and the program variables themselves (not web-scraping). They are exposed through Grafana. Mango dashboard Develop our own validator plugin to keep track of Serum's event queue in order to collect perfect order-book data. Our validator nodes 🖧 are running the plugin and we will soon make the data available to Serum project. Publish high-level dashboards on Solana ecosystem. These dashboards visualize the activity of various programs and tokens 🪙 on a daily basis. Token overview dashboard Whale 🐋 dashboard tracking large token transfers. Largest transactions dashboard How we built it Thanks to our previous experiences in building data pipelines we chose a scalable architecture that has served us very well during the past month. For analyzing historical data we are using Apache Spark as the processing engine along with Apache Parquet as the storage format. We use this cluster to backfill our live indices for our real-time APIs as well. For storing account specific metrics through time, we are using a time-series database to automatically optimize storage efficiency based on data resolution. Apart from using them in APIs, we use Grafana for visualizing them. We developed online crawlers that fetch the blocks as soon as they are finalized and store them for historical processing as well as live APIs. We use spark streaming for compression of the new data on the fly. We also developed various decoding tools for understanding the binary data of different programs transactions like Mango, NFTs, etc. Challenges we ran into Our main challenge is the sheer scale of data and how to keep up with the speed of transactions. Around 300GB per day is just the uncompressed version of the transaction data. The account (state) data is at a whole other level, especially for Serum which produces 8 GB of data PER MINUTE! However, we are genuinely enjoying the challenge. Accomplishments that we're proud of We are the first group on Solana to report historical token and Solana balances. Other UIs are abusing RPC nodes to extract data that these nodes are not designed to give. We received a lot of attention especially from the Kin community on this matter. We are also proud to have received the Eco-Serum grant. We are firm believers in DeFi. Our goal is to make sure that it succeeds and it is a pleasure to help them keep track of their open orders, event queue, and order book. We are using this grant towards making Serum-specific API calls much more efficient. Our projects caught the attention of many well-known projects in the Solana ecosystem and we are in contact with them in order to provide better APIs and data feeds. We're collaborating with Serum, Mango, Step finance, Solana-floor, and ... at the moment. What we learned That there is always more data to process. What's next for ChainCrunch For us, this started as a side-project. After around a week, we saw huge interest in our project from the community. Therefore, we found ourselves collaborating and working late into the night 🌙 or early in the morning. We have managed to build all of these features in just one month. We believe that there is still a lot left to do for ChainCrunch. ⛓️ Our priority is to make sure our data lakes and computation platforms are scalable and the APIs that we are providing to our current users continue to work well. We are trying to squeeze in the more recent data/API requests from other groups in our schedule.😎 We have other full-time obligations. One person will soon join Google Zurich, another is a PhD student in ML and the third works in encryption. As ours systems at ChainCrunch grow, we find it inevitable to quit these activities and devote our time to ChainCrunch full-time. 🕒 Fortunately, the community has found our solutions useful. Multiple groups have reached out to us to express their interest in our services and we are working on providing APIs to them. We are in contact with VC firms and also lawyers for the path forward. We are still debating whether to choose to become a DAO or a corporate company. 🚀## Inspiration <div