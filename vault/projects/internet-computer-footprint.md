---
slug: "internet-computer-footprint"
url: "https://devpost.com/software/internet-computer-footprint"
title: "Internet Computer Footprint"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 979
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/video_visual"
---

# Internet Computer Footprint

> Internet Computer Footprint tracks the cycle burn rate of IC projects, and uses VERRA carbon credits to offset project emissions

[Devpost](https://devpost.com/software/internet-computer-footprint) · hackathon [[Supernova]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[finance_payments]]
**substrate** [[code_repository]] [[geospatial]] [[regulation_legal_text]] [[video_visual]]

**stack** ic, javascript, motoko, react, verra

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for internet computer footprint
- get in touch

## Body

Inspiration Any idea that wants to play a positive role in defining the future must take into account the health of our planet. We want the IC footprint to help represent, protect and regenerate the planet as the IC shapes it. We started the IC footprint to support the IC move towards a more environmentally conscious future. In our mind, a prerequisite for making the IC a force for good in the world is to ensure that we develop it in a way that considers its impact on the planet. We see IC footprint as the first step in a journey to harness the unique capabilities of the IC to help tackle climate change. What it does IC footprint uses verified carbon credits to offset IC projects on-chain. We have developed a methodology to calculate the entire emissions of the IC and then, using cycles, determine the carbon emissions of specific projects operating on the IC and provide a route to account for those emissions. “Carbon credits are measurable, verifiable emission reductions from certified climate action projects. These projects reduce, remove or avoid greenhouse gas (GHG) emissions. But they also bring a whole host of other positive benefits, for example, they empower communities, protect ecosystems, restore forests or reduce reliance on fossil fuels.” - South Pole - 2022 We have developed a methodology to calculate the entire emissions of the IC and then, using cycles, can determine the carbon emissions of specific projects operating on the IC. Once the carbon footprint of a project is calculated, it can be offset using nature-based carbon credits from VERRA. These are credits with a high-degree of additionality, meaning without the funding provided through credit sales, that specific climate project would not have been feasible. A dynamic ICF token is minted to keep track of the carbon neutrality status of canisters. The token will include all the information necessary for the project to prove their climate commitment. In the short term, the aim of IC footprint is to build a trustless measurement mechanism which can automatically calculate carbon emissions from canisters, and then offset those emissions using high-grade carbon credits. Longer term, we see a path to use near real-time emission data to adapt the network and allow it to reduce its carbon-intensity. How we built it Click here for in depth architecture of our project. The below image gives the canister architecture for phase II of IC footprint. The front end that we demo sits on top of this canister architecture. Note: the below architecture outlines the end-goal of phase II, and certain aspects are still in development The methodology used by IC Footprint is essentially the algorithm we have developed to calculate the carbon emissions of the IC at large and for individual projects operating within it. It’s important to note this is an iterative process, and the quality of the output is directly tied to the quality and robustness of the data which we use as an input. This is why it’s best to view this as a dynamic methodology developed to drive improvement, with clearly stated assumptions that are open to testing and examination. We hope to work with Dfinity directly to improve this coefficient over time. Challenges we ran into Developing an end-to-end trustless mechanism for IC footprint has certain complexities. Cycle measurement on the IC is not straightforward and requires architecture to ensure we can reliably measure a project’s canister cycles without compromising canister security. Further trust is required in a project’s reporting of canisters, with no clear way to ensure we are indeed taking into account all a project’s canisters. In the Voluntary carbon market, all emissions are reported voluntary (clue is in the name), but the IC gives the possibility of going one step further, towards a fully trustles system. Calculating an emissions coefficient that can accurately measure the carbon footprint of a single cycle remains a challenge. Instead, what we have developed should be viewed as a framework, and we want to work with the IC community, and Dfinity to evolve and improve our coefficient over time. Our discord channel #icfootprint-coefficient, currently serves as a forum for discussion on this topic, and we encourage anyone who has done work in this area already, or would like to participate to reach out. Due to changes in VERRA’s regulation, we cannot move the credits they have created on-chain, so they can be directly consumed. In the future, VERRA plans to allow for on-chain assets, which will open the door to move our end-to-end process on chain. Accomplishments that we're proud of Receiving a VERRA licence in order to receive, transfer and retire carbon credits. Making our first purchase of 500 tonnes of Verra accredited Verified Carbon United (VCS) Selling out our round on Crowdfund NFT in under five minutes. Giving us confidence the IC community is rallying behind our projects. Our technical roadmap - we’re excited we have come up with practical ways to leverage the ICs capabilities to start making the network more green. What's next for Internet Computer Footprint Phase 1 (complete) Tech roadmap VERRA licence Project roadmap purchase high-quality credits retire carbon credits 1 tonne retired - @Dfinity 1 tonne retired - @dominic_w Phase 2 (Supernova) Tech roadmap automatically measure cycle burn rate over time derive carbon footprint from cycle burn-rate prove with dynamic, soulbound NFT Project roadmap Serve and offset 75 golden ticket holders Phase 3 Tech roadmap expose real-time carbon intensity data of network develop smart node allocation, based on data centre energy mix consumption implement computation timing decisions for canister managers, based on network carbon intensity Project roadmap ICF is standard for carbon measurement and offsetting Get in touch Interested in our projects, want to get involved, or just want to join the conversation? Join us on the Carbon Crowd discord, or follow us on twitter @icfootprint and @carboncrowd__io <div