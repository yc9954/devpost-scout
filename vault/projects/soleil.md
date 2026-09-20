---
slug: "soleil"
url: "https://devpost.com/software/soleil"
title: "Soleil"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 926
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Soleil

> A way to incentivise both growths of the entire solar industry with one transaction and of a decentralised off-chain public feed of solar energy production data for all to use

[Devpost](https://devpost.com/software/soleil) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]

**stack** ceramic, chainlink, google-cloud, moralis, open-zeppelin, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for soleil ☀
- thanks

## Body

Architecture diagram User's dashboard page Landing page GIF GIF of user registering their site GIF GIF of user submitting a DAI schedule to the contract GIF GIF of user claiming earned SLL token rewards Inspiration Smart contracts have a lot of potential to greatly improve the transparency and efficiency of the funding of public goods. I had the idea that any data feed that we bootstrap which can be interpreted to obtain the relative effort/performance of entities towards achieving a common public good can allow smart contracts to provide an extremely efficient method of distributing funds to the entities to incentivise their progress. In turn, the respective data feed grows larger and larger as more entities are incentivised to provide their data to it. I had recently done a job for a friend which involved working with a solar monitoring API. I realised that the data returned by these monitoring APIs would make a great fit for this model. What it does Soleil (the French word for "sun", pronounced /sɔlɛj/, like "soh-lay") is a prototype of the above idea around the solar industry. It aims to fight climate change by providing a way to incentivise growth in the entire solar industry with a single transaction. Solar energy producers are paid in stablecoins and project funders are rewarded with native SLL tokens based on the amount of energy produced by registered sites. The more DAI paid in, the more sites are incentivised to join the data feed - the more sites joining the data feed, the more SLL are minted daily. Therefore the solar energy production data feed grows larger and (with enough decentralisation of data sources and aggregators) can be used as a source of truth for this data by any other project. Uses for the SLL token can be created by other projects as a way of fighting climate change by supporting the Soleil project. How we built it Solar sites can register through the web app by submitting their monitoring API credentials. The web app is connected to a Moralis server and a custom Moralis cloud function verifies the API credentials against the respective monitoring API before it stores them in the database. Users can submit DAI distribution schedules through the web app to the pool manager smart contract. External adapters connect between Ceramic data streams, the monitoring APIs, the Moralis database and the pool manager smart contract to facilitate the updating of three Ceramic data streams: Energy production data stream DAI earnings data stream SLL rewards data stream The external adapters are triggered hourly by Cron Chainlink jobs. To manage the potential distribution of DAI to thousands of solar sites and of SLL to thousands of funders, we have implemented a 'cumulative merkle drop' solution where a Chainlink node calculates the earnings for each token, publishes the data in a public Ceramic data stream and then only submits the merkle root of this data back on-chain. At any time, users are able to submit a merkle proof to claim (in full or partially) their earnings from the contract. The web app displays a number of stats on the state of the protocol. The aggregated energy production stats come from a Moralis database table which is populated by a scheduled Moralis cloud job that calculates aggregates of data from the energy production Ceramic data stream. Challenges we ran into Initial drafts of the earnings calculator external adapters made a lot of calls to our RPC node (with increasing offsets applied to each to avoid all the requests hitting at once), which understandably sometimes meant that the Chainlink node gave up waiting for a response! To fix this we learned about multicall functionality from one of Patrick Collins' video tutorials and added it to the adapters. Now this isn't a problem at all 🥳 Accomplishments that we're proud of Particularly proud of both the use of Ceramic in our solution and of the cumulative merkle drops implementation. I think Ceramic and a Chainlink DON can work extremely well together to allow the creation of off-chain sources of truth which are very useful for certain use cases. What we learned Learned about: Ceramic data streams - the documentation was great for this Moralis cloud functions and scheduled jobs - very impressed with how well these worked! The new Chainlink TOML job specs - again found these very developer friendly and powerful; a definite improvement on the JSON job specs Merkle trees Multicall Writing and testing contracts with hardhat What's next for Soleil ☀ Taking this project further we would love to improve the decentralisation of the solution, both in terms of the number of data sources (comparing monitoring API data with satellite imaging data and/or weather data for example) and in terms of the number of Chainlink nodes collaborating on the maintenance of the data feeds. Currently only the SolarEdge monitoring API is supported so we would look to improve this to support a wider range of monitoring API providers. Once ready and on a live network we could also make contact with the providers and strike up some deals to help spread awareness of the project to solar panel owners. Bootstrapping the project with enough funders and enough registered solar sites may be a challenge but beyond that, it would hopefully grow quite organically. Thanks Huge thank you to the Chainlink team and all the sponsors for making this hackathon happen. A special thank you to Linkpool for allowing a free trial use of their node-as-a-service product for the duration of the hackathon 🙏 <div