---
slug: "wynd"
url: "https://devpost.com/software/wynd"
title: "Wynd"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 1108
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/climate_energy"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Wynd

> We connect complex environmental data to the blockchain. Enabling us to leverage DeFi protocols to protect the environment.

[Devpost](https://devpost.com/software/wynd) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[climate_energy]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** cosmjs, cosmwasm, deckgl, juno, keplr, mapbox, pandas, python, react, rust

## How they structured the write-up

- data sources
- hexagons ⬡
- frontend app
- contracts
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wynd

## Body

Wynd is an example of an environmental DeFi app with the goal of channeling the DeFi funding towards environmental goods. We had discussed many ideas related to tracking deforestation/reforestation, and those would be wonderful projects to bring to production, but given the time constraints of the hackathon, we decided on a metric that changed much more quickly... Air Quality. The goal is to make visible the invisible - in this case air pollution - and allow people to profit when they can reduce it. An investor can place WYND tokens on a given area and then work/lobby/tweet to improve the air quality. Several months later, when the investment is mature, we compare the new air quality with the original quality and reward the investor with a return based on the change. If the pollution levels decrease, they get more WYND back. If pollution increases, they lose WYND (do not get all their initial investment back). For the prototype, we have a quite short investment duration (2 days) just to serve as a quick to use demo, but any real system should configure this for several months and use a time-averaged value to encourage long-term improvements Data Sources For the original data, we use Emissions API , which is based on public domain ESA (European Space Agency) satellite data. We poll the data for the last several months for the US, and then combine it into a standard grid, so nearby measurements are grouped together. The first product is measuring Carbon Monoxide, which is a toxic pollutant. Further work would be to normalize the data to remove some of the noise/variation. This could be done by averaging, but also we would like to investigate if there is a high correlation between wind/rain and pollution levels (high wind or rain removing atmospheric pollution) and if so, we could compensate for this correlation by reading in historical weather information and processing the data from Emissions API, before we perform some time averaging on it. Once we have "clean data" for one metric, we would like to add the other frequently updated pollution sources (methane and ozone), preprocess them as above, and then combine them to produce a combine WYND index that represents a more holistic view of air quality. We chose one country to limit the scale of the data we work with. And chose the USA, as it is the most widely recognized country. (We also considered Europe, but that would involve 30+ different API calls, so we started with the simpler one). Hexagons ⬡ Since every measurement is at a slightly different location, we need to group them together in a reasonable spatial resolution to allow meaningful aggregation and historical data. To do so, we searched for a regular grid system that covers the planet and went with the H3 Hexagonal Hierarchical Spatial Index . This can easily be adjusted to different spatial resolutions and covers the whole globe with mostly-equally sized hexagons in contrast to e.g. the distortion of squares in the Mercator projection. Frontend App The frontend app provides the user access to both the data platform and the blockchain. It queries the latest values of all grid points from the data platform, and when you click on a hexagon, it will also show a graph of the historical values of pollution. It also uses Keplr and connects to Juno's Uni testnet. We deployed a faucet API server to give out 10 JUNOX to each new user, so they can pay gas. And then use a smart contract faucet to release 10.000 WYND to each user once, to allow them to invest in the protocol, allowing a quick and easy onboarding experience for the prototype. Once you have connected your wallet and filled it with tokens, you can browse the different hexagons and invest in the one(s) that you would like to clean up. We display all your current investments in the sidebar, and also allow you to withdraw any investments that have reached maturity, calculating your winnings. Contracts We use CosmWasm contracts to handle the blockchain side. The main contract you interact with is the wynd-invest contract. You can view the API here . But the main actions are "invest", "withdraw" and "store_oracle". Queries will show detailed info for one hex, or list all investments for one user. The implementation of the oracle is quite simple for now. The first version allows a privileges user to submit the data directly. We work on an oracle contract which verifies data from multiple sources before submitting. Challenges we ran into It took some research to find a good data source with a usable API. After finding emissions-api, which provides great access to high level data, we had issues of inconsistent coverage (some places were measured daily, others weekly). We solved most of this by grouping data points into large-enough hexagons to capture a data point every 1-2 days for most regions. Deciding on the R3 grid system was a nice design to display and to avoid the issues with the mercator projection. We still have issues in normalising the data and smoothing out the peaks, but that is for future work. Once this data was provided, grouped and available to the frontend via API, we had to bring it on chain. It is expensive to place so much data at once and we end up paying 3-4 million gas to submit a daily update to the chain (for all the hexagons). We added some filtering to reduce the amount of unused data, and tried to limit the format to make it a bit smaller, but it is still quite the data flow, even at this resolution. Integrating all the libraries for mapping and data visualisation, as well as CosmJS and Keplr was a great achievement. And dealing with some breaking signatures in Keplr due to the Uni testnet upgrade, that left us confused for several hours (this code worked fine yesterday). Accomplishments that we're proud of A UI integrating maps, real data feeds, and blockchain interactions. Designing an API for data feeds. Oracle to put complex environmental data onto smart contracts What we learned That it was fun to work together, and we can combine all these different aspects in one fluid UI. What's next for Wynd Depends who wants to sponsor it. As mentioned in the video, we would love to improve the quality of the data platform, build out stronger oracles, and design more attractive tokenomics for the DeFi aspects. After this, we would love to deploy this in multiple domains - Earth, Water, Air - and connect it to real world actions. Who's in? <div